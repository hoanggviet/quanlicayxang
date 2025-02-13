from flask import Flask, render_template, request, redirect, url_for, jsonify, Response, session, flash
from flask_bcrypt import Bcrypt
from models import db, NguoiDung, DanhGia, CayXang, GiaNhienLieu, BaoCao
from datetime import datetime

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Cấu hình Flask
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:2003@localhost:5432/QLCayXang"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "your_secret_key_here"  # Thay bằng khóa bí mật thực tế
hashed_password = bcrypt.generate_password_hash('mat_khau_cua_user').decode('utf-8')
db.init_app(app)


@app.route("/")
def home():
    """
    Trang chính hiển thị bản đồ và điều hướng giữa các chức năng
    """
    logged_in = "ten_dang_nhap" in session
    return render_template("index.html", logged_in=logged_in)

# Hàm đăng nhập
@app.route('/dang_nhap', methods=['GET', 'POST'])
def dang_nhap():
    if request.method == 'POST':
        ten_dang_nhap = request.form['ten_dang_nhap']
        mat_khau = request.form['mat_khau']
        nguoi_dung = NguoiDung.query.filter_by(TenDangNhap=ten_dang_nhap).first()

        # Kiểm tra thông tin người dùng và mật khẩu
        if nguoi_dung and bcrypt.check_password_hash(nguoi_dung.MatKhau, mat_khau):
            session['ten_dang_nhap'] = ten_dang_nhap  # Lưu tên đăng nhập vào session

            # Kiểm tra vai trò của người dùng
            if nguoi_dung.VaiTro == 'Admin':
                flash('Đăng nhập thành công! Chào mừng quản trị viên.', 'success')
                return redirect(url_for("quan_ly_cay_xang"))
            else:
                flash('Đăng nhập thành công! Chào mừng người dùng.', 'success')
                return redirect(url_for("ban_do"))
        else:
            flash('Tên đăng nhập hoặc mật khẩu không đúng.', 'danger')

    return render_template('dang_nhap.html')

# Hàm đăng ký
@app.route('/dang_ky', methods=['GET', 'POST'])
def dang_ky():
    if request.method == 'POST':
        ten_dang_nhap = request.form['ten_dang_nhap']
        mat_khau = request.form['mat_khau']
        mat_khau_hash = bcrypt.generate_password_hash(mat_khau).decode('utf-8')

        email = request.form['email']
        
        if not email:
            flash("Email không được để trống.", "danger")
            return redirect(url_for("dang_ky"))

        vai_tro = 'user'

        new_user = NguoiDung(
            TenDangNhap=ten_dang_nhap,
            MatKhau=mat_khau_hash,
            VaiTro=vai_tro,
            Email=email,
            SoDienThoai=request.form['so_dien_thoai']
        )

        db.session.add(new_user)
        db.session.commit()

        flash('Đăng ký thành công! Bạn có thể đăng nhập.', 'success')
        return redirect(url_for("home"))

    return render_template('dang_ky.html')

# Hàm đăng xuất
@app.route('/dang_xuat')
def dang_xuat():
    session.pop('ten_dang_nhap', None)
    flash('Đăng xuất thành công!', 'success')
    return redirect(url_for('home'))

# Route bản đồ
@app.route('/ban_do')
def ban_do():
    # Lấy thông tin cây xăng từ cơ sở dữ liệu
    cay_xang = CayXang.query.all()  # Lấy tất cả cây xăng từ cơ sở dữ liệu
    
    # Truyền dữ liệu vào template
    return render_template('ban_do.html', cay_xang=cay_xang)

# API trả về cây xăng
@app.route("/api/cayxang")
def api_cayxang():
    danh_sach_cay_xang = CayXang.query.all()
    data = []

    
    for cx in danh_sach_cay_xang:
        data.append({
            "TenCayXang": cx.TenCayXang,
            "DiaChi": cx.DiaChi,
            "ViDo": cx.ViDo,
            "KinhDo": cx.KinhDo,
            "TrangThaiHoatDong": cx.TrangThaiHoatDong,
            "DichVu": cx.DichVu
            
        })

    return jsonify(data)



# ---------------------------------------------------------------------------------------
# 3.1 Quản lý người dùng

