import time
import threading
import random

TOP = 6
BOTTOM = 1
STATE = {0:"Дверь открыта",1:"Дверь закрыта",2:"Лифт поднимается",3:"Лифт падает"}
DIR = {0:"Вниз", 1:"Up"}

lock = threading.Lock()
class Msg:
    def __init__(self,type,value):
        self.type = type
        self.value = value

exitFlag = []
MsgQueue = []


def Msgfunction():

    global  MsgQueue,exitFlag
    for i in range(4):
        type = random.randint(0, 3)
        value = 0
        if type == 0:
            value = random.randint(0, 2)
            if lock.acquire():
                exitFlag.append(1)
                lock.release()
        if type == 2:
            value = random.randint(BOTTOM,TOP-1)
        if type == 3:
            value = random.randint(BOTTOM+1,TOP)
        if type == 1:
            value = random.randint(BOTTOM, TOP)

        TIME = random.randint(1, 8)
        m = Msg(type, value)
        if lock.acquire():
            MsgQueue.append(m)
            print("Создать кодировку сообщения:"+ str([m.type,m.value]))
            lock.release()
        time.sleep(TIME)


def closed(state, cur, d):

    if d == 1:
        if startup(cur,d):
            state = 2
        else:
            d = 0
            if startup(cur,d):
                state = 3
            else:
                return state,cur,d
    else:
        if startup(cur,d):
            state = 3
        else:
            d = 1
            if startup(cur,d):
                state = 2
            else:
                return state,cur,d
    return state,cur,d

def up(state,cur,d):
    while True:
        state = state
        if stop(cur,d):
            state = 1
            print("Текущее состояние:% s, текущий этаж:% d, направление движения:% s" % (STATE[state], cur, DIR[d]))
            break
        cur +=1
        print("Переход на уровень% d ..." % cur)
        time.sleep(2)
    return state,cur,d


def down(state,cur,d):
    while True:
        state = state
        if stop(cur,d):
            state = 1
            print("Текущее состояние:% s, текущий этаж:% d, направление движения:% s" % (STATE[state], cur, DIR[d]))
            break
        cur -=1
        print("Переход на уровень% d ..." % cur)
        time.sleep(2)


    return state,cur,d


def startup(cur,d):
    global MsgQueue
    tmp = False
    if d == 1:
        for m in MsgQueue:
            if m.type == 1 and m.value > cur:
                tmp = True
            if m.type == 2 and m.value > cur:
                tmp = True
            if m.type == 3 and m.value > cur:
                tmp = True
    if d == 0:
        for m in MsgQueue:
            if m.type == 1 and m.value < cur:
                tmp = True
            if m.type == 2 and m.value < cur:
                tmp = True
            if m.type == 3 and m.value < cur:
                tmp = True

    return tmp


def stop(cur,d):
    global MsgQueue
    tmp = False
    if d == 1:
        if cur == TOP:
            tmp = True
        tmplist = MsgQueue[:]
        for m in MsgQueue:
            if m.type == 1 and m.value == cur:
                tmp = True
                tmplist.remove(m)
            if m.type == 2 and m.value == cur:
                tmp = True
                tmplist.remove(m)
        MsgQueue = tmplist[:]
    if d == 0:
        if cur == BOTTOM:
            tmp = True
        tmplist = MsgQueue[:]
        for m in MsgQueue:
            if m.type == 1 and m.value == cur:
                tmp = True
                tmplist.remove(m)
            if m.type == 3 and m.value == cur:
                tmp = True
                tmplist.remove(m)
        MsgQueue = tmplist[:]
    return tmp


def closeThread():
    global exitFlag
    counter = 3
    print("Закрыто ...")
    while counter:
        if exitFlag != [1]:
            print("Закрытая дверь")
            break
        time.sleep(1)
        counter -=1
    if counter == 0:
        print("Это было закрыто.")



def closedoor():

    t = threading.Thread(target=closeThread)
    t.start()
    t.join()



def openThread():
    global exitFlag
    counter = 3
    print("Дверь открывается ...")
    while counter:
        if exitFlag != [1]:
            print("Конец двери")
            break
        time.sleep(1)
        counter -=1
    if counter == 0:
        print("Дверь была открыта")


def opendoor():

    t = threading.Thread(target=openThread)
    t.start()
    t.join()


def statemachine():
    global MsgQueue,exitFlag
    state = 0
    cur = 1
    d = 0
    while True:
        time.sleep(0.3)
        print("Текущее состояние:% s, текущий этаж:% d, направление движения:% s" % (STATE[state], cur, DIR[d]))
        if MsgQueue == [] and state == 1:
            continue
        if exitFlag != []:
            tmplist = MsgQueue[:]
            for m in tmplist:
                if m.type == 0 and m.value == 0:
                    if state == 0:
                        state = 1
                        closedoor()
                    exitFlag.pop(0)
                    tmplist.remove(m)
                if m.type == 0 and m.value == 1:
                    if state == 1 or state == 0:
                        state = 0
                        opendoor()
                    exitFlag.pop(0)
                    tmplist.remove(m)
                if m.type == 0 and m.value == 2:
                    if state == 1:
                        state = 0
                        opendoor()
                    exitFlag.pop(0)
                    tmplist.remove(m)
            MsgQueue = tmplist[:]
            continue

        if state == 0:
            counter = 4
            while counter:
                if exitFlag != []:
                    print("Тайм-аут прерван")
                    break
                time.sleep(1)
                counter -= 1
            if counter == 0:
                print("Тайм-аут")
                exitFlag.append(1)
                closedoor()
                exitFlag.pop(0)
                state = 1
            continue
        if state == 1:
            if MsgQueue == []:
                continue
            state, cur, d = closed(state, cur, d)
            continue
        if state == 2:
            if MsgQueue == []:
                continue
            state,cur,d = up(state, cur, d)
            if state == 1:
                exitFlag.append(1)
                opendoor()
                exitFlag.pop(0)
                state = 0
            continue
        if state == 3:
            if MsgQueue == []:
                continue
            state,cur,d = down(state, cur, d)
            if state == 1:
                exitFlag.append(1)
                opendoor()
                exitFlag.pop(0)
                state = 0
            continue


if __name__ == "__main__":

    thread1 = threading.Thread(target=Msgfunction)
    thread2 = threading.Thread(target=statemachine)
    thread1.start()
    thread2.start()
