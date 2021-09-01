names = ["couchbase", "postgres", "ubuntu", "alpine", "mongo", "traefil", "redis", "busybox", "mariadb", "node"]

for n in names:
    tem = """apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: %name
    spec:
      selector:
        matchLabels:
          app: %name
      replicas: 1
      template:
        metadata:
          labels:
            app: %name
        spec:
          containers:
          - name: flask
            image: %name:latest
            imagePullPolicy: IfNotPresent
    """
    with open(f"{n}.yaml","w") as f:
        f.write(tem.replace("%name",n))
