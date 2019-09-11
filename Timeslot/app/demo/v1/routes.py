# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.timelots import Timelots
from .api.timeslots_timeslot import TimeslotsTimeslot
from .api.dentist_dentist import DentistDentist
from .api.timeslotsdentist_time import TimeslotsdentistTime


routes = [
    dict(resource=Timelots, urls=['/timelots'], endpoint='timelots'),
    dict(resource=TimeslotsTimeslot, urls=['/timeslots/<int:timeslot>'], endpoint='timeslots_timeslot'),
    dict(resource=DentistDentist, urls=['/dentist/<dentist>'], endpoint='dentist_dentist'),
    dict(resource=TimeslotsdentistTime, urls=['/timeslotsdentist/<time>'], endpoint='timeslotsdentist_time'),
]