import matplotlib.pyplot as plt
import pandas as pd

def plot_shower(t1,V1,a,t2=0,V2=0):
    if a==0:
        'plot of the total time trace-figure divided by the gain'
        # plotting the points 
        plt.plot(t1,V1)
      
        # naming the x axis
        plt.xlabel('time[s]')
        # naming the y axis
        plt.ylabel('Current [A]')
      
        # giving a title to my graph


        plt.title('total time trace')
      
    # function to show the plot
        plt.show()
        
        'now we reinitialize the V and t variables with the choosen time range'





        'plot of the noise trace'
        # plotting the points 
        plt.plot(t2,V2)
      
        # naming the x axis
        plt.xlabel('time[s]')
        # naming the y axis
        plt.ylabel('Current [A]')
      
        # giving a title to my graph
        plt.title('noise trace')
      
        # function to show the plot
        plt.show()
        
    elif a==1:
        
        'plot of the choosen partial time trace-figure divided by the gain'
        # plotting the points 
        plt.plot(t1,V1)
        # naming the x axis
        plt.xlabel('time[s]')
        # naming the y axis
        plt.ylabel('Current [A]')

        # giving a title to my graph
        plt.title('your choosen partial time trace')

        # function to show the plot
        plt.show()
    
    elif a==2:
        
        'plot of the extracted peaks through height constraint'
        # plotting the points 
        plt.plot(t1,V1)
        # naming the x axis
        plt.xlabel('time[s]')
        # naming the y axis
        plt.ylabel('Current [A]')

        # giving a title to my graph
        plt.title('extracted peaks thorugh height constraint')

        # function to show the plot
        plt.show()
        
    elif a==3:
        
        'plot of the extracted peaks through time constraint'
        # plotting the points 
        plt.plot(t1,V1)
        # naming the x axis
        plt.xlabel('time[s]')
        # naming the y axis
        plt.ylabel('Current [A]')

        # giving a title to my graph
        plt.title('extracted peaks thorugh time constraint')

        # function to show the plot
        plt.show()
        
    elif a==4:
         'plot of the levelled peaks '
         # plotting the points 
         plt.plot(t1,V1)
  
         # naming the x axis
         plt.xlabel('time[s]')
         # naming the y axis
         plt.ylabel('Current [A]')
  
         # giving a title to my graph


         plt.title('integrated peaks')
  
         # function to show the plot
         plt.show()
        
         plt.hist(V2)
         # naming the x axis
         plt.xlabel('diameter [m]')
         plt.ylabel('Counts')
         plt.title('diameter distribution')
         plt.show()
        
        
        

    return 0