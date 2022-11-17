import matplotlib.pyplot as plt
import numpy as np
company=["google","tcs","wipro","techsrijan","techanand"]
revenue=[10000,5000,3000,1000,500]
profit=[5000,1000,800,200,100]
xpos=np.arange(len(company))
print(xpos)
#plt.bar(company,revenue,label="Revenue",color="blue")
#plt.bar(company,profit,label="Profit",color="green")
plt.bar(xpos-0.2,revenue,label="Revenue",color="blue",width=0.4)
plt.bar(xpos+0.2,profit,label="Profit",color="green",width=0.4)
plt.xticks(xpos,company)
plt.grid()
plt.title("revenue information")
plt.xlabel("Company")
plt.ylabel("Revenue in million")
plt.title("Company profit & loss")
plt.legend(shadow="true",fontsize="large")
plt.show()
