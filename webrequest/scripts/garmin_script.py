from webrequest.scripts.utils import *

#------------------------------
#------ CUSTOM FUNCTIONS ------
#------------------------------

def convert_time(t):
    t_naive = datetime.datetime.fromtimestamp(t)
    timezone = pytz.timezone("UTC")
    t_aware = timezone.localize(t_naive)

    return t_aware

def print_time(t):
    t_aware = convert_time(t)
    return t_aware.astimezone(pytz.timezone('Etc/GMT+7')).strftime("%H:%M:%S")

def convert_to_binary_string(n):
    return ''.join(str(1 & int(n) >> i) for i in range(0, 32)[::-1])

def merge_timestamps(t, t_16):
    unixEpoch = datetime.datetime(1970, 1, 1, 0, 0, 0, tzinfo=pytz.utc)
    javaEpoch = datetime.datetime(1989, 12, 31, 0, 0, 0, tzinfo=pytz.utc)

    epochDelta = (javaEpoch - unixEpoch).total_seconds()

    return int(convert_to_binary_string(t)[:16] + convert_to_binary_string(t_16)[16:], 2) + epochDelta

def process_data_csv(df_in):
    df_hr = df_in[np.isfinite(df_in['monitoring.heart_rate[bpm]'])][["monitoring.timestamp[s]", "monitoring.timestamp_16[s]", "monitoring.heart_rate[bpm]"]].reset_index(drop=True)

    df_hr["timestamp"] = list(map(merge_timestamps, df_hr["monitoring.timestamp[s]"], df_hr["monitoring.timestamp_16[s]"]))

    df_hr["time"] = list(map(print_time, df_hr["timestamp"]))

    df_hr["heart_rate[bpm]"] = df_hr['monitoring.heart_rate[bpm]']

    return df_hr

def add_minutes(df_in):
    df_out = df_in
    df_out["minutes"] = 0

    for i in range(1,len(df_out)):
        df_out.at[i,"minutes"] = math.ceil((convert_time(df_in.at[i,"timestamp"]) - convert_time(df_in.at[0,"timestamp"])).total_seconds() / 60)

    return df_out

#------------------------------
#------ CUSTOM FUNCTIONS ------
#------------------------------

def create_report(pathToZip):
    #read the archive with input file to the memory
    archive = zipfile.ZipFile(pathToZip, 'r')
    filesInArchive = get_list_of_files(archive)


    df_out = pd.DataFrame()

    for i in range(0, len(filesInArchive)):
        #read file
        df_in = pd.read_csv(io.BytesIO(archive.read(filesInArchive[i])), delimiter=",", encoding = 'utf-8')
        try:
            df_tmp = process_data_csv(df_in)
            df_out = pd.concat([df_out, df_tmp])
        except:
            pass

    #reshape the output
    df_out = add_minutes(df_out.sort_values(by=['timestamp']).reset_index(drop=True))
    df_out = df_out[['minutes', 'time', 'heart_rate[bpm]']][df_out["minutes"] > 0][df_out["heart_rate[bpm]"] > 0].drop_duplicates().reset_index(drop=True)

    # save the report
    sheetName = convert_time(df_tmp.at[0,"timestamp"]).strftime("%d %b %Y")
    reportPath = write_report(df_out, sheetName)

    # close the reading session
    archive.close()

    return reportPath
