import plot_shower as ps
import numpy as np
import integrator as intg

def peak_levelling(ssp,sep,peak_n,l,noise,time_constraint,t_peak,V_peak):
    print('***^^ PEAK LEVELLING METHOD STARTS^^***\n')
    
    
    selected_peaks=0
    t_plot=[0]*l
    V_plot=[0]*l
    Delta_t=[0]*peak_n
    
   
    points_nth_peak=[0]*peak_n
    points_nth_peak1=[0]*peak_n
    points_nth_peak_nan=[0]*peak_n
    

 
    'step 4.0: for loop that goes through all the peaks extracted in the previous module'
    for i in range(0,peak_n):
        points_nth_peak[i]=sep[i]-ssp[i]+1;
        
                

        
        Delta_t[i]=float(t_peak[sep[i]])-float(t_peak[ssp[i]]);'time distance of the peaks'
        
        
        if Delta_t[i]>=time_constraint: 
            'step 4.1.0: when the time constraint is true it means the peak has a size t(end_peak)-t(start_peak)>time_constraint'    
        
        
            selected_peaks=selected_peaks+1;'variable that increases when the if condition is true in order to count newly the number of surviving peaks to the time constraint'
            points_nth_peak1[i]=sep[i]-ssp[i]+1;'save the number of point constituting the current peak'
            
            
            #if V_plot[ssp[i]] is np.nan:
                #print(i,' the first point of this peak is nan')
                #points_nth_peak_nan[i-1]=points_nth_peak_nan[i]-1
                
            for j in range(ssp[i],sep[i]+1):
                'step 4.1.1: save the points'
                
                

                t_plot[j]=t_peak[j]; 'save the t points of the correpondent peak survived to the time constraint'
                V_plot[j]=V_peak[j]; 'same thing as the previous'
                
                ' if this is the last point of the peak save the current t and substitute the current V with 1e-30 instead 0'
                if j==sep[i]:
                
                    t_plot[j]=t_peak[j] 
                    V_plot[j]=1e-30
                    
                    ' do the same for the first peak point'
                    t_plot[ssp[i]]=t_peak[ssp[i]]
                    V_plot[ssp[i]]=1e-30
                    assert V_plot[ssp[i]]==V_plot[sep[i]], 'the first and last point of the current peak must be equals'
                
                    
                    
        else :
            'step 4.2.0: if the peak does not pass the time constraint if condition, then change its points as nan and count the number of such points'
            points_nth_peak_nan[i]=sep[i]-ssp[i]+1;
            
            if ssp[i] is sep[i-1]:
                 
                 'step 4.2.1: if the peak has a common point with the previous one (survived to the time constraint) skip to erase this common point'
                 for j in range(ssp[i]+1,sep[i]+1):
                     t_plot[j]=np.nan
                     V_plot[j]=np.nan
                     
                 assert V_plot[ssp[i]+1] is V_plot[sep[i]], 'at the end of the for-loop we must be sure that the nan of the second point is the same as the ending one'
                 
                 
            else:
                'step 4.2.2: if the previous if is not true then do not skip the first peak point'
            
                
                for j in range(ssp[i],sep[i]+1):
                    t_plot[j]=np.nan
                    V_plot[j]=np.nan
                assert V_plot[ssp[i]] is V_plot[sep[i]]
        
        
               
            
        
                
    for i in range(0,l):
        'step 4.3: when all the first for-loop is terminated all the 0 values of the initialized vectors t_plot=[0]*l (l=len(t_peak) should be changed to nan to not be plotted)'
        
        if V_plot[i]==0:
            t_plot[i]=np.nan
            V_plot[i]=np.nan
    
            
               
    
       
    'step 4.4: plot the result'
    ps.plot_shower(t_plot,V_plot,3)
    
    
    print('-The number of peaks surviving to the ime_constraint condition are:',selected_peaks)
    print('\n***^^PEAK LEVELLING METHOD ENDS^^***\n')


    #assert sum(points_nth_peak)-sum(points_nth_peak1)==sum(points_nth_peak_nan),'simple rule to be sure that the method made its job as we want it does'
    
    [n11,n22,peak_n,noise,time_constraint,t_plot,V_plot,peak_n,n11,n22,q0,d_NP]=intg.integrator_function(ssp,sep,peak_n,noise,time_constraint,t_plot,V_plot)
    
    return [points_nth_peak_nan,points_nth_peak1,ssp,sep,peak_n,noise,time_constraint,t_peak,V_peak,t_plot,V_plot,t_plot,V_plot,peak_n,n11,n22,peak_n,noise,time_constraint,t_plot,V_plot,peak_n,n11,n22,q0,d_NP]
