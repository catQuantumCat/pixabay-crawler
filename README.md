# Pixabay Crawler

## Giới thiệu

Đây là một công cụ tự động tải ảnh từ Pixabay dựa trên các từ khóa được chỉ định. Công cụ này giúp bạn tải nhiều ảnh chất lượng cao từ Pixabay một cách tự động và có tổ chức.

## Yêu cầu hệ thống

- Python 3.x
- Thư viện pixabay-python
- Đăng ký tài khoản Pixabay: https://pixabay.com/accounts/register/
- Lấy key: https://pixabay.com/api/docs/ (để ý đã đăng nhập hay chưa)

## Cài đặt

1. Cài đặt thư viện cần thiết:

```bash
pip install pixabay-python
```

2. Cấu hình API key:

- Mở file `pixabay_config.json`
- Thêm API key của bạn vào trường `pixabay_api_key`

## Cấu trúc thư mục

```
.
├── pixabay_crawler.py     # Script chính để tải ảnh
├── pixabay_config.json    # File cấu hình
├── keywords.json         # Danh sách từ khóa tìm kiếm
└── Crawl/               # Thư mục chứa ảnh đã tải
```

## Cách sử dụng

1. Cấu hình file `keywords.json`:

```json
{
  "từ_khóa_1": "tag_tìm_kiếm_1",
  "từ_khóa_2": "tag_tìm_kiếm_2"
}
```

2. Cấu hình file `pixabay_config.json`:

```json
{
  "pixabay_api_key": "API_KEY_CỦA_BẠN",
  "save_root": "đường_dẫn_lưu_ảnh",
  "keywords_file": "keywords.json",
  "npage": 10,
  "max_images": 500
}
```
`npage` càng nhiều, scope tìm càng rộng


3. Chạy script:

Chỉnh số lượng ảnh muốn crawl ở `pixabay_crawler.py`: 
```
MAX_IMAGES = config.get('max_images', 500)
````

```bash
python pixabay_crawler.py
```

## Tính năng

- Tự động tạo thư mục cho mỗi từ khóa
- Tải ảnh chất lượng cao
- Giới hạn số lượng ảnh tải xuống
- Xử lý lỗi tự động
- Tạm dừng ngẫu nhiên giữa các lần tải để tránh bị chặn

## Lưu ý

- Đảm bảo bạn có đủ dung lượng ổ đĩa
- Tuân thủ điều khoản sử dụng của Pixabay
- API key có giới hạn số lượng request, hãy sử dụng hợp lý

## Xử lý lỗi

- Nếu gặp lỗi khi tải ảnh, script sẽ ghi log và tiếp tục với ảnh tiếp theo
- Kiểm tra file log để xem chi tiết lỗi nếu có

## Giấy phép

Sử dụng theo giấy phép MIT
