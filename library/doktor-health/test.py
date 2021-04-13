from doktor_health import health


def test():
    """ 正常系 """
    h_red = health.Health(status=health.HealthStatus.RED,
                          description="Invalid")
    assert h_red.status == health.HealthStatus.RED
    assert h_red.description == "Invalid"
    print(h_red.to_dict())

    h_default = health.Health(status=health.HealthStatus.GREEN,
                              description="It works")
    assert h_default.status == health.HealthStatus.GREEN
    assert h_default.description == "It works"
    print(h_default.to_dict())


if __name__ == '__main__':
    test()
