# Redash Development Setup
This docker-compose.yml sets up a local Redash instance along with its supporting services so you can quickly prototype creating a Redash dashboard off of data in Rockset.

## Setup
First install Docker by following the guides for

* [Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [Mac](https://docs.docker.com/docker-for-mac/install/)
* [Windows](https://docs.docker.com/docker-for-windows/install/)

Then install docker-compose by following this [guide](https://docs.docker.com/compose/install/).

Next, in your terminal run

    git clone git@github.com:rockset/community.git
    cd community/redash
    docker-compose up -d

Finally, open [http://localhost:5000](http://localhost:5000) to access the Redash dashboard (it may take up to 60s for everything to start up).

## Configuration

To configure your integration with Rockset:

1. Add Rockset as a Database source in Redash by pressing the settings icon on the upper right-hand corner then
    press `Data Sources > New Data Source` and select Rockset from the list.

2. Configure the source as follows:
    - Fill in a **Name** for the source
    - Fill in an **API Key** that you created in the [Rockset Console](https://console.rockset.com)
    - Fill in the URL for the **Rockset API Server** as `https://api.rs2.usw2.rockset.com`

You can test the connection and if everything seems fine, click `Save`.

## Usage

To create a new query, click `Create > New Query`. Select the Rockset Database added in the previous step.
    This will populate the various collections.
    Select the collection you want to run the query on and enter the SQL statement to execute.

You can now click on `New Visualization` to visualize and create dashboards over the query results.
    To further explore how to build visualizations, dashboards and alerts, refer to
    the [Redash Getting Started Guide](https://redash.io/help/user-guide/getting-started)

> **Note:** We recommend that you use Rockset's [interactive query editor](https://console.rockset.com/query) as the starting
    point to refine your queries and then copy-paste them into the Redash query page when you are done. Rockset's query
    editor supports more fully featured auto-complete, type hints, and more descriptive error messages to help you get
    to your desired end query faster and with fewer mistakes along the way

> **Note:** If you are running into strange behavior with your queries in Redash, one possible solution is to turn
    off caching on your browser (by default, the Cache-Control header Redash sends to the browser is very high).
    Here are some guides to disable browser-side caching for [Chrome](https://www.technipages.com/google-chrome-how-to-completely-disable-cache),
    [Safari](https://www.technipages.com/apple-safari-completely-disable-cache), and [Firefox](https://dzone.com/articles/how-turn-firefox-browser-cache).

## Related

For more information refer to the Rockset [Redash documentation](https://docs.rockset.com/redash)
