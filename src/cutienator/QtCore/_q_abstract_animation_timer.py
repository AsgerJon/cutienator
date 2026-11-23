"""
QAbstractAnimationTimer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qabstractanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAbstractAnimationTimer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractAnimationTimer(QObject):
  """
  The cute side of Qt's QAbstractAnimationTimer: a plain Python object
  standing in front of one C++ QAbstractAnimationTimer.

  It is built on the cute 'QObject', as Qt's QAbstractAnimationTimer is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractAnimationTimer that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'tr',
  'updateAnimationsTime', 'restartAnimationTimer', 'runningAnimationCount'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractAnimationTimer::~QAbstractAnimationTimer()': the
    destructor: Python never removes a C++ QAbstractAnimationTimer.

  What has no ritual
  ------------------

  5 of the 11 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 1 a template; 1 declared and nowhere to be found; 1 the class
  is abstract, so C++ cannot make one.

  What to expect
  --------------

  - The C++ QAbstractAnimationTimer is created at the first use, not by
    'QAbstractAnimationTimer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractAnimationTimer.
  - Qt tells when it has removed the C++ QAbstractAnimationTimer. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QAbstractAnimationTimer::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractanimationtimer.html#tr

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
    #  QString QAbstractAnimationTimer::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QAbstractAnimationTimer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractAnimationTimer'

  #  A C++ QAbstractAnimationTimer Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractAnimationTimer'

  #  The functions Qt calls itself that QAbstractAnimationTimer is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'updateAnimationsTime': (
          ('_ZN23QAbstractAnimationTimer20updateAnimationsTimeEx',
           ('nothing', 'nothing', ''),
           (
               ('long long', 'number', ''),
           )),
      ),
      'restartAnimationTimer': (
          ('_ZN23QAbstractAnimationTimer21restartAnimationTimerEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'runningAnimationCount': (
          ('_ZNK23QAbstractAnimationTimer21runningAnimationCountEv',
           ('long long', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstractAnimationTimer::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationtimer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractAnimationTimer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QAbstractAnimationTimer10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def runningAnimationCount(self) -> int:
    """
    Calls Qt's 'qsizetype QAbstractAnimationTimer::runningAnimationCount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationtimer.html#runningAnimationCount
    """
    #  qsizetype QAbstractAnimationTimer::runningAnimationCount() const
    return self.uglySide.call(
        'ritual_ZNK23QAbstractAnimationTimer21runningAnimationCountEv',
    )

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

  @overload(int)
  def updateAnimationsTime(self, delta: int) -> None:
    """
    Calls Qt's 'void QAbstractAnimationTimer::updateAnimationsTime(qint64
    delta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationtimer.html#updateAnimationsTime

    Parameters
    ----------

    delta : int
      Passed on as it is.
    """
    #  void QAbstractAnimationTimer::updateAnimationsTime(qint64 delta)
    self.uglySide.call(
        'ritual_ZN23QAbstractAnimationTimer20updateAnimationsTimeEx', delta,
    )

  def restartAnimationTimer(self) -> None:
    """
    Calls Qt's 'void QAbstractAnimationTimer::restartAnimationTimer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationtimer.html#restartAnimationTimer
    """
    #  void QAbstractAnimationTimer::restartAnimationTimer()
    self.uglySide.call(
        'ritual_ZN23QAbstractAnimationTimer21restartAnimationTimerEv',
    )
