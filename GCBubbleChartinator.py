import os;
import pandas as pd;
import matplotlib.pyplot as mpl;
import seaborn as sns;

print('What is the name of your GC Excel File? Without the extension, please.')
filename = str(input())
filename = filename + '.xlsx'
print('What is the title of your figure?')
title = str(input())

#using pandas to read the data
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path =  os.path.join(script_dir, filename)
data2 = pd.read_excel(f'{script_dir}\\{filename}', index_col=0, sheet_name=0, header=0)

#parsing columns for acid names and index for worm names
acids = pd.Series(data2.columns.values)
worms = pd.Series(data2.index.values)
print('The worms are:')
print(worms)
print('The fatty acids are:')
print(acids)

# replicating worms a bunch to 3 tuple data
# (worm, acid, radius) x a bunch of triplets
threecols ={'worm':[],'acid':[],'rad':[]}
for ind in data2.index:
    for col in data2.columns:
     threecols['worm'].append(ind)
     threecols['acid'].append(col)
     threecols['rad'].append(data2[col][ind])

# using seaborn to draw dots
sns.scatterplot(
   y=threecols['acid'], 
   x= threecols['worm'], 
   size= threecols['rad'], 
   hue=threecols['rad'],
   )

# using mpl to style figure
mpl.xlabel('Worm')
mpl.ylabel('Fatty Acid')
mpl.title(title)
mpl.show()