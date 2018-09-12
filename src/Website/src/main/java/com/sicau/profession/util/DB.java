package com.sicau.profession.util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;


public class DB {
	
	public static String driver = "com.mysql.jdbc.Driver";
	public static String url = "jdbc:mysql://47.100.11.75/prediction";
	public static String user = "root";
	public static String password = "5880940";
	

	public static Connection getConnection()  {

		Connection con = null;
		try{
			Class.forName(driver);
			con =  DriverManager.getConnection(url,user,password);
		}catch (Exception e) {
			// TODO: handle exception
		}
		
		return con;
	}

	public static PreparedStatement getPreparedStatement(String sql){
		try{
			return DB.getConnection().prepareStatement(sql);
		}catch (Exception e){
			return null;
		}
	}

}
