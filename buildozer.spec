[app]
title = AXNN
package.name = axnn
package.domain = org.axnnote.app
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.1.0

# Dependencies WAJIB (Bab 4 & 5)
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pygments,jedi,sqlite3

# Permissions Android
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Target SDK (Bab 17 Security)
android.api = 33
android.minapi = 24

# Arsitektur
android.archs = arm64-v8a,armeabi-v7a

# Gradle & Build
android.accept_sdk_license = True
android.skip_update = False
log_level = 2
warn_on_root = 1 
