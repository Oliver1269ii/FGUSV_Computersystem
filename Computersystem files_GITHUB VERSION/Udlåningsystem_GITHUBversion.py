# Version 1.7
# Last change 22/01-23



from tkinter import *
from tkinter import ttk
from time import sleep, strftime, time
from customtkinter import *
import json, os
from getpass import getpass
import sys


global history





lang = {
"Fortryd" : {"da": "Fortryd", "en" : "Cancel"},
"Forsæt" : {"da": "Forsæt", "en" : "Continue"},
"Ja" : {"da": "Ja", "en" : "Yes"},
"Nej" : {"da": "Nej", "en" : "No"},
"Damage" : {"da" : "Var computeren beskadiget?", "en" : "Was the computer damaged?"},
"PcPlaceholder" : {"da" : "Computer navn", "en" : "Computer name"},
"Elev" : {"da" : "Elev navn", "en": "Student name"},
"Skader" : {"da": "Skader", "en": "Damages"},
"Historik" : {"da" : "Historik", "en": "History"},
"Udlån" : {"da": "Udlån", "en": "Lend out"},
"Aflever" : {"da": "Aflever", "en": "Hand in"},
"Luk" : {"da": "Luk Program", "en": "Shut down program"},
"aflevering" : {"da" : "Aflevering", "en" : "Handing in"},
"choosedamage" : {"da": "Hvilke skader?", "en" : "What damages?"},
"vislånte" : {"da": "Vis lånte", "en": "Show borrowed"},
"lånte" : {"da" : "Lånte PC liste", "en": "Borrowed PC list"},
"opdater" : {"da" : "Opdater", "en": "Update"},
"quit" : {"da" : "Er du sikker på du vil afslutte?", "en" : "Are you sure you want to quit?"},
"restart" : {"da" : "Genstart for at bruge dine indstillinger", "en" : "Restart to apply your settings"},
"hold" : {"da" : "Hold", "en" : "Team"},
"Insertpc" : {"da" : "Indtast PC", "en" : "Insert PC"},
"restartnow" : {"da" : "Genstart Nu", "en" : "Restart Now"}
}

appearmode = {
    "background" : {"dark" : "#242424", "light" : "#ebebeb"},
    "foreground" : {"dark" : "lightgray", "light" : "black"},
    "color" : {"blue" : "#1f6aa5", "green" : "#2cc985", "darkblue" : "#1f538d"}
}


