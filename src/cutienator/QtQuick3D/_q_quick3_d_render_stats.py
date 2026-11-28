"""
QQuick3DRenderStats binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3drenderstats_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DRenderStats to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQuick import QQuickWindow
  from ..QtQuick3DRuntimeRender import QSSGRenderLayer, QSSGRhiContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickWindow = WAIT['QQuickWindow']
  QSSGRenderLayer = WAIT['QSSGRenderLayer']
  QSSGRhiContext = WAIT['QSSGRhiContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DRenderStats(QObject):
  """
  The cute side of Qt's QQuick3DRenderStats: a plain Python object standing
  in front of one C++ QQuick3DRenderStats.

  It is built on the cute 'QObject', as Qt's QQuick3DRenderStats is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DRenderStats that has a ritual and that
  Python can call so far, 61 names in all: 'metaObject', 'tr', 'fps',
  'frameTime', 'renderTime', 'renderPrepareTime', 'syncTime', 'maxFrameTime',
  'startSync', 'endSync', 'startRender', 'startRenderPrepare',
  'endRenderPrepare', 'endRender', 'setRhiContext',
  'extendedDataCollectionEnabled', 'setExtendedDataCollectionEnabled',
  'drawCallCount', 'drawVertexCount', 'imageDataSize', 'meshDataSize',
  'renderPassCount', 'renderPassDetails', 'textureDetails', 'meshDetails',
  'pipelineCount', 'materialGenerationTime', 'effectGenerationTime',
  'pipelineCreationTime', 'vmemAllocCount', 'vmemUsedBytes',
  'graphicsApiName', 'lastCompletedGpuTime', 'releaseCachedResources',
  'setWindow', 'fpsChanged', 'frameTimeChanged', 'renderTimeChanged',
  'syncTimeChanged', 'maxFrameTimeChanged',
  'extendedDataCollectionEnabledChanged', 'drawCallCountChanged',
  'drawVertexCountChanged', 'imageDataSizeChanged', 'meshDataSizeChanged',
  'renderPassCountChanged', 'renderPassDetailsChanged',
  'textureDetailsChanged', 'meshDetailsChanged', 'pipelineCountChanged',
  'materialGenerationTimeChanged', 'effectGenerationTimeChanged',
  'pipelineCreationTimeChanged', 'vmemAllocCountChanged',
  'vmemUsedBytesChanged', 'graphicsApiNameChanged',
  'lastCompletedGpuTimeChanged', 'onFrameSwapped', 'timestamp',
  'processRhiContextStats', 'notifyRhiContextStats'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DRenderStats::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DRenderStats::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuick3DRenderStats::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.

  What has no ritual
  ------------------

  2 of the 67 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DRenderStats is created at the first use, not by
    'QQuick3DRenderStats(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DRenderStats.
  - Qt tells when it has removed the C++ QQuick3DRenderStats. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuick3DRenderStats::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drenderstats.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DRenderStats::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuick3DRenderStats2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DRenderStats'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DRenderStats::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DRenderStats::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuick3DRenderStats10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def fps(self) -> int:
    """
    Calls Qt's 'int QQuick3DRenderStats::fps() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drenderstats.html#fps
    """
    #  int QQuick3DRenderStats::fps() const
    return self.uglySide.call('ritual_ZNK19QQuick3DRenderStats3fpsEv')

  def frameTime(self) -> float:
    """
    Calls Qt's 'float QQuick3DRenderStats::frameTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drenderstats.html#frameTime
    """
    #  float QQuick3DRenderStats::frameTime() const
    return self.uglySide.call('ritual_ZNK19QQuick3DRenderStats9frameTimeEv')

  def renderTime(self) -> float:
    """
    Calls Qt's 'float QQuick3DRenderStats::renderTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#renderTime
    """
    #  float QQuick3DRenderStats::renderTime() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DRenderStats10renderTimeEv',
    )

  def renderPrepareTime(self) -> float:
    """
    Calls Qt's 'float QQuick3DRenderStats::renderPrepareTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#renderPrepareTime
    """
    #  float QQuick3DRenderStats::renderPrepareTime() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DRenderStats17renderPrepareTimeEv',
    )

  def syncTime(self) -> float:
    """
    Calls Qt's 'float QQuick3DRenderStats::syncTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drenderstats.html#syncTime
    """
    #  float QQuick3DRenderStats::syncTime() const
    return self.uglySide.call('ritual_ZNK19QQuick3DRenderStats8syncTimeEv')

  def maxFrameTime(self) -> float:
    """
    Calls Qt's 'float QQuick3DRenderStats::maxFrameTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#maxFrameTime
    """
    #  float QQuick3DRenderStats::maxFrameTime() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DRenderStats12maxFrameTimeEv',
    )

  def extendedDataCollectionEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DRenderStats::extendedDataCollectionEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html
    """
    #  bool QQuick3DRenderStats::extendedDataCollectionEnabled() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DRenderStats29extendedDataCollectionEnabledEv',
    )

  def drawCallCount(self) -> int:
    """
    Calls Qt's 'quint64 QQuick3DRenderStats::drawCallCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#drawCallCount
    """
    #  quint64 QQuick3DRenderStats::drawCallCount() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DRenderStats13drawCallCountEv',
    )

  def drawVertexCount(self) -> int:
    """
    Calls Qt's 'quint64 QQuick3DRenderStats::drawVertexCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#drawVertexCount
    """
    #  quint64 QQuick3DRenderStats::drawVertexCount() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DRenderStats15drawVertexCountEv',
    )

  def imageDataSize(self) -> int:
    """
    Calls Qt's 'quint64 QQuick3DRenderStats::imageDataSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#imageDataSize
    """
    #  quint64 QQuick3DRenderStats::imageDataSize() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DRenderStats13imageDataSizeEv',
    )

  def meshDataSize(self) -> int:
    """
    Calls Qt's 'quint64 QQuick3DRenderStats::meshDataSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#meshDataSize
    """
    #  quint64 QQuick3DRenderStats::meshDataSize() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DRenderStats12meshDataSizeEv',
    )

  def renderPassCount(self) -> int:
    """
    Calls Qt's 'int QQuick3DRenderStats::renderPassCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#renderPassCount
    """
    #  int QQuick3DRenderStats::renderPassCount() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DRenderStats15renderPassCountEv',
    )

  def renderPassDetails(self) -> str:
    """
    Calls Qt's 'QString QQuick3DRenderStats::renderPassDetails() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#renderPassDetails

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DRenderStats::renderPassDetails() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DRenderStats17renderPassDetailsEv',
    )

  def textureDetails(self) -> str:
    """
    Calls Qt's 'QString QQuick3DRenderStats::textureDetails() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#textureDetails

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DRenderStats::textureDetails() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DRenderStats14textureDetailsEv',
    )

  def meshDetails(self) -> str:
    """
    Calls Qt's 'QString QQuick3DRenderStats::meshDetails() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#meshDetails

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DRenderStats::meshDetails() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DRenderStats11meshDetailsEv',
    )

  def pipelineCount(self) -> int:
    """
    Calls Qt's 'int QQuick3DRenderStats::pipelineCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#pipelineCount
    """
    #  int QQuick3DRenderStats::pipelineCount() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DRenderStats13pipelineCountEv',
    )

  def materialGenerationTime(self) -> int:
    """
    Calls Qt's 'qint64 QQuick3DRenderStats::materialGenerationTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#materialGenerationTime
    """
    #  qint64 QQuick3DRenderStats::materialGenerationTime() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DRenderStats22materialGenerationTimeEv',
    )

  def effectGenerationTime(self) -> int:
    """
    Calls Qt's 'qint64 QQuick3DRenderStats::effectGenerationTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#effectGenerationTime
    """
    #  qint64 QQuick3DRenderStats::effectGenerationTime() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DRenderStats20effectGenerationTimeEv',
    )

  def pipelineCreationTime(self) -> int:
    """
    Calls Qt's 'qint64 QQuick3DRenderStats::pipelineCreationTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#pipelineCreationTime
    """
    #  qint64 QQuick3DRenderStats::pipelineCreationTime() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DRenderStats20pipelineCreationTimeEv',
    )

  def vmemAllocCount(self) -> int:
    """
    Calls Qt's 'quint32 QQuick3DRenderStats::vmemAllocCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#vmemAllocCount
    """
    #  quint32 QQuick3DRenderStats::vmemAllocCount() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DRenderStats14vmemAllocCountEv',
    )

  def vmemUsedBytes(self) -> int:
    """
    Calls Qt's 'quint64 QQuick3DRenderStats::vmemUsedBytes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#vmemUsedBytes
    """
    #  quint64 QQuick3DRenderStats::vmemUsedBytes() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DRenderStats13vmemUsedBytesEv',
    )

  def graphicsApiName(self) -> str:
    """
    Calls Qt's 'QString QQuick3DRenderStats::graphicsApiName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#graphicsApiName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DRenderStats::graphicsApiName() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DRenderStats15graphicsApiNameEv',
    )

  def lastCompletedGpuTime(self) -> float:
    """
    Calls Qt's 'float QQuick3DRenderStats::lastCompletedGpuTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#lastCompletedGpuTime
    """
    #  float QQuick3DRenderStats::lastCompletedGpuTime() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DRenderStats20lastCompletedGpuTimeEv',
    )

  def timestamp(self) -> float:
    """
    Calls Qt's 'float QQuick3DRenderStats::timestamp() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drenderstats.html#timestamp
    """
    #  float QQuick3DRenderStats::timestamp() const
    return self.uglySide.call('ritual_ZNK19QQuick3DRenderStats9timestampEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSSGRhiContext, QSSGRenderLayer)
  @overload(QSSGRhiContext, NoneType)
  @overload(NoneType, QSSGRenderLayer)
  @overload(NoneType, NoneType)
  def setRhiContext(
      self,
      ctx: Optional[QSSGRhiContext],
      layer: Optional[QSSGRenderLayer],
  ) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::setRhiContext(QSSGRhiContext *ctx,
    QSSGRenderLayer *layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#setRhiContext

    Parameters
    ----------

    ctx : Optional[QSSGRhiContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    layer : Optional[QSSGRenderLayer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DRenderStats::setRhiContext(QSSGRhiContext *ctx,
    #      QSSGRenderLayer *layer)
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats13setRhiContextEP14QSSGRhiContextP15'
        'QSSGRenderLayer',
        self._addressOf(ctx), self._addressOf(layer),
    )

  @overload(bool)
  def setExtendedDataCollectionEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void
    QQuick3DRenderStats::setExtendedDataCollectionEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuick3DRenderStats::setExtendedDataCollectionEnabled(bool
    #      enable)
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats32setExtendedDataCollectionEnabledEb',
        enable,
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def setWindow(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::setWindow(QQuickWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drenderstats.html#setWindow

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DRenderStats::setWindow(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats9setWindowEP12QQuickWindow',
        self._addressOf(window),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DRenderStats::QQuick3DRenderStats(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#QQuick3DRenderStats

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DRenderStats::QQuick3DRenderStats(QObject *parent)
    self._noteCreation(QQuick3DRenderStats, lambda: Rituals.call(
        'ritual_ZN19QQuick3DRenderStatsC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def startSync(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::startSync()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drenderstats.html#startSync
    """
    #  void QQuick3DRenderStats::startSync()
    self.uglySide.call('ritual_ZN19QQuick3DRenderStats9startSyncEv')

  @overload()
  @overload(bool)
  def endSync(self, dump: bool = False) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::endSync(bool dump)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drenderstats.html#endSync

    Parameters
    ----------

    dump : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuick3DRenderStats::endSync(bool dump)
    self.uglySide.call('ritual_ZN19QQuick3DRenderStats7endSyncEb', dump)

  def startRender(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::startRender()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#startRender
    """
    #  void QQuick3DRenderStats::startRender()
    self.uglySide.call('ritual_ZN19QQuick3DRenderStats11startRenderEv')

  def startRenderPrepare(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::startRenderPrepare()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#startRenderPrepare
    """
    #  void QQuick3DRenderStats::startRenderPrepare()
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats18startRenderPrepareEv',
    )

  def endRenderPrepare(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::endRenderPrepare()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#endRenderPrepare
    """
    #  void QQuick3DRenderStats::endRenderPrepare()
    self.uglySide.call('ritual_ZN19QQuick3DRenderStats16endRenderPrepareEv')

  @overload()
  @overload(bool)
  def endRender(self, dump: bool = False) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::endRender(bool dump)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drenderstats.html#endRender

    Parameters
    ----------

    dump : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuick3DRenderStats::endRender(bool dump)
    self.uglySide.call('ritual_ZN19QQuick3DRenderStats9endRenderEb', dump)

  def releaseCachedResources(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::releaseCachedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#releaseCachedResources
    """
    #  void QQuick3DRenderStats::releaseCachedResources()
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats22releaseCachedResourcesEv',
    )

  def fpsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::fpsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#fpsChanged
    """
    #  void QQuick3DRenderStats::fpsChanged()
    self.uglySide.call('ritual_ZN19QQuick3DRenderStats10fpsChangedEv')

  def frameTimeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::frameTimeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#frameTimeChanged
    """
    #  void QQuick3DRenderStats::frameTimeChanged()
    self.uglySide.call('ritual_ZN19QQuick3DRenderStats16frameTimeChangedEv')

  def renderTimeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::renderTimeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#renderTimeChanged
    """
    #  void QQuick3DRenderStats::renderTimeChanged()
    self.uglySide.call('ritual_ZN19QQuick3DRenderStats17renderTimeChangedEv')

  def syncTimeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::syncTimeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#syncTimeChanged
    """
    #  void QQuick3DRenderStats::syncTimeChanged()
    self.uglySide.call('ritual_ZN19QQuick3DRenderStats15syncTimeChangedEv')

  def maxFrameTimeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::maxFrameTimeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#maxFrameTimeChanged
    """
    #  void QQuick3DRenderStats::maxFrameTimeChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats19maxFrameTimeChangedEv',
    )

  def extendedDataCollectionEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DRenderStats::extendedDataCollectionEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html
    """
    #  void QQuick3DRenderStats::extendedDataCollectionEnabledChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats36extendedDataCollectionEnabledChang'
        'edEv',
    )

  def drawCallCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::drawCallCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#drawCallCountChanged
    """
    #  void QQuick3DRenderStats::drawCallCountChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats20drawCallCountChangedEv',
    )

  def drawVertexCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::drawVertexCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#drawVertexCountChanged
    """
    #  void QQuick3DRenderStats::drawVertexCountChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats22drawVertexCountChangedEv',
    )

  def imageDataSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::imageDataSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#imageDataSizeChanged
    """
    #  void QQuick3DRenderStats::imageDataSizeChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats20imageDataSizeChangedEv',
    )

  def meshDataSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::meshDataSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#meshDataSizeChanged
    """
    #  void QQuick3DRenderStats::meshDataSizeChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats19meshDataSizeChangedEv',
    )

  def renderPassCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::renderPassCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#renderPassCountChanged
    """
    #  void QQuick3DRenderStats::renderPassCountChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats22renderPassCountChangedEv',
    )

  def renderPassDetailsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::renderPassDetailsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#renderPassDetailsChanged
    """
    #  void QQuick3DRenderStats::renderPassDetailsChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats24renderPassDetailsChangedEv',
    )

  def textureDetailsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::textureDetailsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#textureDetailsChanged
    """
    #  void QQuick3DRenderStats::textureDetailsChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats21textureDetailsChangedEv',
    )

  def meshDetailsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::meshDetailsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#meshDetailsChanged
    """
    #  void QQuick3DRenderStats::meshDetailsChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats18meshDetailsChangedEv',
    )

  def pipelineCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::pipelineCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#pipelineCountChanged
    """
    #  void QQuick3DRenderStats::pipelineCountChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats20pipelineCountChangedEv',
    )

  def materialGenerationTimeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::materialGenerationTimeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html
    """
    #  void QQuick3DRenderStats::materialGenerationTimeChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats29materialGenerationTimeChangedEv',
    )

  def effectGenerationTimeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::effectGenerationTimeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html
    """
    #  void QQuick3DRenderStats::effectGenerationTimeChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats27effectGenerationTimeChangedEv',
    )

  def pipelineCreationTimeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::pipelineCreationTimeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html
    """
    #  void QQuick3DRenderStats::pipelineCreationTimeChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats27pipelineCreationTimeChangedEv',
    )

  def vmemAllocCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::vmemAllocCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#vmemAllocCountChanged
    """
    #  void QQuick3DRenderStats::vmemAllocCountChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats21vmemAllocCountChangedEv',
    )

  def vmemUsedBytesChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::vmemUsedBytesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#vmemUsedBytesChanged
    """
    #  void QQuick3DRenderStats::vmemUsedBytesChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats20vmemUsedBytesChangedEv',
    )

  def graphicsApiNameChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::graphicsApiNameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#graphicsApiNameChanged
    """
    #  void QQuick3DRenderStats::graphicsApiNameChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats22graphicsApiNameChangedEv',
    )

  def lastCompletedGpuTimeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::lastCompletedGpuTimeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html
    """
    #  void QQuick3DRenderStats::lastCompletedGpuTimeChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats27lastCompletedGpuTimeChangedEv',
    )

  def onFrameSwapped(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::onFrameSwapped()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#onFrameSwapped
    """
    #  void QQuick3DRenderStats::onFrameSwapped()
    self.uglySide.call('ritual_ZN19QQuick3DRenderStats14onFrameSwappedEv')

  def processRhiContextStats(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::processRhiContextStats()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#processRhiContextStats
    """
    #  void QQuick3DRenderStats::processRhiContextStats()
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats22processRhiContextStatsEv',
    )

  def notifyRhiContextStats(self) -> None:
    """
    Calls Qt's 'void QQuick3DRenderStats::notifyRhiContextStats()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drenderstats.html#notifyRhiContextStats
    """
    #  void QQuick3DRenderStats::notifyRhiContextStats()
    self.uglySide.call(
        'ritual_ZN19QQuick3DRenderStats21notifyRhiContextStatsEv',
    )
