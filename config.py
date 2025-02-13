# --------------------- Add dữ liệu bảng CayXang ------------------
from models import db, CayXang, GiaNhienLieu
from app import app 
from datetime import datetime
from app import app, db, GiaNhienLieu


# # Dữ liệu mẫu cho 10 cây xăng quanh Hà Nội, cập nhật thêm trường DichVu
# data = [
#     CayXang(MaCayXang='CX001', TenCayXang='Cây Xăng Nam Trung Yên', DiaChi='Số 1, Nam Trung Yên, Cầu Giấy', ThanhPho='Hà Nội', ViDo=21.018582, KinhDo=105.785291, TrangThaiHoatDong=True, TongNhienLieu=5000, NhienLieuTieuThu=1200, DichVu='Rửa xe, Bơm lốp, Cung cấp nước uống'),
#     CayXang(MaCayXang='CX002', TenCayXang='Cây Xăng Giảng Võ', DiaChi='Số 95, Giảng Võ, Ba Đình', ThanhPho='Hà Nội', ViDo=21.026191, KinhDo=105.827790, TrangThaiHoatDong=True, TongNhienLieu=4000, NhienLieuTieuThu=900, DichVu='Bơm lốp, Chữa xe máy'),
#     CayXang(MaCayXang='CX003', TenCayXang='Cây Xăng Phan Đình Phùng', DiaChi='Số 50, Phan Đình Phùng, Ba Đình', ThanhPho='Hà Nội', ViDo=21.035883, KinhDo=105.837213, TrangThaiHoatDong=True, TongNhienLieu=6000, NhienLieuTieuThu=1500, DichVu='Rửa xe, Chữa xe ô tô, Cung cấp nước uống'),
#     CayXang(MaCayXang='CX004', TenCayXang='Cây Xăng Nguyễn Chí Thanh', DiaChi='Số 200, Nguyễn Chí Thanh, Đống Đa', ThanhPho='Hà Nội', ViDo=21.022495, KinhDo=105.823952, TrangThaiHoatDong=True, TongNhienLieu=7000, NhienLieuTieuThu=1800, DichVu='Bơm lốp, Chữa xe máy'),
#     CayXang(MaCayXang='CX005', TenCayXang='Cây Xăng Láng', DiaChi='Số 45, Láng, Đống Đa', ThanhPho='Hà Nội', ViDo=21.012564, KinhDo=105.815415, TrangThaiHoatDong=True, TongNhienLieu=5500, NhienLieuTieuThu=1300, DichVu='Rửa xe, Bơm lốp'),
#     CayXang(MaCayXang='CX006', TenCayXang='Cây Xăng Thái Hà', DiaChi='Số 82, Thái Hà, Đống Đa', ThanhPho='Hà Nội', ViDo=21.017567, KinhDo=105.822470, TrangThaiHoatDong=True, TongNhienLieu=4500, NhienLieuTieuThu=1100, DichVu='Chữa xe máy, Cung cấp nước uống'),
#     CayXang(MaCayXang='CX007', TenCayXang='Cây Xăng Mỹ Đình', DiaChi='Mỹ Đình, Nam Từ Liêm', ThanhPho='Hà Nội', ViDo=21.031293, KinhDo=105.803177, TrangThaiHoatDong=True, TongNhienLieu=4000, NhienLieuTieuThu=950, DichVu='Bơm lốp, Rửa xe'),
#     CayXang(MaCayXang='CX008', TenCayXang='Cây Xăng Cầu Giấy', DiaChi='Cầu Giấy, Hà Nội', ThanhPho='Hà Nội', ViDo=21.033293, KinhDo=105.791122, TrangThaiHoatDong=True, TongNhienLieu=4800, NhienLieuTieuThu=1200, DichVu='Rửa xe, Cung cấp nước uống'),
#     CayXang(MaCayXang='CX009', TenCayXang='Cây Xăng Tố Hữu', DiaChi='Số 25, Tố Hữu, Nam Từ Liêm', ThanhPho='Hà Nội', ViDo=21.009373, KinhDo=105.776678, TrangThaiHoatDong=True, TongNhienLieu=5100, NhienLieuTieuThu=1400, DichVu='Bơm lốp, Chữa xe ô tô'),
#     CayXang(MaCayXang='CX010', TenCayXang='Cây Xăng Kim Mã', DiaChi='Số 70, Kim Mã, Ba Đình', ThanhPho='Hà Nội', ViDo=21.027743, KinhDo=105.814984, TrangThaiHoatDong=True, TongNhienLieu=6200, NhienLieuTieuThu=1600, DichVu='Rửa xe, Bơm lốp, Cung cấp nước uống'),
#     CayXang(MaCayXang='CX011', TenCayXang='Cây Xăng Hoàng Mai', DiaChi='Số 120, Hoàng Mai, Hoàng Mai', ThanhPho='Hà Nội', ViDo=20.987645, KinhDo=105.847138, TrangThaiHoatDong=True, TongNhienLieu=5300, NhienLieuTieuThu=1300, DichVu='Rửa xe, Chữa xe máy'),
#     CayXang(MaCayXang='CX012', TenCayXang='Cây Xăng Hà Đông', DiaChi='Số 15, Quang Trung, Hà Đông', ThanhPho='Hà Nội', ViDo=20.971532, KinhDo=105.777764, TrangThaiHoatDong=True, TongNhienLieu=6000, NhienLieuTieuThu=1450, DichVu='Bơm lốp, Cung cấp nước uống'),
#     CayXang(MaCayXang='CX013', TenCayXang='Cây Xăng Long Biên', DiaChi='Số 42, Ngọc Lâm, Long Biên', ThanhPho='Hà Nội', ViDo=21.048574, KinhDo=105.880048, TrangThaiHoatDong=True, TongNhienLieu=5800, NhienLieuTieuThu=1250, DichVu='Rửa xe, Bơm lốp, Chữa xe ô tô'),
#     CayXang(MaCayXang='CX014', TenCayXang='Cây Xăng Tây Hồ', DiaChi='Số 10, Lạc Long Quân, Tây Hồ', ThanhPho='Hà Nội', ViDo=21.072847, KinhDo=105.811964, TrangThaiHoatDong=True, TongNhienLieu=4700, NhienLieuTieuThu=1150, DichVu='Rửa xe, Chữa xe máy, Cung cấp nước uống'),
#     CayXang(MaCayXang='CX015', TenCayXang='Cây Xăng Thanh Xuân', DiaChi='Số 35, Nguyễn Trãi, Thanh Xuân', ThanhPho='Hà Nội', ViDo=20.993852, KinhDo=105.812856, TrangThaiHoatDong=True, TongNhienLieu=5200, NhienLieuTieuThu=1400, DichVu='Bơm lốp, Rửa xe'),
#     CayXang(MaCayXang='CX016', TenCayXang='Cây Xăng Gia Lâm', DiaChi='Số 5, Trâu Quỳ, Gia Lâm', ThanhPho='Hà Nội', ViDo=21.005487, KinhDo=105.935874, TrangThaiHoatDong=True, TongNhienLieu=4500, NhienLieuTieuThu=1200, DichVu='Cung cấp nước uống, Rửa xe'),
#     CayXang(MaCayXang='CX017', TenCayXang='Cây Xăng Trường Chinh', DiaChi='Số 78, Trường Chinh, Đống Đa', ThanhPho='Hà Nội', ViDo=21.003194, KinhDo=105.828153, TrangThaiHoatDong=True, TongNhienLieu=4900, NhienLieuTieuThu=1300, DichVu='Rửa xe, Chữa xe máy'),
#     CayXang(MaCayXang='CX018', TenCayXang='Cây Xăng Lê Văn Lương', DiaChi='Số 150, Lê Văn Lương, Thanh Xuân', ThanhPho='Hà Nội', ViDo=20.989867, KinhDo=105.796784, TrangThaiHoatDong=True, TongNhienLieu=5600, NhienLieuTieuThu=1450, DichVu='Rửa xe, Bơm lốp, Chữa xe ô tô'),
#     CayXang(MaCayXang='CX019', TenCayXang='Cây Xăng Yên Phụ', DiaChi='Số 18, Yên Phụ, Tây Hồ', ThanhPho='Hà Nội', ViDo=21.048924, KinhDo=105.836097, TrangThaiHoatDong=True, TongNhienLieu=5100, NhienLieuTieuThu=1350, DichVu='Bơm lốp, Rửa xe'),
#     CayXang(MaCayXang='CX020', TenCayXang='Cây Xăng Phú Thượng', DiaChi='Số 65, Phú Thượng, Tây Hồ', ThanhPho='Hà Nội', ViDo=21.082347, KinhDo=105.812134, TrangThaiHoatDong=True, TongNhienLieu=5000, NhienLieuTieuThu=1200, DichVu='Cung cấp nước uống, Rửa xe'),

