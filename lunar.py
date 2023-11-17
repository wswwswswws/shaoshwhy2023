from flask import Flask, render_template
import datetime
from lunarcalendar import Converter, Solar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def get_lunar_chinese_date(lunar_date):
    chinese_months = "正二三四五六七八九十冬腊"
    chinese_days1 = "初十廿三"
    chinese_days2 = "一二三四五六七八九十"
    month = chinese_months[lunar_date.month - 1]
    day = chinese_days1[(lunar_date.day - 1) // 10] if lunar_date.day != 20 else "二十"
    if lunar_date.day != 20:
        day += chinese_days2[(lunar_date.day - 1) % 10]
    return f"{month}月{day}"

@app.route('/get_current_datetime', methods=['GET'])
def get_current_datetime():
    # 获取当前公历时间
    current_time = datetime.datetime.now()

    # 转换为农历日期
    solar_date = Solar(current_time.year, current_time.month, current_time.day)
    lunar_date = Converter.Solar2Lunar(solar_date)
    lunar_date = get_lunar_chinese_date(lunar_date)
    # 格式化输出农历日期
    return lunar_date

app.run(debug=True)
