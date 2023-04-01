# coding=utf-8 
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['KaiTi']
plt.rcParams['axes.unicode_minus']=False
y1=[-0.032,-0.020,0.022,0.052,0.056,0.020,-0.002,-0.034,-0.013,0.014]
x1=['1.00','2.00','3.00','4.00','5.00','6.00','7.00','8.00','9.00','10.00']
plt.plot(x1,y1,'o--',alpha=0.7)
for a,b in zip(x1,y1):
    plt.text(a,b,str(b),ha='center',va='bottom')
plt.xlabel('改装表读数/mA')
plt.ylabel('校准值ΔI/mA')
plt.title('校准值')
plt.legend()
plt.show()