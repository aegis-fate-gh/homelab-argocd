from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage
from diagrams.k8s.storage import PVC

with Diagram("app", show=False, direction="TB"):
    with Cluster("Homelab"):
        unas_pro = Custom("UNAS-Pro", "/app/icons/unifi-drive.png")
        with Cluster("Eos"):
            with Cluster("LXC"):
                tdarr_lxc = Custom("Tdarr Workers", "/app/icons/tdarr.png")
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    with Cluster("Pod: Tdarr"):
                        tdarr = Custom("Tdarr Server", "/app/icons/tdarr.png")
                    with Cluster("Pod: Arrstack"):
                        radarr = Custom("Radarr", "/app/icons/radarr.png")
                        sonarr = Custom("Sonarr", "/app/icons/sonarr.png")
                        
                    ceph = storage.Ceph("CephFS PVC")
                    smb = PVC("Media SMB PVC")
                    loadbalancer = Custom("MetalLB IP", "/app/icons/metallb.png")

                with Cluster("Namespace: kube-system"):
                    traefik = network.Traefik("Traefik\nInternal Proxy")

    traefik >> Edge(color="blue", style="dotted") >> tdarr
    ceph >> Edge(color="darkorange", style="solid") >> tdarr
    smb - Edge(color="black", style="solid") - tdarr
    tdarr_lxc >> Edge(color="royalblue", style="solid") >> loadbalancer >> Edge(color="royalblue", style="solid") >> tdarr
    unas_pro - Edge(color="royalblue", style="solid") - tdarr_lxc
    unas_pro - Edge(color="royalblue", style="solid") - smb

    tdarr >> Edge(color="royalblue", style="solid") >> sonarr
    tdarr >> Edge(color="royalblue", style="solid") >> radarr