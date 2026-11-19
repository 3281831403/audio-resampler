"""音频重采样：相位、下混与时钟：待实现的核心模块。"""


def phase_increment(input_rate, output_rate):
    """相位增量等于输入/输出采样率比。"""
    raise NotImplementedError

def downmix_51(channels):
    """5.1 下混到立体声，中置只计一次。"""
    raise NotImplementedError

def align_block(frames, block):
    """按块大小对齐输入帧数。"""
    raise NotImplementedError

def output_capacity(input_frames, ratio):
    """按比例预分配输出缓冲并留一个余量。"""
    raise NotImplementedError

def lowpass_cutoff(input_rate, output_rate):
    """低通截止频率随采样率自适应。"""
    raise NotImplementedError

def clock_drift(device_time, host_time):
    """计算设备时钟相对主机时钟的漂移。"""
    raise NotImplementedError

def carry_state(previous, block):
    """跨块保留上一块尾部状态。"""
    raise NotImplementedError

def clamp_pcm(value):
    """浮点转 16 bit 前钳制。"""
    raise NotImplementedError

def fallback_layout(channels):
    """未知声道布局回退到立体声。"""
    raise NotImplementedError

def reset_history(history):
    """暂停恢复时重置滤波历史。"""
    raise NotImplementedError
