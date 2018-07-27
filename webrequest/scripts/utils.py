import os
from os import listdir
from os.path import isfile, join

import sys

import datetime
import pandas as pd
import numpy as np
import re

import string
import random

import zipfile
import io

#for storing files properly
from django.conf import settings

def write_report(df):
    # make random file name
    fileName = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)) + ".xlsx"
    filePath = settings.MEDIA_ROOT + fileName

    # write the output to excel
    writer = pd.ExcelWriter(filePath, engine='openpyxl')
    df.to_excel(writer, "output", index=False)

    workbook  = writer.book
    worksheet = writer.sheets['output']

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

# when i archived 2 excel files on Mac, it turned out to be 5 files in the archive
# this utility function helps count real files in the archive
def get_list_of_files(zf):
    fileNames = []
    for i in range(0,len(zf.infolist())):
        if not ("__" in zf.infolist()[i].filename):
            fileNames.append(zf.infolist()[i].filename)
    return fileNames
