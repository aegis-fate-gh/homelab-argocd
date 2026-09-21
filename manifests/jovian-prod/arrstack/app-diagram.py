from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage

with Diagram("APP", show=False, direction="TB"):
    with Cluster("Homelab"):
        unas_pro = Custom("UNAS-Pro", "/app/icons/unifi-drive.png")
        with Cluster("Eos"):
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    with Cluster("Pod: Arrstack"):
                        bazarr = Custom("Bazarr", "/app/icons/bazarr.png")
                        prowlarr = Custom("Prowlarr", "/app/icons/prowlarr.png")
                        radarr = Custom("Radarr", "/app/icons/radarr.png")
                        sonarr = Custom("Sonarr", "/app/icons/sonarr.png")
                        cleanuparr = Custom("Cleanuparr", "/app/icons/cleanuparr.png")
                        flaresolverr = Custom("Flaresolverr", "/app/icons/flaresolverr.png")
                    with Cluster("Pod: Plex"):
                        plex = Custom("Plex", "/app/icons/plex.png")
                    with Cluster("Pod: Plex-Beta"):
                        plex_beta = Custom("Plex-Beta", "/app/icons/plex.png")
                    with Cluster("Pod: Jellyfin"):
                        jellyfin = Custom("Jellyfin", "/app/icons/jellyfin.png")
                    with Cluster("Pod: Arch-qbittorrent"):
                        arch_qbittorrent = Custom("Arch-Qbitorrent", "/app/icons/qbittorrent.png")
                    with Cluster("Pod: Seerr"):
                        seerr = Custom("Seerr", "/app/icons/overseerr.png")
                    with Cluster("Pod: Tdarr"):
                        tdarr = Custom("Tdarr", "/app/icons/tdarr.png")
                    bazarr_pvc = storage.Ceph("PVC")
                    prowlarr_pvc = storage.Ceph("PVC")
                    radarr_pvc = storage.Ceph("PVC")
                    sonarr_pvc = storage.Ceph("PVC")
                    cleanuparr_pvc = storage.Ceph("PVC")
                with Cluster("Namespace: kube-system"):
                    traefik = network.Traefik("Traefik\nInternal Proxy")

seerr >> [sonarr, radarr]