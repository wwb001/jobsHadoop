from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse,render
import json
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.http import JsonResponse
from django.core import serializers
import pymysql

db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': '123456',
    'db':'jobs' #这里需要改成你的数据库名
}
con = pymysql.connect(**db_config)

def login(request):
    """
    处理用户请求并返回内容
    """
    # return HttpResponse('login')
    return render(request,'login.html')

def dSalaryPart(request):
    return render(request,'3dSalaryPart.html')

def guoneixuqiu(request):
    return render(request,'guoneixuqiu.html')

def gangweizongxuqiu(request):
    return render(request,'gangweizongxuqiu.html')

def gangweipingjunxinzi(request):
    return render(request,'gangweipingjunxinzi.html')

def shengpingjunxinzi(request):
    return render(request,'shengpingjunxinzi.html')

def zhaopingaopinci(request):
    return render(request,'zhaopingaopinci.html')

def main(request):
    return render(request,'main.html')

def TestServlet(request):
    datas = [
        {
            "name": "手机",
            "num":"5"
        },
        {
            "name": "电脑",
            "num":"9"
        },
        {
            "name": "冰箱",
            "num":"8"
        }
    ]
    return JsonResponse(datas,safe=False,json_dumps_params={'ensure_ascii':False})

def getMapMessage(request):
    '''
    * 返回地图信息的接口
    * 关于AI人工智能职位的地理信息
    * 以{"position":{"北京市":["经度,纬度"]},"value":[{"北京市"："20"},{""：""}]} 格式返回
    '''
    result = {
        "value":[]
    }
    con.ping(reconnect=True)#固有写法
    cu = con.cursor(cursor=pymysql.cursors.DictCursor)
    cu.execute('select distinct(province) from ai_table')
    message = cu.fetchall()
    cu.close()
    position={}
    for i in range(0, len(message)):
        province = message[i]['province']
        entity = {province: []}  #存 {"北京市":总数量}
        #查latitude,longitude
        cu1 = con.cursor(cursor=pymysql.cursors.DictCursor)
        cu1.execute("select latitude,longitude from ai_table WHERE province='" + str(province) + "'")
        locationMessage = cu1.fetchall()
        cu1.close()
        locations=[]
        locations.append(locationMessage[0]['latitude'])
        locations.append(locationMessage[0]['longitude'])
        position[str(province)]=locations
        cu2=con.cursor(cursor=pymysql.cursors.DictCursor)
        cu2.execute("SELECT count(*) from ai_table where province='" + str(province) + "'")
        num = cu2.fetchall()
        cu2.close()
        # print("num"+str(num))
        entity[province]=str(num[0]['count(*)'])
        result['value'].append(entity)
    result['position']=position
    return JsonResponse(result,safe=False,json_dumps_params={'ensure_ascii':False})

def getCityNum(request):
    '''
    * 返回人工智能岗位每个城市的职位数量
    * 返回 {"data":[{"city":"北京市","value":"1234"},{"city":"天津市","value":"4321"}]}
    '''
    result = {
        "data":[]
    }
    con.ping(reconnect=True)  #固有写法
    #查询所有的城市
    cu = con.cursor(cursor=pymysql.cursors.DictCursor)
    cu.execute('select distinct(province) from ai_table')
    message = cu.fetchall()
    cu.close()
    for i in range(0, len(message)):
        province = message[i]['province']
        entity = {}
        entity['city'] = province
        cu=con.cursor(cursor=pymysql.cursors.DictCursor)
        cu.execute("SELECT count(*) from ai_table where province='" + str(province) + "'")
        num = cu.fetchall()
        cu.close()
        entity['value'] = str(num[0]['count(*)'])
        result['data'].append(entity)
    return JsonResponse(result,safe=False,json_dumps_params={'ensure_ascii':False})

