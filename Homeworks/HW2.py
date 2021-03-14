listCv=[]

def list_append ():
     #to add dictionaries to the list. the number of dictionaries can be increased
     listCv.append(cv1)
     listCv.append(cv2)
     listCv.append(cv3)
     listCv.append(cv4)
     listCv.append(cv5)

def iterate_list ():
    #To print the information on the screen
    for person in listCv:
        for k, v in person.items():
            print('{}: {}'.format(k, v))
        print("")
    return

cv1={'Name': 'Onur',
     'Surname': 'Demirel',
     'Age': 22,
     'E-mail':'demirelonur6@gmail.com',
     'Education': 'Türk Alman Üniversitesi',
     'Department': 'Mechatronic Engineering',
     'Work Experience': 'None',
     'Language': 'Turkish-English-German',
     'Skils': 'C-Python-Matlab-AutoCAD'}

cv2={'Name': 'Begüm',
     'Surname': 'Şahin',
     'Age': 22,
     'E-mail':'begüm@gmail.com',
     'Education': 'Türk Alman Üniversitesi',
     'Department': 'Molecular Biology',
     'Work Experience': 'Workt in AB Company (2018-2020)',
     'Language': 'Turkish-English-German',
     'Skils': 'TeamWork-Communication-Leadership'}

cv3={'Name': 'Burak',
     'Surname': 'Susam',
     'Age': 21,
     'E-mail':'berke1223@gmail.com',
     'Education': 'İstanbul Üniversitesi',
     'Department': 'Law',
     'Work Experience': 'Workt in Zoom Company (2018-2029)',
     'Language': 'Turkish-English',
     'Skils': 'TeamWork-Investmen-Social Media Management'}

cv4={'Name': 'Bedirhan',
     'Surname': 'Bülbül',
     'Age': 21,
     'E-mail':'bedoblbl@gmail.com',
     'Education': 'Türk Alman Üniversitesi',
     'Departman': 'Materials Science and Engineering',
     'Work Experience': 'Workt in BKM (2017-2018)-Educator in Darüşafaka',
     'Language': 'Turkish-English-German',
     'Skils': 'Instructor-Communication-Matlab'}

cv5={'Name': 'Oğuzhan',
     'Surname': 'Aktay',
     'Age': 20,
     'E-mail':'ogz3516@gmail.com',
     'Education': 'İzmir Ekonomi Üniversitesi',
     'Departman': 'Software Engineering',
     'Work Experience': 'None',
     'Language': 'Turkish-English',
     'Skils': 'TeamWork-Communication-Java-HTML-CSS-C++-C#'}


list_append()
iterate_list()



