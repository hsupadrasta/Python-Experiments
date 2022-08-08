from turtle import color, title
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
skip_print = True
def print_it(string):
    if not skip_print:
        print(string)


number_of_frames = range(200)

data = np.random.randint(100,size= 500000)
print_it(data)
print_it('mean of the data is ',np.mean(data) )
print_it('Std of the data is ',np.std(data) )
mean_data = np.mean(data)
print_it('mean of data =',np.mean(data))
means=[]
def update_hist(num, data):
    plt.cla()
    sample = np.random.choice(data, size=500, replace=False, p=None)
        #find mean of sample
    #print_it(len(means),np.mean(means))
    print_it(len(means),'mean of the data is ',np.mean(means),'Std of the data is ',np.std(means)/np.sqrt(len(means)) )
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
animation.save('\\meanofmeans.gif',
		 fps = 5)
#plt.show()
#print_it(data)
print_it('mean of the data is ',np.mean(means),'Std of the data is ',np.std(means)/np.sqrt(len(means)) )
