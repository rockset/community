# SSB Benchmark

This subdirectory contains scripts to load the SSB 100SF dataset into Rockset and run the SSB queries against it.

# Load

Make sure you have the Rockset python client version >= 0.7.54 installed.
```
pip3 install 'rockset>=0.7.54'
```

Select the Rockset profile you want to use in the cli.
```
rock configure select PROFILE
```

Create collection `denormalized` in workspace `commons` sourced from the denormalized ssb dataset corresponding to scale factor 100.
```
./load.py -c denormalized --s3-bucket=rockset-public-datasets --s3-prefix=ssb-denormalized-100GB/ --schema schema.yml
```

> Note: You will need to have field partitioning enabled for your organization for this to work. If during creation you get an error that it is not, contact support so we can enable it for you.

# Query

Select the Rockset profile you want to use in the cli.
```
rock configure select PROFILE
```

Run the queries
```
./query.py -d queries/optimal
```

