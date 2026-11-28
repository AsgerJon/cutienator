"""
QDeclarativeGeoMapItemTransitionManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapitemtransitionmanager_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeGeoMapItemTransitionManager to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickTransitionManager

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeGeoMapItemTransitionManager(QQuickTransitionManager):
  """
  The cute side of Qt's QDeclarativeGeoMapItemTransitionManager: a plain
  Python object standing in front of one C++
  QDeclarativeGeoMapItemTransitionManager.

  It is built on the cute 'QQuickTransitionManager', as Qt's
  QDeclarativeGeoMapItemTransitionManager is built on Qt's
  QQuickTransitionManager, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeGeoMapItemTransitionManager that has a
  ritual and that Python can call so far, 7 names in all: 'transitionEnter',
  'transitionExit', 'prepareEnterTransition', 'prepareExitTransition',
  'finalizeEnterTransition', 'finalizeExitTransition', 'finished'. It can be
  made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QDeclarativeGeoMapItemTransitionManager is created at the first
    use, not by 'QDeclarativeGeoMapItemTransitionManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeGeoMapItemTransitionManager.
  """

  #  The enums Qt writes inside QDeclarativeGeoMapItemTransitionManager, each
  #  a class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class TransitionState(CuteNum):
    """
    The enum 'QDeclarativeGeoMapItemTransitionManager::TransitionState' of
    Qt, with the 3 names Qt gives in it.
    """

    NoTransition = Kee[int](0)
    EnterTransition = Kee[int](1)
    ExitTransition = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeGeoMapItemTransitionManager'

  #  A C++ QDeclarativeGeoMapItemTransitionManager Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeGeoMapItemTransitionManager'

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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, mapItem: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QDeclarativeGeoMapItemTransitionManager::
    QDeclarativeGeoMapItemTransitionManager(QObject *mapItem)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemtransitionmanager.html

    Parameters
    ----------

    mapItem : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDeclarativeGeoMapItemTransitionManager::
    #      QDeclarativeGeoMapItemTransitionManager(QObject *mapItem)
    self._noteCreation(
        QDeclarativeGeoMapItemTransitionManager, lambda: Rituals.call(
            'ritual_ZN39QDeclarativeGeoMapItemTransitionManagerC1EP7QObject',
            self._addressOf(mapItem, 'QObject'),
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

  def transitionEnter(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapItemTransitionManager::transitionEnter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemtransitionmanager.html
    """
    #  void QDeclarativeGeoMapItemTransitionManager::transitionEnter()
    self.uglySide.call(
        'ritual_ZN39QDeclarativeGeoMapItemTransitionManager15transitionEnte'
        'rEv',
    )

  def transitionExit(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapItemTransitionManager::transitionExit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemtransitionmanager.html
    """
    #  void QDeclarativeGeoMapItemTransitionManager::transitionExit()
    self.uglySide.call(
        'ritual_ZN39QDeclarativeGeoMapItemTransitionManager14transitionExit'
        'Ev',
    )

  def prepareEnterTransition(self) -> bool:
    """
    Calls Qt's 'bool
    QDeclarativeGeoMapItemTransitionManager::prepareEnterTransition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemtransitionmanager.html
    """
    #  bool QDeclarativeGeoMapItemTransitionManager::prepareEnterTransition()
    return self.uglySide.call(
        'ritual_ZN39QDeclarativeGeoMapItemTransitionManager22prepareEnterTr'
        'ansitionEv',
    )

  def prepareExitTransition(self) -> bool:
    """
    Calls Qt's 'bool
    QDeclarativeGeoMapItemTransitionManager::prepareExitTransition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemtransitionmanager.html
    """
    #  bool QDeclarativeGeoMapItemTransitionManager::prepareExitTransition()
    return self.uglySide.call(
        'ritual_ZN39QDeclarativeGeoMapItemTransitionManager21prepareExitTra'
        'nsitionEv',
    )

  def finalizeEnterTransition(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapItemTransitionManager::finalizeEnterTransition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemtransitionmanager.html
    """
    #  void
    #      QDeclarativeGeoMapItemTransitionManager::finalizeEnterTransition()
    self.uglySide.call(
        'ritual_ZN39QDeclarativeGeoMapItemTransitionManager23finalizeEnterT'
        'ransitionEv',
    )

  def finalizeExitTransition(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapItemTransitionManager::finalizeExitTransition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemtransitionmanager.html
    """
    #  void QDeclarativeGeoMapItemTransitionManager::finalizeExitTransition()
    self.uglySide.call(
        'ritual_ZN39QDeclarativeGeoMapItemTransitionManager22finalizeExitTr'
        'ansitionEv',
    )

  def finished(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemTransitionManager::finished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemtransitionmanager.html
    """
    #  void QDeclarativeGeoMapItemTransitionManager::finished()
    ritual = 'ritual_ZN39QDeclarativeGeoMapItemTransitionManager8finishedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN39QDeclarativeGeoMapItemTransitionManager8finishedE'
          'v')
    self.uglySide.call(ritual)
