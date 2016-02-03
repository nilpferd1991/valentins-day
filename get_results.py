#!/usr/bin/python3.4

from git import Repo

repo = Repo(".")

tags = repo.tags

sorted_tags = sorted(tags, key=lambda tag: tag.commit.count())

newest_tag = sorted_tags[-1]

print(newest_tag)

