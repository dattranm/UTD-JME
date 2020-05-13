# importing libraries
import glob
import numpy as np
import pandas as pd
import pickle
import re
import random

### Collect all results
results = []

# Open all text files for the source
jme_top_files = glob.glob("top5storiesPart*.txt")
current_position = 0
for file in jme_top_files:
    paragraphs = []
    f = open(file)
    lines = f.read().splitlines()
    paragraph = ''
    line_key = ''
    line_date = ''
    line_source = ''
    line_preformat = ''
    for i, line in enumerate(lines):
        for part1 in line.split():
            if "Key:" in part1:
                line_key = line
                line_preformat = lines[i + 1]
                if ", 1970" in line_preformat:
                    line_date = "1970"
                elif ", 1971" in line_preformat:
                    line_date = "1971"
                elif ", 1972" in line_preformat:
                    line_date = "1972"
                elif ", 1973" in line_preformat:
                    line_date = "1973"
                elif ", 1974" in line_preformat:
                    line_date = "1974"
                elif ", 1975" in line_preformat:
                    line_date = "1975"
                elif ", 1976" in line_preformat:
                    line_date = "1976"
                elif ", 1977" in line_preformat:
                    line_date = "1977"
                elif ", 1978" in line_preformat:
                    line_date = "1978"
                elif ", 1979" in line_preformat:
                    line_date = "1979"
                elif ", 1980" in line_preformat:
                    line_date = "1980"
                elif ", 1981" in line_preformat:
                    line_date = "1981"
                elif ", 1982" in line_preformat:
                    line_date = "1982"
                elif ", 1983" in line_preformat:
                    line_date = "1983"
                elif ", 1984" in line_preformat:
                    line_date = "1984"
                elif ", 1985" in line_preformat:
                    line_date = "1985"
                elif ", 1986" in line_preformat:
                    line_date = "1986"
                elif ", 1987" in line_preformat:
                    line_date = "1987"
                elif ", 1988" in line_preformat:
                    line_date = "1988"
                elif ", 1989" in line_preformat:
                    line_date = "1989"
                elif ", 1990" in line_preformat:
                    line_date = "1990"
                elif ", 1991" in line_preformat:
                    line_date = "1991"
                elif ", 1992" in line_preformat:
                    line_date = "1992"
                elif ", 1993" in line_preformat:
                    line_date = "1993"
                elif ", 1994" in line_preformat:
                    line_date = "1994"
                elif ", 1995" in line_preformat:
                    line_date = "1995"
                elif ", 1996" in line_preformat:
                    line_date = "1996"
                elif ", 1997" in line_preformat:
                    line_date = "1997"
                elif ", 1998" in line_preformat:
                    line_date = "1998"
                elif ", 1999" in line_preformat:
                    line_date = "1999"
                elif ", 2000" in line_preformat:
                    line_date = "2000"
                elif ", 2001" in line_preformat:
                    line_date = "2001"
                elif ", 2002" in line_preformat:
                    line_date = "2002"
                elif ", 2003" in line_preformat:
                    line_date = "2003"
                elif ", 2004" in line_preformat:
                    line_date = "2004"
                elif ", 2005" in line_preformat:
                    line_date = "2005"
                elif ", 2006" in line_preformat:
                    line_date = "2006"
                elif ", 2007" in line_preformat:
                    line_date = "2007"
                elif ", 2008" in line_preformat:
                    line_date = "2008"
                elif ", 2009" in line_preformat:
                    line_date = "2009"
                elif ", 2010" in line_preformat:
                    line_date = "2010"
                elif ", 2011" in line_preformat:
                    line_date = "2011"
                elif ", 2012" in line_preformat:
                    line_date = "2012"

                if "January" in line_preformat or "JANUARY" in line_preformat or "Jan" in line_preformat:
                    line_date += "01"
                elif "February" in line_preformat or "FEBRUARY" in line_preformat or "Feb" in line_preformat:
                    line_date += "02"
                elif "March" in line_preformat or "MARCH" in line_preformat or "Mar" in line_preformat:
                    line_date += "03"
                elif "April" in line_preformat or "APRIL" in line_preformat or "Apr" in line_preformat:
                    line_date += "04"
                elif "May" in line_preformat or "MAY" in line_preformat or "May" in line_preformat:
                    line_date += "05"
                elif "June" in line_preformat or "JUNE" in line_preformat or "Jun" in line_preformat:
                    line_date += "06"
                elif "July" in line_preformat or "JULY" in line_preformat or "July" in line_preformat:
                    line_date += "07"
                elif "August" in line_preformat or "AUGUST" in line_preformat or "Aug" in line_preformat:
                    line_date += "08"
                elif "September" in line_preformat or "SEPTEMBER" in line_preformat or "Sep" in line_preformat:
                    line_date += "09"
                elif "October" in line_preformat or "OCTOBER" in line_preformat or "Oct" in line_preformat:
                    line_date += "10"
                elif "November" in line_preformat or "NOVEMBER" in line_preformat or "Nov" in line_preformat:
                    line_date += "11"
                elif "December" in line_preformat or "DECEMBER" in line_preformat or "Dec" in line_preformat:
                    line_date += "12"

                if " 01," in line_preformat or " 1," in line_preformat:
                    line_date = line_date + "01"
                elif " 02," in line_preformat or " 2," in line_preformat:
                    line_date = line_date + "02"
                elif " 03," in line_preformat or " 3," in line_preformat:
                    line_date = line_date + "03"
                elif " 04," in line_preformat or " 4," in line_preformat:
                    line_date = line_date + "04"
                elif " 05," in line_preformat or " 5," in line_preformat:
                    line_date = line_date + "05"
                elif " 06," in line_preformat or " 6," in line_preformat:
                    line_date = line_date + "06"
                elif " 07," in line_preformat or " 7," in line_preformat:
                    line_date = line_date + "07"
                elif " 08," in line_preformat or " 8," in line_preformat:
                    line_date = line_date + "08"
                elif " 09," in line_preformat or " 9," in line_preformat:
                    line_date = line_date + "09"
                elif " 10," in line_preformat:
                    line_date = line_date + "10"
                elif " 11," in line_preformat:
                    line_date = line_date + "11"
                elif " 12," in line_preformat:
                    line_date = line_date + "12"
                elif " 13," in line_preformat:
                    line_date = line_date + "13"
                elif " 14," in line_preformat:
                    line_date = line_date + "14"
                elif " 15," in line_preformat:
                    line_date = line_date + "15"
                elif " 16," in line_preformat:
                    line_date = line_date + "16"
                elif " 17," in line_preformat:
                    line_date = line_date + "17"
                elif " 18," in line_preformat:
                    line_date = line_date + "18"
                elif " 19," in line_preformat:
                    line_date = line_date + "19"
                elif " 20," in line_preformat:
                    line_date = line_date + "20"
                elif " 21," in line_preformat:
                    line_date = line_date + "21"
                elif " 22," in line_preformat:
                    line_date = line_date + "22"
                elif " 23," in line_preformat:
                    line_date = line_date + "23"
                elif " 24," in line_preformat:
                    line_date = line_date + "24"
                elif " 25," in line_preformat:
                    line_date = line_date + "25"
                elif " 26," in line_preformat:
                    line_date = line_date + "26"
                elif " 27," in line_preformat:
                    line_date = line_date + "27"
                elif " 28," in line_preformat:
                    line_date = line_date + "28"
                elif " 29," in line_preformat:
                    line_date = line_date + "29"
                elif " 30," in line_preformat:
                    line_date = line_date + "30"
                elif " 31," in line_preformat:
                    line_date = line_date + "31"

            elif "(c)" in part1:
                line_source = line

            if "------------------------------" in line:
                results.append({'key': line_key, 'date': line_date, 'source': line_source, 'paragraph': paragraph})
                paragraph = ''
            elif 'Key:' not in line and line != line_preformat and "(c)" not in line and "Section Not Found" not in line and "DATELINE:" not in line and "Dateline Not" not in line and "SECTION: " not in line and "Byline" not in line and "BYLINE" not in line and "LENGTH:" not in line and "Probable dyad:" not in line and ">>>>>>>>>>>>>>>>>>" not in line and "<<<<<<<<<<<<<<<<<<" not in line and "------------------------------" not in line:
                paragraph += ' %s' % line
                break

data = pd.DataFrame(results)

data.iloc[:, 0] = data.iloc[:, 0].str.replace("Key: ", "")
data.iloc[:, 2] = data.iloc[:, 2].str.replace('\(c*\)', '')

data.to_csv('top_stories_JME_data_FINAL.csv', index=False)
