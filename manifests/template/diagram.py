from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage

with Diagram("APP", show=False, direction="TB"):
    with Cluster("Eos"):
        with Cluster("k3s"):
            with Cluster("Namespace: jovian-prod"):
                ceph = storage.Ceph("PVC")
                backup = Custom("Backups", "/app/icons/restic.png")
            with Cluster("Namespace: kube-system"):
                traefik = network.Traefik("Traefik\nInternal Proxy")                
                