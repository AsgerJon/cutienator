"""
QQuickAbstractAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickAbstractAnimation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus, QQmlPropertyValueSource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtQml import QAbstractAnimationJob, QQmlProperty
  from . import QQuickAbstractAnimationPrivate, QQuickAnimationGroup
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractAnimationJob = WAIT['QAbstractAnimationJob']
  QQmlProperty = WAIT['QQmlProperty']
  QQuickAnimationGroup = WAIT['QQuickAnimationGroup']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAbstractAnimation(QObject, QQmlPropertyValueSource, QQmlParserStatus):
  """
  The cute side of Qt's QQuickAbstractAnimation: a plain Python object
  standing in front of one C++ QQuickAbstractAnimation.

  It is built on the cute 'QObject', as Qt's QQuickAbstractAnimation is built
  on Qt's QObject, and has everything that class has. It is built on the cute
  'QQmlPropertyValueSource' as well, as Qt's QQuickAbstractAnimation is built
  on Qt's QQmlPropertyValueSource too, and has everything that class has. It
  is built on the cute 'QQmlParserStatus' as well, as Qt's
  QQuickAbstractAnimation is built on Qt's QQmlParserStatus too, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAbstractAnimation that has a ritual and that
  Python can call so far, 40 names in all: 'metaObject', 'tr', 'd_func',
  'isRunning', 'setRunning', 'isPaused', 'setPaused', 'alwaysRunToEnd',
  'setAlwaysRunToEnd', 'loops', 'setLoops', 'duration', 'currentTime',
  'setCurrentTime', 'group', 'setGroup', 'setDefaultTarget',
  'setDisableUserControl', 'setEnableUserControl', 'userControlDisabled',
  'classBegin', 'componentComplete', 'threadingModel', 'started', 'stopped',
  'runningChanged', 'pausedChanged', 'alwaysRunToEndChanged',
  'loopCountChanged', 'finished', 'restart', 'start', 'pause', 'resume',
  'stop', 'complete', 'initInstance', 'qtAnimation', 'setTarget',
  'notifyRunningChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickAbstractAnimation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickAbstractAnimation::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickAbstractAnimationPrivate
    *QQuickAbstractAnimation::d_func() const': takes in Python what
    'QQuickAbstractAnimationPrivate *QQuickAbstractAnimation::d_func()'
    takes.
  - Qt's 'void QQuickAbstractAnimation::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'QQuickAbstractAnimation::~QQuickAbstractAnimation()': the
    destructor: Python never removes a C++ QQuickAbstractAnimation.
  - Qt's 'QQuickAbstractAnimation::QQuickAbstractAnimation(
    QQuickAbstractAnimationPrivate &dd, QObject *parent)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QAbstractAnimationJob
    *QQuickAbstractAnimation::transition(QQuickStateActions &actions,
    QQmlProperties &modified, TransitionDirection direction, QObject
    *defaultTarget)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 50 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickAbstractAnimation is created at the first use, not by
    'QQuickAbstractAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAbstractAnimation.
  - Qt tells when it has removed the C++ QQuickAbstractAnimation. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickAbstractAnimation that has no cute function yet,
    'transition', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQuickAbstractAnimation, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Loops(CuteNum):
    """
    The enum 'QQuickAbstractAnimation::Loops' of Qt, with the 1 names Qt
    gives in it.
    """

    Infinite = Kee[int](-2)

  class ThreadingModel(CuteNum):
    """
    The enum 'QQuickAbstractAnimation::ThreadingModel' of Qt, with the 3
    names Qt gives in it.
    """

    GuiThread = Kee[int](0)
    RenderThread = Kee[int](1)
    AnyThread = Kee[int](2)

  class TransitionDirection(CuteNum):
    """
    The enum 'QQuickAbstractAnimation::TransitionDirection' of Qt, with the 2
    names Qt gives in it.
    """

    Forward = Kee[int](0)
    Backward = Kee[int](1)

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
    Calls Qt's 'QString QQuickAbstractAnimation::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractanimation.html#tr

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
    #  QString QQuickAbstractAnimation::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuickAbstractAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAbstractAnimation'

  #  Qt's QQuickAbstractAnimation is built on more than one class. The part
  #  of a C++ QQuickAbstractAnimation that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlPropertyValueSource':
          'ritual_cast_QQuickAbstractAnimation_QQmlPropertyValueSource',
      'QQmlParserStatus':
          'ritual_cast_QQuickAbstractAnimation_QQmlParserStatus',
  }

  #  A C++ QQuickAbstractAnimation Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAbstractAnimation'

  #  The functions Qt calls itself that QQuickAbstractAnimation is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'transition': (
          'QAbstractAnimationJob '
          '*QQuickAbstractAnimation::transition(QQuickStateActions &, '
          'QQmlProperties &, TransitionDirection, QObject *)',
      ),
  }

  #  The functions Qt calls itself that QQuickAbstractAnimation is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'threadingModel': (
          ('_ZNK23QQuickAbstractAnimation14threadingModelEv',
           ('int', 'enum', 'QtQuick:QQuickAbstractAnimation.ThreadingModel'),
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
    Calls Qt's 'const QMetaObject *QQuickAbstractAnimation::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickAbstractAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickAbstractAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractAnimation::isRunning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#isRunning
    """
    #  bool QQuickAbstractAnimation::isRunning() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickAbstractAnimation9isRunningEv',
    )

  def isPaused(self) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractAnimation::isPaused() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#isPaused
    """
    #  bool QQuickAbstractAnimation::isPaused() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickAbstractAnimation8isPausedEv',
    )

  def alwaysRunToEnd(self) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractAnimation::alwaysRunToEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#alwaysRunToEnd
    """
    #  bool QQuickAbstractAnimation::alwaysRunToEnd() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickAbstractAnimation14alwaysRunToEndEv',
    )

  def loops(self) -> int:
    """
    Calls Qt's 'int QQuickAbstractAnimation::loops() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractanimation.html#loops
    """
    #  int QQuickAbstractAnimation::loops() const
    return self.uglySide.call('ritual_ZNK23QQuickAbstractAnimation5loopsEv')

  def duration(self) -> int:
    """
    Calls Qt's 'int QQuickAbstractAnimation::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#duration
    """
    #  int QQuickAbstractAnimation::duration() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickAbstractAnimation8durationEv',
    )

  def group(self) -> Optional[QQuickAnimationGroup]:
    """
    Calls Qt's 'QQuickAnimationGroup *QQuickAbstractAnimation::group()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractanimation.html#group

    Returns
    -------

    Optional[QQuickAnimationGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAnimationGroup *QQuickAbstractAnimation::group() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickAbstractAnimation5groupEv',
    )
    from . import QQuickAnimationGroup
    return QQuickAnimationGroup._cuteAt(address)

  def userControlDisabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractAnimation::userControlDisabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#userControlDisabled
    """
    #  bool QQuickAbstractAnimation::userControlDisabled() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickAbstractAnimation19userControlDisabledEv',
    )

  def threadingModel(self) -> ThreadingModel:
    """
    Calls Qt's 'ThreadingModel QQuickAbstractAnimation::threadingModel()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#threadingModel

    Returns
    -------

    ThreadingModel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ThreadingModel(number)'
      gives.
    """
    #  ThreadingModel QQuickAbstractAnimation::threadingModel() const
    ritual = 'ritual_ZNK23QQuickAbstractAnimation14threadingModelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QQuickAbstractAnimation14threadingModelEv'
    return QQuickAbstractAnimation.ThreadingModel(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setRunning(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::setRunning(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#setRunning

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickAbstractAnimation::setRunning(bool a0)
    self.uglySide.call(
        'ritual_ZN23QQuickAbstractAnimation10setRunningEb', a0,
    )

  @overload(bool)
  def setPaused(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::setPaused(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#setPaused

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickAbstractAnimation::setPaused(bool a0)
    self.uglySide.call('ritual_ZN23QQuickAbstractAnimation9setPausedEb', a0)

  @overload(bool)
  def setAlwaysRunToEnd(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::setAlwaysRunToEnd(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#setAlwaysRunToEnd

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickAbstractAnimation::setAlwaysRunToEnd(bool a0)
    self.uglySide.call(
        'ritual_ZN23QQuickAbstractAnimation17setAlwaysRunToEndEb', a0,
    )

  @overload(int)
  def setLoops(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::setLoops(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#setLoops

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickAbstractAnimation::setLoops(int a0)
    self.uglySide.call('ritual_ZN23QQuickAbstractAnimation8setLoopsEi', a0)

  @overload(int)
  def setCurrentTime(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::setCurrentTime(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#setCurrentTime

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickAbstractAnimation::setCurrentTime(int a0)
    self.uglySide.call(
        'ritual_ZN23QQuickAbstractAnimation14setCurrentTimeEi', a0,
    )

  @overload(QQuickAnimationGroup)
  @overload(NoneType)
  @overload(QQuickAnimationGroup, int)
  @overload(NoneType, int)
  def setGroup(
      self,
      a0: Optional[QQuickAnimationGroup],
      index: int = -1,
  ) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::setGroup(QQuickAnimationGroup
    *a0, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#setGroup

    Parameters
    ----------

    a0 : Optional[QQuickAnimationGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QQuickAbstractAnimation::setGroup(QQuickAnimationGroup *a0, int
    #      index)
    self.uglySide.call(
        'ritual_ZN23QQuickAbstractAnimation8setGroupEP20QQuickAnimationGrou'
        'pi',
        self._addressOf(a0), index,
    )

  @overload(QQmlProperty)
  def setDefaultTarget(self, a0: QQmlProperty) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::setDefaultTarget(const
    QQmlProperty &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#setDefaultTarget

    Parameters
    ----------

    a0 : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.
    """
    #  void QQuickAbstractAnimation::setDefaultTarget(const QQmlProperty &a0)
    self.uglySide.call(
        'ritual_ZN23QQuickAbstractAnimation16setDefaultTargetERK12QQmlPrope'
        'rty',
        self._valueOf(a0),
    )

  def setDisableUserControl(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::setDisableUserControl()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#setDisableUserControl
    """
    #  void QQuickAbstractAnimation::setDisableUserControl()
    self.uglySide.call(
        'ritual_ZN23QQuickAbstractAnimation21setDisableUserControlEv',
    )

  def setEnableUserControl(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::setEnableUserControl()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#setEnableUserControl
    """
    #  void QQuickAbstractAnimation::setEnableUserControl()
    self.uglySide.call(
        'ritual_ZN23QQuickAbstractAnimation20setEnableUserControlEv',
    )

  @overload(QQmlProperty)
  def setTarget(self, a0: QQmlProperty) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::setTarget(const QQmlProperty
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#setTarget

    Parameters
    ----------

    a0 : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.
    """
    #  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
    ritual = 'ritual_ZN23QQuickAbstractAnimation9setTargetERK12QQmlProperty'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuickAbstractAnimation9setTargetERK12QQmlPropert'
          'y')
    self.uglySide.call(ritual, self._valueOf(a0))

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
    'QQuickAbstractAnimation::QQuickAbstractAnimation(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickAbstractAnimation::QQuickAbstractAnimation(QObject *parent)
    self._noteCreation(QQuickAbstractAnimation, lambda: Rituals.call(
        'ritual_ZN23QQuickAbstractAnimationC1EP7QObject',
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

  def d_func(self) -> Optional[QQuickAbstractAnimationPrivate]:
    """
    Calls Qt's 'QQuickAbstractAnimationPrivate
    *QQuickAbstractAnimation::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#d_func

    Returns
    -------

    Optional[QQuickAbstractAnimationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAbstractAnimationPrivate *QQuickAbstractAnimation::d_func()
    address = self.uglySide.call(
        'ritual_ZN23QQuickAbstractAnimation6d_funcEv',
    )
    from . import QQuickAbstractAnimationPrivate
    return QQuickAbstractAnimationPrivate._cuteAt(address)

  def currentTime(self) -> int:
    """
    Calls Qt's 'int QQuickAbstractAnimation::currentTime()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#currentTime
    """
    #  int QQuickAbstractAnimation::currentTime()
    return self.uglySide.call(
        'ritual_ZN23QQuickAbstractAnimation11currentTimeEv',
    )

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#classBegin
    """
    #  void QQuickAbstractAnimation::classBegin()
    ritual = 'ritual_ZN23QQuickAbstractAnimation10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuickAbstractAnimation10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#componentComplete
    """
    #  void QQuickAbstractAnimation::componentComplete()
    ritual = 'ritual_ZN23QQuickAbstractAnimation17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuickAbstractAnimation17componentCompleteEv'
    self.uglySide.call(ritual)

  def started(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::started()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#started
    """
    #  void QQuickAbstractAnimation::started()
    self.uglySide.call('ritual_ZN23QQuickAbstractAnimation7startedEv')

  def stopped(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::stopped()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#stopped
    """
    #  void QQuickAbstractAnimation::stopped()
    self.uglySide.call('ritual_ZN23QQuickAbstractAnimation7stoppedEv')

  @overload(bool)
  def runningChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::runningChanged(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#runningChanged

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickAbstractAnimation::runningChanged(bool a0)
    self.uglySide.call(
        'ritual_ZN23QQuickAbstractAnimation14runningChangedEb', a0,
    )

  @overload(bool)
  def pausedChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::pausedChanged(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#pausedChanged

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickAbstractAnimation::pausedChanged(bool a0)
    self.uglySide.call(
        'ritual_ZN23QQuickAbstractAnimation13pausedChangedEb', a0,
    )

  @overload(bool)
  def alwaysRunToEndChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::alwaysRunToEndChanged(bool
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#alwaysRunToEndChanged

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickAbstractAnimation::alwaysRunToEndChanged(bool a0)
    self.uglySide.call(
        'ritual_ZN23QQuickAbstractAnimation21alwaysRunToEndChangedEb', a0,
    )

  @overload(int)
  def loopCountChanged(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::loopCountChanged(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#loopCountChanged

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickAbstractAnimation::loopCountChanged(int a0)
    self.uglySide.call(
        'ritual_ZN23QQuickAbstractAnimation16loopCountChangedEi', a0,
    )

  def finished(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::finished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#finished
    """
    #  void QQuickAbstractAnimation::finished()
    self.uglySide.call('ritual_ZN23QQuickAbstractAnimation8finishedEv')

  def restart(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::restart()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#restart
    """
    #  void QQuickAbstractAnimation::restart()
    self.uglySide.call('ritual_ZN23QQuickAbstractAnimation7restartEv')

  def start(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractanimation.html#start
    """
    #  void QQuickAbstractAnimation::start()
    self.uglySide.call('ritual_ZN23QQuickAbstractAnimation5startEv')

  def pause(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::pause()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractanimation.html#pause
    """
    #  void QQuickAbstractAnimation::pause()
    self.uglySide.call('ritual_ZN23QQuickAbstractAnimation5pauseEv')

  def resume(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::resume()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#resume
    """
    #  void QQuickAbstractAnimation::resume()
    self.uglySide.call('ritual_ZN23QQuickAbstractAnimation6resumeEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractanimation.html#stop
    """
    #  void QQuickAbstractAnimation::stop()
    self.uglySide.call('ritual_ZN23QQuickAbstractAnimation4stopEv')

  def complete(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::complete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#complete
    """
    #  void QQuickAbstractAnimation::complete()
    self.uglySide.call('ritual_ZN23QQuickAbstractAnimation8completeEv')

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def initInstance(
      self,
      animation: Optional[QAbstractAnimationJob],
  ) -> Optional[QAbstractAnimationJob]:
    """
    Calls Qt's 'QAbstractAnimationJob
    *QQuickAbstractAnimation::initInstance(QAbstractAnimationJob
    *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#initInstance

    Parameters
    ----------

    animation : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAbstractAnimationJob]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAnimationJob
    #      *QQuickAbstractAnimation::initInstance(QAbstractAnimationJob
    #      *animation)
    address = self.uglySide.call(
        'ritual_ZN23QQuickAbstractAnimation12initInstanceEP21QAbstractAnima'
        'tionJob',
        self._addressOf(animation, 'QAbstractAnimationJob'),
    )
    from ..QtQml import QAbstractAnimationJob
    return QAbstractAnimationJob._cuteAt(address)

  def qtAnimation(self) -> Optional[QAbstractAnimationJob]:
    """
    Calls Qt's 'QAbstractAnimationJob
    *QQuickAbstractAnimation::qtAnimation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#qtAnimation

    Returns
    -------

    Optional[QAbstractAnimationJob]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAnimationJob *QQuickAbstractAnimation::qtAnimation()
    address = self.uglySide.call(
        'ritual_ZN23QQuickAbstractAnimation11qtAnimationEv',
    )
    from ..QtQml import QAbstractAnimationJob
    return QAbstractAnimationJob._cuteAt(address)

  @overload(bool)
  def notifyRunningChanged(self, running: bool) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimation::notifyRunningChanged(bool
    running)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimation.html#notifyRunningChanged

    Parameters
    ----------

    running : bool
      Passed on as it is.
    """
    #  void QQuickAbstractAnimation::notifyRunningChanged(bool running)
    self.uglySide.call(
        'ritual_ZN23QQuickAbstractAnimation20notifyRunningChangedEb',
        running,
    )

  @staticmethod
  def transition(*__, **_) -> Never:
    """
    Qt's 'QAbstractAnimationJob
    *QQuickAbstractAnimation::transition(QQuickStateActions &actions,
    QQmlProperties &modified, TransitionDirection direction, QObject
    *defaultTarget)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickAbstractAnimation.transition' has no cute function yet. "
        "Qt's 'QAbstractAnimationJob "
        "*QQuickAbstractAnimation::transition(QQuickStateActions &actions, "
        "QQmlProperties &modified, TransitionDirection direction, QObject "
        "*defaultTarget)': takes a type Python has no way to hand over yet.")
