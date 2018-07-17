import os
import datetime
import pandas as pd
import numpy as np
import re

# for random filenames
import string
import random

#for storing files properly
from django.conf import settings

def write_report(df_f):
    #generate the report file name
    fileName = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)) + ".xlsx"
    filePath = settings.MEDIA_ROOT + fileName

    #write the output to file
    writer = pd.ExcelWriter(filePath, engine='openpyxl')
    df_f.to_excel(writer, "output", index=False)

    workbook  = writer.book
    worksheet = writer.sheets['output']

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
