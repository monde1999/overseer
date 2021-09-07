# overseer
This is the server side of flood forecast module.
To run: python manage.py runserver

To add data, go to http://locationhost:8000/forecast/reports/ .
 Data are automatically made on the other tables when a report is done


To use report Reaction,
link:  ../report/react-to-report/
send data in json format:
{
    "user": {user_id}[required]
    "report": {report_id}[required]
    "isPositive": {True|False}[required]
}