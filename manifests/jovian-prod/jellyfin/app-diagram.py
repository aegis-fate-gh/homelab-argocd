from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import storage, logging, network
from diagrams.k8s.storage import PVC

with Diagram("app", show=False, direction="TB"):
    with Cluster("Parents House"):
        with Cluster("Synology RS1221+"):
            synology = Custom("Off-Site Backups", "/app/icons/synology.png")
    with Cluster("Backblaze"):
        backblaze = Custom("Backups", "/app/icons/backblaze.png")
    with Cluster("Homelab"):
        unas_pro = Custom("UNAS-Pro", "/app/icons/unifi-drive.png")
        with Cluster("Eos"):
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    with Cluster("Pod: Jellyfin"):
                        jellyfin = Custom("Jellyfin", "/app/icons/jellyfin.png")
                    with Cluster("Pod: Tracearr"):
                        tracearr = Custom("Tracearr", "/app/icons/tracearr.png")
                    with Cluster("Pod: Arrstack"):
                        radarr = Custom("Radarr", "/app/icons/radarr.png")
                        sonarr = Custom("Sonarr", "/app/icons/sonarr.png")
                    with Cluster("Deployment: Cloudflare-tunnel"):
                        cloudflare_tunnel = Custom("Cloudflare Tunnel", "/app/icons/cf-tunnel.png")
                with Cluster("Namespace: kube-system"):
                    traefik = network.Traefik("Traefik\nInternal Proxy")

                    ceph = storage.Ceph("Jellyfin PVC")
                    backup = Custom("Backups", "/app/icons/restic.png")
                    smb = PVC("Media SMB PVC")

                metallb = Custom("MetalLB IP", "/app/icons/metallb.png")

    ceph >> Edge(color="darkorange", style="solid") >> jellyfin

    metallb >> jellyfin
    traefik >> Edge(color="blue", style="dotted") >> traefik

    backblaze << Edge(color="black", style="solid") << backup << Edge(color="black", style="solid") << jellyfin
    jellyfin << Edge(color="orangered", style="bold") << smb >> Edge(color="orangered", style="bold") << unas_pro
    cloudflare_tunnel >> Edge(color="#CEA400", style="solid") >> jellyfin

    unas_pro >> synology

    sonarr >> Edge(color="turquoise1", style="bold", minlen="2") >> jellyfin
    radarr >> Edge(color="orange1", style="bold", minlen="2") >> jellyfin

    jellyfin >> Edge(color="BlueViolet", style="bold") >> tracearr