def main():
    global langsetting
    langsetting = "da"

    pythondir = os.path.dirname(__file__)
    
    jsonfiles = pythondir + "/jsonfiles"
    try:
        os.chdir(pythondir + "/jsonfiles")
    except:
        os.mkdir(jsonfiles)
        os.chdir(jsonfiles)
    
    

    
    try:
        with open("options.json", "r") as file:
            set = json.load(file)
            
            
            if "Dansk" in set["Language"]:
                langsetting = "da"
                
            else:
                langsetting = "en"
                
            
            
            if "Lightmode" in set["MainTheme"]:
                set_appearance_mode("light")
                apmode = "light"
            else:
                set_appearance_mode("dark")
                apmode = "dark"

            
            if "Darkblue" in set["SecondTheme"]:
                set_default_color_theme("dark-blue")
                apcolor = "darkblue"
            elif "Green" in set["SecondTheme"]:
                set_default_color_theme("green")
                apcolor = "green"
            else:
                set_default_color_theme("blue")
                apcolor = "blue"
    except:
        open("options.json", "x")
        tempdict = {"Language": "English", "MainTheme": "Dark", "SecondTheme": "Blue"}
        with open("options.json", "w") as file:
            json.dump(tempdict, file)
    
    history = []
    try:
        try:
            with open("history.json", "r") as file:
                
                history = json.load(file)
                
        except:
            open("history.json", "x")
    except:
        pass


    borrowdict = {} 
    try:
        try: 
            with open("borrowed.json", "r") as file:
                borrowdict = json.load(file)
                
            
        except:
            open("borrowed.json", "x")
    except: 
        pass

    dmgdict = {}
    try:
        try:
            with open("damaged.json", "r") as file:
                dmgdict = json.load(file)
        
        except:
            open("damaged.json", "x")
    except: 
        pass
   
    today = strftime("%H:%M | %d/%m-%y")

    class Borrow:
        
        def combine(pcname, nameteam, today):
            today = strftime("%H:%M | %d/%m-%y")
            full = pcname + " | " + nameteam + " at " + today
            history.append(full)
            
            rowcount = 6
            rowcount = int(rowcount)
        
            borrowdict[pcname] = full
                
            return full

    def restart():
        root.destroy()
        os.execv(sys.executable, ['python'] + sys.argv)

    def settings():

        def savesettings():
            opti = {}
            language = languageselect.get()
            stheme = ttheme.get()
            stheme = stheme.split("-")
            
            if language == "Dansk":
                langsetting = "da"

            elif language == "English":
                langsetting = "en"

            else:
                with open("options.json", "r") as file:
                    jsondict = json.load(file)
                    
                    if jsondict["Language"] == "Dansk":
                        langsetting = "da"
                    else:
                        langsetting = "en"
            
            if "Language" not in language:

                opti["Language"] = language
            else:
                with open("options.json", "r") as file:
                    jsondict = json.load(file)
                    if jsondict["Language"] == "Dansk":
                        opti["Language"] = "Dansk"
                    else:
                        opti["Language"] = "English"

            if "Theme" not in stheme:
                for index in stheme:
                    index = index.strip()
                    
                    if "Lightmode" in index:
                        opti["MainTheme"] = "Lightmode"
                        break
                    else:
                        opti["MainTheme"] = "Darkmode"

                    
                    
                for index in stheme:
                    index = index.strip()
                    
                    if "Darkblue" in index:
                        opti["SecondTheme"] = "Darkblue"
                        break
                    
                    elif "Green" in index:
                        opti["SecondTheme"] = "Green"
                        break
                    else:
                        opti["SecondTheme"] = "Blue"
            else:
                
                with open("options.json", "r") as file:
                    jsondict = json.load(file)
                    opti["MainTheme"] = jsondict["MainTheme"]
                    opti["SecondTheme"] = jsondict["SecondTheme"]
            
            

            with open("options.json", "w") as file:
                json.dump(opti, file)
            reminder = CTkToplevel()
            
            CTkLabel(reminder, text=lang["restart"][langsetting]).pack(padx=15, pady=15)
            CTkButton(reminder, text=lang["restartnow"][langsetting], command=restart).pack(padx=15, pady=15)
        
        def console():
            
            print("\n Udlånings Console [version 1.7]\n Created by Oliver Larsen (2023) \n Some things you do in here are permanent, so BE CAREFUL")
            print('''
 Type "Help" for help''')
            
            UsrIn = ""
            while UsrIn != "quit":
                today = strftime("%H:%M %d/%m-%y")
                save()
                print("\n")
                print({today})
                UsrIn = input(">>>")
                UsrIn = UsrIn.lower()
                def remove(file):
                    try:
                        os.remove(file)
                        print(f"{file} has been succesfully removed")
                        return True
                    except:
                        print(f"Couldn't find {file}")
                        return False


                if UsrIn == "help":
                    print("\n'jsonfiles' == Prints out all json files\n\n'quit' == Leaves console mode\n\n'removeall' == Deletes all json files (CANNOT BE UNDONE)\n\n'remove {file}' == Tries to remove said file\n\n'cwd' = Prints current working directory")
                
                elif UsrIn == "jsonfiles":
                    with open("borrowed.json", "r") as file:
                        print("\n\nborrowed.json; ")
                        print(json.load(file))
                    with open("damaged.json", "r") as file:
                        print("\n\ndamaged.json; ")
                        print(json.load(file))
                    try:
                        with open("options.json", "r") as file:
                            print("\n\noptions.json")
                            print(json.load(file))
                    except:
                        pass
                    with open("history.json", "r") as file:
                        print("\n\nhistory.json")
                        print(json.load(file))
                        print("\n\n")

                elif "remove" in UsrIn:
                    
                    if UsrIn != "removeall":
                        
                        UsrIn = UsrIn.replace("remove", " ").strip()
                        
                        if getpass("Input Enrollment password: ") == "CODE":
                            check = input("Are you sure you want to delete " +UsrIn+ "? This can't be undone (y/n)").lower()
                            if check == "y" or check == "yes":
                                
                                if remove(UsrIn) == True:
                                    
                                    UsrIn = "quit"
                                    print("\n\n        RESTARTING PROGRAM\n")
                                    restart()


                    elif UsrIn == "removeall":
                        if getpass("Input Enrollment password: ") == "CODE":
                                
                            check = input("Are you sure? This can't be undone (y/n)").lower()
                            if check == "y" or check == "yes":
                                remove("history.json")
                                remove("borrowed.json")
                                remove("options.json")
                                remove("damaged.json")
                                
                                UsrIn = "quit"
                                
                                
                                print("\nGenerating new files on launch\n")
                                
                                with open("options.json", "w") as file:
                                    json.dump({"Language": "English", "MainTheme": "Darkmode", "SecondTheme": "Blue"}, file)
                                restart()
                elif "cwd" in UsrIn:
                    print("\n\n" + os.getcwd())


                
                         
            
            
        settings = CTkToplevel()
        settings.title("Settings")
        settings.geometry("300x200")
        languageselect =CTkOptionMenu(settings, values=["Dansk", "English"])
        languageselect.set("Language")
        ttheme = CTkOptionMenu(settings, values=["Blue - Darkmode", "Darkblue - Darkmode", "Green - Darkmode", "Blue - Lightmode", "Darkblue - Lightmode", "Green - Lightmode", "Default"])
        ttheme.set("Theme")
        button = CTkButton(settings, text="Save", command=savesettings)
        adminbutton= CTkButton(settings, text="Console", command=console)

        languageselect.grid(row=5, pady=20, padx=50)
        ttheme.grid(row=6, pady=20, padx=50)
        adminbutton.grid(row=6, column=1, padx=(500, 0))
        button.grid(row=7, column=0)
    
    def save():

        with open("damaged.json", "w") as file:
            json.dump(dmgdict, file)
        with open("borrowed.json", "w") as file:
            json.dump(borrowdict, file)
        with open("history.json", "w") as file:
            json.dump(history, file)
         
    def quitcheck():

        def yes():
            save()
            quit.destroy()
            sleep(0.2)
            root.quit()
            

        
            
        quit = CTkToplevel()
        quit.configure( padx= 50, pady=75)

        lbl = CTkLabel(quit, text=lang["quit"][langsetting])
        yes = CTkButton(quit, text=lang["Ja"][langsetting], command=yes)
        no = CTkButton(quit, text=lang["Nej"][langsetting], command=lambda: quit.destroy())

        padx=20

        lbl.grid(row=0, column=0, columnspan=2, padx=padx, pady=(10, 25))
        yes.grid(row=1, column=0, columnspan=2, padx=padx, pady=15)
        no.grid(row=2, column=0, columnspan=2, padx=padx, pady=15)

    def funcmultiudlån():
        top = CTkToplevel()
        top.title(lang["PcPlaceholder"][langsetting])
        top.geometry("300x300")
        top.attributes('-topmost', True)
        top.update()
        def secondlayer():
            top2 = CTkToplevel()
            top2.title(lang["Elev"][langsetting])
            top2.geometry("300x450")
            top2.attributes('-topmost', True)

            def finish2(event):
                # This function is to bypass the needed event pass
                finish()

            def finish():
                hold = holdentry.get().strip()
                elevnavn = enterfield2.get().strip()
                studentname = elevnavn + " - " + hold
                if len(elevnavn) == 0 or elevnavn.isspace() == True or hold.isspace() == True or len(hold) == 0:
                    CTkLabel(top2, text="Indtast elev navn og hold ").grid(row=4, column=0, columnspan=2)
                
                else:
                    discription = Borrow.combine(pcnumber, studentname, today)
                    
                    top2.destroy()
                    top2.update()
                    save()
                    funcmultiudlån()
                    
            def cancel2():
                top2.destroy()
                top2.update()
                borrowrefresh()
            
            width=300
            height=250
            
            padx=width/4 
            
            elevlabel = CTkLabel(top2, text=lang["Elev"][langsetting])
            enterfield2 = CTkEntry(top2, placeholder_text=lang["Elev"][langsetting])
            holdlabel = CTkLabel(top2, text=lang["hold"][langsetting])
            holdentry = CTkEntry(top2, placeholder_text=lang["hold"][langsetting])
            enterbutton = CTkButton(top2, text=lang["Forsæt"][langsetting], command= finish)
            cancelbutton = CTkButton(top2, text=lang["Fortryd"][langsetting], command=cancel2)

            elevlabel.grid(row=0, column=0, pady=(25, 0), padx=padx)
            enterfield2.grid(row=1, column=0, pady=10, padx=padx)
            holdlabel.grid(row=2, column=0, pady=(30, 0), padx=padx)
            holdentry.grid(row=3, column=0, pady=(10, 50), padx=padx)
            enterbutton.grid(row=5, column=0, pady=25, padx=padx)
            cancelbutton.grid(row=6, column=0, padx=padx)
            
            enterfield2.after(0, enterfield2.focus)

            top2.bind('<Return>', finish2)
            top2.update()

        def UDenter2(event):
            # This function is to bypass the needed event pass
            UDenter()
            
        def UDenter():

            global pcnumber
            pcnumber = enterfield.get().upper()
            if "FGUSVNPC" in pcnumber:
                    
                pass
            elif "PC" in pcnumber:
                pcnumber = "FGUSVN" + pcnumber
            else:
                pcnumber = "FGUSVNPC" + pcnumber
            
            if len(pcnumber) == 0 or pcnumber.isspace() == True:
                CTkLabel(top, text=lang["Insertpc"][langsetting]).grid(row=0, column=0, columnspan=2)
            
            else:
                if pcnumber in borrowdict:
                    CTkLabel(top, text="Denne PC udlånt").grid(row=0, column=0, columnspan=2)
                else:
                    
                    top.destroy()
                    top.update()
                    
                    
                    secondlayer()
            save()

        def cancel():
            top.destroy()
            top.update()
            borrowrefresh()
        
        width=300
        height=300
        

        padx=width/4 

        enterlabel = CTkLabel(top, text=lang["PcPlaceholder"][langsetting])
        enterfield = CTkEntry(top, placeholder_text=lang["PcPlaceholder"][langsetting], )
        enterbutton = CTkButton(top, text=lang["Forsæt"][langsetting], command= UDenter)
        cancelbutton = CTkButton(top, text=lang["Fortryd"][langsetting], command=cancel)

        enterlabel.grid(row=1, column=0, pady=(15, 10), padx=padx)
        enterfield.grid(row=2, column=0, pady=(0, 50), padx=padx)
        enterbutton.grid(row=3, column=0, pady=25, padx=padx)
        cancelbutton.grid(row=4, column=0, padx=padx)
        
        enterfield.after(0, enterfield.focus)
        

        top.bind('<Return>', UDenter2)
        top.update()

    def Udlån():
        

        top = CTkToplevel()
        top.title(lang["PcPlaceholder"][langsetting])
        top.geometry("300x300")
        top.attributes('-topmost', True)
        top.update()
        def secondlayer():
            top2 = CTkToplevel()
            top2.title(lang["Elev"][langsetting])
            top2.geometry("300x450")
            top2.attributes('-topmost', True)

            def finish2(event):
                # This function is to bypass the needed event pass
                finish()

            def finish():
                hold = holdentry.get().strip()
                elevnavn = enterfield2.get().strip()
                studentname = elevnavn + " - " + hold
                if len(elevnavn) == 0 or elevnavn.isspace() == True or hold.isspace() == True or len(hold) == 0:
                    CTkLabel(top2, text="Indtast elev navn og hold ").grid(row=4, column=0, columnspan=2)
                
                else:
                    discription = Borrow.combine(pcnumber, studentname, today)
                    
                    top2.destroy()
                    top2.update()
                    save()
                    borrowrefresh()
            def cancel2():
                top2.destroy()
                top2.update()

            
            width=300
            height=250
            
            padx=width/4 
            
            elevlabel = CTkLabel(top2, text=lang["Elev"][langsetting])
            enterfield2 = CTkEntry(top2, placeholder_text=lang["Elev"][langsetting])
            holdlabel = CTkLabel(top2, text=lang["hold"][langsetting])
            holdentry = CTkEntry(top2, placeholder_text=lang["hold"][langsetting])
            enterbutton = CTkButton(top2, text=lang["Forsæt"][langsetting], command= finish)
            cancelbutton = CTkButton(top2, text=lang["Fortryd"][langsetting], command=cancel2)

            elevlabel.grid(row=0, column=0, pady=(25, 0), padx=padx)
            enterfield2.grid(row=1, column=0, pady=10, padx=padx)
            holdlabel.grid(row=2, column=0, pady=(30, 0), padx=padx)
            holdentry.grid(row=3, column=0, pady=(10, 50), padx=padx)
            enterbutton.grid(row=5, column=0, pady=25, padx=padx)
            cancelbutton.grid(row=6, column=0, padx=padx)
            
            enterfield2.after(0, enterfield2.focus)

            top2.bind('<Return>', finish2)
            top2.update()

        def UDenter2(event):
            # This function is to bypass the needed event pass
            UDenter()
            
        def UDenter():

            global pcnumber
            pcnumber = enterfield.get().upper()
            if "FGUSVNPC" in pcnumber:
                    
                pass
            elif "PC" in pcnumber:
                pcnumber = "FGUSVN" + pcnumber
            else:
                pcnumber = "FGUSVNPC" + pcnumber
            
            if len(pcnumber) == 0 or pcnumber.isspace() == True:
                CTkLabel(top, text=lang["Insertpc"][langsetting]).grid(row=0, column=0, columnspan=2)
            
            else:
                if pcnumber in borrowdict:
                    CTkLabel(top, text="Denne PC udlånt").grid(row=0, column=0, columnspan=2)
                else:
                    
                    top.destroy()
                    top.update()
                    
                    
                    secondlayer()
            save()

        def cancel():
            top.destroy()
            top.update()
            
        
        width=300
        height=300
        

        padx=width/4 

        enterlabel = CTkLabel(top, text=lang["PcPlaceholder"][langsetting])
        enterfield = CTkEntry(top, placeholder_text=lang["PcPlaceholder"][langsetting], )
        enterbutton = CTkButton(top, text=lang["Forsæt"][langsetting], command= UDenter)
        cancelbutton = CTkButton(top, text=lang["Fortryd"][langsetting], command=cancel)

        enterlabel.grid(row=1, column=0, pady=(15, 10), padx=padx)
        enterfield.grid(row=2, column=0, pady=(0, 50), padx=padx)
        enterbutton.grid(row=3, column=0, pady=25, padx=padx)
        cancelbutton.grid(row=4, column=0, padx=padx)
        
        enterfield.after(0, enterfield.focus)
        

        top.bind('<Return>', UDenter2)
        top.update()

    def multiaflever():
        top = CTkToplevel()
        top.geometry("300x450")
        top.title(lang["aflevering"][langsetting])
        top.attributes('-topmost', True)

        def AFenter2(event):
            AFenter()

        def AFenter():

            pcnumber = enterfield.get().upper()
            if len(enterfield.get()) == 0 or enterfield.get().isspace() == True:
                CTkLabel(top, text=lang["Insertpc"][langsetting]).grid(row=0, column=0, pady=15)            


            else:
                def dmgenter():
                    manual = damage.get()
                    tegnet = tegnetcheck.get()
                    taster = tastercheck.get()
                    skærm = skærmskade.get()
                    hjørner = hjørneskade.get()

                    dmglist = [tegnet, taster, skærm, hjørner]
                    totaldamage = ""
                    totaldamage = totaldamage + manual
                    print(dmglist)

                    if True in dmglist:
                        if len(totaldamage) > 0:
                            if tegnet:
                                totaldamage += ", Tegnet"

                            if taster:
                                totaldamage += ", Taster mangler"
                            
                            if skærm:
                                totaldamage += ", Skærmskade"
                            
                            if hjørner:
                                totaldamage += ", Hjørneskade"

                        else:
                            if tegnet:
                                totaldamage += "Tegnet"
                                if taster:
                                    totaldamage += ", Taster mangler"
                                
                                if skærm:
                                    totaldamage += ", Skærmskade"
                                
                                if hjørner:
                                    totaldamage += ", Hjørneskade"
                            elif taster:
                                totaldamage += "Taster mangler"
                                if skærm:
                                    totaldamage += ", Skærmskade"
                                
                                if hjørner:
                                    totaldamage += ", Hjørneskade"
                            elif skærm:
                                totaldamage += "Skærmskade"
                                if hjørner:
                                    totaldamage += ", Hjørneskade"
                            elif hjørner:
                                totaldamage += "Hjørneskade"

                            

                    dmgdict[borrowdict.get(pcnumber)] = totaldamage
                    for index in borrowdict:
                        if index == pcnumber:
                            borrowdict.pop(pcnumber)
                            break
                    save()
                    
                    top.destroy()
                    top2.destroy()
                    top2.update()  
                    multiaflever()
                    
                
                def dmgcancel():
                    top2.destroy()
                    top2.update()
                    borrowrefresh()
                
                
                if "FGUSVNPC" not in pcnumber:
                    if "PC" in pcnumber:
                        
                        pcnumber = "FGUSVN" + pcnumber
                    else:
                        
                        pcnumber = "FGUSVNPC" + pcnumber
                
                
                

                if answer.get() == 2:
                    
                    
                    top2 = CTkToplevel()
                    top2.geometry("400x550")
                    top2.title(lang["Skader"][langsetting])
                    top2.attributes('-topmost', True)
                    padx=90
                    top2.config(padx=padx)
                    
                    txt = CTkLabel(top2, text=lang["choosedamage"][langsetting])
                    damage = CTkEntry(top2, placeholder_text=lang["Skader"][langsetting])
                    tegnetcheck = CTkCheckBox(top2, text="Tegnet          ", onvalue=True)
                    tastercheck = CTkCheckBox(top2, text="Tast mangel ", onvalue=True)
                    skærmskade = CTkCheckBox(top2, text="Skærmskade", onvalue=True)
                    hjørneskade = CTkCheckBox(top2, text="Hjørneskade ", onvalue=True)


                    cancelbutton = CTkButton(top2, text=lang["Fortryd"][langsetting], command=dmgcancel)
                    enterbutton = CTkButton(top2, text=lang["Forsæt"][langsetting], command=dmgenter)

                    
                    txt.grid(row=2, column=0, columnspan=2, pady=(15, 0))
                    damage.grid(row=3, column=0, pady=20)
                    tegnetcheck.grid(row=4, column=0, pady=10)
                    tastercheck.grid(row=5, column=0, pady=10)
                    skærmskade.grid(row=6, column=0, pady=10)
                    hjørneskade.grid(row=7, column=0, pady=10,)
                    enterbutton.grid(row=10, column=0, pady=10)
                    cancelbutton.grid(row=11, column=0, pady=10)

                    damage.after(0, damage.focus)
                else:
                    for index in borrowdict:
                        if index == pcnumber:
                            borrowdict.pop(pcnumber)
                            break
                            
                    save()
                    
                    top.destroy()
                    top.update()
                    multiaflever()
                    

        def cancel():
            top.destroy()
            top.update()
            borrowrefresh()
        
        
        padx=65
        answer = IntVar()


        pclabel = CTkLabel(top, text=lang["PcPlaceholder"][langsetting])
        enterfield = CTkEntry(top, placeholder_text=lang["PcPlaceholder"][langsetting])
        enterbutton = CTkButton(top, text=lang["Forsæt"][langsetting], command=AFenter)
        cancelbutton = CTkButton(top, text=lang["Fortryd"][langsetting], command=cancel)
        dmgQuestion = CTkLabel(top, text=lang["Damage"][langsetting]) 
        dmgNo = CTkRadioButton(master=top, text=lang["Nej"][langsetting], variable=answer, value=1,)
        dmgYes = CTkRadioButton(master=top, text=lang["Ja"][langsetting], variable=answer, value=2,)

        pclabel.grid(row=1, column=0, pady=15, padx=padx)
        enterfield.grid(row=2, column=0, columnspan=2, padx=padx, pady=10)
        dmgQuestion.grid(row=3, column=0, columnspan=2, padx=45)
        dmgYes.grid(row=4, column=0, padx=padx, sticky="w",)
        dmgNo.grid(row=5, column=0, padx=padx, pady=5, sticky="w",)
        enterbutton.grid(row=6, column=0,padx=padx, pady=25)
        cancelbutton.grid(row=7,padx=padx, pady=25, column=0,)

        enterfield.after(0, enterfield.focus)
        top.update()
        
        top.bind('<Return>', AFenter2)

    def aflever():
        top = CTkToplevel()
        top.geometry("300x450")
        top.title(lang["aflevering"][langsetting])
        top.attributes('-topmost', True)

        def AFenter2(event):
            AFenter()
        def AFenter():
            pcnumber = enterfield.get().upper()
            if len(enterfield.get()) == 0 or enterfield.get().isspace() == True:
                CTkLabel(top, text=lang["Insertpc"][langsetting]).grid(row=0, column=0, pady=15)            


            else:
                def dmgenter():
                    manual = damage.get()
                    tegnet = tegnetcheck.get()
                    taster = tastercheck.get()
                    skærm = skærmskade.get()
                    hjørner = hjørneskade.get()

                    dmglist = [tegnet, taster, skærm, hjørner]
                    totaldamage = ""
                    totaldamage = totaldamage + manual
                    print(dmglist)

                    if True in dmglist:
                        if len(totaldamage) > 0:
                            if tegnet:
                                totaldamage += ", Tegnet"

                            if taster:
                                totaldamage += ", Taster mangler"
                            
                            if skærm:
                                totaldamage += ", Skærmskade"
                            
                            if hjørner:
                                totaldamage += ", Hjørneskade"

                        else:
                            if tegnet:
                                totaldamage += "Tegnet"
                                if taster:
                                    totaldamage += ", Taster mangler"
                                
                                if skærm:
                                    totaldamage += ", Skærmskade"
                                
                                if hjørner:
                                    totaldamage += ", Hjørneskade"
                            elif taster:
                                totaldamage += "Taster mangler"
                                if skærm:
                                    totaldamage += ", Skærmskade"
                                
                                if hjørner:
                                    totaldamage += ", Hjørneskade"
                            elif skærm:
                                totaldamage += "Skærmskade"
                                if hjørner:
                                    totaldamage += ", Hjørneskade"
                            elif hjørner:
                                totaldamage += "Hjørneskade"

                            

                    dmgdict[borrowdict.get(pcnumber)] = totaldamage
                    for index in borrowdict:
                        if index == pcnumber:
                            borrowdict.pop(pcnumber)
                            break
                    save()
                    
                    top.destroy()
                    top2.destroy()
                    top2.update()  

                def dmgcancel():
                    top2.destroy()
                    top2.update()

                
                
                if "FGUSVNPC" not in pcnumber:
                    if "PC" in pcnumber:
                        
                        pcnumber = "FGUSVN" + pcnumber
                    else:
                        
                        pcnumber = "FGUSVNPC" + pcnumber
                
                
                

                if answer.get() == 2:
                    
                    
                    top2 = CTkToplevel()
                    top2.geometry("400x550")
                    top2.title(lang["Skader"][langsetting])
                    top2.attributes('-topmost', True)
                    padx=90
                    top2.config(padx=padx)
                    
                    txt = CTkLabel(top2, text=lang["choosedamage"][langsetting])
                    damage = CTkEntry(top2, placeholder_text=lang["Skader"][langsetting])
                    tegnetcheck = CTkCheckBox(top2, text="Tegnet          ", onvalue=True)
                    tastercheck = CTkCheckBox(top2, text="Tast mangel ", onvalue=True)
                    skærmskade = CTkCheckBox(top2, text="Skærmskade", onvalue=True)
                    hjørneskade = CTkCheckBox(top2, text="Hjørneskade ", onvalue=True)


                    cancelbutton = CTkButton(top2, text=lang["Fortryd"][langsetting], command=dmgcancel)
                    enterbutton = CTkButton(top2, text=lang["Forsæt"][langsetting], command=dmgenter)

                    
                    txt.grid(row=2, column=0, columnspan=2, pady=(15, 0))
                    damage.grid(row=3, column=0, pady=20)
                    tegnetcheck.grid(row=4, column=0, pady=10)
                    tastercheck.grid(row=5, column=0, pady=10)
                    skærmskade.grid(row=6, column=0, pady=10)
                    hjørneskade.grid(row=7, column=0, pady=10,)
                    enterbutton.grid(row=10, column=0, pady=10)
                    cancelbutton.grid(row=11, column=0, pady=10)

                    damage.after(0, damage.focus)
                else:
                    for index in borrowdict:
                        if index == pcnumber:
                            borrowdict.pop(pcnumber)
                            break
                            
                    save()
                    
                    top.destroy()
                    top.update()
                    borrowrefresh()

        def cancel():
            top.destroy()
            top.update()

        
        
        padx=65
        answer = IntVar()


        pclabel = CTkLabel(top, text=lang["PcPlaceholder"][langsetting])
        enterfield = CTkEntry(top, placeholder_text=lang["PcPlaceholder"][langsetting])
        enterbutton = CTkButton(top, text=lang["Forsæt"][langsetting], command=AFenter)
        cancelbutton = CTkButton(top, text=lang["Fortryd"][langsetting], command=cancel)
        dmgQuestion = CTkLabel(top, text=lang["Damage"][langsetting]) 
        dmgNo = CTkRadioButton(master=top, text=lang["Nej"][langsetting], variable=answer, value=1,)
        dmgYes = CTkRadioButton(master=top, text=lang["Ja"][langsetting], variable=answer, value=2,)

        pclabel.grid(row=1, column=0, pady=15, padx=padx)
        enterfield.grid(row=2, column=0, columnspan=2, padx=padx, pady=10)
        dmgQuestion.grid(row=3, column=0, columnspan=2, padx=45)
        dmgYes.grid(row=4, column=0, padx=padx, sticky="w",)
        dmgNo.grid(row=5, column=0, padx=padx, pady=5, sticky="w",)
        enterbutton.grid(row=6, column=0,padx=padx, pady=25)
        cancelbutton.grid(row=7,padx=padx, pady=25, column=0,)

        enterfield.after(0, enterfield.focus)
        top.update()
        
        top.bind('<Return>', AFenter2)

    def dsplyhist():
        sublevel = CTkToplevel()
        sublevel.title(lang["Historik"][langsetting])
        sublevel.configure(padx=150, pady=100)
        sublevel.attributes('-topmost', True)

        
        
        historylist = Listbox(sublevel, font=("Ariel", 10), bd=1, highlightthickness=0)
        historylist.grid(row=0, column=0, padx=(25,5), pady=15)
        scrollbar = CTkScrollbar(sublevel, command=historylist.yview, button_color=appearmode["color"][apcolor])
        scrollbar.grid(row=0, column=1, sticky="ns", pady=10)
        historylist.config(width=75, height=22, bg=appearmode["background"][apmode], fg=appearmode["foreground"][apmode], yscrollcommand=scrollbar.set)
        
        for x in history:
            
            historylist.insert(0, x,)

    def dsplydmg():
        sublevel = CTkToplevel()
        
        sublevel.title(lang["Skader"][langsetting])
        sublevel.configure(height=150, width=100)
        
        dmglist = Listbox(sublevel, font=("Ariel", 10), bd=1, highlightthickness=0)
        dmglist.grid(row=0, column=0, padx=(25,5), pady=15)
        scrollbar = CTkScrollbar(sublevel, command=dmglist.yview, button_color=appearmode["color"][apcolor])
        scrollbar.grid(row=0, column=1, sticky="ns", pady=10)
        dmglist.config(width=75, height=22, bg=appearmode["background"][apmode], fg=appearmode["foreground"][apmode], yscrollcommand=scrollbar.set)


        for x in dmgdict:
            
            damage = x + " -|- " + dmgdict.get(x)
            dmglist.insert(0, damage)

    def showborrowed():
        global borrowrefresh
        def borrowrefresh():
            
            borrowed.destroy()
            showborrowed()

        borrowed = CTkToplevel()
        borrowed.title(lang["lånte"][langsetting])
        borrowed.configure(padx=100, pady=50)
        borrowed.attributes('-topmost', True)

        sortedborrowdict = sorted(borrowdict)
        
        borrowlist = Listbox(borrowed, font=("Ariel", 10), bd=1, highlightthickness=0)
        borrowlist.grid(row=0, column=0, padx=(25,5), pady=15)
        scrollbar = CTkScrollbar(borrowed, command=borrowlist.yview, button_color=appearmode["color"][apcolor])
        scrollbar.grid(row=0, column=1, sticky="ns", pady=10)
        borrowlist.config(width=55, height=22, bg=appearmode["background"][apmode], fg=appearmode["foreground"][apmode], yscrollcommand=scrollbar.set)

        for label in sortedborrowdict:
            
            borrowlist.insert(END, borrowdict[label], )
            
        refresh = CTkButton(borrowed, text=lang["opdater"][langsetting], command=borrowrefresh).grid(row=1, column=0,padx=15, pady=15)
        borrowed.update()

    height = 36
    width = 160
    fontsize = 15
    
    
    root = CTk()
    root.title("Computer System")
    root.eval('tk::PlaceWindow . Center')
    root.geometry("350x725")
    root.attributes('-topmost', True)
    padx = (300/4, 0 )

    text1 = "Multi " + lang["Udlån"][langsetting]
    text2 = "Multi " + lang["Aflever"][langsetting]

    computerlabel = CTkLabel(root, text="Computer System", font=("", 25))
    udlånbtn = CTkButton(root, text=lang["Udlån"][langsetting],font=("", fontsize), command=Udlån, height=height, width=width)
    multiudlån = CTkButton(root, text=text1, font=("", fontsize), height=height, width=width, command=funcmultiudlån)
    aflever = CTkButton(root, text=lang["Aflever"][langsetting],font=("", fontsize), command=aflever, height=height, width=width)
    mutliaflever = CTkButton(root, text=text2, font=("", fontsize), height=height, width=width, command=multiaflever)
    exit2 = CTkButton(root, text=lang["Luk"][langsetting],font=("", fontsize),command=quitcheck, height=height, width=width)
    currentborrow = CTkButton(root, text=lang["vislånte"][langsetting],font=("", fontsize), command=showborrowed, height=height, width=width)
    historybutton = CTkButton(root, text=lang["Historik"][langsetting],font=("", fontsize), command=dsplyhist, height=height, width=width)
    dmgbutton = CTkButton(root, text=lang["Skader"][langsetting],font=("", fontsize), command=dsplydmg, height=height, width=width)
    settings = CTkButton(root, text="Options", font=("Ariel",10), width=45, command=settings )

    # Put it in grid
    computerlabel.grid(row=0, column=0, pady=25, padx=padx)
    udlånbtn.grid(row=1, column=0, pady=(25,20), padx=padx)
    multiudlån.grid(row=2, column=0, pady=(0,40), padx=padx)
    aflever.grid(row=3, column=0,pady=(0, 20), padx=padx)
    mutliaflever.grid(row=4, column=0, pady=(0, 40), padx=padx)
    historybutton.grid(row=6, column=0, pady=(0,20), padx=padx)
    currentborrow.grid(row=5, column=0,pady=(0,20), padx=padx)
    dmgbutton.grid(row=7, padx=padx,)
    exit2.grid(row=8, column=0, padx=padx, pady=(100, 25))
    settings.grid(row=9, column=1)
    
    root.mainloop()
    
    
if __name__ == "__main__":
    main()
