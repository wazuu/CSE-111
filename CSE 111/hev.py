import math
import csv
from posixpath import lexists
from pupils import read_compound_list
filename = "10301_hev_sale_2-28-20.csv"
year = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
sales = [5562, 15556, 20119, 24627, 53991, 107897, 106971, 181221, 158886, 139682, 140928, 136463, 223906, 222140, 194108, 180603, 134155, 87725, 59995, 47862]
vehicle_brands = """Honda Insight,Toyota Prius, Honda Civic, Ford Escape/Mercury Mariner, Honda Accord, Toyota Highlander, Lexus RX 450h, Toyota Camry ,Lexus GS 450h
    Nissan Altima, Lexus LS 600hL, Saturn Vue, Tahoe, Yukon, Escalade, Chevrolet Malibu, Saturn Aura, Aspen & Durango, Silverado & Sierra, Ford Fusion & Milan
    Lexus HS 250h, Mercedes S400, Mercedes ML450, Mercedes E320, Mazda Tribute, BMW X6 & Activehybrid 3&5&7, Honda CR-z, Lincoln MKZ, Porsche Cayenne, Lexus CT 200h
    VW Touareg, Infinity Q70 (formerly M Hybrid), Hyundai Sonata, Buick LaCrosse, Buick Regal, Porsche Panamera S, Kia Optima Acura ILX, Ford C-Max Hybrid, Lexus  ES Hybrid
    Audi Q5 Hybrid, Toyota Avalon, VW Jetta, Mercedes E400h, Infiniti Q50, Chevrolet Impala Hybrid, Infiniti QX60, Nissan Pathfinder Hybrid, Subaru XV,Acura RLX
    Lexus NX Hybrid, Toyota RAV4, Acura NSX, Kia Niro, Hyundai Ioniq Hybrid, Acura MDX Hybrid, GMC Sierra Hybrid, Lexus LC500h, Nissan Rogue Hybrid, Lexus LS 500h, Lexus UX, Toyota Corolla"""


def main():
    vehicles_list = read_compound_list("10301_hev_sale_2-28-20.csv")
    print(vehicles_list)
    vehicles_list.pop(0)
    vehicles_list.pop()
    for i in range(len(vehicles_list)):
        if vehicles_list[i] == "Total":
                vehicles_list[i] == "Total"

    total = vehicles_list.count("Total")
    print()
    year_list = str(year)[1:-1]
    print("Years of hev vehicles were sold in the United States:", year_list)
    print()
    print("Brands of hev vehicles sold in the United States between 1990 and 2019", vehicle_brands)
    print()
    
    print()
    print(f"Between 1999 and 2019, the total amound of hev vehicles that were sold in the United States were: 5,374,023" )
    total = sum(sales)
    print()
    print(f"Between the years 2000 and 2019, the total amount of Toyota Prius that were sold in the United States were:", total)

def elctrical_vehicles(filename):
    text_list = []
    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)

    return text_list



if __name__ == "__main__":
    main()