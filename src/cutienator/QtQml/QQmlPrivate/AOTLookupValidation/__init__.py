"""
The namespace 'QQmlPrivate::AOTLookupValidation' of Qt, a package of 'cutienator.QtQml':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtQml import QQmlPrivate
  QQmlPrivate.AOTLookupValidation.EnumKeySignature

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

from ..._q_qml_private__a_o_t_lookup_validation import AOTLookupValidation as _Enums

#  The enums of the namespace, and the names of their
#  members, as names of the package itself, where C++ has
#  them: 'Qt.AlignLeft'.
globals().update({
    name: value for name, value in _Enums.__dict__.items()
    if not name.startswith('_')})

__all__ = (
    'EnumKeySignature',
    'Lookup',
    'MethodSignature',
    'PropertySignature',
    'Type',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ..._q_qml_private__a_o_t_lookup_validation__enum_key_signature import EnumKeySignature
  from ..._q_qml_private__a_o_t_lookup_validation__lookup import Lookup
  from ..._q_qml_private__a_o_t_lookup_validation__method_signature import MethodSignature
  from ..._q_qml_private__a_o_t_lookup_validation__property_signature import PropertySignature
  from ..._q_qml_private__a_o_t_lookup_validation__type import Type
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'EnumKeySignature': '_q_qml_private__a_o_t_lookup_validation__enum_key_signature',
      'Lookup': '_q_qml_private__a_o_t_lookup_validation__lookup',
      'MethodSignature': '_q_qml_private__a_o_t_lookup_validation__method_signature',
      'PropertySignature': '_q_qml_private__a_o_t_lookup_validation__property_signature',
      'Type': '_q_qml_private__a_o_t_lookup_validation__type',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QQmlPrivate.AOTLookupValidation.EnumKeySignature'.
    Python calls this for a name the package does not hold yet, and what it
    gives is kept here for the next time.

    Raises
    ------

    AttributeError
      The namespace has nothing of that name.
    """
    if name in __space_packages__:
      value = importlib.import_module('.%s' % name, __name__)
    else:
      try:
        fileName = __class_files__[name]
      except KeyError:
        infoSpec = """module '%s' has no attribute '%s'"""
        raise AttributeError(infoSpec % (__name__, name)) from None
      module = importlib.import_module('...%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__, *(
        name for name in _Enums.__dict__ if not name.startswith('_'))]
