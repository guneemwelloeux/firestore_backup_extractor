from protopy.basic_pb2 import Root, Header, Footer, DocumentPath, InnerPath, Field, Value, GeoPoint
import json

class Document:
    def __init__(self, collection, id):
        self.collection = collection
        self.id = id
        self.fields = {}

class GeoPoint:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"GeoPoint(latitude={self.latitude}, longitude={self.longitude})"

class Reference:
    def __init__(self, project, collection, id):
        self.project = project
        self.collection = collection
        self.id = id

    def __repr__(self):
        return f"Reference(project={self.project}, collection={self.collection}, id={self.id})"

class Timestamp:
    def __init__(self, seconds, nanoseconds):
        self.seconds = seconds
        self.nanoseconds = nanoseconds
    def __repr__(self):
        return f"Timestamp(seconds={self.seconds}, nanoseconds={self.nanoseconds})"

def main():
    with open("out_2.bin", "rb") as f:
        data = f.read()
    root = Root()
    root.ParseFromString(data)

    document = process_root(root)
    print(document.__dict__)

def process_root(root: Root) -> Document:
    document = Document(root.header.path.documentpath.collection, root.header.path.documentpath.document_id)
    for field in root.fields:
        f = parse_field(field)
        print(f)
        if field.array_indicator == 1:
            document.fields.setdefault(field.name, []).append(f)
        else:
            document.fields[field.name] = f
    return document

def parse_field(field: Field) -> any:
    print(field)
    print(field.value)
    print(field.value.boolean_value)
    if field.value.HasField("integer_value"):
        if field.type_indicator == 7:
            return Timestamp(field.value.integer_value//1000000, 1000*field.value.integer_value%1000000)
        return field.value.integer_value
    elif field.value.HasField("boolean_value"):
        print("BOOL", field.value.boolean_value)
        return field.value.boolean_value
    elif field.value.HasField("double_value"):
        return field.value.double_value
    elif field.value.HasField("geo_point_value"):
        return GeoPoint(field.value.geo_point_value.latitude, field.value.geo_point_value.longitude)
    elif field.value.HasField("reference_value"):
        return Reference(field.value.reference_value.project, field.value.reference_value.path.collection, field.value.reference_value.path.document_id)
    elif field.value.HasField("bytes_value"):
        if field.type_indicator == 19:
            map = Root()
            map.ParseFromString(field.value.bytes_value)
            doc = process_root(map)
            return doc.fields
        else:
            return field.value.bytes_value.decode("utf-8")
    else:
        print("UNK", field)

if __name__ == "__main__":
    main()