# Quản lý người dùng
@app.route("/quan_ly_nguoi_dung", methods=["GET"])
def quan_ly_nguoi_dung():
    vai_tro = request.args.get("vai_tro", "")
    ten_nguoi_dung = request.args.get("ten_nguoi_dung", "")
    query = NguoiDung.query
    if vai_tro:
        query = query.filter_by(VaiTro=vai_tro)
    if ten_nguoi_dung:
        query = query.filter(NguoiDung.TenDangNhap.ilike(f"%{ten_nguoi_dung}%"))

    danh_sach_nguoi_dung = query.all()

    return render_template("admin/quan_ly_nguoi_dung.html", danh_sach_nguoi_dung=danh_sach_nguoi_dung, vai_tro=vai_tro, ten_nguoi_dung=ten_nguoi_dung)

# Thêm người dùng
@app.route("/them_nguoi_dung", methods=["GET", "POST"])
def them_nguoi_dung():
    if request.method == "POST":
        ma_nguoi_dung = request.form.get("ma_nguoi_dung")
        ten_dang_nhap = request.form.get("ten_dang_nhap")
        mat_khau = request.form.get("mat_khau")
        vai_tro = request.form.get("vai_tro")
        email = request.form.get("email")
        so_dien_thoai = request.form.get("so_dien_thoai")

        nguoi_dung = NguoiDung(TenDangNhap=ten_dang_nhap, MatKhau=mat_khau, VaiTro=vai_tro, Email=email, SoDienThoai=so_dien_thoai)
        db.session.add(nguoi_dung)
        db.session.commit()
        return redirect(url_for("quan_ly_nguoi_dung"))
    return render_template("admin/them_nguoi_dung.html")

# Hàm sửa thông tin người dùng
@app.route("/sua_nguoi_dung/<string:ma_nguoi_dung>", methods=["GET", "POST"])
def sua_nguoi_dung(ma_nguoi_dung):
    nguoi_dung = NguoiDung.query.get(ma_nguoi_dung)
    if request.method == "POST":
        nguoi_dung.TenDangNhap = request.form.get("ten_dang_nhap")
        
        # Kiểm tra nếu người dùng nhập mật khẩu mới
        if request.form.get("mat_khau"):
            mat_khau = request.form.get("mat_khau")
            nguoi_dung.MatKhau = bcrypt.generate_password_hash(mat_khau).decode('utf-8')  # Mã hóa mật khẩu
        
        nguoi_dung.VaiTro = request.form.get("vai_tro")
        nguoi_dung.Email = request.form.get("email")
        nguoi_dung.SoDienThoai = request.form.get("so_dien_thoai")
        db.session.commit()
        return redirect(url_for("quan_ly_nguoi_dung"))
    return render_template("admin/sua_nguoi_dung.html", nguoi_dung=nguoi_dung)

# Xóa người dùng
@app.route("/xoa_nguoi_dung/<string:ma_nguoi_dung>")
def xoa_nguoi_dung(ma_nguoi_dung):
    nguoi_dung = NguoiDung.query.get(ma_nguoi_dung)
    db.session.delete(nguoi_dung)
    db.session.commit()
    return redirect(url_for("quan_ly_nguoi_dung"))

# Route: Khóa/Mở khóa người dùng
@app.route("/khoa_nguoi_dung/<string:ma_nguoi_dung>")
def khoa_nguoi_dung(ma_nguoi_dung):
    nguoi_dung = NguoiDung.query.get(ma_nguoi_dung)
    if nguoi_dung:
        nguoi_dung.TrangThai = not nguoi_dung.TrangThai
        db.session.commit()
    return redirect(url_for("quan_ly_nguoi_dung"))

# 3.1.2 Quản lý đánh giá và phản hồi

# Hiển thị danh sách đánh giá
@app.route('/quan_ly_danh_gia', methods=['GET', 'POST'])
def quan_ly_danh_gia():
    cay_xang_list = CayXang.query.all()  # Lấy tất cả cây xăng
    ten_cay_xang = None
    danh_gia_list = []

    if request.method == 'POST':
        ma_cay_xang = request.form.get('ma_cay_xang')
        if ma_cay_xang:
            ten_cay_xang = CayXang.query.get(ma_cay_xang).TenCayXang
            danh_gia_list = DanhGia.query.filter_by(MaCayXang=ma_cay_xang).all()  # Lấy đánh giá của cây xăng được chọn

    return render_template('admin/quan_ly_danh_gia.html', 
                           cay_xang_list=cay_xang_list, 
                           ten_cay_xang=ten_cay_xang, 
                           danh_gia_list=danh_gia_list)


