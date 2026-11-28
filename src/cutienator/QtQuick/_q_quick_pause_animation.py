"""
QQuickPauseAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickPauseAnimation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickAbstractAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickPauseAnimationPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPauseAnimation(QQuickAbstractAnimation):
  """
  The cute side of Qt's QQuickPauseAnimation: a plain Python object standing
  in front of one C++ QQuickPauseAnimation.

  It is built on the cute 'QQuickAbstractAnimation', as Qt's
  QQuickPauseAnimation is built on Qt's QQuickAbstractAnimation, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPauseAnimation that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr', 'd_func',
  'duration', 'setDuration', 'durationChanged'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPauseAnimation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickPauseAnimation::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickPauseAnimationPrivate *QQuickPauseAnimation::d_func()
    const': takes in Python what 'QQuickPauseAnimationPrivate
    *QQuickPauseAnimation::d_func()' takes.
  - Qt's 'QQuickPauseAnimation::~QQuickPauseAnimation()': the destructor:
    Python never removes a C++ QQuickPauseAnimation.
  - Qt's 'QAbstractAnimationJob
    *QQuickPauseAnimation::transition(QQuickStateActions &actions,
    QQmlProperties &modified, TransitionDirection direction, QObject
    *defaultTarget)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPauseAnimation is created at the first use, not by
    'QQuickPauseAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPauseAnimation.
  - Qt tells when it has removed the C++ QQuickPauseAnimation. Every call on
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
    Calls Qt's 'QString QQuickPauseAnimation::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpauseanimation.html#tr

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
    #  QString QQuickPauseAnimation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickPauseAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPauseAnimation'

  #  A C++ QQuickPauseAnimation Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPauseAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPauseAnimation::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpauseanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPauseAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickPauseAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def duration(self) -> int:
    """
    Calls Qt's 'int QQuickPauseAnimation::duration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpauseanimation.html#duration
    """
    #  int QQuickPauseAnimation::duration() const
    return self.uglySide.call('ritual_ZNK20QQuickPauseAnimation8durationEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setDuration(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickPauseAnimation::setDuration(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpauseanimation.html#setDuration

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickPauseAnimation::setDuration(int a0)
    self.uglySide.call('ritual_ZN20QQuickPauseAnimation11setDurationEi', a0)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickPauseAnimation::QQuickPauseAnimation(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpauseanimation.html#QQuickPauseAnimation

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPauseAnimation::QQuickPauseAnimation(QObject *parent)
    self._noteCreation(QQuickPauseAnimation, lambda: Rituals.call(
        'ritual_ZN20QQuickPauseAnimationC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QQuickPauseAnimationPrivate]:
    """
    Calls Qt's 'QQuickPauseAnimationPrivate *QQuickPauseAnimation::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpauseanimation.html#d_func

    Returns
    -------

    Optional[QQuickPauseAnimationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPauseAnimationPrivate *QQuickPauseAnimation::d_func()
    address = self.uglySide.call('ritual_ZN20QQuickPauseAnimation6d_funcEv')
    from . import QQuickPauseAnimationPrivate
    return QQuickPauseAnimationPrivate._cuteAt(address)

  @overload(int)
  def durationChanged(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickPauseAnimation::durationChanged(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpauseanimation.html#durationChanged

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickPauseAnimation::durationChanged(int a0)
    self.uglySide.call(
        'ritual_ZN20QQuickPauseAnimation15durationChangedEi', a0,
    )
