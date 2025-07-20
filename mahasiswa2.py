import sys
import sqlite3
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QFormLayout, QLabel, QLineEdit, QPushButton, 
                           QTableWidget, QTableWidgetItem, QMessageBox, QHeaderView)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class MahasiswaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_database()
        self.init_ui()
        self.load_data()
    
    def init_database(self):
        """Inisialisasi database SQLite"""
        self.conn = sqlite3.connect('mahasiswa.db')
        self.cursor = self.conn.cursor()
        
        # Membuat tabel mahasiswa jika belum ada
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS mahasiswa (
                npm TEXT PRIMARY KEY,
                nama_lengkap TEXT NOT NULL,
                nama_panggilan TEXT,
                telepon TEXT,
                email TEXT,
                kelas TEXT,
                matakuliah TEXT,
                lokasi_kampus TEXT
            )
        ''')
        self.conn.commit()
    
    def init_ui(self):
        """Inisialisasi User Interface"""
        self.setWindowTitle('MainWindow - untitled.ui*')
        self.setGeometry(100, 100, 600, 500)
        
        # Set style yang mirip dengan contoh
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                font-weight: bold;
                color: #333;
            }
            QLineEdit {
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 3px;
                background: white;
            }
            QLineEdit:focus {
                border: 2px solid #0078d4;
            }
        """)
        
        # Widget utama
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout utama
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)
        
        # Title
        title_label = QLabel('MAHASISWA')
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: white;
                background-color: #4a90e2;
                padding: 10px;
                border-radius: 5px;
            }
        """)
        main_layout.addWidget(title_label)
        
        # Form layout
        form_layout = QFormLayout()
        form_layout.setSpacing(8)
        
        # Input fields sesuai contoh
        self.npm_input = QLineEdit()
        self.nama_lengkap_input = QLineEdit()
        self.nama_panggilan_input = QLineEdit()
        self.telepon_input = QLineEdit()
        self.email_input = QLineEdit()
        self.kelas_input = QLineEdit()
        self.matakuliah_input = QLineEdit()
        self.lokasi_kampus_input = QLineEdit()
        
        # Tambahkan ke form layout
        form_layout.addRow(QLabel('NPM'), self.npm_input)
        form_layout.addRow(QLabel('NAMA LENGKAP'), self.nama_lengkap_input)
        form_layout.addRow(QLabel('NAMA PANGGILAN'), self.nama_panggilan_input)
        form_layout.addRow(QLabel('TELEPON'), self.telepon_input)
        form_layout.addRow(QLabel('EMAIL'), self.email_input)
        form_layout.addRow(QLabel('KELAS'), self.kelas_input)
        form_layout.addRow(QLabel('MATAKULIAH'), self.matakuliah_input)
        form_layout.addRow(QLabel('LOKASI KAMPUS'), self.lokasi_kampus_input)
        
        main_layout.addLayout(form_layout)
        
        # Buttons layout
        button_layout = QHBoxLayout()
        
        # Tombol sesuai contoh dengan warna
        self.btn_tambah = QPushButton('TAMBAH')
        self.btn_ubah = QPushButton('UBAH')
        self.btn_hapus = QPushButton('HAPUS')
        self.btn_batal = QPushButton('BATAL')
        
        # Style tombol dengan warna
        self.btn_tambah.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                border: none;
                padding: 8px 15px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        
        self.btn_ubah.setStyleSheet("""
            QPushButton {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 8px 15px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        
        self.btn_hapus.setStyleSheet("""
            QPushButton {
                background-color: #dc3545;
                color: white;
                border: none;
                padding: 8px 15px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
        """)
        
        self.btn_batal.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border: none;
                padding: 8px 15px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #545b62;
            }
        """)
        
        # Connect button signals
        self.btn_tambah.clicked.connect(self.tambah_data)
        self.btn_ubah.clicked.connect(self.ubah_data)
        self.btn_hapus.clicked.connect(self.hapus_data)
        self.btn_batal.clicked.connect(self.batal)
        
        # Tambahkan tombol ke layout
        button_layout.addWidget(self.btn_tambah)
        button_layout.addWidget(self.btn_ubah)
        button_layout.addWidget(self.btn_hapus)
        button_layout.addWidget(self.btn_batal)
        
        main_layout.addLayout(button_layout)
        
        # Table untuk menampilkan data
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            'NPM', 'NAMA LENGKAP', 'NAMA PANGGILAN', 'TELEPON',
            'EMAIL', 'KELAS', 'MATAKULIAH', 'LOKASI KAMPUS'
        ])
        
        # Table styling
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: white;
                gridline-color: #ddd;
                selection-background-color: #e6f3ff;
            }
            QHeaderView::section {
                background-color: #f8f9fa;
                padding: 5px;
                border: 1px solid #ddd;
                font-weight: bold;
            }
        """)
        
        # Set table properties
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.cellClicked.connect(self.on_table_click)
        
        main_layout.addWidget(self.table)
    
    def load_data(self):
        """Memuat data dari database ke tabel"""
        self.cursor.execute('SELECT * FROM mahasiswa')
        data = self.cursor.fetchall()
        
        self.table.setRowCount(len(data))
        
        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                item = QTableWidgetItem(str(value) if value else '')
                self.table.setItem(row_idx, col_idx, item)
    
    def on_table_click(self, row, column):
        """Handle klik pada tabel untuk mengisi form"""
        self.npm_input.setText(self.table.item(row, 0).text() if self.table.item(row, 0) else '')
        self.nama_lengkap_input.setText(self.table.item(row, 1).text() if self.table.item(row, 1) else '')
        self.nama_panggilan_input.setText(self.table.item(row, 2).text() if self.table.item(row, 2) else '')
        self.telepon_input.setText(self.table.item(row, 3).text() if self.table.item(row, 3) else '')
        self.email_input.setText(self.table.item(row, 4).text() if self.table.item(row, 4) else '')
        self.kelas_input.setText(self.table.item(row, 5).text() if self.table.item(row, 5) else '')
        self.matakuliah_input.setText(self.table.item(row, 6).text() if self.table.item(row, 6) else '')
        self.lokasi_kampus_input.setText(self.table.item(row, 7).text() if self.table.item(row, 7) else '')
    
    def get_form_data(self):
        """Mengambil data dari form"""
        return {
            'npm': self.npm_input.text().strip(),
            'nama_lengkap': self.nama_lengkap_input.text().strip(),
            'nama_panggilan': self.nama_panggilan_input.text().strip(),
            'telepon': self.telepon_input.text().strip(),
            'email': self.email_input.text().strip(),
            'kelas': self.kelas_input.text().strip(),
            'matakuliah': self.matakuliah_input.text().strip(),
            'lokasi_kampus': self.lokasi_kampus_input.text().strip()
        }
    
    def clear_form(self):
        """Membersihkan form"""
        self.npm_input.clear()
        self.nama_lengkap_input.clear()
        self.nama_panggilan_input.clear()
        self.telepon_input.clear()
        self.email_input.clear()
        self.kelas_input.clear()
        self.matakuliah_input.clear()
        self.lokasi_kampus_input.clear()
    
    def tambah_data(self):
        """Menambah data baru"""
        data = self.get_form_data()
        
        if not data['npm']:
            QMessageBox.warning(self, 'Peringatan', 'NPM harus diisi!')
            return
        
        if not data['nama_lengkap']:
            QMessageBox.warning(self, 'Peringatan', 'Nama lengkap harus diisi!')
            return
        
        try:
            self.cursor.execute('''
                INSERT INTO mahasiswa 
                (npm, nama_lengkap, nama_panggilan, telepon, email, kelas, matakuliah, lokasi_kampus)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', tuple(data.values()))
            
            self.conn.commit()
            self.load_data()
            self.clear_form()
            QMessageBox.information(self, 'Sukses', 'Data berhasil ditambahkan!')
            
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, 'Error', 'NPM sudah ada dalam database!')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Terjadi kesalahan: {str(e)}')
    
    def ubah_data(self):
        """Mengubah data yang sudah ada"""
        data = self.get_form_data()
        
        if not data['npm']:
            QMessageBox.warning(self, 'Peringatan', 'Pilih data yang akan diubah!')
            return
        
        try:
            self.cursor.execute('''
                UPDATE mahasiswa SET 
                nama_lengkap=?, nama_panggilan=?, telepon=?, email=?, 
                kelas=?, matakuliah=?, lokasi_kampus=?
                WHERE npm=?
            ''', (data['nama_lengkap'], data['nama_panggilan'], data['telepon'],
                  data['email'], data['kelas'], data['matakuliah'], 
                  data['lokasi_kampus'], data['npm']))
            
            if self.cursor.rowcount > 0:
                self.conn.commit()
                self.load_data()
                self.clear_form()
                QMessageBox.information(self, 'Sukses', 'Data berhasil diubah!')
            else:
                QMessageBox.warning(self, 'Peringatan', 'Data tidak ditemukan!')
                
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Terjadi kesalahan: {str(e)}')
    
    def hapus_data(self):
        """Menghapus data"""
        npm = self.npm_input.text().strip()
        
        if not npm:
            QMessageBox.warning(self, 'Peringatan', 'Pilih data yang akan dihapus!')
            return
        
        reply = QMessageBox.question(self, 'Konfirmasi', 
                                   f'Yakin ingin menghapus data NPM {npm}?',
                                   QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            try:
                self.cursor.execute('DELETE FROM mahasiswa WHERE npm=?', (npm,))
                
                if self.cursor.rowcount > 0:
                    self.conn.commit()
                    self.load_data()
                    self.clear_form()
                    QMessageBox.information(self, 'Sukses', 'Data berhasil dihapus!')
                else:
                    QMessageBox.warning(self, 'Peringatan', 'Data tidak ditemukan!')
                    
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Terjadi kesalahan: {str(e)}')
    
    def batal(self):
        """Membersihkan form"""
        self.clear_form()
    
    def closeEvent(self, event):
        """Handle penutupan aplikasi"""
        self.conn.close()
        event.accept()

def main():
    app = QApplication(sys.argv)
    window = MahasiswaApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()