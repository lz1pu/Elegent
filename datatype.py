'''
python数据类型
    整数：不受限制，有无限大的精度
    浮点数：有精度误差，例如0.1+0.2不严格等于0.3，小数采用科学计数法表示
    复数:
    
'''

import decimal
a = decimal.Decimal('0.1')
b = decimal.Decimal('0.2')
print(a + b)
c = 0.000000005
print(c)


'''
操作                                                            结果
x + y
x - y
x * y
x / y
x % y                                               x除以y的余数
x // y                                             x除以y取整数部分，向下取整。
-x                                                   x的相反数
+x                                                  x本身
abs(x)                                           x的绝对值，若x为复数，则返回模
int(x)                                             将x转换成整数
float(x)                                         将x转换成浮点数
c0mplex(re, im)                         返回一个复数，re是实部，im是虚部
c.conjugate()                               返回c的共轭复数
divmod(x, y)                                 返回(x // y ,  x % y)
pow(x, y)                                        计算x的y次方
x**y                                                  计算x的y次方                   


'''

