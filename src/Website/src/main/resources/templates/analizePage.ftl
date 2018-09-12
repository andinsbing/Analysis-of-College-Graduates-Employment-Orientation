<!DOCTYPE HTML>
<html lang="en">
<head>
    <title>${jobName}工资收入</title>
    <meta name="description" content=""/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="renderer" content="webkit" charset="UTF-8">
    <link href="${rc.contextPath}/static/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="${rc.contextPath}/static/css/style.css">
</head>
<body style="background-color:#F2F2F2;">
<script type="text/javascript">
    var contextPath = '${rc.contextPath}';
    var jobName = '${jobName}';
</script>
<div class="topdat" id="commonHeaderNav">
    <div class="Hnav-wrap">
        <div class="cfix Hnav-wrap-room">
            <div class="fl mr20">
                <a href="${rc.contextPath}/toIndexPage" title="">
                    <span style="color: #f2f2f2;vertical-align: middle;font-size: 20px;margin-left: 30px;">首页</span>
                    <span class="fs14" style="color: #f2f2f2;vertical-align: middle;">让就业决策更聪明</span>
                </a>
            </div>
            <div class="fl header-search-top-box ">
                <div class="header-search-seletedType ">
                    <span data-type="job" class="">工作搜索</span>
                    <em class="fr" style="font-size: 18px;color: #eeeeee;">|</em>

                </div>

                <form action="${rc.contextPath}/toPredictJobPage" class="header-search-form">
                    <input type="text" class="header-search-text-input fs14" placeholder="输入职业关键词" name="jobName" data-set-tipslist="job" class="fs16" autocomplete="off">
                    <input type="submit" value="" class="header-search-submit " style="display:inline-block;width:25px;height:25px;background:url('${rc.contextPath}/static/img/2.png') no-repeat 0 1px;cursor:pointer;top:7px!important">
                </form>
            </div>


        </div>
    </div>
</div>

<div class="job-head-box mb20">
    <div class="banner">
        <h1 title="上海客户经理就业形势分析" class="headtitle ml30" style="padding-top: 10px;">${jobName} &bull; 就业形势分析</h1>
        <p class="fs16 gray9 mb20 ml30" style="padding-bottom: 20px;"> ${jobName}： 岗位分析如下</p>

    </div>
</div>

<div class="row" style="margin-bottom: 10px;">
    <div class="col-md-1"></div>
    <div class="col-md-4" style="background-color: white"">
        <div style="height: 300px;">
            <div class="money">￥${aveSalary}</div>
            <div class="spans">分析近${recordCount.记录总数}条数据 | ${recordCount.城市数量}个不同城市</div>
            <div class="able">通过数据分析，可以得出${jobName}这个职业最看重的能力是</div>
            <div><a id="3" class="able1"></a></div>
            <div><a id="4" class="able1"></a></div>
            <div class="note">注：平均工资为该职业大量招聘信息的平均工资</div>
        </div>
    </div>
    <div class="col-md-6" style="background-color: white">
        <div id="5" style="height: 300px;"></div>
    </div>
    <div class="col-md-1"></div>
</div>
<div class="row" style="margin-bottom: 10px;">
    <div class="col-md-1"></div>
    <div class="col-md-6">

        <div class="row" style="margin-bottom: 10px;">
            <div class="col-md-12" style="background-color: white">
                <div id="1" style="height: 300px;"></div>
            </div>

        </div>
        <div class="row" style="margin-bottom: 10px;">

            <div class="col-md-12" style="background-color: white">
                <div id="2" style="height: 300px;"></div>
            </div>
        </div>
        <div class="row" style="margin-bottom: 10px;">
            <div class="col-md-12">
                <div style="background-color: #eee;height: 50px;">
                    <div>*预测的数据是通过大数据分析得到的结果，可以选择不同经验查看城市最高、最低工资。</div>
                </div>
            </div>

        </div>
    </div>
    <div class="col-md-4" style="background-color: white; margin-left: 10px">
        <div class="row" style="margin-bottom: 10px; ">
            <div class="col-md-12" style="">
                <div style="height: 230px;">
                    <h2 class="fs16" style="margin-bottom: 15px;padding-left: 20px;padding-top: 5px;font-family: bold">${jobName}工资情况</h2>
                <#list salaryPercentInfos as salaryPercentInfo>
                    <div >
                        <div class="col-md-4">
                            <span style="padding-left: 10px;text-align: center;">${salaryPercentInfo.工资情况}</span>
                        </div>
                        <div class="col-md-8">
                            <div class="progress">
                                <div class="progress-bar success" role="progressbar"
                                     style="width: ${salaryPercentInfo.比例}%" aria-valuenow="${salaryPercentInfo.比例}" aria-valuemin="0"
                                     aria-valuemax="100">${salaryPercentInfo.比例}%
                                </div>
                            </div>
                        </div>
                    </div>
                </#list>
                </div>

            </div>

        </div>
        <div class="row" style="margin-bottom: 10px;">

            <div class="col-md-12" >
                <div style="height: 300px;">
                    <h2 class="fs16" style="margin-bottom: 15px;padding-left: 20px;padding-top: 5px;font-family: bold;">${jobName}经验要求</h2>
                <#list expPercentInfos as expPercentInfo>
                    <div>
                        <div class="col-md-4">
                            <span style="padding-left: 10px;text-align: center;">${expPercentInfo.经验要求}</span>
                        </div>
                        <div class="col-md-8">
                            <div class="progress">
                                <div class="progress-bar success" role="progressbar"
                                     style="width: ${expPercentInfo.比例}%" aria-valuenow="${expPercentInfo.比例}" aria-valuemin="0"
                                     aria-valuemax="100">${expPercentInfo.比例}%
                                </div>
                            </div>
                        </div>
                    </div>

                </#list>

                </div>
            </div>
        </div>
    </div>
    <div class="col-md-1"></div>
</div>


</body>
<script src="${rc.contextPath}/static/js/jquery.min.js"></script>
<script src="${rc.contextPath}/static/js/echarts.js"></script>
<script src="${rc.contextPath}/static/js/thyme-macarons.js"></script>
<script src="${rc.contextPath}/static/js/analizePage.js"></script>
</html>