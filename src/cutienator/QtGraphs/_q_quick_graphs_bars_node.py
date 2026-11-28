"""
QQuickGraphsBarsNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qquickgraphsbarsnode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickGraphsBarsNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QQuickGraphsNode
from ..QtQuick3D import QQuick3DNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF, QSizeF
  from ..QtGui import QVector3D
  from . import QBar3DSeries, QCategory3DAxis, QQuickGraphsBars, QValue3DAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBar3DSeries = WAIT['QtGraphs:QBar3DSeries']
  QCategory3DAxis = WAIT['QtGraphs:QCategory3DAxis']
  QPointF = WAIT['QPointF']
  QSizeF = WAIT['QSizeF']
  QValue3DAxis = WAIT['QtGraphs:QValue3DAxis']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGraphsBarsNode(QQuickGraphsNode):
  """
  The cute side of Qt's QQuickGraphsBarsNode: a plain Python object standing
  in front of one C++ QQuickGraphsBarsNode.

  It is built on the cute 'QQuickGraphsNode', as Qt's QQuickGraphsBarsNode is
  built on Qt's QQuickGraphsNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickGraphsBarsNode that has a ritual and that
  Python can call so far, 43 names in all: 'metaObject', 'tr', 'setRowAxis',
  'rowAxis', 'setValueAxis', 'valueAxis', 'setColumnAxis', 'columnAxis',
  'setMultiSeriesUniform', 'isMultiSeriesUniform', 'setBarThickness',
  'barThickness', 'setBarSpacing', 'barSpacing', 'setBarSpacingRelative',
  'isBarSpacingRelative', 'setBarSeriesMargin', 'barSeriesMargin',
  'selectedSeries', 'setPrimarySeries', 'primarySeries', 'setFloorLevel',
  'floorLevel', 'barSeriesList', 'addSeries', 'removeSeries', 'insertSeries',
  'clearSelection', 'doPicking', 'doRayPicking', 'componentComplete',
  'rowAxisChanged', 'valueAxisChanged', 'columnAxisChanged',
  'multiSeriesUniformChanged', 'barThicknessChanged', 'barSpacingChanged',
  'barSpacingRelativeChanged', 'barSeriesMarginChanged',
  'primarySeriesChanged', 'selectedSeriesChanged', 'floorLevelChanged',
  'graphBars'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGraphsBarsNode::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickGraphsBarsNode::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickGraphsBarsNode::~QQuickGraphsBarsNode()': the destructor:
    Python never removes a C++ QQuickGraphsBarsNode.
  - Qt's 'QQmlListProperty<QBar3DSeries> QQuickGraphsBarsNode::seriesList()':
    gives a type Python has no way to take yet.
  - Qt's 'void
    QQuickGraphsBarsNode::appendSeriesFunc(QQmlListProperty<QBar3DSeries>
    *list, QBar3DSeries *series)': names 'QQmlListProperty<QBar3DSeries>',
    which has no cute class yet.
  - Qt's 'qsizetype
    QQuickGraphsBarsNode::countSeriesFunc(QQmlListProperty<QBar3DSeries>
    *list)': names 'QQmlListProperty<QBar3DSeries>', which has no cute class
    yet.
  - Qt's 'QBar3DSeries
    *QQuickGraphsBarsNode::atSeriesFunc(QQmlListProperty<QBar3DSeries> *list,
    qsizetype index)': names 'QQmlListProperty<QBar3DSeries>', which has no
    cute class yet.
  - Qt's 'void
    QQuickGraphsBarsNode::clearSeriesFunc(QQmlListProperty<QBar3DSeries>
    *list)': names 'QQmlListProperty<QBar3DSeries>', which has no cute class
    yet.
  - Qt's 'const QQuickGraphsBars *QQuickGraphsBarsNode::graphBars() const':
    takes in Python what 'QQuickGraphsBars
    *QQuickGraphsBarsNode::graphBars()' takes.

  What has no ritual
  ------------------

  2 of the 55 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickGraphsBarsNode is created at the first use, not by
    'QQuickGraphsBarsNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGraphsBarsNode.
  - Qt tells when it has removed the C++ QQuickGraphsBarsNode. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickGraphsBarsNode that has no cute function yet,
    'appendSeriesFunc', 'atSeriesFunc', 'clearSeriesFunc', 'countSeriesFunc',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
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
    Calls Qt's 'QString QQuickGraphsBarsNode::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#tr

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
    #  QString QQuickGraphsBarsNode::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickGraphsBarsNode2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGraphsBarsNode'

  #  A C++ QQuickGraphsBarsNode Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickGraphsBarsNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGraphsBarsNode::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGraphsBarsNode::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickGraphsBarsNode10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rowAxis(self) -> Optional[QCategory3DAxis]:
    """
    Calls Qt's 'QCategory3DAxis *QQuickGraphsBarsNode::rowAxis() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#rowAxis

    Returns
    -------

    Optional[QCategory3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCategory3DAxis *QQuickGraphsBarsNode::rowAxis() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickGraphsBarsNode7rowAxisEv',
    )
    from . import QCategory3DAxis
    return QCategory3DAxis._cuteAt(address)

  def valueAxis(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QQuickGraphsBarsNode::valueAxis() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#valueAxis

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QQuickGraphsBarsNode::valueAxis() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickGraphsBarsNode9valueAxisEv',
    )
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def columnAxis(self) -> Optional[QCategory3DAxis]:
    """
    Calls Qt's 'QCategory3DAxis *QQuickGraphsBarsNode::columnAxis() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#columnAxis

    Returns
    -------

    Optional[QCategory3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCategory3DAxis *QQuickGraphsBarsNode::columnAxis() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickGraphsBarsNode10columnAxisEv',
    )
    from . import QCategory3DAxis
    return QCategory3DAxis._cuteAt(address)

  def isMultiSeriesUniform(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsBarsNode::isMultiSeriesUniform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#isMultiSeriesUniform
    """
    #  bool QQuickGraphsBarsNode::isMultiSeriesUniform() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickGraphsBarsNode20isMultiSeriesUniformEv',
    )

  def barThickness(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsBarsNode::barThickness() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#barThickness
    """
    #  float QQuickGraphsBarsNode::barThickness() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickGraphsBarsNode12barThicknessEv',
    )

  def barSpacing(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QQuickGraphsBarsNode::barSpacing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#barSpacing

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QQuickGraphsBarsNode::barSpacing() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickGraphsBarsNode10barSpacingEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def isBarSpacingRelative(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsBarsNode::isBarSpacingRelative() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#isBarSpacingRelative
    """
    #  bool QQuickGraphsBarsNode::isBarSpacingRelative() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickGraphsBarsNode20isBarSpacingRelativeEv',
    )

  def barSeriesMargin(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QQuickGraphsBarsNode::barSeriesMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#barSeriesMargin

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QQuickGraphsBarsNode::barSeriesMargin() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickGraphsBarsNode15barSeriesMarginEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def selectedSeries(self) -> Optional[QBar3DSeries]:
    """
    Calls Qt's 'QBar3DSeries *QQuickGraphsBarsNode::selectedSeries() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#selectedSeries

    Returns
    -------

    Optional[QBar3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBar3DSeries *QQuickGraphsBarsNode::selectedSeries() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickGraphsBarsNode14selectedSeriesEv',
    )
    from . import QBar3DSeries
    return QBar3DSeries._cuteAt(address)

  def primarySeries(self) -> Optional[QBar3DSeries]:
    """
    Calls Qt's 'QBar3DSeries *QQuickGraphsBarsNode::primarySeries() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#primarySeries

    Returns
    -------

    Optional[QBar3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBar3DSeries *QQuickGraphsBarsNode::primarySeries() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickGraphsBarsNode13primarySeriesEv',
    )
    from . import QBar3DSeries
    return QBar3DSeries._cuteAt(address)

  def floorLevel(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsBarsNode::floorLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#floorLevel
    """
    #  float QQuickGraphsBarsNode::floorLevel() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickGraphsBarsNode10floorLevelEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QCategory3DAxis)
  @overload(NoneType)
  def setRowAxis(self, axis: Optional[QCategory3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::setRowAxis(QCategory3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#setRowAxis

    Parameters
    ----------

    axis : Optional[QCategory3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBarsNode::setRowAxis(QCategory3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode10setRowAxisEP15QCategory3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setValueAxis(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::setValueAxis(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#setValueAxis

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBarsNode::setValueAxis(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode12setValueAxisEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QCategory3DAxis)
  @overload(NoneType)
  def setColumnAxis(self, axis: Optional[QCategory3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::setColumnAxis(QCategory3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#setColumnAxis

    Parameters
    ----------

    axis : Optional[QCategory3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBarsNode::setColumnAxis(QCategory3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode13setColumnAxisEP15QCategory3DAxis',
        self._addressOf(axis),
    )

  @overload(bool)
  def setMultiSeriesUniform(self, uniform: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::setMultiSeriesUniform(bool
    uniform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#setMultiSeriesUniform

    Parameters
    ----------

    uniform : bool
      Passed on as it is.
    """
    #  void QQuickGraphsBarsNode::setMultiSeriesUniform(bool uniform)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode21setMultiSeriesUniformEb', uniform,
    )

  @overload(float)
  def setBarThickness(self, thickness: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::setBarThickness(float thickness)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#setBarThickness

    Parameters
    ----------

    thickness : float
      Passed on as it is.
    """
    #  void QQuickGraphsBarsNode::setBarThickness(float thickness)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode15setBarThicknessEf', thickness,
    )

  @overload(QSizeF)
  def setBarSpacing(self, spacing: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::setBarSpacing(QSizeF spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#setBarSpacing

    Parameters
    ----------

    spacing : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickGraphsBarsNode::setBarSpacing(QSizeF spacing)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode13setBarSpacingE6QSizeF',
        self._valueOf(spacing),
    )

  @overload(bool)
  def setBarSpacingRelative(self, relative: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::setBarSpacingRelative(bool
    relative)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#setBarSpacingRelative

    Parameters
    ----------

    relative : bool
      Passed on as it is.
    """
    #  void QQuickGraphsBarsNode::setBarSpacingRelative(bool relative)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode21setBarSpacingRelativeEb', relative,
    )

  @overload(QSizeF)
  def setBarSeriesMargin(self, margin: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::setBarSeriesMargin(QSizeF
    margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#setBarSeriesMargin

    Parameters
    ----------

    margin : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickGraphsBarsNode::setBarSeriesMargin(QSizeF margin)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode18setBarSeriesMarginE6QSizeF',
        self._valueOf(margin),
    )

  @overload(QBar3DSeries)
  @overload(NoneType)
  def setPrimarySeries(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::setPrimarySeries(QBar3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#setPrimarySeries

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBarsNode::setPrimarySeries(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode16setPrimarySeriesEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(float)
  def setFloorLevel(self, floorLevel: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::setFloorLevel(float floorLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#setFloorLevel

    Parameters
    ----------

    floorLevel : float
      Passed on as it is.
    """
    #  void QQuickGraphsBarsNode::setFloorLevel(float floorLevel)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode13setFloorLevelEf', floorLevel,
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
  @overload(QQuick3DNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickGraphsBarsNode::QQuickGraphsBarsNode(QQuick3DNode *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#QQuickGraphsBarsNode

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickGraphsBarsNode::QQuickGraphsBarsNode(QQuick3DNode *parent)
    self._noteCreation(QQuickGraphsBarsNode, lambda: Rituals.call(
        'ritual_ZN20QQuickGraphsBarsNodeC1EP12QQuick3DNode',
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

  def barSeriesList(self) -> QList[QBar3DSeries]:
    """
    Calls Qt's 'QList<QBar3DSeries *> QQuickGraphsBarsNode::barSeriesList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#barSeriesList

    Returns
    -------

    QList[QBar3DSeries]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QBar3DSeries *> QQuickGraphsBarsNode::barSeriesList()
    address = self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode13barSeriesListEv',
    )
    from . import QBar3DSeries
    return QList[QBar3DSeries]._cuteOwning(address)

  @overload(QBar3DSeries)
  @overload(NoneType)
  def addSeries(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::addSeries(QBar3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#addSeries

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBarsNode::addSeries(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode9addSeriesEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(QBar3DSeries)
  @overload(NoneType)
  def removeSeries(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::removeSeries(QBar3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#removeSeries

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBarsNode::removeSeries(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode12removeSeriesEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(int, QBar3DSeries)
  @overload(int, NoneType)
  def insertSeries(self, index: int, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::insertSeries(qsizetype index,
    QBar3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#insertSeries

    Parameters
    ----------

    index : int
      Passed on as it is.

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBarsNode::insertSeries(qsizetype index, QBar3DSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode12insertSeriesExP12QBar3DSeries',
        index, self._addressOf(series),
    )

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::clearSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#clearSelection
    """
    #  void QQuickGraphsBarsNode::clearSelection()
    ritual = 'ritual_ZN20QQuickGraphsBarsNode14clearSelectionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickGraphsBarsNode14clearSelectionEv'
    self.uglySide.call(ritual)

  @overload(QPointF)
  def doPicking(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsBarsNode::doPicking(QPointF point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#doPicking

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QQuickGraphsBarsNode::doPicking(QPointF point)
    ritual = 'ritual_ZN20QQuickGraphsBarsNode9doPickingE7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickGraphsBarsNode9doPickingE7QPointF'
    return self.uglySide.call(ritual, self._valueOf(point, 'QPointF'))

  @overload(QVector3D, QVector3D)
  def doRayPicking(self, origin: QVector3D, direction: QVector3D) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsBarsNode::doRayPicking(const QVector3D
    &origin, const QVector3D &direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#doRayPicking

    Parameters
    ----------

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  bool QQuickGraphsBarsNode::doRayPicking(const QVector3D &origin, const
    #      QVector3D &direction)
    ritual = 'ritual_ZN20QQuickGraphsBarsNode12doRayPickingERK9QVector3DS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickGraphsBarsNode12doRayPickingERK9QVector3DS2'
          '_')
    return self.uglySide.call(
        ritual, self._valueOf(origin), self._valueOf(direction),
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#componentComplete
    """
    #  void QQuickGraphsBarsNode::componentComplete()
    ritual = 'ritual_ZN20QQuickGraphsBarsNode17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickGraphsBarsNode17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QCategory3DAxis)
  @overload(NoneType)
  def rowAxisChanged(self, axis: Optional[QCategory3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::rowAxisChanged(QCategory3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#rowAxisChanged

    Parameters
    ----------

    axis : Optional[QCategory3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBarsNode::rowAxisChanged(QCategory3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode14rowAxisChangedEP15QCategory3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def valueAxisChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::valueAxisChanged(QValue3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#valueAxisChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBarsNode::valueAxisChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode16valueAxisChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QCategory3DAxis)
  @overload(NoneType)
  def columnAxisChanged(self, axis: Optional[QCategory3DAxis]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::columnAxisChanged(QCategory3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#columnAxisChanged

    Parameters
    ----------

    axis : Optional[QCategory3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBarsNode::columnAxisChanged(QCategory3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode17columnAxisChangedEP15QCategory3DA'
        'xis',
        self._addressOf(axis),
    )

  @overload(bool)
  def multiSeriesUniformChanged(self, uniform: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::multiSeriesUniformChanged(bool
    uniform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html

    Parameters
    ----------

    uniform : bool
      Passed on as it is.
    """
    #  void QQuickGraphsBarsNode::multiSeriesUniformChanged(bool uniform)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode25multiSeriesUniformChangedEb',
        uniform,
    )

  @overload(float)
  def barThicknessChanged(self, thicknessRatio: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::barThicknessChanged(float
    thicknessRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#barThicknessChanged

    Parameters
    ----------

    thicknessRatio : float
      Passed on as it is.
    """
    #  void QQuickGraphsBarsNode::barThicknessChanged(float thicknessRatio)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode19barThicknessChangedEf',
        thicknessRatio,
    )

  @overload(QSizeF)
  def barSpacingChanged(self, spacing: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::barSpacingChanged(QSizeF
    spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#barSpacingChanged

    Parameters
    ----------

    spacing : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickGraphsBarsNode::barSpacingChanged(QSizeF spacing)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode17barSpacingChangedE6QSizeF',
        self._valueOf(spacing),
    )

  @overload(bool)
  def barSpacingRelativeChanged(self, relative: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::barSpacingRelativeChanged(bool
    relative)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html

    Parameters
    ----------

    relative : bool
      Passed on as it is.
    """
    #  void QQuickGraphsBarsNode::barSpacingRelativeChanged(bool relative)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode25barSpacingRelativeChangedEb',
        relative,
    )

  @overload(QSizeF)
  def barSeriesMarginChanged(self, margin: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::barSeriesMarginChanged(QSizeF
    margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#barSeriesMarginChanged

    Parameters
    ----------

    margin : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickGraphsBarsNode::barSeriesMarginChanged(QSizeF margin)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode22barSeriesMarginChangedE6QSizeF',
        self._valueOf(margin),
    )

  @overload(QBar3DSeries)
  @overload(NoneType)
  def primarySeriesChanged(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::primarySeriesChanged(QBar3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#primarySeriesChanged

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBarsNode::primarySeriesChanged(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode20primarySeriesChangedEP12QBar3DSer'
        'ies',
        self._addressOf(series),
    )

  @overload(QBar3DSeries)
  @overload(NoneType)
  def selectedSeriesChanged(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::selectedSeriesChanged(QBar3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#selectedSeriesChanged

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsBarsNode::selectedSeriesChanged(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode21selectedSeriesChangedEP12QBar3DSe'
        'ries',
        self._addressOf(series),
    )

  @overload(float)
  def floorLevelChanged(self, level: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsBarsNode::floorLevelChanged(float level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#floorLevelChanged

    Parameters
    ----------

    level : float
      Passed on as it is.
    """
    #  void QQuickGraphsBarsNode::floorLevelChanged(float level)
    self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode17floorLevelChangedEf', level,
    )

  def graphBars(self) -> Optional[QQuickGraphsBars]:
    """
    Calls Qt's 'QQuickGraphsBars *QQuickGraphsBarsNode::graphBars()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsbarsnode.html#graphBars

    Returns
    -------

    Optional[QQuickGraphsBars]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickGraphsBars *QQuickGraphsBarsNode::graphBars()
    address = self.uglySide.call(
        'ritual_ZN20QQuickGraphsBarsNode9graphBarsEv',
    )
    from . import QQuickGraphsBars
    return QQuickGraphsBars._cuteAt(address)

  @staticmethod
  def appendSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickGraphsBarsNode::appendSeriesFunc(QQmlListProperty<QBar3DSeries>
    *list, QBar3DSeries *series)': names 'QQmlListProperty<QBar3DSeries>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsBarsNode.appendSeriesFunc' has no cute function yet. "
        "Qt's 'void "
        "QQuickGraphsBarsNode::appendSeriesFunc(QQmlListProperty<QBar3DSerie"
        "s> *list, QBar3DSeries *series)': names "
        "'QQmlListProperty<QBar3DSeries>', which has no cute class yet.")

  @staticmethod
  def atSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'QBar3DSeries
    *QQuickGraphsBarsNode::atSeriesFunc(QQmlListProperty<QBar3DSeries> *list,
    qsizetype index)': names 'QQmlListProperty<QBar3DSeries>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsBarsNode.atSeriesFunc' has no cute function yet. Qt's "
        "'QBar3DSeries "
        "*QQuickGraphsBarsNode::atSeriesFunc(QQmlListProperty<QBar3DSeries> "
        "*list, qsizetype index)': names 'QQmlListProperty<QBar3DSeries>', "
        "which has no cute class yet.")

  @staticmethod
  def clearSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickGraphsBarsNode::clearSeriesFunc(QQmlListProperty<QBar3DSeries>
    *list)': names 'QQmlListProperty<QBar3DSeries>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsBarsNode.clearSeriesFunc' has no cute function yet. "
        "Qt's 'void "
        "QQuickGraphsBarsNode::clearSeriesFunc(QQmlListProperty<QBar3DSeries"
        "> *list)': names 'QQmlListProperty<QBar3DSeries>', which has no "
        "cute class yet.")

  @staticmethod
  def countSeriesFunc(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQuickGraphsBarsNode::countSeriesFunc(QQmlListProperty<QBar3DSeries>
    *list)': names 'QQmlListProperty<QBar3DSeries>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsBarsNode.countSeriesFunc' has no cute function yet. "
        "Qt's 'qsizetype "
        "QQuickGraphsBarsNode::countSeriesFunc(QQmlListProperty<QBar3DSeries"
        "> *list)': names 'QQmlListProperty<QBar3DSeries>', which has no "
        "cute class yet.")
