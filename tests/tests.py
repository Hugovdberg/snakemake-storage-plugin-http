from typing import Optional, Type
from snakemake_interface_storage_plugins.tests import TestStorageBase
from snakemake_interface_storage_plugins.storage_provider import StorageProviderBase
from snakemake_interface_storage_plugins.settings import StorageProviderSettingsBase
from snakemake_storage_plugin_http import StorageProvider, StorageProviderSettings


class TestStorageNoSettings(TestStorageBase):
    __test__ = True
    retrieve_only = True

    def get_query(self) -> str:
        return "https://www.google.com"
    
    def get_storage_provider_cls(self) -> Type[StorageProviderBase]:
        return StorageProvider

    def get_storage_provider_settings(self) -> Optional[StorageProviderSettingsBase]:
        return StorageProviderSettings()
