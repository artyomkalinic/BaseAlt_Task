from module.getter import Getter
from module.packages import Package, PackagesByBranch
from module.comparator import Comparator
import json
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--branch1", required=True)
    parser.add_argument("--branch2", required=True)
    parser.add_argument("--output", required=True, default="result.json")

    args = parser.parse_args()

    getter = Getter()

    branch_1 = getter.get_packages(args.branch1)["packages"]
    branch_2 = getter.get_packages(args.branch2)["packages"]
    
    branch_packs_1 = PackagesByBranch(branch_1)
    branch_packs_2 = PackagesByBranch(branch_2)

    comparator = Comparator(args.branch1, args.branch2, branch_packs_1, branch_packs_2)

    result = comparator.compare()

    with open("result.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=2, ensure_ascii=False)
