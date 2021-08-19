import matplotlib.pyplot as plt

#Pie Plot

goal_types = ["Penalty","Shooting","Freekick"]

goals = [12,35,7]
colors = ["pink","red","blue"]

plt.pie(goals,labels=goal_types,colors=colors,shadow=True,explode=(0.05,0.05,0.05),autopct="%1.1f%%")

plt.show()