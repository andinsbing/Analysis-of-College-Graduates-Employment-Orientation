package com.sicau.profession.dao;


import com.sicau.profession.util.DB;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

/**
 * TestDao
 * create by chenshihang on 2018/8/30
 */
public class TestDao {

    private static String GET_CITIES = "SELECT DISTINCT 城市 FROM Resultsalary";


    public static List<String>  getCities() throws SQLException {
        PreparedStatement preparedStatement = DB.getPreparedStatement(GET_CITIES);
        ResultSet rs = preparedStatement.executeQuery();
        List<String> result = new ArrayList<>();
        while (rs.next()){
            result.add(rs.getString(1));
        }
        return result;
    }


    public static void main(String[] args) {
        String jobName = "?交互设计经理与主管";

        System.out.println(jobName.substring(1));
    }






}
