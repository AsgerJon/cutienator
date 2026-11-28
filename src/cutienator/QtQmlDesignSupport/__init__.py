"""
The 'cutienator.QtQmlDesignSupport' package provides the cute classes of
the part of Qt named QtQmlDesignSupport, under the name PySide6 has for
it.

  from cutienator.QtQmlDesignSupport import QObjectRegistry, QObjectRegistryAttachedType

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
    'QObjectRegistry',
    'QObjectRegistryAttachedType',
    'QAbstractObjectRegistryRefPrivate',
    'QAbstractObjectRegistryRef',
    'QMultiObjectRegistryRefPrivate',
    'QObjectRegistryRefPrivate',
    'QObjectRegistrySingleton',
    'QMultiObjectRegistryRef',
    'QObjectRegistryRef',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_object_registry import QObjectRegistry
  from ._q_object_registry_attached_type import QObjectRegistryAttachedType
  from ._q_abstract_object_registry_ref_private import QAbstractObjectRegistryRefPrivate
  from ._q_abstract_object_registry_ref import QAbstractObjectRegistryRef
  from ._q_multi_object_registry_ref_private import QMultiObjectRegistryRefPrivate
  from ._q_object_registry_ref_private import QObjectRegistryRefPrivate
  from ._q_object_registry_singleton import QObjectRegistrySingleton
  from ._q_multi_object_registry_ref import QMultiObjectRegistryRef
  from ._q_object_registry_ref import QObjectRegistryRef
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QObjectRegistry': '_q_object_registry',
      'QObjectRegistryAttachedType': '_q_object_registry_attached_type',
      'QAbstractObjectRegistryRefPrivate': '_q_abstract_object_registry_ref_private',
      'QAbstractObjectRegistryRef': '_q_abstract_object_registry_ref',
      'QMultiObjectRegistryRefPrivate': '_q_multi_object_registry_ref_private',
      'QObjectRegistryRefPrivate': '_q_object_registry_ref_private',
      'QObjectRegistrySingleton': '_q_object_registry_singleton',
      'QMultiObjectRegistryRef': '_q_multi_object_registry_ref',
      'QObjectRegistryRef': '_q_object_registry_ref',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQmlDesignSupport import QObjectRegistryRef'. Python calls
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
