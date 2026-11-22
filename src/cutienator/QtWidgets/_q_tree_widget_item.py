"""
QTreeWidgetItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qtreewidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize, QVariant
  from ..QtGui import QBrush, QFont, QIcon
  from . import QTreeWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QFont = WAIT['QFont']
  QIcon = WAIT['QIcon']
  QSize = WAIT['QSize']
  QTreeWidget = WAIT['QTreeWidget']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTreeWidgetItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTreeWidgetItem: a plain Python object standing in
  front of one C++ QTreeWidgetItem.

  C++ hands a QTreeWidgetItem around as a copy, so every C++ QTreeWidgetItem
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTreeWidgetItem that has a ritual and that Python
  can call so far, 55 names in all: 'clone', 'treeWidget', 'setSelected',
  'isSelected', 'setHidden', 'isHidden', 'setExpanded', 'isExpanded',
  'setFirstColumnSpanned', 'isFirstColumnSpanned', 'setDisabled',
  'isDisabled', 'setChildIndicatorPolicy', 'childIndicatorPolicy', 'flags',
  'setFlags', 'text', 'setText', 'icon', 'setIcon', 'statusTip',
  'setStatusTip', 'toolTip', 'setToolTip', 'whatsThis', 'setWhatsThis',
  'font', 'setFont', 'textAlignment', 'setTextAlignment', 'background',
  'setBackground', 'foreground', 'setForeground', 'checkState',
  'setCheckState', 'sizeHint', 'setSizeHint', 'data', 'setData', '__lt__',
  'parent', 'child', 'childCount', 'columnCount', 'indexOfChild', 'addChild',
  'insertChild', 'removeChild', 'takeChild', 'addChildren', 'insertChildren',
  'takeChildren', 'type', 'sortChildren'. It can be made from Python, in 8
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTreeWidgetItem::QTreeWidgetItem(const QTreeWidgetItem &other)':
    takes in Python what 'QTreeWidgetItem::QTreeWidgetItem(QTreeWidgetItem
    *parent, int type)' takes.
  - Qt's 'QTreeWidgetItem::~QTreeWidgetItem()': the destructor: Python
    removes its C++ QTreeWidgetItem by it, and has no other use for it.
  - Qt's 'void QTreeWidgetItem::setTextAlignment(int column, Qt::Alignment
    alignment)': takes in Python what 'void
    QTreeWidgetItem::setTextAlignment(int column, Qt::AlignmentFlag
    alignment)' takes.

  What has no ritual
  ------------------

  9 of the 76 functions Qt declares: 5 private; 3 takes or gives a type that
  cannot be passed yet; 1 protected.

  What to expect
  --------------

  - The C++ QTreeWidgetItem is created at the first use, not by
    'QTreeWidgetItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTreeWidgetItem back gives a copy the ritual made for
    Python, in a new cute QTreeWidgetItem.
  """

  #  The enums Qt writes inside QTreeWidgetItem, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ChildIndicatorPolicy(CuteNum):
    """
    The enum 'QTreeWidgetItem::ChildIndicatorPolicy' of Qt, with the 3 names
    Qt gives in it.
    """

    ShowIndicator = Kee[int](0)
    DontShowIndicator = Kee[int](1)
    DontShowIndicatorWhenChildless = Kee[int](2)

  class ItemType(CuteNum):
    """
    The enum 'QTreeWidgetItem::ItemType' of Qt, with the 2 names Qt gives in
    it.
    """

    Type = Kee[int](0)
    UserType = Kee[int](1000)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTreeWidgetItem'

  #  A C++ QTreeWidgetItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTreeWidgetItem'

  #  The functions Qt calls itself that QTreeWidgetItem is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'read': (
          'void QTreeWidgetItem::read(QDataStream &)',
      ),
      'write': (
          'void QTreeWidgetItem::write(QDataStream &) const',
      ),
  }

  #  The functions Qt calls itself that QTreeWidgetItem is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'clone': (
          ('_ZNK15QTreeWidgetItem5cloneEv',
           ('address', 'address', 'QtWidgets:QTreeWidgetItem'),
           ()),
      ),
      'data': (
          ('_ZNK15QTreeWidgetItem4dataEii',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'setData': (
          ('_ZN15QTreeWidgetItem7setDataEiiRK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
  }

  #  Qt's '~QTreeWidgetItem()'. Naming it makes this a value class: Python
  #  owns every C++ QTreeWidgetItem behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QTreeWidgetItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidgetItem::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#clone

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidgetItem::clone() const
    ritual = 'ritual_ZNK15QTreeWidgetItem5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QTreeWidgetItem5cloneEv'
    address = self.uglySide.call(ritual)
    return QTreeWidgetItem._cuteAt(address)

  def treeWidget(self) -> Optional[QTreeWidget]:
    """
    Calls Qt's 'QTreeWidget *QTreeWidgetItem::treeWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#treeWidget

    Returns
    -------

    Optional[QTreeWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidget *QTreeWidgetItem::treeWidget() const
    address = self.uglySide.call('ritual_ZNK15QTreeWidgetItem10treeWidgetEv')
    from . import QTreeWidget
    return QTreeWidget._cuteAt(address)

  def isSelected(self) -> bool:
    """
    Calls Qt's 'bool QTreeWidgetItem::isSelected() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#isSelected
    """
    #  bool QTreeWidgetItem::isSelected() const
    return self.uglySide.call('ritual_ZNK15QTreeWidgetItem10isSelectedEv')

  def isHidden(self) -> bool:
    """
    Calls Qt's 'bool QTreeWidgetItem::isHidden() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#isHidden
    """
    #  bool QTreeWidgetItem::isHidden() const
    return self.uglySide.call('ritual_ZNK15QTreeWidgetItem8isHiddenEv')

  def isExpanded(self) -> bool:
    """
    Calls Qt's 'bool QTreeWidgetItem::isExpanded() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#isExpanded
    """
    #  bool QTreeWidgetItem::isExpanded() const
    return self.uglySide.call('ritual_ZNK15QTreeWidgetItem10isExpandedEv')

  def isFirstColumnSpanned(self) -> bool:
    """
    Calls Qt's 'bool QTreeWidgetItem::isFirstColumnSpanned() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitem.html#isFirstColumnSpanned
    """
    #  bool QTreeWidgetItem::isFirstColumnSpanned() const
    return self.uglySide.call(
        'ritual_ZNK15QTreeWidgetItem20isFirstColumnSpannedEv',
    )

  def isDisabled(self) -> bool:
    """
    Calls Qt's 'bool QTreeWidgetItem::isDisabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#isDisabled
    """
    #  bool QTreeWidgetItem::isDisabled() const
    return self.uglySide.call('ritual_ZNK15QTreeWidgetItem10isDisabledEv')

  def childIndicatorPolicy(self) -> ChildIndicatorPolicy:
    """
    Calls Qt's 'QTreeWidgetItem::ChildIndicatorPolicy
    QTreeWidgetItem::childIndicatorPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitem.html#childIndicatorPolicy

    Returns
    -------

    ChildIndicatorPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'ChildIndicatorPolicy(number)' gives.
    """
    #  QTreeWidgetItem::ChildIndicatorPolicy
    #      QTreeWidgetItem::childIndicatorPolicy() const
    return QTreeWidgetItem.ChildIndicatorPolicy(self.uglySide.call(
        'ritual_ZNK15QTreeWidgetItem20childIndicatorPolicyEv',
    ))

  def flags(self) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QTreeWidgetItem::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#flags

    Returns
    -------

    Qt.ItemFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::ItemFlags QTreeWidgetItem::flags() const
    return Qt.ItemFlags(self.uglySide.call(
        'ritual_ZNK15QTreeWidgetItem5flagsEv',
    ))

  @overload(int)
  def text(self, column: int) -> str:
    """
    Calls Qt's 'QString QTreeWidgetItem::text(int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#text

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTreeWidgetItem::text(int column) const
    return self.uglySide.call('ritual_ZNK15QTreeWidgetItem4textEi', column)

  @overload(int)
  def icon(self, column: int) -> QIcon:
    """
    Calls Qt's 'QIcon QTreeWidgetItem::icon(int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#icon

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QTreeWidgetItem::icon(int column) const
    address = self.uglySide.call(
        'ritual_ZNK15QTreeWidgetItem4iconEi', column,
    )
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  @overload(int)
  def statusTip(self, column: int) -> str:
    """
    Calls Qt's 'QString QTreeWidgetItem::statusTip(int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#statusTip

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTreeWidgetItem::statusTip(int column) const
    return self.uglySide.call(
        'ritual_ZNK15QTreeWidgetItem9statusTipEi', column,
    )

  @overload(int)
  def toolTip(self, column: int) -> str:
    """
    Calls Qt's 'QString QTreeWidgetItem::toolTip(int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#toolTip

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTreeWidgetItem::toolTip(int column) const
    return self.uglySide.call(
        'ritual_ZNK15QTreeWidgetItem7toolTipEi', column,
    )

  @overload(int)
  def whatsThis(self, column: int) -> str:
    """
    Calls Qt's 'QString QTreeWidgetItem::whatsThis(int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#whatsThis

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTreeWidgetItem::whatsThis(int column) const
    return self.uglySide.call(
        'ritual_ZNK15QTreeWidgetItem9whatsThisEi', column,
    )

  @overload(int)
  def font(self, column: int) -> QFont:
    """
    Calls Qt's 'QFont QTreeWidgetItem::font(int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#font

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QTreeWidgetItem::font(int column) const
    address = self.uglySide.call(
        'ritual_ZNK15QTreeWidgetItem4fontEi', column,
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  @overload(int)
  def textAlignment(self, column: int) -> int:
    """
    Calls Qt's 'int QTreeWidgetItem::textAlignment(int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#textAlignment

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  int QTreeWidgetItem::textAlignment(int column) const
    return self.uglySide.call(
        'ritual_ZNK15QTreeWidgetItem13textAlignmentEi', column,
    )

  @overload(int)
  def background(self, column: int) -> QBrush:
    """
    Calls Qt's 'QBrush QTreeWidgetItem::background(int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#background

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QTreeWidgetItem::background(int column) const
    address = self.uglySide.call(
        'ritual_ZNK15QTreeWidgetItem10backgroundEi', column,
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  @overload(int)
  def foreground(self, column: int) -> QBrush:
    """
    Calls Qt's 'QBrush QTreeWidgetItem::foreground(int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#foreground

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QTreeWidgetItem::foreground(int column) const
    address = self.uglySide.call(
        'ritual_ZNK15QTreeWidgetItem10foregroundEi', column,
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  @overload(int)
  def checkState(self, column: int) -> Qt.CheckState:
    """
    Calls Qt's 'Qt::CheckState QTreeWidgetItem::checkState(int column)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#checkState

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    Qt.CheckState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.CheckState(number)'
      gives.
    """
    #  Qt::CheckState QTreeWidgetItem::checkState(int column) const
    return Qt.CheckState(self.uglySide.call(
        'ritual_ZNK15QTreeWidgetItem10checkStateEi', column,
    ))

  @overload(int)
  def sizeHint(self, column: int) -> QSize:
    """
    Calls Qt's 'QSize QTreeWidgetItem::sizeHint(int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#sizeHint

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QTreeWidgetItem::sizeHint(int column) const
    address = self.uglySide.call(
        'ritual_ZNK15QTreeWidgetItem8sizeHintEi', column,
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(int, int)
  def data(self, column: int, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant QTreeWidgetItem::data(int column, int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#data

    Parameters
    ----------

    column : int
      Passed on as it is.

    role : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QTreeWidgetItem::data(int column, int role) const
    ritual = 'ritual_ZNK15QTreeWidgetItem4dataEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QTreeWidgetItem4dataEii'
    address = self.uglySide.call(ritual, column, role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def parent(self) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidgetItem::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#parent

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidgetItem::parent() const
    address = self.uglySide.call('ritual_ZNK15QTreeWidgetItem6parentEv')
    return QTreeWidgetItem._cuteAt(address)

  @overload(int)
  def child(self, index: int) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidgetItem::child(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#child

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidgetItem::child(int index) const
    address = self.uglySide.call(
        'ritual_ZNK15QTreeWidgetItem5childEi', index,
    )
    return QTreeWidgetItem._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QTreeWidgetItem::childCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#childCount
    """
    #  int QTreeWidgetItem::childCount() const
    return self.uglySide.call('ritual_ZNK15QTreeWidgetItem10childCountEv')

  def columnCount(self) -> int:
    """
    Calls Qt's 'int QTreeWidgetItem::columnCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#columnCount
    """
    #  int QTreeWidgetItem::columnCount() const
    return self.uglySide.call('ritual_ZNK15QTreeWidgetItem11columnCountEv')

  @overload(THIS)
  @overload(NoneType)
  def indexOfChild(self, child: Optional[QTreeWidgetItem]) -> int:
    """
    Calls Qt's 'int QTreeWidgetItem::indexOfChild(QTreeWidgetItem *child)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#indexOfChild

    Parameters
    ----------

    child : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QTreeWidgetItem::indexOfChild(QTreeWidgetItem *child) const
    return self.uglySide.call(
        'ritual_ZNK15QTreeWidgetItem12indexOfChildEPS_',
        self._addressOf(child),
    )

  def type(self) -> int:
    """
    Calls Qt's 'int QTreeWidgetItem::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#type
    """
    #  int QTreeWidgetItem::type() const
    return self.uglySide.call('ritual_ZNK15QTreeWidgetItem4typeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setSelected(self, select: bool) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::setSelected(bool select)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#setSelected

    Parameters
    ----------

    select : bool
      Passed on as it is.
    """
    #  void QTreeWidgetItem::setSelected(bool select)
    self.uglySide.call('ritual_ZN15QTreeWidgetItem11setSelectedEb', select)

  @overload(bool)
  def setHidden(self, hide: bool) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::setHidden(bool hide)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#setHidden

    Parameters
    ----------

    hide : bool
      Passed on as it is.
    """
    #  void QTreeWidgetItem::setHidden(bool hide)
    self.uglySide.call('ritual_ZN15QTreeWidgetItem9setHiddenEb', hide)

  @overload(bool)
  def setExpanded(self, expand: bool) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::setExpanded(bool expand)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#setExpanded

    Parameters
    ----------

    expand : bool
      Passed on as it is.
    """
    #  void QTreeWidgetItem::setExpanded(bool expand)
    self.uglySide.call('ritual_ZN15QTreeWidgetItem11setExpandedEb', expand)

  @overload(bool)
  def setFirstColumnSpanned(self, span: bool) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::setFirstColumnSpanned(bool span)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitem.html#setFirstColumnSpanned

    Parameters
    ----------

    span : bool
      Passed on as it is.
    """
    #  void QTreeWidgetItem::setFirstColumnSpanned(bool span)
    self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem21setFirstColumnSpannedEb', span,
    )

  @overload(bool)
  def setDisabled(self, disabled: bool) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::setDisabled(bool disabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#setDisabled

    Parameters
    ----------

    disabled : bool
      Passed on as it is.
    """
    #  void QTreeWidgetItem::setDisabled(bool disabled)
    self.uglySide.call('ritual_ZN15QTreeWidgetItem11setDisabledEb', disabled)

  @overload(ChildIndicatorPolicy)
  def setChildIndicatorPolicy(self, policy: ChildIndicatorPolicy) -> None:
    """
    Calls Qt's 'void
    QTreeWidgetItem::setChildIndicatorPolicy(QTreeWidgetItem::
    ChildIndicatorPolicy policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitem.html#setChildIndicatorPolicy

    Parameters
    ----------

    policy : ChildIndicatorPolicy
      Passed on as its number.
    """
    #  void QTreeWidgetItem::setChildIndicatorPolicy(QTreeWidgetItem::
    #      ChildIndicatorPolicy policy)
    self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem23setChildIndicatorPolicyENS_20ChildIndi'
        'catorPolicyE',
        policy.value,
    )

  @overload(Qt.ItemFlags)
  def setFlags(self, flags: Qt.ItemFlags) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::setFlags(Qt::ItemFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#setFlags

    Parameters
    ----------

    flags : Qt.ItemFlags
      Passed on as its number.
    """
    #  void QTreeWidgetItem::setFlags(Qt::ItemFlags flags)
    self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem8setFlagsE6QFlagsIN2Qt8ItemFlagEE',
        flags.value,
    )

  @overload(int, str)
  def setText(self, column: int, text: str) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::setText(int column, const QString
    &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#setText

    Parameters
    ----------

    column : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTreeWidgetItem::setText(int column, const QString &text)
    self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem7setTextEiRK7QString', column, text,
    )

  @overload(int, QIcon)
  def setIcon(self, column: int, icon: QIcon) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::setIcon(int column, const QIcon
    &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#setIcon

    Parameters
    ----------

    column : int
      Passed on as it is.

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QTreeWidgetItem::setIcon(int column, const QIcon &icon)
    self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem7setIconEiRK5QIcon',
        column, self._valueOf(icon),
    )

  @overload(int, str)
  def setStatusTip(self, column: int, statusTip: str) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::setStatusTip(int column, const QString
    &statusTip)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#setStatusTip

    Parameters
    ----------

    column : int
      Passed on as it is.

    statusTip : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTreeWidgetItem::setStatusTip(int column, const QString
    #      &statusTip)
    self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem12setStatusTipEiRK7QString',
        column, statusTip,
    )

  @overload(int, str)
  def setToolTip(self, column: int, toolTip: str) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::setToolTip(int column, const QString
    &toolTip)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#setToolTip

    Parameters
    ----------

    column : int
      Passed on as it is.

    toolTip : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTreeWidgetItem::setToolTip(int column, const QString &toolTip)
    self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem10setToolTipEiRK7QString',
        column, toolTip,
    )

  @overload(int, str)
  def setWhatsThis(self, column: int, whatsThis: str) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::setWhatsThis(int column, const QString
    &whatsThis)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#setWhatsThis

    Parameters
    ----------

    column : int
      Passed on as it is.

    whatsThis : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTreeWidgetItem::setWhatsThis(int column, const QString
    #      &whatsThis)
    self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem12setWhatsThisEiRK7QString',
        column, whatsThis,
    )

  @overload(int, QFont)
  def setFont(self, column: int, font: QFont) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::setFont(int column, const QFont
    &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#setFont

    Parameters
    ----------

    column : int
      Passed on as it is.

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QTreeWidgetItem::setFont(int column, const QFont &font)
    self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem7setFontEiRK5QFont',
        column, self._valueOf(font),
    )

  @overload(int, int)
  def setTextAlignment(self, column: int, alignment: int) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::setTextAlignment(int column, int
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitem.html#setTextAlignment

    Parameters
    ----------

    column : int
      Passed on as it is.

    alignment : int
      Passed on as it is.
    """
    #  void QTreeWidgetItem::setTextAlignment(int column, int alignment)
    self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem16setTextAlignmentEii', column, alignment,
    )

  @overload(int, Qt.AlignmentFlag)
  def setTextAlignment(
      self,
      column: int,
      alignment: Qt.AlignmentFlag,
  ) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::setTextAlignment(int column,
    Qt::AlignmentFlag alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitem.html#setTextAlignment

    Parameters
    ----------

    column : int
      Passed on as it is.

    alignment : Qt.AlignmentFlag
      Passed on as its number.
    """
    #  void QTreeWidgetItem::setTextAlignment(int column, Qt::AlignmentFlag
    #      alignment)
    self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem16setTextAlignmentEiN2Qt13AlignmentFlagE',
        column, alignment.value,
    )

  @overload(int, QBrush)
  def setBackground(self, column: int, brush: QBrush) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::setBackground(int column, const QBrush
    &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#setBackground

    Parameters
    ----------

    column : int
      Passed on as it is.

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QTreeWidgetItem::setBackground(int column, const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem13setBackgroundEiRK6QBrush',
        column, self._valueOf(brush),
    )

  @overload(int, QBrush)
  def setForeground(self, column: int, brush: QBrush) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::setForeground(int column, const QBrush
    &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#setForeground

    Parameters
    ----------

    column : int
      Passed on as it is.

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QTreeWidgetItem::setForeground(int column, const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem13setForegroundEiRK6QBrush',
        column, self._valueOf(brush),
    )

  @overload(int, Qt.CheckState)
  def setCheckState(self, column: int, state: Qt.CheckState) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::setCheckState(int column,
    Qt::CheckState state)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#setCheckState

    Parameters
    ----------

    column : int
      Passed on as it is.

    state : Qt.CheckState
      Passed on as its number.
    """
    #  void QTreeWidgetItem::setCheckState(int column, Qt::CheckState state)
    self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem13setCheckStateEiN2Qt10CheckStateE',
        column, state.value,
    )

  @overload(int, QSize)
  def setSizeHint(self, column: int, size: QSize) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::setSizeHint(int column, const QSize
    &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#setSizeHint

    Parameters
    ----------

    column : int
      Passed on as it is.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QTreeWidgetItem::setSizeHint(int column, const QSize &size)
    self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem11setSizeHintEiRK5QSize',
        column, self._valueOf(size),
    )

  @overload(int, int, QVariant)
  def setData(self, column: int, role: int, value: QVariant) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::setData(int column, int role, const
    QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#setData

    Parameters
    ----------

    column : int
      Passed on as it is.

    role : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QTreeWidgetItem::setData(int column, int role, const QVariant
    #      &value)
    ritual = 'ritual_ZN15QTreeWidgetItem7setDataEiiRK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QTreeWidgetItem7setDataEiiRK8QVariant'
    self.uglySide.call(ritual, column, role, self._valueOf(value))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __lt__(self, other: QTreeWidgetItem) -> bool:
    """
    Calls Qt's 'bool QTreeWidgetItem::operator<(const QTreeWidgetItem &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#operator<

    Parameters
    ----------

    other : QTreeWidgetItem
      Passed on as a value: Qt reads the C++ QTreeWidgetItem, which stays
      Python's own.
    """
    #  bool QTreeWidgetItem::operator<(const QTreeWidgetItem &other) const
    return self.uglySide.call(
        'ritual_ZNK15QTreeWidgetItemltERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
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
  @overload(int)
  def __init__(self, type: int = 0) -> None:
    """
    Notes what was given, for Qt's 'QTreeWidgetItem::QTreeWidgetItem(int
    type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitem.html#QTreeWidgetItem

    Parameters
    ----------

    type : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QTreeWidgetItem::QTreeWidgetItem(int type)
    self._noteCreation(QTreeWidgetItem, lambda: Rituals.call(
        'ritual_ZN15QTreeWidgetItemC1Ei', type,
    ))

  @overload(QStringList)
  @overload(QStringList, int)
  def __init__(self, strings: QStringList, type: int = 0) -> None:
    """
    Notes what was given, for Qt's 'QTreeWidgetItem::QTreeWidgetItem(const
    QStringList &strings, int type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitem.html#QTreeWidgetItem

    Parameters
    ----------

    strings : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    type : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QTreeWidgetItem::QTreeWidgetItem(const QStringList &strings, int type)
    self._noteCreation(QTreeWidgetItem, lambda: Rituals.call(
        'ritual_ZN15QTreeWidgetItemC1ERK5QListI7QStringEi',
        self._valueOf(strings), type,
    ))

  @overload(QTreeWidget)
  @overload(NoneType)
  @overload(QTreeWidget, int)
  @overload(NoneType, int)
  def __init__(self, treeview: Optional[QTreeWidget], type: int = 0) -> None:
    """
    Notes what was given, for Qt's
    'QTreeWidgetItem::QTreeWidgetItem(QTreeWidget *treeview, int type)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitem.html#QTreeWidgetItem

    Parameters
    ----------

    treeview : Optional[QTreeWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QTreeWidgetItem::QTreeWidgetItem(QTreeWidget *treeview, int type)
    self._noteCreation(QTreeWidgetItem, lambda: Rituals.call(
        'ritual_ZN15QTreeWidgetItemC1EP11QTreeWidgeti',
        self._addressOf(treeview), type,
    ))

  @overload(QTreeWidget, QStringList)
  @overload(NoneType, QStringList)
  @overload(QTreeWidget, QStringList, int)
  @overload(NoneType, QStringList, int)
  def __init__(
      self,
      treeview: Optional[QTreeWidget],
      strings: QStringList,
      type: int = 0,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QTreeWidgetItem::QTreeWidgetItem(QTreeWidget *treeview, const
    QStringList &strings, int type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitem.html#QTreeWidgetItem

    Parameters
    ----------

    treeview : Optional[QTreeWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    strings : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    type : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QTreeWidgetItem::QTreeWidgetItem(QTreeWidget *treeview, const
    #      QStringList &strings, int type)
    self._noteCreation(QTreeWidgetItem, lambda: Rituals.call(
        'ritual_ZN15QTreeWidgetItemC1EP11QTreeWidgetRK5QListI7QStringEi',
        self._addressOf(treeview), self._valueOf(strings), type,
    ))

  @overload(QTreeWidget, THIS)
  @overload(QTreeWidget, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  @overload(QTreeWidget, THIS, int)
  @overload(QTreeWidget, NoneType, int)
  @overload(NoneType, THIS, int)
  @overload(NoneType, NoneType, int)
  def __init__(
      self,
      treeview: Optional[QTreeWidget],
      after: Optional[QTreeWidgetItem],
      type: int = 0,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QTreeWidgetItem::QTreeWidgetItem(QTreeWidget *treeview, QTreeWidgetItem
    *after, int type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitem.html#QTreeWidgetItem

    Parameters
    ----------

    treeview : Optional[QTreeWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    after : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QTreeWidgetItem::QTreeWidgetItem(QTreeWidget *treeview,
    #      QTreeWidgetItem *after, int type)
    self._noteCreation(QTreeWidgetItem, lambda: Rituals.call(
        'ritual_ZN15QTreeWidgetItemC1EP11QTreeWidgetPS_i',
        self._addressOf(treeview), self._addressOf(after), type,
    ))

  @overload(THIS)
  @overload(THIS, int)
  def __init__(
      self,
      parent: Optional[QTreeWidgetItem],
      type: int = 0,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QTreeWidgetItem::QTreeWidgetItem(QTreeWidgetItem *parent, int type)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitem.html#QTreeWidgetItem

    Parameters
    ----------

    parent : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QTreeWidgetItem::QTreeWidgetItem(QTreeWidgetItem *parent, int type)
    self._noteCreation(QTreeWidgetItem, lambda: Rituals.call(
        'ritual_ZN15QTreeWidgetItemC1EPS_i', self._addressOf(parent), type,
    ))

  @overload(THIS, QStringList)
  @overload(THIS, QStringList, int)
  def __init__(
      self,
      parent: Optional[QTreeWidgetItem],
      strings: QStringList,
      type: int = 0,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QTreeWidgetItem::QTreeWidgetItem(QTreeWidgetItem *parent, const
    QStringList &strings, int type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitem.html#QTreeWidgetItem

    Parameters
    ----------

    parent : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    strings : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    type : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QTreeWidgetItem::QTreeWidgetItem(QTreeWidgetItem *parent, const
    #      QStringList &strings, int type)
    self._noteCreation(QTreeWidgetItem, lambda: Rituals.call(
        'ritual_ZN15QTreeWidgetItemC1EPS_RK5QListI7QStringEi',
        self._addressOf(parent), self._valueOf(strings), type,
    ))

  @overload(THIS, THIS)
  @overload(THIS, NoneType)
  @overload(THIS, THIS, int)
  @overload(THIS, NoneType, int)
  def __init__(
      self,
      parent: Optional[QTreeWidgetItem],
      after: Optional[QTreeWidgetItem],
      type: int = 0,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QTreeWidgetItem::QTreeWidgetItem(QTreeWidgetItem *parent,
    QTreeWidgetItem *after, int type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitem.html#QTreeWidgetItem

    Parameters
    ----------

    parent : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    after : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QTreeWidgetItem::QTreeWidgetItem(QTreeWidgetItem *parent,
    #      QTreeWidgetItem *after, int type)
    self._noteCreation(QTreeWidgetItem, lambda: Rituals.call(
        'ritual_ZN15QTreeWidgetItemC1EPS_S0_i',
        self._addressOf(parent), self._addressOf(after), type,
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

  @overload(THIS)
  @overload(NoneType)
  def addChild(self, child: Optional[QTreeWidgetItem]) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::addChild(QTreeWidgetItem *child)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#addChild

    Parameters
    ----------

    child : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTreeWidgetItem::addChild(QTreeWidgetItem *child)
    self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem8addChildEPS_', self._addressOf(child),
    )

  @overload(int, THIS)
  @overload(int, NoneType)
  def insertChild(
      self,
      index: int,
      child: Optional[QTreeWidgetItem],
  ) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::insertChild(int index, QTreeWidgetItem
    *child)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#insertChild

    Parameters
    ----------

    index : int
      Passed on as it is.

    child : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTreeWidgetItem::insertChild(int index, QTreeWidgetItem *child)
    self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem11insertChildEiPS_',
        index, self._addressOf(child),
    )

  @overload(THIS)
  @overload(NoneType)
  def removeChild(self, child: Optional[QTreeWidgetItem]) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::removeChild(QTreeWidgetItem *child)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#removeChild

    Parameters
    ----------

    child : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTreeWidgetItem::removeChild(QTreeWidgetItem *child)
    self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem11removeChildEPS_',
        self._addressOf(child),
    )

  @overload(int)
  def takeChild(self, index: int) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidgetItem::takeChild(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#takeChild

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidgetItem::takeChild(int index)
    address = self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem9takeChildEi', index,
    )
    return QTreeWidgetItem._cuteAt(address)

  @overload(QList[WAIT['QTreeWidgetItem']])
  def addChildren(self, children: QList[QTreeWidgetItem]) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::addChildren(const QList<QTreeWidgetItem
    *> &children)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#addChildren

    Parameters
    ----------

    children : QList[QTreeWidgetItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QTreeWidgetItem::addChildren(const QList<QTreeWidgetItem *>
    #      &children)
    self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem11addChildrenERK5QListIPS_E',
        self._valueOf(children),
    )

  @overload(int, QList[WAIT['QTreeWidgetItem']])
  def insertChildren(
      self,
      index: int,
      children: QList[QTreeWidgetItem],
  ) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::insertChildren(int index, const
    QList<QTreeWidgetItem *> &children)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitem.html#insertChildren

    Parameters
    ----------

    index : int
      Passed on as it is.

    children : QList[QTreeWidgetItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QTreeWidgetItem::insertChildren(int index, const
    #      QList<QTreeWidgetItem *> &children)
    self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem14insertChildrenEiRK5QListIPS_E',
        index, self._valueOf(children),
    )

  def takeChildren(self) -> QList[QTreeWidgetItem]:
    """
    Calls Qt's 'QList<QTreeWidgetItem *> QTreeWidgetItem::takeChildren()'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#takeChildren

    Returns
    -------

    QList[QTreeWidgetItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QTreeWidgetItem *> QTreeWidgetItem::takeChildren()
    address = self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem12takeChildrenEv',
    )
    return QList[QTreeWidgetItem]._cuteOwning(address)

  @overload(int, Qt.SortOrder)
  def sortChildren(self, column: int, order: Qt.SortOrder) -> None:
    """
    Calls Qt's 'void QTreeWidgetItem::sortChildren(int column, Qt::SortOrder
    order)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidgetitem.html#sortChildren

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number.
    """
    #  void QTreeWidgetItem::sortChildren(int column, Qt::SortOrder order)
    self.uglySide.call(
        'ritual_ZN15QTreeWidgetItem12sortChildrenEiN2Qt9SortOrderE',
        column, order.value,
    )


#  Qt's 'QList<QTreeWidgetItem *>': the list of QTreeWidgetItem, which
#  'QList[QTreeWidgetItem]' gives. It is made here, so that there is one as
#  soon as there can be a QTreeWidgetItem.
QList.createKind(
    QTreeWidgetItem, 'address',
    make='ritual_list_make_QTreeWidgetItem_ptr',
    add='ritual_list_add_QTreeWidgetItem_ptr',
    size='ritual_list_size_QTreeWidgetItem_ptr',
    at='ritual_list_at_QTreeWidgetItem_ptr',
    drop='ritual_list_drop_QTreeWidgetItem_ptr',
)
