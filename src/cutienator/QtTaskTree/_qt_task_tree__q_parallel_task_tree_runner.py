"""
QtTaskTree::QParallelTaskTreeRunner binding of the Qt C++
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


class QParallelTaskTreeRunner(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtTaskTree::QParallelTaskTreeRunner: a plain Python
  object standing in front of one C++ QtTaskTree::QParallelTaskTreeRunner.

  What exists
  -----------

  Every function of Qt's QtTaskTree::QParallelTaskTreeRunner that has a
  ritual and that Python can call so far, 3 names in all: 'isRunning',
  'cancel', 'reset'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtTaskTree::QParallelTaskTreeRunner::~QParallelTaskTreeRunner()':
    the destructor: Python never removes a C++
    QtTaskTree::QParallelTaskTreeRunner.
  - Qt's 'void QtTaskTree::QParallelTaskTreeRunner::startImpl(const Group
    &recipe, const TreeSetupHandler &setupHandler, const TreeDoneHandler
    &doneHandler, CallDone callDone)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  7 of the 13 functions Qt declares: 4 forbidden; 2 the compiler refuses its
  ritual as it would be written here; 1 a template.

  What to expect
  --------------

  - The C++ QtTaskTree::QParallelTaskTreeRunner is created at the first use,
    not by 'QtTaskTree::QParallelTaskTreeRunner(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtTaskTree::QParallelTaskTreeRunner.
  - Each name of Qt's QtTaskTree::QParallelTaskTreeRunner that has no cute
    function yet, 'd_func', 'start', 'startImpl', holds a function that
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
  __qt_class__ = 'QtTaskTree::QParallelTaskTreeRunner'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QtTaskTree::QParallelTaskTreeRunner::isRunning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qparalleltasktreerunner.html#isRunning
    """
    #  bool QtTaskTree::QParallelTaskTreeRunner::isRunning() const
    return self.uglySide.call(
        'ritual_ZNK10QtTaskTree23QParallelTaskTreeRunner9isRunningEv',
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
    'QtTaskTree::QParallelTaskTreeRunner::QParallelTaskTreeRunner()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qparalleltasktreerunner.html
    """
    #  QtTaskTree::QParallelTaskTreeRunner::QParallelTaskTreeRunner()
    self._noteCreation(QParallelTaskTreeRunner, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree23QParallelTaskTreeRunnerC1Ev',
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
    Calls Qt's 'void QtTaskTree::QParallelTaskTreeRunner::cancel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qparalleltasktreerunner.html#cancel
    """
    #  void QtTaskTree::QParallelTaskTreeRunner::cancel()
    self.uglySide.call(
        'ritual_ZN10QtTaskTree23QParallelTaskTreeRunner6cancelEv',
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QtTaskTree::QParallelTaskTreeRunner::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qparalleltasktreerunner.html#reset
    """
    #  void QtTaskTree::QParallelTaskTreeRunner::reset()
    self.uglySide.call(
        'ritual_ZN10QtTaskTree23QParallelTaskTreeRunner5resetEv',
    )

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QParallelTaskTreeRunnerPrivate
      *QtTaskTree::QParallelTaskTreeRunner::d_func()': the compiler refuses
      its ritual as it would be written here: unknown type name
      'QParallelTaskTreeRunnerPrivate'; did you mean
      'QtTaskTree::QParallelTaskTreeRunnerPrivate'?.
    - Qt's 'const QParallelTaskTreeRunnerPrivate
      *QtTaskTree::QParallelTaskTreeRunner::d_func() const': the compiler
      refuses its ritual as it would be written here: unknown type name
      'QParallelTaskTreeRunnerPrivate'; did you mean
      'QtTaskTree::QParallelTaskTreeRunnerPrivate'?.
    """
    raise NotImplementedError(
        "'QtTaskTree.QParallelTaskTreeRunner.d_func' has no cute function "
        "yet. Qt's 'QParallelTaskTreeRunnerPrivate "
        "*QtTaskTree::QParallelTaskTreeRunner::d_func()': the compiler "
        "refuses its ritual as it would be written here: unknown type name "
        "'QParallelTaskTreeRunnerPrivate'; did you mean "
        "'QtTaskTree::QParallelTaskTreeRunnerPrivate'?. Qt's 'const "
        "QParallelTaskTreeRunnerPrivate "
        "*QtTaskTree::QParallelTaskTreeRunner::d_func() const': the "
        "compiler refuses its ritual as it would be written here: unknown "
        "type name 'QParallelTaskTreeRunnerPrivate'; did you mean "
        "'QtTaskTree::QParallelTaskTreeRunnerPrivate'?.")

  @staticmethod
  def start(*__, **_) -> Never:
    """
    Qt's 'QtTaskTree::QParallelTaskTreeRunner::start': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QtTaskTree.QParallelTaskTreeRunner.start' has no cute function "
        "yet. Qt's 'QtTaskTree::QParallelTaskTreeRunner::start': a "
        "template: a pattern and no single function.")

  @staticmethod
  def startImpl(*__, **_) -> Never:
    """
    Qt's 'void QtTaskTree::QParallelTaskTreeRunner::startImpl(const Group
    &recipe, const TreeSetupHandler &setupHandler, const TreeDoneHandler
    &doneHandler, CallDone callDone)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QtTaskTree.QParallelTaskTreeRunner.startImpl' has no cute "
        "function yet. Qt's 'void "
        "QtTaskTree::QParallelTaskTreeRunner::startImpl(const Group "
        "&recipe, const TreeSetupHandler &setupHandler, const "
        "TreeDoneHandler &doneHandler, CallDone callDone)': takes a type "
        "Python has no way to hand over yet.")