# Trả lời đánh giá
@app.route("/tra_loi_danh_gia/<int:ma_danh_gia>", methods=["GET", "POST"])
def tra_loi_danh_gia(ma_danh_gia):
    danh_gia = DanhGia.query.get(ma_danh_gia)
    if request.method == "POST":
        danh_gia.BinhLuan = request.form.get("binh_luan_tra_loi")
        db.session.commit()
        return redirect(url_for("quan_ly_danh_gia"))
    return render_template("admin/tra_loi_danh_gia.html", danh_gia=danh_gia)

# 3.2 Quản lý thông tin hoạt động của cây xăng

# Hiển thị danh sách cây xăng
# Quản lý cây xăng
@app.route("/quan_ly_cay_xang")
def quan_ly_cay_xang():
    danh_sach_cay_xang = CayXang.query.all()
    return render_template("admin/quan_ly_cay_xang.html", danh_sach_cay_xang=danh_sach_cay_xang)

# Thêm cây xăng
@app.route("/them_cay_xang", methods=["GET", "POST"])
def them_cay_xang():
    if request.method == "POST":
        # Lấy dữ liệu từ form
        ma_cay_xang = request.form.get("ma_cay_xang")
        ten_cay_xang = request.form.get("ten_cay_xang")
        dia_chi = request.form.get("dia_chi")
        thanh_pho = request.form.get("thanh_pho")
        vi_do = float(request.form.get("vi_do"))
        kinh_do = float(request.form.get("kinh_do"))
        trang_thai = bool(request.form.get("trang_thai"))

        # Kiểm tra xem mã cây xăng đã tồn tại chưa
        if CayXang.query.filter_by(MaCayXang=ma_cay_xang).first():
            return "Mã cây xăng đã tồn tại. Vui lòng nhập mã cây xăng khác."

        # Thêm cây xăng mới
        cay_xang = CayXang(
            MaCayXang=ma_cay_xang,
            TenCayXang=ten_cay_xang,
            DiaChi=dia_chi,
            ThanhPho=thanh_pho,
            ViDo=vi_do,
            KinhDo=kinh_do,
            TrangThaiHoatDong=trang_thai
        )
        db.session.add(cay_xang)
        db.session.commit()

        return redirect("/quan_ly_cay_xang")

    return render_template("admin/them_cay_xang.html")

# Route xử lý sửa cây xăng
@app.route("/sua_cay_xang/<string:ma_cay_xang>", methods=["GET", "POST"])
def sua_cay_xang(ma_cay_xang):
    cay_xang = CayXang.query.get(ma_cay_xang)
    if request.method == "POST":
        # Lấy dữ liệu từ form
        cay_xang.TenCayXang = request.form.get("ten_cay_xang")
        cay_xang.DiaChi = request.form.get("dia_chi")
        cay_xang.ThanhPho = request.form.get("thanh_pho")
        cay_xang.ViDo = float(request.form.get("vi_do"))
        cay_xang.KinhDo = float(request.form.get("kinh_do"))
        cay_xang.TrangThaiHoatDong = bool(request.form.get("trang_thai"))
        
        # Cập nhật thông tin tổng nhiên liệu và nhiên liệu tiêu thụ nếu có
        cay_xang.TongNhienLieu = float(request.form.get("tong_nhien_lieu", 0))
        cay_xang.NhienLieuTieuThu = float(request.form.get("nhien_lieu_tieu_thu", 0))

        # Commit thay đổi vào cơ sở dữ liệu
        db.session.commit()

        # Sau khi sửa xong, redirect về trang quản lý cây xăng
        return redirect("/quan_ly_cay_xang")

    return render_template("admin/sua_cay_xang.html", cay_xang=cay_xang)


# Xóa cây xăng
@app.route("/xoa_cay_xang/<string:ma_cay_xang>")
def xoa_cay_xang(ma_cay_xang):
    """Xóa cây xăng"""
    cay_xang = CayXang.query.get(ma_cay_xang)
    db.session.delete(cay_xang)
    db.session.commit()
    return redirect(url_for("quan_ly_cay_xang"))

