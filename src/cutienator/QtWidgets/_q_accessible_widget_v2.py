"""
QAccessibleWidgetV2 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qaccessiblewidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAccessible, QAccessibleAttributesInterface
from . import QAccessibleWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleWidgetV2(QAccessibleWidget, QAccessibleAttributesInterface):
  """
  The cute side of Qt's QAccessibleWidgetV2: a plain Python object standing
  in front of one C++ QAccessibleWidgetV2.

  It is built on the cute 'QAccessibleWidget', as Qt's QAccessibleWidgetV2 is
  built on Qt's QAccessibleWidget, and has everything that class has. It is
  built on the cute 'QAccessibleAttributesInterface' as well, as Qt's
  QAccessibleWidgetV2 is built on Qt's QAccessibleAttributesInterface too,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleWidgetV2 that has a ritual and that
  Python can call so far, 1 name in all: 'attributeValue'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has no ritual
  ------------------

  5 of the 8 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 protected.

  What to expect
  --------------

  - The C++ QAccessibleWidgetV2 is created at the first use, not by
    'QAccessibleWidgetV2(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleWidgetV2.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleWidgetV2'

  #  Qt's QAccessibleWidgetV2 is built on more than one class. The part of a
  #  C++ QAccessibleWidgetV2 that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAccessibleAttributesInterface':
          'ritual_cast_QAccessibleWidgetV2_QAccessibleAttributesInterface',
  }

  #  A C++ QAccessibleWidgetV2 Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleWidgetV2'

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
    QAccessibleWidgetV2::attributeValue(QAccessible::Attribute key) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblewidgetv2.html#attributeValue

    Parameters
    ----------

    key : QAccessible.Attribute
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAccessibleWidgetV2::attributeValue(QAccessible::Attribute
    #      key) const
    ritual = (
        'ritual_ZNK19QAccessibleWidgetV214attributeValueEN11QAccessible9Att'
        'ributeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QAccessibleWidgetV214attributeValueEN11QAccessib'
          'le9AttributeE')
    address = self.uglySide.call(ritual, key.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

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

  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, QAccessible.Role)
  @overload(NoneType, QAccessible.Role)
  def __init__(
      self,
      object: Optional[QWidget],
      role: QAccessible.Role = QAccessible.Role.Client,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleWidgetV2::QAccessibleWidgetV2(QWidget *object,
    QAccessible::Role role)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblewidgetv2.html#QAccessibleWidgetV2

    Parameters
    ----------

    object : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    role : QAccessible.Role
      Passed on as its number. May be left out, as in Qt: it is then
      QAccessible.Role.Client.
    """
    #  QAccessibleWidgetV2::QAccessibleWidgetV2(QWidget *object,
    #      QAccessible::Role role)
    self._noteCreation(QAccessibleWidgetV2, lambda: Rituals.call(
        'ritual_ZN19QAccessibleWidgetV2C1EP7QWidgetN11QAccessible4RoleE',
        self._addressOf(object), role.value,
    ))

  @overload(QWidget, QAccessible.Role, str)
  @overload(NoneType, QAccessible.Role, str)
  def __init__(
      self,
      object: Optional[QWidget],
      role: QAccessible.Role,
      name: str,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleWidgetV2::QAccessibleWidgetV2(QWidget *object,
    QAccessible::Role role, const QString &name)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblewidgetv2.html#QAccessibleWidgetV2

    Parameters
    ----------

    object : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    role : QAccessible.Role
      Passed on as its number.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QAccessibleWidgetV2::QAccessibleWidgetV2(QWidget *object,
    #      QAccessible::Role role, const QString &name)
    self._noteCreation(QAccessibleWidgetV2, lambda: Rituals.call(
        'ritual_ZN19QAccessibleWidgetV2C1EP7QWidgetN11QAccessible4RoleERK7Q'
        'String',
        self._addressOf(object), role.value, name,
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
