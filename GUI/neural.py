# LSTM for international airline passengers problem with regression framing
'''
from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
img = ImageTk.PhotoImage(Image.open("True1.gif"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()
'''

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

browserwindow = None
text = None
cancel_id = None
entry = None

# convert an array of values into a dataset matrix


class AnimatedGif(object):
    """ Animated GIF Image Container. """
    def __init__(self, image_file_path):
        self.image_file_path = image_file_path
        self._frames = []
        self._load()

    def __len__(self):
        return len(self._frames)

    def __getitem__(self, frame_num):
        return self._frames[frame_num]

    def _load(self):
        """ Read in all the frames of a multi-frame gif image. """
        while True:
            frame_num = len(self._frames)  # number of next frame to read
            try:
                frame = PhotoImage(file=self.image_file_path,
                                   format="gif -index {}".format(frame_num))
            except TclError:
                break
            self._frames.append(frame)

def update_label_image(label, ani_img, ms_delay, frame_num):
    global cancel_id
    label.configure(image=ani_img[frame_num])
    frame_num = (frame_num+1) % len(ani_img)
    cancel_id = root.after(
        ms_delay, update_label_image, label, ani_img, ms_delay, frame_num)

def enable_animation():
    global cancel_id
    ms_delay = 1000 // len(ani_img)
    cancel_id = root.after(
        ms_delay, update_label_image, label, ani_img, ms_delay, 0)

def cancel_animation():
    global cancel_id
    if cancel_id is not None:
        root.after_cancel(cancel_id)
        cancel_id = None




def create_dataset(dataset, look_back=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back-1):
		a = dataset[i:(i+look_back), 0]
		dataX.append(a)
		dataY.append(dataset[i + look_back, 0])
	return numpy.array(dataX), numpy.array(dataY)


def run():
    global entry
    # fix random seed for reproducibility
    numpy.random.seed(7)
    # load the dataset
    dataframe = pandas.read_csv('daily-foreign-exchange-rates-31.csv', usecols=[1], engine='python', skipfooter=3)
    dataset = dataframe.values
    dataset = dataset.astype('float32')
    # normalize the dataset
    scaler = MinMaxScaler(feature_range=(0, 1))
    dataset = scaler.fit_transform(dataset)
    # split into train and test sets
    train_size = int(len(dataset) * 0.67)
    test_size = len(dataset) - train_size
    train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]
    # reshape into X=t and Y=t+1
    look_back = 3
    trainX, trainY = create_dataset(train, look_back)
    testX, testY = create_dataset(test, look_back)
    # reshape input to be [samples, time steps, features]
    trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
    testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
    # create and fit the LSTM network
    #print("here")
    model = Sequential()
    model.add(LSTM(4, input_dim=look_back))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    a = model.fit(trainX, trainY, nb_epoch=1,batch_size=1, verbose=2)
    # make predictions
    trainPredict = model.predict(trainX)
    testPredict = model.predict(testX)
    # invert predictions
    trainPredict = scaler.inverse_transform(trainPredict)
    trainY = scaler.inverse_transform([trainY])
    testPredict = scaler.inverse_transform(testPredict)
    testY = scaler.inverse_transform([testY])
    # calculate root mean squared error
    trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
    print('Train Score: %.2f RMSE' % (trainScore))
    testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
    print('Test Score: %.2f RMSE' % (testScore))
    # shift train predictions for plotting
    trainPredictPlot = numpy.empty_like(dataset)
    trainPredictPlot[:, :] = numpy.nan
    trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
    # shift test predictions for plotting
    testPredictPlot = numpy.empty_like(dataset)
    testPredictPlot[:, :] = numpy.nan
    testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict
    # plot baseline and predictions
    plt.plot(scaler.inverse_transform(dataset),label = "original dataset")
    plt.plot(trainPredictPlot,label="predictions for the training dataset")
    plt.plot(testPredictPlot,label="unseen test dataset")
    legend = plt.legend(fontsize=17,loc='upper center', bbox_to_anchor=(0.47, -0.10),fancybox=False, shadow=False, ncol=5)
    plt.savefig("test.png", bbox_extra_artists=(legend,), bbox_inches='tight')
    #plt.show(bbox_extra_artists=(legend,), bbox_inches='tight')


