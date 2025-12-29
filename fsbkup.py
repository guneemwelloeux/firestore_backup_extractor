# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Fsbkup(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(Fsbkup, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.documents = []
        i = 0
        while not self._io.is_eof():
            self.documents.append(Fsbkup.Document(self._io, self, self._root))
            i += 1



    def _fetch_instances(self):
        pass
        for i in range(len(self.documents)):
            pass
            self.documents[i]._fetch_instances()


    class Document(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Fsbkup.Document, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.prefix = self._io.read_bytes(4)
            self.len_data = self._io.read_u2le()
            self.magic = self._io.read_bytes(1)
            if not self.magic == b"\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\x01", self.magic, self._io, u"/types/document/seq/2")
            self.data = self._io.read_bytes(self.len_data)


        def _fetch_instances(self):
            pass



