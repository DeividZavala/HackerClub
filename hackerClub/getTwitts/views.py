import csv

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index():
    import twitter

    api = twitter.Api(consumer_key='CWzj0wObKkKB2MB7px5Kd7Oaq',
                      consumer_secret='RsqOLiazWIOjtShZS46pHD14xI0V4OzmAnvcfUAq4loRMrPnJD',
                      access_token_key='48614527-N0V8ArqBdMWWnFpWeBG7tsp3aUk22ZxxkAqKxclUq',
                      access_token_secret='nuOolGsVC9vlcvwdWw4PbAA8OnmH6NKopO3z1GnuMd8rI')

    results = api.GetSearch(
        raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=100")

    return "Hola Mundo"

def get_file(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response