def read_process():
	pass
def close_window():
	global browserwindow
	browserwindow.destroy()
	sys.exit()
def clear():
	global text
	text.delete(1.0, END)
def instructions():
	pass
def askdirectory():
	pass
def run_code():
	#global cancel_id
	#cancel_id = None
	#root = Tk()
	#root.title("Loading")

	#image_file_path = "ajax-loader.gif"
	#ani_img = AnimatedGif(image_file_path)

	#label = Label(image=ani_img[0])  # display first frame initially
	#label.pack()
	#enable_animation()

	global text
	stdout = sys.stdout
	result = StringIO.StringIO()
	sys.stdout = result
	run()
	sys.stdout = stdout
	result_string = result.getvalue()
	text.insert(INSERT, result_string)


def load_gui():
    global browserwindow
    global entry
    global text

    browserwindow = Tk()
    output_frame = Frame(browserwindow)
    parameters_frame = Frame(browserwindow)

    browserwindow.title('Neural Network')

    '''label = Label(parameters_frame,text = "Number of epoch")
    entry = Entry(parameters_frame,width=50)
    button = Button(parameters_frame, text='Run', width = "10",command = run_code)
    exit_button = Button (parameters_frame, text = "EXIT", width = "10",command = close_window)
    button2 = Button(parameters_frame, text='Clear',width = "10", command = clear)
    text = Text(output_frame,width =160,height =30,insertborderwidth=3,background = "grey")

    parameters_frame.pack(side=LEFT)

    label.pack()
    entry.pack()
    button.pack()
    button2.pack()
    exit_button.pack()

    output_frame.pack(side=RIGHT)
    text.pack(side= RIGHT)'''

    parameters_frame.pack(side=LEFT)
    output_frame.pack(side=RIGHT)

    text = Text(output_frame,width =160,height =30,insertborderwidth=3,background = "black")
    text.pack(side= RIGHT)

    epoch_frame = Frame(parameters_frame)
    label = Label(epoch_frame,text = "Number of epoch")
    entry = Entry(epoch_frame,width=50)

    button_frame = Frame(parameters_frame)
    run_button = Button(button_frame, text='Run', width = "10",command = run_code)
    exit_button = Button (button_frame, text = "EXIT", width = "10",command = close_window)
    clear_button = Button(button_frame, text='Clear',width = "10", command = clear)


    epoch_frame.pack()
    label.pack(side=LEFT)
    entry.pack(side=RIGHT)

    button_frame.pack()
    run_button.pack(side=LEFT)
    clear_button.pack(side=LEFT)
    exit_button.pack(side=LEFT)

    browserwindow.mainloop()

