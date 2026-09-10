import pgzrun

TITLE = "IT'S TV TIME!"
WIDTH = 870
HEIGHT = 650

marqbx = Rect(0,0,880,80)
quesbx = Rect(0,0,650,150)
timbx = Rect(0,0,150,150)
ansbx1 = Rect(0,0,300,150)
ansbx2 = Rect(0,0,300,150)
ansbx3 = Rect(0,0,300,150)
ansbx4 = Rect(0,0,300,150)
skibx = Rect(0,0,150,330)

score = 0
timlft = 20
qusflenm = "question.txt"
marqmess = ""
isgamov = False

ansboxs = [ansbx1,ansbx2,ansbx3,ansbx4]
anscolr = [(255, 219, 87),(255, 219, 87),(255, 219, 87),(255, 219, 87)]

questions = []
quescnt = 0
quesindx = 0
marx = 0

marqbx.move_ip(0,0)
quesbx.move_ip(20,100)
timbx.move_ip(700,100)
ansbx1.move_ip(20,270)
ansbx2.move_ip(370,270)
ansbx3.move_ip(20,450)
ansbx4.move_ip(370,450)
skibx.move_ip(700,270)

def draw():
    global marqmsg

    screen.clear()
    screen.fill((201, 62, 62))

    screen.draw.filled_rect(marqbx.inflate(13,13), (255, 219, 87))
    screen.draw.filled_rect(quesbx.inflate(13,13), (115, 104, 153))
    screen.draw.filled_rect(timbx.inflate(13,13), (115, 104, 153))
    screen.draw.filled_rect(skibx.inflate(13,13), (132, 196, 116))

    screen.draw.filled_rect(marqbx, (255, 69, 69))
    screen.draw.filled_rect(quesbx, (169, 145, 255))
    screen.draw.filled_rect(timbx, (255, 255, 255))
    screen.draw.filled_rect(skibx, (173, 255, 153))

    for ansbx, color in zip(ansboxs, anscolr):
        screen.draw.filled_rect(ansbx.inflate(13,13), color)
        screen.draw.filled_rect(ansbx, (255, 69, 69))

    marqmess = "IT'S TV TIME!"
    marqmess +=f"  Q: {quesindx} of {quescnt}"

    screen.draw.text(str(marqmess),center = (marx,40), fontname = "pixel", fontsize = 60, anchor = (0.5, 0.5))

    screen.draw.text(str(timlft),(timbx.centerx, timbx.centery), fontname = "pixel", fontsize = 60, color = (115, 104, 153), anchor = (0.5, 0.5))

    screen.draw.text("SKIP", (skibx.centerx, skibx.centery), fontname = "pixel", fontsize = 60, angle = -90, anchor = (0.5, 0.5))

    screen.draw.textbox(questions[0].strip(), quesbx, fontname = "pixel")

    indx = 1

    for ansbx in ansboxs:
        screen.draw.textbox(questions[indx].strip(), ansbx)
        indx += 1

def update():
    global marx
    
    marx += 5

def requesfil():
    global quescnt, questions

    with open(qusflenm, "r") as qfile:
        for q in qfile:
            questions.append(q)
            quescnt += 1

def rednxtques():
    global quesindx

    if quesindx < len(questions):
        q = questions[quesindx]
        quesindx += 1
        return q.split(',')

    else:
        gameover()
        return["GAME OVER","-","-","-","-","5"]

def onmsedwn(pos):
    index = 1
    for box in ansboxs:
        if box.collidepoint(pos):
            try:
                corropt = int(question[5].strip())
            except:
                corropt = 0

            if index == corropt:
                corrans()

            else:
                wronans()

        index += 1

    if skibx.collidepoint(pos):
        skiques()

def corrans():
    global score

    score += 1
    nexques()

def wronans():
    nexques()

def nexques():
    global question, timlft

    if quesindx < quescnt:
        question = rednxtques()
        timlft = 20

    else:
        gameover()

def gameover():
    global question, timlft, isgamov

    message = f"GAME OVER\nScore: {score}/{quescnt}"
    question = [message,"-","-","-","-","5"]
    timlft = 0
    isgamov = True

def skiques():
    global question, timlft

    if quesindx < quescnt and not isgamov:
        question = rednxtques()
        timlft = 20

    else:
        gameover()

def updtimtlft():
    global timlft

    if timlft > 0 and not isgamov:
        timlft -= 1

    else:
        nexques

requesfil()
question = rednxtques()
clock.schedule_interval(updtimtlft, 1)

pgzrun.go()