from webrequest.scripts.utils import *
from webrequest.models import Report

def create_report(reportKey, pathToZip):
    #read the archive with input file to the memory
    archive = zipfile.ZipFile(pathToZip, 'r')
    filesInArchive = get_list_of_files(archive)

    df_out = pd.DataFrame()

    #convert all the input files
    for i in range(0, len(filesInArchive)):
        fileName = filesInArchive[i]
        df_in = read_file(archive, fileName, Report.objects.all().filter(key=reportKey)[0].delimiter)

        #*************************#
        #----- YOUR CODE HERE -----
        #*************************#

    # write report
    reportPath = write_report(df_out, "output")

    # close the reading session
    archive.close()

    return reportPath
