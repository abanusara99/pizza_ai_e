from helperFunctions import *


file_name = "demo_1"

def stt_testing(file):
    print("The transcript from \'" + file_name + "\' is: " + speech_to_text(str(os.getcwd() + "/sample/" + file + ".wav")))

stt_testing(file_name)

def stt_testing(file_name):
    print("The transcript from \'" + file_name + "\' is: " + speech_to_text(str(os.getcwd() + "/sample/" + file_name + ".wav")))

stt_testing("demo_2")