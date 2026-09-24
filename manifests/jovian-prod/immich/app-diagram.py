from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import storage, inmemory, database, network
from diagrams.k8s.storage import PVC

with Diagram("app", show=False, direction="TB"):
    with Cluster("Parents House"):
        with Cluster("Synology RS1221+"):
            syn_sanctuary = Custom("Off-Site Backups", "/app/icons/synology.png")
    with Cluster("Backblaze"):
        backblaze = Custom("Backups", "/app/icons/backblaze.png")
    with Cluster("Dropbox"):
        dropbox = Custom("Dropbox", "/app/icons/dropbox.png")
    with Cluster("Homelab"):
        unas_pro = Custom("UNAS-Pro", "/app/icons/unifi-drive.png")
        synology = Custom("DS923+", "/app/icons/synology.png")

        with Cluster("Eos"):
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    with Cluster("Pod: Immich"):
                        immich = Custom("Immich", "/app/icons/immich.png")
                        ml = Custom("Immich ML", "/app/icons/immich.png")
                        redis = inmemory.Redis("Redis")
                        db = database.Postgresql("Postgres")

                    with Cluster("Deployment: Cloudflare-tunnel"):
                        cloudflare_tunnel = Custom("Cloudflare Tunnel", "/app/icons/cf-tunnel.png")

                    ceph = storage.Ceph("Immich PVC")
                    backup = Custom("Backups", "/app/icons/restic.png")
                    smb_silo = PVC("SMB Storage PVC")
                    smb_syn = PVC("SMB Import PVC")

                with Cluster("Namespace: kube-system"):
                    traefik = network.Traefik("Traefik\nInternal Proxy")

    ceph >> Edge(color="darkorange", style="solid") >> immich

    traefik >> Edge(color="blue", style="dotted") >> immich
    cloudflare_tunnel >> Edge(color="#CEA400", style="solid") >> immich

    backblaze << Edge(color="black", style="solid") << backup << Edge(color="black", style="solid") << immich

    immich << Edge(color="orangered", style="bold") << smb_silo >> Edge(color="orangered", style="bold") << unas_pro
    immich << Edge(color="orangered", style="bold") << smb_syn >> Edge(color="orangered", style="bold") << synology << dropbox
    immich - ml
    immich - redis
    immich - db

    unas_pro >> syn_sanctuary

    syn_sanctuary >> dropbox
