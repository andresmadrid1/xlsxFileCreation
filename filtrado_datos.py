import xlsxwriter

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

# def create_workbook():
#     workbook = xlsxwriter.Workbook('python_dev.xlsx')
#     worksheet = workbook.add_worksheet()
#     worksheet.set_column('A:A', 20)
#     bold = workbook.add_format({'bold': True})
#     worksheet.write('A1', 'Hello')
#     workbook.close()

def run():

    menu = """
    Pls, select which type of list would you like to create:
    1. python_dev:
    2. platzi_workers:
    3. adults:
    4. old_people:

    """

    option = int(input(menu))
    #print(str(option))
    cont = 1

    if option == 1:
        #all_python_dev = [worker["name"] for worker in DATA if worker["language"] == "python"] 
        all_python_dev = list(filter(lambda worker: worker["language"] == "python", DATA))
        all_python_dev = list(map(lambda worker: worker["name"], all_python_dev))
        workbook = xlsxwriter.Workbook('python_dev.xlsx')
        worksheet = workbook.add_worksheet()
        for worker in all_python_dev:
            worksheet.write('A'+str(cont), worker)
            cont += 1
            #print(worker)
        workbook.close()

    elif option == 2:
        #all_platzi_workerks = [worker["name"] for worker in DATA if worker["organization"] == "Platzi" ]
        all_platzi_workerks = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
        all_platzi_workerks = list(map(lambda worker: worker["name"], all_platzi_workerks))
        workbook = xlsxwriter.Workbook('platzi_workers.xlsx')
        worksheet = workbook.add_worksheet()
        for worker in all_platzi_workerks:
            worksheet.write('A'+str(cont), worker)
            cont += 1
            print(worker)
        workbook.close()
    
    elif option == 3:
        # adults = list(filter(lambda worker: worker["age"] > 18, DATA))
        # adults = list(map(lambda worker: worker["name"], adults))
        adults = [worker["name"] for worker in DATA if worker["age"] > 18]
        workbook = xlsxwriter.Workbook('adults.xlsx')
        worksheet = workbook.add_worksheet()
        for worker in adults:
            worksheet.write('A'+str(cont), worker)
            cont += 1
            print(worker)
        workbook.close()

    elif option == 4:
        #old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
        old_people = [worker | {"old": worker["age"] > 70} for worker in DATA if worker["age"] > 70]
        workbook = xlsxwriter.Workbook('old_people.xlsx')
        worksheet = workbook.add_worksheet()
        for worker in old_people:
            worksheet.write('A'+str(cont), worker["name"])
            worksheet.write('B'+str(cont), worker["age"])
            worksheet.write('C'+str(cont), worker["organization"])
            worksheet.write('D'+str(cont), worker["position"])
            worksheet.write('E'+str(cont), worker["language"])
            worksheet.write('F'+str(cont), worker["old"])
            cont += 1
            print(worker)
        workbook.close()


if __name__=='__main__':
    run()