# ScreenshotTaker
created screenshot taker using python


import pyscreenshot: This line imports the pyscreenshot module which allows us to capture screenshots from the screen.
Note: to import this pyscreenshot you first need to install it using command  pip install pyscreenshot   in command prompt

from tkinter import *: This line imports everything from the tkinter module, which is used for building GUI applications in Python.

def takeScreenShot():: This line defines a function called takeScreenShot that will be used to capture a screenshot.

pyscreenshot.grab().save('My_Screen.png'): This line uses the grab method from the pyscreenshot module to capture a screenshot of the entire screen, and then saves the image as a .png file with the name My_Screen.png.

root = Tk(): This line creates a new instance of the Tk class which is the main window for the GUI application.

root.title("My Screenshot App"): This line sets the title of the main window to "My Screenshot App".

canvas = Canvas(root, width=300, height=300): This line creates a new instance of the Canvas class which is used to draw shapes and graphics on the main window. The root parameter specifies the parent window, and width and height set the size of the canvas.

canvas.pack(): This line arranges the canvas on the main window using the pack geometry manager.

btn = Button(root, text="Take Screenshot", command=takeScreenShot, font=10): This line creates a new instance of the Button class which creates a button in the GUI application. The root parameter specifies the parent window, text sets the text displayed on the button, command specifies the function to be called when the button is clicked, and font sets the font size of the text.

canvas.create_window(150, 150, window=btn): This line creates a window in the canvas for the button, with the coordinates 150, 150 specifying the position of the window in the canvas.

root.mainloop(): This line starts the event loop for the GUI application, which listens for events such as button clicks, mouse movements, and updates the GUI accordingly. The event loop continues to run until the user closes the main window.
