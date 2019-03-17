# Dummy Data Generator
# 2/11/19

import sqlite3
import random
import datetime
import time

def fill_dep():
    dname = ['Human Resource', 'Marketing', 'Finance', 'Maintenance']
    head = [1999, 999, 111, 4444]
    for i in range(len(dname)):
        created = str(random.randint(2000, 2019)) + "-" + str(random.randint(1, 12)) \
                  + "-" + str(random.randint(1, 28))
        c.execute("INSERT INTO Department VALUES(?,?,?,?)", (i, dname[i], created, head[i]))


def fill_emp():
    fname = list(open('FirstNames.txt'))
    mname = list(open('MiddleNames.txt'))
    lname = list(open('LastNames.txt'))
    stname = list(open('StreetNames.txt'))
    empID = [x for x in range(50)]
    title = ['Developer', 'Worker', 'Supervisor', 'Manager']
    for i in range(50):
        fRan = random.randint(0, len(fname) - 1)
        mRan = random.randint(0, len(mname) - 1)
        lRan = random.randint(0, len(lname) - 1)
        address = str(random.randint(1000, 10000)) + " " + stname[i]
        created = str(random.randint(2010, 2019)) + "-" + str(random.randint(1, 12)) \
                  + "-" + str(random.randint(1, 28))
        c.execute("INSERT INTO Employee VALUES(?,?,?,?,?,?,?,?,?)",
                  (empID[i], fname[fRan], mname[mRan], lname[lRan],
                   address, random.randint(1, 4), created,
                   title[random.randint(0, 3)], random.randint(30000, 150000)))
    return empID


def fill_inv():
    ran = random.randint(1, 67)
    partID = [x for x in range(ran)]
    locations = list(open('Locations.txt'))
    for i in range(ran):
        quantity = random.randint(1, 1000)
        locRan = random.randint(0, len(locations) - 1)
        created = str(random.randint(2000, 2019)) + "-" + str(random.randint(1, 12)) + "-" + str(random.randint(1, 28))
        # st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
        c.execute("INSERT INTO Inventory VALUES(?,?,?,?)",
                  (partID[i], quantity, created, locations[locRan]))
    return partID


def fill_maint(maint, empID):
    for i in range(maint):
        ran = random.randint(1, 49)
        created = str(random.randint(2018, 2019)) + "-" + str(random.randint(1, 12)) + "-" + str(random.randint(1, 28))
        c.execute("INSERT INTO Maintenance VALUES(?,?,?)",
                  (i, empID[i], created))


def fill_part(pID):
    plst = list(open('Pname.txt'))
    for i in range(len(pID)):
        c.execute("INSERT INTO Part VALUES(?,?)", (pID[i],
                                                   plst[i]))


def fill_RL(rDict, empID):
    locations = list(open('Locations.txt'))
    rockets = list(open('RocketNames.txt'))
    for i in range(len(rockets) // 2):
        launchName = str(rockets[i]) + str(" Launch")
        locRan = random.randint(0, len(locations) - 1)
        c.execute("INSERT INTO Rocket_Launch VALUES(?,?,?,?)",
                  (i, launchName, empID[i], locations[locRan]))


def fill_rocket():
    rDict = {}
    rname = list(open('RocketNames.txt'))
    maintlst = []
    for i in range(len(rname)):
        lastm = str(random.randint(2018, 2019)) + "-" + str(random.randint(1, 12)) + "-" + str(random.randint(1, 28))
        c.execute("INSERT INTO Rocket VALUES(?,?,?)",
                  (i, rname[i], lastm))
        rDict[rname[i]] = i
        maintlst.append(lastm)
    return rDict, len(maintlst)


if __name__ == "__main__":
    conn = sqlite3.connect("475.db")
    c = conn.cursor()

    fill_dep()
    empID = fill_emp()
    a = fill_inv()
    fill_part(a)
    b, maint = fill_rocket()
    fill_RL(b, empID)
    fill_maint(maint, empID)

    c.close()
    conn.commit()
    conn.close()


#
