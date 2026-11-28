"""
QQuickGraphicsDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qquickgraphicsdevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QOpenGLContext, QRhi, QRhiAdapter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLContext = WAIT['QOpenGLContext']
  QRhi = WAIT['QRhi']
  QRhiAdapter = WAIT['QRhiAdapter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGraphicsDevice(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickGraphicsDevice: a plain Python object standing
  in front of one C++ QQuickGraphicsDevice.

  C++ hands a QQuickGraphicsDevice around as a copy, so every C++
  QQuickGraphicsDevice behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickGraphicsDevice that has a ritual and that
  Python can call so far, 5 names in all: 'isNull', 'fromOpenGLContext',
  'fromRhi', 'fromRhiAdapter', 'detach'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickGraphicsDevice::~QQuickGraphicsDevice()': the destructor:
    Python removes its C++ QQuickGraphicsDevice by it, and has no other use
    for it.
  - Qt's 'QQuickGraphicsDevice &QQuickGraphicsDevice::operator=(const
    QQuickGraphicsDevice &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QQuickGraphicsDevice
    QQuickGraphicsDevice::fromDeviceAndCommandQueue(MTLDevice *device,
    MTLCommandQueue *commandQueue)': names 'MTLDevice', which has no cute
    class yet.
  - Qt's 'QQuickGraphicsDevice
    QQuickGraphicsDevice::fromPhysicalDevice(VkPhysicalDevice
    physicalDevice)': names 'struct VkPhysicalDevice_T', which has no cute
    class yet.
  - Qt's 'QQuickGraphicsDevice
    QQuickGraphicsDevice::fromDeviceObjects(VkPhysicalDevice physicalDevice,
    VkDevice device, int queueFamilyIndex, int queueIndex)': names 'struct
    VkPhysicalDevice_T', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQuickGraphicsDevice is created at the first use, not by
    'QQuickGraphicsDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickGraphicsDevice back gives a copy the ritual
    made for Python, in a new cute QQuickGraphicsDevice.
  - Each name of Qt's QQuickGraphicsDevice that has no cute function yet,
    'fromDeviceAndCommandQueue', 'fromDeviceObjects', 'fromPhysicalDevice',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QOpenGLContext)
  @overload(NoneType)
  def fromOpenGLContext(
      context: Optional[QOpenGLContext],
  ) -> QQuickGraphicsDevice:
    """
    Calls Qt's 'QQuickGraphicsDevice
    QQuickGraphicsDevice::fromOpenGLContext(QOpenGLContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsdevice.html#fromOpenGLContext

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQuickGraphicsDevice
      A new cute QQuickGraphicsDevice around the copy Qt gave back. Python
      owns it.
    """
    #  QQuickGraphicsDevice
    #      QQuickGraphicsDevice::fromOpenGLContext(QOpenGLContext *context)
    address = Rituals.call(
        'ritual_ZN20QQuickGraphicsDevice17fromOpenGLContextEP14QOpenGLConte'
        'xt',
        CuteMixin._addressOf(context),
    )
    return QQuickGraphicsDevice._cuteOwning(address)

  @staticmethod
  @overload(QRhi)
  @overload(NoneType)
  def fromRhi(rhi: Optional[QRhi]) -> QQuickGraphicsDevice:
    """
    Calls Qt's 'QQuickGraphicsDevice QQuickGraphicsDevice::fromRhi(QRhi
    *rhi)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphicsdevice.html#fromRhi

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQuickGraphicsDevice
      A new cute QQuickGraphicsDevice around the copy Qt gave back. Python
      owns it.
    """
    #  QQuickGraphicsDevice QQuickGraphicsDevice::fromRhi(QRhi *rhi)
    address = Rituals.call(
        'ritual_ZN20QQuickGraphicsDevice7fromRhiEP4QRhi',
        CuteMixin._addressOf(rhi),
    )
    return QQuickGraphicsDevice._cuteOwning(address)

  @staticmethod
  @overload(QRhiAdapter)
  @overload(NoneType)
  def fromRhiAdapter(adapter: Optional[QRhiAdapter]) -> QQuickGraphicsDevice:
    """
    Calls Qt's 'QQuickGraphicsDevice
    QQuickGraphicsDevice::fromRhiAdapter(QRhiAdapter *adapter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsdevice.html#fromRhiAdapter

    Parameters
    ----------

    adapter : Optional[QRhiAdapter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQuickGraphicsDevice
      A new cute QQuickGraphicsDevice around the copy Qt gave back. Python
      owns it.
    """
    #  QQuickGraphicsDevice QQuickGraphicsDevice::fromRhiAdapter(QRhiAdapter
    #      *adapter)
    address = Rituals.call(
        'ritual_ZN20QQuickGraphicsDevice14fromRhiAdapterEP11QRhiAdapter',
        CuteMixin._addressOf(adapter),
    )
    return QQuickGraphicsDevice._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGraphicsDevice'

  #  Qt's '~QQuickGraphicsDevice()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickGraphicsDevice behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QQuickGraphicsDeviceD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphicsDevice::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphicsdevice.html#isNull
    """
    #  bool QQuickGraphicsDevice::isNull() const
    return self.uglySide.call('ritual_ZNK20QQuickGraphicsDevice6isNullEv')

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
    'QQuickGraphicsDevice::QQuickGraphicsDevice()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsdevice.html#QQuickGraphicsDevice
    """
    #  QQuickGraphicsDevice::QQuickGraphicsDevice()
    self._noteCreation(QQuickGraphicsDevice, lambda: Rituals.call(
        'ritual_ZN20QQuickGraphicsDeviceC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QQuickGraphicsDevice) -> None:
    """
    Notes what was given, for Qt's
    'QQuickGraphicsDevice::QQuickGraphicsDevice(const QQuickGraphicsDevice
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsdevice.html#QQuickGraphicsDevice

    Parameters
    ----------

    other : QQuickGraphicsDevice
      Passed on as a value: Qt reads the C++ QQuickGraphicsDevice, which
      stays Python's own.
    """
    #  QQuickGraphicsDevice::QQuickGraphicsDevice(const QQuickGraphicsDevice
    #      &other)
    self._noteCreation(QQuickGraphicsDevice, lambda: Rituals.call(
        'ritual_ZN20QQuickGraphicsDeviceC1ERKS_', self._valueOf(other),
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

  def detach(self) -> None:
    """
    Calls Qt's 'void QQuickGraphicsDevice::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphicsdevice.html#detach
    """
    #  void QQuickGraphicsDevice::detach()
    self.uglySide.call('ritual_ZN20QQuickGraphicsDevice6detachEv')

  @staticmethod
  def fromDeviceAndCommandQueue(*__, **_) -> Never:
    """
    Qt's 'QQuickGraphicsDevice
    QQuickGraphicsDevice::fromDeviceAndCommandQueue(MTLDevice *device,
    MTLCommandQueue *commandQueue)': names 'MTLDevice', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphicsDevice.fromDeviceAndCommandQueue' has no cute "
        "function yet. Qt's 'QQuickGraphicsDevice "
        "QQuickGraphicsDevice::fromDeviceAndCommandQueue(MTLDevice *device, "
        "MTLCommandQueue *commandQueue)': names 'MTLDevice', which has no "
        "cute class yet.")

  @staticmethod
  def fromDeviceObjects(*__, **_) -> Never:
    """
    Qt's 'QQuickGraphicsDevice
    QQuickGraphicsDevice::fromDeviceObjects(VkPhysicalDevice physicalDevice,
    VkDevice device, int queueFamilyIndex, int queueIndex)': names 'struct
    VkPhysicalDevice_T', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphicsDevice.fromDeviceObjects' has no cute function yet. "
        "Qt's 'QQuickGraphicsDevice "
        "QQuickGraphicsDevice::fromDeviceObjects(VkPhysicalDevice "
        "physicalDevice, VkDevice device, int queueFamilyIndex, int "
        "queueIndex)': names 'struct VkPhysicalDevice_T', which has no cute "
        "class yet.")

  @staticmethod
  def fromPhysicalDevice(*__, **_) -> Never:
    """
    Qt's 'QQuickGraphicsDevice
    QQuickGraphicsDevice::fromPhysicalDevice(VkPhysicalDevice
    physicalDevice)': names 'struct VkPhysicalDevice_T', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphicsDevice.fromPhysicalDevice' has no cute function "
        "yet. Qt's 'QQuickGraphicsDevice "
        "QQuickGraphicsDevice::fromPhysicalDevice(VkPhysicalDevice "
        "physicalDevice)': names 'struct VkPhysicalDevice_T', which has no "
        "cute class yet.")
