from pandas import DataFrame
import pandas as pd


result = pd.DataFrame(columns=['title', 'text', 'wDate', 'name', 'emails', 'Media', 'area', 'grades', 'gain1', 'gain2', 'gain3','gain4', 'gain5', 'rank'])

print(result)

title = pd.Series('aaa'); text = pd.Series('bbb'); wDate = pd.Series('ccc');  name =pd.Series('ddd');  emails = pd.Series('eee'); Media = pd.Series( 'fff'); area = pd.Series( 'ggg');  grades = pd.Series(1)
gain1 = pd.Series(2 );  gain2 = pd.Series(3); gain3 = pd.Series( 4);  gain4 =pd.Series(5 );  gain5 = pd.Series(6);  rank = pd.Series(6)


temp = DataFrame(
    {'title': title, 'text': text, 'wDate': wDate, 'name': name, 'emails': emails, 'Media': Media, 'area': area,
     'grades': grades, 'gain1': gain1, 'gain2': gain2, 'gain3': gain3, 'gain4': gain4, 'gain5': gain5, 'rank': rank},
    columns=['title', 'text', 'wDate', 'name', 'emails', 'Media', 'area', 'grades', 'gain1', 'gain2', 'gain3',
             'gain4', 'gain5', 'rank'])

print(temp)

result = pd.concat([result,temp,temp])
result.reset_index()

print(result)