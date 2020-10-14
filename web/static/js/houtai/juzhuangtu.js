$(function () {

     ceshis();
     function ceshis() {
            //获得图表的options对象
              var myChart = echarts.init(document.getElementById('chart1'));
            //通过Ajax获取数据
            $.ajax({
                url:common_ops.buildUrl("/ht/getdata"),
                type:'POST',
                data:{},
                dataType:'json',
                success : function(result) {
                    if (result) {
                    var dataobj=JSON.parse(result);

                   myChart.setOption({
                         xAxis: {
                             data:dataobj.xList
                         },
                         series: [{
                             // 根据名字对应到相应的系列
                             name: '点击数',
                             data:dataobj.yList
                         }]
                     });

         window.addEventListener("resize",function(){
            myChart.resize();
                     });
                      }
                },
                error : function(errorMsg) {
                    alert("无数据");

                }
            });

        }
}