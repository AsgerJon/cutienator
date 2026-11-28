"""
Qt3DInput::Input::LoadProxyDeviceJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/loadproxydevicejob_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DInput::Input::LoadProxyDeviceJob to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class LoadProxyDeviceJob(Qt3DCore.QAspectJob):
  """
  The cute side of Qt's Qt3DInput::Input::LoadProxyDeviceJob: a plain Python
  object standing in front of one C++ Qt3DInput::Input::LoadProxyDeviceJob.

  It is built on the cute 'Qt3DCore::QAspectJob', as Qt's
  Qt3DInput::Input::LoadProxyDeviceJob is built on Qt's Qt3DCore::QAspectJob,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::Input::LoadProxyDeviceJob that has a
  ritual and that Python can call so far, 2 names in all: 'setInputHandler',
  'inputHandler'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DInput::Input::LoadProxyDeviceJob::~LoadProxyDeviceJob()': the
    destructor: Python never removes a C++
    Qt3DInput::Input::LoadProxyDeviceJob.
  - Qt's 'void Qt3DInput::Input::LoadProxyDeviceJob::setProxiesToLoad(const
    QList<Qt3DCore::QNodeId> &proxies)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DInput::Input::LoadProxyDeviceJob::proxies() const': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here; 1 Qt's library has no name for it, and its code in
  Qt's source does not compile apart from its file; 1 leans on 'Qt3DInput.

  What to expect
  --------------

  - The C++ Qt3DInput::Input::LoadProxyDeviceJob is created at the first use,
    not by 'Qt3DInput::Input::LoadProxyDeviceJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::Input::LoadProxyDeviceJob.
  - Each name of Qt's Qt3DInput::Input::LoadProxyDeviceJob that has no cute
    function yet, '__init__', 'proxies', 'setProxiesToLoad', holds a function
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
  __qt_class__ = 'Qt3DInput::Input::LoadProxyDeviceJob'

  #  A C++ Qt3DInput::Input::LoadProxyDeviceJob Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_Input_LoadProxyDeviceJob'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def inputHandler(self) -> Optional[Qt3DInput.Input.InputHandler]:
    """
    Calls Qt's 'InputHandler
    *Qt3DInput::Input::LoadProxyDeviceJob::inputHandler() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-loadproxydevicejob.html

    Returns
    -------

    Optional[Qt3DInput.Input.InputHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  InputHandler *Qt3DInput::Input::LoadProxyDeviceJob::inputHandler()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input18LoadProxyDeviceJob12inputHandlerEv',
    )
    return Qt3DInput.Input.InputHandler._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DInput.Input.InputHandler'])
  @overload(NoneType)
  def setInputHandler(
      self,
      handler: Optional[Qt3DInput.Input.InputHandler],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::Input::LoadProxyDeviceJob::setInputHandler(InputHandler
    *handler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-loadproxydevicejob.html

    Parameters
    ----------

    handler : Optional[Qt3DInput.Input.InputHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      Qt3DInput::Input::LoadProxyDeviceJob::setInputHandler(InputHandler
    #      *handler)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input18LoadProxyDeviceJob15setInputHandlerEPNS'
        '0_12InputHandlerE',
        self._addressOf(handler),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'Qt3DInput::Input::LoadProxyDeviceJob::LoadProxyDeviceJob()': leans
    on 'Qt3DInput::Input::InputHandler::createPhysicalDevice(QString
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.LoadProxyDeviceJob.__init__' has no cute function "
        "yet. Qt's "
        "'Qt3DInput::Input::LoadProxyDeviceJob::LoadProxyDeviceJob()': "
        "leans on "
        "'Qt3DInput::Input::InputHandler::createPhysicalDevice(QString "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  @staticmethod
  def proxies(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DInput::Input::LoadProxyDeviceJob::proxies() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.LoadProxyDeviceJob.proxies' has no cute function "
        "yet. Qt's 'QList<Qt3DCore::QNodeId> "
        "Qt3DInput::Input::LoadProxyDeviceJob::proxies() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def setProxiesToLoad(*__, **_) -> Never:
    """
    Qt's 'void Qt3DInput::Input::LoadProxyDeviceJob::setProxiesToLoad(const
    QList<Qt3DCore::QNodeId> &proxies)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.LoadProxyDeviceJob.setProxiesToLoad' has no cute "
        "function yet. Qt's 'void "
        "Qt3DInput::Input::LoadProxyDeviceJob::setProxiesToLoad(const "
        "QList<Qt3DCore::QNodeId> &proxies)': takes a type Python has no "
        "way to hand over yet.")
