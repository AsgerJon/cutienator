"""
Qt3DLogic::Logic::Manager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DLogic/6.12.0/Qt3DLogic/private/manager_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DLogic::Logic::Manager to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DLogic

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Manager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DLogic::Logic::Manager: a plain Python object
  standing in front of one C++ Qt3DLogic::Logic::Manager.

  What exists
  -----------

  Every function of Qt's Qt3DLogic::Logic::Manager that has a ritual and that
  Python can call so far, 8 names in all: 'setLogicAspect', 'setExecutor',
  'logicHandlerManager', 'appendHandler', 'removeHandler', 'hasFrameActions',
  'triggerLogicFrameUpdates', 'setDeltaTime'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DLogic::Logic::Manager::~Manager()': the destructor: Python
    never removes a C++ Qt3DLogic::Logic::Manager.

  What to expect
  --------------

  - The C++ Qt3DLogic::Logic::Manager is created at the first use, not by
    'Qt3DLogic::Logic::Manager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DLogic::Logic::Manager.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DLogic::Logic::Manager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def logicHandlerManager(self) -> Optional[Qt3DLogic.Logic.HandlerManager]:
    """
    Calls Qt's 'HandlerManager
    *Qt3DLogic::Logic::Manager::logicHandlerManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-logic-manager.html#logicHandlerManager

    Returns
    -------

    Optional[Qt3DLogic.Logic.HandlerManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  HandlerManager *Qt3DLogic::Logic::Manager::logicHandlerManager() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DLogic5Logic7Manager19logicHandlerManagerEv',
    )
    return Qt3DLogic.Logic.HandlerManager._cuteAt(address)

  def hasFrameActions(self) -> bool:
    """
    Calls Qt's 'bool Qt3DLogic::Logic::Manager::hasFrameActions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-logic-manager.html#hasFrameActions
    """
    #  bool Qt3DLogic::Logic::Manager::hasFrameActions() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DLogic5Logic7Manager15hasFrameActionsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DLogic.QLogicAspect'])
  @overload(NoneType)
  def setLogicAspect(
      self,
      logicAspect: Optional[Qt3DLogic.QLogicAspect],
  ) -> None:
    """
    Calls Qt's 'void Qt3DLogic::Logic::Manager::setLogicAspect(QLogicAspect
    *logicAspect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-logic-manager.html#setLogicAspect

    Parameters
    ----------

    logicAspect : Optional[Qt3DLogic.QLogicAspect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DLogic::Logic::Manager::setLogicAspect(QLogicAspect
    #      *logicAspect)
    self.uglySide.call(
        'ritual_ZN9Qt3DLogic5Logic7Manager14setLogicAspectEPNS_12QLogicAspe'
        'ctE',
        self._addressOf(logicAspect),
    )

  @overload(WAIT['Qt3DLogic.Logic.Executor'])
  @overload(NoneType)
  def setExecutor(
      self,
      executor: Optional[Qt3DLogic.Logic.Executor],
  ) -> None:
    """
    Calls Qt's 'void Qt3DLogic::Logic::Manager::setExecutor(Executor
    *executor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-logic-manager.html#setExecutor

    Parameters
    ----------

    executor : Optional[Qt3DLogic.Logic.Executor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DLogic::Logic::Manager::setExecutor(Executor *executor)
    self.uglySide.call(
        'ritual_ZN9Qt3DLogic5Logic7Manager11setExecutorEPNS0_8ExecutorE',
        self._addressOf(executor),
    )

  @overload(float)
  def setDeltaTime(self, dt: float) -> None:
    """
    Calls Qt's 'void Qt3DLogic::Logic::Manager::setDeltaTime(float dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-logic-manager.html#setDeltaTime

    Parameters
    ----------

    dt : float
      Passed on as it is.
    """
    #  void Qt3DLogic::Logic::Manager::setDeltaTime(float dt)
    self.uglySide.call(
        'ritual_ZN9Qt3DLogic5Logic7Manager12setDeltaTimeEf', dt,
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
    Notes what was given, for Qt's 'Qt3DLogic::Logic::Manager::Manager()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-logic-manager.html#Manager
    """
    #  Qt3DLogic::Logic::Manager::Manager()
    self._noteCreation(Manager, lambda: Rituals.call(
        'ritual_ZN9Qt3DLogic5Logic7ManagerC1Ev',
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

  @overload(WAIT['Qt3DLogic.Logic.Handler'])
  @overload(NoneType)
  def appendHandler(
      self,
      handler: Optional[Qt3DLogic.Logic.Handler],
  ) -> None:
    """
    Calls Qt's 'void Qt3DLogic::Logic::Manager::appendHandler(Handler
    *handler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-logic-manager.html#appendHandler

    Parameters
    ----------

    handler : Optional[Qt3DLogic.Logic.Handler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DLogic::Logic::Manager::appendHandler(Handler *handler)
    self.uglySide.call(
        'ritual_ZN9Qt3DLogic5Logic7Manager13appendHandlerEPNS0_7HandlerE',
        self._addressOf(handler),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def removeHandler(self, id: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DLogic::Logic::Manager::removeHandler(Qt3DCore::QNodeId id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-logic-manager.html#removeHandler

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DLogic::Logic::Manager::removeHandler(Qt3DCore::QNodeId id)
    self.uglySide.call(
        'ritual_ZN9Qt3DLogic5Logic7Manager13removeHandlerEN8Qt3DCore7QNodeI'
        'dE',
        self._valueOf(id),
    )

  def triggerLogicFrameUpdates(self) -> None:
    """
    Calls Qt's 'void Qt3DLogic::Logic::Manager::triggerLogicFrameUpdates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-logic-manager.html
    """
    #  void Qt3DLogic::Logic::Manager::triggerLogicFrameUpdates()
    self.uglySide.call(
        'ritual_ZN9Qt3DLogic5Logic7Manager24triggerLogicFrameUpdatesEv',
    )
