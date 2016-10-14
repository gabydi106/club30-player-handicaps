import csv
import requests
from BeautifulSoup import BeautifulSoup


list_of_rows = []

# RAYMUND C. ALMEDA

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=24132'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)


# BALUYUT ADONES

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=26904'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)



# BRAGANZA JOHN

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=26924'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)

# CAPARROS MARVIN

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=594'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)


# CASARES ED 

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=12640'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)

# CHAM JIMMY

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=26941'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)


# CHUA RENE

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=26990'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)

# CHUA REY

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=24504'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)


# CO ALBERT

list_of_cells = []
list_of_cells.append("ALBERT CO")

# ALEX DI

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=27059'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)


# DY WILLIAM

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=27078'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)

# FERNANDEZ VIC

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=27098'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)

# GO RAMON

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=14651'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)


# HAO NEV

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=38050'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)


# HING DOM

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=40315'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)

# JAVIER MIKE

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=42212'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)


# LEE GREGG

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=27264'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)


# LEE WALLIE

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=27267'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)


# LI SUN YEE

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=21974'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)



# LIM ROGER

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=27303'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)


# MOON ALEX KIHO

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=25478'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)



# NG CIP

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=27366'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)



# ONG MANUEL JR

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=36144'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)



# ONG NEIL

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=36379'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)

# SANDOVAL RICKY

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=27487'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)


# SANTOS DANILO

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=27492'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)


# SO JACK

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=22224'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)


# TAN EDDIE

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=21396'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)


# TAN JEREMY

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=27586'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)



# TAN TOMMY

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=27612'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)


# WEE PATRICK

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=22343'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)



# YUN DAVID JEOUNG

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=38205'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)




# Write to CSV
outfile = open("./club30-HCP.csv","wb")
writer = csv.writer(outfile)
writer.writerow(["PLAYER NAME", "HCP INDEX"])
writer.writerows(list_of_rows)

