import json
from module.packages import Package, PackagesByBranch

def test_packages():
    with open("tests/test_package.json", "r", encoding="utf-8") as file:
        packages = json.load(file)
        packs_by_branch = PackagesByBranch(packages)
    
        assert "x86_64" in packs_by_branch.packages
        assert "test_instance_1" in packs_by_branch.packages["x86_64"]
        assert isinstance(packs_by_branch.packages["x86_64"]["test_instance_1"], Package)