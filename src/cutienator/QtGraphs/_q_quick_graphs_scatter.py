"""
QQuickGraphsScatter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qquickgraphsscatter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickGraphsScatter to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject
from ..QtQuick import QQuickItem
from . import QtGraphs3D, QAbstract3DAxis, QQuickGraphsItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF
  from ..QtGui import QColor, QVector3D
  from . import QAbstract3DSeries, QScatter3DSeries, QValue3DAxis
  from ..QtQuick3D import QQuick3DModel, QQuick3DNode, QQuick3DTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstract3DSeries = WAIT['QtGraphs:QAbstract3DSeries']
  QColor = WAIT['QColor']
  QPointF = WAIT['QPointF']
  QQuick3DModel = WAIT['QQuick3DModel']
  QQuick3DTexture = WAIT['QQuick3DTexture']
  QScatter3DSeries = WAIT['QtGraphs:QScatter3DSeries']
  QValue3DAxis = WAIT['QtGraphs:QValue3DAxis']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGraphsScatter(QQuickGraphsItem):
  """
  The cute side of Qt's QQuickGraphsScatter: a plain Python object standing
  in front of one C++ QQuickGraphsScatter.

  It is built on the cute 'QQuickGraphsItem', as Qt's QQuickGraphsScatter is
  built on Qt's QQuickGraphsItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickGraphsScatter that has a ritual and that
  Python can call so far, 81 names in all: 'metaObject', 'tr', 'setAxisX',
  'axisX', 'setAxisY', 'axisY', 'setAxisZ', 'axisZ', 'clearSelection',
  'addSeries', 'removeSeries', 'scatterSeriesList', 'selectedSeries',
  'setSelectedItem', 'invalidSelectionIndex', 'setSelectionMode',
  'hasSelectedItemChanged', 'setSelectedItemChanged', 'hasItemChanged',
  'setItemChanged', 'handleAxisAutoAdjustRangeChangedInOrientation',
  'handleAxisRangeChangedBySender', 'adjustAxisRanges',
  'handleMultiAxisChanged', 'hasChangedSeriesList', 'isSeriesVisualsDirty',
  'setSeriesVisualsDirty', 'isDataDirty', 'handleLightingModeChanged',
  'handleAxisXChanged', 'handleAxisYChanged', 'handleAxisZChanged',
  'handleSeriesMeshChanged', 'handleMeshSmoothChanged', 'handleArrayReset',
  'handleItemsAdded', 'handleItemsChanged', 'handleItemsRemoved',
  'handleItemsInserted', 'axisXChanged', 'axisYChanged', 'axisZChanged',
  'selectedSeriesChanged', 'calculateSceneScalingFactors',
  'componentComplete', 'doPicking', 'doRayPicking', 'updateShadowQuality',
  'updateLightStrength', 'startRecordingRemovesAndInserts',
  'getSeriesMultiAxis', 'connectSeries', 'disconnectSeries', 'getItemIndex',
  'selectedItemPosition', 'updateItemMaterial', 'updateMaterialProperties',
  'createTexture', 'createSeriesRoot', 'createDataItem', 'getMeshFileName',
  'deleteDataItem', 'recreateDataItems', 'sizeDifference',
  'handleSeriesChanged', 'selectedItemInSeries', 'isDotPositionInAxisRange',
  'calculatePointScaleSize', 'updatePointScaleSize', 'handleSplineChanged',
  'selected', 'setSelected', 'clearSelectionModel',
  'clearAllSelectionInstanced', 'handleItemLabelVisibleChangedBySender',
  'optimizationChanged', 'updateGraph', 'synchData',
  'handleOptimizationHintChange', 'handleSeriesVisibilityChangedBySender',
  'cameraRotationChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGraphsScatter::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickGraphsScatter::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickGraphsScatter::~QQuickGraphsScatter()': the destructor:
    Python never removes a C++ QQuickGraphsScatter.
  - Qt's 'QQmlListProperty<QScatter3DSeries>
    QQuickGraphsScatter::seriesList()': gives a type Python has no way to
    take yet.
  - Qt's 'void
    QQuickGraphsScatter::appendSeriesFunc(QQmlListProperty<QScatter3DSeries>
    *list, QScatter3DSeries *series)': names
    'QQmlListProperty<QScatter3DSeries>', which has no cute class yet.
  - Qt's 'qsizetype
    QQuickGraphsScatter::countSeriesFunc(QQmlListProperty<QScatter3DSeries>
    *list)': names 'QQmlListProperty<QScatter3DSeries>', which has no cute
    class yet.
  - Qt's 'QScatter3DSeries
    *QQuickGraphsScatter::atSeriesFunc(QQmlListProperty<QScatter3DSeries>
    *list, qsizetype index)': names 'QQmlListProperty<QScatter3DSeries>',
    which has no cute class yet.
  - Qt's 'void
    QQuickGraphsScatter::clearSeriesFunc(QQmlListProperty<QScatter3DSeries>
    *list)': names 'QQmlListProperty<QScatter3DSeries>', which has no cute
    class yet.
  - Qt's 'void QQuickGraphsScatter::updateMaterialReference(ScatterModel
    *model)': names 'QQuickGraphsScatter::ScatterModel', which has no cute
    class yet.
  - Qt's 'void
    QQuickGraphsScatter::updateInstancedMaterialProperties(ScatterModel
    *graphModel, const bool isHighlight, QQuick3DTexture *seriesTexture,
    QQuick3DTexture *highlightTexture, const bool transparency)': names
    'QQuickGraphsScatter::ScatterModel', which has no cute class yet.
  - Qt's 'void QQuickGraphsScatter::removeDataItems(ScatterModel *graphModel,
    QtGraphs3D::OptimizationHint optimizationHint)': names
    'QQuickGraphsScatter::ScatterModel', which has no cute class yet.
  - Qt's 'void QQuickGraphsScatter::fixMeshFileName(QString &fileName,
    QAbstract3DSeries *series)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQuickGraphsScatter::removeDataItems(QList<QQuick3DModel *>
    &items, qsizetype count)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQuickGraphsScatter::recreateDataItems(const
    QList<ScatterModel *> &a0)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQuickGraphsScatter::addPointsToScatterModel(ScatterModel
    *graphModel, qsizetype count)': names
    'QQuickGraphsScatter::ScatterModel', which has no cute class yet.
  - Qt's 'void QQuickGraphsScatter::calculatePolarXZ(const float posX, const
    float posZ, float &x, float &z) const': takes a number to change where it
    is.
  - Qt's 'void QQuickGraphsScatter::updateSpline(ScatterModel *model)': names
    'QQuickGraphsScatter::ScatterModel', which has no cute class yet.
  - Qt's 'void QQuickGraphsScatter::createSplineModel(ScatterModel *model)':
    names 'QQuickGraphsScatter::ScatterModel', which has no cute class yet.
  - Qt's 'void
    QQuickGraphsScatter::generatePointsForScatterModel(ScatterModel
    *series)': names 'QQuickGraphsScatter::ScatterModel', which has no cute
    class yet.
  - Qt's 'void
    QQuickGraphsScatter::updateScatterGraphItemPositions(ScatterModel
    *graphModel)': names 'QQuickGraphsScatter::ScatterModel', which has no
    cute class yet.
  - Qt's 'void
    QQuickGraphsScatter::updateScatterGraphItemVisuals(ScatterModel
    *graphModel)': names 'QQuickGraphsScatter::ScatterModel', which has no
    cute class yet.
  - Qt's 'bool QQuickGraphsScatter::selectedItemInRange(const ScatterModel
    *graphModel)': names 'QQuickGraphsScatter::ScatterModel', which has no
    cute class yet.
  - Qt's 'ScatterModel *QQuickGraphsScatter::findGraphModel(QScatter3DSeries
    *series)': gives 'QQuickGraphsScatter::ScatterModel', which has no cute
    class yet.

  What has no ritual
  ------------------

  4 of the 110 functions Qt declares: 4 not a gap.

  What to expect
  --------------

  - The C++ QQuickGraphsScatter is created at the first use, not by
    'QQuickGraphsScatter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGraphsScatter.
  - Qt tells when it has removed the C++ QQuickGraphsScatter. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickGraphsScatter that has no cute function yet,
    'addPointsToScatterModel', 'appendSeriesFunc', 'atSeriesFunc',
    'calculatePolarXZ', 'clearSeriesFunc', 'countSeriesFunc',
    'createSplineModel', 'findGraphModel', 'fixMeshFileName',
    'generatePointsForScatterModel', 'removeDataItems',
    'selectedItemInRange', 'updateInstancedMaterialProperties',
    'updateMaterialReference', 'updateScatterGraphItemPositions',
    'updateScatterGraphItemVisuals', 'updateSpline', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QQuickGraphsScatter, each a class in here
  #  as in C++.

  class ChangeItem(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickGraphsScatter::ChangeItem: a plain Python
    object standing in front of one C++ QQuickGraphsScatter::ChangeItem.

    C++ hands a QQuickGraphsScatter::ChangeItem around as a copy, so every
    C++ QQuickGraphsScatter::ChangeItem behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQuickGraphsScatter::ChangeItem yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickGraphsScatter::ChangeItem::~ChangeItem()': the destructor:
      Python removes its C++ QQuickGraphsScatter::ChangeItem by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QQuickGraphsScatter::ChangeItem is created at the first use,
      not by 'QQuickGraphsScatter::ChangeItem(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickGraphsScatter::ChangeItem back gives a copy
      the ritual made for Python, in a new cute
      QQuickGraphsScatter::ChangeItem.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickGraphsScatter::ChangeItem'

    #  Qt's '~QQuickGraphsScatter::ChangeItem()'. Naming it makes this a
    #  value class: Python owns every C++ QQuickGraphsScatter::ChangeItem
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN19QQuickGraphsScatter10ChangeItemD1Ev'

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
    Calls Qt's 'QString QQuickGraphsScatter::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsscatter.html#tr

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
    #  QString QQuickGraphsScatter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickGraphsScatter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def invalidSelectionIndex() -> int:
    """
    Calls Qt's 'qsizetype QQuickGraphsScatter::invalidSelectionIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#invalidSelectionIndex
    """
    #  qsizetype QQuickGraphsScatter::invalidSelectionIndex()
    return Rituals.call(
        'ritual_ZN19QQuickGraphsScatter21invalidSelectionIndexEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGraphsScatter'

  #  A C++ QQuickGraphsScatter Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickGraphsScatter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGraphsScatter::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGraphsScatter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickGraphsScatter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def axisX(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QQuickGraphsScatter::axisX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsscatter.html#axisX

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QQuickGraphsScatter::axisX() const
    address = self.uglySide.call('ritual_ZNK19QQuickGraphsScatter5axisXEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axisY(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QQuickGraphsScatter::axisY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsscatter.html#axisY

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QQuickGraphsScatter::axisY() const
    address = self.uglySide.call('ritual_ZNK19QQuickGraphsScatter5axisYEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axisZ(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QQuickGraphsScatter::axisZ() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsscatter.html#axisZ

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QQuickGraphsScatter::axisZ() const
    address = self.uglySide.call('ritual_ZNK19QQuickGraphsScatter5axisZEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def selectedSeries(self) -> Optional[QScatter3DSeries]:
    """
    Calls Qt's 'QScatter3DSeries *QQuickGraphsScatter::selectedSeries()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#selectedSeries

    Returns
    -------

    Optional[QScatter3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScatter3DSeries *QQuickGraphsScatter::selectedSeries() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickGraphsScatter14selectedSeriesEv',
    )
    from . import QScatter3DSeries
    return QScatter3DSeries._cuteAt(address)

  def hasSelectedItemChanged(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsScatter::hasSelectedItemChanged() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#hasSelectedItemChanged
    """
    #  bool QQuickGraphsScatter::hasSelectedItemChanged() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickGraphsScatter22hasSelectedItemChangedEv',
    )

  def hasItemChanged(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsScatter::hasItemChanged() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#hasItemChanged
    """
    #  bool QQuickGraphsScatter::hasItemChanged() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickGraphsScatter14hasItemChangedEv',
    )

  def hasChangedSeriesList(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsScatter::hasChangedSeriesList() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#hasChangedSeriesList
    """
    #  bool QQuickGraphsScatter::hasChangedSeriesList() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickGraphsScatter20hasChangedSeriesListEv',
    )

  def isSeriesVisualsDirty(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsScatter::isSeriesVisualsDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#isSeriesVisualsDirty
    """
    #  bool QQuickGraphsScatter::isSeriesVisualsDirty() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickGraphsScatter20isSeriesVisualsDirtyEv',
    )

  def isDataDirty(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsScatter::isDataDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#isDataDirty
    """
    #  bool QQuickGraphsScatter::isDataDirty() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickGraphsScatter11isDataDirtyEv',
    )

  def selected(self) -> Optional[QQuick3DModel]:
    """
    Calls Qt's 'QQuick3DModel *QQuickGraphsScatter::selected() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsscatter.html#selected

    Returns
    -------

    Optional[QQuick3DModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DModel *QQuickGraphsScatter::selected() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickGraphsScatter8selectedEv',
    )
    from ..QtQuick3D import QQuick3DModel
    return QQuick3DModel._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::setAxisX(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsscatter.html#setAxisX

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatter::setAxisX(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter8setAxisXEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::setAxisY(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsscatter.html#setAxisY

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatter::setAxisY(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter8setAxisYEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisZ(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::setAxisZ(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsscatter.html#setAxisZ

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatter::setAxisZ(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter8setAxisZEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(int, QScatter3DSeries)
  @overload(int, NoneType)
  def setSelectedItem(
      self,
      index: int,
      series: Optional[QScatter3DSeries],
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::setSelectedItem(qsizetype index,
    QScatter3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#setSelectedItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    series : Optional[QScatter3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatter::setSelectedItem(qsizetype index,
    #      QScatter3DSeries *series)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter15setSelectedItemExP16QScatter3DSeri'
        'es',
        index, self._addressOf(series),
    )

  @overload(QtGraphs3D.SelectionFlags)
  def setSelectionMode(self, mode: QtGraphs3D.SelectionFlags) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsScatter::setSelectionMode(QtGraphs3D::SelectionFlags mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#setSelectionMode

    Parameters
    ----------

    mode : QtGraphs3D.SelectionFlags
      Passed on as its number.
    """
    #  void QQuickGraphsScatter::setSelectionMode(QtGraphs3D::SelectionFlags
    #      mode)
    ritual = (
        'ritual_ZN19QQuickGraphsScatter16setSelectionModeE6QFlagsIN10QtGrap'
        'hs3D13SelectionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsScatter16setSelectionModeE6QFlagsIN10'
          'QtGraphs3D13SelectionFlagEE')
    self.uglySide.call(ritual, mode.value)

  @overload(bool)
  def setSelectedItemChanged(self, changed: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::setSelectedItemChanged(bool
    changed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#setSelectedItemChanged

    Parameters
    ----------

    changed : bool
      Passed on as it is.
    """
    #  void QQuickGraphsScatter::setSelectedItemChanged(bool changed)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter22setSelectedItemChangedEb', changed,
    )

  @overload(bool)
  def setItemChanged(self, changed: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::setItemChanged(bool changed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#setItemChanged

    Parameters
    ----------

    changed : bool
      Passed on as it is.
    """
    #  void QQuickGraphsScatter::setItemChanged(bool changed)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter14setItemChangedEb', changed,
    )

  def setSeriesVisualsDirty(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::setSeriesVisualsDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#setSeriesVisualsDirty
    """
    #  void QQuickGraphsScatter::setSeriesVisualsDirty()
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter21setSeriesVisualsDirtyEv',
    )

  @overload(QQuick3DModel)
  @overload(NoneType)
  def setSelected(self, newSelected: Optional[QQuick3DModel]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::setSelected(QQuick3DModel
    *newSelected)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#setSelected

    Parameters
    ----------

    newSelected : Optional[QQuick3DModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatter::setSelected(QQuick3DModel *newSelected)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter11setSelectedEP13QQuick3DModel',
        self._addressOf(newSelected),
    )

  @overload(QQuick3DModel, int)
  @overload(NoneType, int)
  def setSelected(self, root: Optional[QQuick3DModel], index: int) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::setSelected(QQuick3DModel *root,
    qsizetype index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#setSelected

    Parameters
    ----------

    root : Optional[QQuick3DModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  void QQuickGraphsScatter::setSelected(QQuick3DModel *root, qsizetype
    #      index)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter11setSelectedEP13QQuick3DModelx',
        self._addressOf(root), index,
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
    'QQuickGraphsScatter::QQuickGraphsScatter(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#QQuickGraphsScatter

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickGraphsScatter::QQuickGraphsScatter(QQuickItem *parent)
    self._noteCreation(QQuickGraphsScatter, lambda: Rituals.call(
        'ritual_ZN19QQuickGraphsScatterC1EP10QQuickItem',
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

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::clearSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#clearSelection
    """
    #  void QQuickGraphsScatter::clearSelection()
    ritual = 'ritual_ZN19QQuickGraphsScatter14clearSelectionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickGraphsScatter14clearSelectionEv'
    self.uglySide.call(ritual)

  @overload(QScatter3DSeries)
  @overload(NoneType)
  def addSeries(self, series: Optional[QScatter3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::addSeries(QScatter3DSeries
    *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsscatter.html#addSeries

    Parameters
    ----------

    series : Optional[QScatter3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatter::addSeries(QScatter3DSeries *series)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter9addSeriesEP16QScatter3DSeries',
        self._addressOf(series),
    )

  @overload(QScatter3DSeries)
  @overload(NoneType)
  def removeSeries(self, series: Optional[QScatter3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::removeSeries(QScatter3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#removeSeries

    Parameters
    ----------

    series : Optional[QScatter3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatter::removeSeries(QScatter3DSeries *series)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter12removeSeriesEP16QScatter3DSeries',
        self._addressOf(series),
    )

  def scatterSeriesList(self) -> QList[QScatter3DSeries]:
    """
    Calls Qt's 'QList<QScatter3DSeries *>
    QQuickGraphsScatter::scatterSeriesList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#scatterSeriesList

    Returns
    -------

    QList[QScatter3DSeries]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QScatter3DSeries *> QQuickGraphsScatter::scatterSeriesList()
    address = self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter17scatterSeriesListEv',
    )
    from . import QScatter3DSeries
    return QList[QScatter3DSeries]._cuteOwning(address)

  @overload(QAbstract3DAxis.AxisOrientation, bool)
  def handleAxisAutoAdjustRangeChangedInOrientation(
      self,
      orientation: QAbstract3DAxis.AxisOrientation,
      autoAdjust: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsScatter::handleAxisAutoAdjustRangeChangedInOrientation(
    QAbstract3DAxis::AxisOrientation orientation, bool autoAdjust)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html

    Parameters
    ----------

    orientation : QAbstract3DAxis.AxisOrientation
      Passed on as its number.

    autoAdjust : bool
      Passed on as it is.
    """
    #  void QQuickGraphsScatter::
    #      handleAxisAutoAdjustRangeChangedInOrientation(QAbstract3DAxis::
    #      AxisOrientation orientation, bool autoAdjust)
    ritual = (
        'ritual_ZN19QQuickGraphsScatter45handleAxisAutoAdjustRangeChangedIn'
        'OrientationEN15QAbstract3DAxis15AxisOrientationEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsScatter45handleAxisAutoAdjustRangeCha'
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
    QQuickGraphsScatter::handleAxisRangeChangedBySender(QObject *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatter::handleAxisRangeChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN19QQuickGraphsScatter30handleAxisRangeChangedBySenderEP7Q'
        'Object')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsScatter30handleAxisRangeChangedBySend'
          'erEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  def adjustAxisRanges(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::adjustAxisRanges()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#adjustAxisRanges
    """
    #  void QQuickGraphsScatter::adjustAxisRanges()
    ritual = 'ritual_ZN19QQuickGraphsScatter16adjustAxisRangesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickGraphsScatter16adjustAxisRangesEv'
    self.uglySide.call(ritual)

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def handleMultiAxisChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsScatter::handleMultiAxisChanged(QAbstract3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#handleMultiAxisChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatter::handleMultiAxisChanged(QAbstract3DAxis
    #      *axis)
    ritual = (
        'ritual_ZN19QQuickGraphsScatter22handleMultiAxisChangedEP15QAbstrac'
        't3DAxis')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsScatter22handleMultiAxisChangedEP15QA'
          'bstract3DAxis')
    self.uglySide.call(ritual, self._addressOf(axis))

  def handleLightingModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::handleLightingModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#handleLightingModeChanged
    """
    #  void QQuickGraphsScatter::handleLightingModeChanged()
    ritual = 'ritual_ZN19QQuickGraphsScatter25handleLightingModeChangedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsScatter25handleLightingModeChangedEv')
    self.uglySide.call(ritual)

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def handleAxisXChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::handleAxisXChanged(QAbstract3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#handleAxisXChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatter::handleAxisXChanged(QAbstract3DAxis *axis)
    ritual = (
        'ritual_ZN19QQuickGraphsScatter18handleAxisXChangedEP15QAbstract3DA'
        'xis')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsScatter18handleAxisXChangedEP15QAbstr'
          'act3DAxis')
    self.uglySide.call(ritual, self._addressOf(axis))

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def handleAxisYChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::handleAxisYChanged(QAbstract3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#handleAxisYChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatter::handleAxisYChanged(QAbstract3DAxis *axis)
    ritual = (
        'ritual_ZN19QQuickGraphsScatter18handleAxisYChangedEP15QAbstract3DA'
        'xis')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsScatter18handleAxisYChangedEP15QAbstr'
          'act3DAxis')
    self.uglySide.call(ritual, self._addressOf(axis))

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def handleAxisZChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::handleAxisZChanged(QAbstract3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#handleAxisZChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatter::handleAxisZChanged(QAbstract3DAxis *axis)
    ritual = (
        'ritual_ZN19QQuickGraphsScatter18handleAxisZChangedEP15QAbstract3DA'
        'xis')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsScatter18handleAxisZChangedEP15QAbstr'
          'act3DAxis')
    self.uglySide.call(ritual, self._addressOf(axis))

  def handleSeriesMeshChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::handleSeriesMeshChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#handleSeriesMeshChanged
    """
    #  void QQuickGraphsScatter::handleSeriesMeshChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter23handleSeriesMeshChangedEv',
    )

  @overload(bool)
  def handleMeshSmoothChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::handleMeshSmoothChanged(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#handleMeshSmoothChanged

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickGraphsScatter::handleMeshSmoothChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter23handleMeshSmoothChangedEb', enable,
    )

  def handleArrayReset(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::handleArrayReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#handleArrayReset
    """
    #  void QQuickGraphsScatter::handleArrayReset()
    self.uglySide.call('ritual_ZN19QQuickGraphsScatter16handleArrayResetEv')

  @overload(int, int)
  def handleItemsAdded(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::handleItemsAdded(qsizetype
    startIndex, qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#handleItemsAdded

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQuickGraphsScatter::handleItemsAdded(qsizetype startIndex,
    #      qsizetype count)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter16handleItemsAddedExx',
        startIndex, count,
    )

  @overload(int, int)
  def handleItemsChanged(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::handleItemsChanged(qsizetype
    startIndex, qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#handleItemsChanged

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQuickGraphsScatter::handleItemsChanged(qsizetype startIndex,
    #      qsizetype count)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter18handleItemsChangedExx',
        startIndex, count,
    )

  @overload(int, int)
  def handleItemsRemoved(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::handleItemsRemoved(qsizetype
    startIndex, qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#handleItemsRemoved

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQuickGraphsScatter::handleItemsRemoved(qsizetype startIndex,
    #      qsizetype count)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter18handleItemsRemovedExx',
        startIndex, count,
    )

  @overload(int, int)
  def handleItemsInserted(self, startIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::handleItemsInserted(qsizetype
    startIndex, qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#handleItemsInserted

    Parameters
    ----------

    startIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQuickGraphsScatter::handleItemsInserted(qsizetype startIndex,
    #      qsizetype count)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter19handleItemsInsertedExx',
        startIndex, count,
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisXChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::axisXChanged(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#axisXChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatter::axisXChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter12axisXChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisYChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::axisYChanged(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#axisYChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatter::axisYChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter12axisYChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisZChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::axisZChanged(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#axisZChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatter::axisZChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter12axisZChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QScatter3DSeries)
  @overload(NoneType)
  def selectedSeriesChanged(
      self,
      series: Optional[QScatter3DSeries],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsScatter::selectedSeriesChanged(QScatter3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#selectedSeriesChanged

    Parameters
    ----------

    series : Optional[QScatter3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatter::selectedSeriesChanged(QScatter3DSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter21selectedSeriesChangedEP16QScatter3'
        'DSeries',
        self._addressOf(series),
    )

  def calculateSceneScalingFactors(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::calculateSceneScalingFactors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html
    """
    #  void QQuickGraphsScatter::calculateSceneScalingFactors()
    ritual = 'ritual_ZN19QQuickGraphsScatter28calculateSceneScalingFactorsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsScatter28calculateSceneScalingFactors'
          'Ev')
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#componentComplete
    """
    #  void QQuickGraphsScatter::componentComplete()
    ritual = 'ritual_ZN19QQuickGraphsScatter17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickGraphsScatter17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QPointF)
  def doPicking(self, position: QPointF) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsScatter::doPicking(QPointF position)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsscatter.html#doPicking

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QQuickGraphsScatter::doPicking(QPointF position)
    ritual = 'ritual_ZN19QQuickGraphsScatter9doPickingE7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickGraphsScatter9doPickingE7QPointF'
    return self.uglySide.call(ritual, self._valueOf(position, 'QPointF'))

  @overload(QVector3D, QVector3D)
  def doRayPicking(self, origin: QVector3D, direction: QVector3D) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsScatter::doRayPicking(QVector3D origin,
    QVector3D direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#doRayPicking

    Parameters
    ----------

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  bool QQuickGraphsScatter::doRayPicking(QVector3D origin, QVector3D
    #      direction)
    ritual = 'ritual_ZN19QQuickGraphsScatter12doRayPickingE9QVector3DS0_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsScatter12doRayPickingE9QVector3DS0_')
    return self.uglySide.call(
        ritual, self._valueOf(origin), self._valueOf(direction),
    )

  @overload(QtGraphs3D.ShadowQuality)
  def updateShadowQuality(self, quality: QtGraphs3D.ShadowQuality) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsScatter::updateShadowQuality(QtGraphs3D::ShadowQuality
    quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#updateShadowQuality

    Parameters
    ----------

    quality : QtGraphs3D.ShadowQuality
      Passed on as its number.
    """
    #  void
    #      QQuickGraphsScatter::updateShadowQuality(QtGraphs3D::ShadowQuality
    #      quality)
    ritual = (
        'ritual_ZN19QQuickGraphsScatter19updateShadowQualityEN10QtGraphs3D1'
        '3ShadowQualityE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsScatter19updateShadowQualityEN10QtGra'
          'phs3D13ShadowQualityE')
    self.uglySide.call(ritual, quality.value)

  def updateLightStrength(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::updateLightStrength()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#updateLightStrength
    """
    #  void QQuickGraphsScatter::updateLightStrength()
    ritual = 'ritual_ZN19QQuickGraphsScatter19updateLightStrengthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickGraphsScatter19updateLightStrengthEv'
    self.uglySide.call(ritual)

  def startRecordingRemovesAndInserts(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::startRecordingRemovesAndInserts()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html
    """
    #  void QQuickGraphsScatter::startRecordingRemovesAndInserts()
    ritual = (
        'ritual_ZN19QQuickGraphsScatter31startRecordingRemovesAndInsertsEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsScatter31startRecordingRemovesAndInse'
          'rtsEv')
    self.uglySide.call(ritual)

  @overload(QAbstract3DSeries, QAbstract3DAxis.AxisOrientation)
  @overload(NoneType, QAbstract3DAxis.AxisOrientation)
  def getSeriesMultiAxis(
      self,
      series: Optional[QAbstract3DSeries],
      orientation: QAbstract3DAxis.AxisOrientation,
  ) -> Optional[QAbstract3DAxis]:
    """
    Calls Qt's 'QAbstract3DAxis
    *QQuickGraphsScatter::getSeriesMultiAxis(QAbstract3DSeries *series,
    QAbstract3DAxis::AxisOrientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#getSeriesMultiAxis

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
    #      *QQuickGraphsScatter::getSeriesMultiAxis(QAbstract3DSeries
    #      *series, QAbstract3DAxis::AxisOrientation orientation)
    ritual = (
        'ritual_ZN19QQuickGraphsScatter18getSeriesMultiAxisEP17QAbstract3DS'
        'eriesN15QAbstract3DAxis15AxisOrientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsScatter18getSeriesMultiAxisEP17QAbstr'
          'act3DSeriesN15QAbstract3DAxis15AxisOrientationE')
    address = self.uglySide.call(
        ritual, self._addressOf(series), orientation.value,
    )
    return QAbstract3DAxis._cuteAt(address)

  @overload(QScatter3DSeries)
  @overload(NoneType)
  def connectSeries(self, series: Optional[QScatter3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::connectSeries(QScatter3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#connectSeries

    Parameters
    ----------

    series : Optional[QScatter3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatter::connectSeries(QScatter3DSeries *series)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter13connectSeriesEP16QScatter3DSeries',
        self._addressOf(series),
    )

  @overload(QScatter3DSeries)
  @overload(NoneType)
  def disconnectSeries(self, series: Optional[QScatter3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::disconnectSeries(QScatter3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#disconnectSeries

    Parameters
    ----------

    series : Optional[QScatter3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatter::disconnectSeries(QScatter3DSeries *series)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter16disconnectSeriesEP16QScatter3DSeri'
        'es',
        self._addressOf(series),
    )

  @overload(QQuick3DModel)
  @overload(NoneType)
  def getItemIndex(self, item: Optional[QQuick3DModel]) -> int:
    """
    Calls Qt's 'qsizetype QQuickGraphsScatter::getItemIndex(QQuick3DModel
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#getItemIndex

    Parameters
    ----------

    item : Optional[QQuick3DModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qsizetype QQuickGraphsScatter::getItemIndex(QQuick3DModel *item)
    return self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter12getItemIndexEP13QQuick3DModel',
        self._addressOf(item),
    )

  def selectedItemPosition(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuickGraphsScatter::selectedItemPosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#selectedItemPosition

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuickGraphsScatter::selectedItemPosition()
    address = self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter20selectedItemPositionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QQuick3DModel, bool, bool, bool, str)
  @overload(NoneType, bool, bool, bool, str)
  def updateItemMaterial(
      self,
      item: Optional[QQuick3DModel],
      useGradient: bool,
      rangeGradient: bool,
      usePoint: bool,
      materialName: str,
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::updateItemMaterial(QQuick3DModel
    *item, bool useGradient, bool rangeGradient, bool usePoint, const QString
    &materialName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#updateItemMaterial

    Parameters
    ----------

    item : Optional[QQuick3DModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    useGradient : bool
      Passed on as it is.

    rangeGradient : bool
      Passed on as it is.

    usePoint : bool
      Passed on as it is.

    materialName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickGraphsScatter::updateItemMaterial(QQuick3DModel *item, bool
    #      useGradient, bool rangeGradient, bool usePoint, const QString
    #      &materialName)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter18updateItemMaterialEP13QQuick3DMode'
        'lbbbRK7QString',
        self._addressOf(item), useGradient, rangeGradient, usePoint,
        materialName,
    )

  @overload(QQuick3DModel, QQuick3DTexture)
  @overload(QQuick3DModel, NoneType)
  @overload(NoneType, QQuick3DTexture)
  @overload(NoneType, NoneType)
  @overload(QQuick3DModel, QQuick3DTexture, QColor)
  @overload(QQuick3DModel, NoneType, QColor)
  @overload(NoneType, QQuick3DTexture, QColor)
  @overload(NoneType, NoneType, QColor)
  @overload(QQuick3DModel, QQuick3DTexture, QColor, bool)
  @overload(QQuick3DModel, NoneType, QColor, bool)
  @overload(NoneType, QQuick3DTexture, QColor, bool)
  @overload(NoneType, NoneType, QColor, bool)
  @overload(QQuick3DModel, QQuick3DTexture, QColor, bool, bool)
  @overload(QQuick3DModel, NoneType, QColor, bool, bool)
  @overload(NoneType, QQuick3DTexture, QColor, bool, bool)
  @overload(NoneType, NoneType, QColor, bool, bool)
  def updateMaterialProperties(
      self,
      item: Optional[QQuick3DModel],
      texture: Optional[QQuick3DTexture],
      color: Optional[QColor] = None,
      transparency: bool = False,
      shaded: bool = True,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsScatter::updateMaterialProperties(QQuick3DModel *item,
    QQuick3DTexture *texture, QColor color, const bool transparency, const
    bool shaded)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#updateMaterialProperties

    Parameters
    ----------

    item : Optional[QQuick3DModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    texture : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    color : Optional[QColor]
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own. May be left out, as in Qt: a new 'QColor(Qt.GlobalColor.white)' is
      then passed on.

    transparency : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    shaded : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQuickGraphsScatter::updateMaterialProperties(QQuick3DModel
    #      *item, QQuick3DTexture *texture, QColor color, const bool
    #      transparency, const bool shaded)
    if color is None:
      from ..QtGui import QColor
      color = QColor(Qt.GlobalColor.white)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter24updateMaterialPropertiesEP13QQuick'
        '3DModelP15QQuick3DTexture6QColorbb',
        self._addressOf(item), self._addressOf(texture),
        self._valueOf(color), transparency, shaded,
    )

  def createTexture(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuickGraphsScatter::createTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#createTexture

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuickGraphsScatter::createTexture()
    address = self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter13createTextureEv',
    )
    from ..QtQuick3D import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def createSeriesRoot(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *QQuickGraphsScatter::createSeriesRoot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#createSeriesRoot

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QQuickGraphsScatter::createSeriesRoot()
    address = self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter16createSeriesRootEv',
    )
    from ..QtQuick3D import QQuick3DNode
    return QQuick3DNode._cuteAt(address)

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def createDataItem(
      self,
      series: Optional[QAbstract3DSeries],
  ) -> Optional[QQuick3DModel]:
    """
    Calls Qt's 'QQuick3DModel
    *QQuickGraphsScatter::createDataItem(QAbstract3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#createDataItem

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuick3DModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DModel *QQuickGraphsScatter::createDataItem(QAbstract3DSeries
    #      *series)
    address = self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter14createDataItemEP17QAbstract3DSerie'
        's',
        self._addressOf(series),
    )
    from ..QtQuick3D import QQuick3DModel
    return QQuick3DModel._cuteAt(address)

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def getMeshFileName(self, series: Optional[QAbstract3DSeries]) -> str:
    """
    Calls Qt's 'QString
    QQuickGraphsScatter::getMeshFileName(QAbstract3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#getMeshFileName

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickGraphsScatter::getMeshFileName(QAbstract3DSeries
    #      *series)
    return self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter15getMeshFileNameEP17QAbstract3DSeri'
        'es',
        self._addressOf(series),
    )

  @overload(QQuick3DModel)
  @overload(NoneType)
  def deleteDataItem(self, item: Optional[QQuick3DModel]) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::deleteDataItem(QQuick3DModel
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#deleteDataItem

    Parameters
    ----------

    item : Optional[QQuick3DModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatter::deleteDataItem(QQuick3DModel *item)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter14deleteDataItemEP13QQuick3DModel',
        self._addressOf(item),
    )

  def recreateDataItems(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::recreateDataItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#recreateDataItems
    """
    #  void QQuickGraphsScatter::recreateDataItems()
    self.uglySide.call('ritual_ZN19QQuickGraphsScatter17recreateDataItemsEv')

  @overload(int, int)
  def sizeDifference(self, size1: int, size2: int) -> int:
    """
    Calls Qt's 'qsizetype QQuickGraphsScatter::sizeDifference(qsizetype
    size1, qsizetype size2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#sizeDifference

    Parameters
    ----------

    size1 : int
      Passed on as it is.

    size2 : int
      Passed on as it is.
    """
    #  qsizetype QQuickGraphsScatter::sizeDifference(qsizetype size1,
    #      qsizetype size2)
    return self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter14sizeDifferenceExx', size1, size2,
    )

  @overload(QList[QAbstract3DSeries])
  def handleSeriesChanged(
      self,
      changedSeries: QList[QAbstract3DSeries],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsScatter::handleSeriesChanged(QList<QAbstract3DSeries *>
    changedSeries)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#handleSeriesChanged

    Parameters
    ----------

    changedSeries : QList[QAbstract3DSeries]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickGraphsScatter::handleSeriesChanged(QList<QAbstract3DSeries
    #      *> changedSeries)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter19handleSeriesChangedE5QListIP17QAbs'
        'tract3DSeriesE',
        self._valueOf(changedSeries),
    )

  @overload(QScatter3DSeries)
  @overload(NoneType)
  def selectedItemInSeries(self, series: Optional[QScatter3DSeries]) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsScatter::selectedItemInSeries(const
    QScatter3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#selectedItemInSeries

    Parameters
    ----------

    series : Optional[QScatter3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickGraphsScatter::selectedItemInSeries(const QScatter3DSeries
    #      *series)
    return self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter20selectedItemInSeriesEPK16QScatter3'
        'DSeries',
        self._addressOf(series),
    )

  @overload(QVector3D, QScatter3DSeries)
  @overload(QVector3D, NoneType)
  def isDotPositionInAxisRange(
      self,
      dotPos: QVector3D,
      series: Optional[QScatter3DSeries],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsScatter::isDotPositionInAxisRange(QVector3D
    dotPos, QScatter3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#isDotPositionInAxisRange

    Parameters
    ----------

    dotPos : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    series : Optional[QScatter3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickGraphsScatter::isDotPositionInAxisRange(QVector3D dotPos,
    #      QScatter3DSeries *series)
    return self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter24isDotPositionInAxisRangeE9QVector3'
        'DP16QScatter3DSeries',
        self._valueOf(dotPos), self._addressOf(series),
    )

  def calculatePointScaleSize(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsScatter::calculatePointScaleSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#calculatePointScaleSize
    """
    #  float QQuickGraphsScatter::calculatePointScaleSize()
    return self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter23calculatePointScaleSizeEv',
    )

  def updatePointScaleSize(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::updatePointScaleSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#updatePointScaleSize
    """
    #  void QQuickGraphsScatter::updatePointScaleSize()
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter20updatePointScaleSizeEv',
    )

  def handleSplineChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::handleSplineChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#handleSplineChanged
    """
    #  void QQuickGraphsScatter::handleSplineChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter19handleSplineChangedEv',
    )

  def clearSelectionModel(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::clearSelectionModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#clearSelectionModel
    """
    #  void QQuickGraphsScatter::clearSelectionModel()
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter19clearSelectionModelEv',
    )

  def clearAllSelectionInstanced(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::clearAllSelectionInstanced()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html
    """
    #  void QQuickGraphsScatter::clearAllSelectionInstanced()
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter26clearAllSelectionInstancedEv',
    )

  @overload(bool, QObject)
  @overload(bool, NoneType)
  def handleItemLabelVisibleChangedBySender(
      self,
      visible: bool,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsScatter::handleItemLabelVisibleChangedBySender(bool visible,
    QObject *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html

    Parameters
    ----------

    visible : bool
      Passed on as it is.

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsScatter::handleItemLabelVisibleChangedBySender(bool
    #      visible, QObject *sender)
    ritual = (
        'ritual_ZN19QQuickGraphsScatter37handleItemLabelVisibleChangedBySen'
        'derEbP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsScatter37handleItemLabelVisibleChange'
          'dBySenderEbP7QObject')
    self.uglySide.call(ritual, visible, self._addressOf(sender, 'QObject'))

  @overload(QtGraphs3D.OptimizationHint)
  def optimizationChanged(
      self,
      toOptimization: QtGraphs3D.OptimizationHint,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsScatter::optimizationChanged(QtGraphs3D::OptimizationHint
    toOptimization)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#optimizationChanged

    Parameters
    ----------

    toOptimization : QtGraphs3D.OptimizationHint
      Passed on as its number.
    """
    #  void QQuickGraphsScatter::optimizationChanged(QtGraphs3D::
    #      OptimizationHint toOptimization)
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter19optimizationChangedEN10QtGraphs3D1'
        '6OptimizationHintE',
        toOptimization.value,
    )

  def updateGraph(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::updateGraph()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#updateGraph
    """
    #  void QQuickGraphsScatter::updateGraph()
    ritual = 'ritual_ZN19QQuickGraphsScatter11updateGraphEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickGraphsScatter11updateGraphEv'
    self.uglySide.call(ritual)

  def synchData(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::synchData()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsscatter.html#synchData
    """
    #  void QQuickGraphsScatter::synchData()
    ritual = 'ritual_ZN19QQuickGraphsScatter9synchDataEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickGraphsScatter9synchDataEv'
    self.uglySide.call(ritual)

  @overload(QtGraphs3D.OptimizationHint)
  def handleOptimizationHintChange(
      self,
      hint: QtGraphs3D.OptimizationHint,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsScatter::handleOptimizationHintChange(QtGraphs3D::
    OptimizationHint hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html

    Parameters
    ----------

    hint : QtGraphs3D.OptimizationHint
      Passed on as its number.
    """
    #  void QQuickGraphsScatter::handleOptimizationHintChange(QtGraphs3D::
    #      OptimizationHint hint)
    ritual = (
        'ritual_ZN19QQuickGraphsScatter28handleOptimizationHintChangeEN10Qt'
        'Graphs3D16OptimizationHintE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsScatter28handleOptimizationHintChange'
          'EN10QtGraphs3D16OptimizationHintE')
    self.uglySide.call(ritual, hint.value)

  @overload(QObject)
  @overload(NoneType)
  def handleSeriesVisibilityChangedBySender(
      self,
      sender: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsScatter::handleSeriesVisibilityChangedBySender(QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QQuickGraphsScatter::handleSeriesVisibilityChangedBySender(QObject
    #      *sender)
    ritual = (
        'ritual_ZN19QQuickGraphsScatter37handleSeriesVisibilityChangedBySen'
        'derEP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickGraphsScatter37handleSeriesVisibilityChange'
          'dBySenderEP7QObject')
    self.uglySide.call(ritual, self._addressOf(sender, 'QObject'))

  def cameraRotationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsScatter::cameraRotationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsscatter.html#cameraRotationChanged
    """
    #  void QQuickGraphsScatter::cameraRotationChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickGraphsScatter21cameraRotationChangedEv',
    )

  @staticmethod
  def addPointsToScatterModel(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsScatter::addPointsToScatterModel(ScatterModel
    *graphModel, qsizetype count)': names
    'QQuickGraphsScatter::ScatterModel', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsScatter.addPointsToScatterModel' has no cute function "
        "yet. Qt's 'void "
        "QQuickGraphsScatter::addPointsToScatterModel(ScatterModel "
        "*graphModel, qsizetype count)': names "
        "'QQuickGraphsScatter::ScatterModel', which has no cute class yet.")

  @staticmethod
  def appendSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickGraphsScatter::appendSeriesFunc(QQmlListProperty<QScatter3DSeries>
    *list, QScatter3DSeries *series)': names
    'QQmlListProperty<QScatter3DSeries>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsScatter.appendSeriesFunc' has no cute function yet. "
        "Qt's 'void "
        "QQuickGraphsScatter::appendSeriesFunc(QQmlListProperty<QScatter3DSe"
        "ries> *list, QScatter3DSeries *series)': names "
        "'QQmlListProperty<QScatter3DSeries>', which has no cute class yet.")

  @staticmethod
  def atSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'QScatter3DSeries
    *QQuickGraphsScatter::atSeriesFunc(QQmlListProperty<QScatter3DSeries>
    *list, qsizetype index)': names 'QQmlListProperty<QScatter3DSeries>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsScatter.atSeriesFunc' has no cute function yet. Qt's "
        "'QScatter3DSeries "
        "*QQuickGraphsScatter::atSeriesFunc(QQmlListProperty<QScatter3DSerie"
        "s> *list, qsizetype index)': names "
        "'QQmlListProperty<QScatter3DSeries>', which has no cute class yet.")

  @staticmethod
  def calculatePolarXZ(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsScatter::calculatePolarXZ(const float posX, const
    float posZ, float &x, float &z) const': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QQuickGraphsScatter.calculatePolarXZ' has no cute function yet. "
        "Qt's 'void QQuickGraphsScatter::calculatePolarXZ(const float posX, "
        "const float posZ, float &x, float &z) const': takes a number to "
        "change where it is.")

  @staticmethod
  def clearSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickGraphsScatter::clearSeriesFunc(QQmlListProperty<QScatter3DSeries>
    *list)': names 'QQmlListProperty<QScatter3DSeries>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsScatter.clearSeriesFunc' has no cute function yet. "
        "Qt's 'void "
        "QQuickGraphsScatter::clearSeriesFunc(QQmlListProperty<QScatter3DSer"
        "ies> *list)': names 'QQmlListProperty<QScatter3DSeries>', which "
        "has no cute class yet.")

  @staticmethod
  def countSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQuickGraphsScatter::countSeriesFunc(QQmlListProperty<QScatter3DSeries>
    *list)': names 'QQmlListProperty<QScatter3DSeries>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsScatter.countSeriesFunc' has no cute function yet. "
        "Qt's 'qsizetype "
        "QQuickGraphsScatter::countSeriesFunc(QQmlListProperty<QScatter3DSer"
        "ies> *list)': names 'QQmlListProperty<QScatter3DSeries>', which "
        "has no cute class yet.")

  @staticmethod
  def createSplineModel(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsScatter::createSplineModel(ScatterModel *model)':
    names 'QQuickGraphsScatter::ScatterModel', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsScatter.createSplineModel' has no cute function yet. "
        "Qt's 'void QQuickGraphsScatter::createSplineModel(ScatterModel "
        "*model)': names 'QQuickGraphsScatter::ScatterModel', which has no "
        "cute class yet.")

  @staticmethod
  def findGraphModel(*__, **_) -> Never:
    """
    Qt's 'ScatterModel *QQuickGraphsScatter::findGraphModel(QScatter3DSeries
    *series)': gives 'QQuickGraphsScatter::ScatterModel', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsScatter.findGraphModel' has no cute function yet. "
        "Qt's 'ScatterModel "
        "*QQuickGraphsScatter::findGraphModel(QScatter3DSeries *series)': "
        "gives 'QQuickGraphsScatter::ScatterModel', which has no cute class "
        "yet.")

  @staticmethod
  def fixMeshFileName(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsScatter::fixMeshFileName(QString &fileName,
    QAbstract3DSeries *series)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsScatter.fixMeshFileName' has no cute function yet. "
        "Qt's 'void QQuickGraphsScatter::fixMeshFileName(QString &fileName, "
        "QAbstract3DSeries *series)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def generatePointsForScatterModel(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickGraphsScatter::generatePointsForScatterModel(ScatterModel
    *series)': names 'QQuickGraphsScatter::ScatterModel', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsScatter.generatePointsForScatterModel' has no cute "
        "function yet. Qt's 'void "
        "QQuickGraphsScatter::generatePointsForScatterModel(ScatterModel "
        "*series)': names 'QQuickGraphsScatter::ScatterModel', which has no "
        "cute class yet.")

  @staticmethod
  def removeDataItems(*__, **_) -> Never:
    """
    - Qt's 'void QQuickGraphsScatter::removeDataItems(ScatterModel
      *graphModel, QtGraphs3D::OptimizationHint optimizationHint)': names
      'QQuickGraphsScatter::ScatterModel', which has no cute class yet.
    - Qt's 'void QQuickGraphsScatter::removeDataItems(QList<QQuick3DModel *>
      &items, qsizetype count)': takes a type Python has no way to hand over
      yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsScatter.removeDataItems' has no cute function yet. "
        "Qt's 'void QQuickGraphsScatter::removeDataItems(ScatterModel "
        "*graphModel, QtGraphs3D::OptimizationHint optimizationHint)': "
        "names 'QQuickGraphsScatter::ScatterModel', which has no cute class "
        "yet. Qt's 'void "
        "QQuickGraphsScatter::removeDataItems(QList<QQuick3DModel *> "
        "&items, qsizetype count)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def selectedItemInRange(*__, **_) -> Never:
    """
    Qt's 'bool QQuickGraphsScatter::selectedItemInRange(const ScatterModel
    *graphModel)': names 'QQuickGraphsScatter::ScatterModel', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsScatter.selectedItemInRange' has no cute function "
        "yet. Qt's 'bool QQuickGraphsScatter::selectedItemInRange(const "
        "ScatterModel *graphModel)': names "
        "'QQuickGraphsScatter::ScatterModel', which has no cute class yet.")

  @staticmethod
  def updateInstancedMaterialProperties(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickGraphsScatter::updateInstancedMaterialProperties(ScatterModel
    *graphModel, const bool isHighlight, QQuick3DTexture *seriesTexture,
    QQuick3DTexture *highlightTexture, const bool transparency)': names
    'QQuickGraphsScatter::ScatterModel', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsScatter.updateInstancedMaterialProperties' has no "
        "cute function yet. Qt's 'void "
        "QQuickGraphsScatter::updateInstancedMaterialProperties(ScatterModel"
        " *graphModel, const bool isHighlight, QQuick3DTexture "
        "*seriesTexture, QQuick3DTexture *highlightTexture, const bool "
        "transparency)': names 'QQuickGraphsScatter::ScatterModel', which "
        "has no cute class yet.")

  @staticmethod
  def updateMaterialReference(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsScatter::updateMaterialReference(ScatterModel
    *model)': names 'QQuickGraphsScatter::ScatterModel', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsScatter.updateMaterialReference' has no cute function "
        "yet. Qt's 'void "
        "QQuickGraphsScatter::updateMaterialReference(ScatterModel "
        "*model)': names 'QQuickGraphsScatter::ScatterModel', which has no "
        "cute class yet.")

  @staticmethod
  def updateScatterGraphItemPositions(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickGraphsScatter::updateScatterGraphItemPositions(ScatterModel
    *graphModel)': names 'QQuickGraphsScatter::ScatterModel', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsScatter.updateScatterGraphItemPositions' has no cute "
        "function yet. Qt's 'void "
        "QQuickGraphsScatter::updateScatterGraphItemPositions(ScatterModel "
        "*graphModel)': names 'QQuickGraphsScatter::ScatterModel', which "
        "has no cute class yet.")

  @staticmethod
  def updateScatterGraphItemVisuals(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickGraphsScatter::updateScatterGraphItemVisuals(ScatterModel
    *graphModel)': names 'QQuickGraphsScatter::ScatterModel', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsScatter.updateScatterGraphItemVisuals' has no cute "
        "function yet. Qt's 'void "
        "QQuickGraphsScatter::updateScatterGraphItemVisuals(ScatterModel "
        "*graphModel)': names 'QQuickGraphsScatter::ScatterModel', which "
        "has no cute class yet.")

  @staticmethod
  def updateSpline(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsScatter::updateSpline(ScatterModel *model)': names
    'QQuickGraphsScatter::ScatterModel', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsScatter.updateSpline' has no cute function yet. Qt's "
        "'void QQuickGraphsScatter::updateSpline(ScatterModel *model)': "
        "names 'QQuickGraphsScatter::ScatterModel', which has no cute class "
        "yet.")
