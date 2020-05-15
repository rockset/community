"use strict";

const API_KEY = "YOUR API KEY";
const COLLECTION_NAME = "myCollectionTest40";

const rockset = require("rockset").default(
  API_KEY,
  "https://api.rs2.usw2.rockset.com"
);

const sleep = (ms) => {
  return new Promise((resolve) => setTimeout(resolve, ms));
};

const setup = async () => {
  console.log(`Creating collection: ${COLLECTION_NAME}`);
  try {
    await rockset.collections.createCollection("commons", {
      name: COLLECTION_NAME,
      field_mappings: [],
      sources: [
        {
          s3: {
            bucket: "rockset-public-datasets",
            pattern: "partial-cities/*.json",
          },
          integration_name: null,
          format_params: {
            csv: null,
            json: true,
            xml: null,
          },
        },
      ],
    });

    await sleep(1000 * 50);
    console.log(`Collection creation complete.`);
  } catch (e) {
    console.log(await e.json());
  }
};

const tearDown = async () => {
  try {
    console.log(`Deleting collection: ${COLLECTION_NAME}`);
    await rockset.collections.deleteCollection("commons", COLLECTION_NAME);
   // await sleep(1000 * 10);

    do {
      console.log("do")
      console.log(e.status)
      await sleep(1000 * 10);
    }
    while (e.status && e.status !== 204);


    console.log(`Deleted collection: ${COLLECTION_NAME}`)

  } catch (e) {
    // silently fail if there is no collection to delete for convenience
    if (e.status && e.status === 404) {
      console.log(`Collection did not exist.`);
      return

    } else {
      console.log(e)
      return;
    }

    console.log("error")
    //console.log(await e.json());
  }
};

const add = async (data = []) => {
  console.log(`Inserting data...`);
  const f = await rockset.documents.addDocuments("commons", COLLECTION_NAME, {
    data: data,
  });

  await sleep(1000 * 10);
  console.log(`Insert complete`);
};

const get = async (query) => {
  console.log(`Getting data...`);

  const out = await rockset.queries.query({
    sql: {
      query,
    },
  });
  return out;
};

(async () => {
  try {
    await tearDown();

    await setup();

    await sleep(1000 * 10);

    const out = await get(
      `SELECT count(*) as recordCount FROM commons.${COLLECTION_NAME};`
    );

    console.log(out.results[0].recordCount);
    console.log(`Complete.`);
  } catch (e) {
    console.log(await e.json());
  }
})();
