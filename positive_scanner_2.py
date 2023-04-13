import plot_shower as ps
import numpy as np
import peak_levelling as pl


    

def positive_scanner_2(t,V,noise,time_constraint):
    '''define the variables used for the negative peak extraction'''
    l=len(t)
    peak_n=0    
    points_nth_peak=[0]*l
    w_parameter=0
    first_while_parameter=0
    second_while_parameter=0
    save_starting_parameter=[0]*l
    save_ending_parameter=[0]*l
    t_peak=[0]*l
    V_peak=[0]*l
    shared_points=0
    
    
    print('***^^ START POSITIVE SCANNER METHOD ^^*** \n')
    
    
    """step 3.0: the firsts and lasts points of the voltage must be positive to avoid an incomplete extraction of the 
     peaks, so the next for-loops allow to change to 0 the voltage values at the onset and at the ending of the trace"""
    
    
    if l<50 :
        print("WARNING:too few points")
        return 0
    
    
    for s in range(0,l):
        
        
        if s==0 and V[0]>0:
            j=0
            
            while V[j]>0:
                j=j+1
                V[j-1]=0
                t[j-1]=0
                if V[j]<0:
                    print('-In order to avoid incomplete peak extraction \n at the left side fo the boundaries, \n we made the scanner to skip the firsts:',j,'points')
                    s=j
                    break
        #assert V[:s].all()==0
        
   
        if s==l-1 and V[s]>0:
            j=s
            while V[j]>0:
                
                j=j-1
                V[j+1]=0
                t[j+1]=0 # correction
                if V[j]<0:
                    
                    print('-In order to avoid incomplete peak extraction \n at the right side of the boundaries, \n we made the scanner to skip the lasts:',l-j,'points')
                    s=j-1
                    break
            #assert V[s:l-1].all()==0
         

    
        
            
            
    '''step 3.1: the first while serves to go through all the values of V and t-> 
       it is always true up to l-2->Here "l-2" is enhanced for a last time, becoming "l-1" 
       that is the last value for V and t, since l starts from 0'''
    
    while w_parameter<=l-2:
        
        
        w_parameter=w_parameter+1; 'it means w_parameter starts from 1'
        
        
        '''if a negative peak is found to be lower than -k*std(data) start the
        peak recording '''   
        
        if V[w_parameter-1] >noise:
            
            'note w_parameter is re-set to 0 at the first cycle'
            peak_n=peak_n+1;'varaiable to count the number of peaks determined from the activation of the if condition: here we would skip the peak_n=0'

            first_while_parameter=w_parameter; ''' the first while parameter serves for the
                             % second while parameter-(w.p) (see below)'''
            #breakpoint()
            
            save_starting_parameter[peak_n-1]=first_while_parameter-1;'save the number of the starting t value of the peak for next integration function: here we make the first save_ending_parameter[peak_n-1] to start from the 0 position because peak_n=1 at the onset!'
            if w_parameter==l-1 :
                print('-the total number of extracted peaks is:',peak_n)
            
            
            
            while 1:
                
                '''step 3.2: if the peak overcome the 'noise=k*std' value, then go backward to the point
                where V>0-> this define the starting point of the peaks'''
                
                 
        
                first_while_parameter=first_while_parameter-1; 'decrease the first w.p.'
        
        
                #if first_while_parameter<1:
                    
                 #   ' if the condition is already true at the onset of the loop, then break the while loop'
                  #  print('N.B]The first V value is already >0')
                    
                   # V_peak[first_while_parameter]=float(V[first_while_parameter]);
                    #t_peak[first_while_parameter]=float(t[first_while_parameter]);
                    #first_while_parameter=first_while_parameter+1;
                    #break; 'go to the second while in order to save the points of the selected peak in a new array'
                    #'N.B) this condition should not be activated anymore, since we implemented the first two for loops at the onset, but is usefull to not erase in order to make the scope of these latter more clear'
    
                if V[first_while_parameter]<0 :
                    
                    'continue untill V<=0 and control if the ending point of the previous extracted peak is the same as the starting point of the current one'
        
                    save_starting_parameter[peak_n-1]=first_while_parameter; 'save the starting point of the n-th peak'
                    if (save_ending_parameter[peak_n-2]) == (save_starting_parameter[peak_n-1]):
                        shared_points=shared_points+1
                    break
        
                    
                    
                    
                
                
             
        

            second_while_parameter=first_while_parameter;'% the second while parameter should start from the last value of the first while p.'
        
           
            while 2:
                
                '''step 3.3: once reached the V>0 at the left, continue up to the V>0 at the right in order to close the peak'''
                
                
                if second_while_parameter==l-1 :
                    print('last cycle')
                   
                
                
                t_peak[second_while_parameter]=float(t[second_while_parameter]);'record t_points of the peak'
                V_peak[second_while_parameter]=float(V[second_while_parameter]);'record the V point of the peak'
            
            
                second_while_parameter=second_while_parameter+1;'increase the second wp'
                

               
         
              
                ''' with the last if condition we terminate the selection of the negative 
                    peak defined as the peak that overcome the V=0 line for two
                    different t, having the max height higher than k*std '''
                if V[second_while_parameter]<=0:
                    

                    'make a condition for the last peak point'
               
                    t_peak[second_while_parameter]=float(t[second_while_parameter]); 'save the last peak point before exit from the while loop'
                    V_peak[second_while_parameter]=float(V[second_while_parameter]); '//////////same/////'
                
                    'now we save the last number of the t and V arrays where the last if condition was true'
                    save_ending_parameter[peak_n-1]=second_while_parameter;
                    
                    'counts the n.of point constituting the peak: the "+1" one serves to account for the 0: if sep=3 and ssp=1 it is sep-ssp=2 but actually the points are V(1=ssp),V(2),V(3=sep)'
                    points_nth_peak[peak_n-1]=save_ending_parameter[peak_n-1]-save_starting_parameter[peak_n-1]+1;
               
                    break
                  
            
                
            
            
            
        
            w_parameter=second_while_parameter; 'with this the first while can re-start from the last point extracted skipping all the ones inside the last peak'
            
    nan_points=0
            
    'step 3.5: at the last while iteration tell me the number of the extracted peaks '
       
    if w_parameter==l-1 :
        print('-the total number of extracted peaks is:',peak_n)
        print('\n***^^ END POSITIVE SCANNER METHOD ^^*** \n')
        
    
    
    '''reinitialize the tr=trestricted and Vr=Vrestricted with the precessed variable by the ns method'''
    for i in range(0,l):
             
         if V_peak[i]==0 and t_peak[i]==0:
             nan_points=nan_points+1
             t_peak[i]=np.nan
             V_peak[i]=np.nan
             
             if i ==l-1:
                 
                 #assert l-nan_points==sum(points_nth_peak)-shared_points+1 or l-nan_points==sum(points_nth_peak)-shared_points ,'the number of the points of the extracted peaks \n should be equal to the number of the \n total point - the number of the ones converted in nan'; 'problem here'
                 break

    #for i in range(0,peak_n):
        
        #assert len(V[save_starting_parameter[i]:save_ending_parameter[i]])+1==points_nth_peak[i], 'the number of points between the starting and ending  parameters should be equal to the number of points under the correspondent peak'
        
    #for i in range(0,l):
        
       #assert type(t_peak[i])==float ,'these numbers should be all float'
       #assert type(V_peak[i])==float ,'these numbers should be all float'
            
        
    #assert len(t_peak)==len(V_peak), 'obviously they should have same length'
         
        
    
 
    ps.plot_shower(t_peak,V_peak,2);'calling the plot shower function for the plotting the ecxtracted peaks'
    
   
    
    
    [points_nth_peak_nan,points_nth_peak1,ssp,sep,peak_n,noise,time_constraint,t_peak,V_peak,t_plot,V_plot,t_plot,V_plot,peak_n,n11,n22,peak_n,noise,time_constraint,t_plot,V_plot,peak_n,n11,n22,q0,d_NP]=pl.peak_levelling(save_starting_parameter,save_ending_parameter,peak_n,l,noise,time_constraint,t_peak,V_peak)
    
  
        
    return [nan_points,l,peak_n,save_ending_parameter,save_starting_parameter,shared_points,points_nth_peak,points_nth_peak_nan,points_nth_peak1,ssp,sep,peak_n,noise,time_constraint,t_peak,V_peak,t_plot,V_plot,t_plot,V_plot,peak_n,n11,n22,peak_n,noise,time_constraint,t_plot,V_plot,peak_n,n11,n22,q0,d_NP]
