
#2017Jan31 rough play of user sign up
import webapp2
import cgi
# def getwarn():
#     if goodusername:
#         return textarea_label + textarea
#     else:
#         warned = "warning appears here."
#         return textarea_label+textarea+warned

# def display_Userwarned(warning):
#     textarea_label = "<label style='display:in-line block;width:150px'>Username</label>"
#     textarea = "<textarea name ='userip'>" +textarea_content +"</textarea>"
#     warn = "<textarea style='color:red' name ='userwarning'>" + warning +"</textarea>"
#     gooduser = valid_info("user")
#     return text_label + textarea + warn
warning=" "
def valid_info(ipgiven):
   return True
def display_Username(fieldname):
    textarea_label = "<label style='display:in-line block;width:150px'>"+fieldname+" </label>"
    if fieldname == "Username" :
        textarea = "<input type='text' name ='ipgiven'/>"
        goodusername = valid_info('ipgiven')
        if goodusername:
            validuser='ipgiven'
            return textarea_label + textarea
        else:
            warned = "warning appears here."
            return textarea_label+textarea+warned
    elif fieldname == "Password" :
        textarea = "<input type='text' name ='ipgiven'/>"
        goodpassword = valid_info("ipgiven")
        if goodpassword:
            pwd='ipgiven'
            return textarea_label + textarea
        else:
            warned = "warning appears here."
            return textarea_label+textarea+warned
def build_signup(bighead):
#    user_line = display_Username("",warning)
    body = "<body style='background-color:white'>.<br><br></body>"
    submit = "<input type='submit' value='Submit Query'/>"
#    if bighead == "header":
    form = ("<form style='color=pink' method='post'>" +
           display_Username("Username")+"<br><br>"+submit+
          "</form>")
    # elif (bighead == "correctinfoheader" ):
    #     form = ("<form style='color=pink' method='post'>" +
    #         display_Username("Username")+"<br><br>"+submit+
    #         "</form>")
    # elif (bighead == "errorinfoheader"):
    #     form = ("<form style='color=pink' method='post'>" +
    #         display_Username("Username")+"<br><br>"+submit+
    #         "</form>")
    return body + form
class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h2 style='font-family: 'Times New Roman';color:black' > Signup</h2>"
        content = build_signup("header")
        self.response.out.write(header + content)
    def post(self):
        user = self.request.get("ipgiven")
        correctinfoheader = "<h1 style='font-family: 'Times New Roman';color:black' > Welcome, "   +user +"! </h1>"
        content= build_signup("correctinfoheader ")
        self.response.out.write(correctinfoheader+content)
app = webapp2.WSGIApplication([
    ('/', MainHandler)
    ], debug=True)
