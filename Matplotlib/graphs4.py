import matplotlib.pyplot as plt


#Histogram

ages = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,11,51]
age_groups = [0,10,20,30,40,50,60,70,80,90,100]

hist = plt.hist(ages,age_groups,histtype="bar",rwidth=0.5)
plt.xlabel("Age Groups")
plt.xticks(age_groups)
plt.ylabel("Person Number")
plt.title("Histogram Graphic")

plt.show()