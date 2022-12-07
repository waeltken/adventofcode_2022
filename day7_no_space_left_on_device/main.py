from anytree import NodeMixin

disk_size = 70000000
least_free_space = 30000000


class File(NodeMixin):
    def __init__(self, name, size, parent=None):
        super(File).__init__()
        self.name = name
        self.size = size
        self.parent = parent

    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name and self.size == __o.size

    def __repr__(self):
        return f"{self.size} {self.name})"


class Folder(NodeMixin):
    def __init__(self, name, children=None):
        super(Folder).__init__()
        self.name = name
        if children:
            self.children = children

    def get_subfolder(self, path):
        for child in self.children:
            if child.name == path and isinstance(child, Folder):
                return child

    def add(self, child):
        self.children = self.children + (child,)

    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name and self.children == __o.children

    def __repr__(self):
        return f"Folder(/{self.name}, {self.children})"

    def _get_size(self):
        return sum(child.size for child in self.children)

    def _get_free_space(self):
        return disk_size - self.size

    def get_smallest_subfolder_to_free_enough_space(self):
        folders = [
            descendant for descendant in self.descendants if not descendant.is_leaf
        ]
        folders = sorted(folders, key=lambda folder: folder.size)
        space_needed = least_free_space - self.free_space
        smallest_option = next(
            (folder for folder in folders if folder.size > space_needed), None
        )
        return smallest_option

    size = property(_get_size)
    free_space = property(_get_free_space)


def parse(input: str) -> Folder:
    root = Folder("")
    current_folder = root
    for line in input.splitlines():
        if line.startswith("$ cd "):
            path = line[5:]
            if path == "/":
                current_folder = root
            elif path == "..":
                current_folder = current_folder.parent
            else:
                current_folder = current_folder.get_subfolder(path)
        elif line.startswith("$ ls"):
            pass
        else:
            size, name = line.split(" ")
            if size == "dir":
                current_folder.add(Folder(name))
            else:
                current_folder.add(File(name, int(size)))
    return root


def read_input():
    with open("./day7_no_space_left_on_device/input.txt") as f:
        return f.read()


def folders_smaller_than(root, size=100000):
    return [node for node in root.descendants if node.size < size and not node.is_leaf]


def main():
    root = parse(read_input())
    print(sum([node.size for node in folders_smaller_than(root)]))
    print(root.get_smallest_subfolder_to_free_enough_space().size)


if __name__ == "__main__":
    main()
