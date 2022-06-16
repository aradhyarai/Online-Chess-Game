import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

z = input('Enter url: ')
x = input('Enter class you want to search: ')
d = input('Enter what to search: ')
y = input('Enter class you want to search: ')
e = input('Enter what to search: ')
w = input('Enter class you want to search: ')
f = input('Enter what to search: ')

driver = webdriver.Chrome(executable_path='C:\\Users\\91989\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get(z)
results = []
other_results = []
more_results= []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

for a in soup.findAll(attrs=x):
    name = a.find(d)
    if name not in results:
        results.append(name.text)
for b in soup.findAll(attrs=y):
    date = b.find(e)
    if date not in results:
        other_results.append(date.text)

for c in soup.findAll(attrs=w):
    project = c.find(f)
    if project not in results:
        more_results.append(project.text)

df = pd.DataFrame({'Names': results, 'Dates': other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')