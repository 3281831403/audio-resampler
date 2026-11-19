import pytest

from audio import resampler as mod

CASES = [
    ('phase_increment', [44100, 48000], 0.91875, True),
    ('downmix_51', [[1.0, 1.0, 1.0, 0.0, 1.0, 1.0]], [2.4139999999999997, 2.4139999999999997], True),
    ('align_block', [1000, 128], 896, False),
    ('output_capacity', [1000, 1.08843537414966], 1090, False),
    ('lowpass_cutoff', [44100, 48000], 19845.0, True),
    ('lowpass_cutoff', [96000, 48000], 21600.0, True),
    ('clock_drift', [10.5, 10.0], 0.5, True),
    ('carry_state', [[1, 2], [3, 4]], [3, 4], False),
    ('carry_state', [[], [3, 4]], [], False),
    ('clamp_pcm', [1.5], 1.0, True),
    ('clamp_pcm', [-1.5], -1.0, True),
    ('fallback_layout', [8], 2, False),
    ('fallback_layout', [1], 1, False),
    ('reset_history', [[1, 2, 3]], [], False),
    ('phase_increment', [48000, 48000], 1.0, True),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_resampler_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
