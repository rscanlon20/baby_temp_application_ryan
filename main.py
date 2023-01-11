""""
author: Ryan Scanlon
this code is a baby temperatue porgram that allows the user to create profiles for the babies and then
they are able to selct the baby and enter their tmeprture. With previous entries shown like their highest and
lowest tempertures.
"""


from guizero import App, PushButton, Window, ListBox, TextBox, ButtonGroup, Box, Picture, Text

temp = None
patient = None
store = []
list_names = []
tally = 0

def menu():
    global store

    def baby_profile():

        def save():
            global store, list_names, temp, patient, tally



            temps = temp.value

            float_temps = float(temps)
            if float_temps > 37.5 or float_temps < 36:
                patient.info("Warning", "Iregular temperature, temperature falls out within the range of  36.0°C to 37.5°C.")
                tally += 1

            if tally == 2:
                patient.info("Warning", "The babies temperature has been outside the acceptable range twice!")


            #checking if the value inputted is a float
            int_temps = float(temps)
            # appending the  to the section of the large list
            item["temperature"].append(int_temps)
            item["current_temperature"] = int_temps

            print(item["temperature"])




        def patient_profile():
            global temp, store, patient

            patient = Window(app, title = "patient")

            header_pt = Box(patient, width="1000", height=100)

            back_pt = PushButton(header_pt, text = "back")
            name_label_pt = Text(header_pt, text="patient")



            back_pt.when_clicked = patient.destroy

            main_pt = Box(patient, width=1000, height=400)


            name_text = item["baby_name"]
            dd_mm_yy = item["date_of_birth"]
            temp_text = item["temperature"]
            actual_temp = item["current_temperature"]

            # finds the min temperature and max temp in the specific section of list.
            lowest = min(temp_text)
            highest = max(temp_text)

            difference = highest - lowest

            # textboxes displayed on babies profile page
            name_pt = TextBox(main_pt, width=21, align = "top", text="name: " + str(name_text) )
            date_of_birth_pt = TextBox(main_pt, grid=[3,1], align = "top", width=21, text="Date of birth: " + str(dd_mm_yy) )
            temp_pt = TextBox(main_pt, align = "top", width=21, text="Past temps : " + str(temp_text) )
            cur_pt = TextBox(main_pt,align = "top", width=21, text="current temp : " + str(actual_temp) )
            highest_pt = TextBox(main_pt,align = "top", width=21, text="Highest temp : " + str(highest) )
            lowest_pt = TextBox(main_pt,align = "top", width=21, text="Lowest temp : " + str(lowest) )
            difference_pt = TextBox(main_pt,align = "top", width=21, text="Difference : " + str(difference) )




            temp = TextBox(main_pt, grid=[3,4], align = "top", width=21)


            button = PushButton(main_pt, text="save", command=save)




        global store, list_names


        baby_name = list.value

        #for loop which loops throiugh the large list of baby nams  and sees if it matches with the baby name pressed,where the value is regidted in store.
        for item in store:
            search = item["baby_name"]
            if search == baby_name:
                patient_profile()

        print(baby_name)


    def add_patient():

        def add_image():

            user_image=(app.select_file(title="Select file", folder=".", filetypes=[["All files", "*.*"]], save=False, filename=""))


            add_pat.image = user_image
        # becasue i have two save function one for creating the baby and one for saving their temperature, this fucntion goes under the add patient
        def save():
            global store, list_names


            temps = temp.value
            date = date_of_birth.value
            names = name.value
            # checks if the initial temperature enters is in the acceptable range
            float_temps = float(temps)
            if float_temps > 37.5 or float_temps < 36:
                add_patient.info("Warning", "Irregular temperature, temperature falls out within the range of  36.0°C to 37.5°C.")



            item = {}



            deci_temps = float(temps)

            # all under one big list however broken up into sections and able to refer to them as the text in quotation marks
            item["temperature"] = []

            item["baby_name"] = names
            item["date_of_birth"] = date
            item["temperature"].append(deci_temps)
            item["current_temperature"] = deci_temps


            list_names.append(names)

            store.append(item)
            list.clear()
            print(store)
        # creating a baby page
        add_patient = Window(app, title = "SECOND WINDOW")
        add_patient.show(wait=True)
        forehead_new_baby = Box(add_patient, width="1000", height=100)

        back_button = PushButton(forehead_new_baby, text="back")

        back_button.when_clicked = add_patient.destroy


        add_pat = PushButton(add_patient, text="Add_photo.gif")
        add_pat.when_clicked = add_image

        # info asked of user
        name = TextBox(add_patient, width=21, align = "top")
        name_text = Text(add_patient, text="Name")
        date_of_birth = TextBox(add_patient, align = "top", width=21)
        date_of_birth_text = Text(add_patient, text="Date of Birth")
        temp = TextBox(add_patient, align = "top", width=21)
        temp_text = Text(add_patient, text="Initial Temperature")

        # when pressed executes save function
        button = PushButton(add_patient, text="Add patient", command=save)


    #menu page
    app = App()
    main = Box(app, width=1000, height=1000, layout="grid")
    button1 = PushButton(main, text="New Baby", command=add_patient)
    list = ListBox(main, items=store, scrollbar=True, grid=[1,1],  command=baby_profile)
    app.display()

menu()



