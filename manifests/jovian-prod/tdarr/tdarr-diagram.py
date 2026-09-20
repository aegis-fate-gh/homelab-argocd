from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage
from diagrams.k8s.storage import pvc

with Diagram("Tdarr", show=False, direction="TB"):
    with Cluster("Homelab"):
        unas_pro = Custom("UNAS-Pro", "/app/icons/unifi-drive.png")
        with Cluster("Eos"):
            tdarr_lxc = Custom("Tdarr Workers", "/app/icons/tdarr.png")
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    tdarr = Custom("Tdarr Server", "/app/icons/tdarr.png")
                    ceph = storage.Ceph("CephFS PVC")
                    smb = pvc("Media SMB PVC")
                    loadbalancer = Custom("MetalLB IP", "/app/icons/metallb.png")
                with Cluster("Namespace: kube-system"):
                    traefik = network.Traefik("Traefik\nInternal Proxy")

    traefik >> Edge(color="blue", style="dotted") >> tdarr
    ceph >> Edge(color="darkorange", style="solid") >> tdarr
    smb >> Edge(color="black", style="solid") >> tdarr
    tdarr_lxc >> Edge(color="royalblue", style="solid") >> loadbalancer >> Edge(color="royalblue", style="solid") >> tdarr
    unas_pro >> Edge(color="royalblue", style="solid") >> tdarr_lxc
    unas_pro >> Edge(color="royalblue", style="solid") >> smb