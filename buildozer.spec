[app]
title = AXNN
package.name = axnn
package.domain = org.axnnote
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,md,txt
version = 1.1.0

# ✅ HAPUS jedi==0.19.1 untuk build M2
requirements = python3,kivy==2.3.0,kivymd==1.2.0,plyer==2.1.0,pygments==2.18.0,androidstorage4kivy,cython==0.29.37

orientation = portrait
fullscreen = 0

android.api = 34
android.ndk = 25b
android.sdk = 24
android.archs = armeabi-v7a, arm64-v8a
android.minapi = 29

android.permissions = WRITE_INTERNAL_STORAGE,READ_INTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,NOTIFICATIONS,VIBRATE,POST_NOTIFICATIONS,WAKE_LOCK

android.allow_backup = True
android.use_aapt2 = True

# ⚠️ Comment dulu jika aset belum ada
# android.icon = assets/icon.png
# android.presplash = assets/splash.png

# ✅ PIN python-for-android ke versi stabil (Python 3.11)
[buildozer]
p4a.url = https://github.com/kivy/python-for-android.git
p4a.branch = master
