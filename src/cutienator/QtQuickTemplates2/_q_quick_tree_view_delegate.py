"""
QQuickTreeViewDelegate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktreeviewdelegate_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickTreeViewDelegate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem
from . import QQuickItemDelegate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF
  from ..QtGui import QFont, QMouseEvent
  from ..QtQuick import QQuickTreeView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMouseEvent = WAIT['QMouseEvent']
  QQuickTreeView = WAIT['QQuickTreeView']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTreeViewDelegate(QQuickItemDelegate):
  """
  The cute side of Qt's QQuickTreeViewDelegate: a plain Python object
  standing in front of one C++ QQuickTreeViewDelegate.

  It is built on the cute 'QQuickItemDelegate', as Qt's
  QQuickTreeViewDelegate is built on Qt's QQuickItemDelegate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTreeViewDelegate that has a ritual and that
  Python can call so far, 40 names in all: 'metaObject', 'tr', 'indentation',
  'setIndentation', 'isTreeNode', 'setIsTreeNode', 'hasChildren',
  'setHasChildren', 'expanded', 'setExpanded', 'current', 'setCurrent',
  'selected', 'setSelected', 'editing', 'setEditing', 'depth', 'setDepth',
  'treeView', 'setTreeView', 'leftMargin', 'setLeftMargin', 'rightMargin',
  'setRightMargin', 'indicatorChanged', 'indentationChanged',
  'isTreeNodeChanged', 'hasChildrenChanged', 'expandedChanged',
  'depthChanged', 'treeviewChanged', 'leftMarginChanged',
  'rightMarginChanged', 'currentChanged', 'selectedChanged',
  'editingChanged', 'defaultFont', 'geometryChange', 'componentComplete',
  'mousePressEvent'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTreeViewDelegate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickTreeViewDelegate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickTreeViewDelegatePrivate *QQuickTreeViewDelegate::d_func()':
    gives 'QQuickTreeViewDelegatePrivate', which has no cute class yet.
  - Qt's 'const QQuickTreeViewDelegatePrivate
    *QQuickTreeViewDelegate::d_func() const': gives
    'QQuickTreeViewDelegatePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 49 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickTreeViewDelegate is created at the first use, not by
    'QQuickTreeViewDelegate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTreeViewDelegate.
  - Qt tells when it has removed the C++ QQuickTreeViewDelegate. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickTreeViewDelegate::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#tr

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
    #  QString QQuickTreeViewDelegate::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QQuickTreeViewDelegate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTreeViewDelegate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTreeViewDelegate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTreeViewDelegate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickTreeViewDelegate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def indentation(self) -> float:
    """
    Calls Qt's 'qreal QQuickTreeViewDelegate::indentation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#indentation
    """
    #  qreal QQuickTreeViewDelegate::indentation() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTreeViewDelegate11indentationEv',
    )

  def isTreeNode(self) -> bool:
    """
    Calls Qt's 'bool QQuickTreeViewDelegate::isTreeNode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#isTreeNode
    """
    #  bool QQuickTreeViewDelegate::isTreeNode() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTreeViewDelegate10isTreeNodeEv',
    )

  def hasChildren(self) -> bool:
    """
    Calls Qt's 'bool QQuickTreeViewDelegate::hasChildren() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#hasChildren
    """
    #  bool QQuickTreeViewDelegate::hasChildren() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTreeViewDelegate11hasChildrenEv',
    )

  def expanded(self) -> bool:
    """
    Calls Qt's 'bool QQuickTreeViewDelegate::expanded() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#expanded
    """
    #  bool QQuickTreeViewDelegate::expanded() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTreeViewDelegate8expandedEv',
    )

  def current(self) -> bool:
    """
    Calls Qt's 'bool QQuickTreeViewDelegate::current() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#current
    """
    #  bool QQuickTreeViewDelegate::current() const
    return self.uglySide.call('ritual_ZNK22QQuickTreeViewDelegate7currentEv')

  def selected(self) -> bool:
    """
    Calls Qt's 'bool QQuickTreeViewDelegate::selected() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#selected
    """
    #  bool QQuickTreeViewDelegate::selected() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTreeViewDelegate8selectedEv',
    )

  def editing(self) -> bool:
    """
    Calls Qt's 'bool QQuickTreeViewDelegate::editing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#editing
    """
    #  bool QQuickTreeViewDelegate::editing() const
    return self.uglySide.call('ritual_ZNK22QQuickTreeViewDelegate7editingEv')

  def depth(self) -> int:
    """
    Calls Qt's 'int QQuickTreeViewDelegate::depth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#depth
    """
    #  int QQuickTreeViewDelegate::depth() const
    return self.uglySide.call('ritual_ZNK22QQuickTreeViewDelegate5depthEv')

  def treeView(self) -> Optional[QQuickTreeView]:
    """
    Calls Qt's 'QQuickTreeView *QQuickTreeViewDelegate::treeView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#treeView

    Returns
    -------

    Optional[QQuickTreeView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTreeView *QQuickTreeViewDelegate::treeView() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickTreeViewDelegate8treeViewEv',
    )
    from ..QtQuick import QQuickTreeView
    return QQuickTreeView._cuteAt(address)

  def leftMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickTreeViewDelegate::leftMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#leftMargin
    """
    #  qreal QQuickTreeViewDelegate::leftMargin() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTreeViewDelegate10leftMarginEv',
    )

  def rightMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickTreeViewDelegate::rightMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#rightMargin
    """
    #  qreal QQuickTreeViewDelegate::rightMargin() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTreeViewDelegate11rightMarginEv',
    )

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickTreeViewDelegate::defaultFont() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickTreeViewDelegate::defaultFont() const
    ritual = 'ritual_ZNK22QQuickTreeViewDelegate11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickTreeViewDelegate11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setIndentation(self, indentation: float) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::setIndentation(qreal
    indentation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#setIndentation

    Parameters
    ----------

    indentation : float
      Passed on as it is.
    """
    #  void QQuickTreeViewDelegate::setIndentation(qreal indentation)
    self.uglySide.call(
        'ritual_ZN22QQuickTreeViewDelegate14setIndentationEd', indentation,
    )

  @overload(bool)
  def setIsTreeNode(self, isTreeNode: bool) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::setIsTreeNode(bool isTreeNode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#setIsTreeNode

    Parameters
    ----------

    isTreeNode : bool
      Passed on as it is.
    """
    #  void QQuickTreeViewDelegate::setIsTreeNode(bool isTreeNode)
    self.uglySide.call(
        'ritual_ZN22QQuickTreeViewDelegate13setIsTreeNodeEb', isTreeNode,
    )

  @overload(bool)
  def setHasChildren(self, hasChildren: bool) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::setHasChildren(bool
    hasChildren)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#setHasChildren

    Parameters
    ----------

    hasChildren : bool
      Passed on as it is.
    """
    #  void QQuickTreeViewDelegate::setHasChildren(bool hasChildren)
    self.uglySide.call(
        'ritual_ZN22QQuickTreeViewDelegate14setHasChildrenEb', hasChildren,
    )

  @overload(bool)
  def setExpanded(self, expanded: bool) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::setExpanded(bool expanded)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#setExpanded

    Parameters
    ----------

    expanded : bool
      Passed on as it is.
    """
    #  void QQuickTreeViewDelegate::setExpanded(bool expanded)
    self.uglySide.call(
        'ritual_ZN22QQuickTreeViewDelegate11setExpandedEb', expanded,
    )

  @overload(bool)
  def setCurrent(self, current: bool) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::setCurrent(bool current)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#setCurrent

    Parameters
    ----------

    current : bool
      Passed on as it is.
    """
    #  void QQuickTreeViewDelegate::setCurrent(bool current)
    self.uglySide.call(
        'ritual_ZN22QQuickTreeViewDelegate10setCurrentEb', current,
    )

  @overload(bool)
  def setSelected(self, selected: bool) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::setSelected(bool selected)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#setSelected

    Parameters
    ----------

    selected : bool
      Passed on as it is.
    """
    #  void QQuickTreeViewDelegate::setSelected(bool selected)
    self.uglySide.call(
        'ritual_ZN22QQuickTreeViewDelegate11setSelectedEb', selected,
    )

  @overload(bool)
  def setEditing(self, editing: bool) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::setEditing(bool editing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#setEditing

    Parameters
    ----------

    editing : bool
      Passed on as it is.
    """
    #  void QQuickTreeViewDelegate::setEditing(bool editing)
    self.uglySide.call(
        'ritual_ZN22QQuickTreeViewDelegate10setEditingEb', editing,
    )

  @overload(int)
  def setDepth(self, depth: int) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::setDepth(int depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#setDepth

    Parameters
    ----------

    depth : int
      Passed on as it is.
    """
    #  void QQuickTreeViewDelegate::setDepth(int depth)
    self.uglySide.call('ritual_ZN22QQuickTreeViewDelegate8setDepthEi', depth)

  @overload(QQuickTreeView)
  @overload(NoneType)
  def setTreeView(self, treeView: Optional[QQuickTreeView]) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::setTreeView(QQuickTreeView
    *treeView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#setTreeView

    Parameters
    ----------

    treeView : Optional[QQuickTreeView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTreeViewDelegate::setTreeView(QQuickTreeView *treeView)
    self.uglySide.call(
        'ritual_ZN22QQuickTreeViewDelegate11setTreeViewEP14QQuickTreeView',
        self._addressOf(treeView),
    )

  @overload(float)
  def setLeftMargin(self, leftMargin: float) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::setLeftMargin(qreal
    leftMargin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#setLeftMargin

    Parameters
    ----------

    leftMargin : float
      Passed on as it is.
    """
    #  void QQuickTreeViewDelegate::setLeftMargin(qreal leftMargin)
    self.uglySide.call(
        'ritual_ZN22QQuickTreeViewDelegate13setLeftMarginEd', leftMargin,
    )

  @overload(float)
  def setRightMargin(self, rightMargin: float) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::setRightMargin(qreal
    rightMargin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#setRightMargin

    Parameters
    ----------

    rightMargin : float
      Passed on as it is.
    """
    #  void QQuickTreeViewDelegate::setRightMargin(qreal rightMargin)
    self.uglySide.call(
        'ritual_ZN22QQuickTreeViewDelegate14setRightMarginEd', rightMargin,
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
    'QQuickTreeViewDelegate::QQuickTreeViewDelegate(QQuickItem *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#QQuickTreeViewDelegate

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTreeViewDelegate::QQuickTreeViewDelegate(QQuickItem *parent)
    self._noteCreation(QQuickTreeViewDelegate, lambda: Rituals.call(
        'ritual_ZN22QQuickTreeViewDelegateC1EP10QQuickItem',
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

  def indicatorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::indicatorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#indicatorChanged
    """
    #  void QQuickTreeViewDelegate::indicatorChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickTreeViewDelegate16indicatorChangedEv',
    )

  def indentationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::indentationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#indentationChanged
    """
    #  void QQuickTreeViewDelegate::indentationChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickTreeViewDelegate18indentationChangedEv',
    )

  def isTreeNodeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::isTreeNodeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#isTreeNodeChanged
    """
    #  void QQuickTreeViewDelegate::isTreeNodeChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickTreeViewDelegate17isTreeNodeChangedEv',
    )

  def hasChildrenChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::hasChildrenChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#hasChildrenChanged
    """
    #  void QQuickTreeViewDelegate::hasChildrenChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickTreeViewDelegate18hasChildrenChangedEv',
    )

  def expandedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::expandedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#expandedChanged
    """
    #  void QQuickTreeViewDelegate::expandedChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickTreeViewDelegate15expandedChangedEv',
    )

  def depthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::depthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#depthChanged
    """
    #  void QQuickTreeViewDelegate::depthChanged()
    self.uglySide.call('ritual_ZN22QQuickTreeViewDelegate12depthChangedEv')

  def treeviewChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::treeviewChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#treeviewChanged
    """
    #  void QQuickTreeViewDelegate::treeviewChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickTreeViewDelegate15treeviewChangedEv',
    )

  def leftMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::leftMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#leftMarginChanged
    """
    #  void QQuickTreeViewDelegate::leftMarginChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickTreeViewDelegate17leftMarginChangedEv',
    )

  def rightMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::rightMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#rightMarginChanged
    """
    #  void QQuickTreeViewDelegate::rightMarginChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickTreeViewDelegate18rightMarginChangedEv',
    )

  def currentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::currentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#currentChanged
    """
    #  void QQuickTreeViewDelegate::currentChanged()
    self.uglySide.call('ritual_ZN22QQuickTreeViewDelegate14currentChangedEv')

  def selectedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::selectedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#selectedChanged
    """
    #  void QQuickTreeViewDelegate::selectedChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickTreeViewDelegate15selectedChangedEv',
    )

  def editingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::editingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#editingChanged
    """
    #  void QQuickTreeViewDelegate::editingChanged()
    self.uglySide.call('ritual_ZN22QQuickTreeViewDelegate14editingChangedEv')

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickTreeViewDelegate::geometryChange(const QRectF &newGeometry,
    #      const QRectF &oldGeometry)
    ritual = 'ritual_ZN22QQuickTreeViewDelegate14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTreeViewDelegate14geometryChangeERK6QRectFS'
          '2_')
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#componentComplete
    """
    #  void QQuickTreeViewDelegate::componentComplete()
    ritual = 'ritual_ZN22QQuickTreeViewDelegate17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickTreeViewDelegate17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTreeViewDelegate::mousePressEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewdelegate.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTreeViewDelegate::mousePressEvent(QMouseEvent *event)
    ritual = (
        'ritual_ZN22QQuickTreeViewDelegate15mousePressEventEP11QMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTreeViewDelegate15mousePressEventEP11QMouse'
          'Event')
    self.uglySide.call(ritual, self._addressOf(event))
