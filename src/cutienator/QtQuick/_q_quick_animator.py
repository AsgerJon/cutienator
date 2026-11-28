"""
QQuickAnimator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimator_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickAnimator to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickAbstractAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEasingCurve, QMetaObject
  from . import QQuickAnimatorJob, QQuickAnimatorPrivate, QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEasingCurve = WAIT['QEasingCurve']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAnimator(QQuickAbstractAnimation):
  """
  The cute side of Qt's QQuickAnimator: a plain Python object standing in
  front of one C++ QQuickAnimator.

  It is built on the cute 'QQuickAbstractAnimation', as Qt's QQuickAnimator
  is built on Qt's QQuickAbstractAnimation, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's QQuickAnimator that has a ritual and that Python can
  call so far, 21 names in all: 'metaObject', 'tr', 'd_func', 'targetItem',
  'setTargetItem', 'duration', 'setDuration', 'easing', 'setEasing', 'to',
  'setTo', 'from_', 'setFrom', 'threadingModel', 'createJob', 'propertyName',
  'targetItemChanged', 'durationChanged', 'easingChanged', 'toChanged',
  'fromChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickAnimator::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickAnimator::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickAnimatorPrivate *QQuickAnimator::d_func() const': takes
    in Python what 'QQuickAnimatorPrivate *QQuickAnimator::d_func()' takes.
  - Qt's 'void QQuickAnimator::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QAbstractAnimationJob
    *QQuickAnimator::transition(QQuickStateActions &actions, QQmlProperties
    &modified, TransitionDirection a2, QObject *a3)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QQuickAnimator::QQuickAnimator(QQuickAnimatorPrivate &dd, QObject
    *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 30 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickAnimator is created at the first use, not by
    'QQuickAnimator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAnimator.
  - Qt tells when it has removed the C++ QQuickAnimator. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickAnimator::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimator.html#tr

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
    #  QString QQuickAnimator::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickAnimator2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAnimator'

  #  A C++ QQuickAnimator Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAnimator'

  #  The functions Qt calls itself that QQuickAnimator is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createJob': (
          ('_ZNK14QQuickAnimator9createJobEv',
           ('address', 'address', 'QtQuick:QQuickAnimatorJob'),
           ()),
      ),
      'propertyName': (
          ('_ZNK14QQuickAnimator12propertyNameEv',
           ('address', 'text', ''),
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
    Calls Qt's 'const QMetaObject *QQuickAnimator::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimator.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickAnimator::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickAnimator10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def targetItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickAnimator::targetItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimator.html#targetItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickAnimator::targetItem() const
    address = self.uglySide.call('ritual_ZNK14QQuickAnimator10targetItemEv')
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def duration(self) -> int:
    """
    Calls Qt's 'int QQuickAnimator::duration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimator.html#duration
    """
    #  int QQuickAnimator::duration() const
    return self.uglySide.call('ritual_ZNK14QQuickAnimator8durationEv')

  def easing(self) -> QEasingCurve:
    """
    Calls Qt's 'QEasingCurve QQuickAnimator::easing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimator.html#easing

    Returns
    -------

    QEasingCurve
      A new cute QEasingCurve around the copy Qt gave back. Python owns it.
    """
    #  QEasingCurve QQuickAnimator::easing() const
    address = self.uglySide.call('ritual_ZNK14QQuickAnimator6easingEv')
    from ..QtCore import QEasingCurve
    return QEasingCurve._cuteOwning(address)

  def to(self) -> float:
    """
    Calls Qt's 'qreal QQuickAnimator::to() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimator.html#to
    """
    #  qreal QQuickAnimator::to() const
    return self.uglySide.call('ritual_ZNK14QQuickAnimator2toEv')

  def from_(self) -> float:
    """
    Calls Qt's 'qreal QQuickAnimator::from() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimator.html#from
    """
    #  qreal QQuickAnimator::from() const
    return self.uglySide.call('ritual_ZNK14QQuickAnimator4fromEv')

  def threadingModel(self) -> QQuickAbstractAnimation.ThreadingModel:
    """
    Calls Qt's 'ThreadingModel QQuickAnimator::threadingModel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimator.html#threadingModel

    Returns
    -------

    QQuickAbstractAnimation.ThreadingModel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickAbstractAnimation.ThreadingModel(number)' gives.
    """
    #  ThreadingModel QQuickAnimator::threadingModel() const
    ritual = 'ritual_ZNK14QQuickAnimator14threadingModelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickAnimator14threadingModelEv'
    return QQuickAbstractAnimation.ThreadingModel(self.uglySide.call(ritual))

  def createJob(self) -> Optional[QQuickAnimatorJob]:
    """
    Calls Qt's 'QQuickAnimatorJob *QQuickAnimator::createJob() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimator.html#createJob

    Returns
    -------

    Optional[QQuickAnimatorJob]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAnimatorJob *QQuickAnimator::createJob() const
    address = self.uglySide.call('ritual_ZNK14QQuickAnimator9createJobEv')
    from . import QQuickAnimatorJob
    return QQuickAnimatorJob._cuteAt(address)

  def propertyName(self) -> str:
    """
    Calls Qt's 'QString QQuickAnimator::propertyName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimator.html#propertyName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickAnimator::propertyName() const
    return self.uglySide.call('ritual_ZNK14QQuickAnimator12propertyNameEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem)
  @overload(NoneType)
  def setTargetItem(self, target: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickAnimator::setTargetItem(QQuickItem *target)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimator.html#setTargetItem

    Parameters
    ----------

    target : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAnimator::setTargetItem(QQuickItem *target)
    self.uglySide.call(
        'ritual_ZN14QQuickAnimator13setTargetItemEP10QQuickItem',
        self._addressOf(target),
    )

  @overload(int)
  def setDuration(self, duration: int) -> None:
    """
    Calls Qt's 'void QQuickAnimator::setDuration(int duration)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimator.html#setDuration

    Parameters
    ----------

    duration : int
      Passed on as it is.
    """
    #  void QQuickAnimator::setDuration(int duration)
    self.uglySide.call('ritual_ZN14QQuickAnimator11setDurationEi', duration)

  @overload(QEasingCurve)
  def setEasing(self, easing: QEasingCurve) -> None:
    """
    Calls Qt's 'void QQuickAnimator::setEasing(const QEasingCurve &easing)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimator.html#setEasing

    Parameters
    ----------

    easing : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void QQuickAnimator::setEasing(const QEasingCurve &easing)
    self.uglySide.call(
        'ritual_ZN14QQuickAnimator9setEasingERK12QEasingCurve',
        self._valueOf(easing),
    )

  @overload(float)
  def setTo(self, to: float) -> None:
    """
    Calls Qt's 'void QQuickAnimator::setTo(qreal to)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimator.html#setTo

    Parameters
    ----------

    to : float
      Passed on as it is.
    """
    #  void QQuickAnimator::setTo(qreal to)
    self.uglySide.call('ritual_ZN14QQuickAnimator5setToEd', to)

  @overload(float)
  def setFrom(self, from_: float) -> None:
    """
    Calls Qt's 'void QQuickAnimator::setFrom(qreal from)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimator.html#setFrom

    Parameters
    ----------

    from_ : float
      Passed on as it is.
    """
    #  void QQuickAnimator::setFrom(qreal from)
    self.uglySide.call('ritual_ZN14QQuickAnimator7setFromEd', from_)

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
    Notes what was given, for Qt's 'QQuickAnimator::QQuickAnimator(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimator.html#QQuickAnimator

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickAnimator::QQuickAnimator(QObject *parent)
    self._noteCreation(QQuickAnimator, lambda: Rituals.call(
        'ritual_ZN14QQuickAnimatorC1EP7QObject',
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

  def d_func(self) -> Optional[QQuickAnimatorPrivate]:
    """
    Calls Qt's 'QQuickAnimatorPrivate *QQuickAnimator::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimator.html#d_func

    Returns
    -------

    Optional[QQuickAnimatorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAnimatorPrivate *QQuickAnimator::d_func()
    address = self.uglySide.call('ritual_ZN14QQuickAnimator6d_funcEv')
    from . import QQuickAnimatorPrivate
    return QQuickAnimatorPrivate._cuteAt(address)

  @overload(QQuickItem)
  @overload(NoneType)
  def targetItemChanged(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickAnimator::targetItemChanged(QQuickItem *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimator.html#targetItemChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAnimator::targetItemChanged(QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN14QQuickAnimator17targetItemChangedEP10QQuickItem',
        self._addressOf(a0),
    )

  @overload(int)
  def durationChanged(self, duration: int) -> None:
    """
    Calls Qt's 'void QQuickAnimator::durationChanged(int duration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimator.html#durationChanged

    Parameters
    ----------

    duration : int
      Passed on as it is.
    """
    #  void QQuickAnimator::durationChanged(int duration)
    self.uglySide.call(
        'ritual_ZN14QQuickAnimator15durationChangedEi', duration,
    )

  @overload(QEasingCurve)
  def easingChanged(self, curve: QEasingCurve) -> None:
    """
    Calls Qt's 'void QQuickAnimator::easingChanged(const QEasingCurve
    &curve)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimator.html#easingChanged

    Parameters
    ----------

    curve : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void QQuickAnimator::easingChanged(const QEasingCurve &curve)
    self.uglySide.call(
        'ritual_ZN14QQuickAnimator13easingChangedERK12QEasingCurve',
        self._valueOf(curve),
    )

  @overload(float)
  def toChanged(self, to: float) -> None:
    """
    Calls Qt's 'void QQuickAnimator::toChanged(qreal to)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimator.html#toChanged

    Parameters
    ----------

    to : float
      Passed on as it is.
    """
    #  void QQuickAnimator::toChanged(qreal to)
    self.uglySide.call('ritual_ZN14QQuickAnimator9toChangedEd', to)

  @overload(float)
  def fromChanged(self, from_: float) -> None:
    """
    Calls Qt's 'void QQuickAnimator::fromChanged(qreal from)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimator.html#fromChanged

    Parameters
    ----------

    from_ : float
      Passed on as it is.
    """
    #  void QQuickAnimator::fromChanged(qreal from)
    self.uglySide.call('ritual_ZN14QQuickAnimator11fromChangedEd', from_)
