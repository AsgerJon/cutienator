"""
QEventLoopLocker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qeventloop.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QEventLoop, QThread
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEventLoop = WAIT['QEventLoop']
  QThread = WAIT['QThread']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QEventLoopLocker(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QEventLoopLocker: a plain Python object standing in
  front of one C++ QEventLoopLocker.

  What exists
  -----------

  No function of Qt's QEventLoopLocker yet. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QEventLoopLocker::~QEventLoopLocker()': the destructor: Python
    never removes a C++ QEventLoopLocker.

  What has no ritual
  ------------------

  9 of the 13 functions Qt declares: 3 takes or gives a type that cannot be
  passed yet; 3 private; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QEventLoopLocker is created at the first use, not by
    'QEventLoopLocker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QEventLoopLocker.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QEventLoopLocker'

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
    Notes what was given, for Qt's 'QEventLoopLocker::QEventLoopLocker()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventlooplocker.html#QEventLoopLocker
    """
    #  QEventLoopLocker::QEventLoopLocker()
    self._noteCreation(QEventLoopLocker, lambda: Rituals.call(
        'ritual_ZN16QEventLoopLockerC1Ev',
    ))

  @overload(QEventLoop)
  @overload(NoneType)
  def __init__(self, loop: Optional[QEventLoop]) -> None:
    """
    Notes what was given, for Qt's
    'QEventLoopLocker::QEventLoopLocker(QEventLoop *loop)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventlooplocker.html#QEventLoopLocker

    Parameters
    ----------

    loop : Optional[QEventLoop]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QEventLoopLocker::QEventLoopLocker(QEventLoop *loop)
    self._noteCreation(QEventLoopLocker, lambda: Rituals.call(
        'ritual_ZN16QEventLoopLockerC1EP10QEventLoop', self._addressOf(loop),
    ))

  @overload(QThread)
  def __init__(self, thread: Optional[QThread]) -> None:
    """
    Notes what was given, for Qt's
    'QEventLoopLocker::QEventLoopLocker(QThread *thread)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventlooplocker.html#QEventLoopLocker

    Parameters
    ----------

    thread : Optional[QThread]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QEventLoopLocker::QEventLoopLocker(QThread *thread)
    self._noteCreation(QEventLoopLocker, lambda: Rituals.call(
        'ritual_ZN16QEventLoopLockerC1EP7QThread', self._addressOf(thread),
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
