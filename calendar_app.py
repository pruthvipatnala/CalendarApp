"""
Calendar
"""
import calendar
import datetime as dt
import sys
import re
import subprocess
from IPython.display import HTML


def display_calendar(month_offset=0):
    """
    Function to display calendar with current date highlighted
    """

    if month_offset > 12 or month_offset < -12:
        print("The application does not handle offsets greater than 12 or less than -12")
        return None

    # Todays's Date
    today = dt.datetime.today()

    final_month = today.month + month_offset
    final_year = today.year

    if final_month < 1:
        final_month = 12 + final_month
        final_year = final_year - 1
    elif final_month > 12:
        final_month = final_month - 12
        final_year = final_year + 1

    # create HTML Calendar month
    cal = calendar.HTMLCalendar()
    html_string = cal.formatmonth(final_year, final_month)

    css = "<style> table {\
    width: 100%;\
    height: 100%;\
    }</style>"

    # ss = s.replace('>%i<'%t.day, ' bgcolor="#66ff66"><b><u>%i</u></b><'%t.day)

    pat = re.findall(r">\d+", html_string)
    for i in pat:
        number = i[1:]
        html_string = html_string.replace(i, ' style="text-align:center">'+number)

    html_string = html_string.replace('>%i<'%today.day, 'bgcolor="#34C420"><b>%i</b><'%today.day)
    final_html = "<html>"+css+"<body>"+HTML(html_string).data+"</body>"+"</html>"

    # Creating HTML file used by GUI
    with open('calendarApp.html', 'w') as html_file:
        html_file.write(final_html)

    # Opening the GUI in background
    subprocess.Popen(["pythonw", "calendar_gui.py"])
    return None

if __name__ == '__main__':
    # Initialize parser
    HELP_MESSAGE = "Project developed by -- \n\
                    Name: Prudhvi Raj Patnala\n\
                    Email: pruthvipatnala@gmail.com\n\
                    **************************\n\
                    Usage Info -- \n\
                    Command - python calendarApp.py <int:month_offset>"
    try:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            print(HELP_MESSAGE)
        elif sys.argv[1].isdigit():
            display_calendar(int(sys.argv[1]))
    except IndexError:
        print(HELP_MESSAGE)
        display_calendar()
