from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage
from diagrams.k8s.storage import PVC

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
                    smb = PVC("Media SMB PVC")
                with Cluster("Namespace: kube-system"):
                    traefik = network.Traefik("Traefik\nInternal Proxy")

traefik >> Edge(color="blue", style="dotted") >> sonarr
traefik >> Edge(color="blue", style="dotted") >> radarr
traefik >> Edge(color="blue", style="dotted") >> bazarr
traefik >> Edge(color="blue", style="dotted") >> prowlarr
traefik >> Edge(color="blue", style="dotted") >> cleanuparr

bazarr_pvc >> Edge(color="darkorange", style="solid") >> bazarr
prowlarr_pvc >> Edge(color="darkorange", style="solid") >> prowlarr
radarr_pvc >> Edge(color="darkorange", style="solid") >> radarr
sonarr_pvc >> Edge(color="darkorange", style="solid") >> sonarr
cleanuparr_pvc >> Edge(color="darkorange", style="solid") >> cleanuparr

smb - Edge(color="black", style="solid") - bazarr
smb - Edge(color="black", style="solid") - radarr
smb - Edge(color="black", style="solid") - sonarr

unas_pro - Edge(color="royalblue", style="solid") - smb

seerr >> Edge(color="magenta1", style="bold", minlen="3") >> sonarr
seerr >> Edge(color="magenta1", style="bold", minlen="3") >> radarr

cleanuparr >> Edge(color="darkviolet", style="bold") >> sonarr
cleanuparr >> Edge(color="darkviolet", style="bold") >> radarr
cleanuparr >> Edge(color="darkviolet", style="bold") >> arch_qbittorrent

bazarr >> Edge(color="black", style="bold") >> sonarr
bazarr >> Edge(color="black", style="bold") >> radarr

prowlarr >> arch_qbittorrent
prowlarr >> flaresolverr

sonarr >> Edge(color="turquoise1", style="bold", minlen="2") >> arch_qbittorrent
sonarr >> Edge(color="turquoise1", style="bold", minlen="2") >> plex
sonarr >> Edge(color="turquoise1", style="bold", minlen="2") >> plex_beta
sonarr >> Edge(color="turquoise1", style="bold", minlen="2") >> jellyfin
sonarr >> Edge(color="turquoise1", style="bold", minlen="2") >> prowlarr

radarr >> Edge(color="orange1", style="bold", minlen="2") >> arch_qbittorrent
radarr >> Edge(color="orange1", style="bold", minlen="2") >> plex
radarr >> Edge(color="orange1", style="bold", minlen="2") >> plex_beta
radarr >> Edge(color="orange1", style="bold", minlen="2") >> jellyfin
radarr >> Edge(color="orange1", style="bold", minlen="2") >> prowlarr

tdarr >> Edge(color="royalblue", style="solid") >> sonarr
tdarr >> Edge(color="royalblue", style="solid") >> radarr
