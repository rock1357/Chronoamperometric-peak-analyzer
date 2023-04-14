# Chronoamperometric-peak-analyzer
# what is it?
This program is made in order to select and integrate the peaks present in a chronoamperometric time trace; 
the chronoamperometric time trace is a trace that show the current peaks related with the impact of nanoparticles (in water solution) against the working electrode. 
The oxidation/reduction of such NPs, as consequence of the impact, is stimulated by the presence of: a) chathalist molecules b) bias use c) Stimulation by light (if in the case of organic nanoparticles). 
Then the goal is to make a software able to extract the peaks that are more probable to be realted to NPs discharge processes and not to the background noise.
For this aim is advisable to relize at least two chronoamperometric recording in which we measure just the background noise (coming from the solution itself) in the first registration, and the nanoparticle impacts in the second (after having injected them in the solution).
Nevertheless the noise measurement is not necessary for the analyzer.
If the noise time trace is taken, the analyzer will use this information to set a level below which there is a (>60%) probability that those peaks comes from sthocastic fluctuations at microscopic level: it calculates the standard deviation of the noise.

Below there is an example of the circuit with which i was able to obtain the chronoamperometric trace.
We can use a two electrode set-up: only working and reference ones are present here; This circuit  can be approximated as a capacitance in parallel to a resistor. Next to this latter ther can be an amplifier of the signal (in this case a femto-current aplifier DPLCA-200 model), it is enclosed in the second
square.

At the and there is the representation of a data acquier (as the lock in amplfier or an analog digilent data reciever).


<img width="452" alt="image" src="https://user-images.githubusercontent.com/61994200/231841919-1734833c-708c-405d-bc65-1dd0432f0b97.png">


# How does it works?

Before to play the program we must have filled some of the parameters that will be used as values to make the analysis. It is the main module from which
all the other functions will be called, as reproduced in the following explanation order: 

a) data_extractor.py module is the first module in which you have to put the data-file in order to extract the chronoamperometric data in form of array.The data should have the .csv or .txt extension. Also you have to initialize some parameters as: 


a.1) c=number of row to skip in the acqusition files (integer) -> line 13 (ex: c=10-> in this way we make data extraction from the 10th row of the data file)


a.2)' delimiter= symbol between the time data and Voltage/current data columns'-> line 15  (ex: delimiter=';' )


a.3) filename_acquisition=name of the experiment chronoamperometric registration file where NPs were stimulated to oxidize/reduce->line 17 


a.4) filename_noise= name of the file where only noise is recorded-> we can know the standard deviation of the noise at the electrode-> line 19 

b) parameter_setter.py is the second module og the program; here we have to set: 

b.1) The gain of the eventual amplification step in order to bring the data to the real dimension unit->line 16 (ex: gain=1 if no amplification was used). 

b.2) The time interval of the part of the total trace we want to analyze (ex: it is possible to select the whole trace by putting t1=0 and t2=duration)-> lines 51 and 52. 

b.3) The k factor (for positive or negative analysis) is a parameter that will be multiplied for the standard deviation value of the noise trace; this value (called noise=k*std(V_noise)) will be used as noise delimiting level for the height constraint->line 91 and 92 

b.4) The time constraint for peak selection. b.5) The desire if we want to scan the positive (V>0 side) or the negative (V<0) part of the trace.

c) Negative/postive_scanner.py is the third module: here we don't have to select any parameter because they were almost all already written in the previous module. This module will simply apply an alghoritm where the trace is scanned, starting from the first value of V>0 up to the last value of V>0 of the whole trace. Suppose we selected to scan the negative part of the trace. When a value V<noise (noise is negative here because k_factor is set to be <0) is found, the algorithm come back to the first preceeding value V>0 and here set the starting point of that peak. Done that, it go forward up to the second V>0 ( at the right of the min value of the peak) completing the peak delimitation. In the middle all the peak points are saved in a new array. So the peaks are selected in height in this module! After the whole selected trace was scanned, the current module will invoce the negative_peak_levelling() method.

d) peak_levelling.py is the fourth module: here the peak are selected in time width and are levelled with same base level: 1e-30 will be the two minima of each extracted peak (not zero because zeros are the eliminated peaks and they become nan in order to not be plotted) 

e) integrato.py is the fifth and last module: here we conclude the peaks analysis by making an integration of the selected peaks! 
Here is important to set previously the parameters: 

-density of the element constituting the NPs 

-atomic/molecular weight of the element constituting the NPs. 

In fact it will be asked to the user if he want also to calculate the diameters of the peaks and this can be posibbile only if he knows these two quantities.

NB) between one module and the other will be activated the plot_shower() method which can plot all the graphs at the end of each process in order to make the programmer/user to be able to see the results in a pictorial way.


# main features
With this tool is possible:
1) to use the noise time trace in order to set a maximum level of the noise peaks. This is made by calculating the standard deviation of the noise distribution.
2) to extract certain specific peaks belogning to a positive or negative half of a current (or voltage) vs time or chronoamperometric measuerement; we can select them by exploiting the height constraint and the size constraint (time distance between the two minima of the peaks).
3) to know how much charge is contained in the nanoparticle discharges: an integrator under the peaks is implemented.
4) To plot the hystogram of the released charge by nanoparticles distribution.

# example

step a):


<img width="715" alt="image" src="https://user-images.githubusercontent.com/61994200/232000147-6d53e069-3707-4ef4-b6d8-5b2a2a6f3aee.png">

step b):

<img width="217" alt="image" src="https://user-images.githubusercontent.com/61994200/232100078-d6b58ce6-c595-4efe-8c7c-bb25861dc810.png">
<img width="563" alt="image" src="https://user-images.githubusercontent.com/61994200/232002494-e423187c-623e-4a63-bc8b-0e5f8e73f6b2.png">

# example

![image](https://user-images.githubusercontent.com/61994200/232003310-5eda1498-a9d5-4dfb-974d-10830f48d949.png)

![image](https://user-images.githubusercontent.com/61994200/232003379-e20edb3d-b500-47d3-a721-a94c7c66272d.png)


here you can see the starting peak is not considered even if it is higher than the minimum level ( i used 0.202, corresponding to 1*std(V)) , since i made the tool to start the anlysis from the first point that cross the 0 level. 


![image](https://user-images.githubusercontent.com/61994200/232003423-fd269078-4cf6-43ec-95ac-bcc33fb6ce56.png)

![image](https://user-images.githubusercontent.com/61994200/232003497-6aca7962-3e01-40b0-a563-a2a0e147c29d.png)

# testing the different modules
after having done a first execution we can see if everything was well done by using
<img width="260" alt="image" src="https://user-images.githubusercontent.com/61994200/232009638-36b8aa99-d059-42ca-93bb-1c5a7266746e.png">

in this way we will test:


<img width="720" alt="image" src="https://user-images.githubusercontent.com/61994200/232007943-fe0708b3-55e6-4eae-981c-018a0d87189e.png">
<img width="743" alt="image" src="https://user-images.githubusercontent.com/61994200/232008842-c743def0-e072-4159-9597-c033411f5e36.png">
<img width="733" alt="image" src="https://user-images.githubusercontent.com/61994200/232009142-013ad2a7-3bb1-4894-8b3e-8a872a92deb6.png">

and the result is
<img width="543" alt="image" src="https://user-images.githubusercontent.com/61994200/232009918-4c509a46-d294-468f-9ba7-6c6e8ab30e47.png">


