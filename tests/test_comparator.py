from module.packages import PackagesByBranch
from module.comparator import Comparator

def test_comparator():
    packages_1 = [
        {
            "name": "test_instance",
            "epoch": 0,
            "version": "1.0.0",
            "release": "alt1",
            "arch": "x86_64"
        }
    ]
    packages_2 = [
        {
            "name": "test_instance",
            "epoch": 0,
            "version": "2.0.0",
            "release": "alt1",
            "arch": "x86_64"
        }
    ]

    packages_3 = [
        {
            "name": "test_instance",
            "epoch": 0,
            "version": "3.0.0",
            "release": "alt1",
            "arch": "x86_64"
        }
    ]

    branch1 = PackagesByBranch(packages_1)
    branch2 = PackagesByBranch(packages_2)
    branch3 = PackagesByBranch(packages_3)

    comparator = Comparator("sisyphus", "p11", branch1, branch2)
    result = comparator.compare()

    assert "x86_64" in result
    assert "newer_in_sisyphus" in result["x86_64"]
    assert len(result["x86_64"]["newer_in_sisyphus"]) == 0

    comparator = Comparator("sisyphus", "p11", branch3, branch2)
    result = comparator.compare()
    assert len(result["x86_64"]["newer_in_sisyphus"]) == 1