'''
def load_gui():
    global browserwindow
    global entry
    global text
    browserwindow = Tk()
    frame = Frame(browserwindow)
    frame1 = Frame(browserwindow)
    browserwindow.title('Neural Network')
    #label3 = Label(browserwindow,text = "DEVELOPED BY Abhishek Jain and PK")
    label = Label(browserwindow,text = "Number of epoch")
    #label1 = Label(browserwindow,text = "The result is as follows :")
    #label2 = Label(browserwindow,text = "IR DOCUMENT RETRIEVER retrieves documents based on the entered queries \n and also prints their respective probabilities")
    #label4 = Label(browserwindow,text="Browse to insert the Directory path")
    entry = Entry(browserwindow,width=50)
    #entry1= Entry(browserwindow,width=50)
    #entry.insert(0, "My default text here")
    button = Button(frame, text='Run', width = "10",command = run_code)
    button1 = Button (browserwindow, text = "EXIT", width = "10",command = close_window)
    button2 = Button(frame, text='Clear',width = "10", command = clear)

    #button3 = Button(browserwindow,text = "INSTRUCTIONS",width="10",command=instructions)
    #button4 = Button(frame1,text = "Browse",width="10",command=askdirectory)
    #button5 = Button(frame1,text = "Train",width="10",command=runcode)
    text = Text(browserwindow,width =160,height =30,insertborderwidth=3,background = "grey")
    #label2.pack(side=TOP)
    #button3.pack(side=TOP)
    #label4.pack(side=TOP)
    #entry1.pack(side=TOP)
    frame1.pack(side=LEFT)
    #button4.pack(side=LEFT)
    #button5.pack(side=LEFT)
    label.pack(side=LEFT)
    entry.pack(side=LEFT)
    button.pack(side=LEFT)
    button2.pack(side=LEFT)
    button1.pack(side = LEFT)
    frame.pack(side=RIGHT)

    #label1.pack(side=TOP)
    text.pack(side= RIGHT)
    #label3.pack(side=BOTTOM)
    browserwindow.mainloop()


'''


if __name__ == "__main__":
	'''# fix random seed for reproducibility
	numpy.random.seed(7)
	# load the dataset
	dataframe = pandas.read_csv('international-airline-passengers.csv', usecols=[1], engine='python', skipfooter=3)
	dataset = dataframe.values
	dataset = dataset.astype('float32')


	# normalize the dataset
	scaler = MinMaxScaler(feature_range=(0, 1))
	dataset = scaler.fit_transform(dataset)


	# split into train and test sets
	train_size = int(len(dataset) * 0.67)
	test_size = len(dataset) - train_size
	train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]


	# reshape into X=t and Y=t+1
	look_back = 1
	trainX, trainY = create_dataset(train, look_back)
	testX, testY = create_dataset(test, look_back)


	# reshape input to be [samples, time steps, features]
	trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
	testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

	# create and fit the LSTM network
	model = Sequential()
	model.add(LSTM(4, input_dim=look_back))
	model.add(Dense(1))
	model.compile(loss='mean_squared_error', optimizer='adam')
	model.fit(trainX, trainY, nb_epoch=1, batch_size=1, verbose=2)


	# make predictions
	trainPredict = model.predict(trainX)
	testPredict = model.predict(testX)


	# invert predictions
	trainPredict = scaler.inverse_transform(trainPredict)
	trainY = scaler.inverse_transform([trainY])
	testPredict = scaler.inverse_transform(testPredict)
	testY = scaler.inverse_transform([testY])


	# calculate root mean squared error
	trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
	print('Train Score: %.2f RMSE' % (trainScore))
	testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
	print('Test Score: %.2f RMSE' % (testScore))


	# shift train predictions for plotting
	trainPredictPlot = numpy.empty_like(dataset)
	trainPredictPlot[:, :] = numpy.nan
	trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict


	# shift test predictions for plotting
	testPredictPlot = numpy.empty_like(dataset)
	testPredictPlot[:, :] = numpy.nan
	testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict


	# plot baseline and predictions
	plt.plot(scaler.inverse_transform(dataset),label = "original dataset")
	plt.plot(trainPredictPlot,label="predictions for the training dataset")
	plt.plot(testPredictPlot,label="unseen test dataset")
	legend = plt.legend(fontsize=17,loc='upper center', bbox_to_anchor=(0.47, -0.10),fancybox=False, shadow=False, ncol=5)
	plt.savefig("test.png", bbox_extra_artists=(legend,), bbox_inches='tight')
	#plt.show(bbox_extra_artists=(legend,), bbox_inches='tight')
	stdout = sys.stdout
	result = StringIO.StringIO()
	sys.stdout = result
	run()
	sys.stdout = stdout
	result_string = result.getvalue()'''
	#print(type(result_string))
	run()
	#load_gui()
