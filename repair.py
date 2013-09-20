import sys
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

if len(sys.argv) != 4:
    print "Usage: python repair.py /path/to/schema.json brokenfile.avro repairedfile.avro"
    sys.exit(0)
    
schemafile = sys.argv[1]
infile=sys.arv[2]
outfile=sys.argv[3]

schema = avro.schema.parse(open(schemafile).read())

writer = DataFileWriter(open(outfile, "w"), DatumWriter(), schema)

reader = DataFileReader(open(infile, "r"), DatumReader())
for row in reader:
    writer.append(row)
reader.close()
writer.close()
