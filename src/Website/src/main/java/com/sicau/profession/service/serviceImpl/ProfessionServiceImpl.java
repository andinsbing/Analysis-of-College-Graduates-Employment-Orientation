package com.sicau.profession.service.serviceImpl;

import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import com.sicau.profession.dao.ProfessionInfoDao;
import com.sicau.profession.service.ProfessionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * ProfessionServiceImpl
 * create by chenshihang on 2018/9/1
 */
@Service
public class ProfessionServiceImpl implements ProfessionService {

    @Autowired
    private ProfessionInfoDao professionInfoDao;

    @Override
    public List<String> getJobExperiences(String jobName) {
        return professionInfoDao.getJobExperiences(jobName);
    }

    @Override
    public List<String> getJobCities(String jobName) {
        return professionInfoDao.getJobCities(jobName);

    }

    @Override
    public PageInfo<Map> getProfessionsPage(String jobName,String jobExperience, String jobCity,  int pageNum, int pageSize) {

        PageHelper.startPage(pageNum,pageSize);
        List<Map> maps = professionInfoDao.getProfessions(jobName,jobExperience,jobCity);
        PageInfo<Map> pageInfo = new PageInfo<>(maps);
        pageInfo.setList(maps);
        return pageInfo;

    }

    @Override
    public List<Map> getSalaryTop10(String jobName) {
        return professionInfoDao.getSalaryTop10(jobName);
    }

    @Override
    public List<Map> getDemandTop10(String jobName) {
        return professionInfoDao.getDemandTop10(jobName);
    }

    @Override
    public Map getJobInfo(String jobName, int id) {
        return professionInfoDao.getJobInfo(jobName,id);
    }

    @Override
    public List<String> getAbilities() {
        return professionInfoDao.getAbilities();
    }

    @Override
    public List<String> getCities() {
        return professionInfoDao.getCities();
    }

    @Override
    public List<String> getJobs() {
        return professionInfoDao.getJobs();
    }

    @Override
    public int getAveSalary(String jobName) {
        int result ;
        List<Map> maps = professionInfoDao.getAllCityAveSalary(jobName);
        int sum = 0;
        for(Map map:maps){
            sum += Integer.valueOf(map.get("平均工资").toString().replace(",",""));
        }
        result = sum/maps.size();
        return result;
    }



    @Override
    public Map<String, Object> getAbilityAnalyze(String jobName) {
        List<String> abilityNames = new ArrayList<>();
        List<Double> abilityValues = new ArrayList<>();

        List<Map> maps = professionInfoDao.getAbilityAnalyze(jobName);
        for(Map map:maps){
            abilityNames.add(map.get("名称").toString());
            abilityValues.add(Double.valueOf(map.get("相对比率").toString()));
        }
        Map<String,Object> result = new HashMap<>();
        result.put("abilityNames",abilityNames);
//        result.put("abilityValues",abilityValues);
        result.put("datas",maps);

        return result;
    }

    @Override
    public List<Map> getPredictInfoClassifyByExp(String jobName) {
        List<String> exps = professionInfoDao.getPredictExperiences(jobName);
        List<Map> result = new ArrayList<>();
        for (String exp:exps){
            result.add(professionInfoHandle(professionInfoDao.getPredictInfo(jobName,exp),exp));
        }
        return result;

    }

    static Map<String,Object> professionInfoHandle(List<Map> maps,String exp){
        Map<String,Object> result = new HashMap<>();
        List<String> cities = new ArrayList<>();
        List<Double> lowestSalaries = new ArrayList<>();
        List<Double> highestSalaries = new ArrayList<>();
        for(Map map:maps){
            cities.add(map.get("城市").toString());
            lowestSalaries.add(Double.valueOf(map.get("预测最低工资").toString()));
            highestSalaries.add(Double.valueOf(map.get("预测最高工资").toString()));
        }
        result.put("cities",cities);
        result.put("lowestSalaries",lowestSalaries);
        result.put("highestSalaries",highestSalaries);
        result.put("exp",exp);
        return result;
    }

    public List<String> getPredictExperiences(String jobName){
        return professionInfoDao.getPredictExperiences(jobName);
    }

    @Override
    public List<Map> getSalaryPercent(String jobName) {
        return professionInfoDao.getSalaryPercent(jobName);
    }

    @Override
    public List<Map> getExpPercent(String jobName) {
        return professionInfoDao.getExpPercent(jobName);
    }

    @Override
    public Map getRecordCount(String jobName) {

        System.out.println("-------------"+jobName);

        return professionInfoDao.getRecordCount(jobName);
    }

    @Override
    public List<Map> getSalaryPercent2(String jobName, String city, String exp) {
        return professionInfoDao.getSalaryPercent2(jobName,city,exp);
    }

    @Override
    public Map getPredictInfo2(String jobName, String city, String exp) {
        return professionInfoDao.getPredictInfo2(jobName,city,exp);
    }

    @Override
    public List<String> getRelateJobName(String jobName) {
        List<Map> maps = professionInfoDao.getRelateJob(jobName);
        List<String> result = new ArrayList<>();
        for(Map map:maps){
            if(map.get("职业名称").toString() == jobName){
                continue;
            }else {
                result.add(map.get("职业名称").toString());
            }
        }
        return result;
    }

//    @Override
//    public Map<String, Object> getSalaryPercent(String jobName) {
//        List<Map> maps = professionInfoDao.getSalaryPercent(jobName);
//        Map<String,Object> result = new HashMap<>();
//        List<String> ranges = new ArrayList<>();
//        List<Double> percents = new ArrayList<>();
//        for(Map map: maps){
//            ranges.add(map.get("工资情况").toString());
//            percents.add(Double.valueOf(map.get("比例").toString()));
//        }
//        result.put("ranges",ranges);
//        result.put("percents",percents);
//        return result;
//    }
//
//    @Override
//    public Map<String, Object> getExpPercent(String jobName) {
//        List<Map> maps = professionInfoDao.getExpPercent(jobName);
//        Map<String,Object> result = new HashMap<>();
//        List<String> ranges = new ArrayList<>();
//        List<Double> percents = new ArrayList<>();
//        for(Map map: maps){
//            ranges.add(map.get("经验要求").toString());
//            percents.add(Double.valueOf(map.get("比例").toString()));
//        }
//        result.put("ranges",ranges);
//        result.put("percents",percents);
//        return result;
//    }




}
