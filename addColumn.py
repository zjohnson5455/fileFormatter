import csv

linkMap = {
    "1": "form1@cognito.com",
    "2": "form2@cognito.com",
    "3": "form3@cognito.com",
    "4": "form4@cognito.com"
}

def editFile():
    with open("testData1.csv", mode= 'r') as file:
        csvFile = csv.reader(file)

        firstLine = True
        listOfLists = []

        for line in csvFile:
            if (firstLine):
                line.append('Link')
                firstLine = False
                listOfLists.append(",".join(line))

            else:
                link = linkMap[line[2]]
                line.append(link)
                listOfLists.append(",".join(line))

    with open("testData1.csv", mode= 'w') as editedFile:
        new_file_contents = "\n".join(listOfLists)
        editedFile.write(new_file_contents)


editFile()
