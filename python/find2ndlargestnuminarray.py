# created by sidhanshu monga
# 08 may, 2018

#Problem statement :  find second largest number in the array

array = [3,5,6,2,6,8,9,7,3,5,10,8,9,4,9]

array.sort(reverse=True);
# print array
max = array[0]
for a in array:
    if(a < max):
        print a;
        break;
    max = a;