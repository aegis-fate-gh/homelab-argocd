from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage

with Diagram("app", show=False, direction="TB"):
    with Cluster("Discord"):
        discord = Custom("Discord", "/app/icons/discord.png")
    with Cluster("Homelab"):
        with Cluster("Eos"):
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    uptime = Custom("Uptime-Kuma", "/app/icons/uptime-kuma.png")
                    ceph = storage.Ceph("Uptime-Kuma PVC")
                with Cluster("Namespace: kube-system"):
                    traefik = network.Traefik("Traefik\nInternal Proxy")

    traefik >> Edge(color="blue", style="dotted") >> uptime
    ceph >> Edge(color="darkorange", style="solid") >> uptime
    uptime >> discord


