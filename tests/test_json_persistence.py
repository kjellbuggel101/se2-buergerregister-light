import os
import tempfile

from buergerregister.json_persistence import JsonPersistence
from buergerregister.models import Person
from buergerregister.register import Buergerregister


def test_save_and_load_roundtrip():
    register = Buergerregister()
    register.add(Person("Anna", "Schmidt", 1990, "Bremen"))

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        filename = tmp.name

    JsonPersistence.save(register, filename)
    loaded = JsonPersistence.load(filename)

    assert len(loaded.list()) == 1
    assert loaded.list()[0].nachname == "Schmidt"

    os.remove(filename)


def test_load_non_existing_file_returns_empty_register():
    register = JsonPersistence.load("does_not_exist.json")
    assert len(register.list()) == 0


def test_save_and_load_empty_register():
    register = Buergerregister()

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        filename = tmp.name

    JsonPersistence.save(register, filename)
    loaded = JsonPersistence.load(filename)

    assert len(loaded.list()) == 0
    os.remove(filename)


def test_load_skips_invalid_entries():
    with tempfile.NamedTemporaryFile(delete=False, mode="w") as tmp:
        tmp.write('[{"vorname": "Max"}]')
        filename = tmp.name

    loaded = JsonPersistence.load(filename)
    assert len(loaded.list()) == 0
    os.remove(filename)


def test_load_multiple_persons_same_lastname():
    register = Buergerregister()
    register.add(Person("Anna", "Meier", 1990, "Bremen"))
    register.add(Person("Tom", "Meier", 1985, "Hamburg"))

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        filename = tmp.name

    JsonPersistence.save(register, filename)
    loaded = JsonPersistence.load(filename)

    assert len(loaded.list()) == 2
    os.remove(filename)
