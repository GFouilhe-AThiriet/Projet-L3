Worksheet :

https://docs.google.com/document/d/1SY5bn5L_R2vqLS5i3iNWATqsn_-3c4BE1hlDDt5Gbqk/edit

Dataset (photos from Pl@ntnet) : https://gitlab.inria.fr/cgarcin/plantnet_dataset

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Update 04/04/21 by Aurelien :
We were told to write our scripts in English, so I don't know if we are also expected to write in english our reports. Finally, I got GithubDesktop, VisualStudioCode and Python to work. It was much harder than expected but it works now.

I completed the step 1) of the worksheet. I plotted the graph with two different styles. The first one is a histogram and the second one a dotted line. I thought the second one could be more visual than the first one.

Result : https://i.ibb.co/NWDCSqb/Capture-d-cran-2021-04-04-234953.png

I used pandas in order to complete the histogram (bar plot).

I have also tried to get a fitting curve of the exponential decay, by using the polynomial tool polyfit. I managed to get the graph but the approximation wasn't great, even with a degree equal to 100. Nevertheless, I understood it was normal considering that there is more than 1000 values in the x-axis. I had tried to get a fitting curve because I thought it could have been more visual than a histogram but, eventually, the red dotted line returns the same thing.

That's basically what I did today.
Aurelien

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Update 08/04 by Aurelien :
In order to complete the second step, I've learnt how to make subplots with matplotlib. The complexity of the display notably required to change the plt.plot for ax.plot and consequently to change all of the linked commands (for the graphs).

%%%%%%%Reminder on the library choice :
Then, to get an interactive display, I looked into the Ipywidgets documentation, as we were invited to. It didn't seem to me extremely obvious that it could be the appropriate library in order to get the interactive display we wanted. It seemed to me that Ipywidget was great to modulate the scale, the axes, the printed function, but I didn't find how it could help us to modificate plants images (jpg) in real time. So I looked for something else.

So I looked into Pygame documentation. I thought and I still think that it would be the best way to have an complicated interactive display in real time. Nevertheless, I still looked for something else since the Pygame code is a whole thing in itself, and I didn't want, if I had the possibility, to go directly into it. Also, I looked for something else because I thought that Pygame might not be a regular tool in order to complete a serious work.

FuncAnimation might be the appropriate tool. The only problem is that the documentation didn't seem great in general -in my opinion-, except for the Ken Hughes' article that I linked in the code.
%%%%%%%

I added a cursor that follows the mouse and it obtains the coordinates of the mouse in real time. Thus, mouse's coordinates are correctly printed for each click.

Current state : https://i.ibb.co/99rX13G/Capture-d-cran-2021-04-08-192809.png

Update 09/04 by Au. : Step 2) almost done.
Now, the plant image changes when someone clicks on the graph. There still is some presentation to do, but the code works now.


Update 11/04 by Guilhem : 
I cleaned the code by removing unnecessary features, simplifying some lines, formatted comments and created a separated "doc.txt" to save doc info on tools we use.
I also added the actual names of species on the picture displayed instead of their id.

Update 22/05 by Au. : Tentative to have a fluider display with Altair. Altair does open an internet window from VSC where the graph is displayed. I have tried to have an intern display but it seems that it does not work with VSC. I thought that I had found a possibility but the code didn't work and then, when I looked in some discussions of 2020 in StackOverflow, some people who both seemed to know programmation better than me were saying that the documentation indicating that there were a possiblity to have an intern display in VSC was not good. So I stopped that and I did it with the window display -which is good, so it's fine.

There are possibilities to display images so I will look into it in the next days. (I might also try to display an interactive horizontal or vertical bar in real time.)

Update 24/05 by Au. : Finally I opted for Pygame and as I thought, it is clearly better than the rest to have an interactive display. I created the basics of interactive windows and controls. I also added a new column "groups" in the cvs file in order to complete the step 3.

Update 25/05 by Au. : Today minor updates. I think the Pygame code should be rebuilt properly. Otherwise we'll end up with a 600 lines illigible code.

Update 27/05 by Au. : Code rebuilt properly. I redid a more beautiful presentation of the main window and coded a scrolling group_species list. When you click on it, the name of the species within the selected group are displayed. Still have to see how to display images considering the number of species per group varies.