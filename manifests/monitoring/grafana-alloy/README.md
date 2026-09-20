#### Use Case
This contains the config and manifests for Grafana Alloy, which replaces Promtail in the Jovian cluster as the primary logging forwarder.

After the logs are captured, they are then shipped off to Loki, which runs via a docker container on a different host.

#### Architecture

#### Diagram

#### Source
https://github.com/grafana/alloy