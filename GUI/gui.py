from Tkinter import *
import tkMessageBox
import tkFileDialog
import os
import StringIO
import numpy
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import pandas
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

from tkFileDialog import askopenfilename

browserwindow = None
text = None
cancel_id = None
training_file = None
file_var = None
optimizer_variable = None


def clear():
	global text
	text.delete(1.0, END)

def close_window():
    global browserwindow
    browserwindow.destroy()
    sys.exit()

def fetchfile():
    global training_file
    global file_var
    file_path = askopenfilename()
    print(file_path)
    file_var.set(file_path)

def parameter_packer(frame,label,entry):
    frame.pack(side=TOP)
    label.pack(side=LEFT)
    entry.pack(side=RIGHT)


def load_gui_backup():
    global browserwindow
    global text
    global file_var
    global optimizer_variable

    browserwindow = Tk()
    browserwindow.resizable(width=False, height=False)

    #FRAMES
    parameters_frame = Frame(browserwindow,width=700,height=600)
    output_frame = Frame(browserwindow)
    parameters_frame.pack_propagate(False)
    #output_frame.pack_propagate(False)


    #Packing containing FRAMES

    parameters_frame.pack(side=LEFT)
    output_frame.pack(side=TOP)
    #output text in output_frame

    text = Text(output_frame,width=100,height=45,insertborderwidth=3,background="black")
    text.pack()

    #parameters input frames and Packing

    '''epoch_frame = Frame(parameters_frame)
    epoch_label = Label(epoch_frame, text = "Number of epoch ")
    epoch_entry = Entry(epoch_entry,width=50)'''

    heading_frame  = Frame(parameters_frame)
    heading_label = Label(heading_frame,text = "PARAMETER(S) :")


    filename_frame = Frame(parameters_frame)
    filename_label = Label(filename_frame, text = "Load input filename :")
    filename_load_button = Button(filename_frame,text= "Browse",width="10",command=fetchfile)

    file_var = StringVar()
    file_var.set("")
    file_frame = Frame(parameters_frame)
    file_label = Label(file_frame,textvariable=file_var)

    training_percent_frame = Frame(parameters_frame)
    training_percent_label = Label(training_percent_frame, text = "Training percentage : ")
    training_percent_entry = Entry(training_percent_frame,width=10)

    n_dropout_layers_frame = Frame(parameters_frame)
    n_dropout_layers_label = Label(n_dropout_layers_frame, text = "Number of dropout layers : ")
    n_dropout_layers_entry = Entry(n_dropout_layers_frame,width=10)

    optimizer_frame = Frame(parameters_frame)
    optimizer_label = Label(optimizer_frame,text = "Optimizer type :")
    OPTIMIZER_OPTIONS = ["adam","SGD","nadam","adamax","RMSprop"]
    optimizer_variable = StringVar(optimizer_frame)
    optimizer_variable.set(OPTIMIZER_OPTIONS[0])
    optimizer_dropdown = apply(OptionMenu,(optimizer_frame,optimizer_variable)+tuple(OPTIMIZER_OPTIONS))

    layer_dimention_frame = Frame(parameters_frame)
    layer_dimention_label = Label(layer_dimention_frame, text = "Layer dimentions [LAYERDIM1,LAYERDIM2,...] : ")
    layer_dimention_entry = Entry(layer_dimention_frame,width=15)

    learning_rate_frame = Frame(parameters_frame)
    learning_rate_label = Label(learning_rate_frame, text = "Learning rate :")
    learning_rate_entry = Entry(learning_rate_frame,width=10)

    momentum_frame = Frame(parameters_frame)
    momentum_label = Label(momentum_frame, text = "Momentum :")
    momentum_entry = Entry(momentum_frame,width=10)



    #packing inner frames,entries and buttons

    heading_frame.pack(side=TOP)
    heading_label.pack()

    filename_frame.pack(side=TOP)
    filename_label.pack(side=LEFT)
    filename_load_button.pack(side=RIGHT)

    file_frame.pack(side=TOP)
    file_label.pack(side=LEFT)

    training_percent_frame.pack(side=TOP)
    training_percent_label.pack(side=LEFT)
    training_percent_entry.pack(side=RIGHT)

    n_dropout_layers_frame.pack(side=TOP)
    n_dropout_layers_label.pack(side=LEFT)
    n_dropout_layers_entry.pack(side=RIGHT)

    optimizer_frame.pack(side=TOP)
    optimizer_label.pack(side=LEFT)
    optimizer_dropdown.pack(side=RIGHT)

    layer_dimention_frame.pack(side=TOP)
    layer_dimention_label.pack(side=LEFT)
    layer_dimention_entry.pack(side=RIGHT)

    learning_rate_frame.pack(side=TOP)
    learning_rate_label.pack(side=LEFT)
    learning_rate_entry.pack(side=RIGHT)

    momentum_frame.pack(side=TOP)
    momentum_label.pack(side=LEFT)
    momentum_entry.pack(side=RIGHT)

    #Run the GUI browserwindow mainloop

    browserwindow.mainloop()



