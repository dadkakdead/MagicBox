from webrequest.scripts.utils import *

def create_report(pathToZip):
    #read the archive with input file to the memory
    archive = zipfile.ZipFile(pathToZip, 'r')
    filesInArchive = get_list_of_files(archive)

    #convert all the templates
    for i in range(0, len(filesInArchive)):
        fileName = filesInArchive[i]

        df = pd.read_excel(io.BytesIO(archive.read(fileName)), sheet_name=0, encoding = 'utf-8', index=False)

        if "tchannels" in fileName:
            df_tchannels = df
            tchannels_list = df_tchannels[["resultId"]].applymap(lambda x: x.replace("@","").lower()).drop_duplicates()
            tchannels_list.columns = ["channel"]
            tchannels_list["tchannels"] = 1

        if "tlgrm" in fileName:
            df_tlgrm = df
            tlgrm_list = df_tlgrm[["resultId"]].applymap(lambda x: x.replace("@","").lower()).drop_duplicates()
            tlgrm_list.columns = ["channel"]
            tlgrm_list["tlgrm"] = 1

        if "tsearch" in fileName:
            df_tsearch = df
            tsearch_list = df_tsearch[["resultId"]].applymap(lambda x: x.replace("@","").lower()).drop_duplicates()
            tsearch_list.columns = ["channel"]
            tsearch_list["tsearch"] = 1

        if "intento" in fileName:
            df_intento = df
            intento_list = df_intento[["channel id"]].applymap(lambda x: x.replace("@","").lower()).drop_duplicates()
            intento_list.columns = ["channel"]
            intento_list["intento"] = 1

    df_concatenated = pd.DataFrame(pd.concat([tchannels_list, tlgrm_list, tsearch_list, intento_list], sort=True)["channel"]).drop_duplicates()

    df_merged = df_concatenated.merge(tchannels_list, on='channel', how='left').merge(tlgrm_list, on='channel', how='left').merge(tsearch_list, on='channel', how='left').merge(intento_list, on='channel', how='left')

    df_filtered = df_merged.replace(np.nan, '', regex=True)

    reportPath = write_report(df_filtered, "output")
    archive.close()
    return reportPath
