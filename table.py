import json


class Table(object):
    # pk = Primary key
    def __init__(self, file_name: str, column_names: list[str], pk: str):
        self.column_names = column_names
        self.pk = pk
        self.file_name = file_name

        with open(file_name) as f:
            data = f.read().strip()
            if data == "":
                self.table = dict()
            else:
                self.table: dict = json.loads(data)

    def save(self):
        with open(self.file_name, 'w') as f:
            f.write(json.dumps(self.table))

    def add(self, record):
        if type(record) != type(dict()):
            record = record.__dict__

        if record[self.pk] in self.table:
            return
        self.table[record[self.pk]] = record
        self.save()
        return record

    def update(self, record: dict):
        target = self.table[record[self.pk]]
        for k in record:
            if k in target:
                target[k] = record[k]
        self.save()

    def delete(self, pk: str):
        if pk in self.table:
            self.table.pop(pk)
        self.save()

    def rows(self):
        return self.table.values()

    def print(self):
        for row in self.rows():
            print(row)

    def find(self, column_name: str, value):
        if self.pk == column_name:
            return self.table.get(value, None)

        for row in self.rows():
            if row[column_name] == value:
                return row
