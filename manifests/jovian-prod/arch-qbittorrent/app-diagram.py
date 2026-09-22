from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage
from diagrams.k8s.storage import PVC

with Diagram("APP", show=False, direction="TB"):
    with Cluster("Proton"):
        proton = Custom("Proton VPN", "/app/icons/proton-vpn.png")
    with Cluster("Homelab"):
        unas_pro = Custom("UNAS-Pro", "/app/icons/unifi-drive.png")
        with Cluster("Eos"):
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    with Cluster("Pod: Arch-qBittorrent"):
                        busybox = Custom("Prowlarr", "/app/icons/busybox.png")
                        arch = Custom("Prowlarr", "/app/icons/qbittorrent.png")
                    with Cluster("Pod: Arrstack"):
                        prowlarr = Custom("Prowlarr", "/app/icons/prowlarr.png")
                        radarr = Custom("Radarr", "/app/icons/radarr.png")
                        sonarr = Custom("Sonarr", "/app/icons/sonarr.png")
                        cleanuparr = Custom("Cleanuparr", "/app/icons/cleanuparr.png")
                    arch_pvc = storage.Ceph("Arch-qBittorrent PVC")
                    smb = PVC("Media SMB PVC")
                with Cluster("Namespace: kube-system"):
                    traefik = network.Traefik("Traefik\nInternal Proxy")

    traefik >> Edge(color="blue", style="dotted") >> arch

    cleanuparr >> Edge(color="darkviolet", style="bold") >> arch
    sonarr >> Edge(color="turquoise1", style="bold", minlen="2") >> arch
    radarr >> Edge(color="orange1", style="bold", minlen="2") >> arch
    prowlarr >> arch

    busybox >> arch_pvc

    arch >> Edge(color="deepskyblue", style="solid") >> arch_pvc
    arch >> Edge(color="deepskyblue", style="solid") >> proton
    arch >> Edge(color="deepskyblue", style="solid") >> smb >> Edge(color="deepskyblue", style="solid") >> unas_pro

                