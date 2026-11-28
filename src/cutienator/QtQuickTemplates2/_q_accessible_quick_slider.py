"""
QAccessibleQuickSlider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qaccessiblequickslider_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QAccessibleQuickSlider to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAccessible
from . import QAccessibleQuickControl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
  from . import QQuickSlider
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickSlider = WAIT['QQuickSlider']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleQuickSlider(QAccessibleQuickControl):
  """
  The cute side of Qt's QAccessibleQuickSlider: a plain Python object
  standing in front of one C++ QAccessibleQuickSlider.

  It is built on the cute 'QAccessibleQuickControl', as Qt's
  QAccessibleQuickSlider is built on Qt's QAccessibleQuickControl, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleQuickSlider that has a ritual and that
  Python can call so far, 2 names in all: 'attributeValue', 'slider'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<QAccessible::Attribute>
    QAccessibleQuickSlider::attributeKeys() const': gives a type Python has
    no way to take yet.

  What to expect
  --------------

  - The C++ QAccessibleQuickSlider is created at the first use, not by
    'QAccessibleQuickSlider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleQuickSlider.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleQuickSlider'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAccessible.Attribute)
  def attributeValue(self, key: QAccessible.Attribute) -> QVariant:
    """
    Calls Qt's 'QVariant
    QAccessibleQuickSlider::attributeValue(QAccessible::Attribute key)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickslider.html#attributeValue

    Parameters
    ----------

    key : QAccessible.Attribute
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleQuickSlider::attributeValue(QAccessible::Attribute
    #      key) const
    ritual = (
        'ritual_ZNK22QAccessibleQuickSlider14attributeValueEN11QAccessible9'
        'AttributeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QAccessibleQuickSlider14attributeValueEN11QAcces'
          'sible9AttributeE')
    address = self.uglySide.call(ritual, key.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def slider(self) -> Optional[QQuickSlider]:
    """
    Calls Qt's 'QQuickSlider *QAccessibleQuickSlider::slider() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblequickslider.html#slider

    Returns
    -------

    Optional[QQuickSlider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSlider *QAccessibleQuickSlider::slider() const
    address = self.uglySide.call(
        'ritual_ZNK22QAccessibleQuickSlider6sliderEv',
    )
    from . import QQuickSlider
    return QQuickSlider._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickSlider)
  @overload(NoneType)
  def __init__(self, slider: Optional[QQuickSlider]) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleQuickSlider::QAccessibleQuickSlider(QQuickSlider *slider)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickslider.html#QAccessibleQuickSlider

    Parameters
    ----------

    slider : Optional[QQuickSlider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessibleQuickSlider::QAccessibleQuickSlider(QQuickSlider *slider)
    self._noteCreation(QAccessibleQuickSlider, lambda: Rituals.call(
        'ritual_ZN22QAccessibleQuickSliderC1EP12QQuickSlider',
        self._addressOf(slider),
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
