from turtle import color, title
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.stats import skewnorm

numValues = 1000000
maxValue = 100
skewness = 5   #Negative values are left skewed, positive values are right skewed.

data = skewnorm.rvs(a = skewness,loc=maxValue, size=numValues)  #Skewnorm function

data = data - min(data)      #Shift the set so the minimum value is equal to zero.
data = data / max(data)      #Standadize all the vlues between 0 and 1. 
data = data * maxValue   

print('mean of the data is ',np.mean(data) )
print('Std of the data is ',np.std(data) )
mean_data = np.mean(data)
print('mean of data =',np.mean(data))
means=[]
def update_hist(num, data):
    plt.cla()
    sample = np.random.choice(data, size=500, replace=False, p=None)
        #find mean of sample
    #print(len(means),np.mean(means))
    print(len(means),'mean of the data is ',np.mean(means),'Std of the data is ',np.std(means)/np.sqrt(len(means)) )
    mean = np.mean(sample)
    means.append(mean)
    mean_mean = np.mean(means)
    #plt.text(-5, 60, 'Parabola $Y = x^2$', fontsize = 22)

    plt.title('Distribution of means of Data Sampled '+ str(len(means))+ ' times')
    plt.hist(means,color='dodgerblue')
    #plt.hist(means,density=True,color='dodgerblue')
    #plt.hist(data,density=True)
    
    plt.axvline(x=mean_data, linewidth=.5, label= 'Mean of Data',color='red')
    plt.axvline(x=mean_mean, linewidth=.5, label= 'Mean of Means',color='blue')

    # Add label

    plt.legend(loc = 'upper left')

fig = plt.figure()
hist = plt.hist(data[0])

animation = animation.FuncAnimation(fig, update_hist,  frames = 200, fargs=(data, ) )
animation.save('meanofmeans.gif',
		 fps = 5)
#plt.show()
#print(data)
print('mean of the data is ',np.mean(means),'Std of the data is ',np.std(means)/np.sqrt(len(means)) )
