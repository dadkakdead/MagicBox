from webrequest.scripts.utils import *'

def create_report(pathToZip):
    #read the archive with input file to the memory
    archive = zipfile.ZipFile(pathToZip, 'r')
    filesInArchive = get_list_of_files(archive)

    df_out = pd.DataFrame()

    #convert all the input files
    for i in range(0, len(filesInArchive)):
        fileName = filesInArchive[i]

        df_in = pd.read_excel(io.BytesIO(archive.read(fileName)), sheet_name=0, encoding = 'utf-8', index=False)

        #*************************#
        #----- YOUR CODE HERE -----
        #*************************#

    # write report
    reportPath = write_report(df_out)

    # close the reading session
    archive.close()

    return reportPath
