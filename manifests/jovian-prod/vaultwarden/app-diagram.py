from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage
from diagrams.k8s.storage import PVC

with Diagram("app", show=False, direction="TB"):
    with Cluster("Backblaze"):
        backblaze = Custom("Backups", "/app/icons/backblaze.png")
    with Cluster("Homelab"):
        with Cluster("Eos"):
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    with Cluster("Pod: Vaultwarden"):
                        vaultwarden = Custom("Vaultwarden", "/app/icons/vaultwarden.png")
                    ceph = storage.Ceph("Vaultwarden PVC")
                    backup = Custom("Backups", "/app/icons/restic.png")
                with Cluster("Namespace: kube-system"):
                    traefik = network.Traefik("Traefik\nInternal Proxy")

    traefik >> Edge(color="blue", style="dotted") >> vaultwarden
    ceph >> Edge(color="darkorange", style="solid") >> vaultwarden
    backblaze << Edge(color="black", style="solid") << backup << Edge(color="black", style="solid") << vaultwarden
