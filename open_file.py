import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

class openFile:
    def __init__(self):
        # Root window
        self.root = tk.Tk()
        self.root.title('Open a Txt-File')
        self.root.resizable(False, False)
        self.root.geometry('150x150')

        self.lbl_info_text = tk.Label(text="Choose a txt file")
        self.lbl_info_text.pack()

            # open file button
        self.open_button = ttk.Button(
            self.root,
            text='Open a File',
            command=self.select_file
        )


        self.open_button.pack(expand=True)
        # self.root.after(10, self.select_file)
        self.root.mainloop()


    def select_file(self):
        # file types
        self.filetypes = (
            ('text files', '*.txt'),
        )
        # show the open file dialog
        self.filepath = fd.askopenfilename(
            title='Open a file',
            # initialdir='/Users/Albert/Docs',
            filetypes=self.filetypes)
        # print(self.filepath)
        self.root.destroy()
        return self.filepath

    # Used for debugging
if __name__ == "__main__":
    openfiledialog = openFile()
    