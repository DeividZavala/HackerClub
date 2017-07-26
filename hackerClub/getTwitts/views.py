import csv

from django.http import HttpResponse
from django.shortcuts import render



def uff():
    import twitter

    api = twitter.Api(consumer_key='CWzj0wObKkKB2MB7px5Kd7Oaq',
                      consumer_secret='RsqOLiazWIOjtShZS46pHD14xI0V4OzmAnvcfUAq4loRMrPnJD',
                      access_token_key='48614527-N0V8ArqBdMWWnFpWeBG7tsp3aUk22ZxxkAqKxclUq',
                      access_token_secret='nuOolGsVC9vlcvwdWw4PbAA8OnmH6NKopO3z1GnuMd8rI')

    return api.GetUserTimeline(screen_name='braincaus', count=200)

def get_file(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    data = uff()

    writer = csv.writer(response)
    writer.writerow(["Texto", "Ubicacion", "hashtags", "retweets"])

    for x in data:
        try:
            print(x)
            writer.writerow([x.text, x.location, len(x.hashtags), x.retweet_count])
        except Exception as e:
            print ("Error de caracter")

    return response