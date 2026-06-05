from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network

with Diagram("Converter Now", show=False, direction="TB"):
    with Cluster("jovian-prod"):
        converternow = Custom("Converter Now", "/app/icons/converternow.png")
    with Cluster("kube-system"):
        traefik = network.Traefik("Traefik\nInternal Proxy")

    traefik >> Edge(color="blue", style="dotted") >> converternow