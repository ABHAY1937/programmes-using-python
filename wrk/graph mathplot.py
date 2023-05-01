import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5])
plt.ylabel("numbers")
plt.show()
#2formatting the style of your plot
plt.plot([1,2,3,4],[1,4,9,16])
plt.plot([1,2,3,4],[1,4,9,16],"ro")
plt.axis([0,6,0,20])
plt.show()
#3plotting several lines
import numpy as np
#evenly sampled time at 200ms intervals
t=np.arange(0.,5.,0.2)
#red dashes,blue squres and green triangles
plt.plot(t,t,'r--', t,t**2,'bs',t,t**3,'g^')
plt.show()

#4 plotting with keyword string
data={'a':np.arange(50),
      'c':np.random.randint(0,50,50),
      'd':np.random.randn(50)}
data['b']=data['a'] + 10 * np.random.randn(50)
data['d']= np.abs(data['d']) * 100
plt.scatter('a','b',c='c',s='d',data=data)
plt.xlabel('entry a')
plt.xlabel('entry b')
plt.show()

#4 plotting with categorical variables
names=['group_a','group_b','group_c']
values= [1,10,100]
plt.figure(figsize=(9,3))
plt.subplot(131)
plt.bar(names,values)
plt.subplot(132)
plt.scatter(names,values)
plt.subplot(133)
plt.plot(names,values)
plt.suptitle('categorical plotting')
plt.show()