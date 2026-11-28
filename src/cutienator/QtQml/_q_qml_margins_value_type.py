"""
QQmlMarginsValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlMarginsValueType to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QMargins

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QMarginsF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMarginsF = WAIT['QMarginsF']


class QQmlMarginsValueType(QMargins):
  """
  The cute side of Qt's QQmlMarginsValueType: a plain Python object standing
  in front of one C++ QQmlMarginsValueType.

  It is built on the cute 'QMargins', as Qt's QQmlMarginsValueType is built
  on Qt's QMargins, and has everything that class has.

  C++ hands a QQmlMarginsValueType around as a copy, so every C++
  QQmlMarginsValueType behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlMarginsValueType that has a ritual and that
  Python can call so far, 9 names in all: 'toString', 'left', 'right', 'top',
  'bottom', 'setLeft', 'setRight', 'setTop', 'setBottom'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlMarginsValueType::qt_qmlMarker_anonymous()': one of Qt's
    own inner workings.
  - Qt's 'void QQmlMarginsValueType::qt_qmlMarker_foreign()': one of Qt's own
    inner workings.
  - Qt's 'void QQmlMarginsValueType::qt_qmlMarker_extended()': one of Qt's
    own inner workings.
  - Qt's 'QQmlMarginsValueType::~QQmlMarginsValueType()': the destructor:
    Python removes its C++ QQmlMarginsValueType by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 19 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQmlMarginsValueType is created at the first use, not by
    'QQmlMarginsValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlMarginsValueType back gives a copy the ritual
    made for Python, in a new cute QQmlMarginsValueType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlMarginsValueType'

  #  Qt's '~QQmlMarginsValueType()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlMarginsValueType behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QQmlMarginsValueTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QQmlMarginsValueType::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmarginsvaluetype.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlMarginsValueType::toString() const
    return self.uglySide.call('ritual_ZNK20QQmlMarginsValueType8toStringEv')

  def left(self) -> int:
    """
    Calls Qt's 'int QQmlMarginsValueType::left() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmarginsvaluetype.html#left
    """
    #  int QQmlMarginsValueType::left() const
    return self.uglySide.call('ritual_ZNK20QQmlMarginsValueType4leftEv')

  def right(self) -> int:
    """
    Calls Qt's 'int QQmlMarginsValueType::right() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmarginsvaluetype.html#right
    """
    #  int QQmlMarginsValueType::right() const
    return self.uglySide.call('ritual_ZNK20QQmlMarginsValueType5rightEv')

  def top(self) -> int:
    """
    Calls Qt's 'int QQmlMarginsValueType::top() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmarginsvaluetype.html#top
    """
    #  int QQmlMarginsValueType::top() const
    return self.uglySide.call('ritual_ZNK20QQmlMarginsValueType3topEv')

  def bottom(self) -> int:
    """
    Calls Qt's 'int QQmlMarginsValueType::bottom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmarginsvaluetype.html#bottom
    """
    #  int QQmlMarginsValueType::bottom() const
    return self.uglySide.call('ritual_ZNK20QQmlMarginsValueType6bottomEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setLeft(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlMarginsValueType::setLeft(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmarginsvaluetype.html#setLeft

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlMarginsValueType::setLeft(int a0)
    self.uglySide.call('ritual_ZN20QQmlMarginsValueType7setLeftEi', a0)

  @overload(int)
  def setRight(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlMarginsValueType::setRight(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmarginsvaluetype.html#setRight

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlMarginsValueType::setRight(int a0)
    self.uglySide.call('ritual_ZN20QQmlMarginsValueType8setRightEi', a0)

  @overload(int)
  def setTop(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlMarginsValueType::setTop(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmarginsvaluetype.html#setTop

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlMarginsValueType::setTop(int a0)
    self.uglySide.call('ritual_ZN20QQmlMarginsValueType6setTopEi', a0)

  @overload(int)
  def setBottom(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlMarginsValueType::setBottom(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmarginsvaluetype.html#setBottom

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlMarginsValueType::setBottom(int a0)
    self.uglySide.call('ritual_ZN20QQmlMarginsValueType9setBottomEi', a0)

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQmlMarginsValueType::QQmlMarginsValueType()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmarginsvaluetype.html#QQmlMarginsValueType
    """
    #  QQmlMarginsValueType::QQmlMarginsValueType()
    self._noteCreation(QQmlMarginsValueType, lambda: Rituals.call(
        'ritual_ZN20QQmlMarginsValueTypeC1Ev',
    ))

  @overload(QMargins)
  def __init__(self, margins: QMargins) -> None:
    """
    Notes what was given, for Qt's
    'QQmlMarginsValueType::QQmlMarginsValueType(const QMargins &margins)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmarginsvaluetype.html#QQmlMarginsValueType

    Parameters
    ----------

    margins : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.
    """
    #  QQmlMarginsValueType::QQmlMarginsValueType(const QMargins &margins)
    self._noteCreation(QQmlMarginsValueType, lambda: Rituals.call(
        'ritual_ZN20QQmlMarginsValueTypeC1ERK8QMargins',
        self._valueOf(margins, 'QMargins'),
    ))

  @overload(QMarginsF)
  def __init__(self, margins: QMarginsF) -> None:
    """
    Notes what was given, for Qt's
    'QQmlMarginsValueType::QQmlMarginsValueType(const QMarginsF &margins)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmarginsvaluetype.html#QQmlMarginsValueType

    Parameters
    ----------

    margins : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.
    """
    #  QQmlMarginsValueType::QQmlMarginsValueType(const QMarginsF &margins)
    self._noteCreation(QQmlMarginsValueType, lambda: Rituals.call(
        'ritual_ZN20QQmlMarginsValueTypeC1ERK9QMarginsF',
        self._valueOf(margins),
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