# Trang nhập tổng nhiên liệu
@app.route("/nhap_nhien_lieu/<string:ma_cay_xang>")
def nhap_nhien_lieu(ma_cay_xang):
    cay_xang = CayXang.query.get(ma_cay_xang)
    return render_template("admin/nhap_nhien_lieu.html", cay_xang=cay_xang)

# Xử lý cập nhật tổng nhiên liệu
@app.route("/cap_nhat_nhien_lieu/<string:ma_cay_xang>", methods=["POST"])
def cap_nhat_nhien_lieu(ma_cay_xang):
    cay_xang = CayXang.query.get(ma_cay_xang)
    cay_xang.TongNhienLieu = int(request.form.get("tong_nhien_lieu"))
    db.session.commit()
    return redirect("/quan_ly_cay_xang")

# Trang nhập nhiên liệu tiêu thụ
@app.route("/nhap_nhien_lieu_tieu_thu/<string:ma_cay_xang>")
def nhap_nhien_lieu_tieu_thu(ma_cay_xang):
    cay_xang = CayXang.query.get(ma_cay_xang)
    return render_template("admin/nhap_nhien_lieu_tieu_thu.html", cay_xang=cay_xang)

# Xử lý cập nhật nhiên liệu tiêu thụ
@app.route("/cap_nhat_nhien_lieu_tieu_thu/<string:ma_cay_xang>", methods=["POST"])
def cap_nhat_nhien_lieu_tieu_thu(ma_cay_xang):
    cay_xang = CayXang.query.get(ma_cay_xang)
    cay_xang.NhienLieuTieuThu = int(request.form.get("nhien_lieu_tieu_thu"))
    db.session.commit()
    return redirect("/quan_ly_cay_xang")


#----------------------------------------------------------------------------------------------------
@app.route('/tim-kiem', methods=['GET'])
def tim_kiem():
    ten_cay_xang = request.args.get('ten', '').strip()
    dia_chi = request.args.get('dia_chi', '').strip()
    thanh_pho = request.args.get('thanh_pho', '').strip()
    trang_thai = request.args.get('trang_thai', None)  # True/False
    loai_nhien_lieu = request.args.get('loai_nhien_lieu', '').strip()
    dich_vu = request.args.get('dich_vu', '').strip()  # Tìm kiếm theo dịch vụ
    vi_do = request.args.get('vi_do', type=float)  # Latitude của người dùng
    kinh_do = request.args.get('kinh_do', type=float)  # Longitude của người dùng
    ban_kinh = request.args.get('ban_kinh', type=float)  # Bán kính tìm kiếm (km)

    query = db.session.query(CayXang)

    # Tìm kiếm theo tên, địa chỉ hoặc thành phố
    if ten_cay_xang:
        query = query.filter(CayXang.TenCayXang.ilike(f'%{ten_cay_xang}%'))
    if dia_chi:
        query = query.filter(CayXang.DiaChi.ilike(f'%{dia_chi}%'))
    if thanh_pho:
        query = query.filter(CayXang.ThanhPho.ilike(f'%{thanh_pho}%'))

    # Lọc theo trạng thái hoạt động
    if trang_thai is not None:
        trang_thai_bool = trang_thai.lower() == 'true'
        query = query.filter(CayXang.TrangThaiHoatDong == trang_thai_bool)

    # Tìm kiếm theo loại nhiên liệu
    if loai_nhien_lieu:
        query = query.join(GiaNhienLieu).filter(GiaNhienLieu.LoaiNhienLieu.ilike(f'%{loai_nhien_lieu}%'))

    # Tìm kiếm theo dịch vụ
    if dich_vu:
        query = query.filter(CayXang.DichVu.ilike(f'%{dich_vu}%'))

    # Tìm kiếm theo vị trí và bán kính
    if vi_do is not None and kinh_do is not None and ban_kinh:
        from math import radians, sin, cos, sqrt, atan2

        def tinh_khoang_cach(lat1, lon1, lat2, lon2):
            # Công thức Haversine
            R = 6371  # Bán kính Trái Đất (km)
            dlat = radians(lat2 - lat1)
            dlon = radians(lon2 - lon1)
            a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            return R * c

        results = []
        for cay_xang in query.all():
            khoang_cach = tinh_khoang_cach(vi_do, kinh_do, cay_xang.ViDo, cay_xang.KinhDo)
            if khoang_cach <= ban_kinh:
                results.append(cay_xang)
        return jsonify([{
            'MaCayXang': cx.MaCayXang,
            'TenCayXang': cx.TenCayXang,
            'DiaChi': cx.DiaChi,
            'ThanhPho': cx.ThanhPho,
            'ViDo': cx.ViDo,
            'KinhDo': cx.KinhDo,
            'DichVu': cx.DichVu
        } for cx in results])

    # Trả về kết quả
    cay_xang_list = query.all()
    return jsonify([{
        'MaCayXang': cx.MaCayXang,
        'TenCayXang': cx.TenCayXang,
        'DiaChi': cx.DiaChi,
        'ThanhPho': cx.ThanhPho,
        'ViDo': cx.ViDo,
        'KinhDo': cx.KinhDo,
        'DichVu': cx.DichVu
    } for cx in cay_xang_list])