def getValue(request):
    '''
    * 返回每个城市的职位数量
    * 返回格式
    * {"value1":{"北京市":"100","天津市","200"},value2":{"北京市":"100","天津市","200"}}
    '''
    result = {}
    con.ping(reconnect=True)  #固有写法

    #获取AI所有城市
    cu = con.cursor(cursor=pymysql.cursors.DictCursor)
    cu.execute('select distinct(province) from ai_table')
    message = cu.fetchall()
    value1={}#{"北京市":"12","天津市":"11"}
    for i in range(0, len(message)):
        province = message[i]['province']
        #查对应城市的数量
        cu.execute("SELECT count(*) from ai_table where province='" + str(province) + "'")
        num = cu.fetchall()
        value1[province]=str(num[0]['count(*)'])
    result['value1'] = value1

    #获取前端开发所有城市
    cu.execute('select distinct(province) from foreend_table')
    message = cu.fetchall()
    value2={}#{"北京市":"12","天津市":"11"}
    for i in range(0, len(message)):
        province = message[i]['province']
        #查对应城市的数量
        cu.execute("SELECT count(*) from foreend_table where province='" + str(province) + "'")
        num = cu.fetchall()
        value2[province]=str(num[0]['count(*)'])
    result['value2'] = value2

    #获取游戏开发所有城市
    cu.execute('select distinct(province) from game_table')
    message = cu.fetchall()
    value3={}#{"北京市":"12","天津市":"11"}
    for i in range(0, len(message)):
        province = message[i]['province']
        #查对应城市的数量
        cu.execute("SELECT count(*) from game_table where province='" + str(province) + "'")
        num = cu.fetchall()
        value3[province]=str(num[0]['count(*)'])
    result['value3'] = value3

    #获取移动开发所有城市
    cu.execute('select distinct(province) from mobile_table')
    message = cu.fetchall()
    value4={}#{"北京市":"12","天津市":"11"}
    for i in range(0, len(message)):
        province = message[i]['province']
        #查对应城市的数量
        cu.execute("SELECT count(*) from mobile_table where province='" + str(province) + "'")
        num = cu.fetchall()
        value4[province]=str(num[0]['count(*)'])
    result['value4'] = value4

    #获取测试岗位所有城市
    cu.execute('select distinct(province) from test_table')
    message = cu.fetchall()
    value5={}#{"北京市":"12","天津市":"11"}
    for i in range(0, len(message)):
        province = message[i]['province']
        #查对应城市的数量
        cu.execute("SELECT count(*) from test_table where province='" + str(province) + "'")
        num = cu.fetchall()
        value5[province]=str(num[0]['count(*)'])
    result['value5'] = value5
    cu.close()
    return JsonResponse(result,safe=False,json_dumps_params={'ensure_ascii':False})

