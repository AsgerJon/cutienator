"""
QQuickStochasticEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickspriteengine_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickStochasticEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickStochasticState
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickStochasticState = WAIT['QQuickStochasticState']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickStochasticEngine(QObject):
  """
  The cute side of Qt's QQuickStochasticEngine: a plain Python object
  standing in front of one C++ QQuickStochasticEngine.

  It is built on the cute 'QObject', as Qt's QQuickStochasticEngine is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickStochasticEngine that has a ritual and that
  Python can call so far, 21 names in all: 'metaObject', 'tr', 'globalGoal',
  'count', 'setCount', 'setGoal', 'start', 'restart', 'advance', 'stop',
  'curState', 'state', 'stateIndex', 'stateCount', 'globalGoalChanged',
  'stateChanged', 'setGlobalGoal', 'updateSprites', 'addToUpdateList',
  'nextState', 'goalSeek'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickStochasticEngine::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickStochasticEngine::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickStochasticEngine::~QQuickStochasticEngine()': the destructor:
    Python never removes a C++ QQuickStochasticEngine.
  - Qt's 'QQmlListProperty<QQuickStochasticState>
    QQuickStochasticEngine::states()': gives a type Python has no way to take
    yet.

  What has no ritual
  ------------------

  2 of the 30 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickStochasticEngine is created at the first use, not by
    'QQuickStochasticEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickStochasticEngine.
  - Qt tells when it has removed the C++ QQuickStochasticEngine. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickStochasticEngine that has no cute function yet,
    'states', holds a function that raises 'NotImplementedError', and its
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
    Calls Qt's 'QString QQuickStochasticEngine::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstochasticengine.html#tr

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
    #  QString QQuickStochasticEngine::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QQuickStochasticEngine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStochasticEngine'

  #  A C++ QQuickStochasticEngine Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickStochasticEngine'

  #  The functions Qt calls itself that QQuickStochasticEngine is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'restart': (
          ('_ZN22QQuickStochasticEngine7restartEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'advance': (
          ('_ZN22QQuickStochasticEngine7advanceEi',
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
    Calls Qt's 'const QMetaObject *QQuickStochasticEngine::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickStochasticEngine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickStochasticEngine10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def globalGoal(self) -> str:
    """
    Calls Qt's 'QString QQuickStochasticEngine::globalGoal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticengine.html#globalGoal

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickStochasticEngine::globalGoal() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickStochasticEngine10globalGoalEv',
    )

  def count(self) -> int:
    """
    Calls Qt's 'int QQuickStochasticEngine::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstochasticengine.html#count
    """
    #  int QQuickStochasticEngine::count() const
    return self.uglySide.call('ritual_ZNK22QQuickStochasticEngine5countEv')

  @overload()
  @overload(int)
  def curState(self, index: int = 0) -> int:
    """
    Calls Qt's 'int QQuickStochasticEngine::curState(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticengine.html#curState

    Parameters
    ----------

    index : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QQuickStochasticEngine::curState(int index) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickStochasticEngine8curStateEi', index,
    )

  @overload(int)
  def state(self, idx: int) -> Optional[QQuickStochasticState]:
    """
    Calls Qt's 'QQuickStochasticState *QQuickStochasticEngine::state(int idx)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstochasticengine.html#state

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuickStochasticState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStochasticState *QQuickStochasticEngine::state(int idx) const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickStochasticEngine5stateEi', idx,
    )
    from . import QQuickStochasticState
    return QQuickStochasticState._cuteAt(address)

  @overload(QQuickStochasticState)
  @overload(NoneType)
  def stateIndex(self, s: Optional[QQuickStochasticState]) -> int:
    """
    Calls Qt's 'int QQuickStochasticEngine::stateIndex(QQuickStochasticState
    *s) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticengine.html#stateIndex

    Parameters
    ----------

    s : Optional[QQuickStochasticState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQuickStochasticEngine::stateIndex(QQuickStochasticState *s) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickStochasticEngine10stateIndexEP21QQuickStochastic'
        'State',
        self._addressOf(s),
    )

  @overload(str)
  def stateIndex(self, s: str) -> int:
    """
    Calls Qt's 'int QQuickStochasticEngine::stateIndex(const QString &s)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticengine.html#stateIndex

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QQuickStochasticEngine::stateIndex(const QString &s) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickStochasticEngine10stateIndexERK7QString', s,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setCount(self, c: int) -> None:
    """
    Calls Qt's 'void QQuickStochasticEngine::setCount(int c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticengine.html#setCount

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  void QQuickStochasticEngine::setCount(int c)
    self.uglySide.call('ritual_ZN22QQuickStochasticEngine8setCountEi', c)

  @overload(int)
  @overload(int, int)
  @overload(int, int, bool)
  def setGoal(self, state: int, sprite: int = 0, jump: bool = False) -> None:
    """
    Calls Qt's 'void QQuickStochasticEngine::setGoal(int state, int sprite,
    bool jump)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticengine.html#setGoal

    Parameters
    ----------

    state : int
      Passed on as it is.

    sprite : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    jump : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickStochasticEngine::setGoal(int state, int sprite, bool jump)
    self.uglySide.call(
        'ritual_ZN22QQuickStochasticEngine7setGoalEiib', state, sprite, jump,
    )

  @overload(str)
  def setGlobalGoal(self, arg: str) -> None:
    """
    Calls Qt's 'void QQuickStochasticEngine::setGlobalGoal(const QString
    &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticengine.html#setGlobalGoal

    Parameters
    ----------

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickStochasticEngine::setGlobalGoal(const QString &arg)
    self.uglySide.call(
        'ritual_ZN22QQuickStochasticEngine13setGlobalGoalERK7QString', arg,
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
    'QQuickStochasticEngine::QQuickStochasticEngine(QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticengine.html#QQuickStochasticEngine

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickStochasticEngine::QQuickStochasticEngine(QObject *parent)
    self._noteCreation(QQuickStochasticEngine, lambda: Rituals.call(
        'ritual_ZN22QQuickStochasticEngineC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QList[QQuickStochasticState])
  @overload(QList[QQuickStochasticState], QObject)
  @overload(QList[QQuickStochasticState], NoneType)
  def __init__(
      self,
      states: QList[QQuickStochasticState],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickStochasticEngine::QQuickStochasticEngine(const
    QList<QQuickStochasticState *> &states, QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticengine.html#QQuickStochasticEngine

    Parameters
    ----------

    states : QList[QQuickStochasticState]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickStochasticEngine::QQuickStochasticEngine(const
    #      QList<QQuickStochasticState *> &states, QObject *parent)
    self._noteCreation(QQuickStochasticEngine, lambda: Rituals.call(
        'ritual_ZN22QQuickStochasticEngineC1ERK5QListIP21QQuickStochasticSt'
        'ateEP7QObject',
        self._valueOf(states), self._addressOf(parent, 'QObject'),
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

  @overload()
  @overload(int)
  @overload(int, int)
  def start(self, index: int = 0, state: int = 0) -> None:
    """
    Calls Qt's 'void QQuickStochasticEngine::start(int index, int state)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstochasticengine.html#start

    Parameters
    ----------

    index : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    state : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QQuickStochasticEngine::start(int index, int state)
    self.uglySide.call(
        'ritual_ZN22QQuickStochasticEngine5startEii', index, state,
    )

  @overload()
  @overload(int)
  def restart(self, index: int = 0) -> None:
    """
    Calls Qt's 'void QQuickStochasticEngine::restart(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticengine.html#restart

    Parameters
    ----------

    index : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QQuickStochasticEngine::restart(int index)
    ritual = 'ritual_ZN22QQuickStochasticEngine7restartEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickStochasticEngine7restartEi'
    self.uglySide.call(ritual, index)

  @overload()
  @overload(int)
  def advance(self, index: int = 0) -> None:
    """
    Calls Qt's 'void QQuickStochasticEngine::advance(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticengine.html#advance

    Parameters
    ----------

    index : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QQuickStochasticEngine::advance(int index)
    ritual = 'ritual_ZN22QQuickStochasticEngine7advanceEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickStochasticEngine7advanceEi'
    self.uglySide.call(ritual, index)

  @overload()
  @overload(int)
  def stop(self, index: int = 0) -> None:
    """
    Calls Qt's 'void QQuickStochasticEngine::stop(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstochasticengine.html#stop

    Parameters
    ----------

    index : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QQuickStochasticEngine::stop(int index)
    self.uglySide.call('ritual_ZN22QQuickStochasticEngine4stopEi', index)

  def stateCount(self) -> int:
    """
    Calls Qt's 'int QQuickStochasticEngine::stateCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticengine.html#stateCount
    """
    #  int QQuickStochasticEngine::stateCount()
    return self.uglySide.call(
        'ritual_ZN22QQuickStochasticEngine10stateCountEv',
    )

  @overload(str)
  def globalGoalChanged(self, arg: str) -> None:
    """
    Calls Qt's 'void QQuickStochasticEngine::globalGoalChanged(const QString
    &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticengine.html#globalGoalChanged

    Parameters
    ----------

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickStochasticEngine::globalGoalChanged(const QString &arg)
    self.uglySide.call(
        'ritual_ZN22QQuickStochasticEngine17globalGoalChangedERK7QString',
        arg,
    )

  @overload(int)
  def stateChanged(self, idx: int) -> None:
    """
    Calls Qt's 'void QQuickStochasticEngine::stateChanged(int idx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticengine.html#stateChanged

    Parameters
    ----------

    idx : int
      Passed on as it is.
    """
    #  void QQuickStochasticEngine::stateChanged(int idx)
    self.uglySide.call(
        'ritual_ZN22QQuickStochasticEngine12stateChangedEi', idx,
    )

  @overload(int)
  def updateSprites(self, time: int) -> int:
    """
    Calls Qt's 'uint QQuickStochasticEngine::updateSprites(uint time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticengine.html#updateSprites

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  uint QQuickStochasticEngine::updateSprites(uint time)
    return self.uglySide.call(
        'ritual_ZN22QQuickStochasticEngine13updateSpritesEj', time,
    )

  @overload(int, int)
  def addToUpdateList(self, t: int, idx: int) -> None:
    """
    Calls Qt's 'void QQuickStochasticEngine::addToUpdateList(uint t, int
    idx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticengine.html#addToUpdateList

    Parameters
    ----------

    t : int
      Passed on as it is.

    idx : int
      Passed on as it is.
    """
    #  void QQuickStochasticEngine::addToUpdateList(uint t, int idx)
    self.uglySide.call(
        'ritual_ZN22QQuickStochasticEngine15addToUpdateListEji', t, idx,
    )

  @overload(int)
  @overload(int, int)
  def nextState(self, curState: int, idx: int = 0) -> int:
    """
    Calls Qt's 'int QQuickStochasticEngine::nextState(int curState, int
    idx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticengine.html#nextState

    Parameters
    ----------

    curState : int
      Passed on as it is.

    idx : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QQuickStochasticEngine::nextState(int curState, int idx)
    return self.uglySide.call(
        'ritual_ZN22QQuickStochasticEngine9nextStateEii', curState, idx,
    )

  @overload(int, int)
  @overload(int, int, int)
  def goalSeek(self, curState: int, idx: int, dist: int = -1) -> int:
    """
    Calls Qt's 'int QQuickStochasticEngine::goalSeek(int curState, int idx,
    int dist)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstochasticengine.html#goalSeek

    Parameters
    ----------

    curState : int
      Passed on as it is.

    idx : int
      Passed on as it is.

    dist : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  int QQuickStochasticEngine::goalSeek(int curState, int idx, int dist)
    return self.uglySide.call(
        'ritual_ZN22QQuickStochasticEngine8goalSeekEiii',
        curState, idx, dist,
    )

  @staticmethod
  def states(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickStochasticState>
    QQuickStochasticEngine::states()': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QQuickStochasticEngine.states' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickStochasticState> "
        "QQuickStochasticEngine::states()': gives a type Python has no way "
        "to take yet.")
