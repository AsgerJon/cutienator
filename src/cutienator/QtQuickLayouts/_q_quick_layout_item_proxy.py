"""
QQuickLayoutItemProxy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutitemproxy_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickLayoutItemProxy to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF
  from . import QQuickLayoutItemProxyPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']


class QQuickLayoutItemProxy(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickLayoutItemProxy: a plain Python object standing
  in front of one C++ QQuickLayoutItemProxy.

  What exists
  -----------

  Every function of Qt's QQuickLayoutItemProxy that has a ritual and that
  Python can call so far, 40 names in all: 'metaObject', 'geometryChange',
  'itemChange', 'target', 'clearTarget', 'updatePos',
  'targetMinimumWidthChanged', 'proxyMinimumWidthChanged',
  'targetMinimumHeightChanged', 'proxyMinimumHeightChanged',
  'targetPreferredWidthChanged', 'proxyPreferredWidthChanged',
  'targetPreferredHeightChanged', 'proxyPreferredHeightChanged',
  'targetMaximumWidthChanged', 'proxyMaximumWidthChanged',
  'targetMaximumHeightChanged', 'proxyMaximumHeightChanged',
  'targetFillWidthChanged', 'proxyFillWidthChanged',
  'targetFillHeightChanged', 'proxyFillHeightChanged',
  'targetAlignmentChanged', 'proxyAlignmentChanged',
  'targetHorizontalStretchFactorChanged',
  'proxyHorizontalStretchFactorChanged',
  'targetVerticalStretchFactorChanged', 'proxyVerticalStretchFactorChanged',
  'targetMarginsChanged', 'proxyMarginsChanged', 'targetLeftMarginChanged',
  'proxyLeftMarginChanged', 'targetTopMarginChanged',
  'proxyTopMarginChanged', 'targetRightMarginChanged',
  'proxyRightMarginChanged', 'targetBottomMarginChanged',
  'proxyBottomMarginChanged', 'targetChanged', 'd_func'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickLayoutItemProxy::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickLayoutItemProxy::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickLayoutItemProxy::~QQuickLayoutItemProxy()': the destructor:
    Python never removes a C++ QQuickLayoutItemProxy.
  - Qt's 'const QQuickLayoutItemProxyPrivate *QQuickLayoutItemProxy::d_func()
    const': takes in Python what 'QQuickLayoutItemProxyPrivate
    *QQuickLayoutItemProxy::d_func()' takes.

  What has no ritual
  ------------------

  7 of the 51 functions Qt declares: 3 leans on 'QQuickLayoutItemProxy; 2 not
  a gap; 1 Qt's library has no name for it, and its code in Qt's source does
  not compile apart from its file; 1 leans on
  'QQuickLayoutItemProxyAttachedData.

  What to expect
  --------------

  - The C++ QQuickLayoutItemProxy is created at the first use, not by
    'QQuickLayoutItemProxy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLayoutItemProxy.
  - Qt tells when it has removed the C++ QQuickLayoutItemProxy. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickLayoutItemProxy that has no cute function yet,
    '__init__', 'effectiveTarget', 'maybeTakeControl', 'setTarget', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLayoutItemProxy'

  #  A C++ QQuickLayoutItemProxy Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickLayoutItemProxy'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickLayoutItemProxy::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLayoutItemProxy::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickLayoutItemProxy10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def target(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickLayoutItemProxy::target() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayoutitemproxy.html#target

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickLayoutItemProxy::target() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickLayoutItemProxy6targetEv',
    )
    return QQuickItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickLayoutItemProxy::QQuickLayoutItemProxy(QQuickItem *parent)':
    leans on 'QQuickLayoutItemProxy::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLayoutItemProxy.__init__' has no cute function yet. Qt's "
        "'QQuickLayoutItemProxy::QQuickLayoutItemProxy(QQuickItem "
        "*parent)': leans on "
        "'QQuickLayoutItemProxy::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeom: QRectF, oldGeom: QRectF) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::geometryChange(const QRectF
    &newGeom, const QRectF &oldGeom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html#geometryChange

    Parameters
    ----------

    newGeom : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeom : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickLayoutItemProxy::geometryChange(const QRectF &newGeom,
    #      const QRectF &oldGeom)
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy14geometryChangeERK6QRectFS2_',
        self._valueOf(newGeom), self._valueOf(oldGeom),
    )

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      c: QQuickItem.ItemChange,
      d: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::itemChange(ItemChange c, const
    ItemChangeData &d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html#itemChange

    Parameters
    ----------

    c : QQuickItem.ItemChange
      Passed on as its number.

    d : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickLayoutItemProxy::itemChange(ItemChange c, const
    #      ItemChangeData &d)
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy10itemChangeEN10QQuickItem10ItemCh'
        'angeERKNS0_14ItemChangeDataE',
        c.value, self._valueOf(d),
    )

  def clearTarget(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::clearTarget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html#clearTarget
    """
    #  void QQuickLayoutItemProxy::clearTarget()
    self.uglySide.call('ritual_ZN21QQuickLayoutItemProxy11clearTargetEv')

  def updatePos(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::updatePos()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html#updatePos
    """
    #  void QQuickLayoutItemProxy::updatePos()
    self.uglySide.call('ritual_ZN21QQuickLayoutItemProxy9updatePosEv')

  def targetMinimumWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::targetMinimumWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html
    """
    #  void QQuickLayoutItemProxy::targetMinimumWidthChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy25targetMinimumWidthChangedEv',
    )

  def proxyMinimumWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::proxyMinimumWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html
    """
    #  void QQuickLayoutItemProxy::proxyMinimumWidthChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy24proxyMinimumWidthChangedEv',
    )

  def targetMinimumHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::targetMinimumHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html
    """
    #  void QQuickLayoutItemProxy::targetMinimumHeightChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy26targetMinimumHeightChangedEv',
    )

  def proxyMinimumHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::proxyMinimumHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html
    """
    #  void QQuickLayoutItemProxy::proxyMinimumHeightChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy25proxyMinimumHeightChangedEv',
    )

  def targetPreferredWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::targetPreferredWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html
    """
    #  void QQuickLayoutItemProxy::targetPreferredWidthChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy27targetPreferredWidthChangedEv',
    )

  def proxyPreferredWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::proxyPreferredWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html
    """
    #  void QQuickLayoutItemProxy::proxyPreferredWidthChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy26proxyPreferredWidthChangedEv',
    )

  def targetPreferredHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::targetPreferredHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html
    """
    #  void QQuickLayoutItemProxy::targetPreferredHeightChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy28targetPreferredHeightChangedEv',
    )

  def proxyPreferredHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::proxyPreferredHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html
    """
    #  void QQuickLayoutItemProxy::proxyPreferredHeightChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy27proxyPreferredHeightChangedEv',
    )

  def targetMaximumWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::targetMaximumWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html
    """
    #  void QQuickLayoutItemProxy::targetMaximumWidthChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy25targetMaximumWidthChangedEv',
    )

  def proxyMaximumWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::proxyMaximumWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html
    """
    #  void QQuickLayoutItemProxy::proxyMaximumWidthChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy24proxyMaximumWidthChangedEv',
    )

  def targetMaximumHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::targetMaximumHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html
    """
    #  void QQuickLayoutItemProxy::targetMaximumHeightChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy26targetMaximumHeightChangedEv',
    )

  def proxyMaximumHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::proxyMaximumHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html
    """
    #  void QQuickLayoutItemProxy::proxyMaximumHeightChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy25proxyMaximumHeightChangedEv',
    )

  def targetFillWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::targetFillWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html#targetFillWidthChanged
    """
    #  void QQuickLayoutItemProxy::targetFillWidthChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy22targetFillWidthChangedEv',
    )

  def proxyFillWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::proxyFillWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html#proxyFillWidthChanged
    """
    #  void QQuickLayoutItemProxy::proxyFillWidthChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy21proxyFillWidthChangedEv',
    )

  def targetFillHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::targetFillHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html#targetFillHeightChanged
    """
    #  void QQuickLayoutItemProxy::targetFillHeightChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy23targetFillHeightChangedEv',
    )

  def proxyFillHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::proxyFillHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html#proxyFillHeightChanged
    """
    #  void QQuickLayoutItemProxy::proxyFillHeightChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy22proxyFillHeightChangedEv',
    )

  def targetAlignmentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::targetAlignmentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html#targetAlignmentChanged
    """
    #  void QQuickLayoutItemProxy::targetAlignmentChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy22targetAlignmentChangedEv',
    )

  def proxyAlignmentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::proxyAlignmentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html#proxyAlignmentChanged
    """
    #  void QQuickLayoutItemProxy::proxyAlignmentChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy21proxyAlignmentChangedEv',
    )

  def targetHorizontalStretchFactorChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickLayoutItemProxy::targetHorizontalStretchFactorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html
    """
    #  void QQuickLayoutItemProxy::targetHorizontalStretchFactorChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy36targetHorizontalStretchFactorCha'
        'ngedEv',
    )

  def proxyHorizontalStretchFactorChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickLayoutItemProxy::proxyHorizontalStretchFactorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html
    """
    #  void QQuickLayoutItemProxy::proxyHorizontalStretchFactorChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy35proxyHorizontalStretchFactorChan'
        'gedEv',
    )

  def targetVerticalStretchFactorChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickLayoutItemProxy::targetVerticalStretchFactorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html
    """
    #  void QQuickLayoutItemProxy::targetVerticalStretchFactorChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy34targetVerticalStretchFactorChang'
        'edEv',
    )

  def proxyVerticalStretchFactorChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickLayoutItemProxy::proxyVerticalStretchFactorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html
    """
    #  void QQuickLayoutItemProxy::proxyVerticalStretchFactorChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy33proxyVerticalStretchFactorChange'
        'dEv',
    )

  def targetMarginsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::targetMarginsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html#targetMarginsChanged
    """
    #  void QQuickLayoutItemProxy::targetMarginsChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy20targetMarginsChangedEv',
    )

  def proxyMarginsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::proxyMarginsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html#proxyMarginsChanged
    """
    #  void QQuickLayoutItemProxy::proxyMarginsChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy19proxyMarginsChangedEv',
    )

  def targetLeftMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::targetLeftMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html#targetLeftMarginChanged
    """
    #  void QQuickLayoutItemProxy::targetLeftMarginChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy23targetLeftMarginChangedEv',
    )

  def proxyLeftMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::proxyLeftMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html#proxyLeftMarginChanged
    """
    #  void QQuickLayoutItemProxy::proxyLeftMarginChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy22proxyLeftMarginChangedEv',
    )

  def targetTopMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::targetTopMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html#targetTopMarginChanged
    """
    #  void QQuickLayoutItemProxy::targetTopMarginChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy22targetTopMarginChangedEv',
    )

  def proxyTopMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::proxyTopMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html#proxyTopMarginChanged
    """
    #  void QQuickLayoutItemProxy::proxyTopMarginChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy21proxyTopMarginChangedEv',
    )

  def targetRightMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::targetRightMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html
    """
    #  void QQuickLayoutItemProxy::targetRightMarginChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy24targetRightMarginChangedEv',
    )

  def proxyRightMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::proxyRightMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html#proxyRightMarginChanged
    """
    #  void QQuickLayoutItemProxy::proxyRightMarginChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy23proxyRightMarginChangedEv',
    )

  def targetBottomMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::targetBottomMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html
    """
    #  void QQuickLayoutItemProxy::targetBottomMarginChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy25targetBottomMarginChangedEv',
    )

  def proxyBottomMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::proxyBottomMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html
    """
    #  void QQuickLayoutItemProxy::proxyBottomMarginChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickLayoutItemProxy24proxyBottomMarginChangedEv',
    )

  def targetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxy::targetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxy.html#targetChanged
    """
    #  void QQuickLayoutItemProxy::targetChanged()
    self.uglySide.call('ritual_ZN21QQuickLayoutItemProxy13targetChangedEv')

  def d_func(self) -> Optional[QQuickLayoutItemProxyPrivate]:
    """
    Calls Qt's 'QQuickLayoutItemProxyPrivate
    *QQuickLayoutItemProxy::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayoutitemproxy.html#d_func

    Returns
    -------

    Optional[QQuickLayoutItemProxyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickLayoutItemProxyPrivate *QQuickLayoutItemProxy::d_func()
    address = self.uglySide.call('ritual_ZN21QQuickLayoutItemProxy6d_funcEv')
    from . import QQuickLayoutItemProxyPrivate
    return QQuickLayoutItemProxyPrivate._cuteAt(address)

  @staticmethod
  def effectiveTarget(*__, **_) -> Never:
    """
    Qt's 'QQuickItem *QQuickLayoutItemProxy::effectiveTarget() const': leans
    on 'QQuickLayoutItemProxyAttachedData::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickLayoutItemProxy.effectiveTarget' has no cute function yet. "
        "Qt's 'QQuickItem *QQuickLayoutItemProxy::effectiveTarget() const': "
        "leans on 'QQuickLayoutItemProxyAttachedData::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def maybeTakeControl(*__, **_) -> Never:
    """
    Qt's 'void QQuickLayoutItemProxy::maybeTakeControl()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: unknown type name 'lcLayouts'; did you mean 'QLayout'?.
    """
    raise NotImplementedError(
        "'QQuickLayoutItemProxy.maybeTakeControl' has no cute function yet. "
        "Qt's 'void QQuickLayoutItemProxy::maybeTakeControl()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: unknown type name 'lcLayouts'; did "
        "you mean 'QLayout'?.")

  @staticmethod
  def setTarget(*__, **_) -> Never:
    """
    Qt's 'void QQuickLayoutItemProxy::setTarget(QQuickItem *newTarget)':
    leans on 'QQuickLayoutItemProxy::targetChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLayoutItemProxy.setTarget' has no cute function yet. Qt's "
        "'void QQuickLayoutItemProxy::setTarget(QQuickItem *newTarget)': "
        "leans on 'QQuickLayoutItemProxy::targetChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
