# Android 16 device tree for Redmi Note 14 Pro 5G / POCO X7 5G (malachite)

This repository contains the malachite device configuration. The original `lineage-23.2` branch targets unofficial LineageOS 23.2 (Android 16). The experimental branch `evox/bka-initial-product-config` carries initial Evolution X Android 16 (bka) product wiring; it is **not yet a verified build or boot**.

**Downloads, updates and support:** [Telegram group](https://t.me/malachite_project)

## Evolution X Android 16 (bka) — experimental

See [the bring-up checklist](bringup/EVOLUTION_X_BKA.md) before syncing or building. The Evolution X local manifest is [manifests/evolution-x-bka.xml](manifests/evolution-x-bka.xml). It selects this device-tree branch plus the malachite-specific vendor, prebuilt-kernel and platform repositories.

The product retains the `lineage_malachite` name used by Evolution X's current bka device-tree examples, inherits the common phone configuration, and selects full GMS. The branch has not yet passed a full Android build, generated-image audit or physical-device validation. Known AVB, persistent-partition, VINTF, SELinux, proprietary-blob and kernel-source evidence gaps remain documented in `bringup/`.

## LineageOS 23.2 baseline

`manifests/malachite.xml` is the local manifest for the LineageOS source tree. The comment at its top lists the device-specific forks and overrides. Kernel sources are built separately; see [kernel_manifest-6.1](https://github.com/malachite-project/kernel_manifest-6.1).

## Credits

Built on the work of [mt6878-devs](https://github.com/mt6878-devs), [puhboo](https://github.com/puhboo), [cmdr-chara](https://github.com/cmdr-chara), the malachite-project maintainers, and the LineageOS project.

```
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#
```
