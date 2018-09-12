package com.sicau.profession.service;

import com.github.pagehelper.PageInfo;

import java.util.List;
import java.util.Map;

/**
 * ProfessionService
 * create by chenshihang on 2018/9/1
 */
public interface ProfessionService {

    List<String> getJobExperiences(String jobName);

    List<String> getJobCities(String jobName);

    PageInfo<Map> getProfessionsPage(String jobName,String jobExperience,String jobCity,int pageNum,int pageSize);

    List<Map> getSalaryTop10(String jobName);

    List<Map> getDemandTop10(String jobName);

    Map getJobInfo(String jobName,int id);

    List<String> getAbilities();

    List<String> getCities();

    List<String> getJobs();

    int getAveSalary(String jobName);


    Map<String,Object> getAbilityAnalyze(String jobName);


    List<Map> getPredictInfoClassifyByExp(String jobName);


    List<String> getPredictExperiences(String jobName);

    List<Map> getSalaryPercent(String jobName);

    List<Map> getExpPercent(String jobName);

    Map getRecordCount(String jobName);

    List<Map> getSalaryPercent2(String jobName,String city,String exp);

    Map getPredictInfo2(String jobName,String city,String exp);

    List<String> getRelateJobName(String jobName);
}
