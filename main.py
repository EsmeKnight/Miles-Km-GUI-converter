from tkinter import *

# functions

# get value of unit
def get_selected():
    choice = variable.get()
    return choice


# calculate conversion
def calculate():
    unit = get_selected()
    num = entry.get().strip()
    print(num)
    num = int(num)
    print(num)
    if unit == "Miles":
        other = "Km"
        res = num * 1.609347
    if unit == "Km":
        other = "Miles"
        res = num / 1.609347
    result_label["text"] = f"{res} {other}"


# create window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=50)
# window.config(padx=20, pady=20)

# entry for number to be converted
entry = Entry()
entry.grid(column=1, row=0)
to_be_converted = entry.get().strip()

# labels
is_equal_to_label = Label(text="Is equal to: ")
is_equal_to_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

# options for making conversion choice
OPTIONS = ["Miles", "Km"]  # more can be added

variable = StringVar(window)
variable.set(OPTIONS[0])  # default value (in this case miles)

unit = OptionMenu(window, variable, *OPTIONS)
unit.grid(column=2, row=0)

# button to execute func
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

# functions as a while loop to keep window open
window.mainloop()
