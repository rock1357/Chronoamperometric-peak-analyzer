import numpy as np
import plot_shower as pls
import negative_scanner_2 as ns
import positive_scanner_2 as ps






def parameter_setter_2(t,V,tn,Vn):
    
    
    print('***^^HERE START THE PARAMETER SETTING STEP: choose your parameters^^***\n')
   
    '----step 2.1: if you used an amplification step, write the gain used----'
    gain=1
    print('-the gain is automatically set as: ', gain, ['Ampere/Volt'])
        
   
    

    #if test==0:
        
        #gain=float(input('A) Did you use an amplification? Set the gain used in the experiment, otherwise write 1 : '))
       


    std=np.std(Vn/float(gain))
    print('-the standard deviation value is: ',std)


    


    '----step 2.2: some usefull info: for example calculation of the total duration of the chronoamperometric trace or the sampling frequency, the total number of point'

    T=(t[1]-t[0]); 'inverse of the sampling frequency'
    Fs=(t[1]-t[0])**-1;'sampling frequency'
    
    print("-you used a sampling frequency:",round(Fs),'[Hz]')

    N=len(t); 'number of points of the recording' 
    print('-number of points of the trace:',N)

    duration=N*T;
    print('-the total duration of the trace is: ',duration,'[s]')
    
    '''----step 2.3: once introduced the chronoamperometric recording with name t and V here we can make the user to 
    choose the range of data to be scanned '''
    
    time_interval1= 0.5;
    time_interval2= 0.501;

    print('-your starting time was automatically set as: ', time_interval1,'[s]')
    print('-your ending time was automatically set as: ', time_interval2,'[s]')
    print('-your time range is:' , time_interval2,'[s]','-',time_interval1,'[s]','that is',time_interval2-time_interval1,'[s]')
    
    #if test==0:
        #y=str(input('B) Do you want to use a portion of the chronoamperometric measure (set:1) \n   or the whole measure (set:2) : '))
        #if y=='1':
            #[time_interval1,time_interval2]=[float(input('enter the initial time you want the scanner to start:t_i=')),float(input('enter the final time you want the scanner to finish:t_i='))]
        #else:
    time_interval1= 0.5;
    time_interval2= 0.51;
            

    'reconverting the seconds in number of points we can extract the part of the trace'
    n1=round(time_interval1/T)
    n2=round(time_interval2/T)
   
    
    #assert n1<n2, 'n1 should be always lower than n2'
    #assert n2<=round(N), 'n2 should be always lower than N=lent(t)'
        
    #assert round(duration)==round(abs(t[len(t)-1]-t[0])), 'duration=len(t)*T and t(end)-t(0) should be equals '
    
    
    V=V/gain;
    Vr=V[n1:n2];'Vr=V-reduced and tr=///'
    tr=t[n1:n2];
    Vn=Vn/gain;

    'step 2.4: plot the graphs of the complete and reduced chronoamperometric experiment'
    

    pls.plot_shower(tr,Vr,1)
    
    '''Here we give the default initializations to the parameters usefull to set the
       minimum height for peak extraction. '''
       
    k_factor_n=-1;'min(Vn)/(std)'
    k_factor_p=1;'max(Vn)/(std)'
    n_noise=k_factor_n*std
    p_noise=k_factor_p*std
    time_constraint=0.0005
    

    'step 2.5: tell if you want to scan the negative or positive part of the trace'
    
    #if test==0:
        #choice=input('C) Do you have peaks on negative [n] or positive [p] side of the trace? ')
  
    
    #else:
    choice='n'
        

    if choice=='n':
        #if test==0:
         #   print('-the min value of the noise trace is negatively bigger \n than the standard deviation value of about: ',k_factor_n)

          #  k_factor_n=-float(input('C.1) Choose the multiplication (=k) factor for the peak extraction above the std level: '))
           # time_constraint=float(input('C.2) Choose the time constraint for peaks extraction (otherwise write 0): '))
            #n_noise=k_factor_n*std
            #print('-your noise level is k*std(V_noise) that is :',n_noise,'since you set k=',k_factor_n)
            #print('-the time constraint is 0 by default (test=1)')


        'call negative scanning function'
        n_noise=k_factor_n*std
        print('-your noise level is k*std(V_noise) that is :',n_noise,'since you set k=',k_factor_n)
        print('-the time constraint is 0 by default (test=1)')
        print('\n***^^ENDING THE PARAMETER SETTING STEP^^*** \n')
        print('*)reduced trace plotted \n')
        [nan_points,l,peak_n,save_ending_parameter,save_starting_parameter,shared_points,points_nth_peak,points_nth_peak_nan,points_nth_peak1,ssp,sep,peak_n,noise,time_constraint,t_peak,V_peak,t_plot,V_plot,t_plot,V_plot,peak_n,n11,n22,peak_n,noise,time_constraint,t_plot,V_plot,peak_n,n11,n22,q0,d_NP]=ns.negative_scanner_2(tr,Vr,-n_noise,time_constraint)
        
        
    else:
        #if test==0: 
            #print('the min value of the noise is positively bigger than the standard deviation value of about:',k_factor_p)

            #k_factor_p=float(input('C.1) Choose the multiplication factor for the peak extraction above the std level:'))
            #time_constraint=float(input('C.2) Choose the time constraint for peaks extraction (otherwise write 0): '))
            #p_noise=k_factor_p*std
            #print('-your noise level is k*std(V_noise) that is :',p_noise,'since you set k=',k_factor_p)
            #print('-the time constraint is 0 by default (test=1)')
        'call positive scanning function'
        p_noise=k_factor_p*std
        print('-your noise level is k*std(V_noise) that is :',p_noise,'since you set k=',k_factor_n)
        print('-the time constraint is 0 by default (test=1)')
        print('\n***^^ENDING THE PARAMETER SETTING STEP^^*** \n')
        print('*)reduced trace plotted \n')
        [nan_points,l,peak_n,save_ending_parameter,save_starting_parameter,shared_points,points_nth_peak,points_nth_peak_nan,points_nth_peak1,ssp,sep,peak_n,noise,time_constraint,t_peak,V_peak,t_plot,V_plot,t_plot,V_plot,peak_n,n11,n22,peak_n,noise,time_constraint,t_plot,V_plot,peak_n,n11,n22,q0,d_NP]=ps.positive_scanner_2(tr,Vr,p_noise,time_constraint)
        

    
    return [n1,n2,duration,N,nan_points,l,peak_n,save_ending_parameter,save_starting_parameter,shared_points,points_nth_peak,points_nth_peak_nan,points_nth_peak1,ssp,sep,peak_n,noise,time_constraint,t_peak,V_peak,t_plot,V_plot,t_plot,V_plot,peak_n,n11,n22,peak_n,noise,time_constraint,t_plot,V_plot,peak_n,n11,n22,q0,d_NP]