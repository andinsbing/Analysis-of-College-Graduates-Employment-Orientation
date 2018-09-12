<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>招聘详情</title>
    <meta name="viewport" content="width=device-width,initial-scale=1" charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <link href="${rc.contextPath}/static/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="${rc.contextPath}/static/css/style.css">
    <style>
        .jk-box{margin-bottom:20px;}
        .jk-box h2{font-size:16px;color:#333;font-weight:bold;margin-bottom:5px}
        .jk-matter{padding:10px 15px;background-color:#fff;position:relative}
        .jk-matter .behavior-btn{color:#fff;position:absolute;right:0;top:0;background-color:#999;font-size:12px;display:inline-block;padding:2px 5px}
        .jk-matter .behavior-btn:hover{background-color:#666}
        .small-search{margin-bottom:10px;border-bottom:1px solid #f2f2f2;width:100%;height:40px}
        .sort-cut .fr{float:right}
        .sort-cut li{display:inline-block}
        .sort-cut li .paixu{padding:0;font-weight:bold;color:#333;display:inline-block;height:28px;line-height:28px}
        .sort-cut{display:inline-block;color:#333}
        .sort-cut li a{color:#333;padding:0 5px;display:inline-block;height:28px;line-height:28px;border-radius:5px}
        .sort-cut li a:hover,.sort-cut li a:active{color:#333;background:#e4e4e4}
        .width100{width:100%}
        .cut-selected{color:#333!important;background-color:#e4e4e4;font-weight:bold}
        .sort-cut-result{padding:0;color:#333;display:inline-block;height:32px;line-height:30px}
        .searcher-job-detail li{padding:10px 0;border-bottom:1px solid #f2f2f2;list-style: none;}
        .searcher-job-detail>a{font-size:18px;text-decoration:none;font-weight:normal}
        .searcher-job-detail h2{font-size:18px;font-weight:bold;color:#099}
        .searcher-job-detail h3{font-weight:normal;font-size:14px;display:inline-block;width:40%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
        .searchTitTxt a:visited{color:#099!important}
        .searchTitTxt a{
            color: #099!important
        }
        .fs18{font-size:18px!important}
        .fs16{font-size:16px!important}
        .mb5{
            margin-bottom: 5px!important
        }
        .grayC{color:#ccc!important}
        .fwb{font-weight:bold}
        .heartHollow{width:25px;height:25px;display:inline-block;background:url('') no-repeat;cursor:pointer}
        .pager{font-size:18px; padding-top:20px;}
        .pager a, .pager em{width:40px; height:40px; float:left; margin-right:10px; border:1px solid #cecece; text-align:center; line-height:40px;  font-weight:bold; color:#666666; text-decoration:none; background-color:#F2F2F2;border-radius:3px;}
        .pager a:hover, .pager .selected{background-color:#DEDEDE; }
        .pager .pg-updown{padding:0 8px; width:80px;}
        .pager a:visited{color:#666}
        .box{margin-bottom:20px}

        .bgf{background-color:#f2f2f2}

        .mr5{margin-right:5px}
        .ml20{
            margin-left: 20px;
        }
        .mr20{
            margin-right: 20px;
        }
        .mb20{
            margin-bottom: 20px;
        }
        .competitive ul{font-size:14px}
        .top10{float:left;width:100%;padding:0 3px;height:30px}
        .competitive .name{display:inline-block;float:left;width:90%}
        .competitive .name .industryCont{display:inline-block;color:#333;text-decoration:none;max-width:170px;overflow:hidden;white-space:nowrap;text-overflow:ellipsis}
        .competitive .name .areaCont{display:inline-block;color:#099;text-decoration:none;max-width:170px;overflow:hidden;white-space:nowrap;text-overflow:ellipsis}
        .competitive .name a:hover{color:#066}
        .competitive .name span{display:inline-block}
        .numbg{background-color:#099;height:20px;float:left;border-radius:10px;margin-right:10px}
        .numtext{width:18px;height:18px;line-height:17px;font-size:11px;color:#fff;display:inline-block;text-align:center;margin-top:2px}
        .orange{background-color:#f60}
        .name .areaCont{display:inline-block;text-decoration:none;max-width:170px;overflow:hidden;white-space:nowrap;text-overflow:ellipsis}
        .name a:hover{color:#c5262a;text-decoration:underline}
        .backGround{float:left;background-image:url();background-repeat:repeat-x;background-position:0 10px;}
        .industry{display:inline-block;background-color:#fff;padding-right:10px;font-size:16px}
        .money{display:inline-block;float:right;width:60px;text-align:right;color:#333}
        .sample-number{font-size:12px;color:#999;vertical-align:top;margin-top:2px;display:inline-block}
        .industry-sample{display:inline-block;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:170px}
        li{
            list-style: none;
        }
        .fr{
            float: right;
        }
    </style>
</head>
<body style="background-color:#F2F2F2;">
<div class="topdat">
    <div class="Hnav-wrap">
        <div class="cfix Hnav-wrap-room">
            <div class="fl mr20">
                <a href="${rc.contextPath}/toIndexPage" title="">
                    <span style="color: #f2f2f2;vertical-align: middle;margin-left: 30px; font-size: 20px;">首页</span>
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





<div class="container astruct cfix">
    <div class="aleft cfix">
        <div class="job-info box">
            <div  class="jk-box jk-matter j-job-detail">
                <h1 class="text-center">${jobInfo.招聘单位}</h1>
                <h3 title="${jobInfo.岗位名称}" style="margin-bottom: 20px;">${jobInfo.岗位名称}</h3>
                <p style="font-size: 16px;color:#333;font-weight: bold;margin-bottom: 10px;">工作要求</p>

                <ul class="laver cfix fs16">
                    <li><span>工作地区：</span>${jobInfo.城市}</li>
                    <li><span>工作经验：</span><span id="jobAge">${jobInfo.经验要求}</span></li>
                    <li><span>薪资范围：</span><span class="fs16 fwb f60">&yen; ${jobInfo.工资}/月</span></li>
                    <li style="width: 100%;"><span>工作地址：</span>${jobInfo.具体地点}</li>
                    <li><span>公司福利：</span><span class="fs16 fwb f60">${jobInfo.公司福利}</span></li>
                </ul>


                <#--<div style="height:63px;position:relative;overflow:hidden;height:45px;padding-top:5px" class="company-tab-box sbox j-tab-box fs14">-->
                    <#--<span><a href="#" target="_blank" rel="nofollow">餐饮补贴</a></span>-->
                    <#--<span><a href="#" target="_blank" rel="nofollow">月度聚餐</a></span>-->
                    <#--<span><a href="#" target="_blank" rel="nofollow">春游</a></span>-->
                    <#--<span><a href="#" target="_blank" rel="nofollow">新人培训</a></span>-->
                    <#--<span><a href="#" target="_blank" rel="nofollow">技能培训</a></span>-->
                <#--</div>-->


                <p style="font-size: 16px;color: #333;font-weight: bold;margin-bottom: 10px;">岗位职责/工作内容/岗位要求</p>

                <div class="cfix">
                    <div class="hasVist cfix sbox fs16" style="word-break: break-all;">
                        岗位职责：<br />
                        ${jobInfo.岗位要求}
                    </div>
                    <p class="gray9">以上内容仅为本站快照，最新信息请查看源网站</p>
                    <p class="gray9">联系我们时，请注明来源，谢谢！</p>
                    <dl class="JI-so fs16">
                        <dt>发布时间：</dt>
                        <dd><em class="uptime common-icon"></em>2018-08-23</dd>
                        <dt>来源网站：</dt>
                        <dd><em class="sourceWeb common-icon"></em>${jobInfo.发布地点}</dd>
                    </dl>



                    <p class="JI-opt">
                        <a class=""   href="#">去源网站申请</a>
                    </p>


                    <p class="fs12 fr" style="display:inline-block;position:relative;top:0px;line-height:50px;">
                        <a href="#" >免责申明</a>&nbsp;&nbsp;|&nbsp;&nbsp;
                        <a rel="nofollow" href="#">安全求职指南&raquo;</a>
                    </p>

                </div>
                <div>
                    <hr>
                    <h2${jobInfo.城市}${jobInfo.岗位名称}-薪酬概况与就业形势分析</h2>

                    <a href="${rc.contextPath}/toAnalizePage?jobName=${jobName}" class="button white small">查看分析报告</a>
                </div>

            </div>
        </div>
    </div>


</div>
</body>
</html>