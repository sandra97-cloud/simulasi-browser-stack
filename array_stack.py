class ArrayStack:
    """Implementasi Stack menggunakan Array (List Python)."""

    def __init__(self):
        self.data = []

    def push(self, item):
        """Menambahkan data ke bagian atas Stack."""
        self.data.append(item)

    def pop(self):
        """Mengambil dan menghapus data paling atas."""
        if self.is_empty():
            return None
        return self.data.pop()

    def peek(self):
        """Melihat data paling atas tanpa menghapusnya."""
        if self.is_empty():
            return None
        return self.data[-1]

    def is_empty(self):
        """Memeriksa apakah Stack kosong."""
        return len(self.data) == 0

    def size(self):
        """Menghitung jumlah data dalam Stack."""
        return len(self.data)

    def display(self):
        """Menampilkan seluruh isi Stack."""
        return self.data.copy()