def getNeedNum(request):
    '''
    * 返回各个岗位的需求
    * 格式：
    {
        "job":["岗位1","岗位2"],
        "pie":[
            {
                "value":"5",
                "name":"岗位1",
                "itemstyle":{"color":"#c1232B"}
            },
            {
                "value":"5",
                "name":"岗位1",
                "itemstyle":{"color":"#c1232B"}
            }
        ],
        "data":["5","20"]
    }
    '''
    result = {
        "job": ['人工智能','后端开发','数据','设计','前端开发','游戏开发','运维技术支持','移动开发','产品','运营','测试'],
        "pie": [],
        "data":[]
    }
    #数据库连接
    con.ping(reconnect=True)  #固有写法
    cu = con.cursor(cursor=pymysql.cursors.DictCursor)
    #查询人工智能数量
    entity = {}
    cu.execute('select count(*) from ai_table')
    num = cu.fetchall()
    entity['value'] = str(num[0]['count(*)']*2)
    entity['name'] = '人工智能'
    entity['itemstyle'] = {'color':'#1D9DFF'}
    result['pie'].append(entity.copy())
    result['data'].append(str(num[0]['count(*)']*2))
    #查询后端开发数量
    cu.execute('select count(*) from backend_table')
    num = cu.fetchall()
    entity['value'] = str(num[0]['count(*)'])
    entity['name'] = '后端开发'
    entity['itemstyle'] = {'color':'#32C519'}
    result['pie'].append(entity.copy())
    result['data'].append(str(num[0]['count(*)']*2))
    #查询数据数量
    cu.execute('select count(*) from data_table')
    num = cu.fetchall()
    entity['value'] = str(num[0]['count(*)']*2)
    entity['name'] = '数据'
    entity['itemstyle'] = {'color':'#9FE6B8'}
    result['pie'].append(entity.copy())
    result['data'].append(str(num[0]['count(*)']*2))
    #查询设计数量
    cu.execute('select count(*) from design_table')
    num = cu.fetchall()
    entity['value'] = str(num[0]['count(*)']*2)
    entity['name'] = '设计'
    entity['itemstyle'] = {'color':'#0096FF'}
    result['pie'].append(entity.copy())
    result['data'].append(str(num[0]['count(*)']*2))
    #查询前端开发数量
    cu.execute('select count(*) from foreend_table')
    num = cu.fetchall()
    entity['value'] = str(num[0]['count(*)']*2)
    entity['name'] = '前端开发'
    entity['itemstyle'] = {'color':'#FF9F7F'}
    result['pie'].append(entity.copy())
    result['data'].append(str(num[0]['count(*)']*2))
    #查询游戏开发数量
    cu.execute('select count(*) from game_table')
    num = cu.fetchall()
    entity['value'] = str(num[0]['count(*)']*2)
    entity['name'] = '游戏开发'
    entity['itemstyle'] = {'color':'#ED8884'}
    result['pie'].append(entity.copy())
    result['data'].append(str(num[0]['count(*)']*2))
    #查询运维技术支持数量
    cu.execute('select count(*) from maintain_table')
    num = cu.fetchall()
    entity['value'] = str(num[0]['count(*)']*2)
    entity['name'] = '运维技术支持'
    entity['itemstyle'] = {'color':'#60CDA0'}
    result['pie'].append(entity.copy())
    result['data'].append(str(num[0]['count(*)']*2))
    #查询移动开发数量
    cu.execute('select count(*) from mobile_table')
    num = cu.fetchall()
    entity['value'] = str(num[0]['count(*)']*2)
    entity['name'] = '移动开发'
    entity['itemstyle'] = {'color':'#FF0000'}
    result['pie'].append(entity.copy())
    result['data'].append(str(num[0]['count(*)']*2))
    #查询产品数量
    cu.execute('select count(*) from product_table')
    num = cu.fetchall()
    entity['value'] = str(num[0]['count(*)']*2)
    entity['name'] = '产品'
    entity['itemstyle'] = {'color':'#FFFF00'}
    result['pie'].append(entity.copy())
    result['data'].append(str(num[0]['count(*)']*2))
    #查询运营数量
    cu.execute('select count(*) from run_table')
    num = cu.fetchall()
    entity['value'] = str(num[0]['count(*)']*2)
    entity['name'] = '运营'
    entity['itemstyle'] = {'color':'#666633'}
    result['pie'].append(entity.copy())
    result['data'].append(str(num[0]['count(*)']*2))
    #查询测试数量
    cu.execute('select count(*) from test_table')
    num = cu.fetchall()
    entity['value'] = str(num[0]['count(*)']*2)
    entity['name'] = '测试'
    entity['itemstyle'] = {'color':'#00FF00'}
    result['pie'].append(entity.copy())
    result['data'].append(str(num[0]['count(*)']*2))
    return JsonResponse(result,safe=False,json_dumps_params={'ensure_ascii':False})

