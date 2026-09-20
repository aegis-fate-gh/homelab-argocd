from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage

with Diagram("APP", show=False, direction="TB"):
    with Cluster("Eos"):
        with Cluster("k3s"):
            with Cluster("Namespace: jovian-prod"):

            with Cluster("Namespace: kube-system"):
                traefik = network.Traefik("Traefik\nInternal Proxy")
            with Cluster("Namespace: ceph-csi-cephfs"):
                ceph = storage.Ceph("PVC")
            with Cluster("Namespace: volsync-system"):
                backup = Custom("Backups", "/app/icons/restic.png")