import calendar
import datetime as dt
from IPython.display import HTML
import sys
import re
import subprocess

def display_calendar(month_offset=0):
    if month_offset > 12 or month_offset < -12:
        print("The application does not handle offsets greater than 12 or less than -12")
        return None

    # find out today's date
    t = dt.datetime.today()

    final_month = t.month + month_offset
    final_year = t.year
    if final_month < 1:
        final_month = 12 + final_month
        final_year = final_year - 1
    elif final_month > 12:
        final_month = final_month - 12
        final_year = final_year + 1

    # create HTML Calendar month
    cal = calendar.HTMLCalendar()
    s = cal.formatmonth(final_year, final_month)

    # display calendar without highlighting today 
    # display(HTML(s))

    css = "<style> table {\
    width: 100%;\
    height: 100%;\
    }</style>"
    

    # add cell's backgroundcolor, bold and underling html tags around today's date
    # ss = s.replace('>%i<'%t.day, ' bgcolor="#66ff66"><b><u>%i</u></b><'%t.day)

    pat = re.findall(">\d+", s)
    for i in pat:
        number = i[1:]
        s = s.replace(i, ' style="text-align:center">'+number)

    ss = s.replace('>%i<'%t.day, 'bgcolor="#66ff66"><b>%i</b><'%t.day)
    final_html = "<html>"+css+"<body>"+HTML(ss).data+"</body>"+"</html>"
    # display(HTML(ss))
    with open('calendarApp.html', 'w') as f:
        f.write(final_html)

    subprocess.Popen(["pythonw","calendar_gui.py"])

if __name__=='__main__':
    # Initialize parser 
    help_message = "Project developed by -- \n\
                    Name: Prudhvi Raj Patnala\n\
                    Email: pruthvipatnala@gmail.com\n\
                    **************************\n\
                    Usage Info -- \n\
                    Command - python calendarApp.py <int:month_offset>"
    try:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            print(help_message)
        elif sys.argv[1].isdigit():
            display_calendar(int(sys.argv[1]))
    except IndexError:
        print(help_message)
        display_calendar()

    
