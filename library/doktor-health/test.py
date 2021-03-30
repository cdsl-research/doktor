from doktor_health import health


def test():
    h_red = health.Health(health.HealthStatus.RED, "Invalid")
    assert h_red.status == health.HealthStatus.RED
    assert h_red.description == "Invalid"
    print(h_red)

    h_default = health.Health()
    assert h_default.status == health.HealthStatus.GREEN
    assert h_default.description == "It works"
    print(h_default)

    h_default.status = health.HealthStatus.YELLOW
    h_default.description = "Slow throughput"
    """
    assert h_default == health.HealthStatus.YELLOW
    assert h_default == "Slow throughput"
    print(h_default)
    """


if __name__ == '__main__':
    test()
