"""
QQuickGraphsSurface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qquickgraphssurface_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickGraphsSurface to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from ..QtQuick import QQuickItem
from . import QtGraphs3D, QAbstract3DAxis, QAbstract3DSeries
from . import QQuickGraphsItem
from ..QtQuick3D import QQuick3DViewport

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint, QPointF, QUrl
  from ..QtGui import QImage, QVector3D
  from . import QSurface3DSeries, QSurfaceDataItem, QValue3DAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QSurface3DSeries = WAIT['QtGraphs:QSurface3DSeries']
  QSurfaceDataItem = WAIT['QtGraphs:QSurfaceDataItem']
  QUrl = WAIT['QUrl']
  QValue3DAxis = WAIT['QtGraphs:QValue3DAxis']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGraphsSurface(QQuickGraphsItem):
  """
  The cute side of Qt's QQuickGraphsSurface: a plain Python object standing
  in front of one C++ QQuickGraphsSurface.

  It is built on the cute 'QQuickGraphsItem', as Qt's QQuickGraphsSurface is
  built on Qt's QQuickGraphsItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickGraphsSurface that has a ritual and that
  Python can call so far, 94 names in all: 'metaObject', 'tr', 'setAxisX',
  'axisX', 'setAxisY', 'axisY', 'setAxisZ', 'axisZ', 'addSeries',
  'removeSeries', 'clearSelection', 'setFlipHorizontalGrid',
  'flipHorizontalGrid', 'isFlatShadingSupported', 'surfaceSeriesList',
  'updateSurfaceTexture', 'invalidSelectionPosition', 'setSelectedPoint',
  'selectedSeries', 'setSelectionMode', 'setDataDimensions',
  'dataDimensions', 'hasChangedSeriesList', 'isSeriesVisibilityDirty',
  'setSeriesVisibilityDirty', 'isDataDirty', 'setDataDirty',
  'isSeriesVisualsDirty', 'setSeriesVisualsDirty', 'isIndexDirty',
  'setIndexDirty', 'changedSeriesList', 'isSelectedPointChanged',
  'setSelectedPointChanged', 'isFlipHorizontalGridChanged',
  'setFlipHorizontalGridChanged', 'isSurfaceTextureChanged',
  'setSurfaceTextureChanged', 'isChangedTexturesEmpty',
  'hasSeriesToChangeTexture',
  'handleAxisAutoAdjustRangeChangedInOrientation',
  'handleAxisRangeChangedBySender', 'handleSeriesVisibilityChangedBySender',
  'handleItemLabelVisibleChangedBySender', 'adjustAxisRanges',
  'handleMultiAxisChanged', 'handleLightingModeChanged',
  'renderSliceToImage', 'componentComplete', 'synchData', 'updateGraph',
  'calculateSceneScalingFactors', 'toggleSliceGraph',
  'updateSingleHighlightColor', 'updateLightStrength',
  'handleThemeTypeChange', 'doPicking', 'doRayPicking', 'getSeriesMultiAxis',
  'createSliceView', 'updateSliceItemLabel', 'updateSelectionMode',
  'createOffscreenSliceView', 'handleAxisXChanged', 'handleAxisYChanged',
  'handleAxisZChanged', 'handleShadingChanged',
  'handleWireframeColorChanged', 'handleFlipHorizontalGridChanged',
  'handleArrayReset', 'handleRowsAdded', 'handleRowsChanged',
  'handleRowsRemoved', 'handleRowsInserted', 'handleItemChanged',
  'handleFlatShadingSupportedChange', 'axisXChanged', 'axisYChanged',
  'axisZChanged', 'selectedSeriesChanged', 'flipHorizontalGridChanged',
  'sliceImageChanged', 'getNormalizedVertex', 'handleChangedSeries',
  'updateSelectedPoint', 'addModel', 'handleMeshTypeChanged',
  'handlePointerChanged', 'changePointerMeshTypeForSeries',
  'changePointerForSeries', 'changeSlicePointerMeshTypeForSeries',
  'changeSlicePointerForSeries', 'getMeshFileName', 'intersectWithAABB'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGraphsSurface::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickGraphsSurface::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickGraphsSurface::~QQuickGraphsSurface()': the destructor:
    Python never removes a C++ QQuickGraphsSurface.
  - Qt's 'QQmlListProperty<QSurface3DSeries>
    QQuickGraphsSurface::seriesList()': gives a type Python has no way to
    take yet.
  - Qt's 'void
    QQuickGraphsSurface::appendSeriesFunc(QQmlListProperty<QSurface3DSeries>
    *list, QSurface3DSeries *series)': names
    'QQmlListProperty<QSurface3DSeries>', which has no cute class yet.
  - Qt's 'qsizetype
    QQuickGraphsSurface::countSeriesFunc(QQmlListProperty<QSurface3DSeries>
    *list)': names 'QQmlListProperty<QSurface3DSeries>', which has no cute
    class yet.
  - Qt's 'QSurface3DSeries
    *QQuickGraphsSurface::atSeriesFunc(QQmlListProperty<QSurface3DSeries>
    *list, qsizetype index)': names 'QQmlListProperty<QSurface3DSeries>',
    which has no cute class yet.
  - Qt's 'void
    QQuickGraphsSurface::clearSeriesFunc(QQmlListProperty<QSurface3DSeries>
    *list)': names 'QQmlListProperty<QSurface3DSeries>', which has no cute
    class yet.
  - Qt's 'QRect QQuickGraphsSurface::calculateSampleSpace(SurfaceModel
    *model, const QSurfaceDataArray &array)': names
    'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.
  - Qt's 'QPointF QQuickGraphsSurface::mapCoordsToWorldSpace(SurfaceModel
    *model, QPointF coords)': names 'QQuickGraphsSurface::SurfaceModel',
    which has no cute class yet.
  - Qt's 'QPoint QQuickGraphsSurface::mapCoordsToSampleSpace(SurfaceModel
    *model, QPointF coords)': names 'QQuickGraphsSurface::SurfaceModel',
    which has no cute class yet.
  - Qt's 'void QQuickGraphsSurface::createIndices(SurfaceModel *model,
    qsizetype columnCount, qsizetype rowCount)': names
    'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.
  - Qt's 'void QQuickGraphsSurface::createLineIndices(SurfaceModel *model,
    qsizetype pointCount)': names 'QQuickGraphsSurface::SurfaceModel', which
    has no cute class yet.
  - Qt's 'void QQuickGraphsSurface::createGridlineIndices(SurfaceModel
    *model, qsizetype x, qsizetype y, qsizetype endX, qsizetype endY)': names
    'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.
  - Qt's 'void QQuickGraphsSurface::updateModel(SurfaceModel *model)': names
    'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.
  - Qt's 'void QQuickGraphsSurface::updateFill(SurfaceModel *model)': names
    'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.
  - Qt's 'void QQuickGraphsSurface::updateLineFill(SurfaceModel *model)':
    names 'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.
  - Qt's 'void QQuickGraphsSurface::updateMaterial(SurfaceModel *model)':
    names 'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.
  - Qt's 'void QQuickGraphsSurface::addFillModel(SurfaceModel *model)': names
    'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.
  - Qt's 'void QQuickGraphsSurface::addSliceModel(SurfaceModel *model)':
    names 'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.
  - Qt's 'QSurfaceDataArray QQuickGraphsSurface::removeNaNRows(const
    QSurfaceDataArray &array)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QVector3D QQuickGraphsSurface::triangleIntersection(QVector3D
    origin, QVector3D dir, const std::array<QVector3D, 3> &triangle)': takes
    a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 121 functions Qt declares: 2 not a gap; 1 takes or gives a type
  that cannot be passed yet.

  What to expect
  --------------

  - The C++ QQuickGraphsSurface is created at the first use, not by
    'QQuickGraphsSurface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGraphsSurface.
  - Qt tells when it has removed the C++ QQuickGraphsSurface. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickGraphsSurface that has no cute function yet,
    'addFillModel', 'addSliceModel', 'appendSeriesFunc', 'atSeriesFunc',
    'calculateSampleSpace', 'clearSeriesFunc', 'countSeriesFunc',
    'createGridlineIndices', 'createIndices', 'createLineIndices',
    'mapCoordsToSampleSpace', 'mapCoordsToWorldSpace', 'pickSurfaces',
    'removeNaNRows', 'triangleIntersection', 'updateFill', 'updateLineFill',
    'updateMaterial', 'updateModel', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickGraphsSurface, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class DataDimension(CuteFlags):
    """
    The flags enum 'QQuickGraphsSurface::DataDimension' of Qt, with the 4
    names Qt gives in it. Qt names the type of its combinations
    'QQuickGraphsSurface::DataDimensions'.
    """

    BothAscending = 0x0
    XDescending = 0x1
    ZDescending = 0x2
    BothDescending = 0x3

  DataDimensions = DataDimension

  #  The classes Qt writes inside QQuickGraphsSurface, each a class in here
  #  as in C++.

  class ChangeItem(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickGraphsSurface::ChangeItem: a plain Python
    object standing in front of one C++ QQuickGraphsSurface::ChangeItem.

    C++ hands a QQuickGraphsSurface::ChangeItem around as a copy, so every
    C++ QQuickGraphsSurface::ChangeItem behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQuickGraphsSurface::ChangeItem yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickGraphsSurface::ChangeItem::~ChangeItem()': the destructor:
      Python removes its C++ QQuickGraphsSurface::ChangeItem by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QQuickGraphsSurface::ChangeItem is created at the first use,
      not by 'QQuickGraphsSurface::ChangeItem(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickGraphsSurface::ChangeItem back gives a copy
      the ritual made for Python, in a new cute
      QQuickGraphsSurface::ChangeItem.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickGraphsSurface::ChangeItem'

    #  Qt's '~QQuickGraphsSurface::ChangeItem()'. Naming it makes this a
    #  value class: Python owns every C++ QQuickGraphsSurface::ChangeItem
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN19QQuickGraphsSurface10ChangeItemD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class ChangeRow(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickGraphsSurface::ChangeRow: a plain Python
    object standing in front of one C++ QQuickGraphsSurface::ChangeRow.

    C++ hands a QQuickGraphsSurface::ChangeRow around as a copy, so every C++
    QQuickGraphsSurface::ChangeRow behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQuickGraphsSurface::ChangeRow yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickGraphsSurface::ChangeRow::~ChangeRow()': the destructor:
      Python removes its C++ QQuickGraphsSurface::ChangeRow by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQuickGraphsSurface::ChangeRow is created at the first use, not
      by 'QQuickGraphsSurface::ChangeRow(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickGraphsSurface::ChangeRow back gives a copy
      the ritual made for Python, in a new cute
      QQuickGraphsSurface::ChangeRow.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickGraphsSurface::ChangeRow'

    #  Qt's '~QQuickGraphsSurface::ChangeRow()'. Naming it makes this a value
    #  class: Python owns every C++ QQuickGraphsSurface::ChangeRow behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN19QQuickGraphsSurface9ChangeRowD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Calls Qt's 'QString QQuickGraphsSurface::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphssurface.html#tr

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
    #  QString QQuickGraphsSurface::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickGraphsSurface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def invalidSelectionPosition() -> QPoint:
    """
    Calls Qt's 'QPoint QQuickGraphsSurface::invalidSelectionPosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#invalidSelectionPosition

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QQuickGraphsSurface::invalidSelectionPosition()
    address = Rituals.call(
        'ritual_ZN19QQuickGraphsSurface24invalidSelectionPositionEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGraphsSurface'

  #  A C++ QQuickGraphsSurface Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickGraphsSurface'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGraphsSurface::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGraphsSurface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickGraphsSurface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def axisX(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QQuickGraphsSurface::axisX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphssurface.html#axisX

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QQuickGraphsSurface::axisX() const
    address = self.uglySide.call('ritual_ZNK19QQuickGraphsSurface5axisXEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axisY(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QQuickGraphsSurface::axisY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphssurface.html#axisY

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QQuickGraphsSurface::axisY() const
    address = self.uglySide.call('ritual_ZNK19QQuickGraphsSurface5axisYEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axisZ(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QQuickGraphsSurface::axisZ() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphssurface.html#axisZ

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QQuickGraphsSurface::axisZ() const
    address = self.uglySide.call('ritual_ZNK19QQuickGraphsSurface5axisZEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def flipHorizontalGrid(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsSurface::flipHorizontalGrid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#flipHorizontalGrid
    """
    #  bool QQuickGraphsSurface::flipHorizontalGrid() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickGraphsSurface18flipHorizontalGridEv',
    )

  def selectedSeries(self) -> Optional[QSurface3DSeries]:
    """
    Calls Qt's 'QSurface3DSeries *QQuickGraphsSurface::selectedSeries()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#selectedSeries

    Returns
    -------

    Optional[QSurface3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSurface3DSeries *QQuickGraphsSurface::selectedSeries() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickGraphsSurface14selectedSeriesEv',
    )
    from . import QSurface3DSeries
    return QSurface3DSeries._cuteAt(address)

  def hasChangedSeriesList(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsSurface::hasChangedSeriesList() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#hasChangedSeriesList
    """
    #  bool QQuickGraphsSurface::hasChangedSeriesList() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickGraphsSurface20hasChangedSeriesListEv',
    )

  def isSeriesVisibilityDirty(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsSurface::isSeriesVisibilityDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#isSeriesVisibilityDirty
    """
    #  bool QQuickGraphsSurface::isSeriesVisibilityDirty() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickGraphsSurface23isSeriesVisibilityDirtyEv',
    )

  def isDataDirty(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsSurface::isDataDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#isDataDirty
    """
    #  bool QQuickGraphsSurface::isDataDirty() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickGraphsSurface11isDataDirtyEv',
    )

  def isSeriesVisualsDirty(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsSurface::isSeriesVisualsDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#isSeriesVisualsDirty
    """
    #  bool QQuickGraphsSurface::isSeriesVisualsDirty() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickGraphsSurface20isSeriesVisualsDirtyEv',
    )

  def isIndexDirty(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsSurface::isIndexDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#isIndexDirty
    """
    #  bool QQuickGraphsSurface::isIndexDirty() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickGraphsSurface12isIndexDirtyEv',
    )

  def isSelectedPointChanged(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsSurface::isSelectedPointChanged() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#isSelectedPointChanged
    """
    #  bool QQuickGraphsSurface::isSelectedPointChanged() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickGraphsSurface22isSelectedPointChangedEv',
    )

  def isFlipHorizontalGridChanged(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsSurface::isFlipHorizontalGridChanged()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html
    """
    #  bool QQuickGraphsSurface::isFlipHorizontalGridChanged() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickGraphsSurface27isFlipHorizontalGridChangedEv',
    )

  def isSurfaceTextureChanged(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsSurface::isSurfaceTextureChanged() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#isSurfaceTextureChanged
    """
    #  bool QQuickGraphsSurface::isSurfaceTextureChanged() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickGraphsSurface23isSurfaceTextureChangedEv',
    )

  def isChangedTexturesEmpty(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsSurface::isChangedTexturesEmpty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#isChangedTexturesEmpty
    """
    #  bool QQuickGraphsSurface::isChangedTexturesEmpty() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickGraphsSurface22isChangedTexturesEmptyEv',
    )

  @overload(QSurface3DSeries)
  @overload(NoneType)
  def hasSeriesToChangeTexture(
      self,
      series: Optional[QSurface3DSeries],
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickGraphsSurface::hasSeriesToChangeTexture(QSurface3DSeries *series)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#hasSeriesToChangeTexture

    Parameters
    ----------

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickGraphsSurface::hasSeriesToChangeTexture(QSurface3DSeries
    #      *series) const
    return self.uglySide.call(
        'ritual_ZNK19QQuickGraphsSurface24hasSeriesToChangeTextureEP16QSurf'
        'ace3DSeries',
        self._addressOf(series),
    )

  @overload(QAbstract3DSeries.Mesh, QSurface3DSeries)
  @overload(QAbstract3DSeries.Mesh, NoneType)
  def getMeshFileName(
      self,
      mesh: QAbstract3DSeries.Mesh,
      series: Optional[QSurface3DSeries],
  ) -> str:
    """
    Calls Qt's 'QString
    QQuickGraphsSurface::getMeshFileName(QAbstract3DSeries::Mesh mesh,
    QSurface3DSeries *series) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#getMeshFileName

    Parameters
    ----------

    mesh : QAbstract3DSeries.Mesh
      Passed on as its number.

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickGraphsSurface::getMeshFileName(QAbstract3DSeries::Mesh
    #      mesh, QSurface3DSeries *series) const
    return self.uglySide.call(
        'ritual_ZNK19QQuickGraphsSurface15getMeshFileNameEN17QAbstract3DSer'
        'ies4MeshEP16QSurface3DSeries',
        mesh.value, self._addressOf(series),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::setAxisX(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphssurface.html#setAxisX

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurface::setAxisX(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface8setAxisXEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::setAxisY(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphssurface.html#setAxisY

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurface::setAxisY(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface8setAxisYEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisZ(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::setAxisZ(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphssurface.html#setAxisZ

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurface::setAxisZ(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface8setAxisZEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(bool)
  def setFlipHorizontalGrid(self, flip: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::setFlipHorizontalGrid(bool flip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#setFlipHorizontalGrid

    Parameters
    ----------

    flip : bool
      Passed on as it is.
    """
    #  void QQuickGraphsSurface::setFlipHorizontalGrid(bool flip)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface21setFlipHorizontalGridEb', flip,
    )

  @overload(QPoint, QSurface3DSeries, bool)
  @overload(QPoint, NoneType, bool)
  def setSelectedPoint(
      self,
      position: QPoint,
      series: Optional[QSurface3DSeries],
      enterSlice: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::setSelectedPoint(QPoint position,
    QSurface3DSeries *series, bool enterSlice)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#setSelectedPoint

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    enterSlice : bool
      Passed on as it is.
    """
    #  void QQuickGraphsSurface::setSelectedPoint(QPoint position,
    #      QSurface3DSeries *series, bool enterSlice)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface16setSelectedPointE6QPointP16QSurfac'
        'e3DSeriesb',
        self._valueOf(position), self._addressOf(series), enterSlice,
    )

  @overload(QtGraphs3D.SelectionFlags)
  def setSelectionMode(self, mode: QtGraphs3D.SelectionFlags) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsSurface::setSelectionMode(QtGraphs3D::SelectionFlags mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#setSelectionMode

    Parameters
    ----------

    mode : QtGraphs3D.SelectionFlags
      Passed on as its number.
    """
    #  void QQuickGraphsSurface::setSelectionMode(QtGraphs3D::SelectionFlags
    #      mode)
    ritual = (
        'ritual_ZN19QQuickGraphsSurface16setSelectionModeE6QFlagsIN10QtGrap'
        'hs3D13SelectionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsSurface16setSelectionModeE6QFlagsIN10'
          'QtGraphs3D13SelectionFlagEE')
    self.uglySide.call(ritual, mode.value)

  @overload(DataDimensions)
  def setDataDimensions(self, dimension: DataDimensions) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::setDataDimensions(DataDimensions
    dimension)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#setDataDimensions

    Parameters
    ----------

    dimension : DataDimensions
      Passed on as its number.
    """
    #  void QQuickGraphsSurface::setDataDimensions(DataDimensions dimension)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface17setDataDimensionsE6QFlagsINS_13Dat'
        'aDimensionEE',
        dimension.value,
    )

  @overload(bool)
  def setSeriesVisibilityDirty(self, dirty: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::setSeriesVisibilityDirty(bool
    dirty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#setSeriesVisibilityDirty

    Parameters
    ----------

    dirty : bool
      Passed on as it is.
    """
    #  void QQuickGraphsSurface::setSeriesVisibilityDirty(bool dirty)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface24setSeriesVisibilityDirtyEb', dirty,
    )

  @overload(bool)
  def setDataDirty(self, dirty: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::setDataDirty(bool dirty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#setDataDirty

    Parameters
    ----------

    dirty : bool
      Passed on as it is.
    """
    #  void QQuickGraphsSurface::setDataDirty(bool dirty)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface12setDataDirtyEb', dirty,
    )

  @overload(bool)
  def setSeriesVisualsDirty(self, dirty: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::setSeriesVisualsDirty(bool dirty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#setSeriesVisualsDirty

    Parameters
    ----------

    dirty : bool
      Passed on as it is.
    """
    #  void QQuickGraphsSurface::setSeriesVisualsDirty(bool dirty)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface21setSeriesVisualsDirtyEb', dirty,
    )

  @overload(bool)
  def setIndexDirty(self, dirty: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::setIndexDirty(bool dirty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#setIndexDirty

    Parameters
    ----------

    dirty : bool
      Passed on as it is.
    """
    #  void QQuickGraphsSurface::setIndexDirty(bool dirty)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface13setIndexDirtyEb', dirty,
    )

  @overload(bool)
  def setSelectedPointChanged(self, changed: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::setSelectedPointChanged(bool
    changed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#setSelectedPointChanged

    Parameters
    ----------

    changed : bool
      Passed on as it is.
    """
    #  void QQuickGraphsSurface::setSelectedPointChanged(bool changed)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface23setSelectedPointChangedEb', changed,
    )

  @overload(bool)
  def setFlipHorizontalGridChanged(self, changed: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::setFlipHorizontalGridChanged(bool
    changed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html

    Parameters
    ----------

    changed : bool
      Passed on as it is.
    """
    #  void QQuickGraphsSurface::setFlipHorizontalGridChanged(bool changed)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface28setFlipHorizontalGridChangedEb',
        changed,
    )

  @overload(bool)
  def setSurfaceTextureChanged(self, changed: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::setSurfaceTextureChanged(bool
    changed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#setSurfaceTextureChanged

    Parameters
    ----------

    changed : bool
      Passed on as it is.
    """
    #  void QQuickGraphsSurface::setSurfaceTextureChanged(bool changed)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface24setSurfaceTextureChangedEb',
        changed,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickGraphsSurface::QQuickGraphsSurface(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#QQuickGraphsSurface

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickGraphsSurface::QQuickGraphsSurface(QQuickItem *parent)
    self._noteCreation(QQuickGraphsSurface, lambda: Rituals.call(
        'ritual_ZN19QQuickGraphsSurfaceC1EP10QQuickItem',
        self._addressOf(parent),
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

  @overload(QSurface3DSeries)
  @overload(NoneType)
  def addSeries(self, series: Optional[QSurface3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::addSeries(QSurface3DSeries
    *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphssurface.html#addSeries

    Parameters
    ----------

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurface::addSeries(QSurface3DSeries *series)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface9addSeriesEP16QSurface3DSeries',
        self._addressOf(series),
    )

  @overload(QSurface3DSeries)
  @overload(NoneType)
  def removeSeries(self, series: Optional[QSurface3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::removeSeries(QSurface3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#removeSeries

    Parameters
    ----------

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurface::removeSeries(QSurface3DSeries *series)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface12removeSeriesEP16QSurface3DSeries',
        self._addressOf(series),
    )

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::clearSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#clearSelection
    """
    #  void QQuickGraphsSurface::clearSelection()
    ritual = 'ritual_ZN19QQuickGraphsSurface14clearSelectionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickGraphsSurface14clearSelectionEv'
    self.uglySide.call(ritual)

  def isFlatShadingSupported(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsSurface::isFlatShadingSupported()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#isFlatShadingSupported
    """
    #  bool QQuickGraphsSurface::isFlatShadingSupported()
    return self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface22isFlatShadingSupportedEv',
    )

  def surfaceSeriesList(self) -> QList[QSurface3DSeries]:
    """
    Calls Qt's 'QList<QSurface3DSeries *>
    QQuickGraphsSurface::surfaceSeriesList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#surfaceSeriesList

    Returns
    -------

    QList[QSurface3DSeries]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSurface3DSeries *> QQuickGraphsSurface::surfaceSeriesList()
    address = self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface17surfaceSeriesListEv',
    )
    from . import QSurface3DSeries
    return QList[QSurface3DSeries]._cuteOwning(address)

  @overload(QSurface3DSeries)
  @overload(NoneType)
  def updateSurfaceTexture(self, series: Optional[QSurface3DSeries]) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsSurface::updateSurfaceTexture(QSurface3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#updateSurfaceTexture

    Parameters
    ----------

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurface::updateSurfaceTexture(QSurface3DSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface20updateSurfaceTextureEP16QSurface3D'
        'Series',
        self._addressOf(series),
    )

  def dataDimensions(self) -> DataDimensions:
    """
    Calls Qt's 'DataDimensions QQuickGraphsSurface::dataDimensions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#dataDimensions

    Returns
    -------

    DataDimensions
      The value standing for the combination Qt gave back.
    """
    #  DataDimensions QQuickGraphsSurface::dataDimensions()
    return QQuickGraphsSurface.DataDimensions(self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface14dataDimensionsEv',
    ))

  def changedSeriesList(self) -> QList[QAbstract3DSeries]:
    """
    Calls Qt's 'QList<QAbstract3DSeries *>
    QQuickGraphsSurface::changedSeriesList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#changedSeriesList

    Returns
    -------

    QList[QAbstract3DSeries]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstract3DSeries *> QQuickGraphsSurface::changedSeriesList()
    address = self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface17changedSeriesListEv',
    )
    return QList[QAbstract3DSeries]._cuteOwning(address)

  @overload(QAbstract3DAxis.AxisOrientation, bool)
  def handleAxisAutoAdjustRangeChangedInOrientation(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      autoAdjust: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsSurface::handleAxisAutoAdjustRangeChangedInOrientation(
    QAbstract3DAxis::AxisOrientation orientation, bool autoAdjust)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    autoAdjust : bool
      Passed on as it is.
    """
    #  void QQuickGraphsSurface::
    #      handleAxisAutoAdjustRangeChangedInOrientation(QAbstract3DAxis::
    #      AxisOrientation orientation, bool autoAdjust)
    ritual = (
        'ritual_ZN19QQuickGraphsSurface45handleAxisAutoAdjustRangeChangedIn'
        'OrientationEN15QAbstract3DAxis15AxisOrientationEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsSurface45handleAxisAutoAdjustRangeCha'
          'ngedInOrientationEN15QAbstract3DAxis15AxisOrientationEb')
    self.uglySide.call(ritual, orientation.value, autoAdjust)

  @overload(QObject)
  @overload(NoneType)
  def handleAxisRangeChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsSurface::handleAxisRangeChangedBySender(QObject *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurface::handleAxisRangeChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN19QQuickGraphsSurface30handleAxisRangeChangedBySenderEP7Q'
        'Object')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsSurface30handleAxisRangeChangedBySend'
          'erEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleSeriesVisibilityChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsSurface::handleSeriesVisibilityChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QQuickGraphsSurface::handleSeriesVisibilityChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN19QQuickGraphsSurface37handleSeriesVisibilityChangedBySen'
        'derEP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsSurface37handleSeriesVisibilityChange'
          'dBySenderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  @overload(bool, QObject)
  @overload(bool, NoneType)
  def handleItemLabelVisibleChangedBySender(
      self,
      visible: bool,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsSurface::handleItemLabelVisibleChangedBySender(bool visible,
    QObject *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html

    Parameters
    ----------

    visible : bool
      Passed on as it is.

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurface::handleItemLabelVisibleChangedBySender(bool
    #      visible, QObject *sender)
    ritual = (
        'ritual_ZN19QQuickGraphsSurface37handleItemLabelVisibleChangedBySen'
        'derEbP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsSurface37handleItemLabelVisibleChange'
          'dBySenderEbP7QObject')
    self.uglySide.call(ritual, visible, self._addressOf(sender, 'QObject'))

  def adjustAxisRanges(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::adjustAxisRanges()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#adjustAxisRanges
    """
    #  void QQuickGraphsSurface::adjustAxisRanges()
    ritual = 'ritual_ZN19QQuickGraphsSurface16adjustAxisRangesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickGraphsSurface16adjustAxisRangesEv'
    self.uglySide.call(ritual)

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def handleMultiAxisChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsSurface::handleMultiAxisChanged(QAbstract3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#handleMultiAxisChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurface::handleMultiAxisChanged(QAbstract3DAxis
    #      *axis)
    ritual = (
        'ritual_ZN19QQuickGraphsSurface22handleMultiAxisChangedEP15QAbstrac'
        't3DAxis')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsSurface22handleMultiAxisChangedEP15QA'
          'bstract3DAxis')
    self.uglySide.call(ritual, self._addressOf(axis))

  def handleLightingModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::handleLightingModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#handleLightingModeChanged
    """
    #  void QQuickGraphsSurface::handleLightingModeChanged()
    ritual = 'ritual_ZN19QQuickGraphsSurface25handleLightingModeChangedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsSurface25handleLightingModeChangedEv')
    self.uglySide.call(ritual)

  @overload(int, int, QtGraphs3D.SliceCaptureType)
  def renderSliceToImage(
      self,
      index: int,
      requestedIndex: int,
      sliceType: QtGraphs3D.SliceCaptureType,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::renderSliceToImage(int index, int
    requestedIndex, QtGraphs3D::SliceCaptureType sliceType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#renderSliceToImage

    Parameters
    ----------

    index : int
      Passed on as it is.

    requestedIndex : int
      Passed on as it is.

    sliceType : QtGraphs3D.SliceCaptureType
      Passed on as its number.
    """
    #  void QQuickGraphsSurface::renderSliceToImage(int index, int
    #      requestedIndex, QtGraphs3D::SliceCaptureType sliceType)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface18renderSliceToImageEiiN10QtGraphs3D'
        '16SliceCaptureTypeE',
        index, requestedIndex, sliceType.value,
    )

  @overload(int, int, QtGraphs3D.SliceCaptureType, QUrl)
  def renderSliceToImage(
      self,
      index: int,
      requestedIndex: int,
      sliceType: QtGraphs3D.SliceCaptureType,
      filePath: QUrl,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::renderSliceToImage(int index, int
    requestedIndex, QtGraphs3D::SliceCaptureType sliceType, const QUrl
    &filePath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#renderSliceToImage

    Parameters
    ----------

    index : int
      Passed on as it is.

    requestedIndex : int
      Passed on as it is.

    sliceType : QtGraphs3D.SliceCaptureType
      Passed on as its number.

    filePath : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickGraphsSurface::renderSliceToImage(int index, int
    #      requestedIndex, QtGraphs3D::SliceCaptureType sliceType, const QUrl
    #      &filePath)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface18renderSliceToImageEiiN10QtGraphs3D'
        '16SliceCaptureTypeERK4QUrl',
        index, requestedIndex, sliceType.value, self._valueOf(filePath),
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#componentComplete
    """
    #  void QQuickGraphsSurface::componentComplete()
    ritual = 'ritual_ZN19QQuickGraphsSurface17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickGraphsSurface17componentCompleteEv'
    self.uglySide.call(ritual)

  def synchData(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::synchData()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphssurface.html#synchData
    """
    #  void QQuickGraphsSurface::synchData()
    ritual = 'ritual_ZN19QQuickGraphsSurface9synchDataEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickGraphsSurface9synchDataEv'
    self.uglySide.call(ritual)

  def updateGraph(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::updateGraph()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#updateGraph
    """
    #  void QQuickGraphsSurface::updateGraph()
    ritual = 'ritual_ZN19QQuickGraphsSurface11updateGraphEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickGraphsSurface11updateGraphEv'
    self.uglySide.call(ritual)

  def calculateSceneScalingFactors(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::calculateSceneScalingFactors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html
    """
    #  void QQuickGraphsSurface::calculateSceneScalingFactors()
    ritual = 'ritual_ZN19QQuickGraphsSurface28calculateSceneScalingFactorsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsSurface28calculateSceneScalingFactors'
          'Ev')
    self.uglySide.call(ritual)

  def toggleSliceGraph(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::toggleSliceGraph()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#toggleSliceGraph
    """
    #  void QQuickGraphsSurface::toggleSliceGraph()
    ritual = 'ritual_ZN19QQuickGraphsSurface16toggleSliceGraphEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickGraphsSurface16toggleSliceGraphEv'
    self.uglySide.call(ritual)

  def updateSingleHighlightColor(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::updateSingleHighlightColor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html
    """
    #  void QQuickGraphsSurface::updateSingleHighlightColor()
    ritual = 'ritual_ZN19QQuickGraphsSurface26updateSingleHighlightColorEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsSurface26updateSingleHighlightColorEv')
    self.uglySide.call(ritual)

  def updateLightStrength(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::updateLightStrength()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#updateLightStrength
    """
    #  void QQuickGraphsSurface::updateLightStrength()
    ritual = 'ritual_ZN19QQuickGraphsSurface19updateLightStrengthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickGraphsSurface19updateLightStrengthEv'
    self.uglySide.call(ritual)

  def handleThemeTypeChange(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::handleThemeTypeChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#handleThemeTypeChange
    """
    #  void QQuickGraphsSurface::handleThemeTypeChange()
    ritual = 'ritual_ZN19QQuickGraphsSurface21handleThemeTypeChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickGraphsSurface21handleThemeTypeChangeEv'
    self.uglySide.call(ritual)

  @overload(QPointF)
  def doPicking(self, position: QPointF) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsSurface::doPicking(QPointF position)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphssurface.html#doPicking

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QQuickGraphsSurface::doPicking(QPointF position)
    ritual = 'ritual_ZN19QQuickGraphsSurface9doPickingE7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickGraphsSurface9doPickingE7QPointF'
    return self.uglySide.call(ritual, self._valueOf(position, 'QPointF'))

  @overload(QVector3D, QVector3D)
  def doRayPicking(self, origin: QVector3D, direction: QVector3D) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsSurface::doRayPicking(QVector3D origin,
    QVector3D direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#doRayPicking

    Parameters
    ----------

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  bool QQuickGraphsSurface::doRayPicking(QVector3D origin, QVector3D
    #      direction)
    ritual = 'ritual_ZN19QQuickGraphsSurface12doRayPickingE9QVector3DS0_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsSurface12doRayPickingE9QVector3DS0_')
    return self.uglySide.call(
        ritual, self._valueOf(origin), self._valueOf(direction),
    )

  @overload(QAbstract3DSeries, QAbstract3DAxis.AxisOrientation)
  @overload(NoneType, QAbstract3DAxis.AxisOrientation)
  def getSeriesMultiAxis(
      self,
      series: Optional[QAbstract3DSeries],
      orientation: QAbstract3DAxis.AxisOrientation,
  ) -> Optional[QAbstract3DAxis]:
    """
    Calls Qt's 'QAbstract3DAxis
    *QQuickGraphsSurface::getSeriesMultiAxis(QAbstract3DSeries *series,
    QAbstract3DAxis::AxisOrientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#getSeriesMultiAxis

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    Returns
    -------

    Optional[QAbstract3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DAxis
    #      *QQuickGraphsSurface::getSeriesMultiAxis(QAbstract3DSeries
    #      *series, QAbstract3DAxis::AxisOrientation orientation)
    ritual = (
        'ritual_ZN19QQuickGraphsSurface18getSeriesMultiAxisEP17QAbstract3DS'
        'eriesN15QAbstract3DAxis15AxisOrientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsSurface18getSeriesMultiAxisEP17QAbstr'
          'act3DSeriesN15QAbstract3DAxis15AxisOrientationE')
    address = self.uglySide.call(
        ritual, self._addressOf(series), orientation.value,
    )
    return QAbstract3DAxis._cuteAt(address)

  def createSliceView(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::createSliceView()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#createSliceView
    """
    #  void QQuickGraphsSurface::createSliceView()
    ritual = 'ritual_ZN19QQuickGraphsSurface15createSliceViewEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickGraphsSurface15createSliceViewEv'
    self.uglySide.call(ritual)

  @overload(str, QVector3D)
  def updateSliceItemLabel(self, label: str, position: QVector3D) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::updateSliceItemLabel(const QString
    &label, QVector3D position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#updateSliceItemLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuickGraphsSurface::updateSliceItemLabel(const QString &label,
    #      QVector3D position)
    ritual = (
        'ritual_ZN19QQuickGraphsSurface20updateSliceItemLabelERK7QString9QV'
        'ector3D')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsSurface20updateSliceItemLabelERK7QStr'
          'ing9QVector3D')
    self.uglySide.call(ritual, label, self._valueOf(position))

  @overload(QtGraphs3D.SelectionFlags)
  def updateSelectionMode(self, mode: QtGraphs3D.SelectionFlags) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsSurface::updateSelectionMode(QtGraphs3D::SelectionFlags
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#updateSelectionMode

    Parameters
    ----------

    mode : QtGraphs3D.SelectionFlags
      Passed on as its number.
    """
    #  void QQuickGraphsSurface::updateSelectionMode(QtGraphs3D::
    #      SelectionFlags mode)
    ritual = (
        'ritual_ZN19QQuickGraphsSurface19updateSelectionModeE6QFlagsIN10QtG'
        'raphs3D13SelectionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsSurface19updateSelectionModeE6QFlagsI'
          'N10QtGraphs3D13SelectionFlagEE')
    self.uglySide.call(ritual, mode.value)

  @overload(int, int, QtGraphs3D.SliceCaptureType)
  def createOffscreenSliceView(
      self,
      index: int,
      requestedIndex: int,
      sliceType: QtGraphs3D.SliceCaptureType,
  ) -> Optional[QQuick3DViewport]:
    """
    Calls Qt's 'QQuick3DViewport
    *QQuickGraphsSurface::createOffscreenSliceView(int index, int
    requestedIndex, QtGraphs3D::SliceCaptureType sliceType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#createOffscreenSliceView

    Parameters
    ----------

    index : int
      Passed on as it is.

    requestedIndex : int
      Passed on as it is.

    sliceType : QtGraphs3D.SliceCaptureType
      Passed on as its number.

    Returns
    -------

    Optional[QQuick3DViewport]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DViewport *QQuickGraphsSurface::createOffscreenSliceView(int
    #      index, int requestedIndex, QtGraphs3D::SliceCaptureType sliceType)
    address = self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface24createOffscreenSliceViewEiiN10QtGr'
        'aphs3D16SliceCaptureTypeE',
        index, requestedIndex, sliceType.value,
    )
    return QQuick3DViewport._cuteAt(address)

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def handleAxisXChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::handleAxisXChanged(QAbstract3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#handleAxisXChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurface::handleAxisXChanged(QAbstract3DAxis *axis)
    ritual = (
        'ritual_ZN19QQuickGraphsSurface18handleAxisXChangedEP15QAbstract3DA'
        'xis')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsSurface18handleAxisXChangedEP15QAbstr'
          'act3DAxis')
    self.uglySide.call(ritual, self._addressOf(axis))

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def handleAxisYChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::handleAxisYChanged(QAbstract3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#handleAxisYChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurface::handleAxisYChanged(QAbstract3DAxis *axis)
    ritual = (
        'ritual_ZN19QQuickGraphsSurface18handleAxisYChangedEP15QAbstract3DA'
        'xis')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsSurface18handleAxisYChangedEP15QAbstr'
          'act3DAxis')
    self.uglySide.call(ritual, self._addressOf(axis))

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def handleAxisZChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::handleAxisZChanged(QAbstract3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#handleAxisZChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurface::handleAxisZChanged(QAbstract3DAxis *axis)
    ritual = (
        'ritual_ZN19QQuickGraphsSurface18handleAxisZChangedEP15QAbstract3DA'
        'xis')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsSurface18handleAxisZChangedEP15QAbstr'
          'act3DAxis')
    self.uglySide.call(ritual, self._addressOf(axis))

  def handleShadingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::handleShadingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#handleShadingChanged
    """
    #  void QQuickGraphsSurface::handleShadingChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface20handleShadingChangedEv',
    )

  def handleWireframeColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::handleWireframeColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html
    """
    #  void QQuickGraphsSurface::handleWireframeColorChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface27handleWireframeColorChangedEv',
    )

  @overload(bool)
  def handleFlipHorizontalGridChanged(self, flip: bool) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsSurface::handleFlipHorizontalGridChanged(bool flip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html

    Parameters
    ----------

    flip : bool
      Passed on as it is.
    """
    #  void QQuickGraphsSurface::handleFlipHorizontalGridChanged(bool flip)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface31handleFlipHorizontalGridChangedEb',
        flip,
    )

  def handleArrayReset(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::handleArrayReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#handleArrayReset
    """
    #  void QQuickGraphsSurface::handleArrayReset()
    self.uglySide.call('ritual_ZN19QQuickGraphsSurface16handleArrayResetEv')

  @overload(int, int)
  def handleRowsAdded(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::handleRowsAdded(qsizetype
    startIndex, qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#handleRowsAdded

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQuickGraphsSurface::handleRowsAdded(qsizetype startIndex,
    #      qsizetype count)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface15handleRowsAddedExx',
        startIndex, count,
    )

  @overload(int, int)
  def handleRowsChanged(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::handleRowsChanged(qsizetype
    startIndex, qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#handleRowsChanged

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQuickGraphsSurface::handleRowsChanged(qsizetype startIndex,
    #      qsizetype count)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface17handleRowsChangedExx',
        startIndex, count,
    )

  @overload(int, int)
  def handleRowsRemoved(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::handleRowsRemoved(qsizetype
    startIndex, qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#handleRowsRemoved

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQuickGraphsSurface::handleRowsRemoved(qsizetype startIndex,
    #      qsizetype count)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface17handleRowsRemovedExx',
        startIndex, count,
    )

  @overload(int, int)
  def handleRowsInserted(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::handleRowsInserted(qsizetype
    startIndex, qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#handleRowsInserted

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQuickGraphsSurface::handleRowsInserted(qsizetype startIndex,
    #      qsizetype count)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface18handleRowsInsertedExx',
        startIndex, count,
    )

  @overload(int, int)
  def handleItemChanged(self, rowIndex: int, columnIndex: int) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::handleItemChanged(qsizetype
    rowIndex, qsizetype columnIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#handleItemChanged

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    columnIndex : int
      Passed on as it is.
    """
    #  void QQuickGraphsSurface::handleItemChanged(qsizetype rowIndex,
    #      qsizetype columnIndex)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface17handleItemChangedExx',
        rowIndex, columnIndex,
    )

  @overload(bool)
  def handleFlatShadingSupportedChange(self, supported: bool) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsSurface::handleFlatShadingSupportedChange(bool supported)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html

    Parameters
    ----------

    supported : bool
      Passed on as it is.
    """
    #  void QQuickGraphsSurface::handleFlatShadingSupportedChange(bool
    #      supported)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface32handleFlatShadingSupportedChangeEb',
        supported,
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisXChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::axisXChanged(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#axisXChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurface::axisXChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface12axisXChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisYChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::axisYChanged(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#axisYChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurface::axisYChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface12axisYChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisZChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::axisZChanged(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#axisZChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurface::axisZChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface12axisZChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QSurface3DSeries)
  @overload(NoneType)
  def selectedSeriesChanged(
      self,
      series: Optional[QSurface3DSeries],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsSurface::selectedSeriesChanged(QSurface3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#selectedSeriesChanged

    Parameters
    ----------

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurface::selectedSeriesChanged(QSurface3DSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface21selectedSeriesChangedEP16QSurface3'
        'DSeries',
        self._addressOf(series),
    )

  @overload(bool)
  def flipHorizontalGridChanged(self, flip: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::flipHorizontalGridChanged(bool
    flip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#flipHorizontalGridChanged

    Parameters
    ----------

    flip : bool
      Passed on as it is.
    """
    #  void QQuickGraphsSurface::flipHorizontalGridChanged(bool flip)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface25flipHorizontalGridChangedEb', flip,
    )

  @overload(QImage)
  def sliceImageChanged(self, image: QImage) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::sliceImageChanged(const QImage
    &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#sliceImageChanged

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QQuickGraphsSurface::sliceImageChanged(const QImage &image)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface17sliceImageChangedERK6QImage',
        self._valueOf(image),
    )

  @overload(QSurfaceDataItem, bool, bool)
  @overload(QSurfaceDataItem, bool, bool, QSurface3DSeries)
  @overload(QSurfaceDataItem, bool, bool, NoneType)
  def getNormalizedVertex(
      self,
      data: QSurfaceDataItem,
      polar: bool,
      flipXZ: bool,
      series: Optional[QSurface3DSeries] = None,
  ) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuickGraphsSurface::getNormalizedVertex(const
    QSurfaceDataItem &data, bool polar, bool flipXZ, QSurface3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#getNormalizedVertex

    Parameters
    ----------

    data : QSurfaceDataItem
      Passed on as a value: Qt reads the C++ QSurfaceDataItem, which stays
      Python's own.

    polar : bool
      Passed on as it is.

    flipXZ : bool
      Passed on as it is.

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuickGraphsSurface::getNormalizedVertex(const
    #      QSurfaceDataItem &data, bool polar, bool flipXZ, QSurface3DSeries
    #      *series)
    address = self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface19getNormalizedVertexERK16QSurfaceDa'
        'taItembbP16QSurface3DSeries',
        self._valueOf(data), polar, flipXZ, self._addressOf(series),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def handleChangedSeries(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::handleChangedSeries()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#handleChangedSeries
    """
    #  void QQuickGraphsSurface::handleChangedSeries()
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface19handleChangedSeriesEv',
    )

  def updateSelectedPoint(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::updateSelectedPoint()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#updateSelectedPoint
    """
    #  void QQuickGraphsSurface::updateSelectedPoint()
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface19updateSelectedPointEv',
    )

  @overload(QSurface3DSeries)
  @overload(NoneType)
  def addModel(self, series: Optional[QSurface3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::addModel(QSurface3DSeries
    *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphssurface.html#addModel

    Parameters
    ----------

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurface::addModel(QSurface3DSeries *series)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface8addModelEP16QSurface3DSeries',
        self._addressOf(series),
    )

  @overload(QAbstract3DSeries.Mesh)
  def handleMeshTypeChanged(self, mesh: QAbstract3DSeries.Mesh) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsSurface::handleMeshTypeChanged(QAbstract3DSeries::Mesh
    mesh)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#handleMeshTypeChanged

    Parameters
    ----------

    mesh : QAbstract3DSeries.Mesh
      Passed on as its number.
    """
    #  void
    #      QQuickGraphsSurface::handleMeshTypeChanged(QAbstract3DSeries::Mesh
    #      mesh)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface21handleMeshTypeChangedEN17QAbstract'
        '3DSeries4MeshE',
        mesh.value,
    )

  @overload(str)
  def handlePointerChanged(self, filename: str) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::handlePointerChanged(const QString
    &filename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#handlePointerChanged

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickGraphsSurface::handlePointerChanged(const QString
    #      &filename)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface20handlePointerChangedERK7QString',
        filename,
    )

  @overload(QAbstract3DSeries.Mesh, QSurface3DSeries)
  @overload(QAbstract3DSeries.Mesh, NoneType)
  def changePointerMeshTypeForSeries(
      self,
      mesh: QAbstract3DSeries.Mesh,
      series: Optional[QSurface3DSeries],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsSurface::changePointerMeshTypeForSeries(QAbstract3DSeries::
    Mesh mesh, QSurface3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html

    Parameters
    ----------

    mesh : QAbstract3DSeries.Mesh
      Passed on as its number.

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurface::changePointerMeshTypeForSeries(
    #      QAbstract3DSeries::Mesh mesh, QSurface3DSeries *series)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface30changePointerMeshTypeForSeriesEN17'
        'QAbstract3DSeries4MeshEP16QSurface3DSeries',
        mesh.value, self._addressOf(series),
    )

  @overload(str, QSurface3DSeries)
  @overload(str, NoneType)
  def changePointerForSeries(
      self,
      filename: str,
      series: Optional[QSurface3DSeries],
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::changePointerForSeries(const
    QString &filename, QSurface3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#changePointerForSeries

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurface::changePointerForSeries(const QString
    #      &filename, QSurface3DSeries *series)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface22changePointerForSeriesERK7QStringP'
        '16QSurface3DSeries',
        filename, self._addressOf(series),
    )

  @overload(QAbstract3DSeries.Mesh, QSurface3DSeries)
  @overload(QAbstract3DSeries.Mesh, NoneType)
  def changeSlicePointerMeshTypeForSeries(
      self,
      mesh: QAbstract3DSeries.Mesh,
      series: Optional[QSurface3DSeries],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsSurface::changeSlicePointerMeshTypeForSeries(
    QAbstract3DSeries::Mesh mesh, QSurface3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html

    Parameters
    ----------

    mesh : QAbstract3DSeries.Mesh
      Passed on as its number.

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurface::changeSlicePointerMeshTypeForSeries(
    #      QAbstract3DSeries::Mesh mesh, QSurface3DSeries *series)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface35changeSlicePointerMeshTypeForSerie'
        'sEN17QAbstract3DSeries4MeshEP16QSurface3DSeries',
        mesh.value, self._addressOf(series),
    )

  @overload(str, QSurface3DSeries)
  @overload(str, NoneType)
  def changeSlicePointerForSeries(
      self,
      filename: str,
      series: Optional[QSurface3DSeries],
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsSurface::changeSlicePointerForSeries(const
    QString &filename, QSurface3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsSurface::changeSlicePointerForSeries(const QString
    #      &filename, QSurface3DSeries *series)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface27changeSlicePointerForSeriesERK7QSt'
        'ringP16QSurface3DSeries',
        filename, self._addressOf(series),
    )

  @overload(QVector3D, QVector3D, QVector3D, QVector3D)
  def intersectWithAABB(
      self,
      boundMin: QVector3D,
      boundsMax: QVector3D,
      origin: QVector3D,
      dir: QVector3D,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsSurface::intersectWithAABB(QVector3D
    boundMin, QVector3D boundsMax, QVector3D origin, QVector3D dir)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphssurface.html#intersectWithAABB

    Parameters
    ----------

    boundMin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    boundsMax : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    dir : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  bool QQuickGraphsSurface::intersectWithAABB(QVector3D boundMin,
    #      QVector3D boundsMax, QVector3D origin, QVector3D dir)
    return self.uglySide.call(
        'ritual_ZN19QQuickGraphsSurface17intersectWithAABBE9QVector3DS0_S0_'
        'S0_',
        self._valueOf(boundMin), self._valueOf(boundsMax),
        self._valueOf(origin), self._valueOf(dir),
    )

  @staticmethod
  def addFillModel(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsSurface::addFillModel(SurfaceModel *model)': names
    'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurface.addFillModel' has no cute function yet. Qt's "
        "'void QQuickGraphsSurface::addFillModel(SurfaceModel *model)': "
        "names 'QQuickGraphsSurface::SurfaceModel', which has no cute class "
        "yet.")

  @staticmethod
  def addSliceModel(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsSurface::addSliceModel(SurfaceModel *model)':
    names 'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurface.addSliceModel' has no cute function yet. Qt's "
        "'void QQuickGraphsSurface::addSliceModel(SurfaceModel *model)': "
        "names 'QQuickGraphsSurface::SurfaceModel', which has no cute class "
        "yet.")

  @staticmethod
  def appendSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickGraphsSurface::appendSeriesFunc(QQmlListProperty<QSurface3DSeries>
    *list, QSurface3DSeries *series)': names
    'QQmlListProperty<QSurface3DSeries>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurface.appendSeriesFunc' has no cute function yet. "
        "Qt's 'void "
        "QQuickGraphsSurface::appendSeriesFunc(QQmlListProperty<QSurface3DSe"
        "ries> *list, QSurface3DSeries *series)': names "
        "'QQmlListProperty<QSurface3DSeries>', which has no cute class yet.")

  @staticmethod
  def atSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'QSurface3DSeries
    *QQuickGraphsSurface::atSeriesFunc(QQmlListProperty<QSurface3DSeries>
    *list, qsizetype index)': names 'QQmlListProperty<QSurface3DSeries>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurface.atSeriesFunc' has no cute function yet. Qt's "
        "'QSurface3DSeries "
        "*QQuickGraphsSurface::atSeriesFunc(QQmlListProperty<QSurface3DSerie"
        "s> *list, qsizetype index)': names "
        "'QQmlListProperty<QSurface3DSeries>', which has no cute class yet.")

  @staticmethod
  def calculateSampleSpace(*__, **_) -> Never:
    """
    Qt's 'QRect QQuickGraphsSurface::calculateSampleSpace(SurfaceModel
    *model, const QSurfaceDataArray &array)': names
    'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurface.calculateSampleSpace' has no cute function "
        "yet. Qt's 'QRect "
        "QQuickGraphsSurface::calculateSampleSpace(SurfaceModel *model, "
        "const QSurfaceDataArray &array)': names "
        "'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.")

  @staticmethod
  def clearSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickGraphsSurface::clearSeriesFunc(QQmlListProperty<QSurface3DSeries>
    *list)': names 'QQmlListProperty<QSurface3DSeries>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurface.clearSeriesFunc' has no cute function yet. "
        "Qt's 'void "
        "QQuickGraphsSurface::clearSeriesFunc(QQmlListProperty<QSurface3DSer"
        "ies> *list)': names 'QQmlListProperty<QSurface3DSeries>', which "
        "has no cute class yet.")

  @staticmethod
  def countSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQuickGraphsSurface::countSeriesFunc(QQmlListProperty<QSurface3DSeries>
    *list)': names 'QQmlListProperty<QSurface3DSeries>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurface.countSeriesFunc' has no cute function yet. "
        "Qt's 'qsizetype "
        "QQuickGraphsSurface::countSeriesFunc(QQmlListProperty<QSurface3DSer"
        "ies> *list)': names 'QQmlListProperty<QSurface3DSeries>', which "
        "has no cute class yet.")

  @staticmethod
  def createGridlineIndices(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsSurface::createGridlineIndices(SurfaceModel
    *model, qsizetype x, qsizetype y, qsizetype endX, qsizetype endY)': names
    'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurface.createGridlineIndices' has no cute function "
        "yet. Qt's 'void "
        "QQuickGraphsSurface::createGridlineIndices(SurfaceModel *model, "
        "qsizetype x, qsizetype y, qsizetype endX, qsizetype endY)': names "
        "'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.")

  @staticmethod
  def createIndices(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsSurface::createIndices(SurfaceModel *model,
    qsizetype columnCount, qsizetype rowCount)': names
    'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurface.createIndices' has no cute function yet. Qt's "
        "'void QQuickGraphsSurface::createIndices(SurfaceModel *model, "
        "qsizetype columnCount, qsizetype rowCount)': names "
        "'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.")

  @staticmethod
  def createLineIndices(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsSurface::createLineIndices(SurfaceModel *model,
    qsizetype pointCount)': names 'QQuickGraphsSurface::SurfaceModel', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurface.createLineIndices' has no cute function yet. "
        "Qt's 'void QQuickGraphsSurface::createLineIndices(SurfaceModel "
        "*model, qsizetype pointCount)': names "
        "'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.")

  @staticmethod
  def mapCoordsToSampleSpace(*__, **_) -> Never:
    """
    Qt's 'QPoint QQuickGraphsSurface::mapCoordsToSampleSpace(SurfaceModel
    *model, QPointF coords)': names 'QQuickGraphsSurface::SurfaceModel',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurface.mapCoordsToSampleSpace' has no cute function "
        "yet. Qt's 'QPoint "
        "QQuickGraphsSurface::mapCoordsToSampleSpace(SurfaceModel *model, "
        "QPointF coords)': names 'QQuickGraphsSurface::SurfaceModel', which "
        "has no cute class yet.")

  @staticmethod
  def mapCoordsToWorldSpace(*__, **_) -> Never:
    """
    Qt's 'QPointF QQuickGraphsSurface::mapCoordsToWorldSpace(SurfaceModel
    *model, QPointF coords)': names 'QQuickGraphsSurface::SurfaceModel',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurface.mapCoordsToWorldSpace' has no cute function "
        "yet. Qt's 'QPointF "
        "QQuickGraphsSurface::mapCoordsToWorldSpace(SurfaceModel *model, "
        "QPointF coords)': names 'QQuickGraphsSurface::SurfaceModel', which "
        "has no cute class yet.")

  @staticmethod
  def pickSurfaces(*__, **_) -> Never:
    """
    Qt's 'QVector3D QQuickGraphsSurface::pickSurfaces(QVector3D rayOrigin,
    QVector3D rayDir, SurfaceModel *&pickedModel)': takes or gives a type
    that cannot be passed yet: QQuickGraphsSurface::SurfaceModel *&.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurface.pickSurfaces' has no cute function yet. Qt's "
        "'QVector3D QQuickGraphsSurface::pickSurfaces(QVector3D rayOrigin, "
        "QVector3D rayDir, SurfaceModel *&pickedModel)': takes or gives a "
        "type that cannot be passed yet: QQuickGraphsSurface::SurfaceModel "
        "*&.")

  @staticmethod
  def removeNaNRows(*__, **_) -> Never:
    """
    Qt's 'QSurfaceDataArray QQuickGraphsSurface::removeNaNRows(const
    QSurfaceDataArray &array)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurface.removeNaNRows' has no cute function yet. Qt's "
        "'QSurfaceDataArray QQuickGraphsSurface::removeNaNRows(const "
        "QSurfaceDataArray &array)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def triangleIntersection(*__, **_) -> Never:
    """
    Qt's 'QVector3D QQuickGraphsSurface::triangleIntersection(QVector3D
    origin, QVector3D dir, const std::array<QVector3D, 3> &triangle)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurface.triangleIntersection' has no cute function "
        "yet. Qt's 'QVector3D "
        "QQuickGraphsSurface::triangleIntersection(QVector3D origin, "
        "QVector3D dir, const std::array<QVector3D, 3> &triangle)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def updateFill(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsSurface::updateFill(SurfaceModel *model)': names
    'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurface.updateFill' has no cute function yet. Qt's "
        "'void QQuickGraphsSurface::updateFill(SurfaceModel *model)': names "
        "'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.")

  @staticmethod
  def updateLineFill(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsSurface::updateLineFill(SurfaceModel *model)':
    names 'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurface.updateLineFill' has no cute function yet. "
        "Qt's 'void QQuickGraphsSurface::updateLineFill(SurfaceModel "
        "*model)': names 'QQuickGraphsSurface::SurfaceModel', which has no "
        "cute class yet.")

  @staticmethod
  def updateMaterial(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsSurface::updateMaterial(SurfaceModel *model)':
    names 'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurface.updateMaterial' has no cute function yet. "
        "Qt's 'void QQuickGraphsSurface::updateMaterial(SurfaceModel "
        "*model)': names 'QQuickGraphsSurface::SurfaceModel', which has no "
        "cute class yet.")

  @staticmethod
  def updateModel(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsSurface::updateModel(SurfaceModel *model)': names
    'QQuickGraphsSurface::SurfaceModel', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsSurface.updateModel' has no cute function yet. Qt's "
        "'void QQuickGraphsSurface::updateModel(SurfaceModel *model)': "
        "names 'QQuickGraphsSurface::SurfaceModel', which has no cute class "
        "yet.")
