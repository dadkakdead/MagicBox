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

from .utils import write_report

def create_telegram_channels_report(paths):
    for filePath in paths:
        revPath = str(filePath)[::-1]
        revFileName = revPath[:revPath.find("/")]
        fileName = revFileName[::-1]

        df = pd.read_excel(filePath, sheet_name=0, encoding = 'utf-8', index=False)

        if "tchannels" in fileName:
            df_tchannels = df
            tchannels_list = df_tchannels[["resultId"]].applymap(lambda x: x.replace("@","").lower()).drop_duplicates()
            tchannels_list.columns = ["channel"]
            tchannels_list["source"] = "tchannels"

        if "tlgrm" in fileName:
            df_tlgrm = df
            tlgrm_list = df_tlgrm[["resultId"]].applymap(lambda x: x.replace("@","").lower()).drop_duplicates()
            tlgrm_list.columns = ["channel"]
            tlgrm_list["source"] = "tlgrm"

        if "tsearch" in fileName:
            df_tsearch = df
            tsearch_list = df_tsearch[["resultId"]].applymap(lambda x: x.replace("@","").lower()).drop_duplicates()
            tsearch_list.columns = ["channel"]
            tsearch_list["source"] = "tsearch"

        if "intento" in fileName:
            df_intento = df
            intento_list = df_intento[["channel id"]].applymap(lambda x: x.replace("@","").lower()).drop_duplicates()
            intento_list.columns = ["channel"]
            intento_list["source"] = "intento"

    df_concatenated = pd.DataFrame(pd.concat([tchannels_list, tlgrm_list, tsearch_list, intento_list])["channel"]).drop_duplicates()

    df_merged = df_concatenated.merge(tchannels_list, on='channel', how='left').merge(tlgrm_list, on='channel', how='left').merge(tsearch_list, on='channel', how='left').merge(intento_list, on='channel', how='left')

    df_filtered = df_merged.replace(np.nan, '', regex=True)
    df_filtered.columns = ["channel", "source 1", "source 2", "source 3", "source 4"]

    reportPath = write_report(df_filtered)
    return reportPath
