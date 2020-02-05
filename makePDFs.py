import random

from PIL import Image
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from datetime import date



def printPDFs(df=None, data=None, dict = None, teamname = "sample"):


    line = Image.open('images/line.png')
    fly = Image.open('images/fly.png')
    ground = Image.open('images/dashed.png')
    #TODO: make system agnostic, also change interdata path
    fileNameLoc = './pdfs/' + str(teamname) + ':' + str(date.today()) + '.pdf'
    c = canvas.Canvas(fileNameLoc, pagesize=landscape(letter))

    namesInOrder = df.ix[:, 1]
    play = df.ix[:, 2]
    ballLoc = df.ix[:, 0]

    names = []
    for name in namesInOrder:
        if name not in names:
            names.append(name)

    # print(names)

    for name in names:
        # print(name)
        field = ImageReader('images/GTSprayCharts.jpg')
        c.drawImage(field, 0, 0, 11 * inch, 8.5 * inch, mask='auto')
        c.setFillColorRGB(1, 0, 0)

        for i in range(len(namesInOrder)):
            if name == namesInOrder.ix[i]:
                thisPlay = play.ix[i]
                thisBallLoc = ballLoc.ix[i]
                # print(thisPlay + " " + thisBallLoc)

                #determines the symbol of the result
                result = None
                if thisPlay == 'grounded' or thisPlay == 'flied' or thisPlay == 'popped' or thisPlay == 'lined' or thisPlay == 'double':
                    result = ''
                elif thisPlay == 'bunt':
                    result = 'b'
                elif thisPlay == 'singled':
                    result = '__'
                elif thisPlay == 'doubled':
                    result = '+'
                elif thisPlay == 'tripled':
                    result = 'X'
                elif thisPlay == 'homered':
                    result = '#'
                linePlay = None
                if thisPlay == 'grounded' or thisPlay == 'double' or thisPlay == 'bunt':
                    linePlay = 0
                elif thisPlay == 'flied' or thisPlay == 'popped':
                    linePlay = 2
                elif thisPlay == 'lined':
                    linePlay = 1
                elif thisPlay == 'singled':
                    if thisBallLoc == 'p' or thisBallLoc == 'pitcher' or thisBallLoc == '1b' or thisBallLoc == 'first' or thisBallLoc == '2b' or thisBallLoc == 'second' or thisBallLoc == 'ss' or thisBallLoc == 'shortstop' or thisBallLoc == 'short' or thisBallLoc == '3b' or thisBallLoc == 'third':
                        linePlay = 0
                    else:
                        linePlay = 1
                elif thisPlay == 'doubled':
                    if thisBallLoc == 'down lf' or thisBallLoc == 'down left' or thisBallLoc == 'down right' or thisBallLoc == 'down rf':
                        linePlay = 1
                    else:
                        linePlay = 2
                elif thisPlay == 'triple' or thisPlay == 'homered':
                    linePlay = 2
                if thisPlay == 'bunt':
                    randx = random.random()
                    randy = random.random()
                    if thisBallLoc == 'p' or thisBallLoc == 'pitcher':
                        if linePlay == 2:
                            c.drawImage(ImageReader(fly.rotate(135, expand=True)),(6.9+randx * .2)*inch,(1.64+randy * .2)*inch,mask = 'auto')

                        elif linePlay == 0:
                            c.drawImage(ImageReader(ground.rotate(135, expand=True)),(7+ randx * .2)*inch,(1.64+randy * .2)*inch,mask = 'auto')

                        elif linePlay == 1:
                            c.drawImage(ImageReader(line.rotate(135, expand=True)),(6.9 + randx * .2)*inch,(1.64+randy * .2)*inch,mask = 'auto')

                        c.drawString((7.1 + randx * .2)*inch,(2.6+randy * .2)*inch, result)
                    elif thisBallLoc == '1b' or thisBallLoc == 'first':
                        if linePlay == 2:
                            c.drawImage(ImageReader(fly.rotate(135, expand=True)),(7.35+randx * .2)*inch,(1.64+randy * .5)*inch,mask = 'auto')

                        elif linePlay == 0:
                            c.drawImage(ImageReader(ground.rotate(135, expand=True)),(7.45+ randx * .2)*inch,(1.64+randy * .5)*inch,mask = 'auto')

                        elif linePlay == 1:
                            c.drawImage(ImageReader(line.rotate(135, expand=True)),(7.35 + randx * .2)*inch,(1.64+randy * .5)*inch,mask = 'auto')

                        c.drawString((7.55 + randx * .2)*inch,(2.6+randy * .5)*inch, result)
                    elif thisBallLoc == '3b' or thisBallLoc == 'third':
                        if linePlay == 2:
                            c.drawImage(ImageReader(fly.rotate(135, expand=True)),(6.3+randx * .5)*inch,(1.09+randy * .2)*inch,mask = 'auto')

                        elif linePlay == 0:
                            c.drawImage(ImageReader(ground.rotate(135, expand=True)),(6.4+ randx * .5)*inch,(1.09+randy * .2)*inch,mask = 'auto')

                        elif linePlay == 1:
                            c.drawImage(ImageReader(line.rotate(135, expand=True)),(6.3 + randx * .5)*inch,(1.09+randy * .2)*inch,mask = 'auto')

                        c.drawString((6.5 + randx * .5)*inch,(2.05+randy * .2)*inch, result)
                elif thisBallLoc == 'p' or thisBallLoc == 'pitcher':  # P
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(135, expand=True)),(6.3+randx * .6)*inch,(1.79+randy * .6)*inch,mask = 'auto')

                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(135, expand=True)),(6.4+ randx * .6)*inch,(1.79+randy * .6)*inch,mask = 'auto')

                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(135, expand=True)),(6.3 + randx * .6)*inch,(1.79+randy * .6)*inch,mask = 'auto')

                    c.drawString((6.5 + randx * .6)*inch,(2.85+randy * .6)*inch, result)
                elif thisBallLoc == '1b' or thisBallLoc == 'first':  # 1B
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(95, expand=True)),(6.85+randx * .7)*inch,(2.8+randy * .75)*inch,mask = 'auto')

                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(95, expand=True)),(6.95+randx * .7)*inch,(2.8+randy * .75)*inch,mask = 'auto')

                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(95, expand=True)),(6.9+randx * .7)*inch,(2.8+randy * .75)*inch,mask = 'auto')

                    c.drawString((7+randx * .7)*inch,(4.2+randy * .75)*inch, result)
                elif thisBallLoc == 'through right':  # through right
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(95, expand=True)),(6.35+randx)*inch,(3.7+randy * .5)*inch,mask = 'auto')

                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(95, expand=True)),(6.45+randx)*inch,(3.7+randy * .5)*inch,mask = 'auto')

                    else:
                        c.drawImage(ImageReader(line.rotate(95, expand=True)),(6.4+randx)*inch,(3.7+randy * .5)*inch,mask = 'auto')

                    c.drawString((6.5+randx)*inch,(5.1+randy * .5)*inch, result)
                elif thisBallLoc == '2b' or thisBallLoc == 'second':  # 2B
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(115, expand=True)),(5.55+randx * .7)*inch,(3.1+randy * .85)*inch,mask = 'auto')

                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(115, expand=True)),(5.65+randx * .7)*inch,(3+randy * .85)*inch,mask = 'auto')

                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(115, expand=True)),(5.55+randx * .7)*inch,(3.1+randy * .85)*inch,mask = 'auto')

                    c.drawString((5.75+randx * .7)*inch,(4.4+randy * .85)*inch, result)
                elif thisBallLoc == '3b' or thisBallLoc == 'third':  # 3B
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(175, expand=True)),(5.1+randx*.7)*inch,(2.15+randy*.7)*inch,mask = 'auto')

                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(175, expand=True)),(5.2+randx*.7)*inch,(2.2+randy*.7)*inch,mask = 'auto')
                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(175, expand=True)),(5.1+randx*.7)*inch,(2.17+randy*.7)*inch,mask = 'auto')

                    c.drawString((5.25+randx * .7)*inch,(2.4+randy *.7)*inch, result)
                elif thisBallLoc == 'through left':  # through left
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(175, expand=True)),(4.05+randx*.5)*inch,(2.5+randy*.8)*inch,mask = 'auto')

                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(175, expand=True)),(4.15+randx*.5)*inch,(2.55+randy*.8)*inch,mask = 'auto')
                    else:
                        c.drawImage(ImageReader(line.rotate(175, expand=True)),(4.05+randx*.5)*inch,(2.52+randy*.8)*inch,mask = 'auto')

                    c.drawString((4.1+randx * .5)*inch,(2.75+randy *.8)*inch, result)
                elif thisBallLoc == 'shortstop' or thisBallLoc == 'ss' or thisBallLoc == 'short':  # SS
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(150, expand=True)),(4.4+randx*.75)*inch,(2.45+randy*1.1)*inch,mask = 'auto')

                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(150, expand=True)),(4.5+randx*.75)*inch,(2.45+randy*1.1)*inch,mask = 'auto')

                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(150, expand=True)),(4.4+randx*.75)*inch,(2.45+randy*1.1)*inch,mask = 'auto')

                    c.drawString((4.6+randx*.75)*inch,(3.25+randy*1.1)*inch, result)
                elif (thisBallLoc == 'lf' or thisBallLoc == 'left') and thisPlay != 'homered':  # LF
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(165, expand=True)),(2.55+randx*1.3)*inch,(2.4+randy*1.3)*inch,mask = 'auto')

                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(165, expand=True)),(2.65+randx*1.3)*inch,(2.4+randy*1.3)*inch,mask = 'auto')

                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(165, expand=True)),(2.55+randx*1.3)*inch,(2.4+randy*1.3)*inch,mask = 'auto')

                    c.drawString((2.75+randx*1.3)*inch,(2.9+randy*1.3)*inch, result)
                elif (thisBallLoc == 'cf' or thisBallLoc == 'center') and thisPlay != 'homered':  # CF
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(135, expand=True)),(3.8+randx)*inch,(3.94+randy)*inch,mask = 'auto')

                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(135, expand=True)),(3.9+randx)*inch,(3.94+randy)*inch,mask = 'auto')

                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(135, expand=True)),(3.8+randx)*inch,(3.94+randy)*inch,mask = 'auto')

                    c.drawString((4+randx)*inch,(5.1+randy)*inch, result)
                elif (thisBallLoc == 'rf' or thisBallLoc == 'right') and thisPlay != 'homered':  # RF
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(105, expand=True)),(5.7+randx*1.1)*inch,(4.75+randy*1.15)*inch,mask = 'auto')


                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(105, expand=True)),(5.8+randx*1.1)*inch,(4.65+randy*1.15)*inch,mask = 'auto')

                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(105, expand=True)),(5.7+randx*1.1)*inch,(4.75+randy*1.15)*inch,mask = 'auto')
                    c.drawString((5.9+randx*1.1)*inch,(6.05+randy*1.15)*inch, result)
                elif thisBallLoc == 'left center' and thisPlay != 'homered':# LeftCenter
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(150, expand=True)),(2.8 + .75 *randx)*inch,(4 + .75 *randy)*inch,mask = 'auto')

                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(150, expand=True)),(2.9 + .75 *randx)*inch,(4 + .75 *randy)*inch,mask = 'auto')
                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(150, expand=True)),(2.8 + .75 *randx)*inch,(4 + .75 *randy)*inch,mask = 'auto')

                    c.drawString((3 + .75 *randx)*inch,(4.8 + .75 *randy)*inch, result)
                elif thisBallLoc == 'right center' and thisPlay != 'homered':# RightCenter
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(115, expand=True)),(4.6 + .75*randx)*inch,(4.9 +.75*randy)*inch,mask = 'auto')

                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(115, expand=True)),(4.7 + .75*randx)*inch,(4.8 +.75*randy)*inch,mask = 'auto')
                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(115, expand=True)),(4.6 + .75*randx)*inch,(4.9 +.75*randy)*inch,mask = 'auto')

                    c.drawString((4.8 + .75*randx)*inch,(6.2 +.75*randy)*inch, result)
                elif thisBallLoc == 'down lf' or thisBallLoc == 'down left':  # LeftLine
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(175, expand=True)),(2.35+randx*1.4)*inch,(1.85+randy*.5)*inch,mask = 'auto')

                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(175, expand=True)),(2.45+randx*1.4)*inch,(1.9+randy*.5)*inch,mask = 'auto')

                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(175, expand=True)),(2.35+randx*1.4)*inch,(1.87+randy*.5)*inch,mask = 'auto')

                    c.drawString((2.5+randx*1.4)*inch,(2.1+randy/2)*inch, result)
                elif thisBallLoc == 'down rf' or thisBallLoc == 'down right':  # RightLine
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(95, expand=True)),(7.15+randx/2)*inch,(4.65+randy*1.25)*inch,mask = 'auto')

                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(95, expand=True)),(7.25+randx/2)*inch,(4.65+randy*1.25)*inch,mask = 'auto')
                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(95, expand=True)),(7.2+randx/2)*inch,(4.65+randy*1.25)*inch,mask = 'auto')

                    c.drawString((7.3+randx/2)*inch,(6.05+randy*1.25)*inch, result)
                elif thisBallLoc == 'middle':  # UpMid
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(135, expand=True)),(4.95+randx*.6)*inch,(3.3+randy*.6)*inch,mask = 'auto')

                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(135, expand=True)),(5.05+randx*.6)*inch,(3.3+randy*.6)*inch,mask = 'auto')

                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(135, expand=True)),(4.95+randx*.6)*inch,(3.3+randy*.6)*inch,mask = 'auto')

                    c.drawString((5.1+randx*.6)*inch,(4.4+randy*.6)*inch, result)
                elif thisBallLoc == 'lf' or thisBallLoc == 'left':  # HRLF
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(165, expand=True)),(1.4+randx*.4)*inch,(2.2+randy)*inch,mask = 'auto')

                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(165, expand=True)),(1.5+randx*.4)*inch,(2.2+randy)*inch,mask = 'auto')

                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(165, expand=True)),(1.4+randx*.4)*inch,(2.2+randy)*inch,mask = 'auto')

                    c.drawString((1.5+randx*.4)*inch,(2.7+randy)*inch, result)
                elif thisBallLoc == 'left center': # HRLCF
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(150, expand=True)),(1.75 + .4 *randx)*inch,(4 + .5 * randy)*inch,mask = 'auto')
                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(150, expand=True)),(1.85 + .4 *randx)*inch,(4 + .5 * randy)*inch,mask = 'auto')

                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(150, expand=True)),(1.75 + .4 *randx)*inch,(4 + .5 * randy)*inch,mask = 'auto')

                    c.drawString((1.95 + .4 *randx)*inch,(4.8 + .5 * randy)*inch, result)
                elif thisBallLoc == 'cf' or thisBallLoc == 'center':  # HRCF
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(135, expand=True)),(2.9+randx*.5)*inch,(5.44+randy*.5)*inch,mask = 'auto')

                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(135, expand=True)),(3+randx*.5)*inch,(5.44+randy*.5)*inch,mask = 'auto')

                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(135, expand=True)),(2.9+randx*.5)*inch,(5.44+randy*.5)*inch,mask = 'auto')

                    c.drawString((3.1+randx*.5)*inch,(6.5+randy*.5)*inch, result)
                elif thisBallLoc == 'right center': # HRRCF
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(115, expand=True)),(4.3 + randx*.3)*inch,(6 + randy*.4)*inch,mask = 'auto')

                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(115, expand=True)),(4.4 + randx*.3)*inch,(5.9 + randy*.4)*inch,mask = 'auto')

                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(115, expand=True)),(4.3 + randx*.3)*inch,(6 + randy*.4)*inch,mask = 'auto')

                    c.drawString((4.5 + randx*.3)*inch,(7.3 + randy*.4)*inch, result)
                elif thisBallLoc == 'rf' or thisBallLoc == 'right':  # HRRF
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(105, expand=True)),(6.2+randx)*inch,(6.6+randy*.25)*inch,mask = 'auto')

                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(105, expand=True)),(6.3+randx)*inch,(6.5+randy*.25)*inch,mask = 'auto')

                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(105, expand=True)),(6.2+randx)*inch,(6.6+randy*.25)*inch,mask = 'auto')

                    c.drawString((6.4+randx)*inch,(7.9+randy*.25)*inch, result)
        for k in range(len(data)):
            if name.upper() in data.ix[k, 0].upper():

                c.drawString(1.5 * inch, 7.85 * inch, data.ix[k, 0].upper())
                # statNames = ['BA (2)', 'OBPct(3)', 'SLGPct(4)', 'AB(5)', 'R(6)', 'H(7)', '2B(8)', '3B(9)',
                #'HR(11)', 'BB(13)', 'HBP(14)', 'RBI(15)','SF(16)', 'SH(17)', 'K(18)', 'SB(23)', 'CS(24)', WOBA, SA]
                c.drawString(.78 * inch, 6.73 * inch, str(data.ix[k, 1][17]))#WOBA


                c.drawString(.84 * inch, 6.41 * inch, str(data.ix[k, 1][15]))#SB
                c.drawString(1.17 * inch, 6.41 * inch, str(data.ix[k, 1][16]))#CS

                c.drawString(.69 * inch, 6.11 * inch, str(data.ix[k, 1][0]))#BA
                c.drawString(1.62 * inch, 6.11 * inch, str(data.ix[k, 1][3]))#AB
                c.drawString(.72 * inch, 5.8 * inch, str(data.ix[k, 1][4]))#Runs
                c.drawString(1.50 * inch, 5.8 * inch, str(data.ix[k, 1][5]))#Hits
                c.drawString(.80 * inch, 5.48 * inch, str(data.ix[k, 1][6]))#Doubles
                c.drawString(1.38 * inch, 5.48 * inch, str(data.ix[k, 1][7]))#triples
                c.drawString(.63 * inch, 5.16 * inch, str(data.ix[k, 1][8]))#HR
                c.drawString(1.29 * inch, 5.16 * inch, str(data.ix[k, 1][11]))#RBI
                c.drawString(.78 * inch, 4.85 * inch, str(data.ix[k, 1][2]))#SLGPct
                c.drawString(1.70 * inch, 4.85 * inch, str(data.ix[k, 1][1]))#OBPct
                c.drawString(.73 * inch, 4.54 * inch, str(data.ix[k, 1][9]))#Walks
                c.drawString(1.19 * inch, 4.54 * inch, str(data.ix[k, 1][14]))#K
                c.drawString(.68 * inch, 4.21 * inch, str(data.ix[k, 1][10]))#HBP
                c.drawString(.78 * inch, 3.9 * inch, str(data.ix[k, 1][12]))#SF
                c.drawString(1.26 * inch, 3.9 * inch, str((int)(data.ix[k, 1][18]) - (int)(data.ix[k,1][12])))#SA


                c.drawString(9*inch, 6.4*inch, 'Strikouts (last 10): ' + str(dict[name][0]))
                c.drawString(9*inch, 6.1*inch, 'Walks (last 10): ' + str(dict[name][1]))
                c.drawString(9*inch, 5.8*inch, 'Stolen Bases (last 10): ' + str(dict[name][2]))
                c.drawString(9*inch, 5.5*inch, 'Bunts (last 10): ' + str(dict[name][3]))


                c.drawImage(ImageReader(ground), 9 * inch, 2.1 * inch, mask='auto')
                c.drawImage(ImageReader(line), 9 * inch, 2.7 * inch, mask='auto')
                c.drawImage(ImageReader(fly), 9 * inch, 3.3 * inch, mask='auto')

                c.drawString(9 * inch, 2 * inch, 'Ground')
                c.drawString(9 * inch, 2.6 * inch, 'Line')
                c.drawString(9 * inch, 3.2 * inch, 'Fly')

                c.drawString(9 * inch, 1.5 * inch, 'b = Bunt')
                c.drawString(9 * inch, 1.3 * inch, '__ = Single')
                c.drawString(9 * inch, 1.1 * inch, ' + = Double')
                c.drawString(9 * inch, .9 * inch, ' X = Triple')
                c.drawString(9 * inch, .7 * inch, ' # = Home Run')

                break

        c.showPage()
    c.save()


if __name__ == "__main__":
    printPDFs()
