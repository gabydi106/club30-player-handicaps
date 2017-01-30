# Feb 2017 Player Handicaps

| PLAYER NAME                  | HCP INDEX | MOUNT | EAST | WEST | MIDLANDS |
|------------------------------|-----------|-------|------|------|----------|
| ADONES T. BALUYUT            | 9.2       | BLUE  | 12   | 11   | 10       |
| ALBERT CO -- not updated     | 36.4      | WHITE | 45   | 40   | 40       |
| Alex Moon                    | 8         | BLUE  | 10   | 9    | 9        |
| ALEXANDER G. DI              | 28.7      | BLUE  | 36   | 33   | 32       |
| BAYANI    TAN                | 15.2      | BLUE  | 19   | 17   | 17       |
| BENJAMIN S. GUEVARA          | 14.1      | BLUE  | 18   | 16   | 16       |
| BREZNEV    HAO               | 12.7      | BLUE  | 16   | 15   | 14       |
| CIPRIANO L. NG               | 26.8      | WHITE | 33   | 30   | 30       |
| DANILO RIVERA SANTOS         | 30.8      | WHITE | 38   | 34   | 34       |
| DOMINIC    HING              | 10.6      | BLUE  | 13   | 12   | 12       |
| EDDIE K. TAN                 | 31.2      | WHITE | 38   | 35   | 35       |
| EDUARDO    CASARES           | 18.9      | BLUE  | 24   | 22   | 21       |
| FEDERICO    SANDOVAL II      | 24.9      | BLUE  | 31   | 29   | 28       |
| GOLDWIN SISON -- no handicap | 0         | BLUE  | 0    | 0    | 0        |
| GREG UY -- no handicap       | 0         | WHITE | 0    | 0    | 0        |
| GREGORIO L. LEE              | 13.9      | BLUE  | 17   | 16   | 16       |
| JACKNEIL Hao SO              | 15.2      | BLUE  | 19   | 18   | 17       |
| JEOUNG    WON-YUN            | 11.7      | BLUE  | 15   | 14   | 13       |
| JEREMY    TAN                | 20.2      | BLUE  | 25   | 23   | 23       |
| JIMMY L. CHAM                | 20.8      | BLUE  | 26   | 23   | 23       |
| JOHN    BRAGANZA             | 19.3      | BLUE  | 24   | 22   | 22       |
| Jun Ong                      | 21.4      | BLUE  | 27   | 25   | 24       |
| KEVIN KIM -- not updated     | 15.1      | BLUE  | 19   | 18   | 17       |
| Marvin    CAPARROS           | 6.1       | BLUE  | 8    | 7    | 7        |
| Michael Joseph L. Javier     | 18.8      | BLUE  | 24   | 22   | 21       |
| Neil    ONG                  | 13.6      | BLUE  | 17   | 16   | 15       |
| PATRICK    WEE               | 18.5      | BLUE  | 23   | 21   | 21       |
| RAMON    GO                  | 24        | BLUE  | 30   | 28   | 27       |
| Raymund C. ALMEDA            | 18.4      | BLUE  | 23   | 21   | 21       |
| RENE S. CHUA                 | 11        | BLUE  | 14   | 13   | 12       |
| Reynaldo S. CHUA             | 20.1      | WHITE | 25   | 22   | 22       |
| ROGER L. LIM                 | 14.1      | BLUE  | 18   | 16   | 16       |
| SQUARE TAN                   | 18.5      | BLUE  | 23   | 21   | 21       |
| SUN YEE    LI                | 29.8      | WHITE | 37   | 33   | 32       |
| TOMMY K. TAN                 | 14.8      | WHITE | 18   | 16   | 16       |
| VIC    FERNANDEZ             | 28        | WHITE | 34   | 31   | 30       |
| WALLIE M. LEE                | 17.2      | BLUE  | 22   | 20   | 19       |
| WILLIAM V. DY                | 15.6      | BLUE  | 20   | 18   | 18       |


# Player Handicap Extractor 
A python script using BeautifulSoup to extract the player handicaps from [UNHS](http://unhs.ph) website and save it as a comma-delimited text.

### How to run this file

 Run `python golf.py`
 
### Output
 
 A CSV file with headers: **NAME** and **HCP INDEX**
 
### Prerequisites

Your computer needs the following tools installed and working to run the file.

- A command-line interface to interact with your computer
- A text editor to work with plain text files
- Version 2.7 of the Python programming language

### Future improvements

Extract more information:

- Tee mount (completed Nov 2016)
- Course specific handicaps (completed Oct 2016)

Automatic Updates

- integrate with cron job to autonomously update monthly handicaps

 
### Disclaimers
 
 I based this project on the tutorial found here: [First web scraper](https://first-web-scraper.readthedocs.io/en/latest/)
 
 This is my first working/usable Python script
