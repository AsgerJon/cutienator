"""
Qt3DInput::Input::UpdateAxisActionJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/updateaxisactionjob_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DInput::Input::UpdateAxisActionJob to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..Qt3DCore import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class UpdateAxisActionJob(Qt3DCore.QAspectJob):
  """
  The cute side of Qt's Qt3DInput::Input::UpdateAxisActionJob: a plain Python
  object standing in front of one C++ Qt3DInput::Input::UpdateAxisActionJob.

  It is built on the cute 'Qt3DCore::QAspectJob', as Qt's
  Qt3DInput::Input::UpdateAxisActionJob is built on Qt's
  Qt3DCore::QAspectJob, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::Input::UpdateAxisActionJob that has a
  ritual and that Python can call so far, 3 names in all: 'run',
  'processActionInput', 'processAxisInput'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DInput::Input::UpdateAxisActionJob::UpdateAxisActionJob(qint64
    currentTime, InputHandler *handler, HLogicalDevice handle)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 8 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here; 2 Qt's library has no name for it, and its code in
  Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ Qt3DInput::Input::UpdateAxisActionJob is created at the first
    use, not by 'Qt3DInput::Input::UpdateAxisActionJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::Input::UpdateAxisActionJob.
  - Each name of Qt's Qt3DInput::Input::UpdateAxisActionJob that has no cute
    function yet, '__init__', 'updateAction', 'updateAxis', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::Input::UpdateAxisActionJob'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'Qt3DInput::Input::UpdateAxisActionJob::UpdateAxisActionJob(qint64
    currentTime, InputHandler *handler, HLogicalDevice handle)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.UpdateAxisActionJob.__init__' has no cute "
        "function yet. Qt's "
        "'Qt3DInput::Input::UpdateAxisActionJob::UpdateAxisActionJob(qint64 "
        "currentTime, InputHandler *handler, HLogicalDevice handle)': takes "
        "a type Python has no way to hand over yet.")

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
    Calls Qt's 'void Qt3DInput::Input::UpdateAxisActionJob::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-updateaxisactionjob.html#run
    """
    #  void Qt3DInput::Input::UpdateAxisActionJob::run()
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input19UpdateAxisActionJob3runEv',
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def processActionInput(self, actionInputId: Qt3DCore.QNodeId) -> bool:
    """
    Calls Qt's 'bool
    Qt3DInput::Input::UpdateAxisActionJob::processActionInput(const
    Qt3DCore::QNodeId actionInputId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-updateaxisactionjob.html

    Parameters
    ----------

    actionInputId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  bool Qt3DInput::Input::UpdateAxisActionJob::processActionInput(const
    #      Qt3DCore::QNodeId actionInputId)
    return self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input19UpdateAxisActionJob18processActionInput'
        'EN8Qt3DCore7QNodeIdE',
        self._valueOf(actionInputId),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def processAxisInput(self, axisInputId: Qt3DCore.QNodeId) -> float:
    """
    Calls Qt's 'float
    Qt3DInput::Input::UpdateAxisActionJob::processAxisInput(const
    Qt3DCore::QNodeId axisInputId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-updateaxisactionjob.html

    Parameters
    ----------

    axisInputId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  float Qt3DInput::Input::UpdateAxisActionJob::processAxisInput(const
    #      Qt3DCore::QNodeId axisInputId)
    return self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input19UpdateAxisActionJob16processAxisInputEN'
        '8Qt3DCore7QNodeIdE',
        self._valueOf(axisInputId),
    )

  @staticmethod
  def updateAction(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DInput::Input::UpdateAxisActionJob::updateAction(LogicalDevice
    *device)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: member access into incomplete type
    'UpdateAxisActionJobPrivate'.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.UpdateAxisActionJob.updateAction' has no cute "
        "function yet. Qt's 'void "
        "Qt3DInput::Input::UpdateAxisActionJob::updateAction(LogicalDevice "
        "*device)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'UpdateAxisActionJobPrivate'.")

  @staticmethod
  def updateAxis(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DInput::Input::UpdateAxisActionJob::updateAxis(LogicalDevice
    *device)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: member access into incomplete type
    'UpdateAxisActionJobPrivate'.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.UpdateAxisActionJob.updateAxis' has no cute "
        "function yet. Qt's 'void "
        "Qt3DInput::Input::UpdateAxisActionJob::updateAxis(LogicalDevice "
        "*device)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'UpdateAxisActionJobPrivate'.")
