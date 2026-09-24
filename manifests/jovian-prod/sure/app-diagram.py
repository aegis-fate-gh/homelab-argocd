from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage, inmemory, database

with Diagram("app", show=False, direction="TB"):
    with Cluster("Simplefin"):
        simplefin = Custom("Simplefin", "/app/icons/simplefin.png")
    with Cluster("Backblaze"):
        backblaze = Custom("Backups", "/app/icons/backblaze.png")
    with Cluster("Homelab"):
        with Cluster("Eos"):
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    with Cluster("Pod: Sure"):
                        sure = Custom("Sure", "/app/icons/youtube-dl.png")
                        worker = Custom("Worker", "/app/icons/sure-finance.png")
                        postgres = database.Postgresql("Postgres")
                        redis = inmemory.Redis("Redis")

                    ceph_sure = storage.Ceph("Sure PVC")
                    ceph_postgres = storage.Ceph("Postgres PVC")
                    ceph_redis = storage.Ceph("Redis PVC")

                    backup = Custom("Backups", "/app/icons/restic.png")

                with Cluster("Namespace: kube-system"):
                    traefik = network.Traefik("Traefik\nInternal Proxy")

    traefik >> Edge(color="blue", style="dotted") >> sure
    ceph_sure >> Edge(color="darkorange", style="solid") >> sure
    ceph_postgres >> Edge(color="darkorange", style="solid") >> postgres
    ceph_redis >> Edge(color="darkorange", style="solid") >> redis

    backblaze << Edge(color="black", style="solid") << backup << Edge(color="black", style="solid") << sure

    sure >> simplefin
    sure >> worker
    sure >> postgres
    sure >> redis
