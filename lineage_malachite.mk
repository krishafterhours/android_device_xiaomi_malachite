#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit base Android product definitions.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit_only.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Evolution X's bka tree follows the LineageOS device-product contract.
# Its vendor/lineage common config includes Evolution X's custom config.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Inherit device-specific configuration after common defaults.
$(call inherit-product, device/xiaomi/malachite/device.mk)

# Full GMS: leave both reduced package variants disabled.
WITH_GMS := true
TARGET_USES_MINI_GAPPS := false
TARGET_USES_PICO_GAPPS := false

PRODUCT_NAME := lineage_malachite
PRODUCT_DEVICE := malachite
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_BRAND := Redmi
PRODUCT_MODEL := 24090RA29G

PRODUCT_SYSTEM_NAME := malachite_global
PRODUCT_SYSTEM_DEVICE := malachite

# This fingerprint is retained from the current tree. It describes OS3 while
# the documented proprietary userspace baseline is OS2; do not treat it as
# proof that OS3 binaries or firmware are in use or compatible.
PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildFingerprint=Xiaomi/hal_mgvi_64_armv82_mt6878_global/mgvi_64_armv82:14/UP1A.231005.007/OS3.0.10.0.WOOMIXM:user/release-keys \
    SystemModel=$(PRODUCT_SYSTEM_DEVICE) \
    SystemName=$(PRODUCT_SYSTEM_NAME) \
    ProductModel=$(PRODUCT_SYSTEM_DEVICE) \
    DeviceProduct=$(PRODUCT_SYSTEM_NAME)

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi
