import pandas as pd
from collections import OrderedDict
from datetime import date

#dict
#Rows -> print
sales = [{'account': 'Jones LLC', 'Jan': 150, 'Feb': 200, 'Mar': 140},
         {'account': 'Alpha Co', 'Jan': 200, 'Feb': 210, 'Mar': 215},
         {'account': 'Blue Inc', 'Jan': 50, 'Feb': 90, 'Mar': 95}]
df = pd.DataFrame(sales)

print 'Row oriented'
print df

#Column -> from_dict
sales = {'account': ['Jones LLC', 'Alpha Co', 'Blue Inc'],
         'Jan': [150, 200, 50],
         'Feb': [200, 210, 90],
         'Mar': [140, 215, 95]}
df = pd.DataFrame.from_dict(sales)

print 'Column oriented'
print df

#change order
df = df[['account', 'Jan', 'Feb', 'Mar']]
print 'Ordered'
print df

#list

#Rows -> from_records
sales = [('Jones LLC', 150, 200, 50),
         ('Alpha Co', 200, 210, 90),
         ('Blue Inc', 140, 215, 95)]
labels = ['account', 'Jan', 'Feb', 'Mar']
df = pd.DataFrame.from_records(sales, columns=labels)

print 'Row oriented'
print df

#Columns -> from_items
sales = [('account', ['Jones LLC', 'Alpha Co', 'Blue Inc']),
         ('Jan', [150, 200, 50]),
         ('Feb', [200, 210, 90]),
         ('Mar', [140, 215, 95]),
         ]
df = pd.DataFrame.from_items(sales)

print 'Column oriented'
print df



create_date = "{:%m-%d-%Y}".format(date.today())
created_by = "kotek"
footer = [('Created by', [created_by]), ('Created on', [create_date]), ('Version', [1.1])]
df_footer = pd.DataFrame.from_items(footer)

print 'Footer'
print df_footer

#to excel, pycharm project localization
writer = pd.ExcelWriter('simple-report.xlsx', engine='xlsxwriter')
df.to_excel(writer, index=False)
df_footer.to_excel(writer, startrow=6, index=False)
writer.save()
