



import webapp2
a ="<br>"
b="Hannah"
c="<br>"
months = ['January','February','March','April','May','June','July',
        'August','September','October','November','December']
def mymonths():
    r=0
    for i in (range(len(months))):
        year= (str(i)+":-- "+months[i])
        r=+1
        print(year)
    return year
month_abbvs=dict((m[:3].lower(),m) for m in months)
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Test my dictionary""<br>")
        self.response.write(a+b+c)
        r=0
        for i in (range(len(months))):
            year= (str(i+1)+":-- "+months[i])
            r=+1
            self.response.write(str(year)+"<br>")
        self.response.write(b[:3]+"<br>")
        self.response.write(b[:3].lower()+"<br>")
        self.response.write(month_abbvs)
        self.response.write("<br>""All done !"+"<br>")
    def post(self):
        self.response.out.write("Thanks for a valid day !""<br>")
        self.response.write("The month you've entered is : ")
        self.response.out.write(valid_month("jan"))

app = webapp2.WSGIApplication([
	('/',MainPage)
	], debug=True)
