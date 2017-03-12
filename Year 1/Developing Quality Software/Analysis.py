from tkinter import *


class MyFrame(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        window.geometry("1000x750+300+300")
        # Generates the window to be of fixed size
        self.Show()

    def Show(self):
        global a_label
        global a_button
        global R1Y1
        global R2Y2
        global R3Y3
        global R4C1
        global R5C2
        global R6C3
        #Declares the objects so they can be placed or removed in different functions
        a_label = Label(self, text="Do you want to analyse your results?")
        a_label.grid(row=1, column=1)
        # Creates a message on the form and specifies where to place it.

        self.Year = StringVar()
        #Sets the variable to be a string

        R1Y1 = Radiobutton(self, text="First year", variable=self.Year, value="Year1")
        R1Y1.grid(row=3, column=0, sticky=W)

        R2Y2 = Radiobutton(self,text="Second year", variable= self.Year, value="Year2") 
        R2Y2.grid(row=4, column=0, sticky=W)

        R3Y3 = Radiobutton(self, text="Third year", variable= self.Year, value="Year3")
        R3Y3.grid(row=5, column=0, sticky=W)

        R4C1 = Radiobutton(self, text="Course 1", variable=self.Year, value="CompSci")
        R4C1.grid(row=3, column=2, sticky=W)

        R5C2 = Radiobutton(self,text="Course 2", variable= self.Year, value="PlaceHolder") 
        R5C2.grid(row=4, column=2, sticky=W)

        R6C3 = Radiobutton(self, text="Course 3", variable= self.Year, value="Engineering")
        R6C3.grid(row=5, column=2, sticky=W)
        # Creates the radio buttons which allows the user to select them to decide which analysis they would like to look at
        # Untested - Come back later when file open works
        R1Y1.select()
        #  Has the first radio button selected by default

        a_button = Button(self, text="Analysis")
        a_button.grid(row=2, column=4)
        a_button.config(command=lambda: self.button_test(self.Year.get()))
        # Creates a button on the form and specifies where to place it.

    def button_test(self, Type):
        R1Y1.grid_remove()
        R2Y2.grid_remove()
        R3Y3.grid_remove()
        R4C1.grid_remove()
        R5C2.grid_remove()
        R6C3.grid_remove()
        # Untested - Come back later when file open works
        a_label.grid_remove()
        a_button.grid_remove()
        #Clears the whole form ready for the correct objects to be placed
        global Text
        global Visual
        global Audio
        global Reading
        global Kinesthetic
        global Activist
        global Theorist
        global Pragmatist
        global Reflector
        global NoData
        global b_button
        #Declaring global variables so they can be used in different functions
        Array = [{"Course": "Yes", "Year": 1, "Activist": 11, "Theorist": 12, "Pragmatist": 13, "Reflector": 14, "Visual": 11, "Audio": 12, "Reading": 13, "Kinesthetic": 14}, {
            "Course": "No", "Year": 1, "Activist": 5, "Theorist": 5, "Pragmatist": 5, "Reflector": 5, "Visual": 5, "Audio": 5, "Reading": 5, "Kinesthetic": 5}]
        # Two variables above is just test data
        List = self.CreateList(Array, Type)
        # Calls a function to grab scores from dictionary depending on if
        # year/course selected and places them into a list
        if List == [0, 0, 0, 0, 0, 0, 0, 0]:
            NoData = Label(
                self, text="Sorry, but we do not have any results for the option you have selected")
            NoData.grid(row=7, column=1)
            #Checks to see if there were any changes to the list. If there aren't any changes it will output a different message
            b_button = Button(self, text="Back")
            b_button.grid(row=7, column=2)
            b_button.config(command=lambda: self.ErrorClear())
        # Just some general error checking if there is no data, e.g no Year 1
        # Students took the test
        else:
            d = (self.Dictionary(
                List))
            # Calls a function to create a dictionary
            Text = Label(
                self, text="These are the average scores for each learning style")
            Text.grid(row=7, column=2)
            Visual = Label(self, text="Score for Visual : " + str(d["Visual"]))
            Visual.grid(row=8, column=1)
            Audio = Label(self, text="Score for Audio : " + str(d["Audio"]))
            Audio.grid(row=9, column=1)
            Reading = Label(
                self, text="Score for Reading : " + str(d["Reading"]))
            Reading.grid(row=10, column=1)
            Kinesthetic = Label(
                self, text="Score for Kinesthetic : " + str(d["Kinesthetic"]))
            Kinesthetic.grid(row=11, column=1)
            Activist = Label(
                self, text="Score for Activist : " + str(d["Activist"]))
            Activist.grid(row=8, column=3)
            Theorist = Label(
                self, text="Score for Theorist : " + str(d["Theorist"]))
            Theorist.grid(row=9, column=3)
            Pragmatist = Label(
                self, text="Score for Pragmatist : " + str(d["Pragmatist"]))
            Pragmatist.grid(row=10, column=3)
            Reflector = Label(
                self, text="Score for Reflector : " + str(d["Reflector"]))
            Reflector.grid(row=11, column=3)
            #Creates labels to display the calculated data for each learning style
            b_button = Button(self, text="Back")
            b_button.grid(row=12, column=4)
            b_button.config(command=lambda: self.Clear())
            #Creates a button which clears the frame and outputs the previous objects

    def Clear(self):
        Text.grid_remove()
        Visual.grid_remove()
        Audio.grid_remove()
        Reading.grid_remove()
        Kinesthetic.grid_remove()
        Activist.grid_remove()
        Theorist.grid_remove()
        Pragmatist.grid_remove()
        Reflector.grid_remove()
        b_button.grid_remove()
        #Clears the frame of all objects
        self.Show()
        #Calls a function which places all default objects back on the frame

    def ErrorClear(self):
        NoData.grid_remove()
        b_button.grid_remove()
        #Clears error message
        self.Show()
        #Calls a function which places all default objects back on the frame

    def Percentages(self, Score):
        x = []
    # Creates a empty list to put percentages in
        Total = (sum(Score) / 2)
    # Works out the total, so percentage can be found. Divides by 2 because of
    # 2 questionnaire will make it 200% instead of 100%
        for i in range(len(Score)):
            Temp = ((Score[i] / Total) * 100)
        # Works out the percentage of each score
            Temp = "{:2.2f}".format(Temp) + "%"
        # Formats it to 2 decimal places and adds a % to the end of it
            x.append(Temp)
        # Adds the worked out percentage to the list
        return(x)

    def Dictionary(self, Score):
        d = {}
        Answers = ["Visual", "Audio", "Reading", "Kinesthetic",
                   "Activist", "Theorist", "Pragmatist", "Reflector"]
    # Creates a empty dictionary
        Percent = self.Percentages(Score)
    # Gets the percentages of each score from other function
        for i in range(len(Answers)):
            d[Answers[i]] = Percent[i]
        # Puts the answers with their correct percentage into the dictionary
        return(d)

    def CreateList(self, Array, Type):
        List = [0, 0, 0, 0, 0, 0, 0, 0]
        # Creates a list with totals begining at 0 so addition can be applied
        # to them
        if Type == "Year1":
            for i in range(len(Array)):
                if Array[i]["Year"] == 1:
                    List = self.Adding(Array, i, List)
        if Type == "Year2":
            for i in range(len(Array)):
                if Array[i]["Year"] == 2:
                    List = self.Adding(Array, i, List)
        if Type == "Year3":
            for i in range(len(Array)):
                if Array[i]["Year"] == 3:
                    List = self.Adding(Array, i, List)
        if Type == "CompSci":
            for i in range(len(Array)):
                if Array[i]["Course"] == "CompSci":
                    List = self.Adding(Array, i, List)
        if Type == "PlaceHolder":
            for i in range(len(Array)):
                if Array[i]["Course"] == "PlaceHolder":
                    List = self.Adding(Array, i, List)
        if Type == "Engineering":
            for i in range(len(Array)):
                if Array[i]["Course"] == "Engineering":
                    List = self.Adding(Array, i, List)
        # Basically in each if statement it checks which data you want to be
        # displayed, e.g Year 1 student scores. Then Looks through each
        # dictionary checking if they match the required search and if the
        # value matches it uses the function below passing on the list and the
        # current index.
        return (List)

    def Adding(self, Array, i, List):
        List[0] += (Array[i]["Activist"])
        List[1] += (Array[i]["Theorist"])
        List[2] += (Array[i]["Pragmatist"])
        List[3] += (Array[i]["Reflector"])
        List[4] += (Array[i]["Visual"])
        List[5] += (Array[i]["Audio"])
        List[6] += (Array[i]["Reading"])
        List[7] += (Array[i]["Kinesthetic"])
        # Data is passed here where the list is updated (Scores in the current
        # list are increased by the value of the score in the current
        # dictionary).
        return List

window = Tk()
window.wm_title("Learning styles analysis")
# Changes the name of the TKinter title bar
mf = MyFrame(window)
mf.pack(padx=10, pady=10)
window.mainloop()
# I have no idea what most of this does, I took it from the example.
