""" Dataframes will be used for simplicity""" 
import pandas as pd 

"""DATA LOCATIONS"""
MaterialDataLoc = r"C:\Users\drewo\Desktop\Programs\ENME_337\ENME_337_py\337FP\ENME337GROUP38FP\MaterialData.csv"
PipeDataLoc = r"C:\Users\drewo\Desktop\Programs\ENME_337\ENME_337_py\337FP\ENME337GROUP38FP\PipeData.csv"
avsNLoc =r"C:\Users\drewo\Desktop\Programs\ENME_337\ENME_337_py\337FP\ENME337GROUP38FP\avsN.csv"
YGraphDataLoc = r"C:\Users\drewo\Desktop\Programs\ENME_337\ENME_337_py\337FP\ENME337GROUP38FP\YGraphData.csv"

"""DATA IMPORT AND FILTER""" 
## Note for theis section .dropna() drops all rows witht the NaN value 
Materialdata = pd.read_csv(MaterialDataLoc, header=0,delimiter=",").dropna()  
Pipedata = pd.read_csv(PipeDataLoc, header=0,delimiter=",").dropna() # Raw material data 
avsN = pd.read_csv(avsNLoc,header=0,delimiter=",")
"""Special note for Ygraph data, all x,y must have the NAN values deleted becuse the data count is inconsistent""" 
YGraphData = pd.read_csv(YGraphDataLoc,header=0,delimiter=",")
#print(Materialdata)
#print(Pipedata)
#print(avsN)
#print(YGraphData)


""" Main Loop """ 
""" This main menue works off of states
These states will me 
state = "MM" (main menue)
state = "PA" (problem A)
state = "PB" (problem B)
state = "PC" (problem C)
These repersent the four main states 
""" 

LoopCtrl = True
state = "MM" ## the base state for the program is the main menue 
while LoopCtrl:
    if state == "MM": # This if statement forces the user to imput a value: 
        print("==== Main Menue ====")
        print("For Pressue Surge Analisis enter: A ")
        print("For Determination of Crack Growth Rate Material Properties enter: B")
        print("For Failure Probability Analisis enter: C")
        print("To Quit The Program enter: Q")
        MMCtrl = True
        while MMCtrl:
                inp = input(": ")
                if inp == "A" or inp == "a": 
                    state = "PA"
                    MMCtrl = False 
                elif inp == "B" or inp == "b": 
                    state = "PB"
                    MMCtrl = False 
                elif inp == "C" or inp == "c":
                    state = "PC"
                    MMCtrl = False 
                elif inp == "Q" or inp == "q":
                    MMCtrl = False 
                    LoopCtrl = False 
    elif state == "PA":
        print("==== Pressure Surge Analisis ====")
        
        LoopCtrl = False 
    else:
        print("terminate")
        LoopCtrl = False



