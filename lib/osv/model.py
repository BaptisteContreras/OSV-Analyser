from typing import Union


class Query:
    def __init__(self, version: Union[None, str], commit: Union[None, str], name: str, ecosystem: str, purl: str):
        self.version = version
        self.commit = commit
        self.name = name
        self.ecosystem = ecosystem
        self.purl = purl

    @staticmethod
    def buildWithVersion(version: str, name: str, ecosystem: str, purl = "") -> __init__:
        return Query(version, None, name, ecosystem, purl)

    @staticmethod
    def buildWithCommit(commit: str, name: str, ecosystem: str, purl="") -> __init__:
        return Query(None, commit, name, ecosystem, purl)

    def to_json(self) -> dict:
        res = {
            "package" : {
                "name" : self.name,
                "ecosystem" : self.ecosystem
            }
        }

        if self.version:
            res["version"] = self.version
        else:
            res["commit"] = self.commit

        if self.purl:
            res["package"]["purl"] = self.purl

        return res