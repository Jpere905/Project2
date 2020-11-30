from project2_files import mainfunctions
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import requests

#print("in forms.py first statement")

# inherting the super class FlaskForm
class WelcomeAndRequest(FlaskForm):
    search_terms = StringField("Search Terms", validators=[DataRequired(), Length(min=3)])
    submit_form = SubmitField("Submit")

def generate_data_from_api(search_words):
    first_pass = True
    words_with_plus = ""
    # for each item in the string except for the first, append a '+' behind it and add it to
    # the bigger string that will contain each search term
    for word in search_words:
        if first_pass:
            words_with_plus += word
            first_pass = False
        else:
            words_with_plus += "+" + word

    # print("words with plus '" + words_with_plus + "'")

    # getting my api key
    my_key_dict = mainfunctions.read_from_file("project2_files/JSON_Documents/api_keys.json")
    my_key_string = my_key_dict["key"]

    # building the string to request articles
    article_beginning = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q='
    article_end = "&fq=source:(\"The New York Times\")&page=2&sort=newest&api-key=" + my_key_string
    article_request_string = article_beginning + words_with_plus + article_end
    # print ("finished request string " + finished_request_string)

    # saving the article responses into a json file
    request_from_api = requests.get(article_request_string).json()
    mainfunctions.write_to_file(request_from_api, "project2_files/JSON_Documents/article_response.json")
    data_dict = mainfunctions.read_from_file("project2_files/JSON_Documents/article_response.json")

    # filter our requests, and save it as a list of dictionaries
    list_of_nyt_items =[]
    for i in range (5):
        # get comment, save it, and place it into a variable
        url = data_dict["response"]["docs"][i]["web_url"]
        comment_reply = getComments(url, my_key_string)

        list_of_nyt_items.append({
            "url"       : url,
            "lead_para" : data_dict["response"]["docs"][i]["lead_paragraph"],
            "headline"  : data_dict["response"]["docs"][i]["headline"]["main"],
            "comment"   : comment_reply
        })



    # now to filter data for what we want
    # creating empty lists of urls and leading paragraphs
    # nyt_urls        = []
    # nyt_lead_para   = []
    # nyt_headlines   = []
    #
    # for i in range(0, 5):
    #     nyt_urls.append(data_dict["response"]["docs"][i]["web_url"])
    #     nyt_lead_para.append(data_dict["response"]["docs"][i]["lead_paragraph"])
    #     nyt_headlines.append(data_dict["response"]["docs"][i]["headline"]["main"])
    #
    # now for the comments, use the items inside the nyt_urls list

    # nyt_comments = []
    # for url in nyt_urls:
    #     comments_request_string = comments_beginning + '&url=' + url + '&sort=reader'
    #     nyt_comments.append(comments_request_string)


    #print("items in nyt_lead_para:", nyt_lead_para[0:])
    #print("items in nyt_headines:", nyt_headlines[0:])
    #print("items in nyt_urls:", nyt_urls[0:])

    # return the meaningful data as a list
    # return [nyt_urls, nyt_lead_para, nyt_headlines]
    return list_of_nyt_items

class TestForm(FlaskForm):
    name = StringField("Your name:", validators=[DataRequired()])
    submit_name_form = SubmitField("Submit name")


def getComments(url, my_key_string):

    comments_beginning = 'https://api.nytimes.com/svc/community/v3/user-content/url.json?api-key=' + my_key_string
    comment_json_request = comments_beginning + '&url=' + url + '&sort=reader'

    request_from_api = requests.get(comment_json_request).json()
    mainfunctions.write_to_file(request_from_api, "project2_files/JSON_Documents/comment_response.json")
    comment_dict = mainfunctions.read_from_file("project2_files/JSON_Documents/comment_response.json")

    try:
        comment = comment_dict["results"]["comments"][0]["commentBody"]
    except IndexError:
        comment = "Comments were not enabled for this article"

    return comment
