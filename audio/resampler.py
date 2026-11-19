"""音频重采样：相位、下混与时钟：核心模块实现。"""

import math

# 5.1 声道顺序：FL, FR, C, LFE, SL, SR
_SURROUND_GAIN = 0.707  # 中置/环绕混入左右声道的增益，避免重复计入导致过载

# 已知的声道布局（单声道、立体声、5.1）
_KNOWN_LAYOUTS = (1, 2, 6)


def phase_increment(input_rate, output_rate):
    """相位增量等于输入/输出采样率比。"""
    return input_rate / output_rate


def downmix_51(channels):
    """5.1 下混到立体声，中置只计一次。"""
    fl, fr, c, _lfe, sl, sr = channels
    left = fl + _SURROUND_GAIN * c + _SURROUND_GAIN * sl
    right = fr + _SURROUND_GAIN * c + _SURROUND_GAIN * sr
    return [left, right]


def align_block(frames, block):
    """按块大小对齐输入帧数。"""
    return frames - (frames % block)


def output_capacity(input_frames, ratio):
    """按比例预分配输出缓冲并留一个余量。"""
    return math.ceil(input_frames * ratio) + 1


def lowpass_cutoff(input_rate, output_rate):
    """低通截止频率随采样率自适应。"""
    return min(input_rate, output_rate) * 0.45


def clock_drift(device_time, host_time):
    """计算设备时钟相对主机时钟的漂移。"""
    return device_time - host_time


def carry_state(previous, block):
    """跨块保留上一块尾部状态。"""
    n = len(previous)
    if n == 0:
        return []
    return list(block[-n:])


def clamp_pcm(value):
    """浮点转 16 bit 前钳制。"""
    return max(-1.0, min(1.0, value))


def fallback_layout(channels):
    """未知声道布局回退到立体声。"""
    return channels if channels in _KNOWN_LAYOUTS else 2


def reset_history(history):
    """暂停恢复时重置滤波历史。"""
    return []
