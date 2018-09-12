package com.sicau.profession.controller;

import com.sicau.profession.dao.ProfessionInfoDao;
import com.sicau.profession.dao.TestDao;
import com.sun.org.apache.xpath.internal.operations.Mod;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;

import java.sql.SQLException;
import java.util.List;
import java.util.Map;

/**
 * CommonController
 * create by chenshihang on 2018/8/31
 */
@Controller
public class CommonController {

    @Autowired
    private ProfessionInfoDao professionInfoDao;

    @RequestMapping("/toIndex")
    public ModelAndView toIndex() throws SQLException {
        ModelAndView modelAndView = new ModelAndView();
        List<String> cities = TestDao.getCities();
        modelAndView.addObject("cities",cities);
        modelAndView.setViewName("/test");
        return modelAndView;
    }

    @ResponseBody
    @RequestMapping("/testdao")
    public List<Map> toIndex22() throws SQLException {
        System.out.println("---1---");
        List<Map> maps = professionInfoDao.method1();
        System.out.println("---2---");
        return maps;
    }

    @ResponseBody
    @RequestMapping("/testdao2")
    public Object toIndex222() throws SQLException {
        List<String> strings = professionInfoDao.getJobExperiences("会计");
        return strings;
    }

//    @ResponseBody
    @RequestMapping("/testdao23")
    public ModelAndView toIndex2223() throws SQLException {
        List<Map> maps = professionInfoDao.getProfessions("会计","经验1-3年","上海");
        ModelAndView modelAndView = new ModelAndView();
        modelAndView.addObject("maps",maps);
        modelAndView.setViewName("/map_test");
        return modelAndView;
    }



}
