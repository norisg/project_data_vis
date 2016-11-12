#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 10:28:18 2016

@author: nnorit
"""

import csv

def ParseData_Departure():
    f1 = open('data/2008.csv', 'r')
  #  f2 = open('airports.csv', 'r')
    f3 = open('Departure_year.csv', 'w')
                     
    c1 = csv.DictReader(f1)
   # c2 = csv.DictReader(f2)
    fieldnames = ['Airport', 'DepDelay_Mean','DepFlights'];
    c3 = csv.DictWriter(f3,fieldnames)


    count_departure = 0 ;
    delay_departure = 0;
    


    row={'Origin':"IAD"}

    flights_month =[]
    flight_year = []
    


     
    # Departure Analysis

    for i in c1:
    
        if i['Origin']!= row['Origin'] and count_departure !=0:
            
            flights_month.append({fieldnames[0]: row['Origin'], fieldnames[1]:(delay_departure/count_departure),
                         fieldnames[2]: count_departure});
            #print(row['Origin']+ '\n' + str(count_departure))
            count_departure = 0;
            delay_departure = 0;
        
        row = i;
        count_departure += 1;
        if row['DepDelay']!= 'NA':
            delay_departure += int(row['DepDelay']);



    #c3.writerows(flights_month);
    airport = False;
    counter = 0;
    delay_departure = 0;
    flight_year.append(flights_month[0]);
    for i in flights_month:
        while counter <=len(flight_year)-1 and not airport:
            if flight_year[counter]['Airport'] == i['Airport']:
                airport = True;
            counter +=1;
        if not airport:
            flight_year.append(i);
        else:
            flight_year[counter-1]['DepFlights']+= i['DepFlights']; 
        counter =0;
        airport = False;
    c3.writeheader();
    for i in flight_year:
        c3.writerow(i);
    print()

#ParseData_Departure();

#Adding Arrivals to the Data

def ParseData_Arrivals():
    f1 = open('Departure_year.csv', 'r');
    f2 = open('data/2008.csv','r');
    f3 = open('Arrivals_year.csv','w');

    c1 = csv.DictReader(f1);
    c2 = csv.DictReader(f2);
    fieldnames = ['Airport', 'DepDelay_Mean','DepFlights','Arrivals','ArrivalsDelay_Mean'];
    c3 = csv.DictWriter(f3,fieldnames);
    Dep_Arr_Data =[];

    for i in c1:
        i.update({'Arrivals': 0, 'ArrivalsDelay_Mean':0});
        Dep_Arr_Data.append(i);
    
    airport = False;
    counter = 0;
    for i in c2:
        while counter <=len(Dep_Arr_Data)-1 and not airport:
            if Dep_Arr_Data[counter]['Airport'] == i['Dest']:
                airport = True;
            counter +=1; 
        if airport:
           Dep_Arr_Data[counter-1]['Arrivals']+=1;
           if i['ArrDelay']!= 'NA':
               Dep_Arr_Data[counter-1]['ArrivalsDelay_Mean'] = int(i['ArrDelay']);

        counter =0;
        airport = False; 
    c3.writeheader();
    for i in Dep_Arr_Data:
        if i['Arrivals']!= 0:
           i['ArrivalsDelay_Mean']= i['ArrivalsDelay_Mean']/i['Arrivals'];
        c3.writerow(i)
        
        
#ParseData_Arrivals();



        
                
                 
        
        

    
        
    
            
 
         
    
    

    

               