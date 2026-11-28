"""
The namespace 'QCss' of Qt, a package of 'cutienator.QtGui':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtGui import QCss
  QCss.AnimationRule

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

from .._q_css import QCss as _Enums

#  The enums of the namespace, and the names of their
#  members, as names of the package itself, where C++ has
#  them: 'Qt.AlignLeft'.
globals().update({
    name: value for name, value in _Enums.__dict__.items()
    if not name.startswith('_')})

__all__ = (
    'AnimationRule',
    'AttributeSelector',
    'BackgroundData',
    'BasicSelector',
    'BorderData',
    'ImportRule',
    'LengthData',
    'MediaRule',
    'PageRule',
    'Pseudo',
    'Selector',
    'StyleRule',
    'StyleSheet',
    'Symbol',
    'Value',
    'Scanner',
    'StyleSelector',
    'Parser',
    'BrushData',
    'ColorData',
    'Declaration',
    'ValueExtractor',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._q_css__animation_rule import AnimationRule
  from .._q_css__attribute_selector import AttributeSelector
  from .._q_css__background_data import BackgroundData
  from .._q_css__basic_selector import BasicSelector
  from .._q_css__border_data import BorderData
  from .._q_css__import_rule import ImportRule
  from .._q_css__length_data import LengthData
  from .._q_css__media_rule import MediaRule
  from .._q_css__page_rule import PageRule
  from .._q_css__pseudo import Pseudo
  from .._q_css__selector import Selector
  from .._q_css__style_rule import StyleRule
  from .._q_css__style_sheet import StyleSheet
  from .._q_css__symbol import Symbol
  from .._q_css__value import Value
  from .._q_css__scanner import Scanner
  from .._q_css__style_selector import StyleSelector
  from .._q_css__parser import Parser
  from .._q_css__brush_data import BrushData
  from .._q_css__color_data import ColorData
  from .._q_css__declaration import Declaration
  from .._q_css__value_extractor import ValueExtractor
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'AnimationRule': '_q_css__animation_rule',
      'AttributeSelector': '_q_css__attribute_selector',
      'BackgroundData': '_q_css__background_data',
      'BasicSelector': '_q_css__basic_selector',
      'BorderData': '_q_css__border_data',
      'ImportRule': '_q_css__import_rule',
      'LengthData': '_q_css__length_data',
      'MediaRule': '_q_css__media_rule',
      'PageRule': '_q_css__page_rule',
      'Pseudo': '_q_css__pseudo',
      'Selector': '_q_css__selector',
      'StyleRule': '_q_css__style_rule',
      'StyleSheet': '_q_css__style_sheet',
      'Symbol': '_q_css__symbol',
      'Value': '_q_css__value',
      'Scanner': '_q_css__scanner',
      'StyleSelector': '_q_css__style_selector',
      'Parser': '_q_css__parser',
      'BrushData': '_q_css__brush_data',
      'ColorData': '_q_css__color_data',
      'Declaration': '_q_css__declaration',
      'ValueExtractor': '_q_css__value_extractor',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QCss.AnimationRule'. Python calls this for a name the
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
