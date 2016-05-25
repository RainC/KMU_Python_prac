import matplotlib.pyplot as plt

labels = ['Java', 'C/C++' ,'Python', 'Javascript']
sizes = [35,30,25,50]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0,0,0.1,0)

plt.pie(sizes, explode = explode , labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=90)

plt.axis('equal')
plt.show()
