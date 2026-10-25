# Evolution X Android 16 (bka) bring-up for malachite

**State: initial source integration only. No full ROM build, image audit or device boot has been performed.**

## What this branch changes

- Keeps the normal `lineage_malachite` product naming used by Evolution X's current bka device trees.
- Inherits `vendor/lineage/config/common_full_phone.mk`; on Evolution X's bka source this is the common device entry point that brings in the Evolution X additions through the Lineage config.
- Explicitly selects full GMS by setting `WITH_GMS := true` and disabling the mini/pico variants.
- Adds `manifests/evolution-x-bka.xml` to override the device tree with this branch and bring in the malachite-specific vendor, prebuilt-kernel and platform forks.

Do not replace the product inheritance with a guessed `vendor/evolution/config/common_full_phone.mk` path. The upstream Evolution X bka device-tree example uses `vendor/lineage/config/common_full_phone.mk`.

## Cloud build setup

Start from a clean Android 16 workspace with adequate disk, RAM and swap. Do not reuse a workspace initialized from another ROM without first checking its root manifest and local manifests.

Initialize the Evolution X bka manifest, then download the local manifest **before the first sync**:

```bash
repo init -u https://github.com/Evolution-X/manifest.git -b bka --git-lfs
mkdir -p .repo/local_manifests
curl -fL https://raw.githubusercontent.com/nx7rq/android_device_xiaomi_malachite/evox/bka-initial-product-config/manifests/evolution-x-bka.xml -o .repo/local_manifests/malachite-evox.xml
repo sync -c -j4
```

After sync, record the exact source state before trying a build:

```bash
repo manifest -r > out-malachite-resolved-manifest.xml
git -C device/xiaomi/malachite rev-parse HEAD
git -C vendor/xiaomi/malachite rev-parse HEAD
git -C device/xiaomi/malachite-kernel rev-parse HEAD
```

Keep the resolved manifest with build logs. The branch-based dependency references are not an immutable lock until `repo manifest -r` is saved.

## Product configuration check

```bash
source build/envsetup.sh
lunch lineage_malachite-userdebug
```

Only proceed if that product appears in the lunch target list and product configuration completes without missing-inherit, missing-file or duplicate-copy errors. If the target name is not listed, stop and inspect `lunch` output rather than inventing a product alias.

For the first build, preserve the device tree's current prebuilt-kernel selection. Do not flip `TARGET_FORCE_PREBUILT_KERNEL`, replace the kernel image, add a DTBO image, or change firmware assumptions as part of this product-config bring-up.

## Required gates before calling this a successful ROM bring-up

1. Product/Kati configuration succeeds on the exact resolved manifest.
2. Full Android build succeeds; a product makefile parse or kernel `cquery` is not a ROM build.
3. Generated VINTF passes `checkvintf` for applicable SKUs.
4. Compiled SELinux policy passes neverallow and policy checks while enforcing.
5. Proprietary blob provenance, ELF dependencies and extraction/fixup results are recorded against the actual userspace baseline.
6. Generated boot/recovery/vendor_boot/super and OTA payloads pass partition-size, AVB, signing, rollback, module-load-order and exclusion audits.
7. Physical testing is separately authorized and performed on the exact device SKU. No flashing, reboot, slot change, wipe or firmware operation is authorized by this source branch.

## Known inherited blockers

The current device-tree evidence describes the proprietary userspace extraction baseline as OS2.0.208.0.VOOMIXM while the build fingerprint string names OS3.0.10.0.WOOMIXM. This metadata mismatch is documented, not resolved by changing the fingerprint. Do not infer OS3 binary or firmware compatibility from the fingerprint.

The current BoardConfig forces the hybrid prebuilt kernel. The source-kernel candidate previously failed its KMI symbol check and its isolated repair still needs completed distribution-build/ABI evidence. Keep the prebuilt path for initial product configuration and track source-kernel work separately.

The existing audit also records unresolved AVB/release-key policy, persistent-partition autoformat risk, full Android compilation, merged VINTF, compiled SELinux, binary-fixup, generated-image and hardware-test gates. Do not remove assertions, disable verification, relax SELinux globally, or weaken charging/thermal protections to get past a failed gate.
