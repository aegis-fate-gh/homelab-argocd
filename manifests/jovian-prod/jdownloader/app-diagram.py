from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage
from diagrams.k8s.storage import PVC

with Diagram("APP", show=False, direction="TB"):
    with Cluster("Homelab"):
        unas_pro = Custom("UNAS-Pro", "/app/icons/unifi-drive.png")
        with Cluster("Eos"):
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    with Cluster("Pod: jdownloader"):
                        jd = Custom("jdownloader-2", "/app/icons/jdownloader2.png")

                    jd_pvc = storage.Ceph("jdownloader PVC")
                    smb = PVC("Media SMB PVC")
                with Cluster("Namespace: kube-system"):
                    traefik = network.Traefik("Traefik\nInternal Proxy")

    traefik >> Edge(color="blue", style="dotted") >> jd

    jd >> jd_pvc
    jd >> smb >>  unas_pro

                