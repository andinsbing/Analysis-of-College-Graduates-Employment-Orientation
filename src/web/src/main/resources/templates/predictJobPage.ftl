
<!DOCTYPE HTML>
<html lang="en">
<head>
<title>分析情况总览</title>

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

	<div class="job-head-box mb20">
		<div class="banner">
			<h3 class="headtitle" style=" padding-top: 10px; margin-left: 30px;">为您推荐的职位：${jobName}</h3>
			<a href="${rc.contextPath}/toAnalizePage?jobName=${jobName}" class="button white small">查看职业分析</a>
			<p class="fs16 gray9 ml30" style="margin-top: 5px;margin-bottom: 5px">相关职位推荐：

			<#list relateJobNames as relateJobName>
                <a  title="${relateJobName}" href="${rc.contextPath}/toAnalizePage?jobName=${relateJobName}"   style="margin-left: 5px;margin-right: 5px; display:inline-block;text-decoration:none;white-space:nowrap;text-overflow:ellipsis ;text-align: center">${relateJobName}</a>
			</#list>
			</p>

			<p class="fs16 gray9 mb20 ml30" style="padding-bottom: 20px;"> 根据你提供的信息，推荐系统得出的结果</p>
		</div>
	</div>


    <#--<div class="jk-matter">-->
        <#--<ul class="screen-ul">-->
            <#--<li>-->
                <#--<span>工作经验：</span>-->
				<#--<#list experiences as experience>-->
                    <#--<a  href="#">${experience}</a>-->
				<#--</#list>-->
            <#--</li>-->
            <#--<li>-->
                <#--<span>城市地区：</span>-->
				<#--<#list cities as citie>-->
                	<#--<a  href="#">${citie}</a>-->
				<#--</#list>-->
            <#--</li>-->
            <#--<li>-->
                <#--<span>薪酬水平：</span>-->
                <#--<a  href="#">所有</a>-->
                <#--<a  href="#"> 2000以下</a>-->
                <#--<a  href="#"> 2000-2999</a>-->
            <#--</li>-->
        <#--</ul>-->
    <#--</div>-->
    <hr>



	<div class="row">
		<div class="col-md-8">
			<div class="jk-box jk-matter ml20" data-hasJob="1">

				<div >
					<h4 title="上海客户经理就业形势分析" class="headtitle" style="padding-top: 10px; margin-left: 30px;">推荐职位招聘信息总览</h4>

					<hr>
				</div>
				<div class="small-search cfix" style="margin-bottom:0">
					<ul class="fl sort-cut cfix width100">
						<li><span class="paixu">排序结果：</span></li>
						<#--<li><a  href="">综合↓</a></li>-->
						<li><a class="cut-selected" href="">综合↓</a></li>
							
						<li class="fr"><span class="sort-cut-result">找到<span style="color:#f60"> ${pageInfo.total} </span>条${jobName}开发招聘 , 来自不同的招聘网站</span></li>
					</ul>
				</div>
			
				<ul class="searcher-job-detail" >
					<#list pageInfo.list as profession>
                        <li>
                            <div class="cfix">

                                <div class="fr searchTitTxt" style="width:100%">
                                    <div class="cfix">
                                        <a href="${rc.contextPath}/toJobInfoPage?jobName=${jobName}&&id=${profession.ID}" title="${profession.招聘单位}" rel="nofollow" class="fl fs18 fwb mb5"  target="_blank">${profession.招聘单位}</a>
                                        <span class="fr heartHollow " data-type="Y"></span>
                                    </div>
                                    <div class="fs16 mb5">
                                        <a href="${rc.contextPath}/toJobInfoPage?jobName=${jobName}&&id=${profession.ID}" target="_blank" title="${profession.岗位名称}">${profession.岗位名称}</a>

                                        <span class="fs14" style="position: relative;top: -1px;margin-left: 5px;">
										<span class="gray9">
											${profession.公司福利}
										</span>
									</span>

                                    </div>

                                    <div>${profession.经验要求}<em class="grayC">|</em>   ${profession.工资}<em class="grayC">|</em>${profession.城市}</div>
                                </div>
                            </div>
                        </li>
					</#list>

				</ul>
			<div style="padding-left: 64px" class="j-pageNum">
				<#--<#list 1..pageInfo.lastPage as i>-->
                    <#--<a href=''>${i}</a>-->
				<#--</#list>-->
				<#--<p class='pager cfix box'>-->
					<#--<em class='selected'>1</em>-->
					<#--<a href=''>2</a>-->
					<#--<a href=''>3</a>-->
					<#--<a href=''>4</a>-->
					<#--<a class='pg-updown' href=''>下一页</a>-->
				<#--</p>-->

					<script type="text/javascript">
						var prePage = '${pageInfo.prePage}';
						if(prePage == '0'){
//                            document.getElementById("prePage").disabled="true";
						}
						var nextPage = '${pageInfo.nextPage}';
						var pagesAddOne = '${pageInfo.pages+1}';
