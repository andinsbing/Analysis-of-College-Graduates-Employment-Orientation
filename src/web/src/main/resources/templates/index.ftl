
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>大学生就业分析</title>
<link rel="stylesheet" href="${rc.contextPath}/static/css/jquery-labelauty.css">
<link rel="stylesheet" href="${rc.contextPath}/static/css/index.css">
<script src="${rc.contextPath}/static/js/info.js"></script>
<script src="${rc.contextPath}/static/js/jquery-1.8.3.min.js"></script>
<script src="${rc.contextPath}/static/js/jquery-labelauty.js"></script>

</head>    
<body style="min-width: 1000px;">	
	<div class="index-search-another" style="position: relative;">
		<div style="margin:0 auto;">
			<h1 style="line-height:1;color: #099;font-size: 50px;">大学生就业分析</h1>			
		</div>
    <div>
      <button style="padding:10px 20px;display:inline-block;font-size:20px;color:#333" class="index-banner-nav-selected">职业预测</button>
      <button style="padding:10px 20px;display:inline-block;font-size:20px;color:#333">工资预测</button>
  </div>
	</div>
  

<center class="show">

<h3>选择您擅长的技能</h3>
<form action="">
  <ul class="dowebok">
      <#list abilities as ability>
          <li><input type="checkbox" name="abilitys" data-labelauty="${ability}" value="${ability}"></li>
      </#list>
</ul>

  <span class="button-wrap">
    <a onclick="toPredictJobPage()" class="button button-pill button-raised button-primary">提交</a>
  </span>
</form>
    <script type="text/javascript">
        function toPredictJobPage() {
            var abilitys = document.getElementsByName("abilitys");
            var abilitysVal = [];
            var options = "";
            for(var i=0;i<abilitys.length;i++){
                if(abilitys[i].checked){
                    abilitysVal.push(abilitys[i].value);
                }
            }
            for(var i=0;i<abilitysVal.length;i++){
                if(i == abilitysVal.length-1){
                    options = options + abilitysVal[i];
                }else {
                    options = options + abilitysVal[i]+" ";
                }
            }

            $.ajax({
                type : "get",
                async : true,        //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
                url : "http://120.79.179.183:8802/getPre?position="+options,    //请求发送到ShowInfoIndexServlet处
                data : {},        //请求内包含一个key为name，value为A0001的参数；服务器接收到客户端请求时通过request.getParameter方法获取该参数值
                dataType : "text",        //返回数据形式为json
                success : function(result) {
                    if (true) {
                        window.location.href = "${rc.contextPath}/toPredictJobPage?jobName="+result;
                    }else {
                       alert("服务器开小差了，数据请求失败");
                    }
                },
                error : function(errorMsg) {
                    //请求失败时执行该函数

                    alert("系统出错误");
                }
            });
        }
    </script>

<script>
$(function(){
  $(':input').labelauty();
});
</script>
</center>

<center>

  <div style="width: 250px;">
    <h3>选择您想要预测的职业</h3>

   <form action="">
      <div class="fs20 cfix">
    <label for="">工作职位:</label>
    <select name="jobName" id="jobName">
        <#list jobs as job>
            <option value="${job}">${job}</option>
        </#list>
    </select>
  </div>
  <div class="fs20 cfix">
    <label for="">工作城市:</label>
    <select name="city" id="city" onchange="getCity()">
    <#--<option value="">省份</option>-->
        <#list cities as city>
            <option value="${city}">${city}</option>
        </#list>
     <!-- 利用js把省份添加到下拉列表里-->
       <#--<script type="text/javascript"> -->
        <#--for(var i=0;i<provinceArr.length;i++)    -->
        <#--{-->
            <#--document.write("<option value='"+i+"'>"+provinceArr[i]+"</option>");-->
            <#---->
        <#--}-->
    <#--</script>-->
    </select>
  </div>
  <div class="fs20 cfix">
    <label for="">工作经验:</label>
    <select name="experience" id="experience">
      <option value="经验1-3年">经验1-3年</option>
      <option value="经验3-5年">经验3-5年</option>
      <option value="经验5-10年">经验5-10年</option>
      <option value="经验不限">经验不限</option>
      <option value="经验10年以上">经验10年以上</option>
      <option value="经验1年以下">经验1年以下</option>
    </select>
  </div>
  <span class="button-wrap" style="margin-top: 20px;">
    <a onclick="toAnalizePage2()" class="button button-pill button-raised button-primary">提交</a>
  </span>

       <script type="text/javascript">
           function toAnalizePage2() {
               var jobName = document.getElementById("jobName").value;
               var city = document.getElementById("city").value;
               var experience = document.getElementById("experience").value;
               window.location.href = '${rc.contextPath}/toAnalizePage2?jobName='+jobName+'&city='+city+'&exp='+experience;
           }
       </script>

   </form>
    </div> 
  
  <script>
          //当省份的选择发生变化时调用 该方法   将市县加载到下拉选择框
        function getCity()
    {
        /*
        //1.获取省份选择框的对象
        var provincesobj=document.getElementById("province");
        //2.获取市县选择框的对象
        var cityobj=document.getElementById("city");
        //3.获取被选择的省份的索引
        var index=provincesobj.selectedIndex;

        //alert(provincesobj[index].value+","+provincesobj[index].text);
        ////4.通过省份的索引获取它的value值，value值也是它在数组的索引值
        var value=provincesobj[index].value;;

        //5.获取对应省份的市县数组
        var cityName=cityArr[value];
        //6.将下拉框清楚索引为0之后的，只保留第一个
        cityobj.length=1;
        //通过循环遍历市县元素给下拉框赋值
        for(var i=1;i<cityArr[value].length;i++)
        {
            cityobj.options[cityobj.options.length]=new Option(cityName[i],i);

        }

        */

    }
 
</script>

</center>
</body>
<script>
var aButton = document.getElementsByTagName('button');
var aDiv = document.getElementsByTagName('center');

//给每一个button都添加点击事件
for (var i = 0; i < aButton.length; i++) {
//通过给button自定义属性来解决
aButton[i].index=i;//每个键存储一下
aButton[i].onclick = function () {
//点击事件的实现？？  this就是点击的button
for (var j = 0; j < aButton.length; j++) {
aButton[j].className = '';
aDiv[j].className = '';
}
//再给应该添加的对象添加className
this.className = 'index-banner-nav-selected';
aDiv[this.index].className = 'show';
};
}

</script>
</html>

