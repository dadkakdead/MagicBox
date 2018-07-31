import os
from os import listdir
from os.path import isfile, join

import sys

import pandas as pd
import numpy as np
import re

import time
import datetime
import pytz

import string
import random
import math

import zipfile
import io

#for storing files properly
from django.conf import settings
from webrequest.models import Report

def read_file(zf, fileNameFull, delimiter):
    fileName, fileExtension = os.path.splitext(fileNameFull)
    pCsv = re.compile('^.CSV')
    pExcel = re.compile('^.XLS*')

    df_in = pd.DataFrame()

    if not(pCsv.match(fileExtension.upper()) is None):
        df_in = pd.read_csv(io.BytesIO(zf.read(fileNameFull)), delimiter=delimiter, encoding = 'utf-8')

    if not(pExcel.match(fileExtension.upper()) is None):
        df_in = pd.read_excel(io.BytesIO(zf.read(fileNameFull)), sheet_name=0, encoding = 'utf-8', index=False)

    return df_in

def get_list_of_files(zf):
    fileNames = []
    for i in range(0,len(zf.infolist())):
        if not ("__" in zf.infolist()[i].filename):
            fileNames.append(zf.infolist()[i].filename)
    return fileNames

def write_report(df, sheetName):
    # make random file name
    fileName = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)) + ".xlsx"

    try:
        filePath =  settings.MEDIA_ROOT + fileName
    except:
        filePath =  "/home/devrazdev/" + fileName

    # write the output to excel
    writer = pd.ExcelWriter(filePath, engine='openpyxl')
    df.to_excel(writer, sheetName, index=False)

    workbook  = writer.book
    worksheet = writer.sheets[sheetName]

    # automatically scale the columns
    for columnCells in worksheet.columns:
        length = 0
        for cell in columnCells:
            cellValueType = type(cell.value).__name__

            #defaults
            cellText = str(cell.value)
            russianWordsCounter = 0

            if cellValueType == 'unicode':
                cellText = cell.value.encode('utf-8')
                russianWordsCounter = re.search('[а-яА-Я]', cellText)
            else:
                if cellValueType == 'date':
                    cellText = "18/11/1993"

            if russianWordsCounter > 0:
                length = max(length, len(cellText)/2)
            else:
                length = max(length, len(cellText))
            worksheet.column_dimensions[columnCells[0].column].width = length

    writer.save()
    return filePath
