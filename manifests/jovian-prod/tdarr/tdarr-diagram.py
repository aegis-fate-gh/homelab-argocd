from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage

with Diagram("APP", show=False, direction="TB"):
    with Cluster("Eos"):
        with Cluster("k3s"):
            with Cluster("Namespace: jovian-prod"):
                tdarr = Custom("Tdarr", "/app/icons/tdarr.png")
                ceph = storage.Ceph("CephFS PVC")
                smb = Custom("SMB to UNAS-Pro", "/app/icons/unifi-drive.png")
            with Cluster("Namespace: kube-system"):
                traefik = network.Traefik("Traefik\nInternal Proxy")

    traefik >> Edge(color="blue", style="dotted") >> tdarr
    ceph >> Edge(color="black", style="solid") >> tdarr
    smb >> Edge(color="black", style="solid") >> tdarr