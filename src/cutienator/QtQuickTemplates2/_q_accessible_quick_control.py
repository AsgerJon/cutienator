"""
QAccessibleQuickControl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qaccessiblequickcontrol_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QAccessibleQuickControl to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAccessible
from ..QtQuick import QAccessibleQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
  from . import QQuickControl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickControl = WAIT['QQuickControl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleQuickControl(QAccessibleQuickItem):
  """
  The cute side of Qt's QAccessibleQuickControl: a plain Python object
  standing in front of one C++ QAccessibleQuickControl.

  It is built on the cute 'QAccessibleQuickItem', as Qt's
  QAccessibleQuickControl is built on Qt's QAccessibleQuickItem, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleQuickControl that has a ritual and that
  Python can call so far, 2 names in all: 'attributeValue', 'control'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<QAccessible::Attribute>
    QAccessibleQuickControl::attributeKeys() const': gives a type Python has
    no way to take yet.

  What to expect
  --------------

  - The C++ QAccessibleQuickControl is created at the first use, not by
    'QAccessibleQuickControl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleQuickControl.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleQuickControl'

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
    QAccessibleQuickControl::attributeValue(QAccessible::Attribute key)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickcontrol.html#attributeValue

    Parameters
    ----------

    key : QAccessible.Attribute
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant
    #      QAccessibleQuickControl::attributeValue(QAccessible::Attribute
    #      key) const
    ritual = (
        'ritual_ZNK23QAccessibleQuickControl14attributeValueEN11QAccessible'
        '9AttributeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QAccessibleQuickControl14attributeValueEN11QAcce'
          'ssible9AttributeE')
    address = self.uglySide.call(ritual, key.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def control(self) -> Optional[QQuickControl]:
    """
    Calls Qt's 'QQuickControl *QAccessibleQuickControl::control() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickcontrol.html#control

    Returns
    -------

    Optional[QQuickControl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickControl *QAccessibleQuickControl::control() const
    address = self.uglySide.call(
        'ritual_ZNK23QAccessibleQuickControl7controlEv',
    )
    from . import QQuickControl
    return QQuickControl._cuteAt(address)

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

  @overload(QQuickControl)
  @overload(NoneType)
  def __init__(self, control: Optional[QQuickControl]) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleQuickControl::QAccessibleQuickControl(QQuickControl
    *control)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickcontrol.html

    Parameters
    ----------

    control : Optional[QQuickControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessibleQuickControl::QAccessibleQuickControl(QQuickControl
    #      *control)
    self._noteCreation(QAccessibleQuickControl, lambda: Rituals.call(
        'ritual_ZN23QAccessibleQuickControlC1EP13QQuickControl',
        self._addressOf(control),
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
