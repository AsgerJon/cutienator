"""
The namespace 'Qt' of Qt, a package of 'cutienator.QtCore':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtCore import Qt
  Qt.Disambiguated_t

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

from .._qt import Qt as _Enums

#  The enums of the namespace, and the names of their
#  members, as names of the package itself, where C++ has
#  them: 'Qt.AlignLeft'.
globals().update({
    name: value for name, value in _Enums.__dict__.items()
    if not name.startswith('_')})

__all__ = (
    'Disambiguated_t',
    'OrderedUniqueRange_t',
    'partial_ordering',
    'strong_ordering',
    'weak_ordering',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._qt__disambiguated_t import Disambiguated_t
  from .._qt__ordered_unique_range_t import OrderedUniqueRange_t
  from .._qt__partial_ordering import partial_ordering
  from .._qt__strong_ordering import strong_ordering
  from .._qt__weak_ordering import weak_ordering
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'Disambiguated_t': '_qt__disambiguated_t',
      'OrderedUniqueRange_t': '_qt__ordered_unique_range_t',
      'partial_ordering': '_qt__partial_ordering',
      'strong_ordering': '_qt__strong_ordering',
      'weak_ordering': '_qt__weak_ordering',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'Qt.Disambiguated_t'. Python calls this for a name the
    package does not hold yet, and what it gives is kept here for the next
    time.

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
      module = importlib.import_module('..%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__, *(
        name for name in _Enums.__dict__ if not name.startswith('_'))]
