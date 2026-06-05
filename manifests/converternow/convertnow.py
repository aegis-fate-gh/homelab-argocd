from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network

with Diagram("Converternow", show=False, direction="TB"):
    with Cluster("jovian-prod"):
        converternow = Custom("Converter Now", "./local_icons/converternow.jpg")
    with Cluster("kube-system"):
        traefik = network.Traefik("Traefik\nInternal Proxy")

    traefik >> Edge(color="blue", style="dotted") >> converternow