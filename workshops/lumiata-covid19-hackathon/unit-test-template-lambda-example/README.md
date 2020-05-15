## Rockset Node.js Example

A simple example that performs the following operations:

* creates a new collection
* connect to S3 so Rockset can have read-access to continuously ingest data in real-time
* create a Query Lambda
* execute a Query Lambda

## Running

* Make sure you have Node.js installed.
* Install dependencies: `npm install`
* Edit the `lambdaIntegration.js` script and add your Rockset API key
* Run script: `lambdaIntegration.js`
