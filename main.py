from Functions.ProductFunctions import *
from Functions.ProductScraperFunctions import *

CheckConnection()
try:
    while True:
        file = OpenFile()

        url = GetUrl()

        retailer = GetRetailer(url)

        # If retailer extraction fails, skip the rest of the loop
        if retailer == -1:
            print("Please provide a valid URL.")
            continue

        # Check if the retailer matches
        if not ProductMatch(retailer):
            print("Retailer not recognized. Skipping entry.")
            continue
        else:
            title, price = ScrapeRetailer(retailer, url)
        # Write the data to the file
        WriteToFile(url, retailer, title, price, file)

        # Close the file after writing
        file.close()

        # Prompt the user to continue or exit
        if not ContinueProgram():
            print("Exiting the program.")
            break

except KeyboardInterrupt:
        print("\nUser Cancelled")
