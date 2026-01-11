import json
import os

from buergerregister.models import Person
from buergerregister.register import Buergerregister
from buergerregister.validation import validiere_person


class JsonPersistence:
    @staticmethod
    def save(register: Buergerregister, filename: str) -> None:
        data = []
        for person in register.list():
            data.append(
                {
                    "vorname": person.vorname,
                    "nachname": person.nachname,
                    "geburtsjahr": person.geburtsjahr,
                    "wohnort": person.wohnort,
                }
            )

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @staticmethod
    def load(filename: str) -> Buergerregister:
        register = Buergerregister()

        if not os.path.exists(filename):
            return register

        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    return register
                data = json.loads(content)
        except (json.JSONDecodeError, OSError):
            return register

        if not isinstance(data, list):
            return register

        for entry in data:
            try:
                validiere_person(entry)
                person = Person(
                    entry["vorname"],
                    entry["nachname"],
                    entry["geburtsjahr"],
                    entry["wohnort"],
                )
                register.add(person)
            except Exception:
                continue

        return register
