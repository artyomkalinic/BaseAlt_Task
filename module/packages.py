from collections import defaultdict
import rpm

BRANCH_1 = "sisyphus"
BRANCH_2 = "p11"


class Package():
    def __init__(self, name, epoch, version, release, arch):
        self.name = name
        self.epoch = epoch
        self.version = version
        self.release = release
        self.arch = arch

    def get_info(self):
        return f"{self.epoch}:{self.version}-{self.release}"
        
    def __repr__(self):
        return f"{self.name}-{self.epoch}:{self.version}-{self.release}.{self.arch}"


class PackagesByBranch():
    def __init__(self, branch_packages):
        self.packages = defaultdict(dict)
        for pack in branch_packages:
            pack_temp = Package(
                name=pack["name"],
                epoch=pack["epoch"],
                version=pack["version"],
                release=pack["release"],
                arch=pack["arch"]
            )
            self.packages[pack_temp.arch][pack_temp.name] = pack_temp
