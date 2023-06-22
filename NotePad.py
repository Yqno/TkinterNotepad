import os
import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class NotePad:

    root = Tk()

    Width = 300
    Height = 300
    TextArea = Text(root)
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)
    HelpMenu = Menu(MenuBar, tearoff=0)
    EditMenu = Menu(MenuBar, tearoff=0)


    def __init__(self,**kwargs):
        # Set the icon for the window
        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        # Set the window size
        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        # Set the window title
        self.__root.title("Untitled - Notepad")

        # Center the window on the screen
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.Width / 2)
        top = (screenHeight / 2) - (self.Height /2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        # Configure grid row and column to make the text area resizable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
        
        # Create and position the text area
        self._TextArea.grid(sticky=N + E + S + W)

        # Create the File menu
        self._FileMenu.add_command(label="New", command=self.newfile)
        self._FileMenu.add_command(label="Open", command=self.openfile)
        self._FileMenu.add_command(label="Save", command=self.saveFile)
        self._FileMenu.add_separator()
        self._FileMenu.add_command(label="Exit", command=self.quitApp)
        self._FileMenu.add_cascade(label="File", menu=self._FileMenu)

        # Create the Edit menu
        self._EditMenu.add_command(label="Cut", command=self.__cut)
        self._EditMenu.add_command(label="Copy", command=self._Copy)
        self._EditMenu.add_command(label="Paste", command=self._Paste)
        self._EditMenu.add_command(label="Edit", command=self._Edit)
        self._FileMenu.add_cascade(label="Help", menu=self._FileMenu)

        # Configure the menu bar
        self.__root.config(menu=self.__MenuBar)

        # Create and position the scrollbar
        self._ScrollBar.pack(side=RIGHT, fill=Y)
        self.ScrollBar.config(command=self._TextArea.yview)
        self.TextArea.config(yscrollcommand=self._ScrollBar.set)

    def quitApp(self):
        # Destroy the application window
        self.__root.destroy()

    def openfile(self):
        # Open a file for editing
        self.file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
        if self.file == "":
            self.file = None
        else:
            self.root.title(os.path.basename(self.__file) + " - Notepad")
            self.TextArea.delete(1.0, END)
            file = open(self.file, "r")

    def newfile(self):
        # Create a new file
        self.root.title("Untitled - Notepad")
        self.file = None
        self.TextArea.delete(1.0, END)

    def saveFile(self):
        # Save the current file
        if self.file == None:
            self.file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
            if self.file == "":
                self.file = None
            else:
                file = open(self.file, "w")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()
                self.__root.title(os.path.basename(self.__file) + " - Notepad")
        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __cut(self):
        # Cut selected text
        self.TextArea.event_generate("Cut")

    def _Copy(self):
        # Copy selected text
        self.TextArea.event_generate("Copy")

    def _Paste(self):
        # Paste clipboard content
        self.TextArea.event_generate("Paste")

        self.__root.mainloop()

# Create and run the Notepad application
notepad = NotePad(width=600, height=400)
notepad.run()
