import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.mapreduce.lib.partition.HashPartitioner;
;

//本程序的目的是通过MapReduce对日志数据进行清洗时
public class LogCleaner
{
    public static String path1="/data/electric.log";//指定文件的输入路径
    public static String path2="/data/electric";//指定日志的输出路径
    public static void main(String[] args) throws Exception
    {
        Configuration conf = new Configuration();
        conf.set("fs.defaultFS", "hdfs://hadoop1:9000/");
        FileSystem fileSystem = FileSystem.get(conf);
        if(fileSystem.exists(new Path(path2)))
        {
            fileSystem.delete(new Path(path2), true);
        }
        Job job = Job.getInstance(conf, "LogCleaner");
        job.setJarByClass(LogCleaner.class);//jar包
        //编写驱动
        FileInputFormat.setInputPaths(job, new Path(path1));
        job.setInputFormatClass(TextInputFormat.class);
        job.setMapperClass(MyMapper.class);
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(NullWritable.class);
        job.setNumReduceTasks(1);//指定Reducer的任务数量为1
        job.setPartitionerClass(HashPartitioner.class);
        job.setReducerClass(MyReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(NullWritable.class);
        FileOutputFormat.setOutputPath(job, new Path(path2));
        job.setOutputFormatClass(TextOutputFormat.class);

        //提交任务
        job.waitForCompletion(true);
    }
    public static class MyMapper extends Mapper<LongWritable, Text, Text, NullWritable>
    {
        protected void map(LongWritable k1, Text v1,Context context)throws IOException, InterruptedException
        {
            String string = v1.toString();//获取待记录
            Parselogs parselogs = new Parselogs();
            try
            {
                String[] sub = parselogs.parseString(string);
                if(sub.length<3)
                    return;
                String temp = sub[3];
                if(temp.contains("无"))
                    return;
//                sub[6]=sub[6].substring(0,sub[6].indexOf(".")+3);
//                sub[7]=sub[7].substring(0,sub[7].indexOf(".")+3);
                if(temp.contains("万")){
                    int index = temp.indexOf("万");
                    String salary = temp.substring(0,index);
                    String[] ss = salary.split("-");
                    if(ss.length<2){
                        Double d1 = Double.parseDouble(ss[0]);
                        d1 = d1 * 10.0;
                        if (temp.contains("年")) {
                            d1 = d1 / 12.0;
                        }
                        String s1 = String.format("%.1f",d1);
                        sub[3] = s1;
                    }
                    else {
                        Double d2 = Double.parseDouble(ss[1]);
                        d2 = d2 * 10.0;
                        if (temp.contains("年")) {
                            d2 = d2 / 12.0;
                        }
                        String s2 = String.format("%.1f",d2);
                        sub[3] = s2;
                    }
                }
                else if(temp.contains("千")){
                    int index = temp.indexOf("千");
                    String salary = temp.substring(0,index);
                    String[] ss = salary.split("-");
                    if(ss.length<2){
                        Double d1 = Double.parseDouble(ss[0]);
                        if (temp.contains("年")) {
                            d1 = d1 / 12.0;
                        }
                        String s1 = String.format("%.1f",d1);
                        sub[3]=s1;
                    }
                    else {
                        Double d2 = Double.parseDouble(ss[1]);
                        if (temp.contains("年")) {
                            d2 = d2 / 12.0;
                        }
                        String s2 = String.format("%.1f", d2);
                        sub[3] = s2;
                    }
                }else if(temp.contains("元")){
                    int index = temp.indexOf("元");
                    String salary = temp.substring(0,index);
                    Double d = Double.parseDouble(salary);
                    d = 1.0*d*30/1000.0;
                    String s1 = String.format("%.1f",d);
                    sub[3]=s1;
                }
                Text k2 = new Text();
                byte[] bs = (sub[0]+"\t"+sub[1]+"\t"+sub[2]+"\t"+sub[3]+"\t"+sub[4]+"\t"+sub[5]).getBytes();
                k2.set(bs);//三个字段之间以制表符进行分开
                context.write(k2, NullWritable.get());
            }

            catch (ParseException e)
            {
                e.printStackTrace();
            }
        }
    }
    public static class MyReducer extends Reducer<Text, NullWritable, Text, NullWritable>
    {
        protected void reduce(Text k2, Iterable<NullWritable> v2s,Context context)throws IOException, InterruptedException
        {
            for (NullWritable v2 : v2s)
            {
                Text k3 = k2;
                context.write(k3, NullWritable.get());
            }
        }
    }
}

