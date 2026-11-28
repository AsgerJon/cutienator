"""
QQuickGeometryChange binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickGeometryChange to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class QQuickGeometryChange(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickGeometryChange: a plain Python object standing
  in front of one C++ QQuickGeometryChange.

  C++ hands a QQuickGeometryChange around as a copy, so every C++
  QQuickGeometryChange behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickGeometryChange that has a ritual and that
  Python can call so far, 20 names in all: 'noChange', 'anyChange',
  'xChange', 'yChange', 'widthChange', 'heightChange', 'positionChange',
  'sizeChange', 'horizontalChange', 'verticalChange', 'setXChange',
  'setYChange', 'setWidthChange', 'setHeightChange', 'setSizeChange',
  'setAllChanged', 'setHorizontalChange', 'setVerticalChange', 'set',
  'matches'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickGeometryChange::~QQuickGeometryChange()': the destructor:
    Python removes its C++ QQuickGeometryChange by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQuickGeometryChange is created at the first use, not by
    'QQuickGeometryChange(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickGeometryChange back gives a copy the ritual
    made for Python, in a new cute QQuickGeometryChange.
  """

  #  The enums Qt writes inside QQuickGeometryChange, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Kind(CuteNum):
    """
    The enum 'QQuickGeometryChange::Kind' of Qt, with the 7 names Qt gives in
    it.
    """

    Nothing = Kee[int](0)
    X = Kee[int](1)
    Y = Kee[int](2)
    Width = Kee[int](4)
    Height = Kee[int](8)
    Size = Kee[int](12)
    All = Kee[int](15)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGeometryChange'

  #  Qt's '~QQuickGeometryChange()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickGeometryChange behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QQuickGeometryChangeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def noChange(self) -> bool:
    """
    Calls Qt's 'bool QQuickGeometryChange::noChange() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgeometrychange.html#noChange
    """
    #  bool QQuickGeometryChange::noChange() const
    return self.uglySide.call('ritual_ZNK20QQuickGeometryChange8noChangeEv')

  def anyChange(self) -> bool:
    """
    Calls Qt's 'bool QQuickGeometryChange::anyChange() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeometrychange.html#anyChange
    """
    #  bool QQuickGeometryChange::anyChange() const
    return self.uglySide.call('ritual_ZNK20QQuickGeometryChange9anyChangeEv')

  def xChange(self) -> bool:
    """
    Calls Qt's 'bool QQuickGeometryChange::xChange() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgeometrychange.html#xChange
    """
    #  bool QQuickGeometryChange::xChange() const
    return self.uglySide.call('ritual_ZNK20QQuickGeometryChange7xChangeEv')

  def yChange(self) -> bool:
    """
    Calls Qt's 'bool QQuickGeometryChange::yChange() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgeometrychange.html#yChange
    """
    #  bool QQuickGeometryChange::yChange() const
    return self.uglySide.call('ritual_ZNK20QQuickGeometryChange7yChangeEv')

  def widthChange(self) -> bool:
    """
    Calls Qt's 'bool QQuickGeometryChange::widthChange() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeometrychange.html#widthChange
    """
    #  bool QQuickGeometryChange::widthChange() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickGeometryChange11widthChangeEv',
    )

  def heightChange(self) -> bool:
    """
    Calls Qt's 'bool QQuickGeometryChange::heightChange() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeometrychange.html#heightChange
    """
    #  bool QQuickGeometryChange::heightChange() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickGeometryChange12heightChangeEv',
    )

  def positionChange(self) -> bool:
    """
    Calls Qt's 'bool QQuickGeometryChange::positionChange() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeometrychange.html#positionChange
    """
    #  bool QQuickGeometryChange::positionChange() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickGeometryChange14positionChangeEv',
    )

  def sizeChange(self) -> bool:
    """
    Calls Qt's 'bool QQuickGeometryChange::sizeChange() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeometrychange.html#sizeChange
    """
    #  bool QQuickGeometryChange::sizeChange() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickGeometryChange10sizeChangeEv',
    )

  def horizontalChange(self) -> bool:
    """
    Calls Qt's 'bool QQuickGeometryChange::horizontalChange() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeometrychange.html#horizontalChange
    """
    #  bool QQuickGeometryChange::horizontalChange() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickGeometryChange16horizontalChangeEv',
    )

  def verticalChange(self) -> bool:
    """
    Calls Qt's 'bool QQuickGeometryChange::verticalChange() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeometrychange.html#verticalChange
    """
    #  bool QQuickGeometryChange::verticalChange() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickGeometryChange14verticalChangeEv',
    )

  @overload(THIS)
  def matches(self, other: QQuickGeometryChange) -> bool:
    """
    Calls Qt's 'bool QQuickGeometryChange::matches(QQuickGeometryChange
    other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgeometrychange.html#matches

    Parameters
    ----------

    other : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.
    """
    #  bool QQuickGeometryChange::matches(QQuickGeometryChange other) const
    return self.uglySide.call(
        'ritual_ZNK20QQuickGeometryChange7matchesES_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setXChange(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickGeometryChange::setXChange(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeometrychange.html#setXChange

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickGeometryChange::setXChange(bool enabled)
    self.uglySide.call(
        'ritual_ZN20QQuickGeometryChange10setXChangeEb', enabled,
    )

  @overload(bool)
  def setYChange(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickGeometryChange::setYChange(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeometrychange.html#setYChange

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickGeometryChange::setYChange(bool enabled)
    self.uglySide.call(
        'ritual_ZN20QQuickGeometryChange10setYChangeEb', enabled,
    )

  @overload(bool)
  def setWidthChange(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickGeometryChange::setWidthChange(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeometrychange.html#setWidthChange

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickGeometryChange::setWidthChange(bool enabled)
    self.uglySide.call(
        'ritual_ZN20QQuickGeometryChange14setWidthChangeEb', enabled,
    )

  @overload(bool)
  def setHeightChange(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickGeometryChange::setHeightChange(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeometrychange.html#setHeightChange

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickGeometryChange::setHeightChange(bool enabled)
    self.uglySide.call(
        'ritual_ZN20QQuickGeometryChange15setHeightChangeEb', enabled,
    )

  @overload(bool)
  def setSizeChange(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickGeometryChange::setSizeChange(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeometrychange.html#setSizeChange

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickGeometryChange::setSizeChange(bool enabled)
    self.uglySide.call(
        'ritual_ZN20QQuickGeometryChange13setSizeChangeEb', enabled,
    )

  @overload(bool)
  def setAllChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickGeometryChange::setAllChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeometrychange.html#setAllChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickGeometryChange::setAllChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN20QQuickGeometryChange13setAllChangedEb', enabled,
    )

  @overload(bool)
  def setHorizontalChange(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickGeometryChange::setHorizontalChange(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeometrychange.html#setHorizontalChange

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickGeometryChange::setHorizontalChange(bool enabled)
    self.uglySide.call(
        'ritual_ZN20QQuickGeometryChange19setHorizontalChangeEb', enabled,
    )

  @overload(bool)
  def setVerticalChange(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickGeometryChange::setVerticalChange(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeometrychange.html#setVerticalChange

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickGeometryChange::setVerticalChange(bool enabled)
    self.uglySide.call(
        'ritual_ZN20QQuickGeometryChange17setVerticalChangeEb', enabled,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(int)
  def __init__(self, change: int = 0) -> None:
    """
    Notes what was given, for Qt's
    'QQuickGeometryChange::QQuickGeometryChange(int change)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeometrychange.html#QQuickGeometryChange

    Parameters
    ----------

    change : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QQuickGeometryChange::QQuickGeometryChange(int change)
    self._noteCreation(QQuickGeometryChange, lambda: Rituals.call(
        'ritual_ZN20QQuickGeometryChangeC1Ei', change,
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

  @overload(int, bool)
  def set(self, bits: int, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickGeometryChange::set(int bits, bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgeometrychange.html#set

    Parameters
    ----------

    bits : int
      Passed on as it is.

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickGeometryChange::set(int bits, bool enabled)
    self.uglySide.call(
        'ritual_ZN20QQuickGeometryChange3setEib', bits, enabled,
    )
