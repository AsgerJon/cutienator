"""
QQuickGraphsNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qquickgraphsnode_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickGraphsNode to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QtGraphs3D

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QLocale, QMetaObject, QPointF
  from ..QtGui import QVector3D
  from . import QAbstract3DAxis, QAbstract3DSeries, QCustom3DItem
  from . import QGraphsTheme
  from ..QtQuick3D import QQuick3DNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstract3DSeries = WAIT['QtGraphs:QAbstract3DSeries']
  QCustom3DItem = WAIT['QtGraphs:QCustom3DItem']
  QGraphsTheme = WAIT['QGraphsTheme']
  QLocale = WAIT['QLocale']
  QPointF = WAIT['QPointF']
  QQuick3DNode = WAIT['QQuick3DNode']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGraphsNode(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickGraphsNode: a plain Python object standing in
  front of one C++ QQuickGraphsNode.

  What exists
  -----------

  Every function of Qt's QQuickGraphsNode that has a ritual and that Python
  can call so far, 57 names in all: 'metaObject', 'tr', 'componentComplete',
  'selectedElement', 'setSelectionMode', 'selectionMode', 'setTheme',
  'theme', 'setAspectRatio', 'aspectRatio', 'setOptimizationHint',
  'optimizationHint', 'setPolar', 'isPolar', 'setLabelMargin', 'labelMargin',
  'setRadialLabelOffset', 'radialLabelOffset', 'setHorizontalAspectRatio',
  'horizontalAspectRatio', 'setLocale', 'locale', 'queriedGraphPosition',
  'setMargin', 'margin', 'gridLineType', 'hasSeries', 'clearSelection',
  'addSeriesInternal', 'insertSeries', 'removeSeriesInternal', 'seriesList',
  'addCustomItem', 'removeCustomItems', 'removeCustomItem',
  'removeCustomItemAt', 'releaseCustomItem', 'selectedLabelIndex',
  'selectedAxis', 'selectedCustomItemIndex', 'selectedCustomItem',
  'doPicking', 'doRayPicking', 'setGraphParent',
  'queriedGraphPositionChanged', 'selectedElementChanged',
  'optimizationHintChanged', 'selectionModeChanged', 'themeChanged',
  'aspectRatioChanged', 'polarChanged', 'labelMarginChanged',
  'radialLabelOffsetChanged', 'horizontalAspectRatioChanged',
  'localeChanged', 'marginChanged', 'gridLineTypeChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGraphsNode::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickGraphsNode::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickGraphsNode::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QQuickGraphsNode::~QQuickGraphsNode()': the destructor: Python
    never removes a C++ QQuickGraphsNode.
  - Qt's 'QQmlListProperty<QCustom3DItem> QQuickGraphsNode::customItemList()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QQuickGraphsNode::setGridLineType(const
    QtGraphs3D::GridLineType &gridLineType)': takes a type Python has no way
    to hand over yet.

  What has no ritual
  ------------------

  2 of the 66 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickGraphsNode is created at the first use, not by
    'QQuickGraphsNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGraphsNode.
  - Qt tells when it has removed the C++ QQuickGraphsNode. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickGraphsNode that has no cute function yet,
    'customItemList', 'setGridLineType', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQuickGraphsNode::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsnode.html#tr

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
    #  QString QQuickGraphsNode::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuickGraphsNode2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGraphsNode'

  #  A C++ QQuickGraphsNode Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickGraphsNode'

  #  The functions Qt calls itself that QQuickGraphsNode is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setSelectionMode': (
          ('_ZN16QQuickGraphsNode16setSelectionModeE6QFlagsIN10QtGraphs3D13'
           'SelectionFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'flags', 'QtGraphs:QtGraphs3D.SelectionFlag'),
           )),
      ),
      'hasSeries': (
          ('_ZN16QQuickGraphsNode9hasSeriesEP17QAbstract3DSeries',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGraphs:QAbstract3DSeries'),
           )),
      ),
      'clearSelection': (
          ('_ZN16QQuickGraphsNode14clearSelectionEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'addSeriesInternal': (
          ('_ZN16QQuickGraphsNode17addSeriesInternalEP17QAbstract3DSeries',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGraphs:QAbstract3DSeries'),
           )),
      ),
      'removeSeriesInternal': (
          ('_ZN16QQuickGraphsNode20removeSeriesInternalEP17QAbstract3DSerie'
           's',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGraphs:QAbstract3DSeries'),
           )),
      ),
      'addCustomItem': (
          ('_ZN16QQuickGraphsNode13addCustomItemEP13QCustom3DItem',
           ('long long', 'number', ''),
           (
               ('address', 'address', 'QtGraphs:QCustom3DItem'),
           )),
      ),
      'removeCustomItems': (
          ('_ZN16QQuickGraphsNode17removeCustomItemsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'removeCustomItem': (
          ('_ZN16QQuickGraphsNode16removeCustomItemEP13QCustom3DItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGraphs:QCustom3DItem'),
           )),
      ),
      'removeCustomItemAt': (
          ('_ZN16QQuickGraphsNode18removeCustomItemAtE9QVector3D',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QVector3D'),
           )),
      ),
      'releaseCustomItem': (
          ('_ZN16QQuickGraphsNode17releaseCustomItemEP13QCustom3DItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGraphs:QCustom3DItem'),
           )),
      ),
      'selectedLabelIndex': (
          ('_ZNK16QQuickGraphsNode18selectedLabelIndexEv',
           ('int', 'number', ''),
           ()),
      ),
      'selectedAxis': (
          ('_ZNK16QQuickGraphsNode12selectedAxisEv',
           ('address', 'address', 'QtGraphs:QAbstract3DAxis'),
           ()),
      ),
      'selectedCustomItemIndex': (
          ('_ZNK16QQuickGraphsNode23selectedCustomItemIndexEv',
           ('long long', 'number', ''),
           ()),
      ),
      'selectedCustomItem': (
          ('_ZNK16QQuickGraphsNode18selectedCustomItemEv',
           ('address', 'address', 'QtGraphs:QCustom3DItem'),
           ()),
      ),
      'doPicking': (
          ('_ZN16QQuickGraphsNode9doPickingE7QPointF',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
           )),
      ),
      'doRayPicking': (
          ('_ZN16QQuickGraphsNode12doRayPickingERK9QVector3DS2_',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtGui:QVector3D'),
               ('address', 'value', 'QtGui:QVector3D'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGraphsNode::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsnode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGraphsNode::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickGraphsNode10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def selectedElement(self) -> QtGraphs3D.ElementType:
    """
    Calls Qt's 'QtGraphs3D::ElementType QQuickGraphsNode::selectedElement()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#selectedElement

    Returns
    -------

    QtGraphs3D.ElementType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtGraphs3D.ElementType(number)' gives.
    """
    #  QtGraphs3D::ElementType QQuickGraphsNode::selectedElement() const
    return QtGraphs3D.ElementType(self.uglySide.call(
        'ritual_ZNK16QQuickGraphsNode15selectedElementEv',
    ))

  def selectionMode(self) -> QtGraphs3D.SelectionFlags:
    """
    Calls Qt's 'QtGraphs3D::SelectionFlags QQuickGraphsNode::selectionMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#selectionMode

    Returns
    -------

    QtGraphs3D.SelectionFlags
      The value standing for the combination Qt gave back.
    """
    #  QtGraphs3D::SelectionFlags QQuickGraphsNode::selectionMode() const
    return QtGraphs3D.SelectionFlags(self.uglySide.call(
        'ritual_ZNK16QQuickGraphsNode13selectionModeEv',
    ))

  def theme(self) -> Optional[QGraphsTheme]:
    """
    Calls Qt's 'QGraphsTheme *QQuickGraphsNode::theme() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsnode.html#theme

    Returns
    -------

    Optional[QGraphsTheme]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphsTheme *QQuickGraphsNode::theme() const
    address = self.uglySide.call('ritual_ZNK16QQuickGraphsNode5themeEv')
    from . import QGraphsTheme
    return QGraphsTheme._cuteAt(address)

  def aspectRatio(self) -> float:
    """
    Calls Qt's 'qreal QQuickGraphsNode::aspectRatio() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsnode.html#aspectRatio
    """
    #  qreal QQuickGraphsNode::aspectRatio() const
    return self.uglySide.call('ritual_ZNK16QQuickGraphsNode11aspectRatioEv')

  def optimizationHint(self) -> QtGraphs3D.OptimizationHint:
    """
    Calls Qt's 'QtGraphs3D::OptimizationHint
    QQuickGraphsNode::optimizationHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#optimizationHint

    Returns
    -------

    QtGraphs3D.OptimizationHint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtGraphs3D.OptimizationHint(number)' gives.
    """
    #  QtGraphs3D::OptimizationHint QQuickGraphsNode::optimizationHint()
    #      const
    return QtGraphs3D.OptimizationHint(self.uglySide.call(
        'ritual_ZNK16QQuickGraphsNode16optimizationHintEv',
    ))

  def isPolar(self) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsNode::isPolar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsnode.html#isPolar
    """
    #  bool QQuickGraphsNode::isPolar() const
    return self.uglySide.call('ritual_ZNK16QQuickGraphsNode7isPolarEv')

  def labelMargin(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsNode::labelMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsnode.html#labelMargin
    """
    #  float QQuickGraphsNode::labelMargin() const
    return self.uglySide.call('ritual_ZNK16QQuickGraphsNode11labelMarginEv')

  def radialLabelOffset(self) -> float:
    """
    Calls Qt's 'float QQuickGraphsNode::radialLabelOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#radialLabelOffset
    """
    #  float QQuickGraphsNode::radialLabelOffset() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsNode17radialLabelOffsetEv',
    )

  def horizontalAspectRatio(self) -> float:
    """
    Calls Qt's 'qreal QQuickGraphsNode::horizontalAspectRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#horizontalAspectRatio
    """
    #  qreal QQuickGraphsNode::horizontalAspectRatio() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGraphsNode21horizontalAspectRatioEv',
    )

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QQuickGraphsNode::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsnode.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QQuickGraphsNode::locale() const
    address = self.uglySide.call('ritual_ZNK16QQuickGraphsNode6localeEv')
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  def queriedGraphPosition(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuickGraphsNode::queriedGraphPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#queriedGraphPosition

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuickGraphsNode::queriedGraphPosition() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickGraphsNode20queriedGraphPositionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def margin(self) -> float:
    """
    Calls Qt's 'qreal QQuickGraphsNode::margin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsnode.html#margin
    """
    #  qreal QQuickGraphsNode::margin() const
    return self.uglySide.call('ritual_ZNK16QQuickGraphsNode6marginEv')

  def gridLineType(self) -> QtGraphs3D.GridLineType:
    """
    Calls Qt's 'QtGraphs3D::GridLineType QQuickGraphsNode::gridLineType()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsnode.html#gridLineType

    Returns
    -------

    QtGraphs3D.GridLineType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtGraphs3D.GridLineType(number)' gives.
    """
    #  QtGraphs3D::GridLineType QQuickGraphsNode::gridLineType() const
    return QtGraphs3D.GridLineType(self.uglySide.call(
        'ritual_ZNK16QQuickGraphsNode12gridLineTypeEv',
    ))

  def selectedLabelIndex(self) -> int:
    """
    Calls Qt's 'int QQuickGraphsNode::selectedLabelIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#selectedLabelIndex
    """
    #  int QQuickGraphsNode::selectedLabelIndex() const
    ritual = 'ritual_ZNK16QQuickGraphsNode18selectedLabelIndexEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQuickGraphsNode18selectedLabelIndexEv'
    return self.uglySide.call(ritual)

  def selectedAxis(self) -> Optional[QAbstract3DAxis]:
    """
    Calls Qt's 'QAbstract3DAxis *QQuickGraphsNode::selectedAxis() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsnode.html#selectedAxis

    Returns
    -------

    Optional[QAbstract3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DAxis *QQuickGraphsNode::selectedAxis() const
    ritual = 'ritual_ZNK16QQuickGraphsNode12selectedAxisEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQuickGraphsNode12selectedAxisEv'
    address = self.uglySide.call(ritual)
    from . import QAbstract3DAxis
    return QAbstract3DAxis._cuteAt(address)

  def selectedCustomItemIndex(self) -> int:
    """
    Calls Qt's 'qsizetype QQuickGraphsNode::selectedCustomItemIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#selectedCustomItemIndex
    """
    #  qsizetype QQuickGraphsNode::selectedCustomItemIndex() const
    ritual = 'ritual_ZNK16QQuickGraphsNode23selectedCustomItemIndexEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQuickGraphsNode23selectedCustomItemIndexEv'
    return self.uglySide.call(ritual)

  def selectedCustomItem(self) -> Optional[QCustom3DItem]:
    """
    Calls Qt's 'QCustom3DItem *QQuickGraphsNode::selectedCustomItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#selectedCustomItem

    Returns
    -------

    Optional[QCustom3DItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCustom3DItem *QQuickGraphsNode::selectedCustomItem() const
    ritual = 'ritual_ZNK16QQuickGraphsNode18selectedCustomItemEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQuickGraphsNode18selectedCustomItemEv'
    address = self.uglySide.call(ritual)
    from . import QCustom3DItem
    return QCustom3DItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QtGraphs3D.SelectionFlags)
  def setSelectionMode(
      self,
      selectionMode: QtGraphs3D.SelectionFlags,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsNode::setSelectionMode(QtGraphs3D::SelectionFlags
    selectionMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#setSelectionMode

    Parameters
    ----------

    selectionMode : QtGraphs3D.SelectionFlags
      Passed on as its number.
    """
    #  void QQuickGraphsNode::setSelectionMode(QtGraphs3D::SelectionFlags
    #      selectionMode)
    ritual = (
        'ritual_ZN16QQuickGraphsNode16setSelectionModeE6QFlagsIN10QtGraphs3'
        'D13SelectionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsNode16setSelectionModeE6QFlagsIN10QtG'
          'raphs3D13SelectionFlagEE')
    self.uglySide.call(ritual, selectionMode.value)

  @overload(QGraphsTheme)
  @overload(NoneType)
  def setTheme(self, theme: Optional[QGraphsTheme]) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::setTheme(QGraphsTheme *theme)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsnode.html#setTheme

    Parameters
    ----------

    theme : Optional[QGraphsTheme]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsNode::setTheme(QGraphsTheme *theme)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsNode8setThemeEP12QGraphsTheme',
        self._addressOf(theme),
    )

  @overload(float)
  def setAspectRatio(self, aspectRatio: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::setAspectRatio(qreal aspectRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#setAspectRatio

    Parameters
    ----------

    aspectRatio : float
      Passed on as it is.
    """
    #  void QQuickGraphsNode::setAspectRatio(qreal aspectRatio)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsNode14setAspectRatioEd', aspectRatio,
    )

  @overload(QtGraphs3D.OptimizationHint)
  def setOptimizationHint(
      self,
      optimizationHint: QtGraphs3D.OptimizationHint,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGraphsNode::setOptimizationHint(QtGraphs3D::OptimizationHint
    optimizationHint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#setOptimizationHint

    Parameters
    ----------

    optimizationHint : QtGraphs3D.OptimizationHint
      Passed on as its number.
    """
    #  void
    #      QQuickGraphsNode::setOptimizationHint(QtGraphs3D::OptimizationHint
    #      optimizationHint)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsNode19setOptimizationHintEN10QtGraphs3D16Op'
        'timizationHintE',
        optimizationHint.value,
    )

  @overload(bool)
  def setPolar(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::setPolar(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsnode.html#setPolar

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickGraphsNode::setPolar(bool enabled)
    self.uglySide.call('ritual_ZN16QQuickGraphsNode8setPolarEb', enabled)

  @overload(float)
  def setLabelMargin(self, labelMargin: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::setLabelMargin(float labelMargin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#setLabelMargin

    Parameters
    ----------

    labelMargin : float
      Passed on as it is.
    """
    #  void QQuickGraphsNode::setLabelMargin(float labelMargin)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsNode14setLabelMarginEf', labelMargin,
    )

  @overload(float)
  def setRadialLabelOffset(self, radialLabelOffset: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::setRadialLabelOffset(float
    radialLabelOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#setRadialLabelOffset

    Parameters
    ----------

    radialLabelOffset : float
      Passed on as it is.
    """
    #  void QQuickGraphsNode::setRadialLabelOffset(float radialLabelOffset)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsNode20setRadialLabelOffsetEf',
        radialLabelOffset,
    )

  @overload(float)
  def setHorizontalAspectRatio(self, horizontalAspectRatio: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::setHorizontalAspectRatio(qreal
    horizontalAspectRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#setHorizontalAspectRatio

    Parameters
    ----------

    horizontalAspectRatio : float
      Passed on as it is.
    """
    #  void QQuickGraphsNode::setHorizontalAspectRatio(qreal
    #      horizontalAspectRatio)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsNode24setHorizontalAspectRatioEd',
        horizontalAspectRatio,
    )

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::setLocale(QLocale locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsnode.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QQuickGraphsNode::setLocale(QLocale locale)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsNode9setLocaleE7QLocale',
        self._valueOf(locale),
    )

  @overload(float)
  def setMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::setMargin(qreal margin)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsnode.html#setMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QQuickGraphsNode::setMargin(qreal margin)
    self.uglySide.call('ritual_ZN16QQuickGraphsNode9setMarginEd', margin)

  def setGraphParent(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::setGraphParent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#setGraphParent
    """
    #  void QQuickGraphsNode::setGraphParent()
    self.uglySide.call('ritual_ZN16QQuickGraphsNode14setGraphParentEv')

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
    'QQuickGraphsNode::QQuickGraphsNode(QQuick3DNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#QQuickGraphsNode

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickGraphsNode::QQuickGraphsNode(QQuick3DNode *parent)
    self._noteCreation(QQuickGraphsNode, lambda: Rituals.call(
        'ritual_ZN16QQuickGraphsNodeC1EP12QQuick3DNode',
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

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#componentComplete
    """
    #  void QQuickGraphsNode::componentComplete()
    ritual = 'ritual_ZN16QQuickGraphsNode17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsNode17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def hasSeries(self, series: Optional[QAbstract3DSeries]) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsNode::hasSeries(QAbstract3DSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsnode.html#hasSeries

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickGraphsNode::hasSeries(QAbstract3DSeries *series)
    ritual = 'ritual_ZN16QQuickGraphsNode9hasSeriesEP17QAbstract3DSeries'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsNode9hasSeriesEP17QAbstract3DSeries')
    return self.uglySide.call(ritual, self._addressOf(series))

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::clearSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#clearSelection
    """
    #  void QQuickGraphsNode::clearSelection()
    self.uglySide.call('ritual_ZN16QQuickGraphsNode14clearSelectionEv')

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def addSeriesInternal(self, series: Optional[QAbstract3DSeries]) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::addSeriesInternal(QAbstract3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#addSeriesInternal

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsNode::addSeriesInternal(QAbstract3DSeries *series)
    ritual = (
        'ritual_ZN16QQuickGraphsNode17addSeriesInternalEP17QAbstract3DSerie'
        's')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsNode17addSeriesInternalEP17QAbstract3'
          'DSeries')
    self.uglySide.call(ritual, self._addressOf(series))

  @overload(int, QAbstract3DSeries)
  @overload(int, NoneType)
  def insertSeries(
      self,
      index: int,
      series: Optional[QAbstract3DSeries],
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::insertSeries(qsizetype index,
    QAbstract3DSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsnode.html#insertSeries

    Parameters
    ----------

    index : int
      Passed on as it is.

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsNode::insertSeries(qsizetype index, QAbstract3DSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsNode12insertSeriesExP17QAbstract3DSeries',
        index, self._addressOf(series),
    )

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def removeSeriesInternal(
      self,
      series: Optional[QAbstract3DSeries],
  ) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::removeSeriesInternal(QAbstract3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#removeSeriesInternal

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsNode::removeSeriesInternal(QAbstract3DSeries *series)
    ritual = (
        'ritual_ZN16QQuickGraphsNode20removeSeriesInternalEP17QAbstract3DSe'
        'ries')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsNode20removeSeriesInternalEP17QAbstra'
          'ct3DSeries')
    self.uglySide.call(ritual, self._addressOf(series))

  def seriesList(self) -> QList[QAbstract3DSeries]:
    """
    Calls Qt's 'QList<QAbstract3DSeries *> QQuickGraphsNode::seriesList()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsnode.html#seriesList

    Returns
    -------

    QList[QAbstract3DSeries]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstract3DSeries *> QQuickGraphsNode::seriesList()
    address = self.uglySide.call('ritual_ZN16QQuickGraphsNode10seriesListEv')
    from . import QAbstract3DSeries
    return QList[QAbstract3DSeries]._cuteOwning(address)

  @overload(QCustom3DItem)
  @overload(NoneType)
  def addCustomItem(self, item: Optional[QCustom3DItem]) -> int:
    """
    Calls Qt's 'qsizetype QQuickGraphsNode::addCustomItem(QCustom3DItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#addCustomItem

    Parameters
    ----------

    item : Optional[QCustom3DItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qsizetype QQuickGraphsNode::addCustomItem(QCustom3DItem *item)
    ritual = 'ritual_ZN16QQuickGraphsNode13addCustomItemEP13QCustom3DItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsNode13addCustomItemEP13QCustom3DItem')
    return self.uglySide.call(ritual, self._addressOf(item))

  def removeCustomItems(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::removeCustomItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#removeCustomItems
    """
    #  void QQuickGraphsNode::removeCustomItems()
    ritual = 'ritual_ZN16QQuickGraphsNode17removeCustomItemsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGraphsNode17removeCustomItemsEv'
    self.uglySide.call(ritual)

  @overload(QCustom3DItem)
  @overload(NoneType)
  def removeCustomItem(self, item: Optional[QCustom3DItem]) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::removeCustomItem(QCustom3DItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#removeCustomItem

    Parameters
    ----------

    item : Optional[QCustom3DItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsNode::removeCustomItem(QCustom3DItem *item)
    ritual = 'ritual_ZN16QQuickGraphsNode16removeCustomItemEP13QCustom3DItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsNode16removeCustomItemEP13QCustom3DIt'
          'em')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QVector3D)
  def removeCustomItemAt(self, position: QVector3D) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::removeCustomItemAt(QVector3D
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#removeCustomItemAt

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuickGraphsNode::removeCustomItemAt(QVector3D position)
    ritual = 'ritual_ZN16QQuickGraphsNode18removeCustomItemAtE9QVector3D'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsNode18removeCustomItemAtE9QVector3D')
    self.uglySide.call(ritual, self._valueOf(position))

  @overload(QCustom3DItem)
  @overload(NoneType)
  def releaseCustomItem(self, item: Optional[QCustom3DItem]) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::releaseCustomItem(QCustom3DItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#releaseCustomItem

    Parameters
    ----------

    item : Optional[QCustom3DItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGraphsNode::releaseCustomItem(QCustom3DItem *item)
    ritual = (
        'ritual_ZN16QQuickGraphsNode17releaseCustomItemEP13QCustom3DItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickGraphsNode17releaseCustomItemEP13QCustom3DI'
          'tem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QPointF)
  def doPicking(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsNode::doPicking(QPointF point)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsnode.html#doPicking

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QQuickGraphsNode::doPicking(QPointF point)
    return self.uglySide.call(
        'ritual_ZN16QQuickGraphsNode9doPickingE7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(QVector3D, QVector3D)
  def doRayPicking(self, origin: QVector3D, direction: QVector3D) -> bool:
    """
    Calls Qt's 'bool QQuickGraphsNode::doRayPicking(const QVector3D &origin,
    const QVector3D &direction)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsnode.html#doRayPicking

    Parameters
    ----------

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  bool QQuickGraphsNode::doRayPicking(const QVector3D &origin, const
    #      QVector3D &direction)
    return self.uglySide.call(
        'ritual_ZN16QQuickGraphsNode12doRayPickingERK9QVector3DS2_',
        self._valueOf(origin), self._valueOf(direction),
    )

  def queriedGraphPositionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::queriedGraphPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#queriedGraphPositionChanged
    """
    #  void QQuickGraphsNode::queriedGraphPositionChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsNode27queriedGraphPositionChangedEv',
    )

  def selectedElementChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::selectedElementChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#selectedElementChanged
    """
    #  void QQuickGraphsNode::selectedElementChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsNode22selectedElementChangedEv',
    )

  def optimizationHintChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::optimizationHintChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#optimizationHintChanged
    """
    #  void QQuickGraphsNode::optimizationHintChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsNode23optimizationHintChangedEv',
    )

  def selectionModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::selectionModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#selectionModeChanged
    """
    #  void QQuickGraphsNode::selectionModeChanged()
    self.uglySide.call('ritual_ZN16QQuickGraphsNode20selectionModeChangedEv')

  def themeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::themeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsnode.html#themeChanged
    """
    #  void QQuickGraphsNode::themeChanged()
    self.uglySide.call('ritual_ZN16QQuickGraphsNode12themeChangedEv')

  def aspectRatioChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::aspectRatioChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#aspectRatioChanged
    """
    #  void QQuickGraphsNode::aspectRatioChanged()
    self.uglySide.call('ritual_ZN16QQuickGraphsNode18aspectRatioChangedEv')

  def polarChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::polarChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgraphsnode.html#polarChanged
    """
    #  void QQuickGraphsNode::polarChanged()
    self.uglySide.call('ritual_ZN16QQuickGraphsNode12polarChangedEv')

  def labelMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::labelMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#labelMarginChanged
    """
    #  void QQuickGraphsNode::labelMarginChanged()
    self.uglySide.call('ritual_ZN16QQuickGraphsNode18labelMarginChangedEv')

  def radialLabelOffsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::radialLabelOffsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#radialLabelOffsetChanged
    """
    #  void QQuickGraphsNode::radialLabelOffsetChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsNode24radialLabelOffsetChangedEv',
    )

  def horizontalAspectRatioChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::horizontalAspectRatioChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#horizontalAspectRatioChanged
    """
    #  void QQuickGraphsNode::horizontalAspectRatioChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsNode28horizontalAspectRatioChangedEv',
    )

  def localeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::localeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#localeChanged
    """
    #  void QQuickGraphsNode::localeChanged()
    self.uglySide.call('ritual_ZN16QQuickGraphsNode13localeChangedEv')

  @overload(float)
  def marginChanged(self, margin: float) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::marginChanged(qreal margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#marginChanged

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QQuickGraphsNode::marginChanged(qreal margin)
    self.uglySide.call(
        'ritual_ZN16QQuickGraphsNode13marginChangedEd', margin,
    )

  def gridLineTypeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGraphsNode::gridLineTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgraphsnode.html#gridLineTypeChanged
    """
    #  void QQuickGraphsNode::gridLineTypeChanged()
    self.uglySide.call('ritual_ZN16QQuickGraphsNode19gridLineTypeChangedEv')

  @staticmethod
  def customItemList(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QCustom3DItem> QQuickGraphsNode::customItemList()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsNode.customItemList' has no cute function yet. Qt's "
        "'QQmlListProperty<QCustom3DItem> "
        "QQuickGraphsNode::customItemList() const': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def setGridLineType(*__, **_) -> Never:
    """
    Qt's 'void QQuickGraphsNode::setGridLineType(const
    QtGraphs3D::GridLineType &gridLineType)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickGraphsNode.setGridLineType' has no cute function yet. Qt's "
        "'void QQuickGraphsNode::setGridLineType(const "
        "QtGraphs3D::GridLineType &gridLineType)': takes a type Python has "
        "no way to hand over yet.")
