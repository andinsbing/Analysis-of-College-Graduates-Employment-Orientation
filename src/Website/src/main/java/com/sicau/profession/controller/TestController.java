package com.sicau.profession.controller;

import com.sicau.profession.dao.ProfessionInfoDao;
import com.sicau.profession.service.ProfessionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletResponse;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * TestController
 * create by chenshihang on 2018/8/30
 */
@Controller
public class TestController {

    @Autowired
    private ProfessionInfoDao professionInfoDao;
    @Autowired
    private ProfessionService professionService;

    @ResponseBody
    @RequestMapping("/test1")
    public String test1(){
        List<Map> mapList = professionInfoDao.getSalaryTop10("会计");

        System.out.println("----------test1-------");
        return "hehe";
    }

    @ResponseBody
    @RequestMapping("/test122")
    public Object test122(){

        System.out.println("----------test13-------");
        return professionInfoDao.otherDbTest();
    }

    @ResponseBody
    @RequestMapping("/test1223")
    public Object test1223(){
        System.out.println("----------test133-------");
        return professionService.getAbilityAnalyze("会计");
    }


    @ResponseBody
    @RequestMapping("/test12234")
    public Object test12234(){
        System.out.println("----------test1334-------");
        List<Map> maps = professionService.getPredictInfoClassifyByExp("会计");
        System.out.println("----");
        return maps;
    }

    @ResponseBody
    @RequestMapping("/test122345")
    public Object test122345(HttpServletResponse response){
        response.setHeader("Access-Control-Allow-Origin", "*");
        System.out.println("----------test1334-------");
        List<String> exps = professionService.getPredictExperiences("会计");
        System.out.println("----");
        return exps;
    }
    @ResponseBody
    @RequestMapping("/test12234566")
    public Object getPredictInfo(HttpServletResponse response,String jobName){
        System.out.println("进入getPredictInfo：jobName="+jobName);
        response.setHeader("Access-Control-Allow-Origin", "*");
        Map<String,Object> result = new HashMap<>();
        List<String> exps = professionService.getPredictExperiences(jobName);
        List<Map> maps = professionService.getPredictInfoClassifyByExp(jobName);
        result.put("exps",exps);
        result.put("maps",maps);
        return result;
    }


    @ResponseBody
    @RequestMapping("/test1223456")
    public Object test1223456(HttpServletResponse response){
        response.setHeader("Access-Control-Allow-Origin", "*");
        List<Map> salaryPercent = professionInfoDao.getSalaryPercent("会计");
        System.out.println("--");

        return salaryPercent;
    }

    @ResponseBody
    @RequestMapping("/test12234567")
    public Object test12234567(HttpServletResponse response){
        response.setHeader("Access-Control-Allow-Origin", "*");
        List<Map> salaryPercent = professionInfoDao.getSalaryPercent2("会计","上海","经验1-3年");
        System.out.println("--");

        return salaryPercent;
    }



    @RequestMapping("/test1223456722")
    public ModelAndView test1223456722(HttpServletResponse response){
        response.setHeader("Access-Control-Allow-Origin", "*");

        ModelAndView modelAndView = new ModelAndView();
        modelAndView.addObject("text1","llllssss");
        modelAndView.setViewName("/test");
        return modelAndView;
    }

    @ResponseBody
    @RequestMapping("/test12234567ss")
    public Object test12234567ss(HttpServletResponse response){
        response.setHeader("Access-Control-Allow-Origin", "*");


        return "景荣第三方";
    }

    @ResponseBody
    @RequestMapping("/test12234567ssaa")
    public Object test12234567ssa(HttpServletResponse response){
        response.setHeader("Access-Control-Allow-Origin", "*");
        Map map = new HashMap();
        map.put("str","hehehexxx");

        return map;
    }

    @ResponseBody
    @RequestMapping("/test12234567ssassa")
    public Object test12234567ssad(HttpServletResponse response){
        response.setHeader("Access-Control-Allow-Origin", "*");
        List<Map> map = professionInfoDao.getRelateJob("会计");

        return map;
    }

}
