"""
Qt3DLogic::Logic::CallbackJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DLogic/6.12.0/Qt3DLogic/private/callbackjob_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DLogic::Logic::CallbackJob to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
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


class CallbackJob(Qt3DCore.QAspectJob):
  """
  The cute side of Qt's Qt3DLogic::Logic::CallbackJob: a plain Python object
  standing in front of one C++ Qt3DLogic::Logic::CallbackJob.

  It is built on the cute 'Qt3DCore::QAspectJob', as Qt's
  Qt3DLogic::Logic::CallbackJob is built on Qt's Qt3DCore::QAspectJob, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DLogic::Logic::CallbackJob that has a ritual and
  that Python can call so far, 4 names in all: 'setManager', 'run',
  'isRequired', 'postFrame'. It can be made from Python, in 1 way; see
  '__init__'.

  What to expect
  --------------

  - The C++ Qt3DLogic::Logic::CallbackJob is created at the first use, not by
    'Qt3DLogic::Logic::CallbackJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DLogic::Logic::CallbackJob.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DLogic::Logic::CallbackJob'

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

  @overload(WAIT['Qt3DLogic.Logic.Manager'])
  @overload(NoneType)
  def setManager(self, manager: Optional[Qt3DLogic.Logic.Manager]) -> None:
    """
    Calls Qt's 'void Qt3DLogic::Logic::CallbackJob::setManager(Manager
    *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-logic-callbackjob.html#setManager

    Parameters
    ----------

    manager : Optional[Qt3DLogic.Logic.Manager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DLogic::Logic::CallbackJob::setManager(Manager *manager)
    self.uglySide.call(
        'ritual_ZN9Qt3DLogic5Logic11CallbackJob10setManagerEPNS0_7ManagerE',
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
    Notes what was given, for Qt's
    'Qt3DLogic::Logic::CallbackJob::CallbackJob()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-logic-callbackjob.html#CallbackJob
    """
    #  Qt3DLogic::Logic::CallbackJob::CallbackJob()
    self._noteCreation(CallbackJob, lambda: Rituals.call(
        'ritual_ZN9Qt3DLogic5Logic11CallbackJobC1Ev',
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

  def run(self) -> None:
    """
    Calls Qt's 'void Qt3DLogic::Logic::CallbackJob::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-logic-callbackjob.html#run
    """
    #  void Qt3DLogic::Logic::CallbackJob::run()
    ritual = 'ritual_ZN9Qt3DLogic5Logic11CallbackJob3runEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9Qt3DLogic5Logic11CallbackJob3runEv'
    self.uglySide.call(ritual)

  def isRequired(self) -> bool:
    """
    Calls Qt's 'bool Qt3DLogic::Logic::CallbackJob::isRequired()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-logic-callbackjob.html#isRequired
    """
    #  bool Qt3DLogic::Logic::CallbackJob::isRequired()
    ritual = 'ritual_ZN9Qt3DLogic5Logic11CallbackJob10isRequiredEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9Qt3DLogic5Logic11CallbackJob10isRequiredEv'
    return self.uglySide.call(ritual)

  @overload(WAIT['Qt3DCore.QAspectEngine'])
  @overload(NoneType)
  def postFrame(
      self,
      aspectEngine: Optional[Qt3DCore.QAspectEngine],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DLogic::Logic::CallbackJob::postFrame(Qt3DCore::QAspectEngine
    *aspectEngine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dlogic-logic-callbackjob.html#postFrame

    Parameters
    ----------

    aspectEngine : Optional[Qt3DCore.QAspectEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DLogic::Logic::CallbackJob::postFrame(Qt3DCore::QAspectEngine
    #      *aspectEngine)
    ritual = (
        'ritual_ZN9Qt3DLogic5Logic11CallbackJob9postFrameEPN8Qt3DCore13QAsp'
        'ectEngineE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9Qt3DLogic5Logic11CallbackJob9postFrameEPN8Qt3DCore'
          '13QAspectEngineE')
    self.uglySide.call(ritual, self._addressOf(aspectEngine))
