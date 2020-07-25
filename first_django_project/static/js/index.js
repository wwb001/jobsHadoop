// 柱状图模块1
(function () {
    $.ajax({
        "url": "static/json/getJobNum.json",
        "type": "post",
        "data": {},
        "dataType": "json",
        "success": function (datajson1) {
            generateChart1(datajson1);
        }
    })

    function generateChart1(datajson1) {

        // 1实例化对象
        var myChart = echarts.init(document.querySelector(".bar .chart"));
        // 2. 指定配置项和数据
        var option = {
            color: ["#2f89cf"],
            tooltip: {
                trigger: "axis",
                axisPointer: {
                    // 坐标轴指示器，坐标轴触发有效
                    type: "shadow" // 默认为直线，可选为：'line' | 'shadow'
                }
            },
            // 修改图表的大小
            grid: {
                left: "0%",
                top: "10px",
                right: "0%",
                bottom: "4%",
                containLabel: true
            },
            xAxis: [
                {
                    type: "category",
                    data: datajson1["data"],
                    axisTick: {
                        alignWithLabel: true
                    },
                    // 修改刻度标签 相关样式
                    axisLabel: {
                        color: "rgba(255,255,255,.6) ",
                        fontSize: "12"
                    },
                    // 不显示x坐标轴的样式
                    axisLine: {
                        show: false
                    }
                }
            ],
            yAxis: [
                {
                    type: "value",
                    // 修改刻度标签 相关样式
                    axisLabel: {
                        color: "rgba(255,255,255,.6) ",
                        fontSize: 12
                    },
                    // y轴的线条改为了 2像素
                    axisLine: {
                        lineStyle: {
                            color: "rgba(255,255,255,.1)",
                            width: 2
                        }
                    },
                    // y轴分割线的颜色
                    splitLine: {
                        lineStyle: {
                            color: "rgba(255,255,255,.1)"
                        }
                    }
                }
            ],
            series: [
                {
                    name: "直接访问",
                    type: "bar",
                    barWidth: "35%",
                    data: datajson1["value"],
                    itemStyle: {
                        // 修改柱子圆角
                        barBorderRadius: 5
                    }
                }
            ]
        };
        // 3. 把配置项给实例对象
        myChart.setOption(option);

        // 4. 让图表跟随屏幕自动的去适应
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }
})();
// 柱状图2
(function () {
    $.ajax({
        "url": "static/json/getJobSalary.json",
        "type": "post",
        "data": {},
        "dataType": "json",
        "success": function (datajson1) {
            generateChart2(datajson1);
        }
    })

    function generateChart2(datajson1) {

        console.log(datajson1);

        var myColor = ["#1089E7", "#F57474", "#56D0E3", "#F8B448", "#8B78F6"];
        // 1. 实例化对象
        var myChart = echarts.init(document.querySelector(".bar2 .chart"));
        // 2. 指定配置和数据
        var option = {
            grid: {
                top: "10%",
                left: "22%",
                bottom: "10%"
                // containLabel: true
            },
            // 不显示x轴的相关信息
            xAxis: {
                show: false
            },
            yAxis: [
                {
                    type: "category",
                    inverse: true,
                    data: datajson1["job"],
                    // 不显示y轴的线
                    axisLine: {
                        show: false
                    },
                    // 不显示刻度
                    axisTick: {
                        show: false
                    },
                    // 把刻度标签里面的文字颜色设置为白色
                    axisLabel: {
                        color: "#fff"
                    }
                },
                {
                    data: datajson1["data"],
                    inverse: true,
                    // 不显示y轴的线
                    axisLine: {
                        show: false
                    },
                    // 不显示刻度
                    axisTick: {
                        show: false
                    },
                    // 把刻度标签里面的文字颜色设置为白色
                    axisLabel: {
                        color: "#fff"
                    }
                }
            ],
            series: [
                {
                    name: "条",
                    type: "bar",
                    data: datajson1["baifenbi"],
                    yAxisIndex: 0,
                    // 修改第一组柱子的圆角
                    itemStyle: {
                        barBorderRadius: 20,
                        // 此时的color 可以修改柱子的颜色
                        color: function (params) {
                            // params 传进来的是柱子对象
                            // console.log(params);
                            // dataIndex 是当前柱子的索引号
                            return myColor[params.dataIndex];
                        }
                    },
                    // 柱子之间的距离
                    barCategoryGap: 50,
                    //柱子的宽度
                    barWidth: 10,
                    // 显示柱子内的文字
                    label: {
                        show: true,
                        position: "inside",
                        // {c} 会自动的解析为 数据  data里面的数据
                        formatter: "{c}"
                    }
                },
                {
                    name: "框",
                    type: "bar",
                    barCategoryGap: 50,
                    barWidth: 15,
                    yAxisIndex: 1,
                    data: [100, 100, 100, 100, 100],
                    itemStyle: {
                        color: "none",
                        borderColor: "#00c1de",
                        borderWidth: 3,
                        barBorderRadius: 15
                    }
                }
            ]
        };

        // 3. 把配置给实例对象
        myChart.setOption(option);

        // 4. 让图表跟随屏幕自动的去适应
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }
})();
// 折线图1模块制作
(function () {
    $.ajax({
        "url": "static/json/salaryPart.json",
        "type": "post",
        "data": {},
        "dataType": "json",
        "success": function (datajson1) {
            generateChart2(datajson1);
        }
    })

    function generateChart2(datajson1) {

        var yearData = [
            {
                year: "分组一", // 年份
                data: datajson1['value1']
            },
            {
                year: "分组二", // 年份
                data: datajson1['value2']
            }
        ];
        // 1. 实例化对象
        var myChart = echarts.init(document.querySelector(".line .chart"));
        // 2.指定配置
        var option = {
            // 通过这个color修改两条线的颜色
            color: ["#00f2f1", "#ed3f35", "#00FF00", "#FFFF00"],
            tooltip: {
                trigger: "axis"
            },
            legend: {
                // 如果series 对象有name 值，则 legend可以不用写data
                // 修改图例组件 文字颜色
                textStyle: {
                    color: "#4c9bfd"
                },
                // 这个10% 必须加引号
                right: "10%"
            },
            grid: {
                top: "20%",
                left: "3%",
                right: "4%",
                bottom: "3%",
                show: true, // 显示边框
                borderColor: "#012f4a", // 边框颜色
                containLabel: true // 包含刻度文字在内
            },

            xAxis: {
                type: "category",
                boundaryGap: false,
                data: datajson1['qujian'],
                axisTick: {
                    show: false // 去除刻度线
                },
                axisLabel: {
                    color: "#4c9bfd" // 文本颜色
                },
                axisLine: {
                    show: false // 去除轴线
                }
            },
            yAxis: {
                type: "value",
                axisTick: {
                    show: false // 去除刻度线
                },
                axisLabel: {
                    color: "#4c9bfd" // 文本颜色
                },
                axisLine: {
                    show: false // 去除轴线
                },
                splitLine: {
                    lineStyle: {
                        color: "#012f4a" // 分割线颜色
                    }
                }
            },
            series: [
                {
                    name: "人工智能",
                    type: "line",
                    // true 可以让我们的折线显示带有弧度
                    smooth: true,
                    data: yearData[0].data[0]
                },
                {
                    name: "后端开发",
                    type: "line",
                    smooth: true,
                    data: yearData[0].data[1]
                },
                {
                    name: "数据",
                    type: "line",
                    smooth: true,
                    color: "#00FF00",
                    data: yearData[0].data[2]
                }, {
                    name: "前端开发",
                    type: "line",
                    smooth: true,
                    color: "#FFFF00",
                    data: yearData[0].data[3]
                }

            ]
        };

        // 3. 把配置给实例对象
        myChart.setOption(option);
        // 4. 让图表跟随屏幕自动的去适应
        window.addEventListener("resize", function () {
            myChart.resize();
        });

        // 5.点击切换效果
        $(".line h2").on("click", "a", function () {
            // alert(1);
            // console.log($(this).index());
            // 点击 a 之后 根据当前a的索引号 找到对应的 yearData的相关对象
            // console.log(yearData[$(this).index()]);
            var obj = yearData[$(this).index()];
            option.series[0].data = obj.data[0];
            option.series[1].data = obj.data[1];
            option.series[2].data = obj.data[2];
            option.series[3].data = obj.data[3];
            // 需要重新渲染
            myChart.setOption(option);
        });
    }
})();

