from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage

with Diagram("FreshRSS", show=False, direction="TB"):
    with Cluster("k3s"):
        with Cluster("Namespace: jovian-prod"):
            cloudflare_tunnel = Custom("Cloudflare Tunnel", "/app/icons/cf-tunnel.png")
            freshrss = Custom("FreshRSS", "/app/icons/freshrss.png")
        with Cluster("Namespace: kube-system"):
            traefik = network.Traefik("Traefik\nInternal Proxy")
        with Cluster("Namespace: ceph-csi-cephfs"):
            ceph = storage.Ceph("PVC")
        with Cluster("Namespace: volsync-system"):
            backup = Custom("Backups", "/app/icons/restic.png")

    cloudflare_tunnel >> Edge(color="#CEA400", style="solid") >> freshrss
    traefik >> Edge(color="blue", style="dotted") >> freshrss
    ceph >> Edge(color="black", style="solid") >> freshrss
    backup << Edge(color="black", style="solid") << freshrss
