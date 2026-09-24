from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage

with Diagram("app", show=False, direction="TB"):
    with Cluster("Proton"):
        proton = Custom("Proton Mail", "/app/icons/proton-mail.png")
    with Cluster("Backblaze"):
        backblaze = Custom("Backups", "/app/icons/backblaze.png")
    with Cluster("Homelab"):
        with Cluster("Eos"):
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    with Cluster("Deployment: Cloudflare-tunnel"):
                        cloudflare_tunnel = Custom("Cloudflare Tunnel", "/app/icons/cf-tunnel.png")
                    with Cluster("Pod: Tautulli"):
                        tautulli = Custom("Tautulli", "/app/icons/tautulli.png")
                    with Cluster("Pod: Plex"):
                        plex = Custom("Plex", "/app/icons/plex.png")
                    with Cluster("Pod: Tracearr"):
                        tracearr = Custom("Tracearr", "/app/icons/tracearr.png")
                    ceph = storage.Ceph("Tautulli PVC")
                    backup = Custom("Backups", "/app/icons/restic.png")
                with Cluster("Namespace: kube-system"):
                    traefik = network.Traefik("Traefik\nInternal Proxy")

    traefik >> Edge(color="blue", style="dotted") >> tautulli
    ceph >> Edge(color="darkorange", style="solid") >> tautulli

    cloudflare_tunnel >> Edge(color="#CEA400", style="solid") >> tautulli

    backblaze << Edge(color="black", style="solid") << backup << Edge(color="black", style="solid") << tautulli

    tautulli >> proton
    plex >> tautulli
    tautulli >> tracearr
