"""Regression checks for the experimental Evolution X bka product wiring."""
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PRODUCT = ROOT / "lineage_malachite.mk"
MANIFEST = ROOT / "manifests" / "evolution-x-bka.xml"
DOC = ROOT / "bringup" / "EVOLUTION_X_BKA.md"


class EvolutionXConfigTests(unittest.TestCase):
    def test_product_selects_full_gms_before_common_config(self):
        product = PRODUCT.read_text()
        common = "vendor/lineage/config/common_full_phone.mk"
        self.assertIn("PRODUCT_NAME := lineage_malachite", product)
        self.assertIn("WITH_GMS := true", product)
        self.assertIn("TARGET_USES_MINI_GAPPS := false", product)
        self.assertIn("TARGET_USES_PICO_GAPPS := false", product)
        common_pos = product.index(common)
        for flag in (
            "WITH_GMS := true",
            "TARGET_USES_MINI_GAPPS := false",
            "TARGET_USES_PICO_GAPPS := false",
        ):
            with self.subTest(flag=flag):
                self.assertLess(product.index(flag), common_pos)

    def test_local_manifest_is_well_formed_and_uses_user_branch(self):
        root = ET.parse(MANIFEST).getroot()
        projects = {p.get("path"): p for p in root.findall("project")}
        device = projects["device/xiaomi/malachite"]
        self.assertEqual(device.get("name"), "nx7rq/android_device_xiaomi_malachite")
        self.assertEqual(device.get("revision"), "evox/bka-initial-product-config")

    def test_local_manifest_does_not_replace_evolution_core_projects(self):
        root = ET.parse(MANIFEST).getroot()
        paths = {p.get("path") for p in root.findall("project")}
        for path in (
            "frameworks/base",
            "frameworks/native",
            "packages/apps/Settings",
            "packages/services/Telephony",
            "packages/modules/Bluetooth",
        ):
            with self.subTest(path=path):
                self.assertNotIn(path, paths)

    def test_bringup_checklist_exists(self):
        self.assertTrue(DOC.is_file())


if __name__ == "__main__":
    unittest.main()
