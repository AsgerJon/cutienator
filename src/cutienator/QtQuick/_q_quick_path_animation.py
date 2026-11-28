"""
QQuickPathAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitemanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickPathAnimation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickAbstractAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEasingCurve, QMetaObject, QPointF
  from . import QQuickItem, QQuickPath, QQuickPathAnimationPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEasingCurve = WAIT['QEasingCurve']
  QPointF = WAIT['QPointF']
  QQuickItem = WAIT['QQuickItem']
  QQuickPath = WAIT['QQuickPath']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPathAnimation(QQuickAbstractAnimation):
  """
  The cute side of Qt's QQuickPathAnimation: a plain Python object standing
  in front of one C++ QQuickPathAnimation.

  It is built on the cute 'QQuickAbstractAnimation', as Qt's
  QQuickPathAnimation is built on Qt's QQuickAbstractAnimation, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPathAnimation that has a ritual and that
  Python can call so far, 30 names in all: 'metaObject', 'tr', 'd_func',
  'duration', 'setDuration', 'easing', 'setEasing', 'path', 'setPath',
  'target', 'setTargetObject', 'orientation', 'setOrientation',
  'anchorPoint', 'setAnchorPoint', 'orientationEntryDuration',
  'setOrientationEntryDuration', 'orientationExitDuration',
  'setOrientationExitDuration', 'endRotation', 'setEndRotation',
  'durationChanged', 'easingChanged', 'pathChanged', 'targetChanged',
  'orientationChanged', 'anchorPointChanged',
  'orientationEntryDurationChanged', 'orientationExitDurationChanged',
  'endRotationChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPathAnimation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickPathAnimation::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickPathAnimationPrivate *QQuickPathAnimation::d_func()
    const': takes in Python what 'QQuickPathAnimationPrivate
    *QQuickPathAnimation::d_func()' takes.
  - Qt's 'QQuickPathAnimation::~QQuickPathAnimation()': the destructor:
    Python never removes a C++ QQuickPathAnimation.
  - Qt's 'QAbstractAnimationJob
    *QQuickPathAnimation::transition(QQuickStateActions &actions,
    QQmlProperties &modified, TransitionDirection direction, QObject
    *defaultTarget)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  6 of the 42 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPathAnimation is created at the first use, not by
    'QQuickPathAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPathAnimation.
  - Qt tells when it has removed the C++ QQuickPathAnimation. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickPathAnimation, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Orientation(CuteNum):
    """
    The enum 'QQuickPathAnimation::Orientation' of Qt, with the 5 names Qt
    gives in it.
    """

    Fixed = Kee[int](0)
    RightFirst = Kee[int](1)
    LeftFirst = Kee[int](2)
    BottomFirst = Kee[int](3)
    TopFirst = Kee[int](4)

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
    Calls Qt's 'QString QQuickPathAnimation::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathanimation.html#tr

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
    #  QString QQuickPathAnimation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickPathAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPathAnimation'

  #  A C++ QQuickPathAnimation Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPathAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPathAnimation::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPathAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickPathAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def duration(self) -> int:
    """
    Calls Qt's 'int QQuickPathAnimation::duration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathanimation.html#duration
    """
    #  int QQuickPathAnimation::duration() const
    return self.uglySide.call('ritual_ZNK19QQuickPathAnimation8durationEv')

  def easing(self) -> QEasingCurve:
    """
    Calls Qt's 'QEasingCurve QQuickPathAnimation::easing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathanimation.html#easing

    Returns
    -------

    QEasingCurve
      A new cute QEasingCurve around the copy Qt gave back. Python owns it.
    """
    #  QEasingCurve QQuickPathAnimation::easing() const
    address = self.uglySide.call('ritual_ZNK19QQuickPathAnimation6easingEv')
    from ..QtCore import QEasingCurve
    return QEasingCurve._cuteOwning(address)

  def path(self) -> Optional[QQuickPath]:
    """
    Calls Qt's 'QQuickPath *QQuickPathAnimation::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathanimation.html#path

    Returns
    -------

    Optional[QQuickPath]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPath *QQuickPathAnimation::path() const
    address = self.uglySide.call('ritual_ZNK19QQuickPathAnimation4pathEv')
    from . import QQuickPath
    return QQuickPath._cuteAt(address)

  def target(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPathAnimation::target() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathanimation.html#target

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPathAnimation::target() const
    address = self.uglySide.call('ritual_ZNK19QQuickPathAnimation6targetEv')
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def orientation(self) -> Orientation:
    """
    Calls Qt's 'Orientation QQuickPathAnimation::orientation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html#orientation

    Returns
    -------

    Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Orientation(number)'
      gives.
    """
    #  Orientation QQuickPathAnimation::orientation() const
    return QQuickPathAnimation.Orientation(self.uglySide.call(
        'ritual_ZNK19QQuickPathAnimation11orientationEv',
    ))

  def anchorPoint(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickPathAnimation::anchorPoint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html#anchorPoint

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickPathAnimation::anchorPoint() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickPathAnimation11anchorPointEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def orientationEntryDuration(self) -> int:
    """
    Calls Qt's 'int QQuickPathAnimation::orientationEntryDuration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html#orientationEntryDuration
    """
    #  int QQuickPathAnimation::orientationEntryDuration() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickPathAnimation24orientationEntryDurationEv',
    )

  def orientationExitDuration(self) -> int:
    """
    Calls Qt's 'int QQuickPathAnimation::orientationExitDuration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html#orientationExitDuration
    """
    #  int QQuickPathAnimation::orientationExitDuration() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickPathAnimation23orientationExitDurationEv',
    )

  def endRotation(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathAnimation::endRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html#endRotation
    """
    #  qreal QQuickPathAnimation::endRotation() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickPathAnimation11endRotationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setDuration(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickPathAnimation::setDuration(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html#setDuration

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickPathAnimation::setDuration(int a0)
    self.uglySide.call('ritual_ZN19QQuickPathAnimation11setDurationEi', a0)

  @overload(QEasingCurve)
  def setEasing(self, a0: QEasingCurve) -> None:
    """
    Calls Qt's 'void QQuickPathAnimation::setEasing(const QEasingCurve &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathanimation.html#setEasing

    Parameters
    ----------

    a0 : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void QQuickPathAnimation::setEasing(const QEasingCurve &a0)
    self.uglySide.call(
        'ritual_ZN19QQuickPathAnimation9setEasingERK12QEasingCurve',
        self._valueOf(a0),
    )

  @overload(QQuickPath)
  @overload(NoneType)
  def setPath(self, a0: Optional[QQuickPath]) -> None:
    """
    Calls Qt's 'void QQuickPathAnimation::setPath(QQuickPath *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathanimation.html#setPath

    Parameters
    ----------

    a0 : Optional[QQuickPath]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPathAnimation::setPath(QQuickPath *a0)
    self.uglySide.call(
        'ritual_ZN19QQuickPathAnimation7setPathEP10QQuickPath',
        self._addressOf(a0),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setTargetObject(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickPathAnimation::setTargetObject(QQuickItem *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html#setTargetObject

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPathAnimation::setTargetObject(QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN19QQuickPathAnimation15setTargetObjectEP10QQuickItem',
        self._addressOf(a0),
    )

  @overload(Orientation)
  def setOrientation(self, orientation: Orientation) -> None:
    """
    Calls Qt's 'void QQuickPathAnimation::setOrientation(Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html#setOrientation

    Parameters
    ----------

    orientation : Orientation
      Passed on as its number.
    """
    #  void QQuickPathAnimation::setOrientation(Orientation orientation)
    self.uglySide.call(
        'ritual_ZN19QQuickPathAnimation14setOrientationENS_11OrientationE',
        orientation.value,
    )

  @overload(QPointF)
  def setAnchorPoint(self, point: QPointF) -> None:
    """
    Calls Qt's 'void QQuickPathAnimation::setAnchorPoint(const QPointF
    &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html#setAnchorPoint

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickPathAnimation::setAnchorPoint(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN19QQuickPathAnimation14setAnchorPointERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(int)
  def setOrientationEntryDuration(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickPathAnimation::setOrientationEntryDuration(int
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickPathAnimation::setOrientationEntryDuration(int a0)
    self.uglySide.call(
        'ritual_ZN19QQuickPathAnimation27setOrientationEntryDurationEi', a0,
    )

  @overload(int)
  def setOrientationExitDuration(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickPathAnimation::setOrientationExitDuration(int
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickPathAnimation::setOrientationExitDuration(int a0)
    self.uglySide.call(
        'ritual_ZN19QQuickPathAnimation26setOrientationExitDurationEi', a0,
    )

  @overload(float)
  def setEndRotation(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickPathAnimation::setEndRotation(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html#setEndRotation

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickPathAnimation::setEndRotation(qreal a0)
    self.uglySide.call(
        'ritual_ZN19QQuickPathAnimation14setEndRotationEd', a0,
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
    'QQuickPathAnimation::QQuickPathAnimation(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html#QQuickPathAnimation

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPathAnimation::QQuickPathAnimation(QObject *parent)
    self._noteCreation(QQuickPathAnimation, lambda: Rituals.call(
        'ritual_ZN19QQuickPathAnimationC1EP7QObject',
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

  def d_func(self) -> Optional[QQuickPathAnimationPrivate]:
    """
    Calls Qt's 'QQuickPathAnimationPrivate *QQuickPathAnimation::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathanimation.html#d_func

    Returns
    -------

    Optional[QQuickPathAnimationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPathAnimationPrivate *QQuickPathAnimation::d_func()
    address = self.uglySide.call('ritual_ZN19QQuickPathAnimation6d_funcEv')
    from . import QQuickPathAnimationPrivate
    return QQuickPathAnimationPrivate._cuteAt(address)

  @overload(int)
  def durationChanged(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickPathAnimation::durationChanged(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html#durationChanged

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickPathAnimation::durationChanged(int a0)
    self.uglySide.call(
        'ritual_ZN19QQuickPathAnimation15durationChangedEi', a0,
    )

  @overload(QEasingCurve)
  def easingChanged(self, a0: QEasingCurve) -> None:
    """
    Calls Qt's 'void QQuickPathAnimation::easingChanged(const QEasingCurve
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html#easingChanged

    Parameters
    ----------

    a0 : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void QQuickPathAnimation::easingChanged(const QEasingCurve &a0)
    self.uglySide.call(
        'ritual_ZN19QQuickPathAnimation13easingChangedERK12QEasingCurve',
        self._valueOf(a0),
    )

  def pathChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathAnimation::pathChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html#pathChanged
    """
    #  void QQuickPathAnimation::pathChanged()
    self.uglySide.call('ritual_ZN19QQuickPathAnimation11pathChangedEv')

  def targetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathAnimation::targetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html#targetChanged
    """
    #  void QQuickPathAnimation::targetChanged()
    self.uglySide.call('ritual_ZN19QQuickPathAnimation13targetChangedEv')

  @overload(Orientation)
  def orientationChanged(self, a0: Orientation) -> None:
    """
    Calls Qt's 'void
    QQuickPathAnimation::orientationChanged(QQuickPathAnimation::Orientation
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html#orientationChanged

    Parameters
    ----------

    a0 : Orientation
      Passed on as its number.
    """
    #  void QQuickPathAnimation::orientationChanged(QQuickPathAnimation::
    #      Orientation a0)
    self.uglySide.call(
        'ritual_ZN19QQuickPathAnimation18orientationChangedENS_11Orientatio'
        'nE',
        a0.value,
    )

  @overload(QPointF)
  def anchorPointChanged(self, a0: QPointF) -> None:
    """
    Calls Qt's 'void QQuickPathAnimation::anchorPointChanged(const QPointF
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html#anchorPointChanged

    Parameters
    ----------

    a0 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickPathAnimation::anchorPointChanged(const QPointF &a0)
    self.uglySide.call(
        'ritual_ZN19QQuickPathAnimation18anchorPointChangedERK7QPointF',
        self._valueOf(a0, 'QPointF'),
    )

  @overload(float)
  def orientationEntryDurationChanged(self, a0: float) -> None:
    """
    Calls Qt's 'void
    QQuickPathAnimation::orientationEntryDurationChanged(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickPathAnimation::orientationEntryDurationChanged(qreal a0)
    self.uglySide.call(
        'ritual_ZN19QQuickPathAnimation31orientationEntryDurationChangedEd',
        a0,
    )

  @overload(float)
  def orientationExitDurationChanged(self, a0: float) -> None:
    """
    Calls Qt's 'void
    QQuickPathAnimation::orientationExitDurationChanged(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickPathAnimation::orientationExitDurationChanged(qreal a0)
    self.uglySide.call(
        'ritual_ZN19QQuickPathAnimation30orientationExitDurationChangedEd',
        a0,
    )

  @overload(float)
  def endRotationChanged(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickPathAnimation::endRotationChanged(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimation.html#endRotationChanged

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickPathAnimation::endRotationChanged(qreal a0)
    self.uglySide.call(
        'ritual_ZN19QQuickPathAnimation18endRotationChangedEd', a0,
    )
