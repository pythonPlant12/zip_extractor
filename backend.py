import zipfile


def extractor_archive(archivepath, destination_directory):
    with zipfile.ZipFile(archivepath, "r") as archive:
        archive.extractall(destination_directory)

# if __name__ == "__main__":
#   extractor_archive()
