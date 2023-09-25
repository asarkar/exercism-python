from __future__ import annotations

import json
from typing import Any, Optional


class User:
    def __init__(
        self,
        name: str,
        owes: Optional[dict[str, float]] = None,
        owed_by: Optional[dict[str, float]] = None,
        balance: float = 0.0,
    ) -> None:
        self.name = name
        self.owes = owes or {}
        self.owed_by = owed_by or {}
        self.balance = balance

    @staticmethod
    def from_json(json_str: str) -> User:
        json_dict = json.loads(json_str)
        return User(**json_dict)

    def __str__(self) -> str:
        return json.dumps(vars(self))


class RestAPI:
    def __init__(self, database: dict[str, list[dict[str, Any]]]) -> None:
        self._database: dict[str, User] = {}
        for u in database["users"]:
            user = User(**u)
            self._database[user.name] = user

    def get(self, url: str, payload: Optional[str] = None) -> str:
        if url != "/users":
            raise NotImplementedError
        if payload is None:
            names = sorted(self._database)
        else:
            names = sorted(json.loads(payload)["users"])

        users = [vars(self._database[name]) for name in names]
        return json.dumps({"users": users})

    def post(self, url: str, payload: str) -> str:
        match url:
            case "/add":
                return self._add(payload)
            case "/iou":
                return self._iou(payload)
            case _:
                raise NotImplementedError

    def _add(self, payload: str) -> str:
        name = json.loads(payload)["user"]
        user = User(name)
        self._database[name] = user
        return str(user)

    def _iou(self, payload: str) -> str:
        json_dict = json.loads(payload)
        lender = self._database[json_dict["lender"]]
        borrower = self._database[json_dict["borrower"]]
        amount = json_dict["amount"]

        lender.balance += amount
        borrower.balance -= amount
        amount += lender.owed_by.get(borrower.name, 0.0) - lender.owes.get(borrower.name, 0.0)
        if amount > 0:
            lender.owed_by[borrower.name] = amount
            borrower.owes[lender.name] = amount
        elif amount < 0:
            borrower.owed_by[lender.name] = -amount
            lender.owes[borrower.name] = -amount
        if amount >= 0:
            if lender.name in borrower.owed_by:
                del borrower.owed_by[lender.name]
            if borrower.name in lender.owes:
                del lender.owes[borrower.name]
        if amount <= 0:
            if borrower.name in lender.owed_by:
                del lender.owed_by[borrower.name]
            if lender.name in borrower.owes:
                del borrower.owes[lender.name]

        return self.get("/users", json.dumps({"users": [lender.name, borrower.name]}))
