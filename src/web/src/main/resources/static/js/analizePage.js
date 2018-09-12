var obj = null;
$.get('macarons.json', function(data){
    obj = JSON.parse(data);
    echarts.registerTheme('macarons', obj);
}, 'json');
var myChart1 = echarts.init(document.getElementById('1'),'macarons');
var myChart2 = echarts.init(document.getElementById('2'),'macarons');
var option1 = {
    title : {
        text: '',
        subtext: '根据真实数据预测而来'
    },
    tooltip : {
        trigger: 'axis'
    },
    legend: {
        data:[],

    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            magicType : {show: true, type: ['line', 'bar']},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    calculable : true,
    xAxis : [
        {
            type : 'category',
            boundaryGap : false,
            data : []
        }
    ],
    yAxis : [
        {
            type : 'value',
            axisLabel : {
                formatter: '￥{value} '
            }
        }
    ],
};
var option2 = {
    title : {
        text: '',
        subtext: '根据真实数据预测而来'
    },
    tooltip : {
        trigger: 'axis'
    },
    legend: {
        data:[]
    },

    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            magicType : {show: true, type: ['line', 'bar']},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    calculable : true,
    xAxis : [
        {
            type : 'category',
            boundaryGap : false,
            data : []
        }
    ],
    yAxis : [
        {
            type : 'value',
            axisLabel : {
                formatter: '￥{value} '
            }
        }
    ],
};

myChart1.setOption(option1);
myChart2.setOption(option2);
myChart1.showLoading();
myChart2.showLoading();
var option1Info;

$.ajax({    //使用JQuery内置的Ajax方法
    type : "post",        //post请求方式
    async : true,        //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
    url : contextPath+"/getPredictInfo?jobName="+jobName,    //请求发送到ShowInfoIndexServlet处
    data : {},        //请求内包含一个key为name，value为A0001的参数；服务器接收到客户端请求时通过request.getParameter方法获取该参数值
    dataType : "json",        //返回数据形式为json
    success : function(result) {
        //请求成功时执行该函数内容，result即为服务器返回的json对象
        if (true) {
            option1Info = result.maps;


            var series = [];
            var series2 = [];
            for(var i = 0;i<option1Info.length;i++){
                var sery = {};
                var sery2 = {};
                sery['name'] = option1Info[i].exp;
                sery['type'] = 'line';
                sery['data'] = option1Info[i].lowestSalaries;
                sery['markPoint'] = {
                    data : [
                        {type : 'max', name: '最大值'},
                        {type : 'min', name: '最小值'}
                    ]
                };
                sery['markLine'] =
                 {
                    data : [
                        {type : 'average', name : '平均值'}
                    ]
                };
                sery2['name'] = sery['name'];
                sery2['type'] = sery['type'];
                sery2['data'] = option1Info[i].highestSalaries;
                sery2['markPoint'] = sery['markPoint'];

                series.push(sery);
                series2.push(sery2);
            }

            var exps = result.exps;
            var exps1 = [] ;
            var exps2 =[];
            if(exps.length>4){
                for(var i=0;i<4;i++){
                    exps1[i] = exps[i];
                }
                for(var i=4;i<exps.length;i++){
                    exps2[i] = exps[i];
                }
                myChart1.setOption({
                    legend: [
                        {
                            x:'center',
                            data:exps1,
                            selectedMode : 'single'

                        },
                        {
                            x:'center',
                            top:'6%',
                            data:exps2,
                            selectedMode : 'single'

                        },
                    ]
                })
            }else {
                myChart1.setOption({
                    legend: [
                        {
                            x:'center',
                            data:exps,
                            selectedMode : 'single'
                        }
                    ]
                })
            }
            myChart1.setOption({
                title:{
                    text:'各城市最低工资预测'
                },
                tooltip:{},
                legend:{
                    // data:exps,
                    selectedMode : 'single'
                },
                xAxis:{
                    data:option1Info[0].cities
                },
                yAxis:{},
                series:series
            });
            myChart2.setOption({
                title:{
                    text:'各城市最高工资预测'
                },
                tooltip:{},
                legend:myChart1.getOption().legend,
                // legend:{
                //     data:exps,
                //     selectedMode : 'single'
                // },
                xAxis:{
                    data:option1Info[0].cities
                },
                yAxis:{},
                series:series2
            });
            myChart1.hideLoading();
            myChart2.hideLoading();



        }else {
            //返回的数据为空时显示提示信息
            alert("图表请求数据为空，您可以稍后再试！");
            myChart1.hideLoading();
            myChart2.hideLoading();
        }

    },
    error : function(errorMsg) {
        //请求失败时执行该函数
        alert("图表请求数据失败，可能是服务器开小差了");
    }
});

myChart1.on('legendselectchanged', function(obj) {
    var name=obj.name;
    var option=myChart1.getOption();

    for(var i=0;i<option1Info.length;i++){
        if(name==option1Info[i].exp){
            option.xAxis[0].data = option1Info[i].cities;
        }
    }
    myChart1.setOption(option,true);
});
myChart2.on('legendselectchanged', function(obj) {
    var name=obj.name;
    var option=myChart2.getOption();
    for(var i=0;i<option1Info.length;i++){
        if(name==option1Info[i].exp){
            option.xAxis[0].data = option1Info[i].cities;
        }
    }
    myChart2.setOption(option,true);
});


//---------------------------------圆饼图数据--------------------------

var myChart5 = echarts.init(document.getElementById('5'),'thyme-macarons');
var option5 = {
    title : {
        text: '职位的能力需求',
        subtext: '数据来源真实可靠',
        x:'center'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
        orient : 'vertical',
        x : 'left',
        data:[]
    },
    calculable : true,
    series : [
        {
            type:'pie',
            radius : '55%',
            center: ['50%', '60%'],
            data:[]

        }
    ]
};
$.ajax({    //使用JQuery内置的Ajax方法
    type : "post",        //post请求方式
    async : true,        //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
    url : contextPath+"/getAbilityAnalize?jobName="+jobName,    //请求发送到ShowInfoIndexServlet处
    data : {},        //请求内包含一个key为name，value为A0001的参数；服务器接收到客户端请求时通过request.getParameter方法获取该参数值
    dataType : "json",        //返回数据形式为json
    success : function(result) {
        //请求成功时执行该函数内容，result即为服务器返回的json对象
        if (true) {

            var seriesData = [];
            var datas = result.datas;
            for(var i=0;i<datas.length;i++){
                var seryData = {};
                seryData['name'] = datas[i].名称;
                seryData['value'] = datas[i].相对比率;
                seriesData.push(seryData);
            }


            var selected = {};
            var names = result.abilityNames;
            for(var i=0;i<datas.length;i++){
                var name = names[i];
                if(i==0){
                    document.getElementById("3").innerText=name;
                }else if(i==1){
                    document.getElementById("4").innerText=name;
                }
                selected[name] = i < 6;
            }
            myChart5.hideLoading();    //隐藏加载动画
            myChart5.setOption({        //载入数据
                title : {
                    text: jobName+'职位的能力需求',
                },
                legend: {
                    type: 'scroll',
                    orient: 'vertical',
                    right: 10,
                    top: 20,
                    bottom: 20,
                    data: names,
                    selected: selected
                },
                series : [
                    {
                        name: '能力',
                        type: 'pie',
                        radius : '55%',
                        center: ['40%', '50%'],
                        data: seriesData,
                        itemStyle: {
                            emphasis: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
                    }
                ]
            });

        }else {
            //返回的数据为空时显示提示信息
            alert("图表请求数据为空，您可以稍后再试！");
            myChart5.hideLoading();
        }

    },
    error : function(errorMsg) {
        //请求失败时执行该函数
        alert("图表请求数据失败，可能是服务器开小差了");
    }
});
myChart5.setOption(option5);

