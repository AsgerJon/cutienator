"""
QtTaskTree::QBarrier binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTaskTree/qbarriertask.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QtTaskTree

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBarrier(QObject):
  """
  The cute side of Qt's QtTaskTree::QBarrier: a plain Python object standing
  in front of one C++ QtTaskTree::QBarrier.

  It is built on the cute 'QObject', as Qt's QtTaskTree::QBarrier is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtTaskTree::QBarrier that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'tr', 'setLimit',
  'limit', 'start', 'advance', 'stopWithResult', 'isRunning', 'current',
  'done', 'event'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtTaskTree::QBarrier::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QtTaskTree::QBarrier::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QtTaskTree::QBarrier::~QBarrier()': the destructor: Python never
    removes a C++ QtTaskTree::QBarrier.
  - Qt's 'std::optional<DoneResult> QtTaskTree::QBarrier::result() const':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 21 functions Qt declares: 2 not a gap; 2 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QtTaskTree::QBarrier is created at the first use, not by
    'QtTaskTree::QBarrier(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtTaskTree::QBarrier.
  - Qt tells when it has removed the C++ QtTaskTree::QBarrier. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QtTaskTree::QBarrier that has no cute function yet,
    'result', holds a function that raises 'NotImplementedError', and its
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
    Calls Qt's 'QString QtTaskTree::QBarrier::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-qbarrier.html#tr

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
    #  QString QtTaskTree::QBarrier::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QtTaskTree8QBarrier2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtTaskTree::QBarrier'

  #  A C++ QtTaskTree::QBarrier Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtTaskTree_QBarrier'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QtTaskTree::QBarrier::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qbarrier.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtTaskTree::QBarrier::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10QtTaskTree8QBarrier10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def limit(self) -> int:
    """
    Calls Qt's 'qsizetype QtTaskTree::QBarrier::limit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-qbarrier.html#limit
    """
    #  qsizetype QtTaskTree::QBarrier::limit() const
    return self.uglySide.call('ritual_ZNK10QtTaskTree8QBarrier5limitEv')

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QtTaskTree::QBarrier::isRunning() const'.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-qbarrier.html#isRunning
    """
    #  bool QtTaskTree::QBarrier::isRunning() const
    return self.uglySide.call('ritual_ZNK10QtTaskTree8QBarrier9isRunningEv')

  def current(self) -> int:
    """
    Calls Qt's 'qsizetype QtTaskTree::QBarrier::current() const'.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-qbarrier.html#current
    """
    #  qsizetype QtTaskTree::QBarrier::current() const
    return self.uglySide.call('ritual_ZNK10QtTaskTree8QBarrier7currentEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setLimit(self, value: int) -> None:
    """
    Calls Qt's 'void QtTaskTree::QBarrier::setLimit(qsizetype value)'.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-qbarrier.html#setLimit

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QtTaskTree::QBarrier::setLimit(qsizetype value)
    self.uglySide.call('ritual_ZN10QtTaskTree8QBarrier8setLimitEx', value)

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QtTaskTree::QBarrier::QBarrier()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-qbarrier.html#QBarrier
    """
    #  QtTaskTree::QBarrier::QBarrier()
    self._noteCreation(QBarrier, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree8QBarrierC1Ev',
    ))

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QtTaskTree::QBarrier::QBarrier(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-qbarrier.html#QBarrier

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QtTaskTree::QBarrier::QBarrier(QObject *parent)
    self._noteCreation(QBarrier, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree8QBarrierC1EP7QObject',
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

  def start(self) -> None:
    """
    Calls Qt's 'void QtTaskTree::QBarrier::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-qbarrier.html#start
    """
    #  void QtTaskTree::QBarrier::start()
    self.uglySide.call('ritual_ZN10QtTaskTree8QBarrier5startEv')

  def advance(self) -> None:
    """
    Calls Qt's 'void QtTaskTree::QBarrier::advance()'.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-qbarrier.html#advance
    """
    #  void QtTaskTree::QBarrier::advance()
    self.uglySide.call('ritual_ZN10QtTaskTree8QBarrier7advanceEv')

  @overload(QtTaskTree.DoneResult)
  def stopWithResult(self, result: QtTaskTree.DoneResult) -> None:
    """
    Calls Qt's 'void QtTaskTree::QBarrier::stopWithResult(DoneResult
    result)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qbarrier.html#stopWithResult

    Parameters
    ----------

    result : QtTaskTree.DoneResult
      Passed on as its number.
    """
    #  void QtTaskTree::QBarrier::stopWithResult(DoneResult result)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree8QBarrier14stopWithResultENS_10DoneResultE',
        result.value,
    )

  @overload(QtTaskTree.DoneResult)
  def done(self, success: QtTaskTree.DoneResult) -> None:
    """
    Calls Qt's 'void QtTaskTree::QBarrier::done(QtTaskTree::DoneResult
    success, QPrivateSignal a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-qbarrier.html#done

    Parameters
    ----------

    success : QtTaskTree.DoneResult
      Passed on as its number.
    """
    #  void QtTaskTree::QBarrier::done(QtTaskTree::DoneResult success,
    #      QPrivateSignal a1)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree8QBarrier4doneENS_10DoneResultENS0_14QPrivate'
        'SignalE',
        success.value,
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QtTaskTree::QBarrier::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-qbarrier.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QtTaskTree::QBarrier::event(QEvent *event)
    ritual = 'ritual_ZN10QtTaskTree8QBarrier5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QtTaskTree8QBarrier5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @staticmethod
  def result(*__, **_) -> Never:
    """
    Qt's 'std::optional<DoneResult> QtTaskTree::QBarrier::result() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtTaskTree.QBarrier.result' has no cute function yet. Qt's "
        "'std::optional<DoneResult> QtTaskTree::QBarrier::result() const': "
        "gives a type Python has no way to take yet.")