def getAvSala(request):
    '''
    @ 查询所有职位的平均薪资
    @ 返回
    @ {
        "job": ['人工智能','后端开发','数据','设计','前端开发','游戏开发','运维技术支持','移动开发','产品','运营','测试'],
        "data":[
            {
                "name":"岗位1",
                "value":"平均薪资"
            },
            {
                "name":"岗位2",
                "value":"平均薪资"
            }
        ]
        }
    '''
    result = {
        "job": ['人工智能','后端开发','数据','设计','前端开发','游戏开发','运维技术支持','移动开发','产品','运营','测试'],
        "data":[]
    }
    jobname=["人工智能","后端开发","数据","设计","前端开发","游戏开发","运维技术支持","移动开发","产品","运营","测试"]
    #数据库所有表名
    tables = ['ai_table', 'backend_table', 'data_table', 'design_table', 'foreend_table', 'game_table', 'maintain_table', 'mobile_table', 'product_table', 'run_table', 'test_table']
    entity = {}
    #数据库连接
    con.ping(reconnect=True)  #固有写法
    cu = con.cursor(cursor=pymysql.cursors.DictCursor)
    for i in range(0, len(tables)):
        tablename = tables[i]
        cu.execute('SELECT avg(money) from ' + tablename)
        num = cu.fetchall()
        # print(num)
        # print(jobname[i])
        entity['name'] = jobname[i]
        entity['value'] = num[0]['avg(money)']
        result['data'].append(entity.copy())
    cu.close()
    return JsonResponse(result,safe=False,json_dumps_params={'ensure_ascii':False})

def getFiveAvSala(request):
    '''
    @ 返回五个职位各省的平均薪资
    @ 返回格式
        {
            "province":[
                ["省份1","省份2"……],
                ["省份1","省份2"……],
                ["省份1","省份2"……]
            ],
            "data":[
                ["平均薪资1","平均薪资2"……],
                ["平均薪资1","平均薪资2"……],
                ["平均薪资1","平均薪资2"……],
            ]
        }
    @ 顺序为 人工智能 前端开发 游戏开发 移动开发 测试
    '''
    tables = ['ai_table', 'foreend_table', 'game_table', 'mobile_table', 'test_table']
    result = {
        "province": [],
        "data":[]
    }
    #数据库连接
    con.ping(reconnect=True)  #固有写法
    cu = con.cursor(cursor=pymysql.cursors.DictCursor)
    for i in range(0, len(tables)):
        tablename = tables[i]
        cu.execute('select distinct(province) from ' + tablename)
        message = cu.fetchall()
        provinces = []  # 每个表的所有城市名放这里
        salaries=[] # 每个城市平均薪资放这里
        for j in range(0, len(message)):
            province = message[j]['province']
            provinces.append(province)
            cu.execute("select avg(money) from " + tablename + " where province= '" + province+"'")
            num = cu.fetchall()
            salaries.append(num[0]['avg(money)'])
        result['province'].append(provinces.copy())
        result['data'].append(salaries.copy())
    return JsonResponse(result,safe=False,json_dumps_params={'ensure_ascii':False})

def getTotalMap(request):
    '''
    * 返回总表地图信息的接口
    * 以{"position":{"北京市":["经度,纬度"]},"data":[{"name":"北京市","value":"20"},{"name":"","value":""}]} 格式返回
    '''
    #数据库连接
    con.ping(reconnect=True)  #固有写法
    cu = con.cursor(cursor=pymysql.cursors.DictCursor)
    result = {
        "data":[]
    }
    #查询总表中所有province
    cu.execute('SELECT DISTINCT(province) from total_table')
    allprovince = cu.fetchall()
    entity = {}
    position={}
    for i in range(0, len(allprovince)):
        province = allprovince[i]['province']
        #查询经纬度
        cu.execute("SELECT latitude,longitude from total_table where province='" + province + "'")
        location = cu.fetchall()
        locations = []
        locations.append(str(location[0]['latitude']))
        locations.append(str(location[0]['longitude']))
        position[province] = locations
        #查询总数
        cu.execute("SELECT count(*) from total_table where province='" + province + "'")
        num = cu.fetchall()
        entity['name'] = province
        entity['value'] = str(num[0]['count(*)']*10)
        result['data'].append(entity.copy())
    result['position']=position
    return JsonResponse(result,safe=False,json_dumps_params={'ensure_ascii':False})

