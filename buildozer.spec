[app]
title = AXNN
package.name = axnn
package.domain = org.axnnote
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,md,txt
version = 1.1.0

requirements = python3,kivy==2.3.0,kivymd==1.2.0,plyer==2.1.0,pygments==2.18.0,jedi==0.19.1,androidstorage4kivy,cython==0.29.37

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

# Jika aset belum ada, komentar dulu dua baris ini agar build tidak gagal
# android.icon = assets/icon.png
# android.presplash = assets/splash.png
