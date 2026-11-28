"""
QVulkanInstance binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qvulkaninstance.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QVersionNumber
  from . import QPlatformVulkanInstance, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QVersionNumber = WAIT['QVersionNumber']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVulkanInstance(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QVulkanInstance: a plain Python object standing in
  front of one C++ QVulkanInstance.

  What exists
  -----------

  Every function of Qt's QVulkanInstance that has a ritual and that Python
  can call so far, 16 names in all: 'supportedApiVersion', 'setFlags',
  'setLayers', 'setExtensions', 'setApiVersion', 'create', 'destroy',
  'isValid', 'flags', 'layers', 'extensions', 'apiVersion', 'handle',
  'presentAboutToBeQueued', 'presentQueued', 'clearDebugOutputFilters'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVulkanInstance::~QVulkanInstance()': the destructor: Python never
    removes a C++ QVulkanInstance.
  - Qt's 'QVulkanInfoVector<QVulkanLayer>
    QVulkanInstance::supportedLayers()': gives a type Python has no way to
    take yet.
  - Qt's 'QVulkanInfoVector<QVulkanLayer> QVulkanInstance::supportedLayers()
    const': gives a type Python has no way to take yet.
  - Qt's 'QVulkanInfoVector<QVulkanExtension>
    QVulkanInstance::supportedExtensions()': gives a type Python has no way
    to take yet.
  - Qt's 'QVulkanInfoVector<QVulkanExtension>
    QVulkanInstance::supportedExtensions() const': gives a type Python has no
    way to take yet.
  - Qt's 'void QVulkanInstance::setVkInstance(VkInstance
    existingVkInstance)': names 'struct VkInstance_T', which has no cute
    class yet.
  - Qt's 'VkResult QVulkanInstance::errorCode() const': gives a type Python
    has no way to take yet.
  - Qt's 'VkInstance QVulkanInstance::vkInstance() const': gives a type
    Python has no way to take yet.
  - Qt's 'PFN_vkVoidFunction QVulkanInstance::getInstanceProcAddr(const char
    *name)': gives a type Python has no way to take yet.
  - Qt's 'QVulkanFunctions *QVulkanInstance::functions() const': gives
    'QVulkanFunctions', which has no cute class yet.
  - Qt's 'QVulkanDeviceFunctions *QVulkanInstance::deviceFunctions(VkDevice
    device)': names 'struct VkDevice_T', which has no cute class yet.
  - Qt's 'void QVulkanInstance::resetDeviceFunctions(VkDevice device)': names
    'struct VkDevice_T', which has no cute class yet.
  - Qt's 'VkSurfaceKHR QVulkanInstance::surfaceForWindow(QWindow *window)':
    gives a type Python has no way to take yet.
  - Qt's 'bool QVulkanInstance::supportsPresent(VkPhysicalDevice
    physicalDevice, uint32_t queueFamilyIndex, QWindow *window)': names
    'struct VkPhysicalDevice_T', which has no cute class yet.
  - Qt's 'void QVulkanInstance::installDebugOutputFilter(DebugFilter
    filter)': takes a type Python has no way to hand over yet.
  - Qt's 'void QVulkanInstance::removeDebugOutputFilter(DebugFilter filter)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QVulkanInstance::installDebugOutputFilter(DebugUtilsFilter
    filter)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 36 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QVulkanInstance is created at the first use, not by
    'QVulkanInstance(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVulkanInstance.
  - Each name of Qt's QVulkanInstance that has no cute function yet,
    'deviceFunctions', 'errorCode', 'functions', 'getInstanceProcAddr',
    'installDebugOutputFilter', 'removeDebugOutputFilter',
    'resetDeviceFunctions', 'setVkInstance', 'supportedExtensions',
    'supportedLayers', 'supportsPresent', 'surfaceForWindow', 'vkInstance',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QVulkanInstance, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DebugMessageSeverityFlag(CuteFlags):
    """
    The flags enum 'QVulkanInstance::DebugMessageSeverityFlag' of Qt, with
    the 4 names Qt gives in it. Qt names the type of its combinations
    'QVulkanInstance::DebugMessageSeverityFlags'.
    """

    VerboseSeverity = 0x1
    InfoSeverity = 0x2
    WarningSeverity = 0x4
    ErrorSeverity = 0x8

  DebugMessageSeverityFlags = DebugMessageSeverityFlag

  class DebugMessageTypeFlag(CuteFlags):
    """
    The flags enum 'QVulkanInstance::DebugMessageTypeFlag' of Qt, with the 3
    names Qt gives in it. Qt names the type of its combinations
    'QVulkanInstance::DebugMessageTypeFlags'.
    """

    GeneralMessage = 0x1
    ValidationMessage = 0x2
    PerformanceMessage = 0x4

  DebugMessageTypeFlags = DebugMessageTypeFlag

  class Flag(CuteFlags):
    """
    The flags enum 'QVulkanInstance::Flag' of Qt, with the 2 names Qt gives
    in it. Qt names the type of its combinations 'QVulkanInstance::Flags'.
    """

    NoDebugOutputRedirect = 0x1
    NoPortabilityDrivers = 0x2

  Flags = Flag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVulkanInstance'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def supportedApiVersion(self) -> QVersionNumber:
    """
    Calls Qt's 'QVersionNumber QVulkanInstance::supportedApiVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkaninstance.html#supportedApiVersion

    Returns
    -------

    QVersionNumber
      A new cute QVersionNumber around the copy Qt gave back. Python owns it.
    """
    #  QVersionNumber QVulkanInstance::supportedApiVersion() const
    address = self.uglySide.call(
        'ritual_ZNK15QVulkanInstance19supportedApiVersionEv',
    )
    from ..QtCore import QVersionNumber
    return QVersionNumber._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QVulkanInstance::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkaninstance.html#isValid
    """
    #  bool QVulkanInstance::isValid() const
    return self.uglySide.call('ritual_ZNK15QVulkanInstance7isValidEv')

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QVulkanInstance::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkaninstance.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QVulkanInstance::flags() const
    return QVulkanInstance.Flags(self.uglySide.call(
        'ritual_ZNK15QVulkanInstance5flagsEv',
    ))

  def layers(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QByteArrayList QVulkanInstance::layers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkaninstance.html#layers

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayList QVulkanInstance::layers() const
    address = self.uglySide.call('ritual_ZNK15QVulkanInstance6layersEv')
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  def extensions(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QByteArrayList QVulkanInstance::extensions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkaninstance.html#extensions

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayList QVulkanInstance::extensions() const
    address = self.uglySide.call('ritual_ZNK15QVulkanInstance10extensionsEv')
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  def apiVersion(self) -> QVersionNumber:
    """
    Calls Qt's 'QVersionNumber QVulkanInstance::apiVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkaninstance.html#apiVersion

    Returns
    -------

    QVersionNumber
      A new cute QVersionNumber around the copy Qt gave back. Python owns it.
    """
    #  QVersionNumber QVulkanInstance::apiVersion() const
    address = self.uglySide.call('ritual_ZNK15QVulkanInstance10apiVersionEv')
    from ..QtCore import QVersionNumber
    return QVersionNumber._cuteOwning(address)

  def handle(self) -> Optional[QPlatformVulkanInstance]:
    """
    Calls Qt's 'QPlatformVulkanInstance *QVulkanInstance::handle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkaninstance.html#handle

    Returns
    -------

    Optional[QPlatformVulkanInstance]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformVulkanInstance *QVulkanInstance::handle() const
    address = self.uglySide.call('ritual_ZNK15QVulkanInstance6handleEv')
    from . import QPlatformVulkanInstance
    return QPlatformVulkanInstance._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Flags)
  def setFlags(self, flags: Flags) -> None:
    """
    Calls Qt's 'void QVulkanInstance::setFlags(Flags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkaninstance.html#setFlags

    Parameters
    ----------

    flags : Flags
      Passed on as its number.
    """
    #  void QVulkanInstance::setFlags(Flags flags)
    self.uglySide.call(
        'ritual_ZN15QVulkanInstance8setFlagsE6QFlagsINS_4FlagEE',
        flags.value,
    )

  @overload(QList[QByteArray])
  def setLayers(self, layers: QList[QByteArray]) -> None:
    """
    Calls Qt's 'void QVulkanInstance::setLayers(const QByteArrayList
    &layers)'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkaninstance.html#setLayers

    Parameters
    ----------

    layers : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QVulkanInstance::setLayers(const QByteArrayList &layers)
    self.uglySide.call(
        'ritual_ZN15QVulkanInstance9setLayersERK5QListI10QByteArrayE',
        self._valueOf(layers),
    )

  @overload(QList[QByteArray])
  def setExtensions(self, extensions: QList[QByteArray]) -> None:
    """
    Calls Qt's 'void QVulkanInstance::setExtensions(const QByteArrayList
    &extensions)'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkaninstance.html#setExtensions

    Parameters
    ----------

    extensions : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QVulkanInstance::setExtensions(const QByteArrayList &extensions)
    self.uglySide.call(
        'ritual_ZN15QVulkanInstance13setExtensionsERK5QListI10QByteArrayE',
        self._valueOf(extensions),
    )

  @overload(QVersionNumber)
  def setApiVersion(self, vulkanVersion: QVersionNumber) -> None:
    """
    Calls Qt's 'void QVulkanInstance::setApiVersion(const QVersionNumber
    &vulkanVersion)'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkaninstance.html#setApiVersion

    Parameters
    ----------

    vulkanVersion : QVersionNumber
      Passed on as a value: Qt reads the C++ QVersionNumber, which stays
      Python's own.
    """
    #  void QVulkanInstance::setApiVersion(const QVersionNumber
    #      &vulkanVersion)
    self.uglySide.call(
        'ritual_ZN15QVulkanInstance13setApiVersionERK14QVersionNumber',
        self._valueOf(vulkanVersion),
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
    Notes what was given, for Qt's 'QVulkanInstance::QVulkanInstance()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkaninstance.html#QVulkanInstance
    """
    #  QVulkanInstance::QVulkanInstance()
    self._noteCreation(QVulkanInstance, lambda: Rituals.call(
        'ritual_ZN15QVulkanInstanceC1Ev',
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

  def create(self) -> bool:
    """
    Calls Qt's 'bool QVulkanInstance::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkaninstance.html#create
    """
    #  bool QVulkanInstance::create()
    return self.uglySide.call('ritual_ZN15QVulkanInstance6createEv')

  def destroy(self) -> None:
    """
    Calls Qt's 'void QVulkanInstance::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkaninstance.html#destroy
    """
    #  void QVulkanInstance::destroy()
    self.uglySide.call('ritual_ZN15QVulkanInstance7destroyEv')

  @overload(QWindow)
  @overload(NoneType)
  def presentAboutToBeQueued(self, window: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QVulkanInstance::presentAboutToBeQueued(QWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkaninstance.html#presentAboutToBeQueued

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVulkanInstance::presentAboutToBeQueued(QWindow *window)
    self.uglySide.call(
        'ritual_ZN15QVulkanInstance22presentAboutToBeQueuedEP7QWindow',
        self._addressOf(window),
    )

  @overload(QWindow)
  @overload(NoneType)
  def presentQueued(self, window: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QVulkanInstance::presentQueued(QWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qvulkaninstance.html#presentQueued

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVulkanInstance::presentQueued(QWindow *window)
    self.uglySide.call(
        'ritual_ZN15QVulkanInstance13presentQueuedEP7QWindow',
        self._addressOf(window),
    )

  def clearDebugOutputFilters(self) -> None:
    """
    Calls Qt's 'void QVulkanInstance::clearDebugOutputFilters()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkaninstance.html#clearDebugOutputFilters
    """
    #  void QVulkanInstance::clearDebugOutputFilters()
    self.uglySide.call(
        'ritual_ZN15QVulkanInstance23clearDebugOutputFiltersEv',
    )

  @staticmethod
  def deviceFunctions(*__, **_) -> Never:
    """
    Qt's 'QVulkanDeviceFunctions *QVulkanInstance::deviceFunctions(VkDevice
    device)': names 'struct VkDevice_T', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QVulkanInstance.deviceFunctions' has no cute function yet. Qt's "
        "'QVulkanDeviceFunctions *QVulkanInstance::deviceFunctions(VkDevice "
        "device)': names 'struct VkDevice_T', which has no cute class yet.")

  @staticmethod
  def errorCode(*__, **_) -> Never:
    """
    Qt's 'VkResult QVulkanInstance::errorCode() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanInstance.errorCode' has no cute function yet. Qt's "
        "'VkResult QVulkanInstance::errorCode() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def functions(*__, **_) -> Never:
    """
    Qt's 'QVulkanFunctions *QVulkanInstance::functions() const': gives
    'QVulkanFunctions', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QVulkanInstance.functions' has no cute function yet. Qt's "
        "'QVulkanFunctions *QVulkanInstance::functions() const': gives "
        "'QVulkanFunctions', which has no cute class yet.")

  @staticmethod
  def getInstanceProcAddr(*__, **_) -> Never:
    """
    Qt's 'PFN_vkVoidFunction QVulkanInstance::getInstanceProcAddr(const char
    *name)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanInstance.getInstanceProcAddr' has no cute function yet. "
        "Qt's 'PFN_vkVoidFunction "
        "QVulkanInstance::getInstanceProcAddr(const char *name)': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def installDebugOutputFilter(*__, **_) -> Never:
    """
    - Qt's 'void QVulkanInstance::installDebugOutputFilter(DebugFilter
      filter)': takes a type Python has no way to hand over yet.
    - Qt's 'void QVulkanInstance::installDebugOutputFilter(DebugUtilsFilter
      filter)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QVulkanInstance.installDebugOutputFilter' has no cute function "
        "yet. Qt's 'void "
        "QVulkanInstance::installDebugOutputFilter(DebugFilter filter)': "
        "takes a type Python has no way to hand over yet. Qt's 'void "
        "QVulkanInstance::installDebugOutputFilter(DebugUtilsFilter "
        "filter)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def removeDebugOutputFilter(*__, **_) -> Never:
    """
    Qt's 'void QVulkanInstance::removeDebugOutputFilter(DebugFilter filter)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QVulkanInstance.removeDebugOutputFilter' has no cute function "
        "yet. Qt's 'void "
        "QVulkanInstance::removeDebugOutputFilter(DebugFilter filter)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def resetDeviceFunctions(*__, **_) -> Never:
    """
    Qt's 'void QVulkanInstance::resetDeviceFunctions(VkDevice device)': names
    'struct VkDevice_T', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QVulkanInstance.resetDeviceFunctions' has no cute function yet. "
        "Qt's 'void QVulkanInstance::resetDeviceFunctions(VkDevice "
        "device)': names 'struct VkDevice_T', which has no cute class yet.")

  @staticmethod
  def setVkInstance(*__, **_) -> Never:
    """
    Qt's 'void QVulkanInstance::setVkInstance(VkInstance
    existingVkInstance)': names 'struct VkInstance_T', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QVulkanInstance.setVkInstance' has no cute function yet. Qt's "
        "'void QVulkanInstance::setVkInstance(VkInstance "
        "existingVkInstance)': names 'struct VkInstance_T', which has no "
        "cute class yet.")

  @staticmethod
  def supportedExtensions(*__, **_) -> Never:
    """
    - Qt's 'QVulkanInfoVector<QVulkanExtension>
      QVulkanInstance::supportedExtensions()': gives a type Python has no way
      to take yet.
    - Qt's 'QVulkanInfoVector<QVulkanExtension>
      QVulkanInstance::supportedExtensions() const': gives a type Python has
      no way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanInstance.supportedExtensions' has no cute function yet. "
        "Qt's 'QVulkanInfoVector<QVulkanExtension> "
        "QVulkanInstance::supportedExtensions()': gives a type Python has "
        "no way to take yet. Qt's 'QVulkanInfoVector<QVulkanExtension> "
        "QVulkanInstance::supportedExtensions() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def supportedLayers(*__, **_) -> Never:
    """
    - Qt's 'QVulkanInfoVector<QVulkanLayer>
      QVulkanInstance::supportedLayers()': gives a type Python has no way to
      take yet.
    - Qt's 'QVulkanInfoVector<QVulkanLayer>
      QVulkanInstance::supportedLayers() const': gives a type Python has no
      way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanInstance.supportedLayers' has no cute function yet. Qt's "
        "'QVulkanInfoVector<QVulkanLayer> "
        "QVulkanInstance::supportedLayers()': gives a type Python has no "
        "way to take yet. Qt's 'QVulkanInfoVector<QVulkanLayer> "
        "QVulkanInstance::supportedLayers() const': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def supportsPresent(*__, **_) -> Never:
    """
    Qt's 'bool QVulkanInstance::supportsPresent(VkPhysicalDevice
    physicalDevice, uint32_t queueFamilyIndex, QWindow *window)': names
    'struct VkPhysicalDevice_T', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QVulkanInstance.supportsPresent' has no cute function yet. Qt's "
        "'bool QVulkanInstance::supportsPresent(VkPhysicalDevice "
        "physicalDevice, uint32_t queueFamilyIndex, QWindow *window)': "
        "names 'struct VkPhysicalDevice_T', which has no cute class yet.")

  @staticmethod
  def surfaceForWindow(*__, **_) -> Never:
    """
    Qt's 'VkSurfaceKHR QVulkanInstance::surfaceForWindow(QWindow *window)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanInstance.surfaceForWindow' has no cute function yet. Qt's "
        "'VkSurfaceKHR QVulkanInstance::surfaceForWindow(QWindow *window)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def vkInstance(*__, **_) -> Never:
    """
    Qt's 'VkInstance QVulkanInstance::vkInstance() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVulkanInstance.vkInstance' has no cute function yet. Qt's "
        "'VkInstance QVulkanInstance::vkInstance() const': gives a type "
        "Python has no way to take yet.")
