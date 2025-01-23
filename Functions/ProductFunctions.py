import socket
import sys


def GetUrl(): 
    url = input("Paste Link: ")
    return url

def GetRetailer(url):
    try:
        start = 'www.'
        end = '.com'
        retailer = url.split(start)[1].split(end)[0]
        return retailer
    except:
        print("Invalid Link")
        return -1

def ProductMatch(retailer):
    match retailer:
        case "amazon":
            print("Retailer Found: Amazon")
            return True
        case "walmart":
            print("Retailer Found: Walmart")
            return True
        case "target":
            print("Retailer Found: Target")
            return True
        case "costco":
            print("Retailer Found: Costco")
            return True
        case "homedepot":
            print("Retailer Found: Home Depot")
            return True
        case "bestbuy":
            print("Retailer Found: Best Buy")
            return True
        case "walgreens":
            print("Retailer Found: Walgreens")
            return True
        case "cvs":
            print("Retailer Found: CVS")
            return True
        case "lowes":
            print("Retailer Found: Lowe's")
            return True
        case "macys":
            print("Retailer Found: Macy's")
            return True
        case "kohls":
            print("Retailer Found: Kohl's")
            return True
        case "jcpenney":
            print("Retailer Found: JCPenney")
            return True
        case "dollargeneral":
            print("Retailer Found: Dollar General")
            return True
        case "dollartree":
            print("Retailer Found: Dollar Tree")
            return True
        case "nike":
            print("Retailer Found: Nike")
            return True
        case "adidas":
            print("Retailer Found: Adidas")
            return True
        case "gap":
            print("Retailer Found: Gap")
            return True
        case "oldnavy":
            print("Retailer Found: Old Navy")
            return True
        case "sephora":
            print("Retailer Found: Sephora")
            return True
        case "ulta beauty":
            print("Retailer Found: Ulta Beauty")
            return True
        case "gamestop":
            print("Retailer Found: GameStop")
            return True
        case _:
            print("Retailer not found")
            return False

def ContinueProgram():
    while True:
        continuePgrm = input("Continue? Y / N: ").upper()
        if continuePgrm == 'Y':
            return True
        elif continuePgrm == 'N':
            return False
        else: 
            print("Invalid")
            continue

def ScrapeWebsite(retailer):
    if ProductMatch(retailer):
        ProductMatch(retailer) #Print Retailer

def OpenFile():
    # Open in append mode, create the file if it doesn't exist
    return open("ProductList.txt", "a")

def WriteToFile(url, retailer, title, price, f):
    # Write the URL followed by a newline to the file
    f.write("Link:" + url + "\n")
    f.write("Retailer: " + retailer + "\n")
    f.write("Item Name: " + title +"\n")
    f.write("Price: $"+ price +"\n")
    f.write("--------------------------------------------------------------------------------------------------------------------\n")
    print("Item Added to File")

def IsConnected():
    try:
        # Attempt to connect to Google's DNS server
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def CheckConnection():
    if IsConnected():
        print("Network connection successful")
    else:
         print("No network connection detected")
         sys.exit(0)
