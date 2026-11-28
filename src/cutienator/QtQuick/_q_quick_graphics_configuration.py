"""
QQuickGraphicsConfiguration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qquickgraphicsconfiguration.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray, QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QDebug = WAIT['QDebug']


class QQuickGraphicsConfiguration(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickGraphicsConfiguration: a plain Python object
  standing in front of one C++ QQuickGraphicsConfiguration.

  C++ hands a QQuickGraphicsConfiguration around as a copy, so every C++
  QQuickGraphicsConfiguration behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQuickGraphicsConfiguration that has a ritual and
  that Python can call so far, 21 names in all:
  'preferredInstanceExtensions', 'setDeviceExtensions', 'deviceExtensions',
  'setDepthBufferFor2D', 'isDepthBufferEnabledFor2D', 'setDebugLayer',
  'isDebugLayerEnabled', 'setDebugMarkers', 'isDebugMarkersEnabled',
  'setTimestamps', 'timestampsEnabled', 'setPreferSoftwareDevice',
  'prefersSoftwareDevice', 'setAutomaticPipelineCache',
  'isAutomaticPipelineCacheEnabled', 'setPipelineCacheSaveFile',
  'pipelineCacheSaveFile', 'setPipelineCacheLoadFile',
  'pipelineCacheLoadFile', 'detach', '__rlshift__'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickGraphicsConfiguration::~QQuickGraphicsConfiguration()': the
    destructor: Python removes its C++ QQuickGraphicsConfiguration by it, and
    has no other use for it.
  - Qt's 'QQuickGraphicsConfiguration
    &QQuickGraphicsConfiguration::operator=(const QQuickGraphicsConfiguration
    &other)': assignment: Python binds a name and has no operator for it.

  What to expect
  --------------

  - The C++ QQuickGraphicsConfiguration is created at the first use, not by
    'QQuickGraphicsConfiguration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickGraphicsConfiguration back gives a copy the
    ritual made for Python, in a new cute QQuickGraphicsConfiguration.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def preferredInstanceExtensions() -> QList[QByteArray]:
    """
    Calls Qt's 'QByteArrayList
    QQuickGraphicsConfiguration::preferredInstanceExtensions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayList
    #      QQuickGraphicsConfiguration::preferredInstanceExtensions()
    address = Rituals.call(
        'ritual_ZN27QQuickGraphicsConfiguration27preferredInstanceExtension'
        'sEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGraphicsConfiguration'

  #  Qt's '~QQuickGraphicsConfiguration()'. Naming it makes this a value
  #  class: Python owns every C++ QQuickGraphicsConfiguration behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QQuickGraphicsConfigurationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def deviceExtensions(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QByteArrayList
    QQuickGraphicsConfiguration::deviceExtensions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html#deviceExtensions

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayList QQuickGraphicsConfiguration::deviceExtensions() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickGraphicsConfiguration16deviceExtensionsEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  def isDepthBufferEnabledFor2D(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphicsConfiguration::isDepthBufferEnabledFor2D()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html
    """
    #  bool QQuickGraphicsConfiguration::isDepthBufferEnabledFor2D() const
    return self.uglySide.call(
        'ritual_ZNK27QQuickGraphicsConfiguration25isDepthBufferEnabledFor2D'
        'Ev',
    )

  def isDebugLayerEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphicsConfiguration::isDebugLayerEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html
    """
    #  bool QQuickGraphicsConfiguration::isDebugLayerEnabled() const
    return self.uglySide.call(
        'ritual_ZNK27QQuickGraphicsConfiguration19isDebugLayerEnabledEv',
    )

  def isDebugMarkersEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphicsConfiguration::isDebugMarkersEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html
    """
    #  bool QQuickGraphicsConfiguration::isDebugMarkersEnabled() const
    return self.uglySide.call(
        'ritual_ZNK27QQuickGraphicsConfiguration21isDebugMarkersEnabledEv',
    )

  def timestampsEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphicsConfiguration::timestampsEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html#timestampsEnabled
    """
    #  bool QQuickGraphicsConfiguration::timestampsEnabled() const
    return self.uglySide.call(
        'ritual_ZNK27QQuickGraphicsConfiguration17timestampsEnabledEv',
    )

  def prefersSoftwareDevice(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphicsConfiguration::prefersSoftwareDevice()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html
    """
    #  bool QQuickGraphicsConfiguration::prefersSoftwareDevice() const
    return self.uglySide.call(
        'ritual_ZNK27QQuickGraphicsConfiguration21prefersSoftwareDeviceEv',
    )

  def isAutomaticPipelineCacheEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QQuickGraphicsConfiguration::isAutomaticPipelineCacheEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html
    """
    #  bool QQuickGraphicsConfiguration::isAutomaticPipelineCacheEnabled()
    #      const
    return self.uglySide.call(
        'ritual_ZNK27QQuickGraphicsConfiguration31isAutomaticPipelineCacheE'
        'nabledEv',
    )

  def pipelineCacheSaveFile(self) -> str:
    """
    Calls Qt's 'QString QQuickGraphicsConfiguration::pipelineCacheSaveFile()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickGraphicsConfiguration::pipelineCacheSaveFile() const
    return self.uglySide.call(
        'ritual_ZNK27QQuickGraphicsConfiguration21pipelineCacheSaveFileEv',
    )

  def pipelineCacheLoadFile(self) -> str:
    """
    Calls Qt's 'QString QQuickGraphicsConfiguration::pipelineCacheLoadFile()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickGraphicsConfiguration::pipelineCacheLoadFile() const
    return self.uglySide.call(
        'ritual_ZNK27QQuickGraphicsConfiguration21pipelineCacheLoadFileEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QByteArray])
  def setDeviceExtensions(self, extensions: QList[QByteArray]) -> None:
    """
    Calls Qt's 'void QQuickGraphicsConfiguration::setDeviceExtensions(const
    QByteArrayList &extensions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html

    Parameters
    ----------

    extensions : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickGraphicsConfiguration::setDeviceExtensions(const
    #      QByteArrayList &extensions)
    self.uglySide.call(
        'ritual_ZN27QQuickGraphicsConfiguration19setDeviceExtensionsERK5QLi'
        'stI10QByteArrayE',
        self._valueOf(extensions),
    )

  @overload(bool)
  def setDepthBufferFor2D(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphicsConfiguration::setDepthBufferFor2D(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphicsConfiguration::setDepthBufferFor2D(bool enable)
    self.uglySide.call(
        'ritual_ZN27QQuickGraphicsConfiguration19setDepthBufferFor2DEb',
        enable,
    )

  @overload(bool)
  def setDebugLayer(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphicsConfiguration::setDebugLayer(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html#setDebugLayer

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphicsConfiguration::setDebugLayer(bool enable)
    self.uglySide.call(
        'ritual_ZN27QQuickGraphicsConfiguration13setDebugLayerEb', enable,
    )

  @overload(bool)
  def setDebugMarkers(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphicsConfiguration::setDebugMarkers(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html#setDebugMarkers

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphicsConfiguration::setDebugMarkers(bool enable)
    self.uglySide.call(
        'ritual_ZN27QQuickGraphicsConfiguration15setDebugMarkersEb', enable,
    )

  @overload(bool)
  def setTimestamps(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphicsConfiguration::setTimestamps(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html#setTimestamps

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphicsConfiguration::setTimestamps(bool enable)
    self.uglySide.call(
        'ritual_ZN27QQuickGraphicsConfiguration13setTimestampsEb', enable,
    )

  @overload(bool)
  def setPreferSoftwareDevice(self, enable: bool) -> None:
    """
    Calls Qt's 'void
    QQuickGraphicsConfiguration::setPreferSoftwareDevice(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphicsConfiguration::setPreferSoftwareDevice(bool enable)
    self.uglySide.call(
        'ritual_ZN27QQuickGraphicsConfiguration23setPreferSoftwareDeviceEb',
        enable,
    )

  @overload(bool)
  def setAutomaticPipelineCache(self, enable: bool) -> None:
    """
    Calls Qt's 'void
    QQuickGraphicsConfiguration::setAutomaticPipelineCache(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphicsConfiguration::setAutomaticPipelineCache(bool
    #      enable)
    self.uglySide.call(
        'ritual_ZN27QQuickGraphicsConfiguration25setAutomaticPipelineCacheE'
        'b',
        enable,
    )

  @overload(str)
  def setPipelineCacheSaveFile(self, filename: str) -> None:
    """
    Calls Qt's 'void
    QQuickGraphicsConfiguration::setPipelineCacheSaveFile(const QString
    &filename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickGraphicsConfiguration::setPipelineCacheSaveFile(const
    #      QString &filename)
    self.uglySide.call(
        'ritual_ZN27QQuickGraphicsConfiguration24setPipelineCacheSaveFileER'
        'K7QString',
        filename,
    )

  @overload(str)
  def setPipelineCacheLoadFile(self, filename: str) -> None:
    """
    Calls Qt's 'void
    QQuickGraphicsConfiguration::setPipelineCacheLoadFile(const QString
    &filename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickGraphicsConfiguration::setPipelineCacheLoadFile(const
    #      QString &filename)
    self.uglySide.call(
        'ritual_ZN27QQuickGraphicsConfiguration24setPipelineCacheLoadFileER'
        'K7QString',
        filename,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDebug)
  def __rlshift__(self, dbg: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug dbg, const
    QQuickGraphicsConfiguration &config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html#operator<<

    Parameters
    ----------

    dbg : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug dbg, const QQuickGraphicsConfiguration
    #      &config)
    address = Rituals.call(
        'ritual_Zls6QDebugRK27QQuickGraphicsConfiguration',
        CuteMixin._valueOf(dbg), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
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
    'QQuickGraphicsConfiguration::QQuickGraphicsConfiguration()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html
    """
    #  QQuickGraphicsConfiguration::QQuickGraphicsConfiguration()
    self._noteCreation(QQuickGraphicsConfiguration, lambda: Rituals.call(
        'ritual_ZN27QQuickGraphicsConfigurationC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QQuickGraphicsConfiguration) -> None:
    """
    Notes what was given, for Qt's
    'QQuickGraphicsConfiguration::QQuickGraphicsConfiguration(const
    QQuickGraphicsConfiguration &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html

    Parameters
    ----------

    other : QQuickGraphicsConfiguration
      Passed on as a value: Qt reads the C++ QQuickGraphicsConfiguration,
      which stays Python's own.
    """
    #  QQuickGraphicsConfiguration::QQuickGraphicsConfiguration(const
    #      QQuickGraphicsConfiguration &other)
    self._noteCreation(QQuickGraphicsConfiguration, lambda: Rituals.call(
        'ritual_ZN27QQuickGraphicsConfigurationC1ERKS_',
        self._valueOf(other),
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
    Calls Qt's 'void QQuickGraphicsConfiguration::detach()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphicsconfiguration.html#detach
    """
    #  void QQuickGraphicsConfiguration::detach()
    self.uglySide.call('ritual_ZN27QQuickGraphicsConfiguration6detachEv')
