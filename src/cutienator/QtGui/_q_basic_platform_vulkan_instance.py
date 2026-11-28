"""
QBasicPlatformVulkanInstance binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qbasicvulkanplatforminstance_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QBasicPlatformVulkanInstance to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QPlatformVulkanInstance

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QLibrary, QVersionNumber
  from . import QVulkanInstance
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QLibrary = WAIT['QLibrary']
  QVulkanInstance = WAIT['QVulkanInstance']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBasicPlatformVulkanInstance(QPlatformVulkanInstance):
  """
  The cute side of Qt's QBasicPlatformVulkanInstance: a plain Python object
  standing in front of one C++ QBasicPlatformVulkanInstance.

  It is built on the cute 'QPlatformVulkanInstance', as Qt's
  QBasicPlatformVulkanInstance is built on Qt's QPlatformVulkanInstance, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QBasicPlatformVulkanInstance that has a ritual and
  that Python can call so far, 8 names in all: 'supportedApiVersion',
  'isValid', 'enabledLayers', 'enabledExtensions', 'loadVulkanLibrary',
  'init', 'initInstance', 'setupDebugOutput'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBasicPlatformVulkanInstance::~QBasicPlatformVulkanInstance()': the
    destructor: Python never removes a C++ QBasicPlatformVulkanInstance.
  - Qt's 'QVulkanInfoVector<QVulkanLayer>
    QBasicPlatformVulkanInstance::supportedLayers() const': gives a type
    Python has no way to take yet.
  - Qt's 'QVulkanInfoVector<QVulkanExtension>
    QBasicPlatformVulkanInstance::supportedExtensions() const': gives a type
    Python has no way to take yet.
  - Qt's 'VkResult QBasicPlatformVulkanInstance::errorCode() const': gives a
    type Python has no way to take yet.
  - Qt's 'VkInstance QBasicPlatformVulkanInstance::vkInstance() const': gives
    a type Python has no way to take yet.
  - Qt's 'PFN_vkVoidFunction
    QBasicPlatformVulkanInstance::getInstanceProcAddr(const char *name)':
    gives a type Python has no way to take yet.
  - Qt's 'bool QBasicPlatformVulkanInstance::supportsPresent(VkPhysicalDevice
    physicalDevice, uint32_t queueFamilyIndex, QWindow *window)': names
    'struct VkPhysicalDevice_T', which has no cute class yet.
  - Qt's 'void QBasicPlatformVulkanInstance::setDebugFilters(const
    QList<QVulkanInstance::DebugFilter> &filters)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QBasicPlatformVulkanInstance::setDebugUtilsFilters(const
    QList<QVulkanInstance::DebugUtilsFilter> &filters)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void QBasicPlatformVulkanInstance::destroySurface(VkSurfaceKHR
    surface) const': names 'struct VkSurfaceKHR_T', which has no cute class
    yet.
  - Qt's 'QList<QVulkanInstance::DebugFilter>
    QBasicPlatformVulkanInstance::debugFilters() const': gives a type Python
    has no way to take yet.
  - Qt's 'QList<QVulkanInstance::DebugUtilsFilter>
    QBasicPlatformVulkanInstance::debugUtilsFilters() const': gives a type
    Python has no way to take yet.

  What to expect
  --------------

  - The C++ QBasicPlatformVulkanInstance is created at the first use, not by
    'QBasicPlatformVulkanInstance(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBasicPlatformVulkanInstance.
  - Each name of Qt's QBasicPlatformVulkanInstance that has no cute function
    yet, 'debugFilters', 'debugUtilsFilters', 'destroySurface', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBasicPlatformVulkanInstance'

  #  A C++ QBasicPlatformVulkanInstance Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBasicPlatformVulkanInstance'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def supportedApiVersion(self) -> QVersionNumber:
    """
    Calls Qt's 'QVersionNumber
    QBasicPlatformVulkanInstance::supportedApiVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicplatformvulkaninstance.html

    Returns
    -------

    QVersionNumber
      A new cute QVersionNumber around the copy Qt gave back. Python owns it.
    """
    #  QVersionNumber QBasicPlatformVulkanInstance::supportedApiVersion()
    #      const
    ritual = (
        'ritual_ZNK28QBasicPlatformVulkanInstance19supportedApiVersionEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK28QBasicPlatformVulkanInstance19supportedApiVersio'
          'nEv')
    address = self.uglySide.call(ritual)
    from ..QtCore import QVersionNumber
    return QVersionNumber._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QBasicPlatformVulkanInstance::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicplatformvulkaninstance.html#isValid
    """
    #  bool QBasicPlatformVulkanInstance::isValid() const
    ritual = 'ritual_ZNK28QBasicPlatformVulkanInstance7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK28QBasicPlatformVulkanInstance7isValidEv'
    return self.uglySide.call(ritual)

  def enabledLayers(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QByteArrayList QBasicPlatformVulkanInstance::enabledLayers()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicplatformvulkaninstance.html#enabledLayers

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayList QBasicPlatformVulkanInstance::enabledLayers() const
    address = self.uglySide.call(
        'ritual_ZNK28QBasicPlatformVulkanInstance13enabledLayersEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  def enabledExtensions(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QByteArrayList
    QBasicPlatformVulkanInstance::enabledExtensions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicplatformvulkaninstance.html

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayList QBasicPlatformVulkanInstance::enabledExtensions() const
    address = self.uglySide.call(
        'ritual_ZNK28QBasicPlatformVulkanInstance17enabledExtensionsEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

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
    'QBasicPlatformVulkanInstance::QBasicPlatformVulkanInstance()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicplatformvulkaninstance.html
    """
    #  QBasicPlatformVulkanInstance::QBasicPlatformVulkanInstance()
    self._noteCreation(QBasicPlatformVulkanInstance, lambda: Rituals.call(
        'ritual_ZN28QBasicPlatformVulkanInstanceC1Ev',
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

  @overload(str)
  @overload(str, int)
  def loadVulkanLibrary(
      self,
      defaultLibraryName: str,
      defaultLibraryVersion: int = -1,
  ) -> None:
    """
    Calls Qt's 'void QBasicPlatformVulkanInstance::loadVulkanLibrary(const
    QString &defaultLibraryName, int defaultLibraryVersion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicplatformvulkaninstance.html

    Parameters
    ----------

    defaultLibraryName : str
      Passed on as it is: a QString is made of it for the call.

    defaultLibraryVersion : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QBasicPlatformVulkanInstance::loadVulkanLibrary(const QString
    #      &defaultLibraryName, int defaultLibraryVersion)
    self.uglySide.call(
        'ritual_ZN28QBasicPlatformVulkanInstance17loadVulkanLibraryERK7QStr'
        'ingi',
        defaultLibraryName, defaultLibraryVersion,
    )

  @overload(QLibrary)
  @overload(NoneType)
  def init(self, lib: Optional[QLibrary]) -> None:
    """
    Calls Qt's 'void QBasicPlatformVulkanInstance::init(QLibrary *lib)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicplatformvulkaninstance.html#init

    Parameters
    ----------

    lib : Optional[QLibrary]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBasicPlatformVulkanInstance::init(QLibrary *lib)
    self.uglySide.call(
        'ritual_ZN28QBasicPlatformVulkanInstance4initEP8QLibrary',
        self._addressOf(lib),
    )

  @overload(QVulkanInstance, QList[QByteArray])
  @overload(NoneType, QList[QByteArray])
  def initInstance(
      self,
      instance: Optional[QVulkanInstance],
      extraExts: QList[QByteArray],
  ) -> None:
    """
    Calls Qt's 'void
    QBasicPlatformVulkanInstance::initInstance(QVulkanInstance *instance,
    const QByteArrayList &extraExts)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicplatformvulkaninstance.html#initInstance

    Parameters
    ----------

    instance : Optional[QVulkanInstance]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    extraExts : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBasicPlatformVulkanInstance::initInstance(QVulkanInstance
    #      *instance, const QByteArrayList &extraExts)
    self.uglySide.call(
        'ritual_ZN28QBasicPlatformVulkanInstance12initInstanceEP15QVulkanIn'
        'stanceRK5QListI10QByteArrayE',
        self._addressOf(instance), self._valueOf(extraExts),
    )

  def setupDebugOutput(self) -> None:
    """
    Calls Qt's 'void QBasicPlatformVulkanInstance::setupDebugOutput()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicplatformvulkaninstance.html#setupDebugOutput
    """
    #  void QBasicPlatformVulkanInstance::setupDebugOutput()
    self.uglySide.call(
        'ritual_ZN28QBasicPlatformVulkanInstance16setupDebugOutputEv',
    )

  @staticmethod
  def debugFilters(*__, **_) -> Never:
    """
    Qt's 'QList<QVulkanInstance::DebugFilter>
    QBasicPlatformVulkanInstance::debugFilters() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QBasicPlatformVulkanInstance.debugFilters' has no cute function "
        "yet. Qt's 'QList<QVulkanInstance::DebugFilter> "
        "QBasicPlatformVulkanInstance::debugFilters() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def debugUtilsFilters(*__, **_) -> Never:
    """
    Qt's 'QList<QVulkanInstance::DebugUtilsFilter>
    QBasicPlatformVulkanInstance::debugUtilsFilters() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QBasicPlatformVulkanInstance.debugUtilsFilters' has no cute "
        "function yet. Qt's 'QList<QVulkanInstance::DebugUtilsFilter> "
        "QBasicPlatformVulkanInstance::debugUtilsFilters() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def destroySurface(*__, **_) -> Never:
    """
    Qt's 'void QBasicPlatformVulkanInstance::destroySurface(VkSurfaceKHR
    surface) const': names 'struct VkSurfaceKHR_T', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QBasicPlatformVulkanInstance.destroySurface' has no cute function "
        "yet. Qt's 'void "
        "QBasicPlatformVulkanInstance::destroySurface(VkSurfaceKHR surface) "
        "const': names 'struct VkSurfaceKHR_T', which has no cute class yet."
    )
