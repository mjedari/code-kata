"""
Example
Given a list of email objects(fromPerson, toPerson, message), find top K persons who received most number of emails. Follow-up question was to count only unique emails sent to a person and then find top K elements.
"""


from collections import defaultdict
from typing import List
from dataclasses import dataclass


@dataclass()
class Email:
    fromPerson: int
    toPerson: int
    message: str


def find_most_freq(emails: List[Email], k: int) -> List[int]:
    emails_to_freq_map = defaultdict(int)
    for email in emails:
        emails_to_freq_map[email.toPerson] += 1

    return sorted(emails_to_freq_map, key=lambda k: emails_to_freq_map[k], reverse=True)[:k]


def find_most_unique_freq(emails: List[Email], k: int) -> List[int]:
    emails_to_freq_map = defaultdict(set)
    for email in emails:
        emails_to_freq_map[email.toPerson].add(email.fromPerson)

    return sorted(emails_to_freq_map, key=lambda k: len(emails_to_freq_map[k]), reverse=True)[:k]


def test():
    emails: List[Email] = [
        Email(1, 2, "msg"),
        Email(1, 2, "msg"),
        Email(1, 2, "msg"),
        Email(2, 3, "msg"),
        Email(1, 3, "msg"),
        Email(2, 1, "msg"),

    ]

    assert find_most_freq(emails, 2) == [2, 3]
    assert find_most_freq(emails, 3) == [2, 3, 1]
    assert find_most_unique_freq(emails, 2) == [3, 2]


test()
