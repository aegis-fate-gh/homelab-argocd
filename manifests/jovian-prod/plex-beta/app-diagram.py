from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import storage, logging
from diagrams.k8s.storage import PVC

with Diagram("app", show=False, direction="TB"):
    with Cluster("Homelab"):
        with Cluster("Router"):
            router = Custom("UDM-PRO SE", "/app/icons/ubiquiti-unifi.png")
        unas_pro = Custom("UNAS-Pro", "/app/icons/unifi-drive.png")
        with Cluster("Host: Donnager"):
            with Cluster("VM: Polaris"):
                with Cluster("Docker"):
                    loki = logging.Loki("Loki")
        with Cluster("Eos"):
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    with Cluster("Pod: Plex-Beta"):
                        plex = Custom("Plex", "/app/icons/plex.png")
                        alloy = Custom("Alloy", "/app/icons/alloy.png")
                    with Cluster("Pod: Tracearr"):
                        tracearr = Custom("Tracearr", "/app/icons/tracearr.png")
                    with Cluster("Pod: Arrstack"):
                        radarr = Custom("Radarr", "/app/icons/radarr.png")
                        sonarr = Custom("Sonarr", "/app/icons/sonarr.png")

                    ceph = storage.Ceph("Plex-Beta PVC")
                    smb = PVC("Media SMB PVC")

                metallb = Custom("MetalLB IP", "/app/icons/metallb.png")

    ceph >> Edge(color="darkorange", style="solid") >> plex

    metallb >> plex

    plex >> Edge(color="orangered", style="bold") >> alloy >> Edge(color="orangered", style="bold") >> loki
    plex << Edge(color="orangered", style="bold") << smb >> Edge(color="orangered", style="bold") << unas_pro

    sonarr >> Edge(color="turquoise1", style="bold", minlen="2") >> plex
    radarr >> Edge(color="orange1", style="bold", minlen="2") >> plex

    plex >> Edge(color="orangered", style="bold") >> tracearr

    router >> plex