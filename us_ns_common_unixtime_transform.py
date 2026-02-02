import datetime

def convert_timestamp_to_readable(timestamp, unit="us"):
    """
    通用时间戳转换函数（无警告+精准东八区）
    支持纳秒(ns)/微秒(us)，输出东八区（UTC+8）格式化时间
    :param timestamp: 时间戳（整数）
    :param unit: 单位，可选 "ns"（纳秒）/"us"（微秒），默认"us"
    :return: 格式化时间字符串，格式：YYYY-MM-DD HH:MM:SS.ffffff
    """
    try:
        # 1. 定义东八区时区对象（Python 3.9+ 推荐写法，无第三方依赖）
        tz_cst = datetime.timezone(datetime.timedelta(hours=8))
        
        # 2. 根据单位转换为总秒数（保留小数，包含微秒精度）
        if unit == "ns":
            # 纳秒转秒：1秒=10^9纳秒，直接除以10^9保留小数
            total_seconds = timestamp / 10**9
        elif unit == "us":
            # 微秒转秒：1秒=10^6微秒，直接除以10^6保留小数
            total_seconds = timestamp / 10**6
        else:
            return "错误：仅支持 ns/us 单位"
        
        # 3. 转换为东八区的datetime对象（无utcfromtimestamp弃用警告）
        dt = datetime.datetime.fromtimestamp(total_seconds, tz=tz_cst)
        
        # 4. 格式化输出（%f自动提取6位微秒，无需手动拼接）
        return dt.strftime("%Y-%m-%d %H:%M:%S.%f")
    
    except Exception as e:
        return f"转换失败：{str(e)}"

# 测试验证（覆盖微秒/纳秒场景）
if __name__ == "__main__":
    # 你的目标微秒时间戳
    target_ts = 1770036527341552
    
    # 微秒转换（东八区精准时间）
    print(f"微秒转换（东八区）：{convert_timestamp_to_readable(target_ts, unit='us')}")
    
    # 纳秒转换（对比验证，注意：同数值纳秒转换日期会不同）
    print(f"纳秒转换（东八区）：{convert_timestamp_to_readable(target_ts, unit='ns')}")
    
    # 测试时间区间
    start_time = 1770036527341552
    end_time = 1770036527341750
    print(f"\nstart_time（微秒）：{convert_timestamp_to_readable(start_time, 'us')}")
    print(f"end_time（微秒）：{convert_timestamp_to_readable(end_time, 'us')}")
