import datetime

def convert_us_timestamp_to_readable(us_timestamp):
    """
    将微秒级 Unix 时间戳转换为东八区（UTC+8）的易读时间字符串
    :param us_timestamp: 微秒级时间戳（整数）
    :return: 格式化的时间字符串，格式：YYYY-MM-DD HH:MM:SS.ffffff
    """
    try:
        # 1. 微秒转秒（核心：1秒=10^6微秒）
        total_seconds = us_timestamp / 10**6  # 保留小数（包含微秒）
        
        # 2. 直接转换为东八区时间（Python 3.9+ 推荐写法）
        # 步骤1：获取东八区时区对象
        tz_cst = datetime.timezone(datetime.timedelta(hours=8))  # UTC+8 东八区
        # 步骤2：将时间戳转换为东八区的datetime对象（无警告）
        dt = datetime.datetime.fromtimestamp(total_seconds, tz=tz_cst)
        
        # 3. 格式化输出（自动包含东八区时间，无需额外转换）
        readable_time = dt.strftime("%Y-%m-%d %H:%M:%S.%f")
        return readable_time
    except Exception as e:
        return f"转换失败：{str(e)}"

# 测试你的时间戳
if __name__ == "__main__":
    start_time = 1770036527341552
    end_time = 1770036527341750
    
    print(f"start_time 转换后：{convert_us_timestamp_to_readable(start_time)}")
    print(f"end_time 转换后：{convert_us_timestamp_to_readable(end_time)}")
