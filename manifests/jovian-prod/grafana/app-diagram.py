from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage, logging

with Diagram("app", show=False, direction="TB"):
    with Cluster("Backblaze"):
        backblaze = Custom("Backups", "/app/icons/backblaze.png")
    with Cluster("Homelab"):
        with Cluster("Host: Donnager"):
            with Cluster("VM: Polaris"):
                with Cluster("Docker"):
                    loki = logging.Loki("Loki")
                    vm = Custom("VictoriaMetrics", "/app/icons/victoriametrics.png")
        with Cluster("Eos"):
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    with Cluster("Pod: Grafana"):
                        grafana = Custom("Grafana", "/app/icons/grafana.png")
                    with Cluster("Heml: Prometheus"):
                        prometheus = Custom("Grafana", "/app/icons/grafana.png")
                    with Cluster("Deployment: Cloudflare-tunnel"):
                        cloudflare_tunnel = Custom("Cloudflare Tunnel", "/app/icons/cf-tunnel.png")

                    ceph = storage.Ceph("Grafana PVC")
                    backup = Custom("Backups", "/app/icons/restic.png")
                with Cluster("Namespace: kube-system"):
                    traefik = network.Traefik("Traefik\nInternal Proxy")

    traefik >> Edge(color="blue", style="dotted") >> grafana
    ceph >> Edge(color="darkorange", style="solid") >> grafana
    backblaze << Edge(color="black", style="solid") << backup << Edge(color="black", style="solid") << ceph
    cloudflare_tunnel >> Edge(color="#CEA400", style="solid") >> grafana

    grafana >> loki
    grafana >> prometheus
    grafana >> vm
