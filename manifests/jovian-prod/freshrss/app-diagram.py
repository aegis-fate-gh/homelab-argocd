from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage

with Diagram("app", show=False, direction="TB"):
    with Cluster("Backblaze"):
        backblaze = Custom("Backups", "/app/icons/backblaze.png")
    with Cluster("Homelab"):
        with Cluster("Eos"):
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    with Cluster("Deployment: Cloudflare-tunnel"):
                        cloudflare_tunnel = Custom("Cloudflare Tunnel", "/app/icons/cf-tunnel.png")
                    with Cluster("Pod: FreshRSS"):
                        freshrss = Custom("FreshRSS", "/app/icons/freshrss.png")
                    ceph = storage.Ceph("FreshRSS PVC")
                    backup = Custom("Backups", "/app/icons/restic.png")
                with Cluster("Namespace: kube-system"):
                    traefik = network.Traefik("Traefik\nInternal Proxy")

    cloudflare_tunnel >> Edge(color="#CEA400", style="solid") >> freshrss
    traefik >> Edge(color="blue", style="dotted") >> freshrss
    ceph >> Edge(color="darkorange", style="solid") >> freshrss
    backblaze << Edge(color="black", style="solid") << backup << Edge(color="black", style="solid") << ceph
