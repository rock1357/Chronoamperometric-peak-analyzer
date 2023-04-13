import numpy as np
import parameter_setter_2 as ps
import plot_shower as pls

q=0
nan_points=0



    


c=10;'c=number of row to skip in the acqusition files'
print('-the number of columns to skip was automatically set to:',c)
delimiter_=','; ' delimiter= symbol between the [time,Voltage/current] columns'
print('-the delimiter of your file was automatically set as:',delimiter_)
filename_acquisition='electrode2-gain10-Fs10k-nofilter-bias-500mV-dark.csv';' filename_acquisition=name of the experiment file where NPs are stimulated to oxidize/reduce'
print('-the file-name of your chronoamperometric experiment is:',filename_acquisition)
filename_noise='electrode2-gain10-Fs10k-nofilter-bias-500mV-dark.csv'; 'filename_noise= name of the file where only noise is recorded in order to extract the standard deviation'
print('-the file-name of your noise registration is:',filename_noise,'\n')





'--------------------------------------------------------------------------------------------'





'step 1.0: asking for the file-name of the NPs experiment and for the recording of the noise trace coming from the electrode'
    
filename_acquisition=str(input('A) put the file name of the acqusition: ')) 
    #filename_noise=str(input('B) put the file-name of the noise acquisition: '))
    #delimiter_=str(input('C) insert the kind of delimiter between time and current data columns in the data file ( , or ; ) : '))
    #c=int(input('E) select how many rows to skip in your csv file before float numbers of the chronoameprometric \n   registration start: '));




   



'step 1.2: extracting the data as float numbers'

print('PROCESSING: importing the data of your recorded chronoamperometric experiment...')
data = np.genfromtxt(filename_acquisition, delimiter=delimiter_,skip_header=c)
    
print('PROCESSING: importing the data of your recorded noise (no bias)... \n')
data2 = np.genfromtxt(filename_noise, delimiter=delimiter_,skip_header=c)



    


'step 1.3: calling the data as t and V for the experiment and tn and Vn for the noise acquisition'

t=data[:,0]
V=data[:,1]

tn= data2[:,0]
Vn= data2[:,1]










print('***^^ENDING PYTHON CHRONOAMPEROMETRIC txt/csv DATA IMPORTER:(PROGRAMMER MODE: test=1)^^*** \n')
    
print('*)noise and experiment traces plotted \n')

#pls.plot_shower(t,V,0,tn,Vn)

    
    
    


 


'----------------------------------------------------------------------------------------------------'
def test_be_sure_your_file_are_txt_or_csv():
    assert 'csv' or 'txt' in filename_acquisition
    assert 'csv' or 'txt' in filename_noise

def test_extracted_data_should_be_time_and_volt_or_amp_so_2xN_dimension():
       assert np.size(data, 1)==2;'make sure the array contains 2 columns: time and Volt/Ampere'
       assert np.size(data2, 1)==2;'make sure the array contains 2 columns: time and Volt/Ampere'

def test_the_length():
       assert len(t)==len(V)
       assert len(tn)==len(Vn)

'testing if the data are read as float numbers'

def test_extracted_data_are_float():
    for i in range(0,len(t)):
           
           assert type(t[i])==np.float64
           assert type(V[i])==type(t[i])

    for i in range(0,len(tn)):
           assert type(tn[i])==np.float64
           assert type(Vn[i])==type(tn[i])
           assert tn[i]!=np.nan
           assert Vn[i]!=np.nan
       
def test_data_are_not_nan():
           
   for i in range(0,len(t)):
               assert t[i]!=np.nan
               assert V[i]!=np.nan
   

   for i in range(0,len(tn)):
           assert tn[i]!=np.nan
           assert Vn[i]!=np.nan
           
           
'------------------------------------------------------------------------------------------------------'           
           
[n1,n2,duration,N,nan_points,l,peak_n,save_ending_parameter,save_starting_parameter,shared_points,points_nth_peak,points_nth_peak_nan,points_nth_peak1,ssp,sep,peak_n,noise,time_constraint,t_peak,V_peak,t_plot,V_plot,t_plot,V_plot,peak_n,n11,n22,peak_n,noise,time_constraint,t_plot,V_plot,peak_n,n11,n22,q0,d_NP]=ps.parameter_setter_2(t,V,tn,Vn)

'------------------------------------------------------------------------------------------------------'

def test_param_setter_2():
    
    assert n1<n2, 'n1 should be always lower than n2'
    assert n2<=round(N), 'n2 should be always lower than N=lent(t)'
        
    assert round(duration)==round(abs(t[len(t)-1]-t[0])), 'duration=len(t)*T and t(end)-t(0) should be equals '
    
'------------------------------------------------------------------------------------------------------'
def test_positive_scanner_2():
    
    for i in range(0,l):
         nan_points=0
         if V_peak[i]==0 and t_peak[i]==0:
             
             nan_points=nan_points+1
             t_peak[i]=np.nan
             V_peak[i]=np.nan
             
             if i ==l-1:
                 
                 assert l-nan_points==sum(points_nth_peak)-shared_points+1 or l-nan_points==sum(points_nth_peak)-shared_points ,'the number of the points of the extracted peaks \n should be equal to the number of the \n total point - the number of the ones converted in nan'
                 break

    for i in range(0,peak_n):
        
        assert len(V[save_starting_parameter[i]:save_ending_parameter[i]])+1==points_nth_peak[i], 'the number of points between the starting and ending  parameters should be equal to the number of points under the correspondent peak'
        
    for i in range(0,l):
        
        assert type(t_peak[i])==float ,'these numbers should be all float'
        assert type(V_peak[i])==float ,'these numbers should be all float'
            
        
    assert len(t_peak)==len(V_peak), 'obviously they should have same length'
    '----------------------------------------------------------------------------------------------------'
    
def test_peak_levelling():
    assert sum(points_nth_peak)-sum(points_nth_peak1)==sum(points_nth_peak_nan),'simple rule to be sure that the method made its job as we want it does'