"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Roman Závorka
email: romanz90zero@gmail.com
discord: romanz90
"""

import requests as r
from bs4 import BeautifulSoup as bs

def municipality_code(link):
        
    server_answer = r.get(link)
    soup = bs(server_answer.text, "html.parser")

    codes = soup.findAll("td", attrs={"class": "cislo"})
    codes_list = list(code.text for code in codes)

    return codes_list
    
def municipality_name(link):
    server_answer = r.get(link)
    soup = bs(server_answer.text, "html.parser")

    names = soup.findAll("td", attrs={"class": "overflow_name"})
    names_list = list(name.text for name in names)

    return names_list

def header(link):

    server_answer = r.get(link)
    soup = bs(server_answer.text, "html.parser")

    party_names = soup.findAll("td", attrs={"class": "overflow_name"})
    header = ["code", "location", "registered", "envelopes", "valid"] + \
        list(name.text for name in party_names)

    return header

def vote_record(link):

    server_answer = r.get(str(link))
    soup = bs(server_answer.text, "html.parser")

    votes_summary = soup.findAll("td", attrs={"class": "cislo"})
    votes_parties1 = soup.findAll(
        "td", attrs={"class": "cislo", "headers": "t1sa2 t1sb3"}
        )
    votes_parties2 = soup.findAll(
        "td", attrs={"class": "cislo", "headers": "t2sa2 t2sb3"}
        )

    record = list(votes.text for votes in votes_summary[3]) + \
        list(votes.text for votes in votes_summary[6:8]) + \
        list(votes.text for votes in votes_parties1) + \
        list(votes.text for votes in votes_parties2)

    return record

def links_list (link):

    server_answer = r.get(link)
    soup = bs(server_answer.text, "html.parser")

    links = soup.find_all("a")
    links_list = list(link.get("href") for link in links)

    condition = lambda x: len(x) < 40

    filter = [x for x in links_list if not condition(x)]
    filtered_list = list(dict.fromkeys(filter))

    return filtered_list

def record_maker(link, order):

    link_prefix = "https://www.volby.cz/pls/ps2017nss/"

    record = []
    record.append(municipality_code(link)[order])
    record.append(municipality_name(link)[order])

    complete_record = record + \
        vote_record(link_prefix + links_list(link)[order])

    return(complete_record)

def input_check(link ="blank", name ="blank"):

    file_name = "results_frýdek-místek.csv"
    input_link = "https://www.volby.cz/pls/ps2017nss/" +\
        "ps32?xjazyk=CZ&xkraj=14&xnumnuts=8102"
   
    if name == file_name and link == input_link:
        return 1
    else:       
        if link == "blank":
            print("Please enter URL link.")
        elif link != input_link:
            print("Wrong web link input.")
        if name == "blank":
            print("Please enter output file name.")
        elif name != file_name:
            print("Wrong file name input.")

def elections_scraper(link, name):
    
    if input_check(link, name) == 1:

        import csv
        link_prefix = "https://www.volby.cz/pls/ps2017nss/"

        new_csv = open(name, mode = "w", newline='')
        writer = csv.writer(new_csv, delimiter=";")
        writer.writerow(header(link_prefix + links_list(link)[0]))

        length = len(municipality_code(link))
        print(f"Initiating data scraping from selected URL: {link}\n"
              f"Saving data into file: {name}.")
        
        index = 0.1
        for number in range(0,length):
            writer.writerow(record_maker(link, number))
            if (number/length) >= index:
                print(f"{round(index*100)}% complete")
                index += 0.1
            
        print(f'100% complete. Your file "{name}" is ready for use.')
        new_csv.close()

def sys_arg_check(order):
    import sys
    if len(sys.argv) >= order + 1:
        return sys.argv[order]
    else:
        return "blank"

elections_scraper(sys_arg_check(1), sys_arg_check(2))

