"""
The namespace 'q23::detail' of Qt, a package of 'cutienator.QtCore':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtCore import q23
  q23.detail.default_constructor_tag

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
    'default_constructor_tag',
    'no_init_t',
    'swap_adl_tests',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ..._q23__detail__default_constructor_tag import default_constructor_tag
  from ..._q23__detail__no_init_t import no_init_t
  from . import swap_adl_tests
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'default_constructor_tag': '_q23__detail__default_constructor_tag',
      'no_init_t': '_q23__detail__no_init_t',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ('swap_adl_tests',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'q23.detail.default_constructor_tag'. Python calls this
    for a name the package does not hold yet, and what it gives is kept here
    for the next time.

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
    return [*__all__]
