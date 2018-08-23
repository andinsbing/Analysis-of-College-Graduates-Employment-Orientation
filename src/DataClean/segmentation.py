import os.path
import os
import jieba
seg_list = jieba.cut('你好，我是林鑫', cut_all=True)
print(seg_list)


work_dir = "C:\\Users\\lx\\Desktop\\test"
os.chdir(work_dir)

test_context="[设计与模式识别、图像智能分析处理相关的算法', '图形图像处理、计算机视觉相关算法的研发以及应用程序的编写', '核心项目算法设计及算法实现；开发和调试算法原型，优化、移植及软件其测试', '负责机器视觉系统图象处理、分析及识别算法的设计、实现及调试', '扎实的数学功底和分析技能，精通计算机视觉中的数学方法', '具备模式识别、图像处理、机器视觉、信号处理和人工智能等基础知识', '对图像特征、机器学习有深刻认识与理解', '精通图像处理基本概念和常用算法包括图像预处理算法和高级处理算法(常见的图像处理算法，包括增强、分割、复原、形态学处理等)', '熟悉常见的模式识别算法，特别是基于图像的模式识别算法，掌握特征提取、特征统计和分类器设计', '熟练使用OpenCV、Matlab、Halcon中的一种或一种以上工具库]"
print('--'.join(jieba.cut(test_context,cut_all=True))) 
print('--'.join(jieba.cut(test_context,cut_all=False))) 
print('--'.join(jieba.cut_for_search(test_context))) 


# test_file = 'bingdufenxi'
# with open(test_file, 'r', encoding='utf-8') as file_handle:
#     print(file_handle.read())
