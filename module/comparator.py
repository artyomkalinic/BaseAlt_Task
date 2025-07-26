from rpm_vercmp import vercmp
from module.packages import PackagesByBranch, BRANCH_1, BRANCH_2

class Comparator():
    def __init__(self, branch1: PackagesByBranch, branch2: PackagesByBranch):
        self.branch1 = branch1
        self.branch2 = branch2
    
    def compare(self):
        res = {}

        for arch in self.branch1.packages:
            branch1_pkgs = self.branch1.packages.get(arch, {})
            branch2_pkgs = self.branch2.packages.get(arch, {})

            only_in_1 = []
            only_in_2 = []
            newer_in_1 = []

            all_names = set(branch1_pkgs.keys()) | set(branch2_pkgs.keys())

            for name in all_names:
                pkg_1 = branch1_pkgs.get(name)
                pkg_2 = branch2_pkgs.get(name)


                if pkg_1 and not pkg_2:
                    only_in_1.append(pkg_1.__repr__())
                elif pkg_2 and not pkg_1:
                    only_in_2.append(pkg_2.__repr__())
                else:
                    ver_1 = pkg_1.get_info()
                    ver_2 = pkg_2.get_info()

                    if vercmp(ver_1, ver_2) > 0:
                        newer_in_1.append(pkg_1.__repr__())

            res[arch] = {
                f"only_in_{BRANCH_1}": only_in_1,
                f"only_in_{BRANCH_2}": only_in_2,
                f"newer_in_{BRANCH_1}": newer_in_1
            }

        return res