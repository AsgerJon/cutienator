"""
QQuickAnchorAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitemanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickAnchorAnimation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickAbstractAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEasingCurve, QMetaObject
  from . import QQuickAnchorAnimationPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEasingCurve = WAIT['QEasingCurve']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAnchorAnimation(QQuickAbstractAnimation):
  """
  The cute side of Qt's QQuickAnchorAnimation: a plain Python object standing
  in front of one C++ QQuickAnchorAnimation.

  It is built on the cute 'QQuickAbstractAnimation', as Qt's
  QQuickAnchorAnimation is built on Qt's QQuickAbstractAnimation, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAnchorAnimation that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'd_func',
  'duration', 'setDuration', 'easing', 'setEasing', 'durationChanged',
  'easingChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickAnchorAnimation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickAnchorAnimation::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickAnchorAnimationPrivate *QQuickAnchorAnimation::d_func()
    const': takes in Python what 'QQuickAnchorAnimationPrivate
    *QQuickAnchorAnimation::d_func()' takes.
  - Qt's 'QQmlListProperty<QQuickItem> QQuickAnchorAnimation::targets()':
    gives a type Python has no way to take yet.
  - Qt's 'QAbstractAnimationJob
    *QQuickAnchorAnimation::transition(QQuickStateActions &actions,
    QQmlProperties &modified, TransitionDirection direction, QObject
    *defaultTarget)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickAnchorAnimation is created at the first use, not by
    'QQuickAnchorAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAnchorAnimation.
  - Qt tells when it has removed the C++ QQuickAnchorAnimation. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickAnchorAnimation that has no cute function yet,
    'targets', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QQuickAnchorAnimation::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchoranimation.html#tr

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
    #  QString QQuickAnchorAnimation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickAnchorAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAnchorAnimation'

  #  A C++ QQuickAnchorAnimation Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAnchorAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickAnchorAnimation::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchoranimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickAnchorAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickAnchorAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def duration(self) -> int:
    """
    Calls Qt's 'int QQuickAnchorAnimation::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchoranimation.html#duration
    """
    #  int QQuickAnchorAnimation::duration() const
    return self.uglySide.call('ritual_ZNK21QQuickAnchorAnimation8durationEv')

  def easing(self) -> QEasingCurve:
    """
    Calls Qt's 'QEasingCurve QQuickAnchorAnimation::easing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchoranimation.html#easing

    Returns
    -------

    QEasingCurve
      A new cute QEasingCurve around the copy Qt gave back. Python owns it.
    """
    #  QEasingCurve QQuickAnchorAnimation::easing() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickAnchorAnimation6easingEv',
    )
    from ..QtCore import QEasingCurve
    return QEasingCurve._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setDuration(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickAnchorAnimation::setDuration(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchoranimation.html#setDuration

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickAnchorAnimation::setDuration(int a0)
    self.uglySide.call('ritual_ZN21QQuickAnchorAnimation11setDurationEi', a0)

  @overload(QEasingCurve)
  def setEasing(self, a0: QEasingCurve) -> None:
    """
    Calls Qt's 'void QQuickAnchorAnimation::setEasing(const QEasingCurve
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchoranimation.html#setEasing

    Parameters
    ----------

    a0 : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void QQuickAnchorAnimation::setEasing(const QEasingCurve &a0)
    self.uglySide.call(
        'ritual_ZN21QQuickAnchorAnimation9setEasingERK12QEasingCurve',
        self._valueOf(a0),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickAnchorAnimation::QQuickAnchorAnimation(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchoranimation.html#QQuickAnchorAnimation

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickAnchorAnimation::QQuickAnchorAnimation(QObject *parent)
    self._noteCreation(QQuickAnchorAnimation, lambda: Rituals.call(
        'ritual_ZN21QQuickAnchorAnimationC1EP7QObject',
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

  def d_func(self) -> Optional[QQuickAnchorAnimationPrivate]:
    """
    Calls Qt's 'QQuickAnchorAnimationPrivate
    *QQuickAnchorAnimation::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchoranimation.html#d_func

    Returns
    -------

    Optional[QQuickAnchorAnimationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAnchorAnimationPrivate *QQuickAnchorAnimation::d_func()
    address = self.uglySide.call('ritual_ZN21QQuickAnchorAnimation6d_funcEv')
    from . import QQuickAnchorAnimationPrivate
    return QQuickAnchorAnimationPrivate._cuteAt(address)

  @overload(int)
  def durationChanged(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickAnchorAnimation::durationChanged(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchoranimation.html#durationChanged

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickAnchorAnimation::durationChanged(int a0)
    self.uglySide.call(
        'ritual_ZN21QQuickAnchorAnimation15durationChangedEi', a0,
    )

  @overload(QEasingCurve)
  def easingChanged(self, a0: QEasingCurve) -> None:
    """
    Calls Qt's 'void QQuickAnchorAnimation::easingChanged(const QEasingCurve
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchoranimation.html#easingChanged

    Parameters
    ----------

    a0 : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void QQuickAnchorAnimation::easingChanged(const QEasingCurve &a0)
    self.uglySide.call(
        'ritual_ZN21QQuickAnchorAnimation13easingChangedERK12QEasingCurve',
        self._valueOf(a0),
    )

  @staticmethod
  def targets(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickItem> QQuickAnchorAnimation::targets()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickAnchorAnimation.targets' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickItem> QQuickAnchorAnimation::targets()': "
        "gives a type Python has no way to take yet.")
