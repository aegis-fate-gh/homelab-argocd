from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage
from diagrams.k8s.storage import PVC
from diagrams.onprem.database import Mongodb

with Diagram("app", show=False, direction="TB"):
    with Cluster("Homelab"):
        unas_pro = Custom("UNAS-Pro", "/app/icons/unifi-drive.png")
        with Cluster("Eos"):
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    ytdl = Custom("YouTube DL Material", "/app/icons/youtube-dl.png")
                    ceph = storage.Ceph("CephFS PVC")
                    smb = PVC("Media SMB PVC")
                    mongo = Mongodb("YTDL Mongo")
                with Cluster("Namespace: kube-system"):
                    traefik = network.Traefik("Traefik\nInternal Proxy")

    traefik >> Edge(color="blue", style="dotted") >> ytdl
    ceph >> Edge(color="darkorange", style="solid") >> ytdl
    ceph >> Edge(color="darkorange", style="solid") >> mongo
    smb - Edge(color="black", style="solid") - ytdl
    unas_pro - Edge(color="royalblue", style="solid") - smb
    ytdl - mongo
