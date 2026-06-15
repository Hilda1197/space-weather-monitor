# 空间天气中断事件监控看板

基于 Flask + SQLite 的 Web 应用，用于可视化卫星 GPS 信号中断事件。

## 功能
- 展示中断事件列表
- 按 Kp 指数范围筛选
- 事件类型统计

## 技术栈
- Python + Flask
- SQLite
- Pandas
- HTML/CSS/JavaScript

## 本地运行
```bash
pip install flask pandas numpy
python init_db.py
python app.py
