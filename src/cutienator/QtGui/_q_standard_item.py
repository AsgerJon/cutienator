"""
QStandardItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qstandarditemmodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QModelIndex, QModelRoleDataSpan, QSize, QVariant
  from . import QBrush, QFont, QIcon, QStandardItemModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QFont = WAIT['QFont']
  QIcon = WAIT['QIcon']
  QModelRoleDataSpan = WAIT['QModelRoleDataSpan']
  QSize = WAIT['QSize']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStandardItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QStandardItem: a plain Python object standing in
  front of one C++ QStandardItem.

  What exists
  -----------

  Every function of Qt's QStandardItem that has a ritual and that Python can
  call so far, 77 names in all: 'data', 'multiData', 'setData', 'clearData',
  'text', 'setText', 'icon', 'setIcon', 'toolTip', 'setToolTip', 'statusTip',
  'setStatusTip', 'whatsThis', 'setWhatsThis', 'sizeHint', 'setSizeHint',
  'font', 'setFont', 'textAlignment', 'setTextAlignment', 'background',
  'setBackground', 'foreground', 'setForeground', 'checkState',
  'setCheckState', 'accessibleText', 'setAccessibleText',
  'accessibleDescription', 'setAccessibleDescription', 'flags', 'setFlags',
  'isEnabled', 'setEnabled', 'isEditable', 'setEditable', 'isSelectable',
  'setSelectable', 'isCheckable', 'setCheckable', 'isAutoTristate',
  'setAutoTristate', 'isUserTristate', 'setUserTristate', 'isDragEnabled',
  'setDragEnabled', 'isDropEnabled', 'setDropEnabled', 'parent', 'row',
  'column', 'index', 'model', 'rowCount', 'setRowCount', 'columnCount',
  'setColumnCount', 'hasChildren', 'child', 'setChild', 'insertRow',
  'insertColumn', 'insertRows', 'insertColumns', 'removeRow', 'removeColumn',
  'removeRows', 'removeColumns', 'appendRow', 'appendRows', 'appendColumn',
  'takeChild', 'takeRow', 'takeColumn', 'sortChildren', 'clone', 'type'. It
  can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStandardItem::~QStandardItem()': the destructor: Python never
    removes a C++ QStandardItem.

  What has no ritual
  ------------------

  9 of the 95 functions Qt declares: 4 protected; 3 takes or gives a type
  that cannot be passed yet; 2 private.

  What to expect
  --------------

  - The C++ QStandardItem is created at the first use, not by
    'QStandardItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStandardItem.
  """

  #  The enums Qt writes inside QStandardItem, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ItemType(CuteNum):
    """
    The enum 'QStandardItem::ItemType' of Qt, with the 2 names Qt gives in
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
  __qt_class__ = 'QStandardItem'

  #  A C++ QStandardItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QStandardItem'

  #  The functions Qt calls itself that QStandardItem is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'read': (
          'void QStandardItem::read(QDataStream &)',
      ),
      'write': (
          'void QStandardItem::write(QDataStream &) const',
      ),
  }

  #  The functions Qt calls itself that QStandardItem is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'data': (
          ('_ZNK13QStandardItem4dataEi',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'number', ''),
           )),
      ),
      'multiData': (
          ('_ZNK13QStandardItem9multiDataE18QModelRoleDataSpan',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelRoleDataSpan'),
           )),
      ),
      'setData': (
          ('_ZN13QStandardItem7setDataERK8QVarianti',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QVariant'),
               ('int', 'number', ''),
           )),
      ),
      'clone': (
          ('_ZNK13QStandardItem5cloneEv',
           ('address', 'address', 'QtGui:QStandardItem'),
           ()),
      ),
      'type': (
          ('_ZNK13QStandardItem4typeEv',
           ('int', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(int)
  def data(self, role: int = 257) -> QVariant:
    """
    Calls Qt's 'QVariant QStandardItem::data(int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#data

    Parameters
    ----------

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 257.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QStandardItem::data(int role) const
    ritual = 'ritual_ZNK13QStandardItem4dataEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QStandardItem4dataEi'
    address = self.uglySide.call(ritual, role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QStandardItem::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStandardItem::text() const
    return self.uglySide.call('ritual_ZNK13QStandardItem4textEv')

  def icon(self) -> QIcon:
    """
    Calls Qt's 'QIcon QStandardItem::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#icon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QStandardItem::icon() const
    address = self.uglySide.call('ritual_ZNK13QStandardItem4iconEv')
    from . import QIcon
    return QIcon._cuteOwning(address)

  def toolTip(self) -> str:
    """
    Calls Qt's 'QString QStandardItem::toolTip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#toolTip

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStandardItem::toolTip() const
    return self.uglySide.call('ritual_ZNK13QStandardItem7toolTipEv')

  def statusTip(self) -> str:
    """
    Calls Qt's 'QString QStandardItem::statusTip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#statusTip

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStandardItem::statusTip() const
    return self.uglySide.call('ritual_ZNK13QStandardItem9statusTipEv')

  def whatsThis(self) -> str:
    """
    Calls Qt's 'QString QStandardItem::whatsThis() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#whatsThis

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStandardItem::whatsThis() const
    return self.uglySide.call('ritual_ZNK13QStandardItem9whatsThisEv')

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QStandardItem::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QStandardItem::sizeHint() const
    address = self.uglySide.call('ritual_ZNK13QStandardItem8sizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QStandardItem::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QStandardItem::font() const
    address = self.uglySide.call('ritual_ZNK13QStandardItem4fontEv')
    from . import QFont
    return QFont._cuteOwning(address)

  def textAlignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QStandardItem::textAlignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#textAlignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QStandardItem::textAlignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK13QStandardItem13textAlignmentEv',
    ))

  def background(self) -> QBrush:
    """
    Calls Qt's 'QBrush QStandardItem::background() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#background

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QStandardItem::background() const
    address = self.uglySide.call('ritual_ZNK13QStandardItem10backgroundEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def foreground(self) -> QBrush:
    """
    Calls Qt's 'QBrush QStandardItem::foreground() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#foreground

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QStandardItem::foreground() const
    address = self.uglySide.call('ritual_ZNK13QStandardItem10foregroundEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def checkState(self) -> Qt.CheckState:
    """
    Calls Qt's 'Qt::CheckState QStandardItem::checkState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#checkState

    Returns
    -------

    Qt.CheckState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.CheckState(number)'
      gives.
    """
    #  Qt::CheckState QStandardItem::checkState() const
    return Qt.CheckState(self.uglySide.call(
        'ritual_ZNK13QStandardItem10checkStateEv',
    ))

  def accessibleText(self) -> str:
    """
    Calls Qt's 'QString QStandardItem::accessibleText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#accessibleText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStandardItem::accessibleText() const
    return self.uglySide.call('ritual_ZNK13QStandardItem14accessibleTextEv')

  def accessibleDescription(self) -> str:
    """
    Calls Qt's 'QString QStandardItem::accessibleDescription() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditem.html#accessibleDescription

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStandardItem::accessibleDescription() const
    return self.uglySide.call(
        'ritual_ZNK13QStandardItem21accessibleDescriptionEv',
    )

  def flags(self) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QStandardItem::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#flags

    Returns
    -------

    Qt.ItemFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::ItemFlags QStandardItem::flags() const
    return Qt.ItemFlags(self.uglySide.call(
        'ritual_ZNK13QStandardItem5flagsEv',
    ))

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QStandardItem::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#isEnabled
    """
    #  bool QStandardItem::isEnabled() const
    return self.uglySide.call('ritual_ZNK13QStandardItem9isEnabledEv')

  def isEditable(self) -> bool:
    """
    Calls Qt's 'bool QStandardItem::isEditable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#isEditable
    """
    #  bool QStandardItem::isEditable() const
    return self.uglySide.call('ritual_ZNK13QStandardItem10isEditableEv')

  def isSelectable(self) -> bool:
    """
    Calls Qt's 'bool QStandardItem::isSelectable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#isSelectable
    """
    #  bool QStandardItem::isSelectable() const
    return self.uglySide.call('ritual_ZNK13QStandardItem12isSelectableEv')

  def isCheckable(self) -> bool:
    """
    Calls Qt's 'bool QStandardItem::isCheckable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#isCheckable
    """
    #  bool QStandardItem::isCheckable() const
    return self.uglySide.call('ritual_ZNK13QStandardItem11isCheckableEv')

  def isAutoTristate(self) -> bool:
    """
    Calls Qt's 'bool QStandardItem::isAutoTristate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#isAutoTristate
    """
    #  bool QStandardItem::isAutoTristate() const
    return self.uglySide.call('ritual_ZNK13QStandardItem14isAutoTristateEv')

  def isUserTristate(self) -> bool:
    """
    Calls Qt's 'bool QStandardItem::isUserTristate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#isUserTristate
    """
    #  bool QStandardItem::isUserTristate() const
    return self.uglySide.call('ritual_ZNK13QStandardItem14isUserTristateEv')

  def isDragEnabled(self) -> bool:
    """
    Calls Qt's 'bool QStandardItem::isDragEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#isDragEnabled
    """
    #  bool QStandardItem::isDragEnabled() const
    return self.uglySide.call('ritual_ZNK13QStandardItem13isDragEnabledEv')

  def isDropEnabled(self) -> bool:
    """
    Calls Qt's 'bool QStandardItem::isDropEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#isDropEnabled
    """
    #  bool QStandardItem::isDropEnabled() const
    return self.uglySide.call('ritual_ZNK13QStandardItem13isDropEnabledEv')

  def parent(self) -> Optional[QStandardItem]:
    """
    Calls Qt's 'QStandardItem *QStandardItem::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#parent

    Returns
    -------

    Optional[QStandardItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStandardItem *QStandardItem::parent() const
    address = self.uglySide.call('ritual_ZNK13QStandardItem6parentEv')
    return QStandardItem._cuteAt(address)

  def row(self) -> int:
    """
    Calls Qt's 'int QStandardItem::row() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#row
    """
    #  int QStandardItem::row() const
    return self.uglySide.call('ritual_ZNK13QStandardItem3rowEv')

  def column(self) -> int:
    """
    Calls Qt's 'int QStandardItem::column() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#column
    """
    #  int QStandardItem::column() const
    return self.uglySide.call('ritual_ZNK13QStandardItem6columnEv')

  def index(self) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QStandardItem::index() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#index

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QStandardItem::index() const
    address = self.uglySide.call('ritual_ZNK13QStandardItem5indexEv')
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  def model(self) -> Optional[QStandardItemModel]:
    """
    Calls Qt's 'QStandardItemModel *QStandardItem::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#model

    Returns
    -------

    Optional[QStandardItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStandardItemModel *QStandardItem::model() const
    address = self.uglySide.call('ritual_ZNK13QStandardItem5modelEv')
    from . import QStandardItemModel
    return QStandardItemModel._cuteAt(address)

  def rowCount(self) -> int:
    """
    Calls Qt's 'int QStandardItem::rowCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#rowCount
    """
    #  int QStandardItem::rowCount() const
    return self.uglySide.call('ritual_ZNK13QStandardItem8rowCountEv')

  def columnCount(self) -> int:
    """
    Calls Qt's 'int QStandardItem::columnCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#columnCount
    """
    #  int QStandardItem::columnCount() const
    return self.uglySide.call('ritual_ZNK13QStandardItem11columnCountEv')

  def hasChildren(self) -> bool:
    """
    Calls Qt's 'bool QStandardItem::hasChildren() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#hasChildren
    """
    #  bool QStandardItem::hasChildren() const
    return self.uglySide.call('ritual_ZNK13QStandardItem11hasChildrenEv')

  @overload(int)
  @overload(int, int)
  def child(self, row: int, column: int = 0) -> Optional[QStandardItem]:
    """
    Calls Qt's 'QStandardItem *QStandardItem::child(int row, int column)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#child

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    Optional[QStandardItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStandardItem *QStandardItem::child(int row, int column) const
    address = self.uglySide.call(
        'ritual_ZNK13QStandardItem5childEii', row, column,
    )
    return QStandardItem._cuteAt(address)

  def clone(self) -> Optional[QStandardItem]:
    """
    Calls Qt's 'QStandardItem *QStandardItem::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#clone

    Returns
    -------

    Optional[QStandardItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStandardItem *QStandardItem::clone() const
    ritual = 'ritual_ZNK13QStandardItem5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QStandardItem5cloneEv'
    address = self.uglySide.call(ritual)
    return QStandardItem._cuteAt(address)

  def type(self) -> int:
    """
    Calls Qt's 'int QStandardItem::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#type
    """
    #  int QStandardItem::type() const
    ritual = 'ritual_ZNK13QStandardItem4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QStandardItem4typeEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  @overload(QVariant, int)
  def setData(self, value: QVariant, role: int = 257) -> None:
    """
    Calls Qt's 'void QStandardItem::setData(const QVariant &value, int
    role)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setData

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 257.
    """
    #  void QStandardItem::setData(const QVariant &value, int role)
    ritual = 'ritual_ZN13QStandardItem7setDataERK8QVarianti'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QStandardItem7setDataERK8QVarianti'
    self.uglySide.call(ritual, self._valueOf(value), role)

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QStandardItem::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QStandardItem::setText(const QString &text)
    self.uglySide.call('ritual_ZN13QStandardItem7setTextERK7QString', text)

  @overload(QIcon)
  def setIcon(self, icon: QIcon) -> None:
    """
    Calls Qt's 'void QStandardItem::setIcon(const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QStandardItem::setIcon(const QIcon &icon)
    self.uglySide.call(
        'ritual_ZN13QStandardItem7setIconERK5QIcon', self._valueOf(icon),
    )

  @overload(str)
  def setToolTip(self, toolTip: str) -> None:
    """
    Calls Qt's 'void QStandardItem::setToolTip(const QString &toolTip)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setToolTip

    Parameters
    ----------

    toolTip : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QStandardItem::setToolTip(const QString &toolTip)
    self.uglySide.call(
        'ritual_ZN13QStandardItem10setToolTipERK7QString', toolTip,
    )

  @overload(str)
  def setStatusTip(self, statusTip: str) -> None:
    """
    Calls Qt's 'void QStandardItem::setStatusTip(const QString &statusTip)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setStatusTip

    Parameters
    ----------

    statusTip : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QStandardItem::setStatusTip(const QString &statusTip)
    self.uglySide.call(
        'ritual_ZN13QStandardItem12setStatusTipERK7QString', statusTip,
    )

  @overload(str)
  def setWhatsThis(self, whatsThis: str) -> None:
    """
    Calls Qt's 'void QStandardItem::setWhatsThis(const QString &whatsThis)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setWhatsThis

    Parameters
    ----------

    whatsThis : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QStandardItem::setWhatsThis(const QString &whatsThis)
    self.uglySide.call(
        'ritual_ZN13QStandardItem12setWhatsThisERK7QString', whatsThis,
    )

  @overload(QSize)
  def setSizeHint(self, sizeHint: QSize) -> None:
    """
    Calls Qt's 'void QStandardItem::setSizeHint(const QSize &sizeHint)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setSizeHint

    Parameters
    ----------

    sizeHint : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QStandardItem::setSizeHint(const QSize &sizeHint)
    self.uglySide.call(
        'ritual_ZN13QStandardItem11setSizeHintERK5QSize',
        self._valueOf(sizeHint),
    )

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QStandardItem::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QStandardItem::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN13QStandardItem7setFontERK5QFont', self._valueOf(font),
    )

  @overload(Qt.Alignment)
  def setTextAlignment(self, textAlignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QStandardItem::setTextAlignment(Qt::Alignment
    textAlignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditem.html#setTextAlignment

    Parameters
    ----------

    textAlignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QStandardItem::setTextAlignment(Qt::Alignment textAlignment)
    self.uglySide.call(
        'ritual_ZN13QStandardItem16setTextAlignmentE6QFlagsIN2Qt13Alignment'
        'FlagEE',
        textAlignment.value,
    )

  @overload(QBrush)
  def setBackground(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QStandardItem::setBackground(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setBackground

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QStandardItem::setBackground(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN13QStandardItem13setBackgroundERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QBrush)
  def setForeground(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QStandardItem::setForeground(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setForeground

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QStandardItem::setForeground(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN13QStandardItem13setForegroundERK6QBrush',
        self._valueOf(brush),
    )

  @overload(Qt.CheckState)
  def setCheckState(self, checkState: Qt.CheckState) -> None:
    """
    Calls Qt's 'void QStandardItem::setCheckState(Qt::CheckState
    checkState)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setCheckState

    Parameters
    ----------

    checkState : Qt.CheckState
      Passed on as its number.
    """
    #  void QStandardItem::setCheckState(Qt::CheckState checkState)
    self.uglySide.call(
        'ritual_ZN13QStandardItem13setCheckStateEN2Qt10CheckStateE',
        checkState.value,
    )

  @overload(str)
  def setAccessibleText(self, accessibleText: str) -> None:
    """
    Calls Qt's 'void QStandardItem::setAccessibleText(const QString
    &accessibleText)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditem.html#setAccessibleText

    Parameters
    ----------

    accessibleText : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QStandardItem::setAccessibleText(const QString &accessibleText)
    self.uglySide.call(
        'ritual_ZN13QStandardItem17setAccessibleTextERK7QString',
        accessibleText,
    )

  @overload(str)
  def setAccessibleDescription(self, accessibleDescription: str) -> None:
    """
    Calls Qt's 'void QStandardItem::setAccessibleDescription(const QString
    &accessibleDescription)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditem.html#setAccessibleDescription

    Parameters
    ----------

    accessibleDescription : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QStandardItem::setAccessibleDescription(const QString
    #      &accessibleDescription)
    self.uglySide.call(
        'ritual_ZN13QStandardItem24setAccessibleDescriptionERK7QString',
        accessibleDescription,
    )

  @overload(Qt.ItemFlags)
  def setFlags(self, flags: Qt.ItemFlags) -> None:
    """
    Calls Qt's 'void QStandardItem::setFlags(Qt::ItemFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setFlags

    Parameters
    ----------

    flags : Qt.ItemFlags
      Passed on as its number.
    """
    #  void QStandardItem::setFlags(Qt::ItemFlags flags)
    self.uglySide.call(
        'ritual_ZN13QStandardItem8setFlagsE6QFlagsIN2Qt8ItemFlagEE',
        flags.value,
    )

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QStandardItem::setEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QStandardItem::setEnabled(bool enabled)
    self.uglySide.call('ritual_ZN13QStandardItem10setEnabledEb', enabled)

  @overload(bool)
  def setEditable(self, editable: bool) -> None:
    """
    Calls Qt's 'void QStandardItem::setEditable(bool editable)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setEditable

    Parameters
    ----------

    editable : bool
      Passed on as it is.
    """
    #  void QStandardItem::setEditable(bool editable)
    self.uglySide.call('ritual_ZN13QStandardItem11setEditableEb', editable)

  @overload(bool)
  def setSelectable(self, selectable: bool) -> None:
    """
    Calls Qt's 'void QStandardItem::setSelectable(bool selectable)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setSelectable

    Parameters
    ----------

    selectable : bool
      Passed on as it is.
    """
    #  void QStandardItem::setSelectable(bool selectable)
    self.uglySide.call(
        'ritual_ZN13QStandardItem13setSelectableEb', selectable,
    )

  @overload(bool)
  def setCheckable(self, checkable: bool) -> None:
    """
    Calls Qt's 'void QStandardItem::setCheckable(bool checkable)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setCheckable

    Parameters
    ----------

    checkable : bool
      Passed on as it is.
    """
    #  void QStandardItem::setCheckable(bool checkable)
    self.uglySide.call('ritual_ZN13QStandardItem12setCheckableEb', checkable)

  @overload(bool)
  def setAutoTristate(self, tristate: bool) -> None:
    """
    Calls Qt's 'void QStandardItem::setAutoTristate(bool tristate)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setAutoTristate

    Parameters
    ----------

    tristate : bool
      Passed on as it is.
    """
    #  void QStandardItem::setAutoTristate(bool tristate)
    self.uglySide.call(
        'ritual_ZN13QStandardItem15setAutoTristateEb', tristate,
    )

  @overload(bool)
  def setUserTristate(self, tristate: bool) -> None:
    """
    Calls Qt's 'void QStandardItem::setUserTristate(bool tristate)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setUserTristate

    Parameters
    ----------

    tristate : bool
      Passed on as it is.
    """
    #  void QStandardItem::setUserTristate(bool tristate)
    self.uglySide.call(
        'ritual_ZN13QStandardItem15setUserTristateEb', tristate,
    )

  @overload(bool)
  def setDragEnabled(self, dragEnabled: bool) -> None:
    """
    Calls Qt's 'void QStandardItem::setDragEnabled(bool dragEnabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setDragEnabled

    Parameters
    ----------

    dragEnabled : bool
      Passed on as it is.
    """
    #  void QStandardItem::setDragEnabled(bool dragEnabled)
    self.uglySide.call(
        'ritual_ZN13QStandardItem14setDragEnabledEb', dragEnabled,
    )

  @overload(bool)
  def setDropEnabled(self, dropEnabled: bool) -> None:
    """
    Calls Qt's 'void QStandardItem::setDropEnabled(bool dropEnabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setDropEnabled

    Parameters
    ----------

    dropEnabled : bool
      Passed on as it is.
    """
    #  void QStandardItem::setDropEnabled(bool dropEnabled)
    self.uglySide.call(
        'ritual_ZN13QStandardItem14setDropEnabledEb', dropEnabled,
    )

  @overload(int)
  def setRowCount(self, rows: int) -> None:
    """
    Calls Qt's 'void QStandardItem::setRowCount(int rows)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setRowCount

    Parameters
    ----------

    rows : int
      Passed on as it is.
    """
    #  void QStandardItem::setRowCount(int rows)
    self.uglySide.call('ritual_ZN13QStandardItem11setRowCountEi', rows)

  @overload(int)
  def setColumnCount(self, columns: int) -> None:
    """
    Calls Qt's 'void QStandardItem::setColumnCount(int columns)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setColumnCount

    Parameters
    ----------

    columns : int
      Passed on as it is.
    """
    #  void QStandardItem::setColumnCount(int columns)
    self.uglySide.call('ritual_ZN13QStandardItem14setColumnCountEi', columns)

  @overload(int, int, THIS)
  @overload(int, int, NoneType)
  def setChild(
      self,
      row: int,
      column: int,
      item: Optional[QStandardItem],
  ) -> None:
    """
    Calls Qt's 'void QStandardItem::setChild(int row, int column,
    QStandardItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setChild

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    item : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStandardItem::setChild(int row, int column, QStandardItem *item)
    self.uglySide.call(
        'ritual_ZN13QStandardItem8setChildEiiPS_',
        row, column, self._addressOf(item),
    )

  @overload(int, THIS)
  @overload(int, NoneType)
  def setChild(self, row: int, item: Optional[QStandardItem]) -> None:
    """
    Calls Qt's 'void QStandardItem::setChild(int row, QStandardItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#setChild

    Parameters
    ----------

    row : int
      Passed on as it is.

    item : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStandardItem::setChild(int row, QStandardItem *item)
    self.uglySide.call(
        'ritual_ZN13QStandardItem8setChildEiPS_', row, self._addressOf(item),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QStandardItem::QStandardItem()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#QStandardItem
    """
    #  QStandardItem::QStandardItem()
    self._noteCreation(QStandardItem, lambda: Rituals.call(
        'ritual_ZN13QStandardItemC1Ev',
    ))

  @overload(str)
  def __init__(self, text: str) -> None:
    """
    Notes what was given, for Qt's 'QStandardItem::QStandardItem(const
    QString &text)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#QStandardItem

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QStandardItem::QStandardItem(const QString &text)
    self._noteCreation(QStandardItem, lambda: Rituals.call(
        'ritual_ZN13QStandardItemC1ERK7QString', text,
    ))

  @overload(QIcon, str)
  def __init__(self, icon: QIcon, text: str) -> None:
    """
    Notes what was given, for Qt's 'QStandardItem::QStandardItem(const QIcon
    &icon, const QString &text)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#QStandardItem

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QStandardItem::QStandardItem(const QIcon &icon, const QString &text)
    self._noteCreation(QStandardItem, lambda: Rituals.call(
        'ritual_ZN13QStandardItemC1ERK5QIconRK7QString',
        self._valueOf(icon), text,
    ))

  @overload(int)
  @overload(int, int)
  def __init__(self, rows: int, columns: int = 1) -> None:
    """
    Notes what was given, for Qt's 'QStandardItem::QStandardItem(int rows,
    int columns)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#QStandardItem

    Parameters
    ----------

    rows : int
      Passed on as it is.

    columns : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  QStandardItem::QStandardItem(int rows, int columns)
    self._noteCreation(QStandardItem, lambda: Rituals.call(
        'ritual_ZN13QStandardItemC1Eii', rows, columns,
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

  @overload(QModelRoleDataSpan)
  def multiData(self, roleDataSpan: QModelRoleDataSpan) -> None:
    """
    Calls Qt's 'void QStandardItem::multiData(QModelRoleDataSpan
    roleDataSpan) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#multiData

    Parameters
    ----------

    roleDataSpan : QModelRoleDataSpan
      Passed on as a value: Qt reads the C++ QModelRoleDataSpan, which stays
      Python's own.
    """
    #  void QStandardItem::multiData(QModelRoleDataSpan roleDataSpan) const
    ritual = 'ritual_ZNK13QStandardItem9multiDataE18QModelRoleDataSpan'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QStandardItem9multiDataE18QModelRoleDataSpan'
    self.uglySide.call(ritual, self._valueOf(roleDataSpan))

  def clearData(self) -> None:
    """
    Calls Qt's 'void QStandardItem::clearData()'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#clearData
    """
    #  void QStandardItem::clearData()
    self.uglySide.call('ritual_ZN13QStandardItem9clearDataEv')

  @overload(int, QList[WAIT['QStandardItem']])
  def insertRow(self, row: int, items: QList[QStandardItem]) -> None:
    """
    Calls Qt's 'void QStandardItem::insertRow(int row, const
    QList<QStandardItem *> &items)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#insertRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    items : QList[QStandardItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QStandardItem::insertRow(int row, const QList<QStandardItem *>
    #      &items)
    self.uglySide.call(
        'ritual_ZN13QStandardItem9insertRowEiRK5QListIPS_E',
        row, self._valueOf(items),
    )

  @overload(int, THIS)
  @overload(int, NoneType)
  def insertRow(self, row: int, item: Optional[QStandardItem]) -> None:
    """
    Calls Qt's 'void QStandardItem::insertRow(int row, QStandardItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#insertRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    item : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStandardItem::insertRow(int row, QStandardItem *item)
    self.uglySide.call(
        'ritual_ZN13QStandardItem9insertRowEiPS_',
        row, self._addressOf(item),
    )

  @overload(int, QList[WAIT['QStandardItem']])
  def insertColumn(self, column: int, items: QList[QStandardItem]) -> None:
    """
    Calls Qt's 'void QStandardItem::insertColumn(int column, const
    QList<QStandardItem *> &items)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#insertColumn

    Parameters
    ----------

    column : int
      Passed on as it is.

    items : QList[QStandardItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QStandardItem::insertColumn(int column, const QList<QStandardItem
    #      *> &items)
    self.uglySide.call(
        'ritual_ZN13QStandardItem12insertColumnEiRK5QListIPS_E',
        column, self._valueOf(items),
    )

  @overload(int, QList[WAIT['QStandardItem']])
  def insertRows(self, row: int, items: QList[QStandardItem]) -> None:
    """
    Calls Qt's 'void QStandardItem::insertRows(int row, const
    QList<QStandardItem *> &items)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#insertRows

    Parameters
    ----------

    row : int
      Passed on as it is.

    items : QList[QStandardItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QStandardItem::insertRows(int row, const QList<QStandardItem *>
    #      &items)
    self.uglySide.call(
        'ritual_ZN13QStandardItem10insertRowsEiRK5QListIPS_E',
        row, self._valueOf(items),
    )

  @overload(int, int)
  def insertRows(self, row: int, count: int) -> None:
    """
    Calls Qt's 'void QStandardItem::insertRows(int row, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#insertRows

    Parameters
    ----------

    row : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QStandardItem::insertRows(int row, int count)
    self.uglySide.call('ritual_ZN13QStandardItem10insertRowsEii', row, count)

  @overload(int, int)
  def insertColumns(self, column: int, count: int) -> None:
    """
    Calls Qt's 'void QStandardItem::insertColumns(int column, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#insertColumns

    Parameters
    ----------

    column : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QStandardItem::insertColumns(int column, int count)
    self.uglySide.call(
        'ritual_ZN13QStandardItem13insertColumnsEii', column, count,
    )

  @overload(int)
  def removeRow(self, row: int) -> None:
    """
    Calls Qt's 'void QStandardItem::removeRow(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#removeRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QStandardItem::removeRow(int row)
    self.uglySide.call('ritual_ZN13QStandardItem9removeRowEi', row)

  @overload(int)
  def removeColumn(self, column: int) -> None:
    """
    Calls Qt's 'void QStandardItem::removeColumn(int column)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#removeColumn

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  void QStandardItem::removeColumn(int column)
    self.uglySide.call('ritual_ZN13QStandardItem12removeColumnEi', column)

  @overload(int, int)
  def removeRows(self, row: int, count: int) -> None:
    """
    Calls Qt's 'void QStandardItem::removeRows(int row, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#removeRows

    Parameters
    ----------

    row : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QStandardItem::removeRows(int row, int count)
    self.uglySide.call('ritual_ZN13QStandardItem10removeRowsEii', row, count)

  @overload(int, int)
  def removeColumns(self, column: int, count: int) -> None:
    """
    Calls Qt's 'void QStandardItem::removeColumns(int column, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#removeColumns

    Parameters
    ----------

    column : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QStandardItem::removeColumns(int column, int count)
    self.uglySide.call(
        'ritual_ZN13QStandardItem13removeColumnsEii', column, count,
    )

  @overload(QList[WAIT['QStandardItem']])
  def appendRow(self, items: QList[QStandardItem]) -> None:
    """
    Calls Qt's 'void QStandardItem::appendRow(const QList<QStandardItem *>
    &items)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#appendRow

    Parameters
    ----------

    items : QList[QStandardItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QStandardItem::appendRow(const QList<QStandardItem *> &items)
    self.uglySide.call(
        'ritual_ZN13QStandardItem9appendRowERK5QListIPS_E',
        self._valueOf(items),
    )

  @overload(THIS)
  @overload(NoneType)
  def appendRow(self, item: Optional[QStandardItem]) -> None:
    """
    Calls Qt's 'void QStandardItem::appendRow(QStandardItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#appendRow

    Parameters
    ----------

    item : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStandardItem::appendRow(QStandardItem *item)
    self.uglySide.call(
        'ritual_ZN13QStandardItem9appendRowEPS_', self._addressOf(item),
    )

  @overload(QList[WAIT['QStandardItem']])
  def appendRows(self, items: QList[QStandardItem]) -> None:
    """
    Calls Qt's 'void QStandardItem::appendRows(const QList<QStandardItem *>
    &items)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#appendRows

    Parameters
    ----------

    items : QList[QStandardItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QStandardItem::appendRows(const QList<QStandardItem *> &items)
    self.uglySide.call(
        'ritual_ZN13QStandardItem10appendRowsERK5QListIPS_E',
        self._valueOf(items),
    )

  @overload(QList[WAIT['QStandardItem']])
  def appendColumn(self, items: QList[QStandardItem]) -> None:
    """
    Calls Qt's 'void QStandardItem::appendColumn(const QList<QStandardItem *>
    &items)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#appendColumn

    Parameters
    ----------

    items : QList[QStandardItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QStandardItem::appendColumn(const QList<QStandardItem *> &items)
    self.uglySide.call(
        'ritual_ZN13QStandardItem12appendColumnERK5QListIPS_E',
        self._valueOf(items),
    )

  @overload(int)
  @overload(int, int)
  def takeChild(self, row: int, column: int = 0) -> Optional[QStandardItem]:
    """
    Calls Qt's 'QStandardItem *QStandardItem::takeChild(int row, int
    column)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#takeChild

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    Optional[QStandardItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStandardItem *QStandardItem::takeChild(int row, int column)
    address = self.uglySide.call(
        'ritual_ZN13QStandardItem9takeChildEii', row, column,
    )
    return QStandardItem._cuteAt(address)

  @overload(int)
  def takeRow(self, row: int) -> QList[QStandardItem]:
    """
    Calls Qt's 'QList<QStandardItem *> QStandardItem::takeRow(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#takeRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    QList[QStandardItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QStandardItem *> QStandardItem::takeRow(int row)
    address = self.uglySide.call('ritual_ZN13QStandardItem7takeRowEi', row)
    return QList[QStandardItem]._cuteOwning(address)

  @overload(int)
  def takeColumn(self, column: int) -> QList[QStandardItem]:
    """
    Calls Qt's 'QList<QStandardItem *> QStandardItem::takeColumn(int
    column)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#takeColumn

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    QList[QStandardItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QStandardItem *> QStandardItem::takeColumn(int column)
    address = self.uglySide.call(
        'ritual_ZN13QStandardItem10takeColumnEi', column,
    )
    return QList[QStandardItem]._cuteOwning(address)

  @overload(int)
  @overload(int, Qt.SortOrder)
  def sortChildren(
      self,
      column: int,
      order: Qt.SortOrder = Qt.SortOrder.AscendingOrder,
  ) -> None:
    """
    Calls Qt's 'void QStandardItem::sortChildren(int column, Qt::SortOrder
    order)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditem.html#sortChildren

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SortOrder.AscendingOrder.
    """
    #  void QStandardItem::sortChildren(int column, Qt::SortOrder order)
    self.uglySide.call(
        'ritual_ZN13QStandardItem12sortChildrenEiN2Qt9SortOrderE',
        column, order.value,
    )


#  Qt's 'QList<QStandardItem *>': the list of QStandardItem, which
#  'QList[QStandardItem]' gives. It is made here, so that there is one as
#  soon as there can be a QStandardItem.
QList.createKind(
    QStandardItem, 'address',
    make='ritual_list_make_QStandardItem_ptr',
    add='ritual_list_add_QStandardItem_ptr',
    size='ritual_list_size_QStandardItem_ptr',
    at='ritual_list_at_QStandardItem_ptr',
    drop='ritual_list_drop_QStandardItem_ptr',
)
