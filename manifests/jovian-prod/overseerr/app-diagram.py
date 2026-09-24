from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network
from diagrams.k8s.storage import PVC

with Diagram("app", show=False, direction="TB"):
    with Cluster("Backblaze"):
        backblaze = Custom("Backups", "/app/icons/backblaze.png")
    with Cluster("Discord"):
        discord = Custom("Discord", "/app/icons/discord.png")
    with Cluster("Homelab"):
        unas_pro = Custom("UNAS-Pro", "/app/icons/unifi-drive.png")
        with Cluster("Eos"):
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    with Cluster("Pod: overseerr"):
                        seerr = Custom("Seerr", "/app/icons/overseerr.png")
                    with Cluster("Pod: Arrstack"):
                        radarr = Custom("Radarr", "/app/icons/radarr.png")
                        sonarr = Custom("Sonarr", "/app/icons/sonarr.png")
                    with Cluster("Pod: Plex"):
                        plex = Custom("Plex", "/app/icons/plex.png")
                    with Cluster("Deployment: Cloudflare-tunnel"):
                        cloudflare_tunnel = Custom("Cloudflare Tunnel", "/app/icons/cf-tunnel.png")

                    backup = Custom("Backups", "/app/icons/restic.png")
                    smb = PVC("Media SMB PVC")

                with Cluster("Namespace: kube-system"):
                    traefik = network.Traefik("Traefik\nInternal Proxy")

    traefik >> Edge(color="blue", style="dotted") >> seerr
    cloudflare_tunnel >> Edge(color="#CEA400", style="solid") >> seerr
    backblaze << Edge(color="black", style="solid") << backup << Edge(color="black", style="solid") << seerr

    seerr >> Edge(color="magenta1", style="bold", minlen="3") >> sonarr
    seerr >> Edge(color="magenta1", style="bold", minlen="3") >> radarr
    seerr >> Edge(color="magenta1", style="bold", minlen="3") >> discord
    seerr << Edge(color="magenta1", style="bold", minlen="3") << plex
    seerr << Edge(color="black", style="solid") << smb << Edge(color="black", style="solid") << unas_pro
