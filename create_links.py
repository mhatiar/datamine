import MySQLdb

def getURLS():

    # connnect to database
    db = MySQLdb.connect(host="snowblossom.mysql.pythonanywhere-services.com",# your host, usually localhost
                 user="snowblossom",# your username
                 passwd="1234test",# your password
                 db="snowblossom$ILOVEOWLS")# name of the data base

    # you must create a Cursor object. It will let you execute all the queries you need
    cur = db.cursor()

    imputURLS = []

    # find last record of the table for standard auctions and find out how many pages have to be crawled.
    cur.execute("SELECT STANDARD FROM OMFGowls ORDER BY ID DESC LIMIT 1;")

    standard = int(cur.fetchone()[0])

    if standard <= 10:
        imputURLS.insert(0, "https://www.zltymelon.sk/auction")
    elif standard <= 20:
        imputURLS.insert(0, "https://www.zltymelon.sk/auction")
        imputURLS.insert(1, "https://www.zltymelon.sk/auction?grid_Standartne_Aukcie-page=2")
    elif standard <= 30:
        imputURLS.insert(0, "https://www.zltymelon.sk/auction")
        imputURLS.insert(1, "https://www.zltymelon.sk/auction?grid_Standartne_Aukcie-page=2")
        imputURLS.insert(2, "https://www.zltymelon.sk/auction?grid_Standartne_Aukcie-page=3")
    elif standard <= 40:
        imputURLS.insert(0, "https://www.zltymelon.sk/auction")
        imputURLS.insert(1, "https://www.zltymelon.sk/auction?grid_Standartne_Aukcie-page=2")
        imputURLS.insert(2, "https://www.zltymelon.sk/auction?grid_Standartne_Aukcie-page=3")
        imputURLS.insert(3, "https://www.zltymelon.sk/auction?grid_Standartne_Aukcie-page=4")

    # find last record of the table for cash-free auctions and find out how many pages have to be crawled.

    cur.execute("SELECT CASHFREE FROM OMFGowls ORDER BY ID DESC LIMIT 1;")

    # variable needs to be converted to int so that it can be used in the condition
    cf = int(cur.fetchone()[0])

    if cf >= 1:
        imputURLS.insert(4, "https://www.zltymelon.sk/loan/list-c-f?language=en_EN")

    # find last record of the table for high-risk auctions and find out how many pages have to be crawled.

    cur.execute("SELECT HIGHRISK FROM OMFGowls ORDER BY ID DESC LIMIT 1;")

    # variable needs to be converted to int so that it can be used in the condition
    hr = int(cur.fetchone()[0])

    if hr >= 1:
        imputURLS.insert(5, "https://www.zltymelon.sk/loan/list-high-risk?language=en_EN")

    db.close()

    print "Final List : ", imputURLS
    return imputURLS
