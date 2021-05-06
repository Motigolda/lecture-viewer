from LectureViewer import *
import tkinter as tk
from tkinter import filedialog

def main():
    print("Select video to see in the lecture viewer.")
    root = tk.Tk()
    root.withdraw()
    filepath = filedialog.askopenfilename()
    viewer = LectureViewer(filepath,"הרצאה")
    viewer.launch()

if __name__ == '__main__':
    main()