// 饼形图2 地区分布模块
(function () {
    var myChart = echarts.init(document.querySelector(".pie2 .chart"));

    $.ajax({
        "url": "static/json/getHotCity.json",
        "type": "post",
        "data": {},
        "dataType": "json",
        "success": function (datajson1) {
            generateChart2(datajson1);
        }
    })

    function generateChart2(datajson1) {
        var option = {
            color: [
                "#006cff",
                "#60cda0",
                "#ed8884",
                "#ff9f7f",
                "#0096ff",
                "#9fe6b8",
                "#32c5e9",
                "#1d9dff"
            ],
            tooltip: {
                trigger: "item",
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            legend: {
                bottom: "0%",
                itemWidth: 10,
                itemHeight: 10,
                textStyle: {
                    color: "rgba(255,255,255,.5)",
                    fontSize: "12"
                }
            },
            series: [
                {
                    name: "地区分布",
                    type: "pie",
                    radius: ["10%", "70%"],
                    center: ["50%", "50%"],
                    roseType: "radius",
                    // 图形的文字标签
                    label: {
                        fontSize: 10
                    },
                    // 链接图形和文字的线条
                    labelLine: {
                        // length 链接图形的线条
                        length: 6,
                        // length2 链接文字的线条
                        length2: 8
                    },
                    data: datajson1["data"],
                }
            ]
        };
        myChart.setOption(option);
        // 监听浏览器缩放，图表对象调用缩放resize函数
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }
})();

(function () {
    var myChart = echarts.init(document.querySelector(".map .chart"));

    $.ajax({
        "url": "static/json/3d.json",
        "type": "post",
        "data": {},
        "dataType": "json",
        "success": function (datajson1) {
            generateChart3(datajson1);
        }
    })

    function generateChart3(datajson1) {


        var geoCoordMap = datajson1["position"];

        var alirl = [[[121.15, 31.89], [109.781327, 39.608266]],
            [[120.38, 37.35], [122.207216, 29.985295]],
            [[123.97, 47.33], [120.13, 33.38]],
            [[118.87, 42.28], [120.33, 36.07]],
            [[121.52, 36.89], [117.93, 40.97]],
            [[102.188043, 38.520089], [122.1, 37.5]],
            [[118.58, 24.93], [101.718637, 26.582347]],
            [[120.53, 36.86], [121.48, 31.22]],
            [[119.46, 35.42], [122.05, 37.2]],
            [[119.97, 35.88], [116.1, 24.55]],
            [[121.05, 32.08], [112.02, 22.93]],
            [[91.11, 29.97], [118.1, 24.46]]
        ]
        var convertData = function (data) {
            var res = [];
            for (var i = 0; i < data.length; i++) {
                var geoCoord = geoCoordMap[data[i].name];
                if (geoCoord) {
                    res.push({
                        name: data[i].name,
                        value: geoCoord.concat(data[i].value)
                    });
                }
            }
            // console.log(res)
            return res;
        };
        option = {
            title: {
                text: '测试bar3D、scatter3D、geo3D',
                x: 'left',
                top: "10",
                textStyle: {
                    color: '#000',
                    fontSize: 14
                }
            },
            tooltip: {
                show: true,
                // formatter:(params)=>{
                //   let data = "测试1:"+params.name + "<br/>"+"值:"+ params.value[2]+"<br/>"+"地理坐标:[" + params.value[0]+","+params.value[1] +"]";
                //   return data;
                // },
            },
            visualMap: [{
                type: 'continuous',
                seriesIndex: 0,
                text: ['bar3D'],
                calculable: true,
                max: 20000,
                inRange: {
                    color: ['#87aa66', '#eba438', '#d94d4c']
                }
            }, {
                type: 'continuous',
                seriesIndex: 1,
                text: ['scatter3D'],
                left: 'right',
                max: 100,
                calculable: true,
                inRange: {
                    color: ['#000', 'blue', 'purple']
                }
            }],
            geo3D: {
                map: 'china',
                roam: true,
                itemStyle: {
                    areaColor: '#1d5e98',
                    opacity: 1,
                    borderWidth: 0.4,
                    borderColor: '#000'
                },
                label: {
                    show: true,
                    textStyle: {
                        color: '#000', //地图初始化区域字体颜色
                        fontSize: 8,
                        opacity: 1,
                        backgroundColor: 'rgba(0,23,11,0)'
                    },
                },
                emphasis: { //当鼠标放上去  地区区域是否显示名称
                    label: {
                        show: true,
                        textStyle: {
                            color: '#fff',
                            fontSize: 3,
                            backgroundColor: 'rgba(0,23,11,0)'
                        }
                    }
                },
                //shading: 'lambert',
                light: { //光照阴影
                    main: {
                        color: '#fff', //光照颜色
                        intensity: 1.2, //光照强度
                        //shadowQuality: 'high', //阴影亮度
                        shadow: false, //是否显示阴影
                        alpha: 55,
                        beta: 10

                    },
                    ambient: {
                        intensity: 0.3
                    }
                }
            },
            series: [
                //柱状图
                {
                    name: 'bar3D',
                    type: "bar3D",
                    coordinateSystem: 'geo3D',
                    barSize: 1, //柱子粗细
                    shading: 'lambert',
                    opacity: 1,
                    bevelSize: 0.3,
                    label: {
                        show: false,
                        formatter: '{b}'
                    },
                    data: convertData(datajson1["data"]),
                },
            ]
        };
        myChart.setOption(option);

        // 监听浏览器缩放，图表对象调用缩放resize函数
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }
})();
