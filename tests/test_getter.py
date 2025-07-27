from module.getter import Getter

def test_getter():
    getter = Getter()

    packages = getter.get_packages("p11")

    assert isinstance(packages, dict)

    assert "packages" in packages

    assert isinstance(packages["packages"], list)

    assert len(packages["packages"]) > 0

    for key in ["name", "epoch", "version", "release", "arch"]:
        assert packages["packages"][0][key] is not None