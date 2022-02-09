# Datadog Openmetrics Configuration Example
Datadog provides an agent that will scrape metrics across various sources including an Openmetrics endpoint like the one provided by Rockset. You can configure this agent to scrape metrics from your Rockset metrics endpoint using the Openmetrics integration.

## Dependencies
1. Datadog Agent version 6.6.0 and above
2. Enable Rockset metrics endpoint

## Instructions
Copy the [example](./openmetrics.d/conf.yaml) from this repository to your agent's host. The location of this configuration file on your agent host will generally be located at:
```
../datadog-agent/etc/conf.d/openmetrics.d
```

The syntax is very specific and please note any differences between your file and the example provided. For exampe, the password must be an empty string in order to be encoded properly.

## References
- https://rockset.com/docs/monitoring-and-alerting/
- https://docs.datadoghq.com/integrations/openmetrics/