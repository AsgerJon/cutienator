"""
QQuickPropertyAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickPropertyAnimation to be private: it declares the class in a
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

  from ..QtCore import QEasingCurve, QMetaObject, QVariant
  from . import QQuickPropertyAnimationPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEasingCurve = WAIT['QEasingCurve']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPropertyAnimation(QQuickAbstractAnimation):
  """
  The cute side of Qt's QQuickPropertyAnimation: a plain Python object
  standing in front of one C++ QQuickPropertyAnimation.

  It is built on the cute 'QQuickAbstractAnimation', as Qt's
  QQuickPropertyAnimation is built on Qt's QQuickAbstractAnimation, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPropertyAnimation that has a ritual and that
  Python can call so far, 24 names in all: 'metaObject', 'tr', 'd_func',
  'duration', 'setDuration', 'from_', 'setFrom', 'to', 'setTo', 'easing',
  'setEasing', 'target', 'setTargetObject', 'property', 'setProperty',
  'properties', 'setProperties', 'durationChanged', 'fromChanged',
  'toChanged', 'easingChanged', 'propertiesChanged', 'targetChanged',
  'propertyChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPropertyAnimation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickPropertyAnimation::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickPropertyAnimationPrivate
    *QQuickPropertyAnimation::d_func() const': takes in Python what
    'QQuickPropertyAnimationPrivate *QQuickPropertyAnimation::d_func()'
    takes.
  - Qt's 'QQuickPropertyAnimation::~QQuickPropertyAnimation()': the
    destructor: Python never removes a C++ QQuickPropertyAnimation.
  - Qt's 'QQmlListProperty<QObject> QQuickPropertyAnimation::targets()':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlListProperty<QObject> QQuickPropertyAnimation::exclude()':
    gives a type Python has no way to take yet.
  - Qt's 'QQuickStateActions
    QQuickPropertyAnimation::createTransitionActions(QQuickStateActions
    &actions, QQmlProperties &modified, QObject *defaultTarget)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QQuickPropertyAnimation::QQuickPropertyAnimation(
    QQuickPropertyAnimationPrivate &dd, QObject *parent)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QAbstractAnimationJob
    *QQuickPropertyAnimation::transition(QQuickStateActions &actions,
    QQmlProperties &modified, TransitionDirection direction, QObject
    *defaultTarget)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 36 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPropertyAnimation is created at the first use, not by
    'QQuickPropertyAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPropertyAnimation.
  - Qt tells when it has removed the C++ QQuickPropertyAnimation. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickPropertyAnimation that has no cute function yet,
    'createTransitionActions', 'exclude', 'targets', holds a function that
    raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQuickPropertyAnimation::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpropertyanimation.html#tr

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
    #  QString QQuickPropertyAnimation::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuickPropertyAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPropertyAnimation'

  #  A C++ QQuickPropertyAnimation Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPropertyAnimation'

  #  The functions Qt calls itself that QQuickPropertyAnimation is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setDuration': (
          ('_ZN23QQuickPropertyAnimation11setDurationEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
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
    Calls Qt's 'const QMetaObject *QQuickPropertyAnimation::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPropertyAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickPropertyAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def duration(self) -> int:
    """
    Calls Qt's 'int QQuickPropertyAnimation::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimation.html#duration
    """
    #  int QQuickPropertyAnimation::duration() const
    ritual = 'ritual_ZNK23QQuickPropertyAnimation8durationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QQuickPropertyAnimation8durationEv'
    return self.uglySide.call(ritual)

  def from_(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickPropertyAnimation::from() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpropertyanimation.html#from

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickPropertyAnimation::from() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickPropertyAnimation4fromEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def to(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickPropertyAnimation::to() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpropertyanimation.html#to

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickPropertyAnimation::to() const
    address = self.uglySide.call('ritual_ZNK23QQuickPropertyAnimation2toEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def easing(self) -> QEasingCurve:
    """
    Calls Qt's 'QEasingCurve QQuickPropertyAnimation::easing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimation.html#easing

    Returns
    -------

    QEasingCurve
      A new cute QEasingCurve around the copy Qt gave back. Python owns it.
    """
    #  QEasingCurve QQuickPropertyAnimation::easing() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickPropertyAnimation6easingEv',
    )
    from ..QtCore import QEasingCurve
    return QEasingCurve._cuteOwning(address)

  def target(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQuickPropertyAnimation::target() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimation.html#target

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickPropertyAnimation::target() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickPropertyAnimation6targetEv',
    )
    return QObject._cuteAt(address)

  def property(self) -> str:
    """
    Calls Qt's 'QString QQuickPropertyAnimation::property() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimation.html#property

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickPropertyAnimation::property() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickPropertyAnimation8propertyEv',
    )

  def properties(self) -> str:
    """
    Calls Qt's 'QString QQuickPropertyAnimation::properties() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimation.html#properties

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickPropertyAnimation::properties() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickPropertyAnimation10propertiesEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setDuration(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickPropertyAnimation::setDuration(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimation.html#setDuration

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickPropertyAnimation::setDuration(int a0)
    ritual = 'ritual_ZN23QQuickPropertyAnimation11setDurationEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuickPropertyAnimation11setDurationEi'
    self.uglySide.call(ritual, a0)

  @overload(QVariant)
  def setFrom(self, a0: QVariant) -> None:
    """
    Calls Qt's 'void QQuickPropertyAnimation::setFrom(const QVariant &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimation.html#setFrom

    Parameters
    ----------

    a0 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickPropertyAnimation::setFrom(const QVariant &a0)
    self.uglySide.call(
        'ritual_ZN23QQuickPropertyAnimation7setFromERK8QVariant',
        self._valueOf(a0),
    )

  @overload(QVariant)
  def setTo(self, a0: QVariant) -> None:
    """
    Calls Qt's 'void QQuickPropertyAnimation::setTo(const QVariant &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpropertyanimation.html#setTo

    Parameters
    ----------

    a0 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickPropertyAnimation::setTo(const QVariant &a0)
    self.uglySide.call(
        'ritual_ZN23QQuickPropertyAnimation5setToERK8QVariant',
        self._valueOf(a0),
    )

  @overload(QEasingCurve)
  def setEasing(self, a0: QEasingCurve) -> None:
    """
    Calls Qt's 'void QQuickPropertyAnimation::setEasing(const QEasingCurve
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimation.html#setEasing

    Parameters
    ----------

    a0 : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void QQuickPropertyAnimation::setEasing(const QEasingCurve &a0)
    self.uglySide.call(
        'ritual_ZN23QQuickPropertyAnimation9setEasingERK12QEasingCurve',
        self._valueOf(a0),
    )

  @overload(QObject)
  @overload(NoneType)
  def setTargetObject(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickPropertyAnimation::setTargetObject(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimation.html#setTargetObject

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPropertyAnimation::setTargetObject(QObject *a0)
    self.uglySide.call(
        'ritual_ZN23QQuickPropertyAnimation15setTargetObjectEP7QObject',
        self._addressOf(a0, 'QObject'),
    )

  @overload(str)
  def setProperty(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickPropertyAnimation::setProperty(const QString
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimation.html#setProperty

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickPropertyAnimation::setProperty(const QString &a0)
    self.uglySide.call(
        'ritual_ZN23QQuickPropertyAnimation11setPropertyERK7QString', a0,
    )

  @overload(str)
  def setProperties(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickPropertyAnimation::setProperties(const QString
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimation.html#setProperties

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickPropertyAnimation::setProperties(const QString &a0)
    self.uglySide.call(
        'ritual_ZN23QQuickPropertyAnimation13setPropertiesERK7QString', a0,
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
    'QQuickPropertyAnimation::QQuickPropertyAnimation(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimation.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPropertyAnimation::QQuickPropertyAnimation(QObject *parent)
    self._noteCreation(QQuickPropertyAnimation, lambda: Rituals.call(
        'ritual_ZN23QQuickPropertyAnimationC1EP7QObject',
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

  def d_func(self) -> Optional[QQuickPropertyAnimationPrivate]:
    """
    Calls Qt's 'QQuickPropertyAnimationPrivate
    *QQuickPropertyAnimation::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimation.html#d_func

    Returns
    -------

    Optional[QQuickPropertyAnimationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPropertyAnimationPrivate *QQuickPropertyAnimation::d_func()
    address = self.uglySide.call(
        'ritual_ZN23QQuickPropertyAnimation6d_funcEv',
    )
    from . import QQuickPropertyAnimationPrivate
    return QQuickPropertyAnimationPrivate._cuteAt(address)

  @overload(int)
  def durationChanged(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickPropertyAnimation::durationChanged(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimation.html#durationChanged

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickPropertyAnimation::durationChanged(int a0)
    self.uglySide.call(
        'ritual_ZN23QQuickPropertyAnimation15durationChangedEi', a0,
    )

  def fromChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPropertyAnimation::fromChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimation.html#fromChanged
    """
    #  void QQuickPropertyAnimation::fromChanged()
    self.uglySide.call('ritual_ZN23QQuickPropertyAnimation11fromChangedEv')

  def toChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPropertyAnimation::toChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimation.html#toChanged
    """
    #  void QQuickPropertyAnimation::toChanged()
    self.uglySide.call('ritual_ZN23QQuickPropertyAnimation9toChangedEv')

  @overload(QEasingCurve)
  def easingChanged(self, a0: QEasingCurve) -> None:
    """
    Calls Qt's 'void QQuickPropertyAnimation::easingChanged(const
    QEasingCurve &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimation.html#easingChanged

    Parameters
    ----------

    a0 : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void QQuickPropertyAnimation::easingChanged(const QEasingCurve &a0)
    self.uglySide.call(
        'ritual_ZN23QQuickPropertyAnimation13easingChangedERK12QEasingCurve',
        self._valueOf(a0),
    )

  @overload(str)
  def propertiesChanged(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickPropertyAnimation::propertiesChanged(const QString
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimation.html#propertiesChanged

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickPropertyAnimation::propertiesChanged(const QString &a0)
    self.uglySide.call(
        'ritual_ZN23QQuickPropertyAnimation17propertiesChangedERK7QString',
        a0,
    )

  def targetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPropertyAnimation::targetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimation.html#targetChanged
    """
    #  void QQuickPropertyAnimation::targetChanged()
    self.uglySide.call('ritual_ZN23QQuickPropertyAnimation13targetChangedEv')

  def propertyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPropertyAnimation::propertyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimation.html#propertyChanged
    """
    #  void QQuickPropertyAnimation::propertyChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickPropertyAnimation15propertyChangedEv',
    )

  @staticmethod
  def createTransitionActions(*__, **_) -> Never:
    """
    Qt's 'QQuickStateActions
    QQuickPropertyAnimation::createTransitionActions(QQuickStateActions
    &actions, QQmlProperties &modified, QObject *defaultTarget)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickPropertyAnimation.createTransitionActions' has no cute "
        "function yet. Qt's 'QQuickStateActions "
        "QQuickPropertyAnimation::createTransitionActions(QQuickStateActions"
        " &actions, QQmlProperties &modified, QObject *defaultTarget)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def exclude(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuickPropertyAnimation::exclude()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickPropertyAnimation.exclude' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQuickPropertyAnimation::exclude()': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def targets(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuickPropertyAnimation::targets()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickPropertyAnimation.targets' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQuickPropertyAnimation::targets()': "
        "gives a type Python has no way to take yet.")