//                        alert("pagesAddOne="+pagesAddOne);
						if(nextPage == pagesAddOne ){
//                            document.getElementById("nextPage").disabled="true";
						}
					</script>

                    <nav aria-label="Page navigation example">
                        <ul  class="pagination justify-content-center">
                            <li id="prePage" class="page-item">
                                <a class="page-link" href="${rc.contextPath}/toPredictJobPage?jobName=${jobName}&pageNum=${pageInfo.prePage}" tabindex="-1" >上一页</a>
                            </li>
							<#list pageInfo.firstPage .. pageInfo.lastPage as i>
                                <li class="page-item"><a class="page-link" href="${rc.contextPath}/toPredictJobPage?jobName=${jobName}&pageNum=${i}">${i}</a></li>
							</#list>
                            <li class="page-item">
                                <a id="nextPage" class="page-link" href="${rc.contextPath}/toPredictJobPage?jobName=${jobName}&pageNum=${pageInfo.nextPage}">下一页</a>
                            </li>
                        </ul>
                    </nav>
			</div>
			</div>
			
		</div>
        <div class="col-md-4">

            <div class="bgf mr20" >
                <div class="cfix jk-box" style="height: 400px;background-color: white;padding-top: 10px;padding-left: 10px">

                    <h2 class="fs16">${jobName}平均薪资排名top10</h2>
					<#assign  a= 1>
                    <ul class="cfix" style="margin-left: -35px;">
					<#list salaryTop10 as salary >
                        <li class="top10 cfix">
							<#if a <= 3>
                                <em class="numbg orange numtext">${a}</em>
							<#else >
                                <em class="numbg #f99 numtext">${a}</em>
							</#if>
                            <div class="name cfix">
									<span class="backGround">
										<span class="industry">
											<a  title="${salary.城市}" href="#" disabled="true"  style="display:inline-block;text-decoration:none;white-space:nowrap;text-overflow:ellipsis ;width: 55px;text-align: center">${salary.城市}</a>
											<div style="display:inline;color:#099; margin-left: 10px;">
												<em style="font-size:3px">----------------------------------------------------------------------------------</em>
											</div>
										</span>
									</span>
                                <em style="margin-left: 5px;">￥${salary.平均工资}</em>
                            </div>
                        </li>
						<#assign a = a + 1>
					</#list>
                    </ul>
                </div>




                <div class="cfix jk-box" style="height: 400px;background-color: white;padding-top: 10px;padding-left: 10px">

                    <h2 class="fs16">${jobName}职位需求排名top10</h2>
				<#assign  b= 1>
                    <ul class="cfix" style="margin-left: -35px;">
					<#list demandTop10 as demand >
                        <li class="top10 cfix">
							<#if b <= 3>
                                <em class="numbg orange numtext">${b}</em>
							<#else >
                                <em class="numbg #f99 numtext">${b}</em>
							</#if>
                            <div class="name cfix">
									<span class="backGround">
										<span class="industry">
											<a  title="${demand.城市}" href="#" disabled="true"  style="display:inline-block;text-decoration:none;white-space:nowrap;text-overflow:ellipsis ;width: 55px;text-align: center">${demand.城市}</a>
											<div style="display:inline;color:#099; margin-left: 10px;">
												<em style="font-size:3px">----------------------------------------------------------------------------------</em>
											</div>
										</span>
									</span>
                                <em style="margin-left: 5px; color: #098;">${demand.数量}个职位</em>
                            </div>
                        </li>
						<#assign b = b + 1>
					</#list>
                    </ul>
                </div>
            </div>
        </div>
	</div>		
</body>
<script src="${rc.contextPath}/static/js/jquery.min.js"></script>
<script src="${rc.contextPath}/static/js/echarts.js"></script>

</html>