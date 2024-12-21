# Sort_Showcase


			        	---G E N E R A L P U R P O S E---
	The Purpose of this Repository is to help visualize the difference in speed of sorting methods,  
	by way of a basic bar-graph coupled with an explanation of the method used,as well as a Big O 
	annotation to assist vocab/ algebraic understanding when talking about algorithms, and wrapping
	it up in a neat python based GUI for ease of use.

	I hope that by the end of this your understanding of algorithms 
	and sorting methods are deepened.


 				    PYTHON LIBRARIES USED TO CREATE / RUN THIS PROJECT:
					- Tkinter
     				- Time
	  				- Matplotlib
	    				- random

					--- HOW TO RUN / TEST THE PROJECT ---

	  				ENSURE YOU HAVE THE PROJECT ALONG WITH ALL CORRESPONDING LIBRARIES DOWNLOADED.
  					
					RUN "main.py" WITHIN THE PROJECT TO START THE SHOWCASE.

     					INSERT AN INTEGER INTO THE INPUT TO GENERATE THAT NUMBER OF ITEMS ON THE GRAPH

   					CHOOSE SORT TYPE TO TEST

 					GENERATE GRAPH WITH THE "Generate"  BUTTON

	   				AFTER VIEWING UNSORTED GRAPH CLICK "Sort" TO VIEW THE SORTING ANIMATION IN REAL TIME
					

     


				        	 ---Ver control---

	            		  feel free to reach out to me to make suggestions

---LEGACY Ver 1.00---

- established basic 'index' page with HTML including a 'welcome' with above text as a reference point

- established a basic Style sheet including style classes for "container", "Global" etc.

- separate div container for bar-graphs and sorting methods

- setup buttons for UI purpose (Generate graph button / dropdown selections / sort button) 



						---   REFACTOR   ----

  - Refactored project to be entirely python based
  - created basic Tkinter / Matplotlib Gui
  - created graph population file "Graph.py"
  - Created basic sort algorithm file "sort.py"
 

						---	TODO	---

    - Timer for sorting currently times how long the sorting window is open as opposed to how long it took to fully sort
    - consider putting the sort button in the same window as the graph perhaps??
    - graph populates first and doesnt sort as expected but the sort requires you to close the first graph to properly reopen and sort the graph real time this needs to be changed so that the graph stays open and then sorts on button push.
       
