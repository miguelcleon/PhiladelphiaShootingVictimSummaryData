import csv
directory = './'


def summarizephillyshootingdata(inputfile, outputfile, includenonefatal=True):
    with open( directory  + inputfile, 'r', errors='ignore') as datafile:
        reader = csv.reader(datafile)
        with open( './' + outputfile, 'w', newline='') as outfile:
            csvout = csv.writer(outfile)
            i = 0
            headerrow = ['year','total', 'black','white','asian', 'u or blank', 'male',
                         'under 35', 'latinx', 'officer_involved','fatal','non-fatal', 'black male',
                         'black male under 35']
            csvout.writerow(headerrow)
            curyear = None
            lastyear = None
            total = 0
            black = 0
            white = 0
            asian = 0
            blank = 0
            male = 0
            age = 0
            latinx = 0
            officer_involved = 0
            fatal = 0
            nonfatal=0
            youngblack = 0
            youngblackm = 0
            yearrow = []
            for sdrow in reader:
                i +=1
                if i > 1:
                    lastyear = curyear
                    curyear = sdrow[3]
                    if lastyear:
                        if curyear == lastyear:
                            if sdrow[22] == '1' or includenonefatal:
                                total +=1
                                if sdrow[8] == 'B':
                                    black +=1
                                elif sdrow[8] == 'W':
                                    white +=1
                                elif sdrow[8] == 'A':
                                    asian +=1
                                else:
                                    blank +=1
                                if sdrow[9] == 'M':
                                    male +=1
                                if len(sdrow[10]) >0:
                                    if int(sdrow[10]) < 35:
                                        age +=1
                                        if sdrow[8] == 'B':
                                            youngblack +=1
                                        if  sdrow[8] == 'B' and  sdrow[9] == 'M':
                                            youngblackm +=1
                                if sdrow[16] =='1':
                                    latinx +=1
                                if sdrow[12] == 'Y':
                                    officer_involved+=1
                                if sdrow[22] == '1':
                                    fatal +=1
                                elif sdrow[22] == '0':
                                    nonfatal +=1
                        else:
                            yearrow.append(lastyear)
                            yearrow.append(total)
                            yearrow.append(black)
                            yearrow.append(white)
                            yearrow.append(asian)
                            yearrow.append(blank)
                            yearrow.append(male)
                            yearrow.append(age)
                            yearrow.append(latinx)
                            yearrow.append(officer_involved)
                            yearrow.append(fatal)
                            yearrow.append(nonfatal)
                            yearrow.append(youngblack)
                            yearrow.append(youngblackm)
                            csvout.writerow(yearrow)
                            yearrow = []
                            total = 0
                            black = 0
                            white = 0
                            asian = 0
                            blank = 0
                            male = 0
                            age = 0
                            latinx = 0
                            officer_involved = 0
                            fatal = 0
                            nonfatal = 0
                            youngblack = 0
                            youngblackm = 0
                    elif sdrow[22] == '1' or includenonefatal: # first row of data
                        total +=1
                        if sdrow[8] == 'B':
                            black +=1
                        elif sdrow[8] == 'W':
                            white +=1
                        elif sdrow[8] == 'A':
                            asian +=1
                        else:
                            blank +=1
                        if sdrow[9] == 'M':
                            male +=1
                        if len(sdrow[10]) >0:
                            if int(sdrow[10]) < 35:
                                age +=1
                                if sdrow[8] == 'B':
                                    youngblack +=1
                                if  sdrow[8] == 'B' and  sdrow[9] == 'M':
                                    youngblackm +=1
                        if sdrow[16] =='1':
                            latinx +=1
                        if sdrow[12] == 'Y':
                            officer_involved+=1
                        if sdrow[22] == '1':
                            fatal +=1
                        elif sdrow[22] == '0':
                            nonfatal +=1
if __name__ == '__main__':
    summarizephillyshootingdata('phillyshooting.csv', 'phillyfatalshootingsummary.csv', False)
    summarizephillyshootingdata('phillyshooting.csv', 'phillyshootingsummary.csv', True)