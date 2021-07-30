from rockset import Client
from dotenv import load_dotenv
import os, time

load_dotenv()

#get rocksetapikey
ROCKSETAPIKEY = os.environ.get('ROCKSETAPIKEY')

# connect securely to Rockset production API servers
rs = Client(api_server='api.rs2.usw2.rockset.com', api_key=ROCKSETAPIKEY)

# write our field mappings
mappings = [
    rs.FieldMapping.mapping(
        name="twitchTransformation1",
        input_fields=[
            rs.FieldMapping.input_field(
                field_name="price",
                if_missing="SKIP",
                is_drop=True,
                param="price"
            )
        ],
        output_field=rs.FieldMapping.output_field(
            field_name="price", sql_expression="TRY_CAST(REGEXP_REPLACE(:price, '[^\d.]') as float)", on_error="FAIL"
        )
    ),

    rs.FieldMapping.mapping(
        name="twitchTransformation2",
        input_fields=[
            rs.FieldMapping.input_field(
                field_name="latitude",
                if_missing="SKIP",
                is_drop=True,
                param="latitude"
            )
        ],
        output_field=rs.FieldMapping.output_field(
            field_name="latitude", sql_expression="TRY_CAST(:latitude as float)", on_error="FAIL"
        )
    )
]

# create our collection
new_collection = rs.Collection.create("codeDemoFieldMappingsTwitch1", field_mappings=mappings)

# we're going to wait for the collection to be created [super hacky way v1.0]
print("Start : %s" % time.ctime())
time.sleep(30)
print("End : %s" % time.ctime())


docs = [
  {"id":"t1", "price": "$125.00 ",  "latitude": "37.78097",  "longitude": "-122.40305"},
]

# create sample doc that we'll write directly to the collection
results = rs.Collection.add_docs("codeDemoFieldMappingsTwitch1", docs)
print(results)

