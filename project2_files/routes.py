# render_template will launch HTML pages
# everytime the user selects a route (or path) a separate function will be called
# that function generates the HTML. This occurs in the url (probably as a GET request)
# when you redirect the user for a certain page, that function for the specific
# URL will be called it will render a certain template
from project2_files import app, forms
from flask import request, render_template, redirect, url_for
print("in routes.py first statement")
import re



# home page, or root
@app.route('/', methods=["GET", "POST"])
def welcomePage():
    print("in routes.py inside def welcomePage():")
    #return "Welcome to the home page"
    # can change this around if you want but its a variable that will
    # grab from our forms.py script the class NewsForm(which uses a super
    # class request.form that does some heavy lifting for us)
    my_form = forms.WelcomeAndRequest(request.form)

    # if the user DID submit the form, he'll be sending a http POST request
    if request.method == "POST":

        #my_form = forms.DisplayResults(request.form)
        # 1- get the values provided by the user,
        # (this is the moment you capture these values)
        # 2- Call the API
        # 3- Generate the requested data
        provided_search_terms = request.form["search_terms"]
        #print("variable search_terms" + " '" + provided_search_terms + "'")

        # removing any non alpha numeric
        only_alphaNum = re.sub(r'\W+', ' ', provided_search_terms)

        # remove any leading or trailing whitespace characters
        tokenized_words = only_alphaNum.split()
        print("tokenized_words:" ,tokenized_words)
        nyt_meaningful_data = forms.generate_data_from_api(tokenized_words)
        return render_template('results.html',
                               nyt_requested_data=nyt_meaningful_data,
                               tokenized_words=tokenized_words)

        #return '<h1>Good request? Maybe?</h1>'
        # return template with the results
        #return render_template('results.html'),

    # page user will see when they first visit, did not submit form yet
    # inside the html page, we will use variable "form" as shown below
    # to present the various input areas to user
    return render_template('welcome_and_request.html', form = my_form)


# first time user visits this view function/page they will have not submitted the form
# therefore the if statement will fail and local variable name will still be set to None
# the page that is rendered will be empty, the welcome string will say
# "Hello Stranger, WELCOME TO INDEX
# After the user submits the form, the server will receive a POST request with the data
# the if statement will succeed and
# the local variable 'name' will be populated with the data attribute that is part
# of the form field name. Then next statement will clear the field inside of the form
# The render_template() call will render the template like on the first visit
# but this time with the name variable containing the value given by the user
# on the first visit. We use this to display it in the header of the page
@app.route('/submit', methods=["GET", "POST"])
def showResults():
    # inside of this function you would call the forms.generate_data_from_api func to then show on
    # the results.html page
    print("inside of showResults:")
    name = None
    form = forms.TestForm(request.form)
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        print("name is:", name)
        #return redirect(url_for('welcomePage'))
    return render_template('results.html', form=form, name=name)