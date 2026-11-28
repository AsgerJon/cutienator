"""
QPlatformVulkanInstance binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformvulkaninstance.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QVersionNumber
  from . import QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformVulkanInstance(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformVulkanInstance: a plain Python object
  standing in front of one C++ QPlatformVulkanInstance.

  What exists
  -----------

  Every function of Qt's QPlatformVulkanInstance that has a ritual and that
  Python can call so far, 9 names in all: 'supportedApiVersion',
  'createOrAdoptInstance', 'isValid', 'enabledLayers', 'enabledExtensions',
  'presentAboutToBeQueued', 'presentQueued', 'beginFrame', 'endFrame'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformVulkanInstancePrivate *QPlatformVulkanInstance::d_func()':
    gives 'QPlatformVulkanInstancePrivate', which has no cute class yet.
  - Qt's 'const QPlatformVulkanInstancePrivate
    *QPlatformVulkanInstance::d_func() const': gives
    'QPlatformVulkanInstancePrivate', which has no cute class yet.
  - Qt's 'QPlatformVulkanInstance::~QPlatformVulkanInstance()': the
    destructor: Python never removes a C++ QPlatformVulkanInstance.
  - Qt's 'QVulkanInfoVector<QVulkanLayer>
    QPlatformVulkanInstance::supportedLayers() const': gives a type Python
    has no way to take yet.
  - Qt's 'QVulkanInfoVector<QVulkanExtension>
    QPlatformVulkanInstance::supportedExtensions() const': gives a type
    Python has no way to take yet.
  - Qt's 'VkResult QPlatformVulkanInstance::errorCode() const': gives a type
    Python has no way to take yet.
  - Qt's 'VkInstance QPlatformVulkanInstance::vkInstance() const': gives a
    type Python has no way to take yet.
  - Qt's 'PFN_vkVoidFunction
    QPlatformVulkanInstance::getInstanceProcAddr(const char *name)': gives a
    type Python has no way to take yet.
  - Qt's 'bool QPlatformVulkanInstance::supportsPresent(VkPhysicalDevice
    physicalDevice, uint32_t queueFamilyIndex, QWindow *window)': names
    'struct VkPhysicalDevice_T', which has no cute class yet.
  - Qt's 'void QPlatformVulkanInstance::setDebugFilters(const
    QList<QVulkanInstance::DebugFilter> &filters)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QPlatformVulkanInstance::setDebugUtilsFilters(const
    QList<QVulkanInstance::DebugUtilsFilter> &filters)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 23 functions Qt declares: 2 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QPlatformVulkanInstance is created at the first use, not by
    'QPlatformVulkanInstance(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformVulkanInstance.
  - Each name of Qt's QPlatformVulkanInstance that has no cute function yet,
    '__init__', 'd_func', 'errorCode', 'getInstanceProcAddr',
    'setDebugFilters', 'setDebugUtilsFilters', 'supportedExtensions',
    'supportedLayers', 'supportsPresent', 'vkInstance', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformVulkanInstance'

  #  A C++ QPlatformVulkanInstance Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformVulkanInstance'

  #  The functions Qt calls itself that QPlatformVulkanInstance is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'supportedLayers': (
          'QVulkanInfoVector<QVulkanLayer> '
          'QPlatformVulkanInstance::supportedLayers() const',
      ),
      'supportedExtensions': (
          'QVulkanInfoVector<QVulkanExtension> '
          'QPlatformVulkanInstance::supportedExtensions() const',
      ),
      'errorCode': (
          'VkResult QPlatformVulkanInstance::errorCode() const',
      ),
      'vkInstance': (
          'VkInstance QPlatformVulkanInstance::vkInstance() const',
      ),
      'enabledLayers': (
          'QByteArrayList QPlatformVulkanInstance::enabledLayers() const',
      ),
      'enabledExtensions': (
          'QByteArrayList QPlatformVulkanInstance::enabledExtensions() '
          'const',
      ),
      'getInstanceProcAddr': (
          'PFN_vkVoidFunction '
          'QPlatformVulkanInstance::getInstanceProcAddr(const char *)',
      ),
      'supportsPresent': (
          'bool QPlatformVulkanInstance::supportsPresent(VkPhysicalDevice, '
          'uint32_t, QWindow *)',
      ),
      'setDebugFilters': (
          'void QPlatformVulkanInstance::setDebugFilters(const '
          'QList<QVulkanInstance::DebugFilter> &)',
      ),
      'setDebugUtilsFilters': (
          'void QPlatformVulkanInstance::setDebugUtilsFilters(const '
          'QList<QVulkanInstance::DebugUtilsFilter> &)',
      ),
  }

  #  The functions Qt calls itself that QPlatformVulkanInstance is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'supportedApiVersion': (
          ('_ZNK23QPlatformVulkanInstance19supportedApiVersionEv',
           ('address', 'value', 'QtCore:QVersionNumber'),
           ()),
      ),
      'createOrAdoptInstance': (
          ('_ZN23QPlatformVulkanInstance21createOrAdoptInstanceEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'isValid': (
          ('_ZNK23QPlatformVulkanInstance7isValidEv',
           ('bool', 'number', ''),
           ()),
      ),
      'presentAboutToBeQueued': (
          ('_ZN23QPlatformVulkanInstance22presentAboutToBeQueuedEP7QWindow',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QWindow'),
           )),
      ),
      'presentQueued': (
          ('_ZN23QPlatformVulkanInstance13presentQueuedEP7QWindow',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QWindow'),
           )),
      ),
      'beginFrame': (
          ('_ZN23QPlatformVulkanInstance10beginFrameEP7QWindow',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QWindow'),
           )),
      ),
      'endFrame': (
          ('_ZN23QPlatformVulkanInstance8endFrameEP7QWindow',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QWindow'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def supportedApiVersion(self) -> QVersionNumber:
    """
    Calls Qt's 'QVersionNumber QPlatformVulkanInstance::supportedApiVersion()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvulkaninstance.html#supportedApiVersion

    Returns
    -------

    QVersionNumber
      A new cute QVersionNumber around the copy Qt gave back. Python owns it.
    """
    #  QVersionNumber QPlatformVulkanInstance::supportedApiVersion() const
    address = self.uglySide.call(
        'ritual_ZNK23QPlatformVulkanInstance19supportedApiVersionEv',
    )
    from ..QtCore import QVersionNumber
    return QVersionNumber._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QPlatformVulkanInstance::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvulkaninstance.html#isValid
    """
    #  bool QPlatformVulkanInstance::isValid() const
    return self.uglySide.call(
        'ritual_ZNK23QPlatformVulkanInstance7isValidEv',
    )

  def enabledLayers(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QByteArrayList QPlatformVulkanInstance::enabledLayers()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvulkaninstance.html#enabledLayers

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayList QPlatformVulkanInstance::enabledLayers() const
    address = self.uglySide.call(
        'ritual_ZNK23QPlatformVulkanInstance13enabledLayersEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  def enabledExtensions(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QByteArrayList QPlatformVulkanInstance::enabledExtensions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvulkaninstance.html#enabledExtensions

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayList QPlatformVulkanInstance::enabledExtensions() const
    address = self.uglySide.call(
        'ritual_ZNK23QPlatformVulkanInstance17enabledExtensionsEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QPlatformVulkanInstance::QPlatformVulkanInstance()': the class is
    abstract, so C++ cannot make one, and the C++ class of ours does not fill
    in every function it leaves open.
    """
    raise NotImplementedError(
        "'QPlatformVulkanInstance.__init__' has no cute function yet. Qt's "
        "'QPlatformVulkanInstance::QPlatformVulkanInstance()': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open.")

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

  def createOrAdoptInstance(self) -> None:
    """
    Calls Qt's 'void QPlatformVulkanInstance::createOrAdoptInstance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvulkaninstance.html#createOrAdoptInstance
    """
    #  void QPlatformVulkanInstance::createOrAdoptInstance()
    self.uglySide.call(
        'ritual_ZN23QPlatformVulkanInstance21createOrAdoptInstanceEv',
    )

  @overload(QWindow)
  @overload(NoneType)
  def presentAboutToBeQueued(self, window: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QPlatformVulkanInstance::presentAboutToBeQueued(QWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvulkaninstance.html

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformVulkanInstance::presentAboutToBeQueued(QWindow *window)
    ritual = (
        'ritual_ZN23QPlatformVulkanInstance22presentAboutToBeQueuedEP7QWind'
        'ow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QPlatformVulkanInstance22presentAboutToBeQueuedEP'
          '7QWindow')
    self.uglySide.call(ritual, self._addressOf(window))

  @overload(QWindow)
  @overload(NoneType)
  def presentQueued(self, window: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QPlatformVulkanInstance::presentQueued(QWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvulkaninstance.html#presentQueued

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformVulkanInstance::presentQueued(QWindow *window)
    ritual = 'ritual_ZN23QPlatformVulkanInstance13presentQueuedEP7QWindow'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QPlatformVulkanInstance13presentQueuedEP7QWindow')
    self.uglySide.call(ritual, self._addressOf(window))

  @overload(QWindow)
  @overload(NoneType)
  def beginFrame(self, window: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QPlatformVulkanInstance::beginFrame(QWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvulkaninstance.html#beginFrame

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformVulkanInstance::beginFrame(QWindow *window)
    ritual = 'ritual_ZN23QPlatformVulkanInstance10beginFrameEP7QWindow'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QPlatformVulkanInstance10beginFrameEP7QWindow'
    self.uglySide.call(ritual, self._addressOf(window))

  @overload(QWindow)
  @overload(NoneType)
  def endFrame(self, window: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QPlatformVulkanInstance::endFrame(QWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvulkaninstance.html#endFrame

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformVulkanInstance::endFrame(QWindow *window)
    ritual = 'ritual_ZN23QPlatformVulkanInstance8endFrameEP7QWindow'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QPlatformVulkanInstance8endFrameEP7QWindow'
    self.uglySide.call(ritual, self._addressOf(window))

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QPlatformVulkanInstancePrivate
      *QPlatformVulkanInstance::d_func()': gives
      'QPlatformVulkanInstancePrivate', which has no cute class yet.
    - Qt's 'const QPlatformVulkanInstancePrivate
      *QPlatformVulkanInstance::d_func() const': gives
      'QPlatformVulkanInstancePrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformVulkanInstance.d_func' has no cute function yet. Qt's "
        "'QPlatformVulkanInstancePrivate "
        "*QPlatformVulkanInstance::d_func()': gives "
        "'QPlatformVulkanInstancePrivate', which has no cute class yet. "
        "Qt's 'const QPlatformVulkanInstancePrivate "
        "*QPlatformVulkanInstance::d_func() const': gives "
        "'QPlatformVulkanInstancePrivate', which has no cute class yet.")

  @staticmethod
  def errorCode(*__, **_) -> Never:
    """
    Qt's 'VkResult QPlatformVulkanInstance::errorCode() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformVulkanInstance.errorCode' has no cute function yet. Qt's "
        "'VkResult QPlatformVulkanInstance::errorCode() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def getInstanceProcAddr(*__, **_) -> Never:
    """
    Qt's 'PFN_vkVoidFunction
    QPlatformVulkanInstance::getInstanceProcAddr(const char *name)': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformVulkanInstance.getInstanceProcAddr' has no cute function "
        "yet. Qt's 'PFN_vkVoidFunction "
        "QPlatformVulkanInstance::getInstanceProcAddr(const char *name)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def setDebugFilters(*__, **_) -> Never:
    """
    Qt's 'void QPlatformVulkanInstance::setDebugFilters(const
    QList<QVulkanInstance::DebugFilter> &filters)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformVulkanInstance.setDebugFilters' has no cute function "
        "yet. Qt's 'void QPlatformVulkanInstance::setDebugFilters(const "
        "QList<QVulkanInstance::DebugFilter> &filters)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def setDebugUtilsFilters(*__, **_) -> Never:
    """
    Qt's 'void QPlatformVulkanInstance::setDebugUtilsFilters(const
    QList<QVulkanInstance::DebugUtilsFilter> &filters)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformVulkanInstance.setDebugUtilsFilters' has no cute "
        "function yet. Qt's 'void "
        "QPlatformVulkanInstance::setDebugUtilsFilters(const "
        "QList<QVulkanInstance::DebugUtilsFilter> &filters)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def supportedExtensions(*__, **_) -> Never:
    """
    Qt's 'QVulkanInfoVector<QVulkanExtension>
    QPlatformVulkanInstance::supportedExtensions() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformVulkanInstance.supportedExtensions' has no cute function "
        "yet. Qt's 'QVulkanInfoVector<QVulkanExtension> "
        "QPlatformVulkanInstance::supportedExtensions() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def supportedLayers(*__, **_) -> Never:
    """
    Qt's 'QVulkanInfoVector<QVulkanLayer>
    QPlatformVulkanInstance::supportedLayers() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformVulkanInstance.supportedLayers' has no cute function "
        "yet. Qt's 'QVulkanInfoVector<QVulkanLayer> "
        "QPlatformVulkanInstance::supportedLayers() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def supportsPresent(*__, **_) -> Never:
    """
    Qt's 'bool QPlatformVulkanInstance::supportsPresent(VkPhysicalDevice
    physicalDevice, uint32_t queueFamilyIndex, QWindow *window)': names
    'struct VkPhysicalDevice_T', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformVulkanInstance.supportsPresent' has no cute function "
        "yet. Qt's 'bool "
        "QPlatformVulkanInstance::supportsPresent(VkPhysicalDevice "
        "physicalDevice, uint32_t queueFamilyIndex, QWindow *window)': "
        "names 'struct VkPhysicalDevice_T', which has no cute class yet.")

  @staticmethod
  def vkInstance(*__, **_) -> Never:
    """
    Qt's 'VkInstance QPlatformVulkanInstance::vkInstance() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformVulkanInstance.vkInstance' has no cute function yet. "
        "Qt's 'VkInstance QPlatformVulkanInstance::vkInstance() const': "
        "gives a type Python has no way to take yet.")
