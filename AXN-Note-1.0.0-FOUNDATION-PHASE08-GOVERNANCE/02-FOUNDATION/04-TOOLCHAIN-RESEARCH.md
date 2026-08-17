# AXN Note 1.0.0 — Toolchain Research Snapshot

Date: 2026-08-16

## Current verified references

- Android Gradle Plugin 9.3.0: stable; Gradle 9.5.0; JDK 17; supports API 37. https://developer.android.com/build/releases/agp-9-3-0-release-notes
- Android Studio Quail 2 (2026.1.2): stable; supports AGP 7.1–9.3. https://developer.android.com/studio/releases/
- Compose BOM 2026.06.00: current stable BOM documented by Android Developers. https://developer.android.com/develop/ui/compose/bom
- Kotlin 2.4.10: latest stable release in the current Kotlin 2.4 line at the audit date. Kotlin 2.4.20 was planned for September 2026; preview builds existed. https://kotlinlang.org/docs/releases.html

These versions are a researched baseline, not yet an Owner-locked dependency manifest. A clean build must validate the exact combination before the first release tag.
