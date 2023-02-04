# FetchBackend
Fetch Backend Initial Screening Question on: https://docs.google.com/document/d/1Yn_xAonwLOINma3MquU5ag6KoNMkrH3uA-99pJvqaWs/edit
# Running the program
1. Open Google Colab at https://colab.research.google.com/ ![colab](https://user-images.githubusercontent.com/124424840/216755211-4f99af95-4a98-4eb0-9aa5-3daca4b76d10.jpg)
2. Open a new notebook by clicking on New Notebook
3. Open transactions.csv (an random example csv file) on github, right click on "raw" on the right corner of the view window, then click on "save link as" and save the csv file on your local device. As a substitute to this step, you can test the program with any csv file named "transactions.csv" available on your local device. ![getcsv](https://user-images.githubusercontent.com/124424840/216755687-b483a9d5-f0b7-4f8f-b802-ae323f6e4cdb.jpg)
4. Now go to the google colab notebook opened in step 2 and paste the following lines into an empty cell.    from google.colab import files
                                                                                                            uploaded = files.upload()
Click on the play button on the left of the cell to run this code![files](https://user-images.githubusercontent.com/124424840/216756545-162c6a36-7317-4fe9-8c4b-14aac31cf2f5.jpg)
5. The output window of the notebook will now display a prompt to upload a file from your local device. Upload a csv file used for testing the program. The test file has to be titled "transactions.csv" for the program to run. Conversely, you could change the name of the csv file to the name of your test file on line 37 of program.py

6. Next, open program.py on github and copy and paste the entire file (58 lines) into a new cell in the google colab notebook. You can open a new cell by clicking on "Code"(highlighted in the picture below)![input](https://user-images.githubusercontent.com/124424840/216756735-013ed39e-e516-4e8a-beff-d8c7e4cbade8.jpg)

7. Now click on the play button beside the cell (highlighted above) in which program.py was pasted. The compiler will now tell you to enter the number of points to be deleted(int). Enter any integer and hit play again or press enter on you keyboard.![fina;](https://user-images.githubusercontent.com/124424840/216756778-4bbc16d3-18bd-4c3b-b729-1fe87a7a7416.jpg)
8. The output dictionary should be printed on your screen now


Alternatively, the program can also be tested by running program.py on a downloaded version of Python 3 on your device (https://www.python.org/downloads/). If you test it using this method, please save the test csv file and program.py in the same directory. 


