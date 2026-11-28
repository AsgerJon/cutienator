"""
QBarCategoryAxisPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qbarcategoryaxis_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QBarCategoryAxisPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAbstractAxisPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
  from . import QBarCategoryAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QBarCategoryAxisPrivate(QAbstractAxisPrivate):
  """
  The cute side of Qt's QBarCategoryAxisPrivate: a plain Python object
  standing in front of one C++ QBarCategoryAxisPrivate.

  It is built on the cute 'QAbstractAxisPrivate', as Qt's
  QBarCategoryAxisPrivate is built on Qt's QAbstractAxisPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QBarCategoryAxisPrivate that has a ritual and that
  Python can call so far, 6 names in all: 'setRange', 'setMin', 'setMax',
  'min', 'max', 'q_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBarCategoryAxisPrivate::~QBarCategoryAxisPrivate()': the
    destructor: Python never removes a C++ QBarCategoryAxisPrivate.
  - Qt's 'const QBarCategoryAxis *QBarCategoryAxisPrivate::q_func() const':
    takes in Python what 'QBarCategoryAxis
    *QBarCategoryAxisPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QBarCategoryAxisPrivate is created at the first use, not by
    'QBarCategoryAxisPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBarCategoryAxisPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBarCategoryAxisPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QBarCategoryAxisPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBarCategoryAxisPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant, QVariant)
  def setRange(self, min: QVariant, max: QVariant) -> None:
    """
    Calls Qt's 'void QBarCategoryAxisPrivate::setRange(const QVariant &min,
    const QVariant &max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarcategoryaxisprivate.html#setRange

    Parameters
    ----------

    min : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    max : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QBarCategoryAxisPrivate::setRange(const QVariant &min, const
    #      QVariant &max)
    ritual = 'ritual_ZN23QBarCategoryAxisPrivate8setRangeERK8QVariantS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QBarCategoryAxisPrivate8setRangeERK8QVariantS2_')
    self.uglySide.call(ritual, self._valueOf(min), self._valueOf(max))

  @overload(float, float)
  def setRange(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QBarCategoryAxisPrivate::setRange(qreal min, qreal
    max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarcategoryaxisprivate.html#setRange

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QBarCategoryAxisPrivate::setRange(qreal min, qreal max)
    ritual = 'ritual_ZN23QBarCategoryAxisPrivate8setRangeEdd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QBarCategoryAxisPrivate8setRangeEdd'
    self.uglySide.call(ritual, min, max)

  @overload(str, str)
  def setRange(self, minCategory: str, maxCategory: str) -> None:
    """
    Calls Qt's 'void QBarCategoryAxisPrivate::setRange(const QString
    &minCategory, const QString &maxCategory)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarcategoryaxisprivate.html#setRange

    Parameters
    ----------

    minCategory : str
      Passed on as it is: a QString is made of it for the call.

    maxCategory : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBarCategoryAxisPrivate::setRange(const QString &minCategory,
    #      const QString &maxCategory)
    self.uglySide.call(
        'ritual_ZN23QBarCategoryAxisPrivate8setRangeERK7QStringS2_',
        minCategory, maxCategory,
    )

  @overload(QVariant)
  def setMin(self, min: QVariant) -> None:
    """
    Calls Qt's 'void QBarCategoryAxisPrivate::setMin(const QVariant &min)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarcategoryaxisprivate.html#setMin

    Parameters
    ----------

    min : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QBarCategoryAxisPrivate::setMin(const QVariant &min)
    ritual = 'ritual_ZN23QBarCategoryAxisPrivate6setMinERK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QBarCategoryAxisPrivate6setMinERK8QVariant'
    self.uglySide.call(ritual, self._valueOf(min))

  @overload(QVariant)
  def setMax(self, max: QVariant) -> None:
    """
    Calls Qt's 'void QBarCategoryAxisPrivate::setMax(const QVariant &max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarcategoryaxisprivate.html#setMax

    Parameters
    ----------

    max : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QBarCategoryAxisPrivate::setMax(const QVariant &max)
    ritual = 'ritual_ZN23QBarCategoryAxisPrivate6setMaxERK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QBarCategoryAxisPrivate6setMaxERK8QVariant'
    self.uglySide.call(ritual, self._valueOf(max))

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
    'QBarCategoryAxisPrivate::QBarCategoryAxisPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarcategoryaxisprivate.html
    """
    #  QBarCategoryAxisPrivate::QBarCategoryAxisPrivate()
    self._noteCreation(QBarCategoryAxisPrivate, lambda: Rituals.call(
        'ritual_ZN23QBarCategoryAxisPrivateC1Ev',
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

  def min(self) -> float:
    """
    Calls Qt's 'qreal QBarCategoryAxisPrivate::min()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxisprivate.html#min
    """
    #  qreal QBarCategoryAxisPrivate::min()
    ritual = 'ritual_ZN23QBarCategoryAxisPrivate3minEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QBarCategoryAxisPrivate3minEv'
    return self.uglySide.call(ritual)

  def max(self) -> float:
    """
    Calls Qt's 'qreal QBarCategoryAxisPrivate::max()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarcategoryaxisprivate.html#max
    """
    #  qreal QBarCategoryAxisPrivate::max()
    ritual = 'ritual_ZN23QBarCategoryAxisPrivate3maxEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QBarCategoryAxisPrivate3maxEv'
    return self.uglySide.call(ritual)

  def q_func(self) -> Optional[QBarCategoryAxis]:
    """
    Calls Qt's 'QBarCategoryAxis *QBarCategoryAxisPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarcategoryaxisprivate.html#q_func

    Returns
    -------

    Optional[QBarCategoryAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBarCategoryAxis *QBarCategoryAxisPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN23QBarCategoryAxisPrivate6q_funcEv',
    )
    from . import QBarCategoryAxis
    return QBarCategoryAxis._cuteAt(address)
