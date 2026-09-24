from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage
from diagrams.k8s.storage import PVC
from diagrams.onprem.database import Mongodb

with Diagram("app", show=False, direction="TB"):
    with Cluster("Homelab"):
        with Cluster("Eos"):
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    with Cluster("Pod: Snapotter"):
                        snapotter = Custom("Snapotter", "/app/icons/snapotter.png")

                    ceph = storage.Ceph("Snapotter PVC")

                with Cluster("Namespace: kube-system"):
                    traefik = network.Traefik("Traefik\nInternal Proxy")

    traefik >> Edge(color="blue", style="dotted") >> snapotter
    ceph >> Edge(color="darkorange", style="solid") >> snapotter
