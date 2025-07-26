from module.getter import Getter
from module.packages import Package, PackagesByBranch, BRANCH_1, BRANCH_2
from module.comparator import Comparator
import json

if __name__ == "__main__":
    getter = Getter()

    branch_1 = getter.get_packages(BRANCH_1)["packages"]
    branch_2 = getter.get_packages(BRANCH_2)["packages"]

    branch_packs_1 = PackagesByBranch(branch_1)
    branch_packs_2 = PackagesByBranch(branch_2)

    comparator = Comparator(branch_packs_1, branch_packs_2)

    result = comparator.compare()

    with open("result.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=2, ensure_ascii=False)
 