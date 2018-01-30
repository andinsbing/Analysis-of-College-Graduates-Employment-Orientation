import os
import shutil

li = [

    'https://www.lagou.com/zhaopin/jinrongtouzijingli/',
    'https://www.lagou.com/zhaopin/jinrongfenxishi/',
    'https://www.lagou.com/zhaopin/touzizhuli/',
    'https://www.lagou.com/zhaopin/rongzi/',
    'https://www.lagou.com/zhaopin/binggou/',
    'https://www.lagou.com/zhaopin/hangyeyanjiu/',
    'https://www.lagou.com/zhaopin/touzizheguanxi/',
    'https://www.lagou.com/zhaopin/zichanguanli/',
    'https://www.lagou.com/zhaopin/licaiguwen/',
    'https://www.lagou.com/zhaopin/jiaoyiyuan/',
    'https://www.lagou.com/zhaopin/jinrong3fengkong/',
    'https://www.lagou.com/zhaopin/zixinpinggu/',
    'https://www.lagou.com/zhaopin/heguijicha/',
    'https://www.lagou.com/zhaopin/jinronglvshi/',
    'https://www.lagou.com/zhaopin/jinrongshenji/',
    'https://www.lagou.com/zhaopin/jinrongfawu/',
    'https://www.lagou.com/zhaopin/jinrongkuaiji/',
    'https://www.lagou.com/zhaopin/jinrongqingsuan/',
    'https://www.lagou.com/zhaopin/jinrongtouzizongjian/',
    'https://www.lagou.com/zhaopin/rongzizongjian/',
    'https://www.lagou.com/zhaopin/binggouzongjian/',
    'https://www.lagou.com/zhaopin/fengxiankongzhizongjian/',
    'https://www.lagou.com/zhaopin/zongcaifuzongcai/',

]
for each in li:
    each = each[30:-1]
    if os.path.exists('D:\\科研项目\\数据\\' + each):
        shutil.copyfile('D:\\科研项目\\数据\\' + each, 'D:\\科研项目\\金融\\' + each)
