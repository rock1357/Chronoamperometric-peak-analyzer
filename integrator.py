import math 
import numpy as np
import plot_shower as ps
integrated_peaks=0;
std_line2=0;

def integrator_function(n11,n22,peak_n,noise,time_constraint,t_plot,V_plot):
    
    print('***^^INTEGRATOR METHOD STARTS^^***')
    t_int=[0]*len(V_plot)
    V_int=[0]*len(V_plot)
    integrated_peaks=0
    q0=[0]*peak_n
    d_NP=[0]*peak_n
    
    'step 5.0: the first for-loop is iterated up to the number of extracted'
    #answer=str(input('-Do you want to calculate the diameters? \n You should know the density and \n the atom/molecular weight!'))
    answer='y';
    
    for m in range(0,len(n11)):
        
        'step 5.1: to be sure that we integrate the wanted peaks (that survive to height and time conditions) we make the same constraint if-conditions in one sentence'
        
        if (min(V_plot[n11[m]:n22[m]+1])<-noise or max(V_plot[n11[m]:n22[m]+1]))>noise and -t_plot[n11[m]]+t_plot[n22[m]]>time_constraint:
            
            for mm in range(n11[m],n22[m]+1):
                'step 5.2: when the if condition is passed, save the peak'
                
                
                #std_line2[mm]=float(noise)
            
            
                
                

                t_int[mm]=t_plot[mm]
                V_int[mm]=V_plot[mm]
                
                if mm==n22[m]:
                    'step 5.3: integrate the peak that passed the if condition when the last point was saved'
                    integrated_peaks=integrated_peaks+1;
                    q0[integrated_peaks-1]=abs(np.trapz(V_int[n11[m]:n22[m]+1],t_int[n11[m]:n22[m]+1]))
            
            
                    
           
                    
                
    
    'step 5.4: if you know the density and the molecular weitght of the element constituting the NPs you can calculate their diameter'
    rho=10490; 'denisty of the Ag'
    molecular_weight=1.79119e-25;
    e_charge=1.6022e-19;
    if  answer=='y':
         
         #rho= float(input('Do you know what is the density of your element constituting the NPs [kg/m^3]?'))
         
         #molecular_weight=float(input('Do you know what is the atom/molecular weight of your element constituting the NPs [kg]?'))
         for mmm in range(0, integrated_peaks):
             
             d_NP[mmm]=2*((q0[mmm]/e_charge*molecular_weight/rho)/(4/3*math.pi))**(1/3)
    
                    
    for i in range(0,len(t_int)):
        'if the array has some zero values, then substitute them with nan value'
        
        if V_int==0:
            
            t_int[i]=np.nan
            V_int[i]=np.nan
        
    assert peak_n-integrated_peaks>=0
    
    if time_constraint==0:
        
        assert peak_n-integrated_peaks==0
                    
    #breakpoint()
    
    'step 5.5: plot the plot of integrated peaks and the histogram of the diameter distribution'
    ps.plot_shower(t_plot,V_plot,4,0,d_NP)
    
    print('***^^ INTEGRATOR METHOD ENDS^^***')
    
    'step 5.6: return the following data'
    
    return [n11,n22,peak_n,noise,time_constraint,t_plot,V_plot,peak_n,n11,n22,q0,d_NP]

                  

    
