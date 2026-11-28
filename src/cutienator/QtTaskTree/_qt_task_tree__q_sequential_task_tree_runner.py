"""
QtTaskTree::QSequentialTaskTreeRunner binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTaskTree/qtasktreerunner.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSequentialTaskTreeRunner(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtTaskTree::QSequentialTaskTreeRunner: a plain Python
  object standing in front of one C++ QtTaskTree::QSequentialTaskTreeRunner.

  What exists
  -----------

  Every function of Qt's QtTaskTree::QSequentialTaskTreeRunner that has a
  ritual and that Python can call so far, 5 names in all: 'isRunning',
  'cancel', 'reset', 'cancelCurrent', 'resetCurrent'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QtTaskTree::QSequentialTaskTreeRunner::~QSequentialTaskTreeRunner()':
    the destructor: Python never removes a C++
    QtTaskTree::QSequentialTaskTreeRunner.
  - Qt's 'void QtTaskTree::QSequentialTaskTreeRunner::enqueueImpl(const Group
    &recipe, const TreeSetupHandler &setupHandler, const TreeDoneHandler
    &doneHandler, CallDone callDone)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  7 of the 15 functions Qt declares: 4 forbidden; 2 the compiler refuses its
  ritual as it would be written here; 1 a template.

  What to expect
  --------------

  - The C++ QtTaskTree::QSequentialTaskTreeRunner is created at the first
    use, not by 'QtTaskTree::QSequentialTaskTreeRunner(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtTaskTree::QSequentialTaskTreeRunner.
  - Each name of Qt's QtTaskTree::QSequentialTaskTreeRunner that has no cute
    function yet, 'd_func', 'enqueue', 'enqueueImpl', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtTaskTree::QSequentialTaskTreeRunner'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QtTaskTree::QSequentialTaskTreeRunner::isRunning()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qsequentialtasktreerunner.html
    """
    #  bool QtTaskTree::QSequentialTaskTreeRunner::isRunning() const
    return self.uglySide.call(
        'ritual_ZNK10QtTaskTree25QSequentialTaskTreeRunner9isRunningEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QtTaskTree::QSequentialTaskTreeRunner::QSequentialTaskTreeRunner()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qsequentialtasktreerunner.html
    """
    #  QtTaskTree::QSequentialTaskTreeRunner::QSequentialTaskTreeRunner()
    self._noteCreation(QSequentialTaskTreeRunner, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree25QSequentialTaskTreeRunnerC1Ev',
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

  def cancel(self) -> None:
    """
    Calls Qt's 'void QtTaskTree::QSequentialTaskTreeRunner::cancel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qsequentialtasktreerunner.html#cancel
    """
    #  void QtTaskTree::QSequentialTaskTreeRunner::cancel()
    self.uglySide.call(
        'ritual_ZN10QtTaskTree25QSequentialTaskTreeRunner6cancelEv',
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QtTaskTree::QSequentialTaskTreeRunner::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qsequentialtasktreerunner.html#reset
    """
    #  void QtTaskTree::QSequentialTaskTreeRunner::reset()
    self.uglySide.call(
        'ritual_ZN10QtTaskTree25QSequentialTaskTreeRunner5resetEv',
    )

  def cancelCurrent(self) -> None:
    """
    Calls Qt's 'void QtTaskTree::QSequentialTaskTreeRunner::cancelCurrent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qsequentialtasktreerunner.html
    """
    #  void QtTaskTree::QSequentialTaskTreeRunner::cancelCurrent()
    self.uglySide.call(
        'ritual_ZN10QtTaskTree25QSequentialTaskTreeRunner13cancelCurrentEv',
    )

  def resetCurrent(self) -> None:
    """
    Calls Qt's 'void QtTaskTree::QSequentialTaskTreeRunner::resetCurrent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qsequentialtasktreerunner.html
    """
    #  void QtTaskTree::QSequentialTaskTreeRunner::resetCurrent()
    self.uglySide.call(
        'ritual_ZN10QtTaskTree25QSequentialTaskTreeRunner12resetCurrentEv',
    )

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QSequentialTaskTreeRunnerPrivate
      *QtTaskTree::QSequentialTaskTreeRunner::d_func()': the compiler refuses
      its ritual as it would be written here: unknown type name
      'QSequentialTaskTreeRunnerPrivate'; did you mean
      'QtTaskTree::QSequentialTaskTreeRunnerPrivate'?.
    - Qt's 'const QSequentialTaskTreeRunnerPrivate
      *QtTaskTree::QSequentialTaskTreeRunner::d_func() const': the compiler
      refuses its ritual as it would be written here: unknown type name
      'QSequentialTaskTreeRunnerPrivate'; did you mean
      'QtTaskTree::QSequentialTaskTreeRunnerPrivate'?.
    """
    raise NotImplementedError(
        "'QtTaskTree.QSequentialTaskTreeRunner.d_func' has no cute function "
        "yet. Qt's 'QSequentialTaskTreeRunnerPrivate "
        "*QtTaskTree::QSequentialTaskTreeRunner::d_func()': the compiler "
        "refuses its ritual as it would be written here: unknown type name "
        "'QSequentialTaskTreeRunnerPrivate'; did you mean "
        "'QtTaskTree::QSequentialTaskTreeRunnerPrivate'?. Qt's 'const "
        "QSequentialTaskTreeRunnerPrivate "
        "*QtTaskTree::QSequentialTaskTreeRunner::d_func() const': the "
        "compiler refuses its ritual as it would be written here: unknown "
        "type name 'QSequentialTaskTreeRunnerPrivate'; did you mean "
        "'QtTaskTree::QSequentialTaskTreeRunnerPrivate'?.")

  @staticmethod
  def enqueue(*__, **_) -> Never:
    """
    Qt's 'QtTaskTree::QSequentialTaskTreeRunner::enqueue': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QtTaskTree.QSequentialTaskTreeRunner.enqueue' has no cute "
        "function yet. Qt's "
        "'QtTaskTree::QSequentialTaskTreeRunner::enqueue': a template: a "
        "pattern and no single function.")

  @staticmethod
  def enqueueImpl(*__, **_) -> Never:
    """
    Qt's 'void QtTaskTree::QSequentialTaskTreeRunner::enqueueImpl(const Group
    &recipe, const TreeSetupHandler &setupHandler, const TreeDoneHandler
    &doneHandler, CallDone callDone)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QtTaskTree.QSequentialTaskTreeRunner.enqueueImpl' has no cute "
        "function yet. Qt's 'void "
        "QtTaskTree::QSequentialTaskTreeRunner::enqueueImpl(const Group "
        "&recipe, const TreeSetupHandler &setupHandler, const "
        "TreeDoneHandler &doneHandler, CallDone callDone)': takes a type "
        "Python has no way to hand over yet.")
