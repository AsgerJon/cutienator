"""
QQmlMarginsFValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlMarginsFValueType to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QMarginsF

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QMargins
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMargins = WAIT['QMargins']


class QQmlMarginsFValueType(QMarginsF):
  """
  The cute side of Qt's QQmlMarginsFValueType: a plain Python object standing
  in front of one C++ QQmlMarginsFValueType.

  It is built on the cute 'QMarginsF', as Qt's QQmlMarginsFValueType is built
  on Qt's QMarginsF, and has everything that class has.

  C++ hands a QQmlMarginsFValueType around as a copy, so every C++
  QQmlMarginsFValueType behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlMarginsFValueType that has a ritual and that
  Python can call so far, 9 names in all: 'toString', 'left', 'right', 'top',
  'bottom', 'setLeft', 'setRight', 'setTop', 'setBottom'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlMarginsFValueType::qt_qmlMarker_anonymous()': one of Qt's
    own inner workings.
  - Qt's 'void QQmlMarginsFValueType::qt_qmlMarker_foreign()': one of Qt's
    own inner workings.
  - Qt's 'void QQmlMarginsFValueType::qt_qmlMarker_extended()': one of Qt's
    own inner workings.
  - Qt's 'QQmlMarginsFValueType::~QQmlMarginsFValueType()': the destructor:
    Python removes its C++ QQmlMarginsFValueType by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 19 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQmlMarginsFValueType is created at the first use, not by
    'QQmlMarginsFValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlMarginsFValueType back gives a copy the ritual
    made for Python, in a new cute QQmlMarginsFValueType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlMarginsFValueType'

  #  Qt's '~QQmlMarginsFValueType()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlMarginsFValueType behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QQmlMarginsFValueTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QQmlMarginsFValueType::toString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmarginsfvaluetype.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlMarginsFValueType::toString() const
    return self.uglySide.call('ritual_ZNK21QQmlMarginsFValueType8toStringEv')

  def left(self) -> float:
    """
    Calls Qt's 'qreal QQmlMarginsFValueType::left() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmarginsfvaluetype.html#left
    """
    #  qreal QQmlMarginsFValueType::left() const
    return self.uglySide.call('ritual_ZNK21QQmlMarginsFValueType4leftEv')

  def right(self) -> float:
    """
    Calls Qt's 'qreal QQmlMarginsFValueType::right() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmarginsfvaluetype.html#right
    """
    #  qreal QQmlMarginsFValueType::right() const
    return self.uglySide.call('ritual_ZNK21QQmlMarginsFValueType5rightEv')

  def top(self) -> float:
    """
    Calls Qt's 'qreal QQmlMarginsFValueType::top() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmarginsfvaluetype.html#top
    """
    #  qreal QQmlMarginsFValueType::top() const
    return self.uglySide.call('ritual_ZNK21QQmlMarginsFValueType3topEv')

  def bottom(self) -> float:
    """
    Calls Qt's 'qreal QQmlMarginsFValueType::bottom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmarginsfvaluetype.html#bottom
    """
    #  qreal QQmlMarginsFValueType::bottom() const
    return self.uglySide.call('ritual_ZNK21QQmlMarginsFValueType6bottomEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setLeft(self, a0: float) -> None:
    """
    Calls Qt's 'void QQmlMarginsFValueType::setLeft(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmarginsfvaluetype.html#setLeft

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQmlMarginsFValueType::setLeft(qreal a0)
    self.uglySide.call('ritual_ZN21QQmlMarginsFValueType7setLeftEd', a0)

  @overload(float)
  def setRight(self, a0: float) -> None:
    """
    Calls Qt's 'void QQmlMarginsFValueType::setRight(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmarginsfvaluetype.html#setRight

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQmlMarginsFValueType::setRight(qreal a0)
    self.uglySide.call('ritual_ZN21QQmlMarginsFValueType8setRightEd', a0)

  @overload(float)
  def setTop(self, a0: float) -> None:
    """
    Calls Qt's 'void QQmlMarginsFValueType::setTop(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmarginsfvaluetype.html#setTop

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQmlMarginsFValueType::setTop(qreal a0)
    self.uglySide.call('ritual_ZN21QQmlMarginsFValueType6setTopEd', a0)

  @overload(float)
  def setBottom(self, a0: float) -> None:
    """
    Calls Qt's 'void QQmlMarginsFValueType::setBottom(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmarginsfvaluetype.html#setBottom

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQmlMarginsFValueType::setBottom(qreal a0)
    self.uglySide.call('ritual_ZN21QQmlMarginsFValueType9setBottomEd', a0)

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
    'QQmlMarginsFValueType::QQmlMarginsFValueType()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmarginsfvaluetype.html#QQmlMarginsFValueType
    """
    #  QQmlMarginsFValueType::QQmlMarginsFValueType()
    self._noteCreation(QQmlMarginsFValueType, lambda: Rituals.call(
        'ritual_ZN21QQmlMarginsFValueTypeC1Ev',
    ))

  @overload(QMarginsF)
  def __init__(self, margins: QMarginsF) -> None:
    """
    Notes what was given, for Qt's
    'QQmlMarginsFValueType::QQmlMarginsFValueType(const QMarginsF &margins)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmarginsfvaluetype.html#QQmlMarginsFValueType

    Parameters
    ----------

    margins : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.
    """
    #  QQmlMarginsFValueType::QQmlMarginsFValueType(const QMarginsF &margins)
    self._noteCreation(QQmlMarginsFValueType, lambda: Rituals.call(
        'ritual_ZN21QQmlMarginsFValueTypeC1ERK9QMarginsF',
        self._valueOf(margins),
    ))

  @overload(QMargins)
  def __init__(self, margins: QMargins) -> None:
    """
    Notes what was given, for Qt's
    'QQmlMarginsFValueType::QQmlMarginsFValueType(const QMargins &margins)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmarginsfvaluetype.html#QQmlMarginsFValueType

    Parameters
    ----------

    margins : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.
    """
    #  QQmlMarginsFValueType::QQmlMarginsFValueType(const QMargins &margins)
    self._noteCreation(QQmlMarginsFValueType, lambda: Rituals.call(
        'ritual_ZN21QQmlMarginsFValueTypeC1ERK8QMargins',
        self._valueOf(margins, 'QMargins'),
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
