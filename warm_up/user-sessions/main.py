import json
from collections import defaultdict
from typing import TypedDict


class Event(TypedDict):
    url: str
    visitorId: str
    timestamp: int


class Input(TypedDict):
    events: list[Event]


class Session(TypedDict):
    duration: int
    pages: list[str]
    startTime: int


class Output(TypedDict):
    sessionsByUser: list[Session]


Timestamp = int
Url = str
Visit = tuple[Timestamp, Url]
VisitorId = str
VisitorEventMap = dict[VisitorId, list[Visit]]


class UserSession:
    SESSION_IN_MS = 600_000

    def __init__(self, input_data: Input) -> None:
        self.data = input_data

    def generate(self) -> Output:
        visitor_events_map = self.map_visitor_to_events()

        return self.split_visitor_events_to_sessions(visitor_events_map)

    def map_visitor_to_events(self) -> VisitorEventMap:
        visitor_events_map = defaultdict(list)
        for event in input['events']:
            visitor_events_map[event['visitorId']].append(
                (event['timestamp'], event['url']))

        return visitor_events_map

    def split_visitor_events_to_sessions(self, visitor_event_map: VisitorEventMap) -> Output:
        output = {}
        for visitorId, visits in visitor_event_map.items():
            self.split_visit_to_sessions(visits)
            output[visitorId] = self.split_visit_to_sessions(visits)
        return {'sessionsByUser': output}

    def split_visit_to_sessions(self, visits: list[Visit]) -> list[Session]:
        sessions: list[Session] = []
        visits.sort()  # Sort visits by timestamp
        startTime, url = visits[0]
        endTime, pages = startTime, [url]

        for timestamp, url in visits[1:]:
            # visit belongs to the same session
            if timestamp <= startTime + UserSession.SESSION_IN_MS:
                pages.append(url)
                endTime = timestamp
            # start a new session
            else:
                sessions.append(
                    Session(duration=endTime - startTime,
                            pages=pages, startTime=startTime)
                )

                pages = [url]
                startTime = endTime = timestamp
        if pages:
            sessions.append(
                Session(duration=endTime - startTime,
                        pages=pages, startTime=startTime)
            )

        return sessions


input: Input = {
    "events": [{
        "url": "/pages/a-big-river",
        "visitorId": "d1177368-2310-11e8-9e2a-9b860a0d9039",
        "timestamp": 1512754583000
    },
        {
        "url": "/pages/a-small-dog",
        "visitorId": "d1177368-2310-11e8-9e2a-9b860a0d9039",
        "timestamp": 1512754631000
    },
        {
        "url": "/pages/a-big-talk",
        "visitorId": "f877b96c-9969-4abc-bbe2-54b17d030f8b",
        "timestamp": 1512709065294
    },
        {
        "url": "/pages/a-sad-story",
        "visitorId": "f877b96c-9969-4abc-bbe2-54b17d030f8b",
        "timestamp": 1512711000000
    },
        {
        "url": "/pages/a-big-river",
        "visitorId": "d1177368-2310-11e8-9e2a-9b860a0d9039",
        "timestamp": 1512754436000
    },
        {
        "url": "/pages/a-sad-story",
        "visitorId": "f877b96c-9969-4abc-bbe2-54b17d030f8b",
        "timestamp": 1512709024000
    }
    ]
}


print(json.dumps(UserSession(input).generate(), indent=2))


"""
Expected Output

output = {
    "sessionsByUser": {
        "d1177368-2310-11e8-9e2a-9b860a0d9039": [
            {
                "duration": 195000,
                "pages": [
                    "/pages/a-big-river",
                    "/pages/a-big-river",
                    "/pages/a-small-dog"
                ],
                "startTime": 1512754436000
            }
        ],
        "f877b96c-9969-4abc-bbe2-54b17d030f8b": [
            {
                "duration": 41294,
                "pages": [
                    "/pages/a-sad-story",
                    "/pages/a-big-talk"
                ],
                "startTime": 1512709024000
            },
            {
                "duration": 0,
                "pages": [
                    "/pages/a-sad-story"
                ],
                "startTime": 1512711000000
            }
        ]
    }
}
"""
