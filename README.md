# cf穿越火线-硬件级驱动辅助
需要win32库和winio库

穿越火线硬件级驱动辅助

目前除了速点是调用winapi的,有一点的几率会检测，不过是封一小时而已,低调使用,本人测试usp和cop0.035是木有被封，这个参数刚好是抖音李宏意同款手速

鬼跳使用方法,先按方向键，然后就是触发键,我这里的触发键是中间，自己调试(0x01是左键，0x02是右键，其他不知道)

上中箱使用方法，靠着箱子按w，然后就是触发键，就可以了

瞬狙，暂时木有问题，自己点触发键顺就是了，我这里是切换手榴弹来顺，而且参数是拿毁灭来测试的，部分枪械可能不准，自己调试

winio🐎键对照表如下，自己调试

++++++++++++++++++++++++++++++++++++++++
    
    'ESC': 0x01,
    '1': 0x02,
    '2': 0x03,
    '3': 0x04,
    '4': 0x05,
    '5': 0x06,
    '6': 0x07,
    '7': 0x08,
    '8': 0x09,
    '9': 0x0a,
    '0': 0x0b,
    '-': 0x0c,
    '=': 0x0d,
    # 0e (Backspace)
    'Tab': 0x0f,
    'q': 0x10,
    'w': 0x11,
    'e': 0x12,
    'r': 0x13,
    't': 0x14,
    'y': 0x15,
    'u': 0x16,
    'i': 0x17,
    'o': 0x18,
    'p': 0x19,
    '[': 0x1a,
    ']': 0x1b,
    'Enter': 0x1c,
     # 1d (LCtrl)
     'a': 0x1e,
    's': 0x1f,
    'd': 0x20,
    'f': 0x21,
    'g': 0x22,
    'h': 0x23,
    'j': 0x24,
    'k': 0x25,
    'l': 0x26,
    ';': 0x27,
    '\'': 0x28,
    '`': 0x29,
    # 2a (LShift)
    '\\': 0x2b,     # (\|), on a 102-key keyboard
    'z': 0x2c,
    'x': 0x2d,
    'c': 0x2e,
    'v': 0x2f,
    'b': 0x30,
    'n': 0x31,
    'm': 0x32,
    ',': 0x33,
    '.': 0x34,
    '/': 0x35}
    # 36 (RShift)
    # 37 (Keypad-*) or (*/PrtScn) on a 83/84-key keyboard
    # 38 (LAlt), 39 (Space bar),
    # 3a (CapsLock)
    # 3b (F1), 3c (F2), 3d (F3), 3e (F4), 3f (F5), 40 (F6), 41 (F7), 42 (F8), 43 (F9), 44 (F10)
++++++++++++++++++++++++++++++++++++++++
