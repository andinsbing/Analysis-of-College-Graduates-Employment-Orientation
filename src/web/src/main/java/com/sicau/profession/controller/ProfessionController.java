package com.sicau.profession.controller;

import com.github.pagehelper.PageInfo;
import com.sicau.profession.service.ProfessionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;

import javax.jws.WebParam;
import javax.servlet.http.HttpServletResponse;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * ProfessionController
 * create by chenshihang on 2018/9/1
 */
@Controller
public class ProfessionController {


    @Autowired
    private ProfessionService professionService;

    @RequestMapping("/toPredictJobPage")
    public ModelAndView toPredictJobPage(String jobName,@RequestParam(value = "pageNum",defaultValue = "1") String pageNum){

        ModelAndView modelAndView = new ModelAndView();

//        List<String> cities = professionService.getJobCities(jobName);
//
//        List<String> experiences = professionService.getJobExperiences(jobName);
        PageInfo<Map> pageInfo = professionService.getProfessionsPage(jobName,null,null,Integer.valueOf(pageNum),10);
        List<Map> salaryTop10 = professionService.getSalaryTop10(jobName);
        List<Map> demandTop10 = professionService.getDemandTop10(jobName);
        System.out.println("---------y--------");

        List<String> relateJobNames = professionService.getRelateJobName(jobName);


//        modelAndView.addObject("cities",cities);
//        modelAndView.addObject("experiences",experiences);
        modelAndView.addObject("pageInfo",pageInfo);
        modelAndView.setViewName("/predictJobPage");
        modelAndView.addObject("jobName",jobName);
        modelAndView.addObject("salaryTop10",salaryTop10);
        modelAndView.addObject("demandTop10",demandTop10);
        modelAndView.addObject("relateJobNames",relateJobNames);
        return modelAndView;

    }

    @RequestMapping("/toJobInfoPage")
    public ModelAndView toJobInfoPage(String jobName,int id){
        ModelAndView modelAndView = new ModelAndView();
        Map jobInfo = professionService.getJobInfo(jobName,id);
        modelAndView.addObject("jobInfo",jobInfo);
        modelAndView.addObject("jobName",jobName);
        modelAndView.setViewName("/jobinfo");
        return  modelAndView;
    }



    @RequestMapping("/getAbilities")
    @ResponseBody
    public List<String> getAbilities(){
        return professionService.getAbilities();

    }
    @RequestMapping("/getCities")
    @ResponseBody
    public List<String> getCities(){
        return professionService.getCities();
    }

    @RequestMapping("/toIndexPage")
    public ModelAndView toIndexPage(){
        ModelAndView modelAndView = new ModelAndView();
        List<String> cities = professionService.getCities();
        List<String> abilities = professionService.getAbilities();
        List<String> jobs = professionService.getJobs();
        modelAndView.addObject("cities",cities);
        modelAndView.addObject("abilities",abilities);
        modelAndView.addObject("jobs",jobs);
        modelAndView.setViewName("/index");
        return modelAndView;
    }

    /**
     * 第三个页面数据准备
     * 1. 工资百分比数据
     * 2. 经验要求百分比数据
     *
     * @param jobName
     * @return
     */
    @RequestMapping("/toAnalizePage")
    public ModelAndView toAnalizePage(String jobName){
        ModelAndView modelAndView = new ModelAndView();
        List<Map> salaryPercentInfos = professionService.getSalaryPercent(jobName);
        List<Map> expPercentInfos = professionService.getExpPercent(jobName);
        Map recordCount = professionService.getRecordCount(jobName);
        int aveSalary = professionService.getAveSalary(jobName);
        modelAndView.addObject("salaryPercentInfos",salaryPercentInfos);
        modelAndView.addObject("expPercentInfos",expPercentInfos);
        modelAndView.addObject("jobName",jobName);
        modelAndView.addObject("aveSalary",aveSalary);
        modelAndView.addObject("recordCount",recordCount);
        modelAndView.setViewName("/analizePage");
        return modelAndView;
    }



    @RequestMapping("/toAnalizePage2")
    public ModelAndView toAnalizePage2(String jobName,String city,String exp){
        if(jobName.charAt(0) == '\uFEFF'){
            jobName = jobName.substring(1);
        }
        System.out.println("-------------jobName1="+jobName);
        ModelAndView modelAndView = new ModelAndView();
        Map recordCount = professionService.getRecordCount(jobName);
        List<Map> salaryPercentInfos = professionService.getSalaryPercent2(jobName,city,exp);
        int aveSalary = professionService.getAveSalary(jobName);
        Map salaryPredictInfoMap = professionService.getPredictInfo2(jobName,city,exp);
        modelAndView.addObject("aveSalary",aveSalary);
        modelAndView.addObject("salaryPredictInfoMap",salaryPredictInfoMap);
        modelAndView.addObject("recordCount",recordCount);
        modelAndView.addObject("salaryPercentInfos",salaryPercentInfos);
        modelAndView.addObject("jobName",jobName);
        modelAndView.addObject("city",city);
        modelAndView.addObject("exp",exp);
        modelAndView.setViewName("/analizePage2");

        return modelAndView;
    }


    /**
     * 第三个页面数据准备
     * 预测最高最低工资：波形图或者柱状图的数据
     * @param response
     * @param jobName
     * @return
     */
    @ResponseBody
    @RequestMapping("/getPredictInfo")
    public Object getPredictInfo(HttpServletResponse response, String jobName){
        response.setHeader("Access-Control-Allow-Origin", "*");
        Map<String,Object> result = new HashMap<>();
        List<String> exps = professionService.getPredictExperiences(jobName);
        List<Map> maps = professionService.getPredictInfoClassifyByExp(jobName);
        result.put("exps",exps);
        result.put("maps",maps);
        return result;
    }

    /**
     * 第三个页面数据准备
     * 职业能力分析：圆饼图的数据
     * @param response
     * @param jobName
     * @return
     */
    @ResponseBody
    @RequestMapping("/getAbilityAnalize")
    public Object getAbilityAnalize(HttpServletResponse response, String jobName){
        response.setHeader("Access-Control-Allow-Origin", "*");
        Map<String,Object> result = professionService.getAbilityAnalyze(jobName);
        return result;
    }





}
