import pandas as pd

import glob
[2]
#getting the files required for concatenation

path = r'C:/Users/agheorghitoiu/Downloads/Monthly Views per Product Group'

all_files = glob.glob(path + '/*.xlsx')

li = []
[3]
for filename in all_files:
    df = pd.read_excel(filename, index_col=None, header=0)
    li.append(df)
[4]
#concatening the files all together

frame =pd.concat(li, axis=0, ignore_index=True)
[5]
#checking the dataframe

frame

[6]
frame.describe()

[7]
frame.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 201210 entries, 0 to 201209
Data columns (total 9 columns):
 #   Column            Non-Null Count   Dtype         
---  ------            --------------   -----         
 0   Unnamed: 0        201210 non-null  int64         
 1   Title             201193 non-null  object        
 2   User Id           201210 non-null  int64         
 3   Username          201210 non-null  object        
 4   Type              201210 non-null  object        
 5   date              201210 non-null  datetime64[ns]
 6   Total View Count  201210 non-null  int64         
 7   Group Name        201210 non-null  object        
 8   Application Name  201210 non-null  object        
dtypes: datetime64[ns](1), int64(3), object(5)
memory usage: 13.8+ MB

[8]
#dropping an unncecessary column

frame.drop(['Unnamed: 0'], inplace=True, axis=1)

frame.head()

[9]
#changing the data format for 1 column to save space

frame = frame.astype({'Total View Count': 'int16'})

#checking the data format again

frame.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 201210 entries, 0 to 201209
Data columns (total 8 columns):
 #   Column            Non-Null Count   Dtype         
---  ------            --------------   -----         
 0   Title             201193 non-null  object        
 1   User Id           201210 non-null  int64         
 2   Username          201210 non-null  object        
 3   Type              201210 non-null  object        
 4   date              201210 non-null  datetime64[ns]
 5   Total View Count  201210 non-null  int16         
 6   Group Name        201210 non-null  object        
 7   Application Name  201210 non-null  object        
dtypes: datetime64[ns](1), int16(1), int64(1), object(5)
memory usage: 11.1+ MB

[10]
#generating a new Excel file containing the existing concatenated files

writer = pd.ExcelWriter('Views_Special_Edition.xlsx',
                       engine='xlsxwriter',
                       engine_kwargs={'options': {'strings_to_urls':False}}
                       )
frame.to_excel(writer)

writer.close()