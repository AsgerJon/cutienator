"""
QQmlIncubationController binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qqmlincubator.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlEngine


class QQmlIncubationController(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlIncubationController: a plain Python object
  standing in front of one C++ QQmlIncubationController.

  What exists
  -----------

  Every function of Qt's QQmlIncubationController that has a ritual and that
  Python can call so far, 4 names in all: 'engine', 'incubatingObjectCount',
  'incubateFor', 'incubatingObjectCountChanged'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlIncubationController::~QQmlIncubationController()': the
    destructor: Python never removes a C++ QQmlIncubationController.
  - Qt's 'void QQmlIncubationController::incubateWhile(std::atomic<bool>
    *flag, int msecs)': names 'std::atomic<bool>', which has no cute class
    yet.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QQmlIncubationController is created at the first use, not by
    'QQmlIncubationController(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlIncubationController.
  - Each name of Qt's QQmlIncubationController that has no cute function yet,
    'incubateWhile', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlIncubationController'

  #  A C++ QQmlIncubationController Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlIncubationController'

  #  The functions Qt calls itself that QQmlIncubationController is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'incubatingObjectCountChanged': (
          ('_ZN24QQmlIncubationController28incubatingObjectCountChangedEi',
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

  def engine(self) -> Optional[QQmlEngine]:
    """
    Calls Qt's 'QQmlEngine *QQmlIncubationController::engine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlincubationcontroller.html#engine

    Returns
    -------

    Optional[QQmlEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlEngine *QQmlIncubationController::engine() const
    address = self.uglySide.call(
        'ritual_ZNK24QQmlIncubationController6engineEv',
    )
    from . import QQmlEngine
    return QQmlEngine._cuteAt(address)

  def incubatingObjectCount(self) -> int:
    """
    Calls Qt's 'int QQmlIncubationController::incubatingObjectCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlincubationcontroller.html
    """
    #  int QQmlIncubationController::incubatingObjectCount() const
    return self.uglySide.call(
        'ritual_ZNK24QQmlIncubationController21incubatingObjectCountEv',
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
    'QQmlIncubationController::QQmlIncubationController()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlincubationcontroller.html
    """
    #  QQmlIncubationController::QQmlIncubationController()
    self._noteCreation(QQmlIncubationController, lambda: Rituals.call(
        'ritual_ZN24QQmlIncubationControllerC1Ev',
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

  @overload(int)
  def incubateFor(self, msecs: int) -> None:
    """
    Calls Qt's 'void QQmlIncubationController::incubateFor(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlincubationcontroller.html#incubateFor

    Parameters
    ----------

    msecs : int
      Passed on as it is.
    """
    #  void QQmlIncubationController::incubateFor(int msecs)
    self.uglySide.call(
        'ritual_ZN24QQmlIncubationController11incubateForEi', msecs,
    )

  @overload(int)
  def incubatingObjectCountChanged(self, a0: int) -> None:
    """
    Calls Qt's 'void
    QQmlIncubationController::incubatingObjectCountChanged(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlincubationcontroller.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlIncubationController::incubatingObjectCountChanged(int a0)
    ritual = (
        'ritual_ZN24QQmlIncubationController28incubatingObjectCountChangedE'
        'i')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQmlIncubationController28incubatingObjectCountCh'
          'angedEi')
    self.uglySide.call(ritual, a0)

  @staticmethod
  def incubateWhile(*__, **_) -> Never:
    """
    Qt's 'void QQmlIncubationController::incubateWhile(std::atomic<bool>
    *flag, int msecs)': names 'std::atomic<bool>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQmlIncubationController.incubateWhile' has no cute function yet. "
        "Qt's 'void "
        "QQmlIncubationController::incubateWhile(std::atomic<bool> *flag, "
        "int msecs)': names 'std::atomic<bool>', which has no cute class "
        "yet.")
