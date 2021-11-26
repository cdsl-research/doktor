names = [
    "couchbase",
    "postgres",
    "ubuntu",
    "alpine",
    "mongo",
    "traefil",
    "redis",
    "busybox",
    "mariadb",
    "node"]

f = open("template.yaml", "r")
tem = f.read()
for n in names:
    with open(f"{n}.yaml", "w") as f:
        f.write(tem.replace("%name", n))
