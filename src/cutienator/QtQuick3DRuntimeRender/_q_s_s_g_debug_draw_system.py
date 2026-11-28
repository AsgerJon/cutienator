"""
QSSGDebugDrawSystem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgdebugdrawsystem_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGDebugDrawSystem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QColor, QRhiRenderPassDescriptor
  from ..QtGui import QRhiResourceUpdateBatch, QRhiShaderResourceBindings
  from ..QtGui import QVector3D
  from ..QtQuick3DUtils import QSSGBounds3
  from . import QSSGRhiContext, QSSGRhiGraphicsPipelineState
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QRhiRenderPassDescriptor = WAIT['QRhiRenderPassDescriptor']
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']
  QRhiShaderResourceBindings = WAIT['QRhiShaderResourceBindings']
  QSSGBounds3 = WAIT['QSSGBounds3']
  QSSGRhiContext = WAIT['QSSGRhiContext']
  QSSGRhiGraphicsPipelineState = WAIT['QSSGRhiGraphicsPipelineState']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGDebugDrawSystem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGDebugDrawSystem: a plain Python object standing
  in front of one C++ QSSGDebugDrawSystem.

  What exists
  -----------

  Every function of Qt's QSSGDebugDrawSystem that has a ritual and that
  Python can call so far, 9 names in all: 'hasContent', 'drawLine',
  'drawBounds', 'drawPoint', 'prepareGeometry', 'recordRenderDebugObjects',
  'setEnabled', 'isEnabled', 'levelOfDetailColor'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGDebugDrawSystem::~QSSGDebugDrawSystem()': the destructor:
    Python never removes a C++ QSSGDebugDrawSystem.
  - Qt's 'void QSSGDebugDrawSystem::generateLine(const LineData &line,
    QVector<VertexData> &vertexArray, QVector<quint32> &indexArray)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QSSGDebugDrawSystem::generateBox(const BoundsData &bounds,
    QVector<VertexData> &vertexArray, QVector<quint32> &indexArray)': takes a
    type Python has no way to hand over yet.
  - Qt's 'bool QSSGDebugDrawSystem::isEnabled(Mode mode) const': names the
    enum 'QSSGDebugDrawSystem::Mode', whose class cannot be named here.
  - Qt's 'void QSSGDebugDrawSystem::debugNormals(QSSGBufferManager
    &bufferManager, const QSSGModelContext &theModelContext, const
    QSSGRenderSubset &theSubset, quint32 subsetLevelOfDetail, float
    lineLength)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QSSGDebugDrawSystem is created at the first use, not by
    'QSSGDebugDrawSystem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGDebugDrawSystem.
  - Each name of Qt's QSSGDebugDrawSystem that has no cute function yet,
    'debugNormals', 'generateBox', 'generateLine', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def levelOfDetailColor(lod: int) -> QColor:
    """
    Calls Qt's 'QColor QSSGDebugDrawSystem::levelOfDetailColor(quint32 lod)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgdebugdrawsystem.html#levelOfDetailColor

    Parameters
    ----------

    lod : int
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QSSGDebugDrawSystem::levelOfDetailColor(quint32 lod)
    address = Rituals.call(
        'ritual_ZN19QSSGDebugDrawSystem18levelOfDetailColorEj', lod,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGDebugDrawSystem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasContent(self) -> bool:
    """
    Calls Qt's 'bool QSSGDebugDrawSystem::hasContent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgdebugdrawsystem.html#hasContent
    """
    #  bool QSSGDebugDrawSystem::hasContent() const
    return self.uglySide.call(
        'ritual_ZNK19QSSGDebugDrawSystem10hasContentEv',
    )

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGDebugDrawSystem::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgdebugdrawsystem.html#isEnabled
    """
    #  bool QSSGDebugDrawSystem::isEnabled() const
    return self.uglySide.call('ritual_ZNK19QSSGDebugDrawSystem9isEnabledEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, v: bool) -> None:
    """
    Calls Qt's 'void QSSGDebugDrawSystem::setEnabled(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgdebugdrawsystem.html#setEnabled

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QSSGDebugDrawSystem::setEnabled(bool v)
    self.uglySide.call('ritual_ZN19QSSGDebugDrawSystem10setEnabledEb', v)

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
    'QSSGDebugDrawSystem::QSSGDebugDrawSystem()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgdebugdrawsystem.html#QSSGDebugDrawSystem
    """
    #  QSSGDebugDrawSystem::QSSGDebugDrawSystem()
    self._noteCreation(QSSGDebugDrawSystem, lambda: Rituals.call(
        'ritual_ZN19QSSGDebugDrawSystemC1Ev',
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

  @overload(QVector3D, QVector3D, QColor)
  @overload(QVector3D, QVector3D, QColor, bool)
  def drawLine(
      self,
      startPoint: QVector3D,
      endPoint: QVector3D,
      color: QColor,
      isPersistent: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QSSGDebugDrawSystem::drawLine(const QVector3D
    &startPoint, const QVector3D &endPoint, const QColor &color, bool
    isPersistent)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgdebugdrawsystem.html#drawLine

    Parameters
    ----------

    startPoint : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    endPoint : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    isPersistent : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QSSGDebugDrawSystem::drawLine(const QVector3D &startPoint, const
    #      QVector3D &endPoint, const QColor &color, bool isPersistent)
    self.uglySide.call(
        'ritual_ZN19QSSGDebugDrawSystem8drawLineERK9QVector3DS2_RK6QColorb',
        self._valueOf(startPoint), self._valueOf(endPoint),
        self._valueOf(color), isPersistent,
    )

  @overload(QSSGBounds3, QColor)
  @overload(QSSGBounds3, QColor, bool)
  def drawBounds(
      self,
      bounds: QSSGBounds3,
      color: QColor,
      isPersistent: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QSSGDebugDrawSystem::drawBounds(const QSSGBounds3
    &bounds, const QColor &color, bool isPersistent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgdebugdrawsystem.html#drawBounds

    Parameters
    ----------

    bounds : QSSGBounds3
      Passed on as a value: Qt reads the C++ QSSGBounds3, which stays
      Python's own.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    isPersistent : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QSSGDebugDrawSystem::drawBounds(const QSSGBounds3 &bounds, const
    #      QColor &color, bool isPersistent)
    self.uglySide.call(
        'ritual_ZN19QSSGDebugDrawSystem10drawBoundsERK11QSSGBounds3RK6QColo'
        'rb',
        self._valueOf(bounds), self._valueOf(color), isPersistent,
    )

  @overload(QVector3D, QColor)
  @overload(QVector3D, QColor, bool)
  def drawPoint(
      self,
      vertex: QVector3D,
      color: QColor,
      isPersistent: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QSSGDebugDrawSystem::drawPoint(const QVector3D &vertex,
    const QColor &color, bool isPersistent)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgdebugdrawsystem.html#drawPoint

    Parameters
    ----------

    vertex : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    isPersistent : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QSSGDebugDrawSystem::drawPoint(const QVector3D &vertex, const
    #      QColor &color, bool isPersistent)
    self.uglySide.call(
        'ritual_ZN19QSSGDebugDrawSystem9drawPointERK9QVector3DRK6QColorb',
        self._valueOf(vertex), self._valueOf(color), isPersistent,
    )

  @overload(QSSGRhiContext, QRhiResourceUpdateBatch)
  @overload(QSSGRhiContext, NoneType)
  @overload(NoneType, QRhiResourceUpdateBatch)
  @overload(NoneType, NoneType)
  def prepareGeometry(
      self,
      rhiCtx: Optional[QSSGRhiContext],
      rub: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void QSSGDebugDrawSystem::prepareGeometry(QSSGRhiContext
    *rhiCtx, QRhiResourceUpdateBatch *rub)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgdebugdrawsystem.html#prepareGeometry

    Parameters
    ----------

    rhiCtx : Optional[QSSGRhiContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rub : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGDebugDrawSystem::prepareGeometry(QSSGRhiContext *rhiCtx,
    #      QRhiResourceUpdateBatch *rub)
    self.uglySide.call(
        'ritual_ZN19QSSGDebugDrawSystem15prepareGeometryEP14QSSGRhiContextP'
        '23QRhiResourceUpdateBatch',
        self._addressOf(rhiCtx), self._addressOf(rub),
    )

  @overload(
      QSSGRhiContext, QSSGRhiGraphicsPipelineState,
      QRhiShaderResourceBindings, QRhiRenderPassDescriptor,
  )
  @overload(
      QSSGRhiContext, QSSGRhiGraphicsPipelineState,
      QRhiShaderResourceBindings, NoneType,
  )
  @overload(
      QSSGRhiContext, QSSGRhiGraphicsPipelineState, NoneType,
      QRhiRenderPassDescriptor,
  )
  @overload(QSSGRhiContext, QSSGRhiGraphicsPipelineState, NoneType, NoneType)
  @overload(
      QSSGRhiContext, NoneType, QRhiShaderResourceBindings,
      QRhiRenderPassDescriptor,
  )
  @overload(QSSGRhiContext, NoneType, QRhiShaderResourceBindings, NoneType)
  @overload(QSSGRhiContext, NoneType, NoneType, QRhiRenderPassDescriptor)
  @overload(QSSGRhiContext, NoneType, NoneType, NoneType)
  @overload(
      NoneType, QSSGRhiGraphicsPipelineState, QRhiShaderResourceBindings,
      QRhiRenderPassDescriptor,
  )
  @overload(
      NoneType, QSSGRhiGraphicsPipelineState, QRhiShaderResourceBindings,
      NoneType,
  )
  @overload(
      NoneType, QSSGRhiGraphicsPipelineState, NoneType,
      QRhiRenderPassDescriptor,
  )
  @overload(NoneType, QSSGRhiGraphicsPipelineState, NoneType, NoneType)
  @overload(
      NoneType, NoneType, QRhiShaderResourceBindings,
      QRhiRenderPassDescriptor,
  )
  @overload(NoneType, NoneType, QRhiShaderResourceBindings, NoneType)
  @overload(NoneType, NoneType, NoneType, QRhiRenderPassDescriptor)
  @overload(NoneType, NoneType, NoneType, NoneType)
  def recordRenderDebugObjects(
      self,
      rhiCtx: Optional[QSSGRhiContext],
      ps: Optional[QSSGRhiGraphicsPipelineState],
      srb: Optional[QRhiShaderResourceBindings],
      rpDesc: Optional[QRhiRenderPassDescriptor],
  ) -> None:
    """
    Calls Qt's 'void
    QSSGDebugDrawSystem::recordRenderDebugObjects(QSSGRhiContext *rhiCtx,
    QSSGRhiGraphicsPipelineState *ps, QRhiShaderResourceBindings *srb,
    QRhiRenderPassDescriptor *rpDesc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgdebugdrawsystem.html#recordRenderDebugObjects

    Parameters
    ----------

    rhiCtx : Optional[QSSGRhiContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ps : Optional[QSSGRhiGraphicsPipelineState]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    srb : Optional[QRhiShaderResourceBindings]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rpDesc : Optional[QRhiRenderPassDescriptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGDebugDrawSystem::recordRenderDebugObjects(QSSGRhiContext
    #      *rhiCtx, QSSGRhiGraphicsPipelineState *ps,
    #      QRhiShaderResourceBindings *srb, QRhiRenderPassDescriptor *rpDesc)
    self.uglySide.call(
        'ritual_ZN19QSSGDebugDrawSystem24recordRenderDebugObjectsEP14QSSGRh'
        'iContextP28QSSGRhiGraphicsPipelineStateP26QRhiShaderResourceBindin'
        'gsP24QRhiRenderPassDescriptor',
        self._addressOf(rhiCtx), self._addressOf(ps), self._addressOf(srb),
        self._addressOf(rpDesc),
    )

  @staticmethod
  def debugNormals(*__, **_) -> Never:
    """
    Qt's 'void QSSGDebugDrawSystem::debugNormals(QSSGBufferManager
    &bufferManager, const QSSGModelContext &theModelContext, const
    QSSGRenderSubset &theSubset, quint32 subsetLevelOfDetail, float
    lineLength)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGDebugDrawSystem.debugNormals' has no cute function yet. Qt's "
        "'void QSSGDebugDrawSystem::debugNormals(QSSGBufferManager "
        "&bufferManager, const QSSGModelContext &theModelContext, const "
        "QSSGRenderSubset &theSubset, quint32 subsetLevelOfDetail, float "
        "lineLength)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def generateBox(*__, **_) -> Never:
    """
    Qt's 'void QSSGDebugDrawSystem::generateBox(const BoundsData &bounds,
    QVector<VertexData> &vertexArray, QVector<quint32> &indexArray)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGDebugDrawSystem.generateBox' has no cute function yet. Qt's "
        "'void QSSGDebugDrawSystem::generateBox(const BoundsData &bounds, "
        "QVector<VertexData> &vertexArray, QVector<quint32> &indexArray)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def generateLine(*__, **_) -> Never:
    """
    Qt's 'void QSSGDebugDrawSystem::generateLine(const LineData &line,
    QVector<VertexData> &vertexArray, QVector<quint32> &indexArray)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGDebugDrawSystem.generateLine' has no cute function yet. Qt's "
        "'void QSSGDebugDrawSystem::generateLine(const LineData &line, "
        "QVector<VertexData> &vertexArray, QVector<quint32> &indexArray)': "
        "takes a type Python has no way to hand over yet.")
