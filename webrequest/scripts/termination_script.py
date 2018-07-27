from webrequest.scripts.utils import *

#convert dates
def convert_1c_date(dateValue):
    return pd.to_datetime(dateValue, format='%d.%m.%Y', utc=True).date()

def convert_1c_template(df, df_output_columns):
    #rename the column with empty title
    df.rename(columns={'Unnamed: 1':''}, inplace=True)

    #fix the column names (1C exports titles in merged cells)
    list1 = list(df.columns.values);
    list2 = list(df.iloc[0].replace(np.nan, '', regex=True));
    df.columns = list(map(lambda x, y: (x + ' ' + y).strip(), list1, list2))

    #drop the top-1 line
    df = df.drop(0);

    #combine columns in one
    df['Location'] = df['Location Country'].map(str) + ', ' + df['City'];
    df = df.drop(columns=['Location Country', 'City']);

    df['Date of hire'] = df['Date of hire'].apply(convert_1c_date)
    df['Date of termination'] = df['Date of termination'].apply(convert_1c_date)

    #get manager name columns in one
    df['Manager'] = ''

    for index, row in df.iterrows():
        if index > 0:
            if pd.isnull(row['Team leader']):
                if pd.isnull(row['Unit manager']):
                    if pd.isnull(row['Department manager']):
                        if pd.isnull(row['SLTmanager']):
                            pass
                        else:
                            df.at[index, 'Manager'] = row['SLTmanager']
                    else:
                        df.at[index, 'Manager'] = row['Department manager']
                else:
                    df.at[index, 'Manager'] = row['Unit manager']
            else:
                df.at[index, 'Manager'] = row['Team leader']

    #bring termination type to single format
    df['Termination type'] = df['Termination type'].replace([r'^voluntary', r'^involuntary'], ['Employee', 'Company'], regex=True)

    #return the converted template
    df_f = df[['Name eng',
                'JobTitle',
                'Manager',
                'Location',
                'Date of hire',
                'Date of termination',
                'Termination type',
                'Resignation reason for statistic']].drop_duplicates()

    df_f.columns = df_output_columns
    return df_f

#convert Lanteria dates
def convert_lanteria_date(dateValue):
    dateValue = pd.to_datetime(dateValue, format='%d %b %Y', utc=True).date()
    return dateValue

def convert_lanteria_template(df, df_output_columns):
    if not('Manager' in df):
        df['Manager'] = ''

    if not('Location' in df):
        df['Location'] = ''

    if not('Date of hire' in df):
        df['Date of hire'] = ''

    df['Termination Date'] = df['Termination Date'].apply(convert_lanteria_date)

    df_f = df[['Employee',
                'Job Position',
                'Manager',
                'Location',
                'Date of hire',
                'Termination Date',
                'Initiator',
                'Reason']].drop_duplicates();

    df_f.columns = df_output_columns
    return df_f

def create_report(pathToZip):
    #template identificator
    df_1C_columns = ['Location',
                            'Организация',
                            'Cost center',
                            'Cost center function',
                            'SLTmanager',
                            'Department manager',
                            'Unit manager',
                            'Team leader',
                            'Name eng',
                            'Name rus',
                            'Job grade',
                            'Job grade level',
                            'Specialization',
                            'Workbook Title RUS',
                            'Date of hire',
                            'Date of termination',
                            'Employment type',
                            'Type of contract',
                            'Resignation reason',
                            'Resignation reason for statistic',
                            'Termination type',
                            'Good bad']

    #template identificator
    df_Lanteria_columns = ['Initiator',
                                'Job Position',
                                'Employment Type',
                                'FTE',
                                'Employee',
                                'Termination Date',
                                'Job Role',
                                'Department',
                                'Reason']

    df_output_columns = ["Full Name",
                        "Job Title",
                        "Manager",
                        "Location",
                        "Date of hire",
                        "Date of termination",
                        "Termination type",
                        "Resignation reason"]

    MIN_DIFF_COLUMNS = 3

    #initialize empty output dataframe
    df_f = pd.DataFrame()

    #read the archive with input file to the memory
    archive = zipfile.ZipFile(pathToZip, 'r')
    filesInArchive = get_list_of_files(archive)

    #convert all the templates
    for i in range(0, len(filesInArchive)):
        fileName = filesInArchive[i]
        df = pd.read_excel(io.BytesIO(archive.read(fileName)), sheet_name=0, encoding = 'utf-8', index=False)

        # input template has unique combination of columns' titles (signature)
        # to guess the input type we compare input signature to templates' signatures
        df_diff_1C_template = len(df_1C_columns) - np.sum([1 * int(df_1C_columns[i] in df.columns) for i in range(len(df_1C_columns))])
        df_diff_Lanteria_template = len(df_Lanteria_columns) - np.sum([1 * int(df_Lanteria_columns[i] in df.columns) for i in range(len(df_Lanteria_columns))])

        df_c = pd.DataFrame()
        #matching criteria is the number of non-matching columns; if it's below the threshold - it's a match
        if df_diff_1C_template < MIN_DIFF_COLUMNS or df_diff_Lanteria_template < MIN_DIFF_COLUMNS:
            if df_diff_1C_template < MIN_DIFF_COLUMNS:
                df_c = convert_1c_template(df, df_output_columns)
            if df_diff_Lanteria_template < MIN_DIFF_COLUMNS:
                df_c = convert_lanteria_template(df, df_output_columns)
        else:
            pass

        df_f = pd.concat([df_f, df_c]).reset_index(drop=True)

    reportPath = write_report(df_f)
    archive.close()
    return reportPath
