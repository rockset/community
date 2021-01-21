
// "use strict";
//import rockset from '@rockset/client';

// Before running this script, be sure to create an integration on the Rockset Console
// with DynamoDB. Once an integration is created, this script will work.

const API_KEY = "Your api key";
const COLLECTION_NAME = "Your Collection name";

const rockset = require("@rockset/client").default(
  API_KEY,
  "https://api.rs2.usw2.rockset.com"
);

const sleep = (ms) => {
  return new Promise((resolve) => setTimeout(resolve, ms));
};

// write collection
rockset.collections.createCollection("commons", {
      name: COLLECTION_NAME,
      field_mappings: [],
      sources: [
        {
          dynamodb: {
            table_name: "Your table name",
          },
          integration_name:"Your integration name that you created on the rockset console"
        },
      ],
    }).then(console.log).catch(console.error)


// write queries / test queries
  rockset.queries
    .query({
      sql: {
        query: `SELECT * FROM commons.${COLLECTION_NAME}`,
      },
    })
    .then(console.log)
    .catch(console.error);


// Create a Query Lambda with your query
rockset.queryLambdas
  .createQueryLambda('commons' /* name of workspace */, {
    name: 'MyFirstQueryLambdaJSAPP' /* name of Query Lambda */,
    description: 'A Query Lambda' /* (optional) description */,
    sql: {
      query: `SELECT * FROM commons.${COLLECTION_NAME}`,
      /* (optional) list of default parameters that may be used in the query */
      // default_parameters: [{ name: 'minimum_age', type: 'int', value: '40' }],
    },
  })
  .then(console.log)
  .catch(console.error);


// Run a Query Lambda by tag
rockset.queryLambdas
  .executeQueryLambdaByTag('commons', 'MyFirstQueryLambda', 'latest', {
    /* (optional) list of parameters that may be used in the query, that overwrite default parameters */
  //  parameters: [{ name: 'minimum_age', type: 'int', value: '20' }],
  })
  .then(console.log)
  .catch(console.error);

// Notes:
// update package.json for  "type":"commonjs",
