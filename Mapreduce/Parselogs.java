import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

class Parselogs //Parselogs这个类用来对字符串进行解析
{
    public String[]  parseString(String str) throws ParseException
    {
//        byte[] bs = str.getBytes();
//        String ustr = bs.toString();
        String[] strs = str.split("\t");//在这里只获取与本次项目有关的数据
        return strs;
    }
//    public String parseIp(String str)//对ip地址进行解析的方法
//    {
//        String[] splited = str.split(" - - ");//用指定的正则表达式进行切分，获取我们需要的字段
//        return splited[0];
//    }
//    public String parseDate(String str) throws ParseException
//    {
//        String[] splited = str.split(" - - ");//用指定的正则表达式进行切分，获取我们需要的字段
//        int index1 = splited[1].indexOf("[");
//        int index2 = splited[1].indexOf("]");
//        String substring = splited[1].substring(index1+1, index2);//到此获取了时间字段30/May/2013:17:38:20 +0800
//        SimpleDateFormat simple1 = new SimpleDateFormat("dd/MMM/yyyy:HH:mm:ss", Locale.ENGLISH);//匹配我们给定的字符串，并将其解析成对应的时间
//        SimpleDateFormat simple2 = new SimpleDateFormat("yyyyMMddHHmmss");//匹配我们给定的字符串
//        Date parse = simple1.parse(substring);
//        String format = simple2.format(parse);
//        return format;
//    }
//    public String parseUrl(String str)//获取访问的url
//    {
//        int index1 = str.indexOf("]");
//        int index2= str.lastIndexOf("\"");
//        String substring = str.substring(index1+3, index2);
//        return substring;
//    }
//    public String parseStatus(String str)//获取访问的状态
//    {
//        int index1= str.lastIndexOf("\"");
//        String str2 = str.substring(index1+1).trim();
//        String[] splited = str2.split(" ");
//        return splited[0];
//    }
//    public String parseFlow(String str)//获取访问的状态
//    {
//        int index1= str.lastIndexOf("\"");
//        String str2 = str.substring(index1+1).trim();
//        String[] splited = str2.split(" ");
//        return splited[1];
//    }
}