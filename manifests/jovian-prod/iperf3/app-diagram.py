from diagrams import Diagram, Cluster
from diagrams.custom import Custom

with Diagram("app", show=False, direction="TB"):
    with Cluster("Homelab"):
        with Cluster("Eos"):
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    with Cluster("Pod: iperf3"):
                        iperf = Custom("iperf3", "/app/icons/iperf.png")

                metallb = Custom("MetalLB IP", "/app/icons/metallb.png")

    metallb >> iperf
