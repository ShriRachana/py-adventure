#Inheritance is when we can use one class and it's methods and objects inside another without specifically creating them all over again

from Chef import Chef
from chinesechef import chinesechef

myChef = Chef()
myChef.make_special_dish()

myChineseChef = chinesechef()
myChineseChef.make_fried_rice()
myChineseChef.make_special_dish()