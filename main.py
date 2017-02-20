

import webapp2
import cgi
print ("Hannah's here !")
header = "<h2 style='color:white;background-color:rgb(145,0,0);text-align:center'>Welcome !</h2>"
form = """
    <html>
    <body =<p style='color:rgb(145,0,0);background-color:pink'>Please enter your birth month.</p>
        <form method="post" style ='background-color:pink'>
            <label style='color:rgb(145,0,0);background-color:pink'>Month<input type="text" name="month" style='color:black'></label><br><br>
            <input type="submit" value="Enter a month" style='background-color:rgb(255,200,14)'>
        </form><br><br>
    </body>
    </html>
    """
months = ['January','February','March','April','May','June','July',
        'August','September','October','November','December']
month_abbvs=dict((m[:3].lower(),m) for m in months)
def valid_month(month):
    if month:
        short_month = month[:3].lower()
        return month_abbvs.get(short_month)
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(header + form )
    def post(self):
        user_month = valid_month(self.request.get("month"))
        errormessage="<albel style='color:rgb(145,0,0);width:200px'><h2>You have entered invalid data</h2></label><br>"
        if not (user_month):
            self.response.write(errormessage+form)
        else:
            outhead ="<h2 style='color:red;background-color:rgb(255,200,14)'>Thanks for a valid month ! </h2><br>"
            outbody=" <body style='background-color:rgb(234,134,10)'>Have a great day!</body>"
            self.response.write(outhead+outbody)
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)





#+===========++++++++++++++======
# import webapp2
# form="""
# <form method="post">
# 	What is your birthday?<br>
# 	<label>Month <input type="text" name="month" ></label> <br><br>
# 	<label>Day <input type="text" name="day"></label><br><br>
#     <label>Year <input type="text" name="year"></label><br><br>
#     <div style="color:red">%(error)s</div>
#   	<br><br>
#     <input type="submit">
# </form>
# """
# months = ['January','February','March','April','May','June','July',
#         'August','September','October','November','December']
# month_abbvs=dict((m[:3].lower(),m) for m in months)
# def valid_month(month):
#     if month :
#         short_month = month[:3].lower()
#         return month_abbvs.get(short_month)
# def valid_day(day):
#     if day and day.isdigit():
#         day = int(day)
#         if (0<day<=31):
#             return day
# def valid_year(year):
#     if year and year.isdigit():
#         year=int(year)
#         if (1900<year<2020):
#             return year
# class MainPage(webapp2.RequestHandler):
#     def write_form(self,error=""):
#         self.response.write(form % {"error":error})
#
#     def get(self):
#         self.write_form()
#     def post(self):
#          user_month = valid_month(self.request.get('month'))
#          user_day = valid_day(self.request.get('day'))
#          user_year = valid_year(self.request.get('year'))
#          if not(user_month and user_day and user_year):
#              self.write_form("Error")
#          else:
#               self.response.out.write("Thanks for  another valid day !""<br>")
# # #        self.response.write("The month you've entered is : ")
# app = webapp2.WSGIApplication([
# 	('/',MainPage)
# 	], debug=True)
