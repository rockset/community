# Datadog Openmetrics Configuration and Dashboard Example
Datadog provides an agent that will scrape metrics across various sources including an Openmetrics endpoint like the one provided by Rockset. You can configure this agent to scrape metrics from your Rockset metrics endpoint using the Openmetrics integration.
You can also import a sample dashboard that visualizes these metrics to get you started quickly.

## Dependencies
1. Datadog Agent version 6.6.0 and above
2. Enable Rockset metrics endpoint
3. Access to a Datadog account

## Instructions
Copy the [example](./openmetrics.d/conf.yaml) from this repository to your agent's host. The location of this configuration file on your agent host will generally be located at:
```
../datadog-agent/etc/conf.d/openmetrics.d
```

The syntax is very specific and please note any differences between your file and the example provided. For exampe, the password must be an empty string in order to be encoded properly.

You can import the sample dashboard into your Datadog account by following the instructions here: https://docs.datadoghq.com/dashboards/#copy-import-or-export-dashboard-json

![image](https://github.com/lukalovosevic/community/assets/62242783/850dd6a2-f9d8-444a-9faa-7ecea01b6268)

## References
- https://rockset.com/docs/monitoring-and-alerting/
- https://docs.datadoghq.com/integrations/openmetrics/