def load_gui():
    global browserwindow
    global text
    global file_var
    global optimizer_variable

    browserwindow = Tk()
    browserwindow.resizable(width=False, height=False)

    #FRAMES
    parameters_frame = Frame(browserwindow,width=700,height=600)
    output_frame = Frame(browserwindow)
    parameters_frame.pack_propagate(False)
    #output_frame.pack_propagate(False)


    #Packing containing FRAMES

    parameters_frame.pack(side=LEFT)
    output_frame.pack(side=TOP)
    #output text in output_frame

    text = Text(output_frame,width=100,height=45,insertborderwidth=3,background="black")
    text.pack()

    #parameters input frames and Packing

    heading_frame  = Frame(parameters_frame)
    heading_label = Label(heading_frame,text = "PARAMETER(S) :")


    filename_frame = Frame(parameters_frame)
    filename_label = Label(filename_frame, text = "Load input filename :")
    filename_load_button = Button(filename_frame,text= "Browse",width="10",command=fetchfile)

    file_var = StringVar()
    file_var.set("")
    file_frame = Frame(parameters_frame)
    file_label = Label(file_frame,textvariable=file_var)

    sub_parameter_frame = Frame(parameters_frame)


    training_percent_label = Label(sub_parameter_frame, text = "Training percentage : ")
    training_percent_entry = Entry(sub_parameter_frame,width=10)


    n_dropout_layers_label = Label(sub_parameter_frame, text = "Number of dropout layers : ")
    n_dropout_layers_entry = Entry(sub_parameter_frame,width=10)


    optimizer_label = Label(sub_parameter_frame,text = "Optimizer type :")
    OPTIMIZER_OPTIONS = ["adam","SGD","nadam","adamax","RMSprop"]
    optimizer_variable = StringVar(sub_parameter_frame)
    optimizer_variable.set(OPTIMIZER_OPTIONS[0])
    optimizer_dropdown = apply(OptionMenu,(sub_parameter_frame,optimizer_variable)+tuple(OPTIMIZER_OPTIONS))
    optimizer_dropdown.config(width=10)

    layer_dimention_frame = Frame(parameters_frame)
    layer_dimention_label = Label(layer_dimention_frame, text = "Layer dimentions [LAYERDIM1,LAYERDIM2,...] : ")
    layer_dimention_entry = Entry(layer_dimention_frame,width=15)

    learning_rate_frame = Frame(parameters_frame)
    learning_rate_label = Label(learning_rate_frame, text = "Learning rate :")
    learning_rate_entry = Entry(learning_rate_frame,width=10)

    momentum_frame = Frame(parameters_frame)
    momentum_label = Label(momentum_frame, text = "Momentum :")
    momentum_entry = Entry(momentum_frame,width=8)



    #packing inner frames,entries and buttons

    heading_frame.pack(side=TOP)
    heading_label.pack()

    filename_frame.pack(side=TOP)
    filename_label.pack()
    filename_load_button.pack()

    file_frame.pack(side=TOP)
    file_label.pack(side=LEFT)

    sub_parameter_frame.pack()

    training_percent_label.grid(row=3)
    training_percent_entry.grid(row=3,column=1)

    n_dropout_layers_label.grid(row=4)
    n_dropout_layers_entry.grid(row=4,column=1)

    optimizer_label.grid(row=5)
    optimizer_dropdown.grid(row=5,column=1)



    #Run the GUI browserwindow mainloop

    browserwindow.mainloop()









if __name__ == "__main__":
    load_gui()
