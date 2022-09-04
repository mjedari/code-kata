from collections import OrderedDict
from datetime import timedelta, datetime
from itertools import tee


def is_consecutive_days(day1, day2):
    difference = abs(datetime.fromisoformat(
        day1) - datetime.fromisoformat(day2))
    return difference == timedelta(days=1)


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def get_result(dataset):
    country_map = dict()
    for partner in dataset["partners"]:
        if not country_map.get(partner["country"]):
            country_map[partner["country"]] = dict()

        for date in partner["availableDates"]:
            if country_map[partner["country"]].get(date):
                country_map[partner["country"]][date].append(partner["email"])
            else:
                country_map[partner["country"]][date] = [partner["email"]]

    countries = []
    for country, dates in country_map.items():
        sorted_dates = OrderedDict(sorted(dates.items()))

        emails = []
        start_date = ""
        for (date1, emails1), (date2, emails2) in pairwise(sorted_dates.items()):
            if is_consecutive_days(date1, date2):
                emails_intersection = set(emails1) & set(emails2)
                if len(emails_intersection) > len(emails):
                    emails = list(emails_intersection)
                    start_date = date1

        countries.append({
            "attendeeCount": len(emails),
            "attendees": emails,
            "name": country,
            "startDate": start_date
        })

    return {"countries": countries}


dataset = {
    "partners": [
        {
            "firstName": "Darin",
            "lastName": "Daignault",
            "email": "ddaignault@hubspotpartners.com",
            "country": "United States",
            "availableDates": ["2017-05-03", "2017-05-06"]
        },
        {
            "firstName": "Crystal",
            "lastName": "Brenna",
            "email": "cbrenna@hubspotpartners.com",
            "country": "Ireland",
            "availableDates": ["2017-04-27", "2017-04-29", "2017-04-30"]
        },
        {
            "firstName": "Janyce",
            "lastName": "Gustison",
            "email": "jgustison@hubspotpartners.com",
            "country": "Spain",
            "availableDates": ["2017-04-29", "2017-04-30", "2017-05-01"]
        },
        {
            "firstName": "Tifany",
            "lastName": "Mozie",
            "email": "tmozie@hubspotpartners.com",
            "country": "Spain",
            "availableDates": ["2017-04-28", "2017-04-29", "2017-05-01", "2017-05-04"]
        },
        {
            "firstName": "Temple",
            "lastName": "Affelt",
            "email": "taffelt@hubspotpartners.com",
            "country": "Spain",
            "availableDates": ["2017-04-28", "2017-04-29", "2017-05-02", "2017-05-04"]
        },
        {
            "firstName": "Robyn",
            "lastName": "Yarwood",
            "email": "ryarwood@hubspotpartners.com",
            "country": "Spain",
            "availableDates": ["2017-04-29", "2017-04-30", "2017-05-02", "2017-05-03"]
        },
        {
            "firstName": "Shirlene",
            "lastName": "Filipponi",
            "email": "sfilipponi@hubspotpartners.com",
            "country": "Spain",
            "availableDates": ["2017-04-30", "2017-05-01"]
        },
        {
            "firstName": "Oliver",
            "lastName": "Majica",
            "email": "omajica@hubspotpartners.com",
            "country": "Spain",
            "availableDates": ["2017-04-28", "2017-04-29", "2017-05-01", "2017-05-03"]
        },
        {
            "firstName": "Wilber",
            "lastName": "Zartman",
            "email": "wzartman@hubspotpartners.com",
            "country": "Spain",
            "availableDates": ["2017-04-29", "2017-04-30", "2017-05-02", "2017-05-03"]
        },
        {
            "firstName": "Eugena",
            "lastName": "Auther",
            "email": "eauther@hubspotpartners.com",
            "country": "United States",
            "availableDates": ["2017-05-04", "2017-05-09"]
        }
    ]
}


def main():
    result = get_result(dataset)
    print(result)


if __name__ == "__main__":
    main()
