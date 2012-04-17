# coding=utf-8

from calendar import HTMLCalendar
from datetime import date
from itertools import groupby
from django.utils.html import conditional_escape as esc

from onlinedoc.accounts.models import Doctor
from onlinedoc.worktimes.models import Worktime

class VisitsCalendar(HTMLCalendar):
    
    def __init__(self, doctor):
        super(VisitsCalendar, self).__init__()
        self.worktimes = Worktime.objects.filter(doctor_id=doctor)

    def formatday(self, day, weekday):
        """
        Return a day as a table cell.
        """
        if day == 0:
            return '<td class="noday">&nbsp;</td>' # day outside month
        else:
            if len(self.worktimes.filter(day=weekday+1))==0:
                return '''
                    <td class="%s">
                        <div class="day">
                            <span class="day_number">%d, %d</span>
                        </div>
                    </td>
                    ''' % (self.cssclasses[weekday], day, weekday)
            else:
                return '''
                    <td class="%s">
                        <div class="day worktime">
                            <span class="day_number">%d, %d</span>
                        </div>
                    </td>
                    ''' % (self.cssclasses[weekday], day, weekday)