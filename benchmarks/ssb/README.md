# SSB Benchmark

This subdirectory contains scripts to load the SSB 100SF dataset into Rockset and run the SSB queries against it.

# Create a Rockset Profile

Follow these instructions to download and install the Rockset CLI:
[Rockset CLI Download and Install Instructions](https://github.com/rockset/rockset-js/tree/master/packages/cli#download--installation-instructions).

Follow these instructions to set up a Rockset profile:
[Authentication and Profile Management](https://github.com/rockset/rockset-js/tree/master/packages/cli#authentication-and-profile-management-rockset-auth).

# Load

Select the Rockset profile you want to use in the CLI.
```
rockset auth:use NAME
```

Create collection `denormalized` in workspace `commons` sourced from the denormalized ssb dataset corresponding to scale factor 100.
```
./load.py -c denormalized --s3-bucket=rockset-public-datasets --s3-prefix=ssb-denormalized-100GB/ --schema schema.yml
```

> Note: You will need to have field partitioning enabled for your organization for this to work. If during creation you get an error that it is not, contact support so we can enable it for you.

# Query

Select the Rockset profile you want to use in the CLI.
```
rockset auth:use NAME
```

Run the queries
```
./query.py -d queries/optimal
```

