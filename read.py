import PyPDF2
from openpyxl import load_workbook

# this part read information from pdf file and place 
# split pdf file in to two pages and extraxt page content to text variables

emails = ["@inbox.lv", "@gmail.com", "@eestikalev.ee"]
tournament_emails = []
tournament_types = []
classic, rapid, blitz = "klasik", "rapid", "blit"

for i in range(1,35):
    FILE=f"regulations/tournament{i}.pdf"
    pdf_file=PyPDF2.PdfReader(open(FILE,"rb"))
    number_of_pages=len(pdf_file.pages)
    print(number_of_pages)
    page1=pdf_file.pages[0]
    text1=page1.extract_text()
    idx = text1.find(emails[0])

    classic = text1.find("klasi")
    rapid = text1.find("rapid")
    if rapid == -1:
        rapid = text1.find("ātrā")
    blitz = text1.find("blic")

    tournament_types.append([classic, rapid, blitz])
    
    email = ""
    if idx == -1 and number_of_pages > 1:
        for at in emails:
            for nr in range(1, number_of_pages):
                page=pdf_file.pages[nr]
                text=page.extract_text()
                # print(text1)
                idx = text.find(at)
                if idx != -1:
                    email = text[idx-20:idx+20]
                    break
            if idx != -1:
                break
    else:
        email = text1[idx-20:idx+20]

    email = email.split()
    for correct in email:
        if correct.find("@") != -1:
            email = correct
            break
    email = email.replace("<","").replace("(","")
    tournament_emails.append(email)
    print(i, classic, rapid, blitz, idx, email)
        
print(tournament_emails)

workbook = load_workbook('tournaments.xlsx')
worksheet=workbook.active

for pos, tournament in enumerate(tournament_emails, 2):
    worksheet['D' + str(pos)] = tournament

for pos, tournament in enumerate(tournament_types, 2):
    if tournament[0] != -1:
        worksheet['E' + str(pos)] = "Klasika"
    elif tournament[1] != -1:
        worksheet['E' + str(pos)] = "Rapid"
    elif tournament[2] != -1:
        worksheet['E' + str(pos)] = "Blitz"
    else:
        worksheet['E' + str(pos)] = "Unknown"

workbook.save('final.xlsx')
workbook.close()