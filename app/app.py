from PIL import Image
import os


class Application:
    max_size = (1920, 1080)
    ignored_exts: list[str] = [".DS_Store"]

    def run(self, args: list[str]) -> None:
        if len(args) == 1:
            base_path = args[0]
        else:
            base_path = os.getcwd()

        files = os.listdir(base_path)
        for file in files:
            full_path = os.path.join(base_path, file)

            if os.path.isdir(full_path):
                continue

            if self.is_ignored_file(full_path):
                print("[Skipping] ", full_path)
                continue

            image = Image.open(full_path)
            image = image.resize(self.max_size)

            out_dir = os.path.join(base_path, "out")
            if not os.path.exists(out_dir):
                os.makedirs(out_dir)

            out_path = os.path.join(out_dir, self.get_filename(file, "jpg"))
            print("[Done] ", out_path)
            image.save(out_path, optimize=True, quality=95)

    def is_ignored_file(self, path: str) -> bool:
        for ignored_ext in self.ignored_exts:
            if path.endswith(ignored_ext):
                return True

        return False

    def get_filename(self, file: str, ext: str) -> str:
        pieces = file.split(".")
        if len(pieces) != 2:
            return f"{file}.{ext}"

        return f"{pieces[0]}.{ext}"
