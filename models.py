from flask_sqlalchemy import SQLAlchemy

# Khởi tạo SQLAlchemy
db = SQLAlchemy()

# Định nghĩa bảng CayXang
class CayXang(db.Model):
    __tablename__ = 'cayxang'
    MaCayXang = db.Column(db.String(50), primary_key=True)  
    TenCayXang = db.Column(db.String(100), nullable=False)
    DiaChi = db.Column(db.String(255), nullable=False)
    ThanhPho = db.Column(db.String(100), nullable=False)
    ViDo = db.Column(db.Float, nullable=False)
    KinhDo = db.Column(db.Float, nullable=False)
    TrangThaiHoatDong = db.Column(db.Boolean, default=True)  
    TongNhienLieu = db.Column(db.Float, default=0)
    NhienLieuTieuThu = db.Column(db.Float, default=0)
    DichVu = db.Column(db.Text, nullable=True)
    
# Định nghĩa bảng GiaNhienLieu
class GiaNhienLieu(db.Model):
    __tablename__ = "gianhienlieu"
    MaGia = db.Column(db.Integer, primary_key=True)
    MaCayXang = db.Column(db.String(50), db.ForeignKey('cayxang.MaCayXang', ondelete='CASCADE'))  
    LoaiNhienLieu = db.Column(db.String(50), nullable=False)
    GiaBan = db.Column(db.Float, nullable=False)
    NgayHieuLuc = db.Column(db.DateTime, nullable=False)


# Định nghĩa bảng NguoiDung
class NguoiDung(db.Model):
    __tablename__ = "nguoidung"
    MaNguoiDung = db.Column(db.Integer, primary_key=True, autoincrement=True)
    TenDangNhap = db.Column(db.String(50), unique=True, nullable=False)
    MatKhau = db.Column(db.String(255), nullable=False)
    VaiTro = db.Column(db.String(20), nullable=False)
    Email = db.Column(db.String(100), unique=True, nullable=False)
    SoDienThoai = db.Column(db.String(20))
    TrangThai = db.Column(db.Boolean, default=True)

# Định nghĩa bảng DanhGia
class DanhGia(db.Model):
    __tablename__ = 'danhgia'
    MaDanhGia = db.Column(db.Integer, primary_key=True)
    MaCayXang = db.Column(db.String(50), db.ForeignKey('cayxang.MaCayXang', ondelete='CASCADE'))
    MaNguoiDung = db.Column(db.Integer, db.ForeignKey('nguoidung.MaNguoiDung', ondelete='SET NULL'))
    DiemDanhGia = db.Column(db.Integer, nullable=False)
    BinhLuan = db.Column(db.Text)
    NgayDanhGia = db.Column(db.DateTime, nullable=False)


# Định nghĩa bảng BaoCao
class BaoCao(db.Model):
    __tablename__ = "baocao"
    MaBaoCao = db.Column(db.Integer, primary_key=True)
    MaCayXang = db.Column(db.String(50), db.ForeignKey('cayxang.MaCayXang', ondelete='CASCADE'))  
    LoaiBaoCao = db.Column(db.String(50), nullable=False)
    DuLieuBaoCao = db.Column(db.Text)
    NgayTaoBaoCao = db.Column(db.DateTime, default=db.func.now(), nullable=False)
