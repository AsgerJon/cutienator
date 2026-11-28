"""
QBackingStoreRhiSupport binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qbackingstorerhisupport_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QBackingStoreRhiSupport to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QPlatformBackingStoreRhiConfig, QRhi, QSurface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QRhiSwapChain, QSurfaceFormat, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSurfaceFormat = WAIT['QSurfaceFormat']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBackingStoreRhiSupport(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBackingStoreRhiSupport: a plain Python object
  standing in front of one C++ QBackingStoreRhiSupport.

  C++ hands a QBackingStoreRhiSupport around as a copy, so every C++
  QBackingStoreRhiSupport behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QBackingStoreRhiSupport that has a ritual and that
  Python can call so far, 9 names in all: 'reset', 'setFormat', 'setWindow',
  'setConfig', 'create', 'swapChainForWindow', 'surfaceTypeForConfig',
  'apiToRhiBackend', 'rhi'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBackingStoreRhiSupport::~QBackingStoreRhiSupport()': the
    destructor: Python removes its C++ QBackingStoreRhiSupport by it, and has
    no other use for it.
  - Qt's 'bool
    QBackingStoreRhiSupport::checkForceRhi(QPlatformBackingStoreRhiConfig
    *outConfig, QSurface::SurfaceType *outType)': names
    'QSurface::SurfaceType', which has no cute class yet.

  What to expect
  --------------

  - The C++ QBackingStoreRhiSupport is created at the first use, not by
    'QBackingStoreRhiSupport(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QBackingStoreRhiSupport back gives a copy the ritual
    made for Python, in a new cute QBackingStoreRhiSupport.
  - Each name of Qt's QBackingStoreRhiSupport that has no cute function yet,
    'checkForceRhi', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPlatformBackingStoreRhiConfig)
  def surfaceTypeForConfig(
      config: QPlatformBackingStoreRhiConfig,
  ) -> QSurface.SurfaceType:
    """
    Calls Qt's 'QSurface::SurfaceType
    QBackingStoreRhiSupport::surfaceTypeForConfig(const
    QPlatformBackingStoreRhiConfig &config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbackingstorerhisupport.html#surfaceTypeForConfig

    Parameters
    ----------

    config : QPlatformBackingStoreRhiConfig
      Passed on as a value: Qt reads the C++ QPlatformBackingStoreRhiConfig,
      which stays Python's own.

    Returns
    -------

    QSurface.SurfaceType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSurface.SurfaceType(number)' gives.
    """
    #  QSurface::SurfaceType
    #      QBackingStoreRhiSupport::surfaceTypeForConfig(const
    #      QPlatformBackingStoreRhiConfig &config)
    return QSurface.SurfaceType(Rituals.call(
        'ritual_ZN23QBackingStoreRhiSupport20surfaceTypeForConfigERK30QPlat'
        'formBackingStoreRhiConfig',
        CuteMixin._valueOf(config),
    ))

  @staticmethod
  @overload(QPlatformBackingStoreRhiConfig.Api)
  def apiToRhiBackend(
      api: QPlatformBackingStoreRhiConfig.Api,
  ) -> QRhi.Implementation:
    """
    Calls Qt's 'QRhi::Implementation
    QBackingStoreRhiSupport::apiToRhiBackend(
    QPlatformBackingStoreRhiConfig::Api api)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbackingstorerhisupport.html#apiToRhiBackend

    Parameters
    ----------

    api : QPlatformBackingStoreRhiConfig.Api
      Passed on as its number.

    Returns
    -------

    QRhi.Implementation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhi.Implementation(number)' gives.
    """
    #  QRhi::Implementation QBackingStoreRhiSupport::apiToRhiBackend(
    #      QPlatformBackingStoreRhiConfig::Api api)
    return QRhi.Implementation(Rituals.call(
        'ritual_ZN23QBackingStoreRhiSupport15apiToRhiBackendEN30QPlatformBa'
        'ckingStoreRhiConfig3ApiE',
        api.value,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBackingStoreRhiSupport'

  #  Qt's '~QBackingStoreRhiSupport()'. Naming it makes this a value class:
  #  Python owns every C++ QBackingStoreRhiSupport behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QBackingStoreRhiSupportD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rhi(self) -> Optional[QRhi]:
    """
    Calls Qt's 'QRhi *QBackingStoreRhiSupport::rhi() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbackingstorerhisupport.html#rhi

    Returns
    -------

    Optional[QRhi]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhi *QBackingStoreRhiSupport::rhi() const
    address = self.uglySide.call('ritual_ZNK23QBackingStoreRhiSupport3rhiEv')
    return QRhi._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSurfaceFormat)
  def setFormat(self, format: QSurfaceFormat) -> None:
    """
    Calls Qt's 'void QBackingStoreRhiSupport::setFormat(const QSurfaceFormat
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbackingstorerhisupport.html#setFormat

    Parameters
    ----------

    format : QSurfaceFormat
      Passed on as a value: Qt reads the C++ QSurfaceFormat, which stays
      Python's own.
    """
    #  void QBackingStoreRhiSupport::setFormat(const QSurfaceFormat &format)
    self.uglySide.call(
        'ritual_ZN23QBackingStoreRhiSupport9setFormatERK14QSurfaceFormat',
        self._valueOf(format),
    )

  @overload(QWindow)
  @overload(NoneType)
  def setWindow(self, window: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QBackingStoreRhiSupport::setWindow(QWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbackingstorerhisupport.html#setWindow

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBackingStoreRhiSupport::setWindow(QWindow *window)
    self.uglySide.call(
        'ritual_ZN23QBackingStoreRhiSupport9setWindowEP7QWindow',
        self._addressOf(window),
    )

  @overload(QPlatformBackingStoreRhiConfig)
  def setConfig(self, config: QPlatformBackingStoreRhiConfig) -> None:
    """
    Calls Qt's 'void QBackingStoreRhiSupport::setConfig(const
    QPlatformBackingStoreRhiConfig &config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbackingstorerhisupport.html#setConfig

    Parameters
    ----------

    config : QPlatformBackingStoreRhiConfig
      Passed on as a value: Qt reads the C++ QPlatformBackingStoreRhiConfig,
      which stays Python's own.
    """
    #  void QBackingStoreRhiSupport::setConfig(const
    #      QPlatformBackingStoreRhiConfig &config)
    self.uglySide.call(
        'ritual_ZN23QBackingStoreRhiSupport9setConfigERK30QPlatformBackingS'
        'toreRhiConfig',
        self._valueOf(config),
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

  def reset(self) -> None:
    """
    Calls Qt's 'void QBackingStoreRhiSupport::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qbackingstorerhisupport.html#reset
    """
    #  void QBackingStoreRhiSupport::reset()
    self.uglySide.call('ritual_ZN23QBackingStoreRhiSupport5resetEv')

  def create(self) -> bool:
    """
    Calls Qt's 'bool QBackingStoreRhiSupport::create()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbackingstorerhisupport.html#create
    """
    #  bool QBackingStoreRhiSupport::create()
    return self.uglySide.call('ritual_ZN23QBackingStoreRhiSupport6createEv')

  @overload(QWindow)
  @overload(NoneType)
  def swapChainForWindow(
      self,
      window: Optional[QWindow],
  ) -> Optional[QRhiSwapChain]:
    """
    Calls Qt's 'QRhiSwapChain
    *QBackingStoreRhiSupport::swapChainForWindow(QWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbackingstorerhisupport.html#swapChainForWindow

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QRhiSwapChain]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiSwapChain *QBackingStoreRhiSupport::swapChainForWindow(QWindow
    #      *window)
    address = self.uglySide.call(
        'ritual_ZN23QBackingStoreRhiSupport18swapChainForWindowEP7QWindow',
        self._addressOf(window),
    )
    from . import QRhiSwapChain
    return QRhiSwapChain._cuteAt(address)

  @staticmethod
  def checkForceRhi(*__, **_) -> Never:
    """
    Qt's 'bool
    QBackingStoreRhiSupport::checkForceRhi(QPlatformBackingStoreRhiConfig
    *outConfig, QSurface::SurfaceType *outType)': names
    'QSurface::SurfaceType', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QBackingStoreRhiSupport.checkForceRhi' has no cute function yet. "
        "Qt's 'bool "
        "QBackingStoreRhiSupport::checkForceRhi(QPlatformBackingStoreRhiConf"
        "ig *outConfig, QSurface::SurfaceType *outType)': names "
        "'QSurface::SurfaceType', which has no cute class yet.")
