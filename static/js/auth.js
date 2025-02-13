// Hiển thị Modal Đăng nhập
document.getElementById('btn-dang-nhap').addEventListener('click', function () {
    new bootstrap.Modal(document.getElementById('modalDangNhap')).show();
});

// Hiển thị Modal Đăng ký
document.getElementById('btn-dang-ky').addEventListener('click', function () {
    new bootstrap.Modal(document.getElementById('modalDangKy')).show();
});
