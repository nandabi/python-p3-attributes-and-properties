#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name = 'Morana', job= 'Legal'):
        self.name = name
        self.job = job

    def getName(self):
        return self._name
    
    def setName(self, name):
        if isinstance(name, str) and 0 < len(name) < 26:
            self._name = name.title()
            # .title() for converting it into a title
        else:
            print ('Name must be string between 1 and 25 characters.')
            

    name = property(getName, setName)

    def getJob(self):
        return self._job
    
    def setJob (self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    job = property(getJob, setJob)
