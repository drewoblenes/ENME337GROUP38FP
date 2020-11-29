# ENSF 337 FINAL ASSIGNMENT

## Main Goal:
The main goal of the final project is to create a pipeline analisis tool  

## Project Requierments: 

### Main menu: 
In the main menue there are three main catagories 
#### Pressure Surge Analysis 
**Problem "A"**
- `Goal` 
    - The magnitude of the pressure surge that would cause complete failure of a pipeline with an initial crack 
    - The number of cycles it would take for there to be a failure is determined and compared with the actual desired lifetime of the pipeline 
- `INPUTS` 
    - Nominal pipe size (NPS)
    - Pipe schedule 
    - Pipe material
    - Initial depth of the crack 
    - Initial length of the crack 
    - internal pressure 
        - limit to (40MPa-2000MPa)
    - desierd lifetime of the pipe
        - limit to (10 years - 50 years)
    - incremental crack growth 
        - limit to (0.5mm-1.0mm)
- `REQUIERMENTS FROM PipeData.csv `
    - plane strain fracture toughness 
    - Paris eqatiion coefficient (A)
- `REQUIERMENTS FROM MaterialData.csv`
    - Paris equation exponent (n)

- `NOTE` 
    - Some pipeline scediles are not assigned in the database, this means that there should be an option for the user to enter this manually 
    - For instances where a minimum and maximum plane strain fracture value is given use the average of the two 
- `EXPECTED OUTPUTS` 
    - A list of all of the user-provided inputs 
    - A statement telling the user the surge pressure value that will cause fracture 
    - A statement telling the user the number of cycles to falure
    - A statement telling the client if the fatigue life is within the desired lifetime of the pipeline
    - A plot of crack depth vs total cycles to falure on a log-log scale 
- `ADDITIONAL REQUIERMENTS`
    - Crate and use a function to convert the obtained data into the correct form 
    - Pipeline outer diameter and wall thicness should be standard values obrained from the database files provided. Wall thickness calues provided by the user can vary from the standard values however a warning messafe should be output.
    - Check that the inital crack depth and critical crack dept are not greater than the wall thickness of the pipeline. If the critial crack depth is calculated as greater than the thickness of the pipe wall then overwrite the calculated value with the pipe wall thickness 
    - Utilize exception handiling and valiudataion 


#### Determination of Crack Growth Rate Material Properties 
**Problem "B"**
- `GOAL`
    - In this part of the assignment we're looking for the Paris equation coeffiecient and ecponent
    - This analizes data from fatigue ewxperements useing a compact tension specimen to obtain fatigue crack growth rate properties for the paris equation 
    - The standard deviation is and mean are calculated considering grometry cariations in the compact tension specimen 
- `INPUTS` (Apaprently there are no user inputs so Most of these are without context)
    - "W' paramiter 
        - limit (23mm-80mm)
    - Specimen Thickness (B)
        - limit (2mm<=B<=20mm)
    - Maximum Force 
        - limit 5.14kN
    - Minimum Force 
        - limit 0.089kN 
    - Number of cycles 
        - From database 
    - Crack Depth 
        - From database 
- `OUTPUTS`
    - A statement stating the value of W and B used in calculations 
    - Plot of crack depth Vs. the No. of cycles
    - plots of the crack depth growth rate Vs. the delta of K (im not sure what k is)
        - show a figure containing 4 subplots one for each geometry evaluated 
            - on each subplot include the Paris coefficient and the Paris exponent 
    - A statement with the standard deviation and mean of the Paris coefficient (A) and the paris exponent(N)
- `NOTE` 
    - Use exception handling for a case where the required input data file cannot be found 
    - This problem dows not require any user inputs (Then how is stuff specified?)

#### Failure Probobility Analysis 
**Problem "C"**
- `GOAL` 
    - This uses a simple Monte Carlo simulation of pipeline fatigue falure to estimate the falure probability of a steel pipeline 
    - This code requiers your code from Probvlem A to calculate the number of cyles to falure 

- `INPUTS` 
    - There are two main modes that the user can pick
        1. Keep the inital length of the crack as a fixed value (standard dev = 0) while changing the initial depth of the crack (normal distribution with a mean of `8.6 mm` and a standard devialtion of `1.5 mm`) . The desired lifetime of the pipeline will face a standard deviation of 10 years with a normal distibution 
        2. Keep the inital length of the crack as a fixed value (standard dev = 0) while changing the initial depth of the crack (normal distribution with a mean of `4.5 mm` and a standard devialtion of `1.6 mm`). The desired lifetime of the pipeline will face a standard deviation of 10 years with a normal distibution 

