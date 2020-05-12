# Rockset-Mongo Integration Sample App
Rockset has  a built-in data source connector to [Mongo DB]([https://www.mongodb.com/](https://www.mongodb.com/)).  By using Rockset on top of Mongo DB, you can build APIs to the SQL you write, have millisecond query latency, and seconds in data latency. To get a quick overview of what this integration looks like, check out this [YouTube video]([https://www.youtube.com/watch?v=eivdshBA-6g&t=1s](https://www.youtube.com/watch?v=eivdshBA-6g&t=1s)).

Here's a sample diagram of how the Rockset-MongoDB integration looks like:
![Rockset-MongoDB Diagram](mongo_horizontal_bgcolor_2x.png)

## Project Organization
This project consists of a few files:
- `script.py`: This file contains the main logic of making API calls to ClimaCell, Rockset, and MongoDB.
- `settings.py`: This file gets our environment variables for the `.env` file.
- `.env`: This is NOT SHOWN. Create this file and add your env variables.
- `mongo_config.py`: Import the Mongo database and collections.

## Run the project

1.  Create a `.env` file in the main project folder and add:
      - `ROCKSET_API_KEY='YOUR KEY'`
      - `MONGO_URI='YOUR STRING'`
      - `CLIMACELL_API_KEY='YOUR KEY'`
2. Create your virtualenv and  `$ pip install -r requirements.txt`
3. Substitute the API calls in `script.py` with your:
    - Paths-- i.e. Rockset Query Lambda calls
4. Make sure your databases and collections are set up on Mongo DB.
5. Run `$ python script.py`


## Resources

- For questions about the tutorial or the challenges find us on [slack](https://bit.ly/rockset-channel) on  **#support** channel or **#mongo**.
- Follow us on Twitter: [Rockset]([https://twitter.com/RocksetCloud](https://twitter.com/RocksetCloud)).
- Check out our [YouTube channel]([https://www.youtube.com/channel/UCy4qLzJ7yuEmsIN2Mm5Pn-w](https://www.youtube.com/channel/UCy4qLzJ7yuEmsIN2Mm5Pn-w)) for tutorials.  We'll be making one for this integration, so stay tuned!
