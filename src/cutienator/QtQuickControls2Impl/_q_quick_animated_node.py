"""
QQuickAnimatedNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickanimatednode_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickAnimatedNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQuick import QSGTransformNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQuick import QQuickItem, QQuickWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAnimatedNode(QObject, QSGTransformNode):
  """
  The cute side of Qt's QQuickAnimatedNode: a plain Python object standing in
  front of one C++ QQuickAnimatedNode.

  It is built on the cute 'QObject', as Qt's QQuickAnimatedNode is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QSGTransformNode' as well, as Qt's QQuickAnimatedNode is built on Qt's
  QSGTransformNode too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAnimatedNode that has a ritual and that Python
  can call so far, 19 names in all: 'metaObject', 'tr', 'isRunning',
  'currentTime', 'setCurrentTime', 'duration', 'setDuration', 'loopCount',
  'setLoopCount', 'sync', 'window', 'start', 'restart', 'stop', 'started',
  'stopped', 'updateCurrentTime', 'advance', 'update'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickAnimatedNode::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickAnimatedNode::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 24 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickAnimatedNode is created at the first use, not by
    'QQuickAnimatedNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAnimatedNode.
  - Qt tells when it has removed the C++ QQuickAnimatedNode. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickAnimatedNode, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class LoopCount(CuteNum):
    """
    The enum 'QQuickAnimatedNode::LoopCount' of Qt, with the 1 names Qt gives
    in it.
    """

    Infinite = Kee[int](-1)

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
    Calls Qt's 'QString QQuickAnimatedNode::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatednode.html#tr

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
    #  QString QQuickAnimatedNode::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickAnimatedNode2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAnimatedNode'

  #  Qt's QQuickAnimatedNode is built on more than one class. The part of a
  #  C++ QQuickAnimatedNode that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QSGTransformNode': 'ritual_cast_QQuickAnimatedNode_QSGTransformNode',
  }

  #  The functions Qt calls itself that QQuickAnimatedNode is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'sync': (
          ('_ZN18QQuickAnimatedNode4syncEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'updateCurrentTime': (
          ('_ZN18QQuickAnimatedNode17updateCurrentTimeEi',
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
    Calls Qt's 'const QMetaObject *QQuickAnimatedNode::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatednode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickAnimatedNode::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickAnimatedNode10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QQuickAnimatedNode::isRunning() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatednode.html#isRunning
    """
    #  bool QQuickAnimatedNode::isRunning() const
    return self.uglySide.call('ritual_ZNK18QQuickAnimatedNode9isRunningEv')

  def currentTime(self) -> int:
    """
    Calls Qt's 'int QQuickAnimatedNode::currentTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatednode.html#currentTime
    """
    #  int QQuickAnimatedNode::currentTime() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickAnimatedNode11currentTimeEv',
    )

  def duration(self) -> int:
    """
    Calls Qt's 'int QQuickAnimatedNode::duration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatednode.html#duration
    """
    #  int QQuickAnimatedNode::duration() const
    return self.uglySide.call('ritual_ZNK18QQuickAnimatedNode8durationEv')

  def loopCount(self) -> int:
    """
    Calls Qt's 'int QQuickAnimatedNode::loopCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatednode.html#loopCount
    """
    #  int QQuickAnimatedNode::loopCount() const
    return self.uglySide.call('ritual_ZNK18QQuickAnimatedNode9loopCountEv')

  def window(self) -> Optional[QQuickWindow]:
    """
    Calls Qt's 'QQuickWindow *QQuickAnimatedNode::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatednode.html#window

    Returns
    -------

    Optional[QQuickWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWindow *QQuickAnimatedNode::window() const
    address = self.uglySide.call('ritual_ZNK18QQuickAnimatedNode6windowEv')
    from ..QtQuick import QQuickWindow
    return QQuickWindow._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setCurrentTime(self, time: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatedNode::setCurrentTime(int time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatednode.html#setCurrentTime

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  void QQuickAnimatedNode::setCurrentTime(int time)
    self.uglySide.call(
        'ritual_ZN18QQuickAnimatedNode14setCurrentTimeEi', time,
    )

  @overload(int)
  def setDuration(self, duration: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatedNode::setDuration(int duration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatednode.html#setDuration

    Parameters
    ----------

    duration : int
      Passed on as it is.
    """
    #  void QQuickAnimatedNode::setDuration(int duration)
    self.uglySide.call(
        'ritual_ZN18QQuickAnimatedNode11setDurationEi', duration,
    )

  @overload(int)
  def setLoopCount(self, count: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatedNode::setLoopCount(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatednode.html#setLoopCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QQuickAnimatedNode::setLoopCount(int count)
    self.uglySide.call(
        'ritual_ZN18QQuickAnimatedNode12setLoopCountEi', count,
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

  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, target: Optional[QQuickItem]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickAnimatedNode::QQuickAnimatedNode(QQuickItem *target)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatednode.html#QQuickAnimatedNode

    Parameters
    ----------

    target : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickAnimatedNode::QQuickAnimatedNode(QQuickItem *target)
    self._noteCreation(QQuickAnimatedNode, lambda: Rituals.call(
        'ritual_ZN18QQuickAnimatedNodeC1EP10QQuickItem',
        self._addressOf(target),
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

  @overload(QQuickItem)
  @overload(NoneType)
  def sync(self, target: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickAnimatedNode::sync(QQuickItem *target)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatednode.html#sync

    Parameters
    ----------

    target : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAnimatedNode::sync(QQuickItem *target)
    ritual = 'ritual_ZN18QQuickAnimatedNode4syncEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickAnimatedNode4syncEP10QQuickItem'
    self.uglySide.call(ritual, self._addressOf(target))

  @overload()
  @overload(int)
  def start(self, duration: int = 0) -> None:
    """
    Calls Qt's 'void QQuickAnimatedNode::start(int duration)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatednode.html#start

    Parameters
    ----------

    duration : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QQuickAnimatedNode::start(int duration)
    self.uglySide.call('ritual_ZN18QQuickAnimatedNode5startEi', duration)

  def restart(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedNode::restart()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatednode.html#restart
    """
    #  void QQuickAnimatedNode::restart()
    self.uglySide.call('ritual_ZN18QQuickAnimatedNode7restartEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedNode::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatednode.html#stop
    """
    #  void QQuickAnimatedNode::stop()
    self.uglySide.call('ritual_ZN18QQuickAnimatedNode4stopEv')

  def started(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedNode::started()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatednode.html#started
    """
    #  void QQuickAnimatedNode::started()
    self.uglySide.call('ritual_ZN18QQuickAnimatedNode7startedEv')

  def stopped(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedNode::stopped()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatednode.html#stopped
    """
    #  void QQuickAnimatedNode::stopped()
    self.uglySide.call('ritual_ZN18QQuickAnimatedNode7stoppedEv')

  @overload(int)
  def updateCurrentTime(self, time: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatedNode::updateCurrentTime(int time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatednode.html#updateCurrentTime

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  void QQuickAnimatedNode::updateCurrentTime(int time)
    ritual = 'ritual_ZN18QQuickAnimatedNode17updateCurrentTimeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickAnimatedNode17updateCurrentTimeEi'
    self.uglySide.call(ritual, time)

  def advance(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedNode::advance()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatednode.html#advance
    """
    #  void QQuickAnimatedNode::advance()
    self.uglySide.call('ritual_ZN18QQuickAnimatedNode7advanceEv')

  def update(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedNode::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatednode.html#update
    """
    #  void QQuickAnimatedNode::update()
    self.uglySide.call('ritual_ZN18QQuickAnimatedNode6updateEv')
