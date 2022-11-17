import  matplotlib.pyplot as plt
days=[1,2,3,4,5,6,7,8]
max_t=[30,51,45,39,36,45,40,42]
min_t=[40,12,44,15,16,17,45,13]
#plt.plot(color="#212F3D",marker="D",markersize="10")
plt.plot(days,max_t,color='red',label='max',linewidth=3)
plt.plot(days,min_t,color='green',label='min',linewidth=3)
plt.xlabel('Days')
plt.ylabel('temperature')
plt.title('weather information')
plt.legend(loc="best",shadow="true",fontsize="large")
plt.grid()
plt.show()
