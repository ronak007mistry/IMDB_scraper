from dateutil.parser import parse
from scraper.models import Movie


def my_function(request):
    with open('finaldata.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Movie.objects.get_or_create(
                title=row[0],
                ratings=row[1],
                release_date=parse(row[3]),
                duration=row[2],
                description=row[4],
                )
            # creates a tuple of the new object or
            # current object and a boolean of if it was created

    return HttpResponse("All done")