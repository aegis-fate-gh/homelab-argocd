from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage

with Diagram("app", show=False, direction="TB"):
    with Cluster("Homelab"):
        with Cluster("Eos"):
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    with Cluster("Pod: Homarr"):
                        homarr = Custom("Homarr", "/app/icons/homarr.png")

                    ceph = storage.Ceph("Homarr PVC")
                with Cluster("Namespace: kube-system"):
                    traefik = network.Traefik("Traefik\nInternal Proxy")

    traefik >> Edge(color="blue", style="dotted") >> homarr
    ceph >> Edge(color="darkorange", style="solid") >> homarr
