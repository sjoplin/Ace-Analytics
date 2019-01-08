import random

from PIL import Image
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


def printPDFs(df=None, data=None):
    line = Image.open('line.png')
    fly = Image.open('fly.png')
    ground = Image.open('dashed.png')

    c = canvas.Canvas("../sample.pdf", pagesize=landscape(letter))

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
        field = ImageReader('rightAngleField.gif')
        c.drawImage(field, inch, .5 * inch, 7 * inch, 7 * inch, mask='auto')
        c.setFillColorRGB(1, 0, 0)
        c.drawString(3 * inch, 8 * inch, 'Player Name: ' + name.upper())
        for i in range(len(namesInOrder)):
            if name == namesInOrder.ix[i]:
                thisPlay = play.ix[i]
                thisBallLoc = ballLoc.ix[i]
                # print(thisPlay + " " + thisBallLoc)
                result = None
                if thisPlay == 'grounded' or thisPlay == 'flied' or thisPlay == 'popped' or thisPlay == 'lined' or thisPlay == 'double':
                    result = ''
                elif thisPlay == 'singled':
                    result = '__'
                elif thisPlay == 'doubled':
                    result = '+'
                elif thisPlay == 'tripled':
                    result = 'X'
                elif thisPlay == 'homered':
                    result = '#'
                lineType = None
                if thisPlay == 'grounded' or thisPlay == 'double':
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

                if thisBallLoc == 'p' or thisBallLoc == 'pitcher':  # P
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(135, expand=True)), (5.8 + randx / 2) * inch,
                                    (.55 + randy / 2) * inch, mask='auto')
                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(135, expand=True)), (5.9 + randx / 2) * inch,
                                    (.55 + randy / 2) * inch, mask='auto')
                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(135, expand=True)), (5.8 + randx / 2) * inch,
                                    (.55 + randy / 2) * inch, mask='auto')
                    c.drawString((6 + randx / 2) * inch, (1.61 + randy / 2) * inch, result)
                elif thisBallLoc == '1b' or thisBallLoc == 'first':  # 1B
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(95, expand=True)), (6.95 + randx / 2) * inch,
                                    (1.85 + randy / 2) * inch, mask='auto')
                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(95, expand=True)), (7.05 + randx / 2) * inch,
                                    (1.85 + randy / 2) * inch, mask='auto')
                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(95, expand=True)), (7 + randx / 2) * inch,
                                    (1.85 + randy / 2) * inch, mask='auto')
                    c.drawString((7.1 + randx / 2) * inch, (3.25 + randy / 2) * inch, result)
                elif thisBallLoc == '2b' or thisBallLoc == 'second':  # 2B
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(115, expand=True)), (5.3 + randx) * inch,
                                    (2.25 + randy / 2) * inch, mask='auto')
                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(115, expand=True)), (5.4 + randx) * inch,
                                    (2.15 + randy / 2) * inch, mask='auto')
                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(115, expand=True)), (5.3 + randx) * inch,
                                    (2.25 + randy / 2) * inch, mask='auto')
                    c.drawString((5.5 + randx) * inch, (3.55 + randy / 2) * inch, result)
                elif thisBallLoc == '3b' or thisBallLoc == 'third':  # 3B
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(175, expand=True)), (4.3 + randx / 2) * inch,
                                    (.55 + randy / 2) * inch, mask='auto')
                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(175, expand=True)), (4.4 + randx / 2) * inch,
                                    (.6 + randy / 2) * inch, mask='auto')
                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(175, expand=True)), (4.3 + randx / 2) * inch,
                                    (.57 + randy / 2) * inch, mask='auto')
                    c.drawString((4.45 + randx / 2) * inch, (0.8 + randy / 2) * inch, result)
                elif thisBallLoc == 'shortstop' or thisBallLoc == 'ss' or thisBallLoc == 'short':  # SS
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(150, expand=True)), (4.05 + randx / 2) * inch,
                                    (1.2 + randy) * inch, mask='auto')
                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(150, expand=True)), (4.15 + randx / 2) * inch,
                                    (1.2 + randy) * inch, mask='auto')
                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(150, expand=True)), (4.05 + randx / 2) * inch,
                                    (1.2 + randy) * inch, mask='auto')
                    c.drawString((4.25 + randx / 2) * inch, (2 + randy) * inch, result)
                elif (thisBallLoc == 'lf' or thisBallLoc == 'left') and thisPlay != 'homered':  # LF
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(165, expand=True)), (1.45 + randx * 1.5) * inch,
                                    (.95 + randy * 2.5) * inch, mask='auto')
                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(165, expand=True)), (1.55 + randx * 1.5) * inch,
                                    (.95 + randy * 2.5) * inch, mask='auto')
                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(165, expand=True)), (1.45 + randx * 1.5) * inch,
                                    (.95 + randy * 2.5) * inch, mask='auto')
                    c.drawString((1.65 + randx * 1.5) * inch, (1.45 + randy * 2.5) * inch, result)
                elif (thisBallLoc == 'cf' or thisBallLoc == 'center') and thisPlay != 'homered':  # CF
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(135, expand=True)), (2.2 + randx * 1.5) * inch,
                                    (3.2 + randy * 1.5) * inch, mask='auto')
                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(135, expand=True)), (2.3 + randx * 1.5) * inch,
                                    (3.2 + randy * 1.5) * inch, mask='auto')
                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(135, expand=True)), (2.2 + randx * 1.5) * inch,
                                    (3.2 + randy * 1.5) * inch, mask='auto')
                    c.drawString((2.4 + randx * 1.5) * inch, (4.36 + randy * 1.5) * inch, result)
                elif (thisBallLoc == 'rf' or thisBallLoc == 'right') and thisPlay != 'homered':  # RF
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(105, expand=True)), (4.6 + randx * 2) * inch,
                                    (4.25 + randy * 1.5) * inch, mask='auto')
                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(105, expand=True)), (4.7 + randx * 2) * inch,
                                    (4.15 + randy * 1.5) * inch, mask='auto')
                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(105, expand=True)), (4.6 + randx * 2) * inch,
                                    (4.25 + randy * 1.5) * inch, mask='auto')
                    c.drawString((4.8 + randx * 2) * inch, (5.55 + randy * 1.5) * inch, result)
                # # LeftCenter
                #     c.drawImage(ImageReader(fly.rotate(150, expand=True)),2.3*inch,3*inch,mask = 'auto')
                #     c.drawImage(ImageReader(ground.rotate(150, expand=True)),2.4*inch,3*inch,mask = 'auto')
                #     c.drawImage(ImageReader(line.rotate(150, expand=True)),2.3*inch,3*inch,mask = 'auto')
                #     c.drawString(2.5*inch,3.8*inch, "X")
                # # RightCenter
                #     c.drawImage(ImageReader(fly.rotate(115, expand=True)),4.3*inch,5*inch,mask = 'auto')
                #     c.drawImage(ImageReader(ground.rotate(115, expand=True)),4.4*inch,4.9*inch,mask = 'auto')
                #     c.drawImage(ImageReader(line.rotate(115, expand=True)),4.3*inch,5*inch,mask = 'auto')
                #     c.drawString(4.5*inch,6.3*inch, "X")
                elif thisBallLoc == 'down lf' or thisBallLoc == 'down left':  # LeftLine
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(175, expand=True)), (1.1 + randx * 2) * inch,
                                    (.55 + randy * .5) * inch, mask='auto')
                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(175, expand=True)), (1.2 + randx * 2) * inch,
                                    (.6 + randy * .5) * inch, mask='auto')
                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(175, expand=True)), (1.1 + randx * 2) * inch,
                                    (.57 + randy * .5) * inch, mask='auto')
                    c.drawString((1.25 + randx * 2) * inch, (.8 + randy / 2) * inch, result)
                elif thisBallLoc == 'down rf' or thisBallLoc == 'down right':  # RightLine
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(95, expand=True)), (7.05 + randx / 2) * inch,
                                    (3.75 + randy * 1.5) * inch, mask='auto')
                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(95, expand=True)), (7.15 + randx / 2) * inch,
                                    (3.75 + randy * 1.5) * inch, mask='auto')
                    c.drawImage(ImageReader(line.rotate(95, expand=True)), (7.1 + randx / 2) * inch,
                                (3.75 + randy * 1.5) * inch, mask='auto')
                    c.drawString((7.2 + randx / 2) * inch, (5.15 + randy * 1.5) * inch, result)
                elif thisBallLoc == 'middle':  # UpMid
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(135, expand=True)), (4.15 + randx / 2) * inch,
                                    (2.85 + randy / 2) * inch, mask='auto')
                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(135, expand=True)), (4.25 + randx / 2) * inch,
                                    (2.85 + randy / 2) * inch, mask='auto')
                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(135, expand=True)), (4.05 + randx / 2) * inch,
                                    (2.85 + randy / 2) * inch, mask='auto')
                    c.drawString((4.3 + randx / 2) * inch, (3.95 + randy / 2) * inch, result)
                elif thisBallLoc == 'lf' or thisBallLoc == 'left':  # HRLF
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(165, expand=True)), (.35 + randx * .5) * inch,
                                    (0.7 + randy * 2) * inch, mask='auto')
                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(165, expand=True)), (.45 + randx * .5) * inch,
                                    (0.7 + randy * 2) * inch, mask='auto')
                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(165, expand=True)), (.35 + randx * .5) * inch,
                                    (0.7 + randy * 2) * inch, mask='auto')
                    c.drawString((.45 + randx * .5) * inch, (1.2 + randy * 2) * inch, result)
                # # HRLCF
                #     c.drawImage(ImageReader(fly.rotate(150, expand=True)),1*inch,3.5*inch,mask = 'auto')
                #     c.drawImage(ImageReader(ground.rotate(150, expand=True)),1.1*inch,3.5*inch,mask = 'auto')
                #     c.drawImage(ImageReader(line.rotate(150, expand=True)),1*inch,3.5*inch,mask = 'auto')
                #     c.drawString(1.2*inch,4.3*inch, "X")
                elif thisBallLoc == 'cf' or thisBallLoc == 'center':  # HRCF
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(135, expand=True)), (1.4 + randx * .75) * inch,
                                    (4.4 + randy * .75) * inch, mask='auto')
                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(135, expand=True)), (1.5 + randx * .75) * inch,
                                    (4.4 + randy * .75) * inch, mask='auto')
                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(135, expand=True)), (1.4 + randx * .75) * inch,
                                    (4.4 + randy * .75) * inch, mask='auto')
                    c.drawString((1.6 + randx * .75) * inch, (5.46 + randy * .75) * inch, result)
                # # HRRCF
                #     c.drawImage(ImageReader(fly.rotate(115, expand=True)),4*inch,6.3*inch,mask = 'auto')
                #     c.drawImage(ImageReader(ground.rotate(115, expand=True)),4.1*inch,6.2*inch,mask = 'auto')
                #     c.drawImage(ImageReader(line.rotate(115, expand=True)),4*inch,6.3*inch,mask = 'auto')
                #     c.drawString(4.2*inch,7.6*inch, "X")
                elif thisBallLoc == 'rf' or thisBallLoc == 'right':  # HRRF
                    randx = random.random()
                    randy = random.random()
                    if linePlay == 2:
                        c.drawImage(ImageReader(fly.rotate(105, expand=True)), (5.05 + randx * 1.5) * inch,
                                    (6.15 + randy / 2) * inch, mask='auto')
                    elif linePlay == 0:
                        c.drawImage(ImageReader(ground.rotate(105, expand=True)), (5.15 + randx * 1.5) * inch,
                                    (6.05 + randy / 2) * inch, mask='auto')
                    elif linePlay == 1:
                        c.drawImage(ImageReader(line.rotate(105, expand=True)), (5.05 + randx * 1.5) * inch,
                                    (6.15 + randy / 2) * inch, mask='auto')
                    c.drawString((5.25 + randx * 1.5) * inch, (7.45 + randy / 2) * inch, result)
        for k in range(len(data)):
            if data.ix[k, 0].upper() in name.upper():
                c.drawString(8 * inch, 7.8 * inch, 'WOBA: ' + str(data.ix[k, 1][14]))
                c.drawString(8 * inch, 7.6 * inch, 'Steals: ' + str(data.ix[k, 1][12]) + ' / ' + str(data.ix[k, 1][15]))
                c.drawString(8 * inch, 7.4 * inch,
                             'AVG: ' + str(data.ix[k, 1][0]) + ' OBP: ' + str(data.ix[k, 1][1]) + '  SLG: ' + str(
                                 data.ix[k, 1][2]))
                c.drawString(8 * inch, 7.2 * inch,
                             'AB: ' + str(data.ix[k, 1][3]) + '  Hits: ' + str(data.ix[k, 1][4]) + '  2B: ' + str(
                                 data.ix[k, 1][5]))
                c.drawString(8 * inch, 7.0 * inch, '3B: ' + str(data.ix[k, 1][6]) + '  HR: ' + str(data.ix[k, 1][7]))
                c.drawString(8 * inch, 6.8 * inch, 'BB/k: ' + str(data.ix[k, 1][8]) + ' / ' + str(data.ix[k, 1][11]))
                c.drawString(8 * inch, 6.6 * inch, 'SF/SH: ' + str(data.ix[k, 1][9]) + ' / ' + str(data.ix[k, 1][10]))

                c.drawImage(ImageReader(ground), 8 * inch, 2.1 * inch, mask='auto')
                c.drawImage(ImageReader(line), 8 * inch, 2.7 * inch, mask='auto')
                c.drawImage(ImageReader(fly), 8 * inch, 3.3 * inch, mask='auto')

                c.drawString(8 * inch, 2 * inch, 'Ground')
                c.drawString(8 * inch, 2.6 * inch, 'Line')
                c.drawString(8 * inch, 3.2 * inch, 'Fly')

                c.drawString(8 * inch, 1.3 * inch, '__ = Single')
                c.drawString(8 * inch, 1.1 * inch, ' + = Double')
                c.drawString(8 * inch, .9 * inch, ' X = Triple')
                c.drawString(8 * inch, .7 * inch, ' # = Home Run')

        c.showPage()
    c.save()


if __name__ == "__main__":
    printPDFs()
