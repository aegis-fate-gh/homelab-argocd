from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage
from diagrams.k8s.storage import PVC

with Diagram("APP", show=False, direction="TB"):
    with Cluster("Parents House"):
        with Cluster("Synology RS1221+"):
            with Cluster("Docker"):
                zen = Custom("Plex", "/app/icons/plex.png")
        with Cluster("UnRaid"):
            with Cluster("Docker"):
                andromeda = Custom("Plex", "/app/icons/plex.png")
    with Cluster("Homelab"):
        with Cluster("Eos"):
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    with Cluster("Pod: Tracearr"):
                        tracearr = Custom("Tracearr", "/app/icons/tracearr.png")
                    with Cluster("Pod: Plex"):
                        plex = Custom("Plex", "/app/icons/plex.png")
                    with Cluster("Pod: Plex-Beta"):
                        plex_beta = Custom("Plex", "/app/icons/plex.png")
                    with Cluster("Pod: Jellyfin"):
                        jellyfin = Custom("Jellyfin", "/app/icons/jellyfin.png")
                    tracearr_pvc = storage.Ceph("Tracearr PVC")
                with Cluster("Namespace: kube-system"):
                    traefik = network.Traefik("Traefik\nInternal Proxy")

    traefik >> Edge(color="blue", style="dotted") >> tracearr
    tracearr >> Edge(color="deepskyblue", style="solid") >> tracearr_pvc

    tracearr << plex
    tracearr << plex_beta
    tracearr << jellyfin
    tracearr << zen
    tracearr << andromeda
                