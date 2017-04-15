
from string import Template

def start_response(resp="text/html"):
    return('Content-type: ' + resp + '\n\n')

def include_header(the_title):
    with open('../templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))

def include_footer(the_links):
    with open('./templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))

def start_form(the_url, form_type="POST"):
    return('<form action="' + the_url + '" method="' + form_type + '">')

def end_form(submit_msg="Submit"):
    return('<p></p><input type=submit value="' + submit_msg + '"></form>')

def radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_value + '"> ' + rb_value + '<br />')

def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)

def header(header_text, header_level=2):
    return('<h' + str(header_level) + '>' + header_text +
           '</h' + str(header_level) + '>')

def para(para_text):
    return('<p>' + para_text + '</p>') 


print (start_response())
print (start_response("text/plain"))
print (start_response("application/jason"))

print (include_header("Welcome to my home on the web!"))
print ('********************************************************')

print (include_footer({'Home': '/index.html', 'Selct': '/cgi-bin/select.py'}))

print ('********************************************************')
print (start_form("/cgi-bin/process-athlete.py"))

print ('********************************************************')
print (end_form())

print ('********************************************************')
print (end_form("Click to Confirm Your Order"))

print ('********************************************************')
for fab in ['John','Paul','George','Ringo']:
    print (radio_button(fab, fab))

print ('********************************************************')
print (u_list(['Life of Brian', 'Holy Grail']))

print ('********************************************************')
print (header("Welcome to my home on the web!"))
print (header("This is a sub-sub-sub-sub heading",5))

print ('********************************************************')
print (para("Was it worth the wait? We hope it was..."))













