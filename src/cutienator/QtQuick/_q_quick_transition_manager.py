"""
QQuickTransitionManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktransitionmanager_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickTransitionManager to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QQuickState, QQuickStateAction, QQuickTransition
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQuickState = WAIT['QQuickState']
  QQuickStateAction = WAIT['QQuickStateAction']
  QQuickTransition = WAIT['QQuickTransition']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTransitionManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickTransitionManager: a plain Python object
  standing in front of one C++ QQuickTransitionManager.

  What exists
  -----------

  Every function of Qt's QQuickTransitionManager that has a ritual and that
  Python can call so far, 6 names in all: 'isRunning', 'transition',
  'cancel', 'finished', 'complete', 'setState'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickTransitionManager::~QQuickTransitionManager()': the
    destructor: Python never removes a C++ QQuickTransitionManager.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickTransitionManager is created at the first use, not by
    'QQuickTransitionManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTransitionManager.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTransitionManager'

  #  A C++ QQuickTransitionManager Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTransitionManager'

  #  The functions Qt calls itself that QQuickTransitionManager is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'finished': (
          ('_ZN23QQuickTransitionManager8finishedEv',
           ('nothing', 'nothing', ''),
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

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QQuickTransitionManager::isRunning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktransitionmanager.html#isRunning
    """
    #  bool QQuickTransitionManager::isRunning() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickTransitionManager9isRunningEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickState)
  @overload(NoneType)
  def setState(self, a0: Optional[QQuickState]) -> None:
    """
    Calls Qt's 'void QQuickTransitionManager::setState(QQuickState *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktransitionmanager.html#setState

    Parameters
    ----------

    a0 : Optional[QQuickState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTransitionManager::setState(QQuickState *a0)
    self.uglySide.call(
        'ritual_ZN23QQuickTransitionManager8setStateEP11QQuickState',
        self._addressOf(a0),
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
    'QQuickTransitionManager::QQuickTransitionManager()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktransitionmanager.html
    """
    #  QQuickTransitionManager::QQuickTransitionManager()
    self._noteCreation(QQuickTransitionManager, lambda: Rituals.call(
        'ritual_ZN23QQuickTransitionManagerC1Ev',
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

  @overload(QList[QQuickStateAction], QQuickTransition)
  @overload(QList[QQuickStateAction], NoneType)
  @overload(QList[QQuickStateAction], QQuickTransition, QObject)
  @overload(QList[QQuickStateAction], QQuickTransition, NoneType)
  @overload(QList[QQuickStateAction], NoneType, QObject)
  @overload(QList[QQuickStateAction], NoneType, NoneType)
  def transition(
      self,
      a0: QList[QQuickStateAction],
      transition: Optional[QQuickTransition],
      defaultTarget: Optional[QObject] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuickTransitionManager::transition(const
    QList<QQuickStateAction> &a0, QQuickTransition *transition, QObject
    *defaultTarget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktransitionmanager.html#transition

    Parameters
    ----------

    a0 : QList[QQuickStateAction]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    transition : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    defaultTarget : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickTransitionManager::transition(const
    #      QList<QQuickStateAction> &a0, QQuickTransition *transition,
    #      QObject *defaultTarget)
    self.uglySide.call(
        'ritual_ZN23QQuickTransitionManager10transitionERK5QListI17QQuickSt'
        'ateActionEP16QQuickTransitionP7QObject',
        self._valueOf(a0), self._addressOf(transition),
        self._addressOf(defaultTarget, 'QObject'),
    )

  def cancel(self) -> None:
    """
    Calls Qt's 'void QQuickTransitionManager::cancel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktransitionmanager.html#cancel
    """
    #  void QQuickTransitionManager::cancel()
    self.uglySide.call('ritual_ZN23QQuickTransitionManager6cancelEv')

  def finished(self) -> None:
    """
    Calls Qt's 'void QQuickTransitionManager::finished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktransitionmanager.html#finished
    """
    #  void QQuickTransitionManager::finished()
    ritual = 'ritual_ZN23QQuickTransitionManager8finishedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuickTransitionManager8finishedEv'
    self.uglySide.call(ritual)

  def complete(self) -> None:
    """
    Calls Qt's 'void QQuickTransitionManager::complete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktransitionmanager.html#complete
    """
    #  void QQuickTransitionManager::complete()
    self.uglySide.call('ritual_ZN23QQuickTransitionManager8completeEv')
