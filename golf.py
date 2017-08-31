import csv
import requests
from BeautifulSoup import BeautifulSoup

eastSlopeBlue = int(142)
westSlopeBlue = int(131)
eastSlopeWhite = int(139)
westSlopeWhite = int(125)
midlandsSlopeBlue = int(127)
midlandsSlopeWhite = int(123)

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

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))


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

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)

# CAPARROS MARVIN

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=412'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeWhite/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeWhite/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeWhite/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('WHITE')

east = float(handicap)*eastSlopeWhite/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeWhite/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeWhite/113
list_of_cells.append(round(midlands))

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)


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

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)

# FERNANDEZ VIC

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=21822'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

list_of_cells.append('WHITE')

east = float(handicap)*eastSlopeWhite/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeWhite/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeWhite/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)


# JIN HUN ROH

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=25789'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('WHITE')

east = float(handicap)*eastSlopeWhite/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeWhite/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeWhite/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

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
list_of_cells.append('Alex Moon')

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('WHITE')

east = float(handicap)*eastSlopeWhite/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeWhite/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

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
list_of_cells.append('Jun Ong')

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

list_of_cells.append('BLUE')


east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('WHITE')

east = float(handicap)*eastSlopeWhite/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeWhite/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeWhite/113
list_of_cells.append(round(midlands))

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)

# SO JACK

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

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeWhite/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeWhite/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeWhite/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('WHITE')

east = float(handicap)*eastSlopeWhite/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeWhite/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)

# TAN SQUARE

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=22246'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = 'SQUARE TAN'
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('WHITE')

east = float(handicap)*eastSlopeWhite/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeWhite/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeWhite/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

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

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)

# NONOY TAN

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=27574'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeWhite/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeWhite/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeWhite/113
list_of_cells.append(round(midlands))

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)

# BENJIE GUEVARA

# Initialize new row
list_of_cells = []

url = 'http://www.unhs.ph/MemberPage.aspx?id=27173'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Cell: Name
name = soup.find('span', attrs={'class': 'nameHeader'}).text.strip()
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)

# ALBERT CO

# Initialize new row
list_of_cells = []

# url = 'http://www.unhs.ph/MemberPage.aspx?id='
# response = requests.get(url)
# html = response.content

# soup = BeautifulSoup(html)

# Cell: Name
name = 'ALBERT CO -- not updated'
list_of_cells.append(name)

# Cell: Index
handicap = '36.4'
list_of_cells.append(handicap)

list_of_cells.append('WHITE')

east = float(handicap)*eastSlopeWhite/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeWhite/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeWhite/113
list_of_cells.append(round(midlands))

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)

# KEVIN KIM

# Initialize new row
list_of_cells = []


# Cell: Name
name = 'KEVIN KIM -- not updated'
list_of_cells.append(name)

# Cell: Index
handicap = '15.1'
list_of_cells.append(handicap)

list_of_cells.append('BLUE')

east = float(handicap)*eastSlopeBlue/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeBlue/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeBlue/113
list_of_cells.append(round(midlands))

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)

# GREG UY

# Initialize new row
list_of_cells = []


# Cell: Name
name = 'GREG UY -- no handicap'
list_of_cells.append(name)

# Cell: Index
handicap = '0'
list_of_cells.append(handicap)

list_of_cells.append('WHITE')

east = float(handicap)*eastSlopeWhite/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeWhite/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeWhite/113
list_of_cells.append(round(midlands))

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)



# FERDINAND AGUILA
# Initialize new row
list_of_cells = []

# url = 'http://www.unhs.ph/MemberPage.aspx?id=26852'
# response = requests.get(url)
# html = response.content

# soup = BeautifulSoup(html)

# Cell: Name
name = 'FERDIDAND AGUILA'
list_of_cells.append(name)

# Cell: Index
handicap = soup.find('span', attrs={'class': 'headr2'}).text.strip()
list_of_cells.append(handicap)

list_of_cells.append('WHITE')

east = float(handicap)*eastSlopeWhite/113
list_of_cells.append(round(east))

west = float(handicap)*westSlopeWhite/113
list_of_cells.append(round(west))

midlands = float(handicap)*midlandsSlopeWhite/113
list_of_cells.append(round(midlands))

# Row = Cell: Name, Index
list_of_rows.append(list_of_cells)


# Write to CSV
outfile = open("./club30-sept2017.csv","wb")
writer = csv.writer(outfile)
writer.writerow(["PLAYER NAME", "HCP INDEX", "MOUNT", "EAST", "WEST", "MIDLANDS"])
writer.writerows(list_of_rows)

