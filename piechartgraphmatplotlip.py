import matplotlib.pyplot as plt
party=["BJP","CONGRESS","SP","BSP","OTHERS"]
votes=[1200,400,200,150,50]
plt.axis("equal")
plt.pie(votes,labels=party,radius=1,explode=[0.1,0.03,0.06,0.08,0.09],autopct="%0.1f%%",startangle=75)
plt.title("ELECTION COMMITION OF INDIA")
plt.show()