class Libccd(Product):
    def __init__(self):
        Product.__init__()
        self.homepage = "http://libccd.danfis.cz"
        self.url = "http://libccd.danfis.cz/files/libccd-2.0.tar.gz"
        self.sha256 = "513e212fbb22cf720cf16ba911e8a8ccb1050c006789631ff2474ecc2f12b47a"
        self.head = "https://github.com/danfis/libccd.git"

    def install(self):
        os.system("cmake .")
        os.system("cmake --build .")

