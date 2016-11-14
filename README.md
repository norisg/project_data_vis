Introduction:

I chose the Flight data set from the Udacity website. After trying to visualise the data I found out, that the data set was too large to 
parse it with d3 into a html document. I prepared the data with a Python Script. 


Summary:

The visualisation lets the person explore the US Flight Data for the year 2008. One can see the most busiest airports
and also the airports with the most delays. Scaled circles with different colours are used to visualise the size of the value.
Moreover when you hover over the airport more information of the data is displayed.


Design:

After reading Mike Bostocks article about a "bubble chart", I definetly wanted to use that kind of map visualisation for the project. 
A clean map of the US with only the state boundaries shown. In addition I created menu buttons on the upper right site to guide the user 
step by step to thourgh data set.

Feedback and Changes that were made:

1. At first I also displayed the mean arrival delay at airport. The values were all near 0 so my visualisation mislead a first person,
because I used the same scale as for the other variables. So I decided to not display this option because airport with less arrivals 
and departures had sometimes a much larger value and this was kind of misleading.

2. Another point was the colour of the buttons. Persons did't like the lightgreen for the buttons so I changed it to lightblue.

3. The legend for the visualisation was coverd by a feedback button which I implemented. So I changed the absolut position of the 
legend label.

4. Another critic was the exploratory aspect of the graphic. So reduced the possibilities of the buttons at the upper right side.
  So focussed on the 10 busiest airports and the airport with the highest delay per flight. Moreover I added barcharts to underline
  the difference between them.
  
5. When you hover over the circles some information is presented. Because of some feedback I added some more important information.

Feedback

All the feedback I received
=========================================================================================================================================
"Thanks for sharing this visualization. I enjoyed exploring the visualization. One interesting thing to me was the incredibly large 
arrival delays for Pierre regional airport. I wonder what is going on there. I expected to see larger delays in the far north 
(Marquette for example) due to the large volume of snow, but delays appear to be moderate.

Something to keep in mind is that the current state of the visualization is primarily exploratory. 
For P6 it is critical that the visualization be explanatory, though it can contain exploratory elements. 
The visualization should focus and center on a finding or set of findings.

Some other things to consider:

The legend for circle size is very difficult to see because it is blocked by the feedback button. 
It might be good to add a more detailed legend for circle size closer to the map.
How were circle areas scaled? Circles should be scaled by the square root of 2 to since circle area is proportional to radius squared.
The tooltip that gives the airport name is very helpful. It may be useful to display data information, 
such as average departure delay, etc. as well.
I hope this was helpful and I look forward to seeing the next version."
=========================================================================================================================================
Green letter color in the right upper corner is not good readable. Further the cursor style when moving to the upper 
right fields could be changed to something more visuable at first glance. The bootom left corner shows some info when clicking on a 
bubble, this info shall be written in more bolt letters in order to achieve a better user experience.
=========================================================================================================================================
I see 2 variables, arrivals and departures and their corresponding means. The gret thing about this visualization,
is that by moving the cursor to one of the four variables, I am able to see the size of each one. 
The size is shown by the size of the bubbles.
=========================================================================================================================================
The graphic is very clean but maybe an autocapturing for the circle would be nice. 
In addition a visualisation when clicking on the circles would appeal nice to me.



Resources:
d3 dokumentation : https://github.com/d3/d3/wiki
Udacity Project 6
D3.js (BSD License)
NodeJS

