from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage, inmemory, database

with Diagram("app", show=False, direction="TB"):
    with Cluster("Backblaze"):
        backblaze = Custom("Backups", "/app/icons/backblaze.png")
    with Cluster("Router"):
        router = Custom("UDM-PRO SE", "/app/icons/ubiquiti-unifi.png")
    with Cluster("Homelab"):
        with Cluster("Homelab"):
            unas_pro = Custom("UNAS-Pro", "/app/icons/unifi-drive.png")
        with Cluster("Eos"):
            with Cluster("VM: Wings-01/02"):
                with Cluster("Docker"):
                    wings = Custom("Pterodactyl Wings", "/app/icons/pterodactyl.png")
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    with Cluster("Deployment: Cloudflare-tunnel"):
                        cloudflare_tunnel = Custom("Cloudflare Tunnel", "/app/icons/cf-tunnel.png")
                    with Cluster("Pod: Pterodactyl-Panel"):
                        pterodactyl = Custom("Pterodactyl Wings", "/app/icons/pterodactyl.png")
                        mariadb = database.Mariadb("Maria DB")
                        redis = inmemory.Redis("Redis")

                    ceph = storage.Ceph("Pterodactyl PVC")

                    backup = Custom("Backups", "/app/icons/restic.png")

                with Cluster("Namespace: kube-system"):
                    traefik = network.Traefik("Traefik\nInternal Proxy")

    traefik >> Edge(color="blue", style="dotted") >> pterodactyl
    ceph >> Edge(color="darkorange", style="solid") >> pterodactyl

    backblaze << Edge(color="black", style="solid") << backup << Edge(color="black", style="solid") << ceph
    backblaze << Edge(color="black", style="solid") << unas_pro

    cloudflare_tunnel >> Edge(color="#CEA400", style="solid") >> pterodactyl

    pterodactyl >> wings
    pterodactyl >> mariadb
    pterodactyl >> redis

    wings >> unas_pro

    router >> wings
