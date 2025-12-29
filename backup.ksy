meta:
  id: fsbkup
  file-extension: Firestorebackup

seq:
  - id: documents
    type: document
    repeat: eos
types:
  document:
   seq:
    - id: prefix
      size: 4
    - id: len_data
      type: u2le
    - id: magic
      contents: [0x01]
    - id: data
      size: len_data
