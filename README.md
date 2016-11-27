Data Visualisation Project 
===================
*by Norbert Norit*

Files in this repository:

 1. Arrivals_year.csv (important for the first visualisation,
	after the first submission I wrangled the data again with numpy for 
	the other graphics 
 2. index_1submissionl.html (visualisation for the first submission)
 3. datawrangling_flight.py (script for DataWrangeling)
 4. index_2.html (Visualisation with a few errors not the final version. However 
    this file contains the whole visualisation history from the beginning (before
    first submission) 
 5. index.html (final visualisation for the second submission)
 6. d3.legend.js (important for index.html)
 7. makefile (creating the underlying us map)
 8. us_map.json 
 9. airport.csv
 10. Visualisation_Airport_Year_2008.csv
 11. Visualisation_Airport_Monthly_2008.csv

> **Links of the visualisations:**
The link for the first visualisation (before first submission)
http://bl.ocks.org/norisg/ed182add89566555c93b951a706d4200
The link for the second submission is:
http://bl.ocks.org/norisg/raw/606b6268dee372597b074e73d14016aa/


Introduction:
===================

I chose the Flight data set from the Udacity website. 
After trying to visualise the data with d3 and html I found out, that the data set was too large to parse it with d3 into a html document. That's why prepared the data with a Python Script. 


    Summary/Introduction:

The visualisation lets the person explore the US Flight Data for the year 2008. US Airports are shown on a Map with circles which decode the number of departures and arrivals for a specific airport. At the first glimpse you get an overview of all major airport in the US. When exploring the circles and selecting them the user gets more information regarding the airport flight delays. Moreover links provided detailed information of the data set and background.
The general story of the visualisation is, that a lot of flights are delayed but weather or security issues are definitely not the problem. Airport capacity or carrier issues are heavy weight factors. The mean arrival delay at the destination airport is not that high, which can be explained by a flexible flight schedule of the airports in combination with the airlines.

    Design:

![Upper Part of Visualisation](https://cloud.githubusercontent.com/assets/14205851/20652324/781db25a-b4f7-11e6-9c5b-12a502f03e70.png)

![Upper Part of Visualisation](https://cloud.githubusercontent.com/assets/14205851/20652325/7b84386a-b4f7-11e6-80b5-b6421f6ac869.png)

> After reading Mike Bostocks article about a "bubble chart", I
> definetly wanted to use that kind of map visualisation for the
> project.  A clean map of the US with only the state boundaries shown.
> In addition I created menu buttons on the upper right site to guide
> the user  step by step through data set.

*After first submission*

> After the first submission the story of the data set was missing so I tried to find one in the data set. Beforing going into detail I want to mentioned that it took me a hell of time with d3 to create this visualisation. I would be glad to hear some tips and trick how one create a html visualisation. Main problem was the arrangement of svg graphs or divs etc. . Every "tag" behaved kind of differently so maybe I arrange an office our to talk about my problems I had with this visualisation. 
> Details: A short description invites the user to dig deeper into the visualisation. At First only the map and the chart down the bottom is visible. The delay chart for one specific airport appear only when selecting an airport. At first there is a white gap between these two chart but after selecting an airport more information of the delay times is provided. At first it is a bit exploratory because the user needs to select an specific airport, but then the story begins. The description gives the user important information to understand the graph completely. 
> The third part with the bar chart for the 10 busiest airports is another explainatory element in my visualisation. Moreover with two buttons the user is able to show only the 10 most important airports, this makes it easier to check the iata code at the bar chart with the map and get an overview of the airports. The text underneath concludes the whole insight of this visualisation.







    Feedback and Changes that were made:
    

>For the  1 Submission:
> 

 1. At first I also displayed the mean arrival delay at airport. The values were all near 0 so my visualisation mislead a first person, because I used the same scale as for the other variables. So I decided
to not display this option because airport with less arrivals  and
departures had sometimes a much larger value and this was kind of
misleading.
 2. Another point was the colour of the buttons. Persons did't like the lightgreen for the buttons so I changed it to lightblue.
 3. The legend for the visualisation was coverd by a feedback button which I implemented. So I changed the absolut position of the  legend
 label.
 4. Another critic was the exploratory aspect of the graphic. So reduced the possibilities of the buttons at the upper right side.   So
 focussed on the 10 busiest airports and the airport with the highest
 delay per flight. Moreover I added barcharts to underline   the
 difference between them. 
 5. When you hover over the circles some information is presented. Because of some feedback I added some more important information.

>For the  2 Submission:

 1. Changed color of the map and the color of the tooltip to make it better readable
 2. Reduced buttons and build a story around the data
 3. Created a line chart with several data sets
 4. Used the bar chart for insights regarding delay times and number of delayed flights

 
> Feedback
> 
> All the feedback I received:
> 
> "Thanks for sharing this visualization. I enjoyed exploring the
> visualization. One interesting thing to me was the incredibly large 
> arrival delays for Pierre regional airport. I wonder what is going on
> there. I expected to see larger delays in the far north  (Marquette
> for example) due to the large volume of snow, but delays appear to be
> moderate. Something to keep in mind is that the current state of the
> visualization is primarily exploratory.  For P6 it is critical that
> the visualization be explanatory, though it can contain exploratory
> elements.  The visualization should focus and center on a finding or
> set of findings.
> 
> Some other things to consider:
> 
> The legend for circle size is very difficult to see because it is
> blocked by the feedback button.  It might be good to add a more
> detailed legend for circle size closer to the map. How were circle
> areas scaled? Circles should be scaled by the square root of 2 to
> since circle area is proportional to radius squared. The tooltip that
> gives the airport name is very helpful. It may be useful to display
> data information,  such as average departure delay, etc. as well. I
> hope this was helpful and I look forward to seeing the next version."
> 


----------

> Green letter color in the right upper corner is not good readable.
> Further the cursor style when moving to the upper  right fields could
> be changed to something more visuable at first glance. The bootom left
> corner shows some info when clicking on a  bubble, this info shall be
> written in more bolt letters in order to achieve a better user
> experience.


----------

> I see 2 variables, arrivals and departures and their corresponding
> means. The gret thing about this visualization, is that by moving the
> cursor to one of the four variables, I am able to see the size of each
> one.  The size is shown by the size of the bubbles.


----------


> The graphic is very clean but maybe an autocapturing for the circle
> would be nice.  In addition a visualisation when clicking on the
> circles would appeal nice to me.



    Resources:

 - d3 dokumentation : https://github.com/d3/d3/wiki
 - Udacity Project 6
 - D3.js (BSD License)
 - NodeJS
 - stackoverflow.com
 - w3schools.com

