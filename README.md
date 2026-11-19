# 音频重采样：相位、下混与时钟

音频设备切到 48 kHz 后重采样出现金属声和节奏漂移：相位不累积、5.1 下混重复计中置、块不对齐、输出缓冲不足、低通截止固定、时钟漂移不补偿、跨块状态重置、浮点转 16 bit 不钳制、未知声道布局丢弃后置、暂停恢复不重置滤波历史。

## 目录结构

```
README.md
conftest.py
.gitignore
audio/__init__.py
audio/resampler.py
tests/test_resampler.py
```

## 当前状态

`audio/resampler.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_resampler.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 相位按采样率比累积
2. 5.1 下混权重正确
3. 可变采样率按块对齐
4. 输出缓冲按比例预分配
5. 低通截止随采样率自适应
6. 设备时钟漂移补偿
7. 重采样器跨块保留状态
8. 浮点转 16 bit 钳制
9. 未知声道布局回退到立体声
10. 暂停恢复重置滤波历史

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `audio/resampler.py`
后 15 条用例应全部通过。
