"""
QtTaskTree::QThreadFunctionBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTaskTree/qthreadfunctiontask.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QThreadPool
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QThreadPool = WAIT['QThreadPool']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QThreadFunctionBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtTaskTree::QThreadFunctionBase: a plain Python
  object standing in front of one C++ QtTaskTree::QThreadFunctionBase.

  What exists
  -----------

  Every function of Qt's QtTaskTree::QThreadFunctionBase that has a ritual
  and that Python can call so far, 7 names in all: 'setThreadPool',
  'threadPool', 'setAutoDelayedSync', 'isAutoDelayedSync', 'setSyncSkipped',
  'isSyncSkipped', 'syncAll'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtTaskTree::QThreadFunctionBase::~QThreadFunctionBase()': the
    destructor: Python never removes a C++ QtTaskTree::QThreadFunctionBase.
  - Qt's 'void QtTaskTree::QThreadFunctionBase::storeFuture(const
    QFuture<void> &future)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  6 of the 16 functions Qt declares: 4 forbidden; 2 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QtTaskTree::QThreadFunctionBase is created at the first use, not
    by 'QtTaskTree::QThreadFunctionBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtTaskTree::QThreadFunctionBase.
  - Each name of Qt's QtTaskTree::QThreadFunctionBase that has no cute
    function yet, 'd_func', 'storeFuture', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def syncAll() -> None:
    """
    Calls Qt's 'void QtTaskTree::QThreadFunctionBase::syncAll()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qthreadfunctionbase.html#syncAll
    """
    #  void QtTaskTree::QThreadFunctionBase::syncAll()
    Rituals.call('ritual_ZN10QtTaskTree19QThreadFunctionBase7syncAllEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtTaskTree::QThreadFunctionBase'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def threadPool(self) -> Optional[QThreadPool]:
    """
    Calls Qt's 'QThreadPool *QtTaskTree::QThreadFunctionBase::threadPool()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qthreadfunctionbase.html#threadPool

    Returns
    -------

    Optional[QThreadPool]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QThreadPool *QtTaskTree::QThreadFunctionBase::threadPool() const
    address = self.uglySide.call(
        'ritual_ZNK10QtTaskTree19QThreadFunctionBase10threadPoolEv',
    )
    from ..QtCore import QThreadPool
    return QThreadPool._cuteAt(address)

  def isAutoDelayedSync(self) -> bool:
    """
    Calls Qt's 'bool QtTaskTree::QThreadFunctionBase::isAutoDelayedSync()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qthreadfunctionbase.html
    """
    #  bool QtTaskTree::QThreadFunctionBase::isAutoDelayedSync() const
    return self.uglySide.call(
        'ritual_ZNK10QtTaskTree19QThreadFunctionBase17isAutoDelayedSyncEv',
    )

  def isSyncSkipped(self) -> bool:
    """
    Calls Qt's 'bool QtTaskTree::QThreadFunctionBase::isSyncSkipped() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qthreadfunctionbase.html#isSyncSkipped
    """
    #  bool QtTaskTree::QThreadFunctionBase::isSyncSkipped() const
    return self.uglySide.call(
        'ritual_ZNK10QtTaskTree19QThreadFunctionBase13isSyncSkippedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QThreadPool)
  @overload(NoneType)
  def setThreadPool(self, pool: Optional[QThreadPool]) -> None:
    """
    Calls Qt's 'void
    QtTaskTree::QThreadFunctionBase::setThreadPool(QThreadPool *pool)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qthreadfunctionbase.html#setThreadPool

    Parameters
    ----------

    pool : Optional[QThreadPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtTaskTree::QThreadFunctionBase::setThreadPool(QThreadPool *pool)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree19QThreadFunctionBase13setThreadPoolEP11QThre'
        'adPool',
        self._addressOf(pool),
    )

  @overload(bool)
  def setAutoDelayedSync(self, on: bool) -> None:
    """
    Calls Qt's 'void QtTaskTree::QThreadFunctionBase::setAutoDelayedSync(bool
    on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qthreadfunctionbase.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QtTaskTree::QThreadFunctionBase::setAutoDelayedSync(bool on)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree19QThreadFunctionBase18setAutoDelayedSyncEb',
        on,
    )

  @overload(bool)
  def setSyncSkipped(self, on: bool) -> None:
    """
    Calls Qt's 'void QtTaskTree::QThreadFunctionBase::setSyncSkipped(bool
    on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qthreadfunctionbase.html#setSyncSkipped

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QtTaskTree::QThreadFunctionBase::setSyncSkipped(bool on)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree19QThreadFunctionBase14setSyncSkippedEb', on,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QtTaskTree::QThreadFunctionBase::QThreadFunctionBase()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qthreadfunctionbase.html
    """
    #  QtTaskTree::QThreadFunctionBase::QThreadFunctionBase()
    self._noteCreation(QThreadFunctionBase, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree19QThreadFunctionBaseC1Ev',
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

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QThreadFunctionBasePrivate
      *QtTaskTree::QThreadFunctionBase::d_func()': the compiler refuses its
      ritual as it would be written here: unknown type name
      'QThreadFunctionBasePrivate'; did you mean
      'QtTaskTree::QThreadFunctionBasePrivate'?.
    - Qt's 'const QThreadFunctionBasePrivate
      *QtTaskTree::QThreadFunctionBase::d_func() const': the compiler refuses
      its ritual as it would be written here: unknown type name
      'QThreadFunctionBasePrivate'; did you mean
      'QtTaskTree::QThreadFunctionBasePrivate'?.
    """
    raise NotImplementedError(
        "'QtTaskTree.QThreadFunctionBase.d_func' has no cute function yet. "
        "Qt's 'QThreadFunctionBasePrivate "
        "*QtTaskTree::QThreadFunctionBase::d_func()': the compiler refuses "
        "its ritual as it would be written here: unknown type name "
        "'QThreadFunctionBasePrivate'; did you mean "
        "'QtTaskTree::QThreadFunctionBasePrivate'?. Qt's 'const "
        "QThreadFunctionBasePrivate "
        "*QtTaskTree::QThreadFunctionBase::d_func() const': the compiler "
        "refuses its ritual as it would be written here: unknown type name "
        "'QThreadFunctionBasePrivate'; did you mean "
        "'QtTaskTree::QThreadFunctionBasePrivate'?.")

  @staticmethod
  def storeFuture(*__, **_) -> Never:
    """
    Qt's 'void QtTaskTree::QThreadFunctionBase::storeFuture(const
    QFuture<void> &future)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtTaskTree.QThreadFunctionBase.storeFuture' has no cute function "
        "yet. Qt's 'void QtTaskTree::QThreadFunctionBase::storeFuture(const "
        "QFuture<void> &future)': takes a type Python has no way to hand "
        "over yet.")
