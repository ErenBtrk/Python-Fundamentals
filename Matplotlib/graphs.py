import matplotlib.pyplot as plt

year = [2011,2012,2013,2014,2015]

player1 = [8,10,12,7,9]
player2 = [7,12,5,15,21]
player3 = [18,20,22,25,19]

#Stack Plot

plt.plot([],[],color="pink",label="player")
plt.plot([],[],color="red",label="player")
plt.plot([],[],color="blue",label="player")

plt.stackplot(year,player1,player2,player3,colors=["pink","red","blue"])

plt.title("Goals per year")

plt.xlabel("Year")

plt.ylabel("Goals")

plt.legend()

plt.show()