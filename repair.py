import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

schema = avro.schema.parse(open("/path/to/schema.json").read())

writer = DataFileWriter(open("repaired.avro", "w"), DatumWriter(), schema)

reader = DataFileReader(open("broken.avro", "r"), DatumReader())
for row in reader:
    writer.append(row)
reader.close()
writer.close()
