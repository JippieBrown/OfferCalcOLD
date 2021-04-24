from OfferGUI import app
import tkinter as tk
from tkinter import filedialog

def xmlreader():
    file = filedialog.askopenfilename()#filetype = ("xml", "*.xml"))
    return file#root.find('Projektland').text


def main():
    root = tk.Tk()
    root.withdraw()
    # file = xmlreader()
    app.run(debug=True)

if __name__ == "__main__":
    main()

    