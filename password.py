# -- coding: utf-8 --
# @Time : 2021/1/22 9:26
# @Author : Los Angeles Clippers
# @Email: 229456906@qq.com
# @sinaemail: angelesclippers@sina.com

import execjs

with open('password.js', 'r', encoding='utf-8') as f:
    jspwd = f.read()
    f.close()

context = execjs.compile(jspwd)
pwd = context.call('pwd', '7777777')
print(pwd)
