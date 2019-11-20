#
#File Name:test.py
#Author:Kgod
#Email:17621512033@163.com
#Homepage:https://aaakgold.github.io
#Create Date:2019-11-19 17:11:50
#Last Modified:2019年11月20日 星期三 19时38分21秒
#Description:
#/

newStr = input("请输入测试字符串：") #按行输入
newStr_sort = sorted(set(newStr)) #使用set去重后排序
for ch in newStr_sort:
    print(ch + str(newStr.count(ch)),end ='')

# print()
