#FIFTH VERSION BEFORE I STARTED UDACITY STYLE CODING
import webapp2
import cgi
#import buildup.py
# USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
# def valid_username(username):
#     return username and USER_RE.match(username)
def valid_username(Username):
    return True
def valid_password(Password):
    return  True
def valid_email(Email):
    return True
# PASS_RE = re.compile(r"^.{3,20}$")
# def valid_password(password):
#     return password and PASS_RE.match(password)
#
# EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[S]+$')
# def valid_email(email):
#     return not email or EMAIL_RE.match(email)
def display_user(Username):
    textarea_label="<label type='text' style='display:inline-block;width:150px;color:red'>" +Username+"</label>"
    textarea = "<input type='text' name='username'/>"
    return textarea_label + textarea
def display_pwd(Password):
    textarea_label="<label type='text' style='display:inline-block;width:150px;color:red'>" +Password+"</label>"
    textarea = "<input type='text' name='password'/>"
    return textarea_label + textarea
def display_vpwd(VerifyPassword):
    textarea_label="<label type='text' style='display:inline-block;width:150px;color:red'>" +VerifyPassword+"</label>"
    textarea = "<input type='text' name='Vpassword'/>"
    return textarea_label + textarea
def display_email(EmailOptional):
    textarea_label="<label type='text' style='display:inline-block;width:150px;color:red'>" +EmailOptional+"</label>"
    textarea = "<input type='text' name='email'/>"
    return textarea_label + textarea

warned = "    " + "This is not a valid email."
def display_fieldout(fieldname,warned):
    textarea_label="<label type='text' style='display:inline-block;width:150px;color:red'>" +fieldname+"</label>"
    textarea = "<input type='text' name='ipgiven'/>"
    warning = warned
    return textarea_label + textarea + warning
def build_signout():
    body = "<body style='background-color:white;'>Hi.</body>"
    submit = "<input type='submit' value='Submit Query'/>"
    form =("<form method='post'>"+
            display_fieldout("Username","")+"<br><br>"+
            display_fieldout("Password","")+"<br><br>"+
            display_fieldout("Verify Password","")+"<br><br>"+
            display_fieldout("Email Optional",warned)+"<br><br>"+
            submit+
            "</form>")
    return body + form
def build_signup():
    body = "<body style='background-color:white;'>Hi.</body>"
    submit = "<input type='submit' value='Submit Query'/>"
    form =("<form method='post'>"+
            display_user("Username")+"<br><br>"+
            display_pwd("Password")+"<br><br>"+
            display_vpwd("Verify Password")+"<br><br>"+
            display_email("Email Optional")+"<br><br>"+
            submit+
            "</form>")
    return body + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Signup</h1>"
        content = build_signup() #"g"
        self.response.out.write(header + content)
    def post(self):
        faulty_form = False
        user = "<label style='color:cyan'>" +self.request.get("username")+" </label>"
#        validuser = cgi. escaped(user)
        passw = "<label style='color:cyan'>" +self.request.get("password")+" </label>"
        VerifiedPassword = "<label style='color:cyan'>" +self.request.get("Vpassword")+" </label>"
        Email = "<label style='color:cyan'>" +self.request.get("email")+" </label>"
        correctheader = "<h1> Welcome, "+user+" ! </h1>"
        errorheader = "<h1>Please signup again, "+user+"." +passw +","+  self.request.get("password") +" ," + Email+ ", is not valid data.</h1>"
        inputinfo = dict(Username = user,Email="email")
        verify = passw
        if not valid_username("username"):
            inputinfo['error_username'] = "That's not a valid username."
            faulty_form = True
        if not valid_password("password"):
            inputinfo['error_password'] = "That's not a valid password."
            faulty_form = True
        elif VerifiedPassword !=verify:
            inputinfo['error_verify'] = "Your passwords didn't match."
            faulty_form = True
        if not valid_email("email"):
            inputinfo['error_email'] = "That's not a valid email."
            faulty_form = True
        if faulty_form:
            header = errorheader
        else:
            header = correctheader

        content = build_signout()
        self.response.out.write(header + content)

app = webapp2.WSGIApplication([
    ('/',MainHandler)
    ],debug=True)
