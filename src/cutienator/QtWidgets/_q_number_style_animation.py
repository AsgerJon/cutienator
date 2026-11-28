"""
QNumberStyleAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qstyleanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QNumberStyleAnimation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QStyleAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNumberStyleAnimation(QStyleAnimation):
  """
  The cute side of Qt's QNumberStyleAnimation: a plain Python object standing
  in front of one C++ QNumberStyleAnimation.

  It is built on the cute 'QStyleAnimation', as Qt's QNumberStyleAnimation is
  built on Qt's QStyleAnimation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNumberStyleAnimation that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr', 'startValue',
  'setStartValue', 'endValue', 'setEndValue', 'currentValue',
  'isUpdateNeeded'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNumberStyleAnimation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QNumberStyleAnimation::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QNumberStyleAnimation is created at the first use, not by
    'QNumberStyleAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNumberStyleAnimation.
  - Qt tells when it has removed the C++ QNumberStyleAnimation. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QNumberStyleAnimation::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qnumberstyleanimation.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNumberStyleAnimation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QNumberStyleAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNumberStyleAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QNumberStyleAnimation::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnumberstyleanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNumberStyleAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QNumberStyleAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def startValue(self) -> float:
    """
    Calls Qt's 'qreal QNumberStyleAnimation::startValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnumberstyleanimation.html#startValue
    """
    #  qreal QNumberStyleAnimation::startValue() const
    return self.uglySide.call(
        'ritual_ZNK21QNumberStyleAnimation10startValueEv',
    )

  def endValue(self) -> float:
    """
    Calls Qt's 'qreal QNumberStyleAnimation::endValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnumberstyleanimation.html#endValue
    """
    #  qreal QNumberStyleAnimation::endValue() const
    return self.uglySide.call('ritual_ZNK21QNumberStyleAnimation8endValueEv')

  def currentValue(self) -> float:
    """
    Calls Qt's 'qreal QNumberStyleAnimation::currentValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnumberstyleanimation.html#currentValue
    """
    #  qreal QNumberStyleAnimation::currentValue() const
    return self.uglySide.call(
        'ritual_ZNK21QNumberStyleAnimation12currentValueEv',
    )

  def isUpdateNeeded(self) -> bool:
    """
    Calls Qt's 'bool QNumberStyleAnimation::isUpdateNeeded() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnumberstyleanimation.html#isUpdateNeeded
    """
    #  bool QNumberStyleAnimation::isUpdateNeeded() const
    ritual = 'ritual_ZNK21QNumberStyleAnimation14isUpdateNeededEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QNumberStyleAnimation14isUpdateNeededEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setStartValue(self, value: float) -> None:
    """
    Calls Qt's 'void QNumberStyleAnimation::setStartValue(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnumberstyleanimation.html#setStartValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QNumberStyleAnimation::setStartValue(qreal value)
    self.uglySide.call(
        'ritual_ZN21QNumberStyleAnimation13setStartValueEd', value,
    )

  @overload(float)
  def setEndValue(self, value: float) -> None:
    """
    Calls Qt's 'void QNumberStyleAnimation::setEndValue(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnumberstyleanimation.html#setEndValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QNumberStyleAnimation::setEndValue(qreal value)
    self.uglySide.call(
        'ritual_ZN21QNumberStyleAnimation11setEndValueEd', value,
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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, target: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QNumberStyleAnimation::QNumberStyleAnimation(QObject *target)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnumberstyleanimation.html#QNumberStyleAnimation

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QNumberStyleAnimation::QNumberStyleAnimation(QObject *target)
    self._noteCreation(QNumberStyleAnimation, lambda: Rituals.call(
        'ritual_ZN21QNumberStyleAnimationC1EP7QObject',
        self._addressOf(target, 'QObject'),
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
