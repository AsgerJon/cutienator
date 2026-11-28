"""
QThreadPipe binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qeventdispatcher_unix_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QThreadPipe to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QThreadPipe(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QThreadPipe: a plain Python object standing in front
  of one C++ QThreadPipe.

  C++ hands a QThreadPipe around as a copy, so every C++ QThreadPipe behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QThreadPipe that has a ritual and that Python can
  call so far, 1 name in all: 'wakeUp'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QThreadPipe::~QThreadPipe()': the destructor: Python removes its
    C++ QThreadPipe by it, and has no other use for it.
  - Qt's 'pollfd QThreadPipe::prepare() const': gives a type Python has no
    way to take yet.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QThreadPipe is created at the first use, not by
    'QThreadPipe(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QThreadPipe back gives a copy the ritual made for
    Python, in a new cute QThreadPipe.
  - Each name of Qt's QThreadPipe that has no cute function yet, 'check',
    'init', 'prepare', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QThreadPipe'

  #  Qt's '~QThreadPipe()'. Naming it makes this a value class: Python owns
  #  every C++ QThreadPipe behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QThreadPipeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's 'QThreadPipe::QThreadPipe()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpipe.html#QThreadPipe
    """
    #  QThreadPipe::QThreadPipe()
    self._noteCreation(QThreadPipe, lambda: Rituals.call(
        'ritual_ZN11QThreadPipeC1Ev',
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

  def wakeUp(self) -> None:
    """
    Calls Qt's 'void QThreadPipe::wakeUp()'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpipe.html#wakeUp
    """
    #  void QThreadPipe::wakeUp()
    self.uglySide.call('ritual_ZN11QThreadPipe6wakeUpEv')

  @staticmethod
  def check(*__, **_) -> Never:
    """
    Qt's 'int QThreadPipe::check(const pollfd &pfd)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'UsingEventfd'.
    """
    raise NotImplementedError(
        "'QThreadPipe.check' has no cute function yet. Qt's 'int "
        "QThreadPipe::check(const pollfd &pfd)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'UsingEventfd'.")

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'bool QThreadPipe::init()': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'UsingEventfd'.
    """
    raise NotImplementedError(
        "'QThreadPipe.init' has no cute function yet. Qt's 'bool "
        "QThreadPipe::init()': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'UsingEventfd'.")

  @staticmethod
  def prepare(*__, **_) -> Never:
    """
    Qt's 'pollfd QThreadPipe::prepare() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QThreadPipe.prepare' has no cute function yet. Qt's 'pollfd "
        "QThreadPipe::prepare() const': gives a type Python has no way to "
        "take yet.")
