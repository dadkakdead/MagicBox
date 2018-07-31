from webrequest.scripts.utils import *

def create_report(pathToZip):
    #read the archive with input file to the memory
    archive = zipfile.ZipFile(pathToZip, 'r')
    filesInArchive = get_list_of_files(archive)

    df_out = pd.DataFrame()

    #convert all the input files
    for i in range(0, len(filesInArchive)):
        fileNameFull = filesInArchive[i]

        fileName, fileExtension = os.path.splitext(fileNameFull)

        pCsv = re.compile('^CSV')
        pExcel = re.compile('^XLS*')

        if not(pCsv.match(fileExtension.upper()) is None):
            pass #df_in = pd.read_csv(io.BytesIO(archive.read(fileNameFull)), delimiter=",", encoding = 'utf-8')

        if not(pExcel.match(fileExtension.upper()) is None):
            pass #df_in = pd.read_excel(io.BytesIO(archive.read(fileNameFull)), sheet_name=0, encoding = 'utf-8', index=False)

        #*************************#
        #----- YOUR CODE HERE -----
        #*************************#

    # write report
    reportPath = write_report(df_out, "output")

    # close the reading session
    archive.close()

    return reportPath