def getHotCity(request):
    '''
    * 返回热门城市及热门城市的岗位需求量
    * 返回 {"data": [
        { value: 20, name: "云南" },
        { value: 26, name: "北京" },
        { value: 24, name: "山东" },
        { value: 25, name: "河北" },
        { value: 20, name: "江苏" },
        ]}
    '''
    result = {
        "data":[]
    }
    con.ping(reconnect=True)  #固有写法
    #查询所有的城市
    cu = con.cursor(cursor=pymysql.cursors.DictCursor)
    cu.execute("select DISTINCT(province) from total_table")
    pro = cu.fetchall()
    print(pro)
    dic = {}
    for i in pro:
        cu.execute("select count(money) from total_table where province="+"'"+i['province']+"'")
        num = cu.fetchall()
        dic[i['province']]=num[0]['count(money)'];
    dic=sorted(dic.items(),key=lambda e:e[1],reverse=True)
    count=6
    for k in dic:
        temp={'value':k[1],'name':k[0]}
        result['data'].append(temp)
        count=count-1
        if count==0:
            break
    return JsonResponse(result,safe=False,json_dumps_params={'ensure_ascii':False})

def getJobNum(request):
    '''
    * 返回最热门的六个岗位需求
    * 返回 {"data":[
      "旅游行业",
      "教育培训",
      "游戏行业",
      "医疗行业",
      "电商行业",
      "社交行业",
      "金融行业"
      ],"value": [200, 300, 300, 900, 1500, 1200, 600]}
    '''
    result = {
        "data":[],"value":[]
    }
    con.ping(reconnect=True)  #固有写法
    #查询所有的城市
    cu = con.cursor(cursor=pymysql.cursors.DictCursor)
    cu.execute('select distinct(type) from whole_table')
    job=cu.fetchall()
    dic = {}
    for j in job:
        name = j['type']
        cu.execute("select count(*) from whole_table where type="+"'"+name+"'")
        num=cu.fetchall()
        dic[name]=num[0]['count(*)']
    dic=sorted(dic.items(),key=lambda e:e[1],reverse=True)

    count=6
    for k in dic:
        result['data'].append(k[0])
        result['value'].append(k[1])
        count=count-1
        if count==0:
            break
    return JsonResponse(result,safe=False,json_dumps_params={'ensure_ascii':False})

def getJobSalary(request):
    '''
    * 返回薪资最高的前五个职业
    * 返回 {"data":[702, 350, 610, 793, 664],"job":["职业一","职业二","职业三","职业四","职业五"],"baifenbi":"60%,49%,51%,59%,80%"}
    '''
    result = {
        "data":[],"job":[],"baifenbi":[]
    }
    con.ping(reconnect=True)  #固有写法
    #查询所有的城市
    cu = con.cursor(cursor=pymysql.cursors.DictCursor)
    cu.execute('select distinct(type) from whole_table')
    job=cu.fetchall()
    dic = {}
    for j in job:
        name = j['type']
        cu.execute("select max(money) from whole_table where type="+"'"+name+"'")
        num=cu.fetchall()
        dic[name]=num[0]['max(money)']
    dic=sorted(dic.items(),key=lambda e:e[1],reverse=True)

    count=5
    sum=0
    for k in dic:
        result['data'].append(k[1])
        result['job'].append(k[0])
        sum=sum+float(k[1])
        count=count-1
        if count==0:
            break
    count=5
    for k in dic:
        s=str(int(100*float(k[1])/sum))
        result['baifenbi'].append(s)
        count=count-1
        if count==0:
            break
    return JsonResponse(result,safe=False,json_dumps_params={'ensure_ascii':False})


'''
* 后端接口:
* getMapMessage ==> 返回人工智能岗位各省的需求数量和各省经纬度
* getCityNum ==> 返回人工智能岗位各省的需求数量
* getValue ==> 返回5个岗位各省的需求量
                value1:人工智能
                value2:前端开发
                value3:游戏开发
                value4:移动开发
                value5:测试
* getNeedNum ==> 返回11个岗位的总需求
* getAVSala == > 返回所有职位（11个）的平均薪资
* getFiveAvSala ==> 返回五个岗位的所有省的平均薪资
*
*
*
*
'''
