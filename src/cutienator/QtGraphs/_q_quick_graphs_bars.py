"""
QQuickGraphsBars binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qquickgraphsbars_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickGraphsBars to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from ..QtQuick import QQuickItem
from . import QtGraphs3D, QAbstract3DAxis, QAbstract3DSeries
from . import QQuickGraphsItem
from ..QtQuick3D import QQuick3DViewport

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint, QPointF, QSizeF, QUrl
  from ..QtGui import QColor, QImage, QVector3D
  from . import BarInstancing, QBar3DSeries, QBarDataItem, QCategory3DAxis
  from . import QValue3DAxis
  from ..QtQuick3D import QQuick3DModel, QQuick3DNode, QQuick3DRepeater
  from ..QtQuick3D import QQuick3DTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  BarInstancing = WAIT['BarInstancing']
  QBar3DSeries = WAIT['QtGraphs:QBar3DSeries']
  QBarDataItem = WAIT['QtGraphs:QBarDataItem']
  QCategory3DAxis = WAIT['QtGraphs:QCategory3DAxis']
  QColor = WAIT['QColor']
  QImage = WAIT['QImage']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QQuick3DModel = WAIT['QQuick3DModel']
  QQuick3DNode = WAIT['QQuick3DNode']
  QQuick3DRepeater = WAIT['QQuick3DRepeater']
  QQuick3DTexture = WAIT['QQuick3DTexture']
  QSizeF = WAIT['QSizeF']
  QUrl = WAIT['QUrl']
  QValue3DAxis = WAIT['QtGraphs:QValue3DAxis']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGraphsBars(QQuickGraphsItem):
  """
  The cute side of Qt's QQuickGraphsBars: a plain Python object standing in
  front of one C++ QQuickGraphsBars.

  It is built on the cute 'QQuickGraphsItem', as Qt's QQuickGraphsBars is
  built on Qt's QQuickGraphsItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickGraphsBars that has a ritual and that Python
  can call so far, 118 names in all: 'metaObject', 'tr', 'rowAxis',
  'setRowAxis', 'valueAxis', 'setValueAxis', 'columnAxis', 'setColumnAxis',
  'setMultiSeriesUniform', 'isMultiSeriesUniform', 'setBarThickness',
  'barThickness', 'setBarSpacing', 'barSpacing', 'setBarSpacingRelative',
  'isBarSpacingRelative', 'setBarSeriesMargin', 'barSeriesMargin',
  'setMultiSeriesScaling', 'multiSeriesScaling', 'setBarSpecs',
  'setFloorLevel', 'floorLevel', 'addSeries', 'removeSeries', 'insertSeries',
  'clearSelection', 'setPrimarySeries', 'primarySeries', 'selectedSeries',
  'invalidSelectionPosition', 'setSelectionMode',
  'handleAxisAutoAdjustRangeChangedInOrientation',
  'handleSeriesVisibilityChangedBySender',
  'handleItemLabelVisibleChangedBySender', 'handleAxisRangeChangedBySender',
  'adjustAxisRanges', 'handleLightingModeChanged', 'handleMultiAxisChanged',
  'setSelectedBar', 'barSeriesList', 'isSeriesVisualsDirty',
  'setSeriesVisualsDirty', 'isDataDirty', 'setDataDirty',
  'renderSliceToImage', 'componentComplete', 'synchData', 'updateFloor',
  'updateParameters', 'updateFloorLevel', 'updateGraph', 'updateAxisRange',
  'updateAxisReversed', 'updateLightStrength',
  'calculateSceneScalingFactors', 'calculateCategoryLabelPosition',
  'calculateCategoryGridLinePosition', 'createSliceView', 'toggleSliceGraph',
  'handleLabelCountChanged', 'updateSelectionMode', 'doPicking',
  'doRayPicking', 'createDefaultAxis', 'updateSliceItemLabel',
  'getSeriesMultiAxis', 'createOffscreenSliceView', 'handleAxisXChanged',
  'handleAxisYChanged', 'handleAxisZChanged', 'handleSeriesMeshChanged',
  'handleMeshSmoothChanged', 'handleCameraRotationChanged',
  'handleArrayReset', 'handleRowsAdded', 'handleRowsChanged',
  'handleRowsRemoved', 'handleRowsInserted', 'handleItemChanged',
  'handleDataRowLabelsChanged', 'handleDataColumnLabelsChanged',
  'handleRowColorsChanged', 'handleValueColoringChanged', 'rowAxisChanged',
  'valueAxisChanged', 'columnAxisChanged', 'multiSeriesUniformChanged',
  'barThicknessChanged', 'barSpacingChanged', 'barSpacingRelativeChanged',
  'barSeriesMarginChanged', 'meshFileNameChanged', 'primarySeriesChanged',
  'selectedSeriesChanged', 'floorLevelChanged', 'sliceImageChanged',
  'calculateHeightAdjustment', 'calculateSeriesStartPosition',
  'connectSeries', 'disconnectSeries', 'createDataItem', 'getMeshFileName',
  'updateBarVisuality', 'updateBarPositions', 'updateBarHeightParameters',
  'updateBarVisuals', 'updateItemMaterial', 'updateMaterialProperties',
  'removeBarModels', 'deleteBarModels', 'deleteBarItemHolders',
  'createTexture', 'updateSelectedBar', 'resetClickedStatus',
  'removeSlicedBarModels', 'updateBarSpecs', 'updateBarSeriesMargin'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGraphsBars::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickGraphsBars::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickGraphsBars::~QQuickGraphsBars()': the destructor: Python
    never removes a C++ QQuickGraphsBars.
  - Qt's 'QQmlListProperty<QBar3DSeries> QQuickGraphsBars::seriesList()':
    gives a type Python has no way to take yet.
  - Qt's 'void
    QQuickGraphsBars::appendSeriesFunc(QQmlListProperty<QBar3DSeries> *list,
    QBar3DSeries *series)': names 'QQmlListProperty<QBar3DSeries>', which has
    no cute class yet.
  - Qt's 'qsizetype
    QQuickGraphsBars::countSeriesFunc(QQmlListProperty<QBar3DSeries> *list)':
    names 'QQmlListProperty<QBar3DSeries>', which has no cute class yet.
  - Qt's 'QBar3DSeries
    *QQuickGraphsBars::atSeriesFunc(QQmlListProperty<QBar3DSeries> *list,
    qsizetype index)': names 'QQmlListProperty<QBar3DSeries>', which has no
    cute class yet.
  - Qt's 'void
    QQuickGraphsBars::clearSeriesFunc(QQmlListProperty<QBar3DSeries> *list)':
    names 'QQmlListProperty<QBar3DSeries>', which has no cute class yet.
  - Qt's 'void QQuickGraphsBars::generateBars(QList<QBar3DSeries *>
    &barSeriesList)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQuickGraphsBars::fixMeshFileName(QString &fileName,
    QAbstract3DSeries::Mesh meshType)': takes a type Python has no way to
    hand over yet.
  - Qt's 'SelectionType QQuickGraphsBars::isSelected(int row, int bar,
    QBar3DSeries *series)': gives the enum 'QQuickGraphsBars::SelectionType',
    whose class cannot be named here.
  - Qt's 'void QQuickGraphsBars::createBarItemHolders(QBar3DSeries *series,
    QList<BarModel *> barList, bool slice)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void QQuickGraphsBars::adjustSelectionPosition(QPoint &pos, const
    QBar3DSeries *series)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 135 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickGraphsBars is created at the first use, not by
    'QQuickGraphsBars(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGraphsBars.
  - Qt tells when it has removed the C++ QQuickGraphsBars. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickGraphsBars that has no cute function yet,
    'adjustSelectionPosition', 'appendSeriesFunc', 'atSeriesFunc',
    'clearSeriesFunc', 'countSeriesFunc', 'createBarItemHolders',
    'fixMeshFileName', 'generateBars', 'isSelected', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QQuickGraphsBars, each a class in here as
  #  in C++.

  class ChangeItem(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickGraphsBars::ChangeItem: a plain Python object
    standing in front of one C++ QQuickGraphsBars::ChangeItem.

    C++ hands a QQuickGraphsBars::ChangeItem around as a copy, so every C++
    QQuickGraphsBars::ChangeItem behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQuickGraphsBars::ChangeItem yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickGraphsBars::ChangeItem::~ChangeItem()': the destructor:
      Python removes its C++ QQuickGraphsBars::ChangeItem by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQuickGraphsBars::ChangeItem is created at the first use, not
      by 'QQuickGraphsBars::ChangeItem(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickGraphsBars::ChangeItem back gives a copy the
      ritual made for Python, in a new cute QQuickGraphsBars::ChangeItem.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickGraphsBars::ChangeItem'

    #  Qt's '~QQuickGraphsBars::ChangeItem()'. Naming it makes this a value
    #  class: Python owns every C++ QQuickGraphsBars::ChangeItem behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QQuickGraphsBars10ChangeItemD1Ev'

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
    The cute side of Qt's QQuickGraphsBars::ChangeRow: a plain Python object
    standing in front of one C++ QQuickGraphsBars::ChangeRow.

    C++ hands a QQuickGraphsBars::ChangeRow around as a copy, so every C++
    QQuickGraphsBars::ChangeRow behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQuickGraphsBars::ChangeRow yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickGraphsBars::ChangeRow::~ChangeRow()': the destructor:
      Python removes its C++ QQuickGraphsBars::ChangeRow by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQuickGraphsBars::ChangeRow is created at the first use, not by
      'QQuickGraphsBars::ChangeRow(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickGraphsBars::ChangeRow back gives a copy the
      ritual made for Python, in a new cute QQuickGraphsBars::ChangeRow.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickGraphsBars::ChangeRow'

    #  Qt's '~QQuickGraphsBars::ChangeRow()'. Naming it makes this a value
    #  class: Python owns every C++ QQuickGraphsBars::ChangeRow behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QQuickGraphsBars9ChangeRowD1Ev'

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
    Calls Qt's 'QString QQuickGraphsBars::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbars.html#tr

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
    #  QString QQuickGraphsBars::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuickGraphsBars2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def invalidSelectionPosition() -> QPoint:
    """
    Calls Qt's 'QPoint QQuickGraphsBars::invalidSelectionPosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#invalidSelectionPosition

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QQuickGraphsBars::invalidSelectionPosition()
    address = Rituals.call(
        'ritual_ZN16QQuickGraphsBars24invalidSelectionPositionEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGraphsBars'

  #  A C++ QQuickGraphsBars Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickGraphsBars'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGraphsBars::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbars.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGraphsBars::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickGraphsBars10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rowAxis(self) -> Optional[QCategory3DAxis]:
    """
    Calls Qt's 'QCategory3DAxis *QQuickGraphsBars::rowAxis() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbars.html#rowAxis

    Returns
    -------

    Optional[QCategory3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCategory3DAxis *QQuickGraphsBars::rowAxis() const
    address = self.uglySide.call('ritual_ZNK16QQuickGraphsBars7rowAxisEv')
    from . import QCategory3DAxis
    return QCategory3DAxis._cuteAt(address)

  def valueAxis(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QQuickGraphsBars::valueAxis() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbars.html#valueAxis

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QQuickGraphsBars::valueAxis() const
    address = self.uglySide.call('ritual_ZNK16QQuickGraphsBars9valueAxisEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def columnAxis(self) -> Optional[QCategory3DAxis]:
    """
    Calls Qt's 'QCategory3DAxis *QQuickGraphsBars::columnAxis() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbars.html#columnAxis

    Returns
    -------

    Optional[QCategory3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCategory3DAxis *QQuickGraphsBars::columnAxis() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickGraphsBars10columnAxisEv',
    )
    from . import QCategory3DAxis
    return QCategory3DAxis._cuteAt(address)

  def isMultiSeriesUniform(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsBars::isMultiSeriesUniform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#isMultiSeriesUniform
    """
    #  bool QQuickGraphsBars::isMultiSeriesUniform() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsBars20isMultiSeriesUniformEv',
    )

  def barThickness(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsBars::barThickness() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbars.html#barThickness
    """
    #  float QQuickGraphsBars::barThickness() const
    return self.uglySide.call('ritual_ZNK16QQuickGraphsBars12barThicknessEv')

  def barSpacing(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QQuickGraphsBars::barSpacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbars.html#barSpacing

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QQuickGraphsBars::barSpacing() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickGraphsBars10barSpacingEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def isBarSpacingRelative(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsBars::isBarSpacingRelative() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#isBarSpacingRelative
    """
    #  bool QQuickGraphsBars::isBarSpacingRelative() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsBars20isBarSpacingRelativeEv',
    )

  def barSeriesMargin(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QQuickGraphsBars::barSeriesMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#barSeriesMargin

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QQuickGraphsBars::barSeriesMargin() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickGraphsBars15barSeriesMarginEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def multiSeriesScaling(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsBars::multiSeriesScaling() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#multiSeriesScaling
    """
    #  bool QQuickGraphsBars::multiSeriesScaling() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsBars18multiSeriesScalingEv',
    )

  def floorLevel(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsBars::floorLevel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbars.html#floorLevel
    """
    #  float QQuickGraphsBars::floorLevel() const
    return self.uglySide.call('ritual_ZNK16QQuickGraphsBars10floorLevelEv')

  def primarySeries(self) -> Optional[QBar3DSeries]:
    """
    Calls Qt's 'QBar3DSeries *QQuickGraphsBars::primarySeries() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#primarySeries

    Returns
    -------

    Optional[QBar3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBar3DSeries *QQuickGraphsBars::primarySeries() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickGraphsBars13primarySeriesEv',
    )
    from . import QBar3DSeries
    return QBar3DSeries._cuteAt(address)

  def selectedSeries(self) -> Optional[QBar3DSeries]:
    """
    Calls Qt's 'QBar3DSeries *QQuickGraphsBars::selectedSeries() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#selectedSeries

    Returns
    -------

    Optional[QBar3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBar3DSeries *QQuickGraphsBars::selectedSeries() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickGraphsBars14selectedSeriesEv',
    )
    from . import QBar3DSeries
    return QBar3DSeries._cuteAt(address)

  def isSeriesVisualsDirty(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsBars::isSeriesVisualsDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#isSeriesVisualsDirty
    """
    #  bool QQuickGraphsBars::isSeriesVisualsDirty() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsBars20isSeriesVisualsDirtyEv',
    )

  def isDataDirty(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsBars::isDataDirty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbars.html#isDataDirty
    """
    #  bool QQuickGraphsBars::isDataDirty() const
    return self.uglySide.call('ritual_ZNK16QQuickGraphsBars11isDataDirtyEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QCategory3DAxis)
  @overload(NoneType)
  def setRowAxis(self, axis: Optional[QCategory3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::setRowAxis(QCategory3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbars.html#setRowAxis

    Parameters
    ----------

    axis : Optional[QCategory3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::setRowAxis(QCategory3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars10setRowAxisEP15QCategory3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setValueAxis(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::setValueAxis(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbars.html#setValueAxis

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::setValueAxis(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars12setValueAxisEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QCategory3DAxis)
  @overload(NoneType)
  def setColumnAxis(self, axis: Optional[QCategory3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::setColumnAxis(QCategory3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#setColumnAxis

    Parameters
    ----------

    axis : Optional[QCategory3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::setColumnAxis(QCategory3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars13setColumnAxisEP15QCategory3DAxis',
        self._addressOf(axis),
    )

  @overload(bool)
  def setMultiSeriesUniform(self, uniform: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::setMultiSeriesUniform(bool uniform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#setMultiSeriesUniform

    Parameters
    ----------

    uniform : bool
      Passed on as it is.
    """
    #  void QQuickGraphsBars::setMultiSeriesUniform(bool uniform)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars21setMultiSeriesUniformEb', uniform,
    )

  @overload(float)
  def setBarThickness(self, thicknessRatio: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::setBarThickness(float
    thicknessRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#setBarThickness

    Parameters
    ----------

    thicknessRatio : float
      Passed on as it is.
    """
    #  void QQuickGraphsBars::setBarThickness(float thicknessRatio)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars15setBarThicknessEf', thicknessRatio,
    )

  @overload(QSizeF)
  def setBarSpacing(self, spacing: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::setBarSpacing(QSizeF spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#setBarSpacing

    Parameters
    ----------

    spacing : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickGraphsBars::setBarSpacing(QSizeF spacing)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars13setBarSpacingE6QSizeF',
        self._valueOf(spacing),
    )

  @overload(bool)
  def setBarSpacingRelative(self, relative: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::setBarSpacingRelative(bool relative)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#setBarSpacingRelative

    Parameters
    ----------

    relative : bool
      Passed on as it is.
    """
    #  void QQuickGraphsBars::setBarSpacingRelative(bool relative)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars21setBarSpacingRelativeEb', relative,
    )

  @overload(QSizeF)
  def setBarSeriesMargin(self, margin: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::setBarSeriesMargin(QSizeF margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#setBarSeriesMargin

    Parameters
    ----------

    margin : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickGraphsBars::setBarSeriesMargin(QSizeF margin)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars18setBarSeriesMarginE6QSizeF',
        self._valueOf(margin),
    )

  @overload(bool)
  def setMultiSeriesScaling(self, uniform: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::setMultiSeriesScaling(bool uniform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#setMultiSeriesScaling

    Parameters
    ----------

    uniform : bool
      Passed on as it is.
    """
    #  void QQuickGraphsBars::setMultiSeriesScaling(bool uniform)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars21setMultiSeriesScalingEb', uniform,
    )

  @overload()
  @overload(float)
  @overload(float, QSizeF)
  @overload(float, QSizeF, bool)
  def setBarSpecs(
      self,
      thicknessRatio: float = 1.0,
      spacing: Optional[QSizeF] = None,
      relative: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::setBarSpecs(float thicknessRatio,
    QSizeF spacing, bool relative)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbars.html#setBarSpecs

    Parameters
    ----------

    thicknessRatio : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.

    spacing : Optional[QSizeF]
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own. May be left out, as in Qt: a new 'QSizeF(1.0, 1.0)' is then passed
      on.

    relative : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQuickGraphsBars::setBarSpecs(float thicknessRatio, QSizeF
    #      spacing, bool relative)
    if spacing is None:
      from ..QtCore import QSizeF
      spacing = QSizeF(1.0, 1.0)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars11setBarSpecsEf6QSizeFb',
        thicknessRatio, self._valueOf(spacing), relative,
    )

  @overload(float)
  def setFloorLevel(self, level: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::setFloorLevel(float level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#setFloorLevel

    Parameters
    ----------

    level : float
      Passed on as it is.
    """
    #  void QQuickGraphsBars::setFloorLevel(float level)
    self.uglySide.call('ritual_ZN16QQuickGraphsBars13setFloorLevelEf', level)

  @overload(QBar3DSeries)
  @overload(NoneType)
  def setPrimarySeries(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::setPrimarySeries(QBar3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#setPrimarySeries

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::setPrimarySeries(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars16setPrimarySeriesEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(QtGraphs3D.SelectionFlags)
  def setSelectionMode(self, mode: QtGraphs3D.SelectionFlags) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsBars::setSelectionMode(QtGraphs3D::SelectionFlags mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#setSelectionMode

    Parameters
    ----------

    mode : QtGraphs3D.SelectionFlags
      Passed on as its number.
    """
    #  void QQuickGraphsBars::setSelectionMode(QtGraphs3D::SelectionFlags
    #      mode)
    ritual = (
        'ritual_ZN16QQuickGraphsBars16setSelectionModeE6QFlagsIN10QtGraphs3'
        'D13SelectionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsBars16setSelectionModeE6QFlagsIN10QtG'
          'raphs3D13SelectionFlagEE')
    self.uglySide.call(ritual, mode.value)

  @overload(QPoint, QBar3DSeries, bool)
  @overload(QPoint, NoneType, bool)
  def setSelectedBar(
      self,
      coord: QPoint,
      series: Optional[QBar3DSeries],
      enterSlice: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::setSelectedBar(QPoint coord,
    QBar3DSeries *series, bool enterSlice)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#setSelectedBar

    Parameters
    ----------

    coord : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    enterSlice : bool
      Passed on as it is.
    """
    #  void QQuickGraphsBars::setSelectedBar(QPoint coord, QBar3DSeries
    #      *series, bool enterSlice)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars14setSelectedBarE6QPointP12QBar3DSeries'
        'b',
        self._valueOf(coord), self._addressOf(series), enterSlice,
    )

  @overload(bool)
  def setSeriesVisualsDirty(self, dirty: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::setSeriesVisualsDirty(bool dirty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#setSeriesVisualsDirty

    Parameters
    ----------

    dirty : bool
      Passed on as it is.
    """
    #  void QQuickGraphsBars::setSeriesVisualsDirty(bool dirty)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars21setSeriesVisualsDirtyEb', dirty,
    )

  @overload(bool)
  def setDataDirty(self, dirty: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::setDataDirty(bool dirty)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbars.html#setDataDirty

    Parameters
    ----------

    dirty : bool
      Passed on as it is.
    """
    #  void QQuickGraphsBars::setDataDirty(bool dirty)
    self.uglySide.call('ritual_ZN16QQuickGraphsBars12setDataDirtyEb', dirty)

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
    'QQuickGraphsBars::QQuickGraphsBars(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#QQuickGraphsBars

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickGraphsBars::QQuickGraphsBars(QQuickItem *parent)
    self._noteCreation(QQuickGraphsBars, lambda: Rituals.call(
        'ritual_ZN16QQuickGraphsBarsC1EP10QQuickItem',
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

  @overload(QBar3DSeries)
  @overload(NoneType)
  def addSeries(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::addSeries(QBar3DSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbars.html#addSeries

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::addSeries(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars9addSeriesEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(QBar3DSeries)
  @overload(NoneType)
  def removeSeries(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::removeSeries(QBar3DSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbars.html#removeSeries

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::removeSeries(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars12removeSeriesEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(int, QBar3DSeries)
  @overload(int, NoneType)
  def insertSeries(self, index: int, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::insertSeries(qsizetype index,
    QBar3DSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbars.html#insertSeries

    Parameters
    ----------

    index : int
      Passed on as it is.

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::insertSeries(qsizetype index, QBar3DSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars12insertSeriesExP12QBar3DSeries',
        index, self._addressOf(series),
    )

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::clearSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#clearSelection
    """
    #  void QQuickGraphsBars::clearSelection()
    ritual = 'ritual_ZN16QQuickGraphsBars14clearSelectionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsBars14clearSelectionEv'
    self.uglySide.call(ritual)

  @overload(QAbstract3DAxis.AxisOrientation, bool)
  def handleAxisAutoAdjustRangeChangedInOrientation(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      autoAdjust: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsBars::handleAxisAutoAdjustRangeChangedInOrientation(
    QAbstract3DAxis::AxisOrientation orientation, bool autoAdjust)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    autoAdjust : bool
      Passed on as it is.
    """
    #  void QQuickGraphsBars::handleAxisAutoAdjustRangeChangedInOrientation(
    #      QAbstract3DAxis::AxisOrientation orientation, bool autoAdjust)
    ritual = (
        'ritual_ZN16QQuickGraphsBars45handleAxisAutoAdjustRangeChangedInOri'
        'entationEN15QAbstract3DAxis15AxisOrientationEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsBars45handleAxisAutoAdjustRangeChange'
          'dInOrientationEN15QAbstract3DAxis15AxisOrientationEb')
    self.uglySide.call(ritual, orientation.value, autoAdjust)

  @overload(QObject)
  @overload(NoneType)
  def handleSeriesVisibilityChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsBars::handleSeriesVisibilityChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::handleSeriesVisibilityChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN16QQuickGraphsBars37handleSeriesVisibilityChangedBySender'
        'EP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsBars37handleSeriesVisibilityChangedBy'
          'SenderEP7QObject')
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
    QQuickGraphsBars::handleItemLabelVisibleChangedBySender(bool visible,
    QObject *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html

    Parameters
    ----------

    visible : bool
      Passed on as it is.

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::handleItemLabelVisibleChangedBySender(bool
    #      visible, QObject *sender)
    ritual = (
        'ritual_ZN16QQuickGraphsBars37handleItemLabelVisibleChangedBySender'
        'EbP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsBars37handleItemLabelVisibleChangedBy'
          'SenderEbP7QObject')
    self.uglySide.call(ritual, visible, self._addressOf(sender, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleAxisRangeChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::handleAxisRangeChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::handleAxisRangeChangedBySender(QObject *sender)
    ritual = (
        'ritual_ZN16QQuickGraphsBars30handleAxisRangeChangedBySenderEP7QObj'
        'ect')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsBars30handleAxisRangeChangedBySenderE'
          'P7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  def adjustAxisRanges(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::adjustAxisRanges()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#adjustAxisRanges
    """
    #  void QQuickGraphsBars::adjustAxisRanges()
    ritual = 'ritual_ZN16QQuickGraphsBars16adjustAxisRangesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsBars16adjustAxisRangesEv'
    self.uglySide.call(ritual)

  def handleLightingModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::handleLightingModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#handleLightingModeChanged
    """
    #  void QQuickGraphsBars::handleLightingModeChanged()
    ritual = 'ritual_ZN16QQuickGraphsBars25handleLightingModeChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsBars25handleLightingModeChangedEv'
    self.uglySide.call(ritual)

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def handleMultiAxisChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::handleMultiAxisChanged(QAbstract3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#handleMultiAxisChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::handleMultiAxisChanged(QAbstract3DAxis *axis)
    ritual = (
        'ritual_ZN16QQuickGraphsBars22handleMultiAxisChangedEP15QAbstract3D'
        'Axis')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsBars22handleMultiAxisChangedEP15QAbst'
          'ract3DAxis')
    self.uglySide.call(ritual, self._addressOf(axis))

  def barSeriesList(self) -> QList[QBar3DSeries]:
    """
    Calls Qt's 'QList<QBar3DSeries *> QQuickGraphsBars::barSeriesList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#barSeriesList

    Returns
    -------

    QList[QBar3DSeries]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QBar3DSeries *> QQuickGraphsBars::barSeriesList()
    address = self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars13barSeriesListEv',
    )
    from . import QBar3DSeries
    return QList[QBar3DSeries]._cuteOwning(address)

  @overload(int, QtGraphs3D.SliceCaptureType)
  def renderSliceToImage(
      self,
      requestedIndex: int,
      sliceType: QtGraphs3D.SliceCaptureType,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::renderSliceToImage(int requestedIndex,
    QtGraphs3D::SliceCaptureType sliceType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#renderSliceToImage

    Parameters
    ----------

    requestedIndex : int
      Passed on as it is.

    sliceType : QtGraphs3D.SliceCaptureType
      Passed on as its number.
    """
    #  void QQuickGraphsBars::renderSliceToImage(int requestedIndex,
    #      QtGraphs3D::SliceCaptureType sliceType)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars18renderSliceToImageEiN10QtGraphs3D16Sl'
        'iceCaptureTypeE',
        requestedIndex, sliceType.value,
    )

  @overload(int, QtGraphs3D.SliceCaptureType, QUrl)
  def renderSliceToImage(
      self,
      requestedIndex: int,
      sliceType: QtGraphs3D.SliceCaptureType,
      filePath: QUrl,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::renderSliceToImage(int requestedIndex,
    QtGraphs3D::SliceCaptureType sliceType, const QUrl &filePath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#renderSliceToImage

    Parameters
    ----------

    requestedIndex : int
      Passed on as it is.

    sliceType : QtGraphs3D.SliceCaptureType
      Passed on as its number.

    filePath : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickGraphsBars::renderSliceToImage(int requestedIndex,
    #      QtGraphs3D::SliceCaptureType sliceType, const QUrl &filePath)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars18renderSliceToImageEiN10QtGraphs3D16Sl'
        'iceCaptureTypeERK4QUrl',
        requestedIndex, sliceType.value, self._valueOf(filePath),
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#componentComplete
    """
    #  void QQuickGraphsBars::componentComplete()
    ritual = 'ritual_ZN16QQuickGraphsBars17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsBars17componentCompleteEv'
    self.uglySide.call(ritual)

  def synchData(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::synchData()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbars.html#synchData
    """
    #  void QQuickGraphsBars::synchData()
    ritual = 'ritual_ZN16QQuickGraphsBars9synchDataEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsBars9synchDataEv'
    self.uglySide.call(ritual)

  def updateFloor(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::updateFloor()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbars.html#updateFloor
    """
    #  void QQuickGraphsBars::updateFloor()
    self.uglySide.call('ritual_ZN16QQuickGraphsBars11updateFloorEv')

  def updateParameters(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::updateParameters()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#updateParameters
    """
    #  void QQuickGraphsBars::updateParameters()
    self.uglySide.call('ritual_ZN16QQuickGraphsBars16updateParametersEv')

  @overload(float)
  def updateFloorLevel(self, level: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::updateFloorLevel(float level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#updateFloorLevel

    Parameters
    ----------

    level : float
      Passed on as it is.
    """
    #  void QQuickGraphsBars::updateFloorLevel(float level)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars16updateFloorLevelEf', level,
    )

  def updateGraph(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::updateGraph()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbars.html#updateGraph
    """
    #  void QQuickGraphsBars::updateGraph()
    ritual = 'ritual_ZN16QQuickGraphsBars11updateGraphEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsBars11updateGraphEv'
    self.uglySide.call(ritual)

  @overload(float, float)
  def updateAxisRange(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::updateAxisRange(float min, float
    max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#updateAxisRange

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QQuickGraphsBars::updateAxisRange(float min, float max)
    ritual = 'ritual_ZN16QQuickGraphsBars15updateAxisRangeEff'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsBars15updateAxisRangeEff'
    self.uglySide.call(ritual, min, max)

  @overload(bool)
  def updateAxisReversed(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::updateAxisReversed(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#updateAxisReversed

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphsBars::updateAxisReversed(bool enable)
    ritual = 'ritual_ZN16QQuickGraphsBars18updateAxisReversedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsBars18updateAxisReversedEb'
    self.uglySide.call(ritual, enable)

  def updateLightStrength(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::updateLightStrength()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#updateLightStrength
    """
    #  void QQuickGraphsBars::updateLightStrength()
    ritual = 'ritual_ZN16QQuickGraphsBars19updateLightStrengthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsBars19updateLightStrengthEv'
    self.uglySide.call(ritual)

  def calculateSceneScalingFactors(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::calculateSceneScalingFactors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#calculateSceneScalingFactors
    """
    #  void QQuickGraphsBars::calculateSceneScalingFactors()
    ritual = 'ritual_ZN16QQuickGraphsBars28calculateSceneScalingFactorsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsBars28calculateSceneScalingFactorsEv')
    self.uglySide.call(ritual)

  @overload(QAbstract3DAxis, QVector3D, int)
  @overload(NoneType, QVector3D, int)
  def calculateCategoryLabelPosition(
      self,
      axis: Optional[QAbstract3DAxis],
      labelPosition: QVector3D,
      index: int,
  ) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    QQuickGraphsBars::calculateCategoryLabelPosition(QAbstract3DAxis *axis,
    QVector3D labelPosition, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    labelPosition : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    index : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D
    #      QQuickGraphsBars::calculateCategoryLabelPosition(QAbstract3DAxis
    #      *axis, QVector3D labelPosition, int index)
    ritual = (
        'ritual_ZN16QQuickGraphsBars30calculateCategoryLabelPositionEP15QAb'
        'stract3DAxis9QVector3Di')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsBars30calculateCategoryLabelPositionE'
          'P15QAbstract3DAxis9QVector3Di')
    address = self.uglySide.call(
        ritual, self._addressOf(axis), self._valueOf(labelPosition), index,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QAbstract3DAxis, int)
  @overload(NoneType, int)
  def calculateCategoryGridLinePosition(
      self,
      axis: Optional[QAbstract3DAxis],
      index: int,
  ) -> float:
    """
    Calls Qt's 'float
    QQuickGraphsBars::calculateCategoryGridLinePosition(QAbstract3DAxis
    *axis, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  float QQuickGraphsBars::calculateCategoryGridLinePosition(
    #      QAbstract3DAxis *axis, int index)
    ritual = (
        'ritual_ZN16QQuickGraphsBars33calculateCategoryGridLinePositionEP15'
        'QAbstract3DAxisi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsBars33calculateCategoryGridLinePositi'
          'onEP15QAbstract3DAxisi')
    return self.uglySide.call(ritual, self._addressOf(axis), index)

  def createSliceView(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::createSliceView()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#createSliceView
    """
    #  void QQuickGraphsBars::createSliceView()
    ritual = 'ritual_ZN16QQuickGraphsBars15createSliceViewEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsBars15createSliceViewEv'
    self.uglySide.call(ritual)

  def toggleSliceGraph(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::toggleSliceGraph()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#toggleSliceGraph
    """
    #  void QQuickGraphsBars::toggleSliceGraph()
    ritual = 'ritual_ZN16QQuickGraphsBars16toggleSliceGraphEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsBars16toggleSliceGraphEv'
    self.uglySide.call(ritual)

  @overload(QQuick3DRepeater, QColor)
  @overload(NoneType, QColor)
  def handleLabelCountChanged(
      self,
      repeater: Optional[QQuick3DRepeater],
      axisLabelColor: QColor,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsBars::handleLabelCountChanged(QQuick3DRepeater *repeater,
    QColor axisLabelColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#handleLabelCountChanged

    Parameters
    ----------

    repeater : Optional[QQuick3DRepeater]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    axisLabelColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickGraphsBars::handleLabelCountChanged(QQuick3DRepeater
    #      *repeater, QColor axisLabelColor)
    ritual = (
        'ritual_ZN16QQuickGraphsBars23handleLabelCountChangedEP16QQuick3DRe'
        'peater6QColor')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsBars23handleLabelCountChangedEP16QQui'
          'ck3DRepeater6QColor')
    self.uglySide.call(
        ritual, self._addressOf(repeater), self._valueOf(axisLabelColor),
    )

  @overload(QtGraphs3D.SelectionFlags)
  def updateSelectionMode(self, mode: QtGraphs3D.SelectionFlags) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsBars::updateSelectionMode(QtGraphs3D::SelectionFlags mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#updateSelectionMode

    Parameters
    ----------

    mode : QtGraphs3D.SelectionFlags
      Passed on as its number.
    """
    #  void QQuickGraphsBars::updateSelectionMode(QtGraphs3D::SelectionFlags
    #      mode)
    ritual = (
        'ritual_ZN16QQuickGraphsBars19updateSelectionModeE6QFlagsIN10QtGrap'
        'hs3D13SelectionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsBars19updateSelectionModeE6QFlagsIN10'
          'QtGraphs3D13SelectionFlagEE')
    self.uglySide.call(ritual, mode.value)

  @overload(QPointF)
  def doPicking(self, position: QPointF) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsBars::doPicking(QPointF position)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbars.html#doPicking

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QQuickGraphsBars::doPicking(QPointF position)
    ritual = 'ritual_ZN16QQuickGraphsBars9doPickingE7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsBars9doPickingE7QPointF'
    return self.uglySide.call(ritual, self._valueOf(position, 'QPointF'))

  @overload(QVector3D, QVector3D)
  def doRayPicking(self, origin: QVector3D, direction: QVector3D) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsBars::doRayPicking(QVector3D origin,
    QVector3D direction)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbars.html#doRayPicking

    Parameters
    ----------

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  bool QQuickGraphsBars::doRayPicking(QVector3D origin, QVector3D
    #      direction)
    ritual = 'ritual_ZN16QQuickGraphsBars12doRayPickingE9QVector3DS0_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsBars12doRayPickingE9QVector3DS0_'
    return self.uglySide.call(
        ritual, self._valueOf(origin), self._valueOf(direction),
    )

  @overload(QAbstract3DAxis.AxisOrientation)
  def createDefaultAxis(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
  ) -> Optional[QAbstract3DAxis]:
    """
    Calls Qt's 'QAbstract3DAxis
    *QQuickGraphsBars::createDefaultAxis(QAbstract3DAxis::AxisOrientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#createDefaultAxis

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    Returns
    -------

    Optional[QAbstract3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DAxis *QQuickGraphsBars::createDefaultAxis(QAbstract3DAxis::
    #      AxisOrientation orientation)
    ritual = (
        'ritual_ZN16QQuickGraphsBars17createDefaultAxisEN15QAbstract3DAxis1'
        '5AxisOrientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsBars17createDefaultAxisEN15QAbstract3'
          'DAxis15AxisOrientationE')
    address = self.uglySide.call(ritual, orientation.value)
    return QAbstract3DAxis._cuteAt(address)

  @overload(str, QVector3D)
  def updateSliceItemLabel(self, label: str, position: QVector3D) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::updateSliceItemLabel(const QString
    &label, QVector3D position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#updateSliceItemLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuickGraphsBars::updateSliceItemLabel(const QString &label,
    #      QVector3D position)
    ritual = (
        'ritual_ZN16QQuickGraphsBars20updateSliceItemLabelERK7QString9QVect'
        'or3D')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsBars20updateSliceItemLabelERK7QString'
          '9QVector3D')
    self.uglySide.call(ritual, label, self._valueOf(position))

  @overload(QAbstract3DSeries, QAbstract3DAxis.AxisOrientation)
  @overload(NoneType, QAbstract3DAxis.AxisOrientation)
  def getSeriesMultiAxis(
      self,
      series: Optional[QAbstract3DSeries],
      orientation: QAbstract3DAxis.AxisOrientation,
  ) -> Optional[QAbstract3DAxis]:
    """
    Calls Qt's 'QAbstract3DAxis
    *QQuickGraphsBars::getSeriesMultiAxis(QAbstract3DSeries *series,
    QAbstract3DAxis::AxisOrientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#getSeriesMultiAxis

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
    #      *QQuickGraphsBars::getSeriesMultiAxis(QAbstract3DSeries *series,
    #      QAbstract3DAxis::AxisOrientation orientation)
    ritual = (
        'ritual_ZN16QQuickGraphsBars18getSeriesMultiAxisEP17QAbstract3DSeri'
        'esN15QAbstract3DAxis15AxisOrientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsBars18getSeriesMultiAxisEP17QAbstract'
          '3DSeriesN15QAbstract3DAxis15AxisOrientationE')
    address = self.uglySide.call(
        ritual, self._addressOf(series), orientation.value,
    )
    return QAbstract3DAxis._cuteAt(address)

  @overload(int, QtGraphs3D.SliceCaptureType)
  def createOffscreenSliceView(
      self,
      requestedIndex: int,
      sliceType: QtGraphs3D.SliceCaptureType,
  ) -> Optional[QQuick3DViewport]:
    """
    Calls Qt's 'QQuick3DViewport
    *QQuickGraphsBars::createOffscreenSliceView(int requestedIndex,
    QtGraphs3D::SliceCaptureType sliceType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#createOffscreenSliceView

    Parameters
    ----------

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
    #  QQuick3DViewport *QQuickGraphsBars::createOffscreenSliceView(int
    #      requestedIndex, QtGraphs3D::SliceCaptureType sliceType)
    address = self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars24createOffscreenSliceViewEiN10QtGraphs'
        '3D16SliceCaptureTypeE',
        requestedIndex, sliceType.value,
    )
    return QQuick3DViewport._cuteAt(address)

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def handleAxisXChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::handleAxisXChanged(QAbstract3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#handleAxisXChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::handleAxisXChanged(QAbstract3DAxis *axis)
    ritual = (
        'ritual_ZN16QQuickGraphsBars18handleAxisXChangedEP15QAbstract3DAxis')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsBars18handleAxisXChangedEP15QAbstract'
          '3DAxis')
    self.uglySide.call(ritual, self._addressOf(axis))

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def handleAxisYChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::handleAxisYChanged(QAbstract3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#handleAxisYChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::handleAxisYChanged(QAbstract3DAxis *axis)
    ritual = (
        'ritual_ZN16QQuickGraphsBars18handleAxisYChangedEP15QAbstract3DAxis')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsBars18handleAxisYChangedEP15QAbstract'
          '3DAxis')
    self.uglySide.call(ritual, self._addressOf(axis))

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def handleAxisZChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::handleAxisZChanged(QAbstract3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#handleAxisZChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::handleAxisZChanged(QAbstract3DAxis *axis)
    ritual = (
        'ritual_ZN16QQuickGraphsBars18handleAxisZChangedEP15QAbstract3DAxis')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsBars18handleAxisZChangedEP15QAbstract'
          '3DAxis')
    self.uglySide.call(ritual, self._addressOf(axis))

  @overload(QAbstract3DSeries.Mesh)
  def handleSeriesMeshChanged(self, mesh: QAbstract3DSeries.Mesh) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsBars::handleSeriesMeshChanged(QAbstract3DSeries::Mesh mesh)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#handleSeriesMeshChanged

    Parameters
    ----------

    mesh : QAbstract3DSeries.Mesh
      Passed on as its number.
    """
    #  void QQuickGraphsBars::handleSeriesMeshChanged(QAbstract3DSeries::Mesh
    #      mesh)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars23handleSeriesMeshChangedEN17QAbstract3'
        'DSeries4MeshE',
        mesh.value,
    )

  @overload(bool)
  def handleMeshSmoothChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::handleMeshSmoothChanged(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#handleMeshSmoothChanged

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphsBars::handleMeshSmoothChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars23handleMeshSmoothChangedEb', enable,
    )

  def handleCameraRotationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::handleCameraRotationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#handleCameraRotationChanged
    """
    #  void QQuickGraphsBars::handleCameraRotationChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars27handleCameraRotationChangedEv',
    )

  def handleArrayReset(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::handleArrayReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#handleArrayReset
    """
    #  void QQuickGraphsBars::handleArrayReset()
    self.uglySide.call('ritual_ZN16QQuickGraphsBars16handleArrayResetEv')

  @overload(int, int)
  def handleRowsAdded(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::handleRowsAdded(qsizetype startIndex,
    qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#handleRowsAdded

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQuickGraphsBars::handleRowsAdded(qsizetype startIndex, qsizetype
    #      count)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars15handleRowsAddedExx', startIndex, count,
    )

  @overload(int, int)
  def handleRowsChanged(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::handleRowsChanged(qsizetype
    startIndex, qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#handleRowsChanged

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQuickGraphsBars::handleRowsChanged(qsizetype startIndex,
    #      qsizetype count)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars17handleRowsChangedExx',
        startIndex, count,
    )

  @overload(int, int)
  def handleRowsRemoved(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::handleRowsRemoved(qsizetype
    startIndex, qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#handleRowsRemoved

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQuickGraphsBars::handleRowsRemoved(qsizetype startIndex,
    #      qsizetype count)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars17handleRowsRemovedExx',
        startIndex, count,
    )

  @overload(int, int)
  def handleRowsInserted(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::handleRowsInserted(qsizetype
    startIndex, qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#handleRowsInserted

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQuickGraphsBars::handleRowsInserted(qsizetype startIndex,
    #      qsizetype count)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars18handleRowsInsertedExx',
        startIndex, count,
    )

  @overload(int, int)
  def handleItemChanged(self, rowIndex: int, columnIndex: int) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::handleItemChanged(qsizetype rowIndex,
    qsizetype columnIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#handleItemChanged

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.

    columnIndex : int
      Passed on as it is.
    """
    #  void QQuickGraphsBars::handleItemChanged(qsizetype rowIndex, qsizetype
    #      columnIndex)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars17handleItemChangedExx',
        rowIndex, columnIndex,
    )

  def handleDataRowLabelsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::handleDataRowLabelsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#handleDataRowLabelsChanged
    """
    #  void QQuickGraphsBars::handleDataRowLabelsChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars26handleDataRowLabelsChangedEv',
    )

  def handleDataColumnLabelsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::handleDataColumnLabelsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html
    """
    #  void QQuickGraphsBars::handleDataColumnLabelsChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars29handleDataColumnLabelsChangedEv',
    )

  def handleRowColorsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::handleRowColorsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#handleRowColorsChanged
    """
    #  void QQuickGraphsBars::handleRowColorsChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars22handleRowColorsChangedEv',
    )

  def handleValueColoringChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::handleValueColoringChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#handleValueColoringChanged
    """
    #  void QQuickGraphsBars::handleValueColoringChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars26handleValueColoringChangedEv',
    )

  @overload(QCategory3DAxis)
  @overload(NoneType)
  def rowAxisChanged(self, axis: Optional[QCategory3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::rowAxisChanged(QCategory3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#rowAxisChanged

    Parameters
    ----------

    axis : Optional[QCategory3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::rowAxisChanged(QCategory3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars14rowAxisChangedEP15QCategory3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def valueAxisChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::valueAxisChanged(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#valueAxisChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::valueAxisChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars16valueAxisChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QCategory3DAxis)
  @overload(NoneType)
  def columnAxisChanged(self, axis: Optional[QCategory3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::columnAxisChanged(QCategory3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#columnAxisChanged

    Parameters
    ----------

    axis : Optional[QCategory3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::columnAxisChanged(QCategory3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars17columnAxisChangedEP15QCategory3DAxis',
        self._addressOf(axis),
    )

  @overload(bool)
  def multiSeriesUniformChanged(self, uniform: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::multiSeriesUniformChanged(bool
    uniform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#multiSeriesUniformChanged

    Parameters
    ----------

    uniform : bool
      Passed on as it is.
    """
    #  void QQuickGraphsBars::multiSeriesUniformChanged(bool uniform)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars25multiSeriesUniformChangedEb', uniform,
    )

  @overload(float)
  def barThicknessChanged(self, thicknessRatio: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::barThicknessChanged(float
    thicknessRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#barThicknessChanged

    Parameters
    ----------

    thicknessRatio : float
      Passed on as it is.
    """
    #  void QQuickGraphsBars::barThicknessChanged(float thicknessRatio)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars19barThicknessChangedEf', thicknessRatio,
    )

  @overload(QSizeF)
  def barSpacingChanged(self, spacing: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::barSpacingChanged(QSizeF spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#barSpacingChanged

    Parameters
    ----------

    spacing : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickGraphsBars::barSpacingChanged(QSizeF spacing)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars17barSpacingChangedE6QSizeF',
        self._valueOf(spacing),
    )

  @overload(bool)
  def barSpacingRelativeChanged(self, relative: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::barSpacingRelativeChanged(bool
    relative)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#barSpacingRelativeChanged

    Parameters
    ----------

    relative : bool
      Passed on as it is.
    """
    #  void QQuickGraphsBars::barSpacingRelativeChanged(bool relative)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars25barSpacingRelativeChangedEb', relative,
    )

  @overload(QSizeF)
  def barSeriesMarginChanged(self, margin: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::barSeriesMarginChanged(QSizeF
    margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#barSeriesMarginChanged

    Parameters
    ----------

    margin : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickGraphsBars::barSeriesMarginChanged(QSizeF margin)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars22barSeriesMarginChangedE6QSizeF',
        self._valueOf(margin),
    )

  @overload(str)
  def meshFileNameChanged(self, filename: str) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::meshFileNameChanged(const QString
    &filename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#meshFileNameChanged

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickGraphsBars::meshFileNameChanged(const QString &filename)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars19meshFileNameChangedERK7QString',
        filename,
    )

  @overload(QBar3DSeries)
  @overload(NoneType)
  def primarySeriesChanged(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::primarySeriesChanged(QBar3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#primarySeriesChanged

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::primarySeriesChanged(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars20primarySeriesChangedEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(QBar3DSeries)
  @overload(NoneType)
  def selectedSeriesChanged(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::selectedSeriesChanged(QBar3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#selectedSeriesChanged

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::selectedSeriesChanged(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars21selectedSeriesChangedEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(float)
  def floorLevelChanged(self, level: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::floorLevelChanged(float level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#floorLevelChanged

    Parameters
    ----------

    level : float
      Passed on as it is.
    """
    #  void QQuickGraphsBars::floorLevelChanged(float level)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars17floorLevelChangedEf', level,
    )

  @overload(QImage)
  def sliceImageChanged(self, image: QImage) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::sliceImageChanged(const QImage
    &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#sliceImageChanged

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QQuickGraphsBars::sliceImageChanged(const QImage &image)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars17sliceImageChangedERK6QImage',
        self._valueOf(image),
    )

  def calculateHeightAdjustment(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::calculateHeightAdjustment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#calculateHeightAdjustment
    """
    #  void QQuickGraphsBars::calculateHeightAdjustment()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars25calculateHeightAdjustmentEv',
    )

  def calculateSeriesStartPosition(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::calculateSeriesStartPosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#calculateSeriesStartPosition
    """
    #  void QQuickGraphsBars::calculateSeriesStartPosition()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars28calculateSeriesStartPositionEv',
    )

  @overload(QBar3DSeries)
  @overload(NoneType)
  def connectSeries(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::connectSeries(QBar3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#connectSeries

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::connectSeries(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars13connectSeriesEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(QBar3DSeries)
  @overload(NoneType)
  def disconnectSeries(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::disconnectSeries(QBar3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#disconnectSeries

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::disconnectSeries(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars16disconnectSeriesEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(QQuick3DNode, QAbstract3DSeries)
  @overload(QQuick3DNode, NoneType)
  @overload(NoneType, QAbstract3DSeries)
  @overload(NoneType, NoneType)
  def createDataItem(
      self,
      scene: Optional[QQuick3DNode],
      series: Optional[QAbstract3DSeries],
  ) -> Optional[QQuick3DModel]:
    """
    Calls Qt's 'QQuick3DModel *QQuickGraphsBars::createDataItem(QQuick3DNode
    *scene, QAbstract3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#createDataItem

    Parameters
    ----------

    scene : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuick3DModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DModel *QQuickGraphsBars::createDataItem(QQuick3DNode *scene,
    #      QAbstract3DSeries *series)
    address = self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars14createDataItemEP12QQuick3DNodeP17QAbs'
        'tract3DSeries',
        self._addressOf(scene), self._addressOf(series),
    )
    from ..QtQuick3D import QQuick3DModel
    return QQuick3DModel._cuteAt(address)

  def getMeshFileName(self) -> str:
    """
    Calls Qt's 'QString QQuickGraphsBars::getMeshFileName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#getMeshFileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickGraphsBars::getMeshFileName()
    return self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars15getMeshFileNameEv',
    )

  @overload(QBar3DSeries, int)
  @overload(NoneType, int)
  def updateBarVisuality(
      self,
      series: Optional[QBar3DSeries],
      visualIndex: int,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::updateBarVisuality(QBar3DSeries
    *series, int visualIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#updateBarVisuality

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    visualIndex : int
      Passed on as it is.
    """
    #  void QQuickGraphsBars::updateBarVisuality(QBar3DSeries *series, int
    #      visualIndex)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars18updateBarVisualityEP12QBar3DSeriesi',
        self._addressOf(series), visualIndex,
    )

  @overload(QBar3DSeries)
  @overload(NoneType)
  def updateBarPositions(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::updateBarPositions(QBar3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#updateBarPositions

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::updateBarPositions(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars18updateBarPositionsEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(QBarDataItem)
  @overload(NoneType)
  @overload(QBarDataItem, QValue3DAxis)
  @overload(QBarDataItem, NoneType)
  @overload(NoneType, QValue3DAxis)
  @overload(NoneType, NoneType)
  def updateBarHeightParameters(
      self,
      item: Optional[QBarDataItem],
      axis: Optional[QValue3DAxis] = None,
  ) -> float:
    """
    Calls Qt's 'float QQuickGraphsBars::updateBarHeightParameters(const
    QBarDataItem *item, QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#updateBarHeightParameters

    Parameters
    ----------

    item : Optional[QBarDataItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  float QQuickGraphsBars::updateBarHeightParameters(const QBarDataItem
    #      *item, QValue3DAxis *axis)
    return self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars25updateBarHeightParametersEPK12QBarDat'
        'aItemP12QValue3DAxis',
        self._addressOf(item), self._addressOf(axis),
    )

  @overload(QBar3DSeries)
  @overload(NoneType)
  def updateBarVisuals(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::updateBarVisuals(QBar3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#updateBarVisuals

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::updateBarVisuals(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars16updateBarVisualsEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(QQuick3DModel, bool, bool, str)
  @overload(NoneType, bool, bool, str)
  def updateItemMaterial(
      self,
      item: Optional[QQuick3DModel],
      useGradient: bool,
      rangeGradient: bool,
      materialName: str,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::updateItemMaterial(QQuick3DModel
    *item, bool useGradient, bool rangeGradient, const QString
    &materialName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#updateItemMaterial

    Parameters
    ----------

    item : Optional[QQuick3DModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    useGradient : bool
      Passed on as it is.

    rangeGradient : bool
      Passed on as it is.

    materialName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickGraphsBars::updateItemMaterial(QQuick3DModel *item, bool
    #      useGradient, bool rangeGradient, const QString &materialName)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars18updateItemMaterialEP13QQuick3DModelbb'
        'RK7QString',
        self._addressOf(item), useGradient, rangeGradient, materialName,
    )

  @overload(QQuick3DModel, bool, bool, QQuick3DTexture, QColor)
  @overload(QQuick3DModel, bool, bool, NoneType, QColor)
  @overload(NoneType, bool, bool, QQuick3DTexture, QColor)
  @overload(NoneType, bool, bool, NoneType, QColor)
  @overload(QQuick3DModel, bool, bool, QQuick3DTexture, QColor, bool)
  @overload(QQuick3DModel, bool, bool, NoneType, QColor, bool)
  @overload(NoneType, bool, bool, QQuick3DTexture, QColor, bool)
  @overload(NoneType, bool, bool, NoneType, QColor, bool)
  def updateMaterialProperties(
      self,
      item: Optional[QQuick3DModel],
      isHighlight: bool,
      isMultiHighlight: bool,
      texture: Optional[QQuick3DTexture],
      color: QColor,
      transparency: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::updateMaterialProperties(QQuick3DModel
    *item, const bool isHighlight, const bool isMultiHighlight,
    QQuick3DTexture *texture, QColor color, const bool transparency)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#updateMaterialProperties

    Parameters
    ----------

    item : Optional[QQuick3DModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    isHighlight : bool
      Passed on as it is.

    isMultiHighlight : bool
      Passed on as it is.

    texture : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    transparency : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickGraphsBars::updateMaterialProperties(QQuick3DModel *item,
    #      const bool isHighlight, const bool isMultiHighlight,
    #      QQuick3DTexture *texture, QColor color, const bool transparency)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars24updateMaterialPropertiesEP13QQuick3DM'
        'odelbbP15QQuick3DTexture6QColorb',
        self._addressOf(item), isHighlight, isMultiHighlight,
        self._addressOf(texture), self._valueOf(color), transparency,
    )

  def removeBarModels(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::removeBarModels()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#removeBarModels
    """
    #  void QQuickGraphsBars::removeBarModels()
    self.uglySide.call('ritual_ZN16QQuickGraphsBars15removeBarModelsEv')

  @overload(QQuick3DModel)
  @overload(NoneType)
  def deleteBarModels(self, model: Optional[QQuick3DModel]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::deleteBarModels(QQuick3DModel
    *model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#deleteBarModels

    Parameters
    ----------

    model : Optional[QQuick3DModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::deleteBarModels(QQuick3DModel *model)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars15deleteBarModelsEP13QQuick3DModel',
        self._addressOf(model),
    )

  @overload(BarInstancing)
  @overload(NoneType)
  def deleteBarItemHolders(
      self,
      instancing: Optional[BarInstancing],
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::deleteBarItemHolders(BarInstancing
    *instancing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#deleteBarItemHolders

    Parameters
    ----------

    instancing : Optional[BarInstancing]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBars::deleteBarItemHolders(BarInstancing *instancing)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars20deleteBarItemHoldersEP13BarInstancing',
        self._addressOf(instancing),
    )

  def createTexture(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuickGraphsBars::createTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#createTexture

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuickGraphsBars::createTexture()
    address = self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars13createTextureEv',
    )
    from ..QtQuick3D import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def updateSelectedBar(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::updateSelectedBar()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#updateSelectedBar
    """
    #  void QQuickGraphsBars::updateSelectedBar()
    self.uglySide.call('ritual_ZN16QQuickGraphsBars17updateSelectedBarEv')

  def resetClickedStatus(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::resetClickedStatus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#resetClickedStatus
    """
    #  void QQuickGraphsBars::resetClickedStatus()
    self.uglySide.call('ritual_ZN16QQuickGraphsBars18resetClickedStatusEv')

  def removeSlicedBarModels(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::removeSlicedBarModels()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#removeSlicedBarModels
    """
    #  void QQuickGraphsBars::removeSlicedBarModels()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars21removeSlicedBarModelsEv',
    )

  @overload(float, QSizeF, bool)
  def updateBarSpecs(
      self,
      thicknessRatio: float,
      spacing: QSizeF,
      relative: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::updateBarSpecs(float thicknessRatio,
    QSizeF spacing, bool relative)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#updateBarSpecs

    Parameters
    ----------

    thicknessRatio : float
      Passed on as it is.

    spacing : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    relative : bool
      Passed on as it is.
    """
    #  void QQuickGraphsBars::updateBarSpecs(float thicknessRatio, QSizeF
    #      spacing, bool relative)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars14updateBarSpecsEf6QSizeFb',
        thicknessRatio, self._valueOf(spacing), relative,
    )

  @overload(QSizeF)
  def updateBarSeriesMargin(self, margin: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickGraphsBars::updateBarSeriesMargin(QSizeF margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbars.html#updateBarSeriesMargin

    Parameters
    ----------

    margin : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickGraphsBars::updateBarSeriesMargin(QSizeF margin)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsBars21updateBarSeriesMarginE6QSizeF',
        self._valueOf(margin),
    )

  @staticmethod
  def adjustSelectionPosition(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsBars::adjustSelectionPosition(QPoint &pos, const
    QBar3DSeries *series)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsBars.adjustSelectionPosition' has no cute function "
        "yet. Qt's 'void QQuickGraphsBars::adjustSelectionPosition(QPoint "
        "&pos, const QBar3DSeries *series)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def appendSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickGraphsBars::appendSeriesFunc(QQmlListProperty<QBar3DSeries> *list,
    QBar3DSeries *series)': names 'QQmlListProperty<QBar3DSeries>', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsBars.appendSeriesFunc' has no cute function yet. Qt's "
        "'void "
        "QQuickGraphsBars::appendSeriesFunc(QQmlListProperty<QBar3DSeries> "
        "*list, QBar3DSeries *series)': names "
        "'QQmlListProperty<QBar3DSeries>', which has no cute class yet.")

  @staticmethod
  def atSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'QBar3DSeries
    *QQuickGraphsBars::atSeriesFunc(QQmlListProperty<QBar3DSeries> *list,
    qsizetype index)': names 'QQmlListProperty<QBar3DSeries>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsBars.atSeriesFunc' has no cute function yet. Qt's "
        "'QBar3DSeries "
        "*QQuickGraphsBars::atSeriesFunc(QQmlListProperty<QBar3DSeries> "
        "*list, qsizetype index)': names 'QQmlListProperty<QBar3DSeries>', "
        "which has no cute class yet.")

  @staticmethod
  def clearSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickGraphsBars::clearSeriesFunc(QQmlListProperty<QBar3DSeries> *list)':
    names 'QQmlListProperty<QBar3DSeries>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsBars.clearSeriesFunc' has no cute function yet. Qt's "
        "'void "
        "QQuickGraphsBars::clearSeriesFunc(QQmlListProperty<QBar3DSeries> "
        "*list)': names 'QQmlListProperty<QBar3DSeries>', which has no cute "
        "class yet.")

  @staticmethod
  def countSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQuickGraphsBars::countSeriesFunc(QQmlListProperty<QBar3DSeries> *list)':
    names 'QQmlListProperty<QBar3DSeries>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsBars.countSeriesFunc' has no cute function yet. Qt's "
        "'qsizetype "
        "QQuickGraphsBars::countSeriesFunc(QQmlListProperty<QBar3DSeries> "
        "*list)': names 'QQmlListProperty<QBar3DSeries>', which has no cute "
        "class yet.")

  @staticmethod
  def createBarItemHolders(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsBars::createBarItemHolders(QBar3DSeries *series,
    QList<BarModel *> barList, bool slice)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsBars.createBarItemHolders' has no cute function yet. "
        "Qt's 'void QQuickGraphsBars::createBarItemHolders(QBar3DSeries "
        "*series, QList<BarModel *> barList, bool slice)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def fixMeshFileName(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsBars::fixMeshFileName(QString &fileName,
    QAbstract3DSeries::Mesh meshType)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsBars.fixMeshFileName' has no cute function yet. Qt's "
        "'void QQuickGraphsBars::fixMeshFileName(QString &fileName, "
        "QAbstract3DSeries::Mesh meshType)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def generateBars(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsBars::generateBars(QList<QBar3DSeries *>
    &barSeriesList)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsBars.generateBars' has no cute function yet. Qt's "
        "'void QQuickGraphsBars::generateBars(QList<QBar3DSeries *> "
        "&barSeriesList)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def isSelected(*__, **_) -> Never:
    """
    Qt's 'SelectionType QQuickGraphsBars::isSelected(int row, int bar,
    QBar3DSeries *series)': gives the enum 'QQuickGraphsBars::SelectionType',
    whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QQuickGraphsBars.isSelected' has no cute function yet. Qt's "
        "'SelectionType QQuickGraphsBars::isSelected(int row, int bar, "
        "QBar3DSeries *series)': gives the enum "
        "'QQuickGraphsBars::SelectionType', whose class cannot be named "
        "here.")
