"""
QQuickRenderTarget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qquickrendertarget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QSize
  from ..QtGui import QPaintDevice, QRhiRenderTarget, QRhiTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPaintDevice = WAIT['QPaintDevice']
  QRhiRenderTarget = WAIT['QRhiRenderTarget']
  QRhiTexture = WAIT['QRhiTexture']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickRenderTarget(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickRenderTarget: a plain Python object standing in
  front of one C++ QQuickRenderTarget.

  C++ hands a QQuickRenderTarget around as a copy, so every C++
  QQuickRenderTarget behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickRenderTarget that has a ritual and that Python
  can call so far, 15 names in all: 'isNull', 'devicePixelRatio',
  'setDevicePixelRatio', 'mirrorVertically', 'setMirrorVertically',
  'depthTexture', 'setDepthTexture', 'fromOpenGLTexture',
  'fromOpenGLRenderBuffer', 'fromRhiRenderTarget', 'fromPaintDevice',
  'detach', 'isEqual', '__eq__', '__ne__'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickRenderTarget::~QQuickRenderTarget()': the destructor: Python
    removes its C++ QQuickRenderTarget by it, and has no other use for it.
  - Qt's 'QQuickRenderTarget &QQuickRenderTarget::operator=(const
    QQuickRenderTarget &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QQuickRenderTarget QQuickRenderTarget::fromMetalTexture(MTLTexture
    *texture, const QSize &pixelSize, int sampleCount)': names 'MTLTexture',
    which has no cute class yet.
  - Qt's 'QQuickRenderTarget QQuickRenderTarget::fromMetalTexture(MTLTexture
    *texture, uint format, const QSize &pixelSize, int sampleCount)': names
    'MTLTexture', which has no cute class yet.
  - Qt's 'QQuickRenderTarget QQuickRenderTarget::fromMetalTexture(MTLTexture
    *texture, uint format, uint viewFormat, QSize pixelSize, int sampleCount,
    int arraySize, Flags flags)': names 'MTLTexture', which has no cute class
    yet.
  - Qt's 'QQuickRenderTarget QQuickRenderTarget::fromVulkanImage(VkImage
    image, VkImageLayout layout, const QSize &pixelSize, int sampleCount)':
    names 'struct VkImage_T', which has no cute class yet.
  - Qt's 'QQuickRenderTarget QQuickRenderTarget::fromVulkanImage(VkImage
    image, VkImageLayout layout, VkFormat format, const QSize &pixelSize, int
    sampleCount)': names 'struct VkImage_T', which has no cute class yet.
  - Qt's 'QQuickRenderTarget QQuickRenderTarget::fromVulkanImage(VkImage
    image, VkImageLayout layout, VkFormat format, VkFormat viewFormat, QSize
    pixelSize, int sampleCount, int arraySize, Flags flags)': names 'struct
    VkImage_T', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQuickRenderTarget is created at the first use, not by
    'QQuickRenderTarget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickRenderTarget back gives a copy the ritual made
    for Python, in a new cute QQuickRenderTarget.
  - Each name of Qt's QQuickRenderTarget that has no cute function yet,
    'fromMetalTexture', 'fromVulkanImage', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickRenderTarget, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags, scoped=True):
    """
    The flags enum 'QQuickRenderTarget::Flag' of Qt, with the 1 names Qt
    gives in it. Qt names the type of its combinations
    'QQuickRenderTarget::Flags'. C++ keeps these names inside the enum, so
    the class that holds the enum does not have them.
    """

    MultisampleResolve = 0x1

  Flags = Flag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int, QSize)
  @overload(int, QSize, int)
  def fromOpenGLTexture(
      textureId: int,
      pixelSize: QSize,
      sampleCount: int = 1,
  ) -> QQuickRenderTarget:
    """
    Calls Qt's 'QQuickRenderTarget QQuickRenderTarget::fromOpenGLTexture(uint
    textureId, const QSize &pixelSize, int sampleCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendertarget.html#fromOpenGLTexture

    Parameters
    ----------

    textureId : int
      Passed on as it is.

    pixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    sampleCount : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    Returns
    -------

    QQuickRenderTarget
      A new cute QQuickRenderTarget around the copy Qt gave back. Python owns
      it.
    """
    #  QQuickRenderTarget QQuickRenderTarget::fromOpenGLTexture(uint
    #      textureId, const QSize &pixelSize, int sampleCount)
    address = Rituals.call(
        'ritual_ZN18QQuickRenderTarget17fromOpenGLTextureEjRK5QSizei',
        textureId, CuteMixin._valueOf(pixelSize), sampleCount,
    )
    return QQuickRenderTarget._cuteOwning(address)

  @staticmethod
  @overload(int, int, QSize)
  @overload(int, int, QSize, int)
  def fromOpenGLTexture(
      textureId: int,
      format: int,
      pixelSize: QSize,
      sampleCount: int = 1,
  ) -> QQuickRenderTarget:
    """
    Calls Qt's 'QQuickRenderTarget QQuickRenderTarget::fromOpenGLTexture(uint
    textureId, uint format, const QSize &pixelSize, int sampleCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendertarget.html#fromOpenGLTexture

    Parameters
    ----------

    textureId : int
      Passed on as it is.

    format : int
      Passed on as it is.

    pixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    sampleCount : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    Returns
    -------

    QQuickRenderTarget
      A new cute QQuickRenderTarget around the copy Qt gave back. Python owns
      it.
    """
    #  QQuickRenderTarget QQuickRenderTarget::fromOpenGLTexture(uint
    #      textureId, uint format, const QSize &pixelSize, int sampleCount)
    address = Rituals.call(
        'ritual_ZN18QQuickRenderTarget17fromOpenGLTextureEjjRK5QSizei',
        textureId, format, CuteMixin._valueOf(pixelSize), sampleCount,
    )
    return QQuickRenderTarget._cuteOwning(address)

  @staticmethod
  @overload(int, int, QSize, int, int, Flags)
  def fromOpenGLTexture(
      textureId: int,
      format: int,
      pixelSize: QSize,
      sampleCount: int,
      arraySize: int,
      flags: Flags,
  ) -> QQuickRenderTarget:
    """
    Calls Qt's 'QQuickRenderTarget QQuickRenderTarget::fromOpenGLTexture(uint
    textureId, uint format, QSize pixelSize, int sampleCount, int arraySize,
    Flags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendertarget.html#fromOpenGLTexture

    Parameters
    ----------

    textureId : int
      Passed on as it is.

    format : int
      Passed on as it is.

    pixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    sampleCount : int
      Passed on as it is.

    arraySize : int
      Passed on as it is.

    flags : Flags
      Passed on as its number.

    Returns
    -------

    QQuickRenderTarget
      A new cute QQuickRenderTarget around the copy Qt gave back. Python owns
      it.
    """
    #  QQuickRenderTarget QQuickRenderTarget::fromOpenGLTexture(uint
    #      textureId, uint format, QSize pixelSize, int sampleCount, int
    #      arraySize, Flags flags)
    address = Rituals.call(
        'ritual_ZN18QQuickRenderTarget17fromOpenGLTextureEjj5QSizeii6QFlags'
        'INS_4FlagEE',
        textureId, format, CuteMixin._valueOf(pixelSize), sampleCount,
        arraySize, flags.value,
    )
    return QQuickRenderTarget._cuteOwning(address)

  @staticmethod
  @overload(int, QSize)
  @overload(int, QSize, int)
  def fromOpenGLRenderBuffer(
      renderbufferId: int,
      pixelSize: QSize,
      sampleCount: int = 1,
  ) -> QQuickRenderTarget:
    """
    Calls Qt's 'QQuickRenderTarget
    QQuickRenderTarget::fromOpenGLRenderBuffer(uint renderbufferId, const
    QSize &pixelSize, int sampleCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendertarget.html#fromOpenGLRenderBuffer

    Parameters
    ----------

    renderbufferId : int
      Passed on as it is.

    pixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    sampleCount : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    Returns
    -------

    QQuickRenderTarget
      A new cute QQuickRenderTarget around the copy Qt gave back. Python owns
      it.
    """
    #  QQuickRenderTarget QQuickRenderTarget::fromOpenGLRenderBuffer(uint
    #      renderbufferId, const QSize &pixelSize, int sampleCount)
    address = Rituals.call(
        'ritual_ZN18QQuickRenderTarget22fromOpenGLRenderBufferEjRK5QSizei',
        renderbufferId, CuteMixin._valueOf(pixelSize), sampleCount,
    )
    return QQuickRenderTarget._cuteOwning(address)

  @staticmethod
  @overload(QRhiRenderTarget)
  @overload(NoneType)
  def fromRhiRenderTarget(
      renderTarget: Optional[QRhiRenderTarget],
  ) -> QQuickRenderTarget:
    """
    Calls Qt's 'QQuickRenderTarget
    QQuickRenderTarget::fromRhiRenderTarget(QRhiRenderTarget *renderTarget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendertarget.html#fromRhiRenderTarget

    Parameters
    ----------

    renderTarget : Optional[QRhiRenderTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQuickRenderTarget
      A new cute QQuickRenderTarget around the copy Qt gave back. Python owns
      it.
    """
    #  QQuickRenderTarget
    #      QQuickRenderTarget::fromRhiRenderTarget(QRhiRenderTarget
    #      *renderTarget)
    address = Rituals.call(
        'ritual_ZN18QQuickRenderTarget19fromRhiRenderTargetEP16QRhiRenderTa'
        'rget',
        CuteMixin._addressOf(renderTarget),
    )
    return QQuickRenderTarget._cuteOwning(address)

  @staticmethod
  @overload(QPaintDevice)
  @overload(NoneType)
  def fromPaintDevice(device: Optional[QPaintDevice]) -> QQuickRenderTarget:
    """
    Calls Qt's 'QQuickRenderTarget
    QQuickRenderTarget::fromPaintDevice(QPaintDevice *device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendertarget.html#fromPaintDevice

    Parameters
    ----------

    device : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQuickRenderTarget
      A new cute QQuickRenderTarget around the copy Qt gave back. Python owns
      it.
    """
    #  QQuickRenderTarget QQuickRenderTarget::fromPaintDevice(QPaintDevice
    #      *device)
    address = Rituals.call(
        'ritual_ZN18QQuickRenderTarget15fromPaintDeviceEP12QPaintDevice',
        CuteMixin._addressOf(device, 'QPaintDevice'),
    )
    return QQuickRenderTarget._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRenderTarget'

  #  Qt's '~QQuickRenderTarget()'. Naming it makes this a value class: Python
  #  owns every C++ QQuickRenderTarget behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQuickRenderTargetD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QQuickRenderTarget::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrendertarget.html#isNull
    """
    #  bool QQuickRenderTarget::isNull() const
    return self.uglySide.call('ritual_ZNK18QQuickRenderTarget6isNullEv')

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'qreal QQuickRenderTarget::devicePixelRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendertarget.html#devicePixelRatio
    """
    #  qreal QQuickRenderTarget::devicePixelRatio() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickRenderTarget16devicePixelRatioEv',
    )

  def mirrorVertically(self) -> bool:
    """
    Calls Qt's 'bool QQuickRenderTarget::mirrorVertically() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendertarget.html#mirrorVertically
    """
    #  bool QQuickRenderTarget::mirrorVertically() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickRenderTarget16mirrorVerticallyEv',
    )

  def depthTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QQuickRenderTarget::depthTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendertarget.html#depthTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QQuickRenderTarget::depthTexture() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickRenderTarget12depthTextureEv',
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  @overload(THIS)
  def isEqual(self, other: QQuickRenderTarget) -> bool:
    """
    Calls Qt's 'bool QQuickRenderTarget::isEqual(const QQuickRenderTarget
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrendertarget.html#isEqual

    Parameters
    ----------

    other : QQuickRenderTarget
      Passed on as a value: Qt reads the C++ QQuickRenderTarget, which stays
      Python's own.
    """
    #  bool QQuickRenderTarget::isEqual(const QQuickRenderTarget &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QQuickRenderTarget7isEqualERKS_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setDevicePixelRatio(self, ratio: float) -> None:
    """
    Calls Qt's 'void QQuickRenderTarget::setDevicePixelRatio(qreal ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendertarget.html#setDevicePixelRatio

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void QQuickRenderTarget::setDevicePixelRatio(qreal ratio)
    self.uglySide.call(
        'ritual_ZN18QQuickRenderTarget19setDevicePixelRatioEd', ratio,
    )

  @overload(bool)
  def setMirrorVertically(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickRenderTarget::setMirrorVertically(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendertarget.html#setMirrorVertically

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickRenderTarget::setMirrorVertically(bool enable)
    self.uglySide.call(
        'ritual_ZN18QQuickRenderTarget19setMirrorVerticallyEb', enable,
    )

  @overload(QRhiTexture)
  @overload(NoneType)
  def setDepthTexture(self, texture: Optional[QRhiTexture]) -> None:
    """
    Calls Qt's 'void QQuickRenderTarget::setDepthTexture(QRhiTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendertarget.html#setDepthTexture

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRenderTarget::setDepthTexture(QRhiTexture *texture)
    self.uglySide.call(
        'ritual_ZN18QQuickRenderTarget15setDepthTextureEP11QRhiTexture',
        self._addressOf(texture),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QQuickRenderTarget) -> bool:
    """
    Calls Qt's 'bool operator==(const QQuickRenderTarget &lhs, const
    QQuickRenderTarget &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrendertarget.html#operator==

    Parameters
    ----------

    rhs : QQuickRenderTarget
      Passed on as a value: Qt reads the C++ QQuickRenderTarget, which stays
      Python's own.
    """
    #  bool operator==(const QQuickRenderTarget &lhs, const
    #      QQuickRenderTarget &rhs)
    return Rituals.call(
        'ritual_ZeqRK18QQuickRenderTargetS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QQuickRenderTarget) -> bool:
    """
    Calls Qt's 'bool operator!=(const QQuickRenderTarget &lhs, const
    QQuickRenderTarget &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrendertarget.html#operator!=

    Parameters
    ----------

    rhs : QQuickRenderTarget
      Passed on as a value: Qt reads the C++ QQuickRenderTarget, which stays
      Python's own.
    """
    #  bool operator!=(const QQuickRenderTarget &lhs, const
    #      QQuickRenderTarget &rhs)
    return Rituals.call(
        'ritual_ZneRK18QQuickRenderTargetS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuickRenderTarget::QQuickRenderTarget()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendertarget.html#QQuickRenderTarget
    """
    #  QQuickRenderTarget::QQuickRenderTarget()
    self._noteCreation(QQuickRenderTarget, lambda: Rituals.call(
        'ritual_ZN18QQuickRenderTargetC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QQuickRenderTarget) -> None:
    """
    Notes what was given, for Qt's
    'QQuickRenderTarget::QQuickRenderTarget(const QQuickRenderTarget
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendertarget.html#QQuickRenderTarget

    Parameters
    ----------

    other : QQuickRenderTarget
      Passed on as a value: Qt reads the C++ QQuickRenderTarget, which stays
      Python's own.
    """
    #  QQuickRenderTarget::QQuickRenderTarget(const QQuickRenderTarget
    #      &other)
    self._noteCreation(QQuickRenderTarget, lambda: Rituals.call(
        'ritual_ZN18QQuickRenderTargetC1ERKS_', self._valueOf(other),
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
    Calls Qt's 'void QQuickRenderTarget::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrendertarget.html#detach
    """
    #  void QQuickRenderTarget::detach()
    self.uglySide.call('ritual_ZN18QQuickRenderTarget6detachEv')

  @staticmethod
  def fromMetalTexture(*__, **_) -> Never:
    """
    - Qt's 'QQuickRenderTarget
      QQuickRenderTarget::fromMetalTexture(MTLTexture *texture, const QSize
      &pixelSize, int sampleCount)': names 'MTLTexture', which has no cute
      class yet.
    - Qt's 'QQuickRenderTarget
      QQuickRenderTarget::fromMetalTexture(MTLTexture *texture, uint format,
      const QSize &pixelSize, int sampleCount)': names 'MTLTexture', which
      has no cute class yet.
    - Qt's 'QQuickRenderTarget
      QQuickRenderTarget::fromMetalTexture(MTLTexture *texture, uint format,
      uint viewFormat, QSize pixelSize, int sampleCount, int arraySize, Flags
      flags)': names 'MTLTexture', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickRenderTarget.fromMetalTexture' has no cute function yet. "
        "Qt's 'QQuickRenderTarget "
        "QQuickRenderTarget::fromMetalTexture(MTLTexture *texture, const "
        "QSize &pixelSize, int sampleCount)': names 'MTLTexture', which has "
        "no cute class yet. Qt's 'QQuickRenderTarget "
        "QQuickRenderTarget::fromMetalTexture(MTLTexture *texture, uint "
        "format, const QSize &pixelSize, int sampleCount)': names "
        "'MTLTexture', which has no cute class yet. Qt's "
        "'QQuickRenderTarget "
        "QQuickRenderTarget::fromMetalTexture(MTLTexture *texture, uint "
        "format, uint viewFormat, QSize pixelSize, int sampleCount, int "
        "arraySize, Flags flags)': names 'MTLTexture', which has no cute "
        "class yet.")

  @staticmethod
  def fromVulkanImage(*__, **_) -> Never:
    """
    - Qt's 'QQuickRenderTarget QQuickRenderTarget::fromVulkanImage(VkImage
      image, VkImageLayout layout, const QSize &pixelSize, int sampleCount)':
      names 'struct VkImage_T', which has no cute class yet.
    - Qt's 'QQuickRenderTarget QQuickRenderTarget::fromVulkanImage(VkImage
      image, VkImageLayout layout, VkFormat format, const QSize &pixelSize,
      int sampleCount)': names 'struct VkImage_T', which has no cute class
      yet.
    - Qt's 'QQuickRenderTarget QQuickRenderTarget::fromVulkanImage(VkImage
      image, VkImageLayout layout, VkFormat format, VkFormat viewFormat,
      QSize pixelSize, int sampleCount, int arraySize, Flags flags)': names
      'struct VkImage_T', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickRenderTarget.fromVulkanImage' has no cute function yet. "
        "Qt's 'QQuickRenderTarget "
        "QQuickRenderTarget::fromVulkanImage(VkImage image, VkImageLayout "
        "layout, const QSize &pixelSize, int sampleCount)': names 'struct "
        "VkImage_T', which has no cute class yet. Qt's 'QQuickRenderTarget "
        "QQuickRenderTarget::fromVulkanImage(VkImage image, VkImageLayout "
        "layout, VkFormat format, const QSize &pixelSize, int "
        "sampleCount)': names 'struct VkImage_T', which has no cute class "
        "yet. Qt's 'QQuickRenderTarget "
        "QQuickRenderTarget::fromVulkanImage(VkImage image, VkImageLayout "
        "layout, VkFormat format, VkFormat viewFormat, QSize pixelSize, int "
        "sampleCount, int arraySize, Flags flags)': names 'struct "
        "VkImage_T', which has no cute class yet.")
