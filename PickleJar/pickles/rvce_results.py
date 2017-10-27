import requests as rq
from bs4 import BeautifulSoup as BS

from Senses.input import listen
from Senses.output import say


triggers = {

    'get_result': [['get', 'result'], ['fetch', 'result']]

}

class Student(object):
    def __init__(self,programme,usn,name,semester,sgpa):
        self.programme=programme
        self.usn=usn
        self.name=name
        self.semester=semester
        self.sgpa=sgpa
        self.grades={}
    def __str__(self):
        res = "Programme: "+self.programme+"\n"
        res += "USN: "+self.usn+"\n"
        res += "Name: "+self.name+"\n"
        res += "Semester: "+self.semester+"\n"
        res += "SGPA: "+self.sgpa+"\n"
        res += "Grades: "+str(self.grades)+"\n"
        return res
    def __repr__(self):
        return self.__str__()


def getResult(usn, captcha_answer):
    params = {
        "usn":usn,
        "captcha":captcha_answer,
    }
    results_url="http://results.rvce.edu.in/viewresult2.php"
    response = s.post(results_url, data=params)
    result_soup = BS(response.content,"html.parser")
    if(result_soup.find("div", {"id":"no-more-tables"})==None):
        print("USN "+usn+" doesn't exist")
        return None
    tables = result_soup.find_all('tbody')
    #print(tables[1].prettify())
    student_details = tables[0].tr.find_all("td")
    student_courses = tables[1].find_all("tr")
    new_student = Student(*[x.text for x in student_details])
    for c in student_courses:
        course_data = [t.text for t in c.find_all("td")]
        if(course_data[0]!=''):
            new_student.grades[course_data[0]]=course_data[2]
    return new_student


def get_result(s):
    say("Ok. What's your USN?")
    usn_text = listen()
    year,dept_code,roll = usn_text.split()
    usn="1rv"+year+dept_code.lower()+"%03d"%int(roll)
    
    results_form_url="cgit "
    s=rq.session()
    r=s.get(results_form_url)
    soup = BS(r.content, "html.parser")
    captcha = soup.find_all("label")[1].text
    captcha_answer = int(captcha[8])+int(captcha[12])
    print("Captcha:"+captcha_answer)
    result = getResult(usn, captcha_answer)
    return str(result)
