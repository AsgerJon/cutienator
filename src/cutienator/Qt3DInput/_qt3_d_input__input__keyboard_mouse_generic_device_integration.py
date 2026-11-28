"""
Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/keyboardmousegenericdeviceintegration_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration to be
#  private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class KeyboardMouseGenericDeviceIntegration(Qt3DInput.QInputDeviceIntegration):
  """
  The cute side of Qt's
  Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration: a plain Python
  object standing in front of one C++
  Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration.

  It is built on the cute 'Qt3DInput::QInputDeviceIntegration', as Qt's
  Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration is built on Qt's
  Qt3DInput::QInputDeviceIntegration, and has everything that class has.

  What exists
  -----------

  Every function of Qt's
  Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration that has a ritual
  and that Python can call so far, 4 names in all: 'metaObject',
  'createPhysicalDevice', 'physicalDevice', 'onInitialize'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::qt_metacast(
    const char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::qt_metacall(
    QMetaObject::Call a0, int a1, void **a2)': one of Qt's own inner
    workings.
  - Qt's 'Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::
    ~KeyboardMouseGenericDeviceIntegration()': the destructor: Python never
    removes a C++ Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration.
  - Qt's 'std::vector<Qt3DCore::QAspectJobPtr>
    Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::jobsToExecute(
    qint64 time)': gives a type Python has no way to take yet.
  - Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::physicalDevices(
    ) const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  5 of the 14 functions Qt declares: 3 leans on 'Qt3DInput; 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration is
    created at the first use, not by
    'Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration.
  - Qt tells when it has removed the C++
    Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration
    that has no cute function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration'

  #  A C++ Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration Python
  #  makes is of a C++ class of ours, in which Python can take functions
  #  over. This ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_Input_KeyboardMouseGenericDeviceIntegration'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-keyboardmousegenericdeviceintegration.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::
    #      metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input37KeyboardMouseGenericDeviceIntegration1'
        '0metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(WAIT['Qt3DCore.QNodeId'])
  def physicalDevice(
      self,
      id: Qt3DCore.QNodeId,
  ) -> Optional[Qt3DInput.QAbstractPhysicalDeviceBackendNode]:
    """
    Calls Qt's 'QAbstractPhysicalDeviceBackendNode
    *Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::physicalDevice(
    Qt3DCore::QNodeId id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-keyboardmousegenericdeviceintegration.html

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    Returns
    -------

    Optional[Qt3DInput.QAbstractPhysicalDeviceBackendNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractPhysicalDeviceBackendNode
    #      *Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::
    #      physicalDevice(Qt3DCore::QNodeId id) const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input37KeyboardMouseGenericDeviceIntegration1'
        '4physicalDeviceEN8Qt3DCore7QNodeIdE',
        self._valueOf(id),
    )
    return Qt3DInput.QAbstractPhysicalDeviceBackendNode._cuteAt(address)

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
    Qt's 'Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::
    KeyboardMouseGenericDeviceIntegration(InputHandler *handleer)': leans on
    'Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::qt_metacall(
    QMetaObject::Call, int, void**)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.KeyboardMouseGenericDeviceIntegration.__init__' "
        "has no cute function yet. Qt's "
        "'Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::KeyboardM"
        "ouseGenericDeviceIntegration(InputHandler *handleer)': leans on "
        "'Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::qt_metaca"
        "ll(QMetaObject::Call, int, void**)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  @overload(str)
  def createPhysicalDevice(
      self,
      name: str,
  ) -> Optional[Qt3DInput.QAbstractPhysicalDevice]:
    """
    Calls Qt's 'QAbstractPhysicalDevice
    *Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::
    createPhysicalDevice(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-keyboardmousegenericdeviceintegration.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[Qt3DInput.QAbstractPhysicalDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractPhysicalDevice
    #      *Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::
    #      createPhysicalDevice(const QString &name)
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input37KeyboardMouseGenericDeviceIntegration20'
        'createPhysicalDeviceERK7QString',
        name,
    )
    return Qt3DInput.QAbstractPhysicalDevice._cuteAt(address)

  def onInitialize(self) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::onInitialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-keyboardmousegenericdeviceintegration.html
    """
    #  void Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::
    #      onInitialize()
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input37KeyboardMouseGenericDeviceIntegration12'
        'onInitializeEv',
    )