# ]

# # Lưu dữ liệu vào cơ sở dữ liệu
# with app.app_context():
#     db.session.bulk_save_objects(data)
#     db.session.commit()
#     print("Dữ liệu đã được thêm thành công!")

# -------------- Add dữ liệu bảng NguoiDung -----------------------
# from werkzeug.security import generate_password_hash
# from app import app
# from models import db, NguoiDung

# # Xóa bảng
# with app.app_context():
#     db.drop_all()  # Xóa tất cả các bảng

# # Tạo lại bảng
# with app.app_context():
#     db.create_all()  # Tạo lại các bảng

# # Tạo danh sách người dùng mới với tên đăng nhập và mật khẩu giống nhau
# users = [
#     NguoiDung(TenDangNhap="admin1", MatKhau="admin1", VaiTro="Admin", Email="admin1@example.com", SoDienThoai="0123456789"),
#     NguoiDung(TenDangNhap="admin2", MatKhau="admin2", VaiTro="Admin", Email="admin2@example.com", SoDienThoai="0123456790"),
#     NguoiDung(TenDangNhap="admin3", MatKhau="admin3", VaiTro="Admin", Email="admin3@example.com", SoDienThoai="0123456791"),
#     NguoiDung(TenDangNhap="user1", MatKhau="user1", VaiTro="user", Email="user1@example.com", SoDienThoai="0123456792"),
#     NguoiDung(TenDangNhap="user2", MatKhau="user2", VaiTro="user", Email="user2@example.com", SoDienThoai="0123456793"),
#     NguoiDung(TenDangNhap="user3", MatKhau="user3", VaiTro="user", Email="user3@example.com", SoDienThoai="0123456794"),
#     NguoiDung(TenDangNhap="user4", MatKhau="user4", VaiTro="user", Email="user4@example.com", SoDienThoai="0123456795"),
#     NguoiDung(TenDangNhap="user5", MatKhau="user5", VaiTro="user", Email="user5@example.com", SoDienThoai="0123456796"),
#     NguoiDung(TenDangNhap="user6", MatKhau="user6", VaiTro="user", Email="user6@example.com", SoDienThoai="0123456797"),
#     NguoiDung(TenDangNhap="user7", MatKhau="user7", VaiTro="user", Email="user7@example.com", SoDienThoai="0123456798"),
#     NguoiDung(TenDangNhap="user8", MatKhau="user8", VaiTro="user", Email="user8@example.com", SoDienThoai="0123456799"),
#     NguoiDung(TenDangNhap="user9", MatKhau="user9", VaiTro="user", Email="user9@example.com", SoDienThoai="0123456800"),
#     NguoiDung(TenDangNhap="user10", MatKhau="user10", VaiTro="user", Email="user10@example.com", SoDienThoai="0123456801")
# ]

