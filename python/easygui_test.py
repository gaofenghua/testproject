import lib_easygui.easygui as gui

#easygui.msgbox("Hello World")
"""
flavor = gui.buttonbox("What's your facorite ice cream flavor?",
                           choices = ['Vanilla', 'chocolate', 'Strawberry'])
"""
flavor = gui.choicebox("What's your facorite ice cream flavor?",
                           choices = ['Vanilla', 'chocolate', 'Strawberry'])

gui.msgbox("You picked" + flavor)
                           
