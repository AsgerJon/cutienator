"""
The 'cutienator.QtQuick3DAssetImport' package provides the cute classes
of the part of Qt named QtQuick3DAssetImport, under the name PySide6 has
for it.

  from cutienator.QtQuick3DAssetImport import QSSGAssetImporterPluginInfo, QSSGAssetImporterFactory

A class is brought in the first time it is asked for, with the files it
needs and no others. So bringing in the package costs nothing, and a
program pays for the classes it uses.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = (
    'QSSGAssetImporterPluginInfo',
    'QSSGAssetImporterFactory',
    'QSSGAssetImporterPlugin',
    'QSSGAssetImportManager',
    'QSSGAssetImporter',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_s_s_g_asset_importer_plugin_info import QSSGAssetImporterPluginInfo
  from ._q_s_s_g_asset_importer_factory import QSSGAssetImporterFactory
  from ._q_s_s_g_asset_importer_plugin import QSSGAssetImporterPlugin
  from ._q_s_s_g_asset_import_manager import QSSGAssetImportManager
  from ._q_s_s_g_asset_importer import QSSGAssetImporter
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QSSGAssetImporterPluginInfo': '_q_s_s_g_asset_importer_plugin_info',
      'QSSGAssetImporterFactory': '_q_s_s_g_asset_importer_factory',
      'QSSGAssetImporterPlugin': '_q_s_s_g_asset_importer_plugin',
      'QSSGAssetImportManager': '_q_s_s_g_asset_import_manager',
      'QSSGAssetImporter': '_q_s_s_g_asset_importer',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQuick3DAssetImport import QSSGAssetImporter'. Python calls
    this for a name the package does not hold yet. The file of the
    class is brought in, which brings in the files that class needs
    and no others, and the class is kept here for the next time.

    Raises
    ------

    AttributeError
      The part has no class of that name.
    """
    try:
      fileName = __class_files__[name]
    except KeyError:
      infoSpec = """module '%s' has no attribute '%s'"""
      raise AttributeError(infoSpec % (__name__, name)) from None
    module = importlib.import_module('.%s' % fileName, __name__)
    value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names every class of the part, brought in or not."""
    return [*__all__]
