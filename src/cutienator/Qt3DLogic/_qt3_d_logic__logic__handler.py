"""
Qt3DLogic::Logic::Handler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DLogic/6.12.0/Qt3DLogic/private/handler_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DLogic::Logic::Handler to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DLogic

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Handler(Qt3DCore.QBackendNode):
  """
  The cute side of Qt's Qt3DLogic::Logic::Handler: a plain Python object
  standing in front of one C++ Qt3DLogic::Logic::Handler.

  It is built on the cute 'Qt3DCore::QBackendNode', as Qt's
  Qt3DLogic::Logic::Handler is built on Qt's Qt3DCore::QBackendNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DLogic::Logic::Handler that has a ritual and that
  Python can call so far, 3 names in all: 'setManager', 'logicManager',
  'syncFromFrontEnd'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ Qt3DLogic::Logic::Handler is created at the first use, not by
    'Qt3DLogic::Logic::Handler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DLogic::Logic::Handler.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DLogic::Logic::Handler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def logicManager(self) -> Optional[Qt3DLogic.Logic.Manager]:
    """
    Calls Qt's 'Manager *Qt3DLogic::Logic::Handler::logicManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-logic-handler.html#logicManager

    Returns
    -------

    Optional[Qt3DLogic.Logic.Manager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Manager *Qt3DLogic::Logic::Handler::logicManager() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DLogic5Logic7Handler12logicManagerEv',
    )
    return Qt3DLogic.Logic.Manager._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DLogic.Logic.Manager'])
  @overload(NoneType)
  def setManager(self, manager: Optional[Qt3DLogic.Logic.Manager]) -> None:
    """
    Calls Qt's 'void Qt3DLogic::Logic::Handler::setManager(Manager
    *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-logic-handler.html#setManager

    Parameters
    ----------

    manager : Optional[Qt3DLogic.Logic.Manager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DLogic::Logic::Handler::setManager(Manager *manager)
    self.uglySide.call(
        'ritual_ZN9Qt3DLogic5Logic7Handler10setManagerEPNS0_7ManagerE',
        self._addressOf(manager),
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
    Notes what was given, for Qt's 'Qt3DLogic::Logic::Handler::Handler()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-logic-handler.html#Handler
    """
    #  Qt3DLogic::Logic::Handler::Handler()
    self._noteCreation(Handler, lambda: Rituals.call(
        'ritual_ZN9Qt3DLogic5Logic7HandlerC1Ev',
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

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DLogic::Logic::Handler::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-logic-handler.html#syncFromFrontEnd

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DLogic::Logic::Handler::syncFromFrontEnd(const Qt3DCore::QNode
    #      *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN9Qt3DLogic5Logic7Handler16syncFromFrontEndEPKN8Qt3DCore5Q'
        'NodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9Qt3DLogic5Logic7Handler16syncFromFrontEndEPKN8Qt3D'
          'Core5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)
