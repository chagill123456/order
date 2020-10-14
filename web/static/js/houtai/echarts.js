$(function () {

    ceshis();
    ceshis2();

    ceshis4();

    function ceshis() {
        var myChart = echarts.init(document.getElementById('chart1'));
         myChart.setOption({
        title: {
              text: "文章点击率排名",
              textStyle:{
                   color: "rgba(102, 0, 255, 1)"
              }


        },
        tooltip: {},
        legend: {
            data:['点击数']
        },
        xAxis: {
                   axisLabel: {
                    show: true,
                    textStyle: {
                        color: "#ebf8ac" //X轴文字颜色
                    }
                },
                axisLine: {
                    lineStyle: {
                        color: '#01FCE3'
                    }
                },
            data: []
        },
        yAxis: {
            axisLabel: {
                    textStyle: {
                        color: "#2EC7C9" //X轴文字颜色
                    }
                },
                axisLine: {
                    lineStyle: {
                        color: '#01FCE3'
                    }
                },


        },
        series: [{
            name: '点击数',
            type: 'bar',
            color:"rgba(0, 170, 255, 1)",
            data: []
        }]
    });

    myChart.showLoading();    //数据加载完之前先显示一段简单的loading动画



    $.ajax({
      url:common_ops.buildUrl("/ht/getdata"),
                type:'POST',
                data:{},
                dataType:'json',
        success : function(result) {
            //请求成功时执行该函数内容，result即为服务器返回的json对象
            if (result) {

                myChart.hideLoading();    //隐藏加载动画
                myChart.setOption({        //加载数据图表
                    xAxis: {
                        data: result.xList,
                    },
                    series: [{
                        // 根据名字对应到相应的系列
                        name: '点击率',

                        data: result.yList,
                    }]
                });

            }

        },
        error : function(errorMsg) {
            //请求失败时执行该函数
            alert("图表请求数据失败!");
            myChart.hideLoading();
        }
    });


        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }

     function ceshis2() {
        var myChart = echarts.init(document.getElementById('chart2'));
         myChart.setOption({
        title: {
              text: "地区点击率排名",
              textStyle:{
                   color: "rgba(102, 0, 255, 1)"
              }


        },
        tooltip: {},
        legend: {
            data:['点击数']
        },
        xAxis: {
                   axisLabel: {
                    show: true,
                    textStyle: {
                        color: "#ebf8ac" //X轴文字颜色
                    }
                },
                axisLine: {
                    lineStyle: {
                        color: '#01FCE3'
                    }
                },
            data: []
        },
        yAxis: {
            axisLabel: {
                    textStyle: {
                        color: "#2EC7C9" //X轴文字颜色
                    }
                },
                axisLine: {
                    lineStyle: {
                        color: '#01FCE3'
                    }
                },


        },
        series: [{
            name: '点击数',
            type: 'bar',
            color:"rgba(0, 170, 255, 1)",
            data: []
        }]
    });

    myChart.showLoading();    //数据加载完之前先显示一段简单的loading动画



    $.ajax({
      url:common_ops.buildUrl("/ht/getssdjvdata"),
                type:'POST',
                data:{},
                dataType:'json',
        success : function(result) {
            //请求成功时执行该函数内容，result即为服务器返回的json对象
            if (result) {

                myChart.hideLoading();    //隐藏加载动画
                myChart.setOption({        //加载数据图表
                    xAxis: {
                        data: result.xList,
                    },
                    series: [{
                        // 根据名字对应到相应的系列
                        name: '点击率',

                        data: result.yList,
                    }]
                });

            }

        },
        error : function(errorMsg) {
            //请求失败时执行该函数
            alert("图表请求数据失败!");
            myChart.hideLoading();
        }
    });


        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }


    function ceshis4() {
        var myChart = echarts.init(document.getElementById('chart4'));

        var ydata = [];
        var color = [];
        var xdata = [];


       myChart.setOption({
            /*backgroundColor: "rgba(255,255,255,1)",*/
            color: color,
            legend: {
                orient: "vartical",
                x: "left",
                top: "center",
                left: "53%",
                bottom: "0%",
                data: xdata,
                itemWidth: 10,
                itemHeight: 10,
                textStyle: {
                    color: '#fff'
                },
                /*itemGap: 16,*/
                /*formatter:function(name){
                  var oa = option.series[0].data;
                  var num = oa[0].value + oa[1].value + oa[2].value + oa[3].value+oa[4].value + oa[5].value + oa[6].value + oa[7].value+oa[8].value + oa[9].value ;
                  for(var i = 0; i < option.series[0].data.length; i++){
                      if(name==oa[i].name){
                          return ' '+name + '    |    ' + oa[i].value + '    |    ' + (oa[i].value/num * 100).toFixed(2) + '%';
                      }
                  }
                }*/

                formatter: function(name) {
                    return '' + name
                }
            },
            series: [{
                type: 'pie',
                clockwise: false, //饼图的扇区是否是顺时针排布
                minAngle: 2, //最小的扇区角度（0 ~ 360）
                radius: ["10%", "55%"],
                center: ["30%", "45%"],
                avoidLabelOverlap: false,
                itemStyle: { //图形样式
                    normal: {
                        borderColor: '#ffffff',
                        borderWidth: 1,
                    },
                },
                label: {
                    normal: {
                        show: false,
                        position: 'center',
                        formatter: '{text|{b}}\n{c} ({d}%)',
                        rich: {
                            text: {
                                color: "#fff",
                                fontSize: 14,
                                align: 'center',
                                verticalAlign: 'middle',
                                padding: 8
                            },
                            value: {
                                color: "#8693F3",
                                fontSize: 24,
                                align: 'center',
                                verticalAlign: 'middle',
                            },
                        }
                    },
                    emphasis: {
                        show: true,
                        textStyle: {
                            fontSize: 24,
                        }
                    }
                },
                data: ydata
            }]
        })


    myChart.showLoading();    //数据加载完之前先显示一段简单的loading动画



    $.ajax({
      url:common_ops.buildUrl("/ht/getareadata"),
                type:'POST',
                data:{},
                dataType:'json',
        success : function(result) {
            //请求成功时执行该函数内容，result即为服务器返回的json对象
            if (result) {

                myChart.hideLoading();    //隐藏加载动画
                myChart.setOption({
                    color: result.cList,
                    legend: {
                        data: result.xList,

                    },
                    series: [{
                        // 根据名字对应到相应的系列

                        data: result.yList,
                    }]
                });

            }

        },
        error : function(errorMsg) {
            //请求失败时执行该函数
            alert("图表请求数据失败!");
            myChart.hideLoading();
        }
    });


        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }




});