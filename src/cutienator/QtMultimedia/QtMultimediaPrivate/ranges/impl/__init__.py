"""
The namespace 'QtMultimediaPrivate::ranges::impl' of Qt, a package of 'cutienator.QtMultimedia':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtMultimedia import QtMultimediaPrivate
  QtMultimediaPrivate.ranges.impl.equal_fn

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = (
    'equal_fn',
    'equal_range_fn',
    'lower_bound_fn',
    'max_element_fn',
    'max_fn',
    'min_element_fn',
    'min_fn',
    'sort_fn',
    'stable_sort_fn',
    'upper_bound_fn',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ...._qt_multimedia_private__ranges__impl__equal_fn import equal_fn
  from ...._qt_multimedia_private__ranges__impl__equal_range_fn import equal_range_fn
  from ...._qt_multimedia_private__ranges__impl__lower_bound_fn import lower_bound_fn
  from ...._qt_multimedia_private__ranges__impl__max_element_fn import max_element_fn
  from ...._qt_multimedia_private__ranges__impl__max_fn import max_fn
  from ...._qt_multimedia_private__ranges__impl__min_element_fn import min_element_fn
  from ...._qt_multimedia_private__ranges__impl__min_fn import min_fn
  from ...._qt_multimedia_private__ranges__impl__sort_fn import sort_fn
  from ...._qt_multimedia_private__ranges__impl__stable_sort_fn import stable_sort_fn
  from ...._qt_multimedia_private__ranges__impl__upper_bound_fn import upper_bound_fn
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'equal_fn': '_qt_multimedia_private__ranges__impl__equal_fn',
      'equal_range_fn': '_qt_multimedia_private__ranges__impl__equal_range_fn',
      'lower_bound_fn': '_qt_multimedia_private__ranges__impl__lower_bound_fn',
      'max_element_fn': '_qt_multimedia_private__ranges__impl__max_element_fn',
      'max_fn': '_qt_multimedia_private__ranges__impl__max_fn',
      'min_element_fn': '_qt_multimedia_private__ranges__impl__min_element_fn',
      'min_fn': '_qt_multimedia_private__ranges__impl__min_fn',
      'sort_fn': '_qt_multimedia_private__ranges__impl__sort_fn',
      'stable_sort_fn': '_qt_multimedia_private__ranges__impl__stable_sort_fn',
      'upper_bound_fn': '_qt_multimedia_private__ranges__impl__upper_bound_fn',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QtMultimediaPrivate.ranges.impl.equal_fn'. Python calls
    this for a name the package does not hold yet, and what it gives is kept
    here for the next time.

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
      module = importlib.import_module('....%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__]
