# Chronoamperometric-peak-analyzer
# what is it?
This program is made in order to select and integrate the peaks present in a chronoamperometric time trace; 
the chronoamperometric time trace is a trace that show the current peaks related with the impact of nanoparticles (in water solution) against the working electrode. 
The oxidation/reduction of such NPs, as consequence of the impact, is stimulated by the presence of: a) chathalist molecules b) bias use. 
Then the goal is to make a software able to extract the peaks that are more probable to be realted to NPs discharge processes and not to the background noise. This aim is reached by the program that we are going to present.
Below there is an example of the circuit with which we can be able to obtain the chronoamperometric trace.
We can use a two electrode set-up; it can be approximated as a capacitance in parallel to a resistor. Next to this latter ther can be an amplifier of the signal (in this case a femto-current aplifier DPLCA-200 model).
At the and there is the representation of a data acquier (as the lock in amplfier or an analog digilent data reciever).


<img width="452" alt="image" src="https://user-images.githubusercontent.com/61994200/231841919-1734833c-708c-405d-bc65-1dd0432f0b97.png">


# How does it works?

Before to play the program we must have written: 

a) In the data_extractor.py module you have to put the data-file in order to extract the chronoamperometric data and initialize some parameters as: 


a.1) c=number of row to skip in the acqusition files (integer) -> line 13 (ex: c=10)


a.2)' delimiter= symbol between the time data and Voltage/current data columns'-> line 15  (ex: delimiter=';')


a.3) filename_acquisition=name of the experiment chronoamperometric registration file where NPs were stimulated to oxidize/reduce->line 17 


a.4) filename_noise= name of the file where only noise is recorded-> we can know the standard deviation of the noise at the electrode-> line 19 

b) In the parameter_setter.py module we have to set: 

b.1) The gain of the eventual amplification step in order to bring the data to the real dimension unit->line 16. 

b.2) The time interval of the part of the total trace we want to analyze (it is possible to select the whole trace by putting t1=0 and t2=duration)-> lines 51 and 52. 

b.3) The k factor (for positive or negative analysis) is a parameter that will be multiplied for the standard deviation value of the noise trace; this value (called noise=k*std(V_noise)) will be used as noise delimiting level for the height constraint->line 91 and 92 

b.4) The time constraint for peak selection. b.5) The desire if we want to scan the positive (V>0 side) or the negative (V<0) part of the trace.


# main features
With this tool is possible:
1) to use the noise time trace in order to set a maximum level of the noise peaks. This is made by calculating the standard deviation of the noise distribution.
2) to