#----------------------------------------------------------------------------------------------------

# 3.2.5 Lập báo cáo thống kê và hiệu suất
@app.route("/lap_bao_cao_thong_ke", methods=["GET", "POST"])
def lap_bao_cao_thong_ke():
    if request.method == "POST":
        # Nhận dữ liệu từ biểu mẫu
        ma_cay_xang = request.form.get("ma_cay_xang")
        loai_bao_cao = request.form.get("loai_bao_cao")
        du_lieu_bao_cao = request.form.get("du_lieu_bao_cao")
        
        # Tạo báo cáo mới và lưu vào cơ sở dữ liệu
        bao_cao = BaoCao(
            MaCayXang=ma_cay_xang, 
            LoaiBaoCao=loai_bao_cao, 
            DuLieuBaoCao=du_lieu_bao_cao, 
            NgayTaoBaoCao=datetime.now()  # Tự động thiết lập thời gian tạo báo cáo
        )
        db.session.add(bao_cao)
        db.session.commit()

        return redirect(url_for("lap_bao_cao_thong_ke"))
    
    bao_cao = BaoCao.query.all()
    return render_template("admin/lap_bao_cao_thong_ke.html", bao_cao=bao_cao)

@app.route("/thong_ke_bao_cao")
def thong_ke_bao_cao():
    bao_cao = BaoCao.query.all()
    return render_template("admin/thong_ke_bao_cao.html", bao_cao=bao_cao)

#--------------------------------------------------------------------------------
@app.route('/danh_gia', methods=['GET', 'POST'])
def danh_gia():
    # Lấy danh sách cây xăng để người dùng chọn
    cay_xang_list = CayXang.query.all()
    
    if request.method == 'POST':
        # Lấy thông tin từ form
        ma_cay_xang = request.form['ma_cay_xang']
        diem_danh_gia = request.form['diem_danh_gia']
        binh_luan = request.form['binh_luan']
        ma_nguoi_dung = 1  
        ngay_danh_gia = datetime.now()

        # Lưu đánh giá vào database
        danh_gia_moi = DanhGia(
            MaCayXang=ma_cay_xang,
            MaNguoiDung=ma_nguoi_dung,
            DiemDanhGia=diem_danh_gia,
            BinhLuan=binh_luan,
            NgayDanhGia=ngay_danh_gia
        )
        db.session.add(danh_gia_moi)
        db.session.commit()
        flash("Đánh giá của bạn đã được lưu thành công!", "success")
        return redirect(url_for('danh_gia'))

    return render_template('danh_gia.html', cay_xang_list=cay_xang_list)

@app.route('/xem_danh_gia', methods=['GET', 'POST'])
def xem_danh_gia():
    # Lấy danh sách cây xăng để hiển thị trong dropdown
    cay_xang_list = CayXang.query.all()

    if request.method == 'POST':
        # Nhận mã cây xăng từ form
        ma_cay_xang = request.form.get('ma_cay_xang')
        if ma_cay_xang:
            # Lấy danh sách đánh giá của cây xăng đã chọn
            danh_gia_list = DanhGia.query.filter_by(MaCayXang=ma_cay_xang).all()
            # Lấy tên cây xăng
            ten_cay_xang = CayXang.query.get(ma_cay_xang).TenCayXang
            return render_template('xem_danh_gia.html', danh_gia_list=danh_gia_list, ten_cay_xang=ten_cay_xang, cay_xang_list=cay_xang_list)
    
    # Trả về giao diện khi chưa chọn cây xăng
    return render_template('xem_danh_gia.html', cay_xang_list=cay_xang_list)


if __name__ == "__main__":
    app.run(debug=True)
