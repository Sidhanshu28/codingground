# created by sidhanshu monga
# 08 may, 2018

#Problem statement :  find sum of given numbers

echo -n "Enter number : "
read n
sd=0
sum=0

while [ $n -gt 0 ]
do
    sd=$(( $n % 10 ))
    n=$(( $n / 10 ))
    sum=$(( $sum + $sd ))
done
echo "sum : $sum"