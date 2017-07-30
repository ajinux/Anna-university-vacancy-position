from time import sleep

import requests
from bs4 import BeautifulSoup as bs
from django.utils.datetime_safe import datetime

from vacancy.models import College, Department, CollegeDepartment, SeatsRemaining, Caste


def get_details(college_code, collg, datetm):
    res = requests.post("http://vacancy.tnea.ac.in",
                        data={'cname': college_code, 'btncname': 'Find', 'ccode': 0, 'bname': 0})

    soup_obj = bs(str(res.text))

    tables = soup_obj.findAll('table')

    castes = ['OC', 'BCM', 'BC', 'MBC', 'SCA', 'SC', 'ST']
    cate_objs = [Caste.objects.get(name=x) for x in castes]

    print len(tables)

    for tr in tables[2]:
        if len(tr) == 30:
            cells = tr.findAll("td")
            # print len(cells)
            count = 0
            department = None
            clgdepart = None
            castes = ['OC', 'BCM', 'BC', 'MBC', 'SCA', 'SC', 'ST']
            caste_objs = [Caste.objects.get(name=x) for x in castes]
            for index, td in enumerate(cells):
                if index == 0:
                    # print "Department: ", td.get_text()
                    department, created = Department.objects.get_or_create(name=td.get_text().strip())
                    clgdepart, created = CollegeDepartment.objects.get_or_create(college=collg, department=department)
                    continue
                if index % 2 == 0:
                    # print "Index : ", index
                    if td.get_text().strip() == "":
                        # print "-1"
                        seats = SeatsRemaining.objects.create(clg_dept=clgdepart, caste=caste_objs[index / 2 - 1],
                                                              seats_remaining=-1, recorded_at=datetm)
                    else:
                        # print td.get_text().strip()
                        seats = SeatsRemaining.objects.create(clg_dept=clgdepart, caste=caste_objs[index / 2 - 1],
                                                              seats_remaining=int(td.get_text().strip()),
                                                              recorded_at=datetm)
                    count = count + 1
                    # print seats.id
            # print "Total count    : ", count
            if count != 7:
                print "Something wrong"


# get_details(2706)


# kct 2712, PSG 2006

def get_remaining_seats(clg):
    for clg_dep in clg.departments.all():
        print "Department :", clg_dep.department
        for seats in clg_dep.clg_dept_seats.all():
            print "Caste : ", seats.caste, ", Seats : ", seats.seats_remaining


def update_vacancy():
    # clg = College.objects.get(counselling_code=2712)
    # get_remaining_seats(clg)
    # pass
    datetm = datetime.now()
    print datetm
    collgs = College.objects.all()
    for collg in collgs:
        print "ID: ", collg.id, ", Name :", collg.name, ", ccode :", collg.counselling_code, "\n"
        get_details(collg.counselling_code, collg, datetm)