# # Cập nhật mật khẩu cho mỗi người dùng bằng cách băm mật khẩu
# for user in users:
#     user.MatKhau = generate_password_hash(user.MatKhau)

# # Thêm người dùng vào cơ sở dữ liệu
# with app.app_context():
#     db.session.bulk_save_objects(data)
#     db.session.commit()
#     print("Dữ liệu đã được thêm thành công!")


from datetime import datetime
from app import app, db, GiaNhienLieu  # Thay `app` bằng tên file Flask của bạn nếu khác

# Dữ liệu đầy đủ cho bảng GiaNhienLieu
gia_nhien_lieu_data = []
gia_xang = [
    {"LoaiNhienLieu": "Xăng RON95", "GiaBan": 24000},
    {"LoaiNhienLieu": "Xăng RON92", "GiaBan": 23000},
    {"LoaiNhienLieu": "Dầu Diesel", "GiaBan": 20000},
]

gia_tang = [0, 100, 200, -100, 50, -50]  # Giá tăng giảm ngẫu nhiên

# Tạo dữ liệu
ma_gia = 1
for index, ma_cay_xang in enumerate([f"CX{str(i).zfill(3)}" for i in range(1, 21)], start=1):
    for idx, xang in enumerate(gia_xang):
        gia_nhien_lieu_data.append({
            "MaGia": ma_gia,
            "MaCayXang": ma_cay_xang,
            "LoaiNhienLieu": xang["LoaiNhienLieu"],
            "GiaBan": xang["GiaBan"] + gia_tang[(index + idx) % len(gia_tang)],
            "NgayHieuLuc": datetime(2024, 12, 9)
        })
        ma_gia += 1

# Thực hiện thêm dữ liệu vào database
with app.app_context():  # Mở application context
    for item in gia_nhien_lieu_data:
        gia_nhien_lieu = GiaNhienLieu(**item)  # Tạo đối tượng
        db.session.add(gia_nhien_lieu)         # Thêm vào session

    db.session.commit()  # Lưu vào database
print("Dữ liệu đã được thêm thành công!")
