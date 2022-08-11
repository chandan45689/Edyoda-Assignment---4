#Write a Python program to triple all the numbers of a given list of integers.Use Python map.

sample_list=[1,2,3,4,5,6,7]

triple=list(map(lambda x:x*3,sample_list))
print(triple)