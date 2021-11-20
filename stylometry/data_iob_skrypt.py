import os
import numpy as np
import pandas as pd
from sklearn.utils import Bunch


def load_train_data():   
    arr = 'c:\\Users\wysoc\desktop\dane_iob\\train'
    #print (arr)
    #data = pd.DataFrame({[string] : []})

    target = np.empty((150,), np.int64)

    data1 = list()
    target_names = ['sien','prus']
    data = np.empty((150,150))
    #target = np.empty(4)
    thisdir = os.getcwd()
    #print (thisdir)
    i = 0
    for r,d,f in os.walk(arr):

        for file in f:

            #print(os.path.basename(os.path.dirname(os.path.join(r, file))))
            #print(os.path.basename(os.path.join(r, file)))
            #print (i)
            with open(os.path.join(r, file),'r',encoding='utf-8') as text:
                data1.append(text.read())
                #data.append(text.read())
                if os.path.basename(os.path.dirname(os.path.join(r, file))) == 'sien':
                    target[i] = np.asarray(0, np.int64)
                else:
                    target[i] = np.asarray(1, np.int64)
            i=i+1       


    #df = pd.DataFrame(data, columns=['string_values'])
    #print(df)       
    data = data1    
    return  Bunch(data = data, target = target, target_names=target_names)

def load_test_data():   
    arr = 'c:\\Users\wysoc\desktop\dane_iob\\test'
    #print (arr)
    #data = pd.DataFrame({[string] : []})

    target = np.empty((60,), np.int64)
    data = list()
    target_names = ['sien','prus']
    #target = np.empty(4)
    thisdir = os.getcwd()
    #print (thisdir)
    i = 0
    for r,d,f in os.walk(arr):

        for file in f:

            #print(os.path.basename(os.path.dirname(os.path.join(r, file))))
            #print(os.path.basename(os.path.join(r, file)))
            #print (i)
            with open(os.path.join(r, file),'r',encoding='utf-8') as text:
                data.append(text.read())
                #data.append(text.read())
                if os.path.basename(os.path.dirname(os.path.join(r, file))) == 'sien':
                    target[i] = np.asarray(0, np.int64)
                else:
                    target[i] = np.asarray(1, np.int64)
            i=i+1       


    #df = pd.DataFrame(data, columns=['string_values'])
    #print(df)           
    return  Bunch(data = data, target = target, target_names=target_names)    