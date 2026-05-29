import numpy as np
from PIL import Image

def trim_save(arr, out, pad=4):
    a = arr[:, :, 3]
    ys, xs = np.where(a > 8)
    if len(xs):
        y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
        arr = arr[y0:y1, x0:x1]
    if pad:
        arr = np.pad(arr, ((pad, pad), (pad, pad), (0, 0)))
    Image.fromarray(arr.astype(np.uint8), 'RGBA').save(out)
    print(out, arr.shape[1], 'x', arr.shape[0])

# 1) Moncatec logo: solid black bg -> transparent, keep yellow+white color
im = np.asarray(Image.open('logo-moncatec.png').convert('RGB')).astype(np.float32)
m = im.max(axis=2)
alpha = np.clip(m * 1.18, 0, 255)
out = np.dstack([im, alpha])
trim_save(out, 'logo-moncatec-trans.png', pad=6)

# 2) brand logos -> white monochrome wordmark on transparent
def white_rgba(path, outp, crop_bottom=0.0):
    arr = np.asarray(Image.open(path).convert('RGBA')).copy()
    if crop_bottom > 0:
        h = arr.shape[0]
        arr = arr[:int(h * (1 - crop_bottom))]
    a = arr[:, :, 3].astype(np.uint8)
    w = np.full(a.shape, 255, np.uint8)
    trim_save(np.dstack([w, w, w, a]), outp)

def white_opaque(path, outp, thr=125):
    arr = np.asarray(Image.open(path).convert('RGB')).astype(np.float32)
    lum = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]
    a = np.clip((thr - lum) / thr * 255 + 120, 0, 255)
    a = np.where(lum < thr, a, 0)
    w = np.full(lum.shape, 255, np.float32)
    trim_save(np.dstack([w, w, w, a]), outp)

white_rgba('logo-marca-hikvision.png', 'logo-marca-hikvision-w.png', crop_bottom=0.42)
white_rgba('logo-marca-zkteco.png', 'logo-marca-zkteco-w.png')
white_rgba('logo-marca-tegui.png', 'logo-marca-tegui-w.png')
white_opaque('logo-marca-televes.png', 'logo-marca-televes-w.png', thr=125)
print('done')
