package com.sicau.profession.dao;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;
import java.util.Map;

/**
 * ProfessionInfoDao
 * create by chenshihang on 2018/9/1
 */
@Mapper
public interface ProfessionInfoDao {

    List<Map> method1();

    List<String> getJobExperiences( @Param("jobName") String jobName);

    List<String> getJobCities(@Param("jobName")String jobName);

    List<Map> getProfessions(@Param("jobName") String jobName,@Param("jobExperience") String jobExperience,@Param("jobCity") String jobCity);

    List<Map> getSalaryTop10(@Param("jobName")String jobName);

    List<Map> getDemandTop10(@Param("jobName")String jobName);

    Map getJobInfo(@Param("jobName")String jobName,@Param("id")int id);

    Map otherDbTest();


    List<String> getAbilities();

    List<String> getCities();

    List<String> getJobs();

    List<Map> getAllCityAveSalary(@Param("jobName")String jobName);

    List<Map> getAbilityAnalyze(@Param("jobName")String jobName);

    List<String> getPredictExperiences(String jobName);

    List<Map> getPredictInfo(@Param("jobName")String jobName,@Param("experience")String experience);


    List<Map> getSalaryPercent(@Param("jobName")String jobName);

    List<Map> getExpPercent(@Param("jobName")String jobName);

    Map getRecordCount(@Param("jobName")String jobName);

    List<Map> getSalaryPercent2(@Param("jobName")String jobName,@Param("city")String city,@Param("exp")String exp);

    Map getPredictInfo2(@Param("jobName")String jobName,@Param("city")String city,@Param("exp")String exp);


    List<Map> getRelateJob(String jobName);
}
