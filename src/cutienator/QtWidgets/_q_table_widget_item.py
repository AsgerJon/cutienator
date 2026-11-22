"""
QTableWidgetItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qtablewidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize, QVariant
  from ..QtGui import QBrush, QFont, QIcon
  from . import QTableWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QFont = WAIT['QFont']
  QIcon = WAIT['QIcon']
  QSize = WAIT['QSize']
  QVariant = WAIT['QVariant']


class QTableWidgetItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTableWidgetItem: a plain Python object standing in
  front of one C++ QTableWidgetItem.

  C++ hands a QTableWidgetItem around as a copy, so every C++
  QTableWidgetItem behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTableWidgetItem that has a ritual and that Python
  can call so far, 34 names in all: 'clone', 'tableWidget', 'row', 'column',
  'setSelected', 'isSelected', 'flags', 'setFlags', 'text', 'setText',
  'icon', 'setIcon', 'statusTip', 'setStatusTip', 'toolTip', 'setToolTip',
  'whatsThis', 'setWhatsThis', 'font', 'setFont', 'textAlignment',
  'setTextAlignment', 'background', 'setBackground', 'foreground',
  'setForeground', 'checkState', 'setCheckState', 'sizeHint', 'setSizeHint',
  'data', 'setData', '__lt__', 'type'. It can be made from Python, in 4 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTableWidgetItem::~QTableWidgetItem()': the destructor: Python
    removes its C++ QTableWidgetItem by it, and has no other use for it.
  - Qt's 'void QTableWidgetItem::setTextAlignment(Qt::Alignment alignment)':
    takes in Python what 'void
    QTableWidgetItem::setTextAlignment(Qt::AlignmentFlag alignment)' takes.

  What has no ritual
  ------------------

  4 of the 45 functions Qt declares: 3 takes or gives a type that cannot be
  passed yet; 1 private.

  What to expect
  --------------

  - The C++ QTableWidgetItem is created at the first use, not by
    'QTableWidgetItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTableWidgetItem back gives a copy the ritual made
    for Python, in a new cute QTableWidgetItem.
  """

  #  The enums Qt writes inside QTableWidgetItem, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ItemType(CuteNum):
    """
    The enum 'QTableWidgetItem::ItemType' of Qt, with the 2 names Qt gives in
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
  __qt_class__ = 'QTableWidgetItem'

  #  Qt's '~QTableWidgetItem()'. Naming it makes this a value class: Python
  #  owns every C++ QTableWidgetItem behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QTableWidgetItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QTableWidgetItem]:
    """
    Calls Qt's 'QTableWidgetItem *QTableWidgetItem::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#clone

    Returns
    -------

    Optional[QTableWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidgetItem *QTableWidgetItem::clone() const
    address = self.uglySide.call('ritual_ZNK16QTableWidgetItem5cloneEv')
    return QTableWidgetItem._cuteAt(address)

  def tableWidget(self) -> Optional[QTableWidget]:
    """
    Calls Qt's 'QTableWidget *QTableWidgetItem::tableWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#tableWidget

    Returns
    -------

    Optional[QTableWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidget *QTableWidgetItem::tableWidget() const
    address = self.uglySide.call(
        'ritual_ZNK16QTableWidgetItem11tableWidgetEv',
    )
    from . import QTableWidget
    return QTableWidget._cuteAt(address)

  def row(self) -> int:
    """
    Calls Qt's 'int QTableWidgetItem::row() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#row
    """
    #  int QTableWidgetItem::row() const
    return self.uglySide.call('ritual_ZNK16QTableWidgetItem3rowEv')

  def column(self) -> int:
    """
    Calls Qt's 'int QTableWidgetItem::column() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#column
    """
    #  int QTableWidgetItem::column() const
    return self.uglySide.call('ritual_ZNK16QTableWidgetItem6columnEv')

  def isSelected(self) -> bool:
    """
    Calls Qt's 'bool QTableWidgetItem::isSelected() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#isSelected
    """
    #  bool QTableWidgetItem::isSelected() const
    return self.uglySide.call('ritual_ZNK16QTableWidgetItem10isSelectedEv')

  def flags(self) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QTableWidgetItem::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#flags

    Returns
    -------

    Qt.ItemFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::ItemFlags QTableWidgetItem::flags() const
    return Qt.ItemFlags(self.uglySide.call(
        'ritual_ZNK16QTableWidgetItem5flagsEv',
    ))

  def text(self) -> str:
    """
    Calls Qt's 'QString QTableWidgetItem::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTableWidgetItem::text() const
    return self.uglySide.call('ritual_ZNK16QTableWidgetItem4textEv')

  def icon(self) -> QIcon:
    """
    Calls Qt's 'QIcon QTableWidgetItem::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#icon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QTableWidgetItem::icon() const
    address = self.uglySide.call('ritual_ZNK16QTableWidgetItem4iconEv')
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  def statusTip(self) -> str:
    """
    Calls Qt's 'QString QTableWidgetItem::statusTip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#statusTip

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTableWidgetItem::statusTip() const
    return self.uglySide.call('ritual_ZNK16QTableWidgetItem9statusTipEv')

  def toolTip(self) -> str:
    """
    Calls Qt's 'QString QTableWidgetItem::toolTip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#toolTip

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTableWidgetItem::toolTip() const
    return self.uglySide.call('ritual_ZNK16QTableWidgetItem7toolTipEv')

  def whatsThis(self) -> str:
    """
    Calls Qt's 'QString QTableWidgetItem::whatsThis() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#whatsThis

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTableWidgetItem::whatsThis() const
    return self.uglySide.call('ritual_ZNK16QTableWidgetItem9whatsThisEv')

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QTableWidgetItem::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QTableWidgetItem::font() const
    address = self.uglySide.call('ritual_ZNK16QTableWidgetItem4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def textAlignment(self) -> int:
    """
    Calls Qt's 'int QTableWidgetItem::textAlignment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidgetitem.html#textAlignment
    """
    #  int QTableWidgetItem::textAlignment() const
    return self.uglySide.call(
        'ritual_ZNK16QTableWidgetItem13textAlignmentEv',
    )

  def background(self) -> QBrush:
    """
    Calls Qt's 'QBrush QTableWidgetItem::background() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#background

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QTableWidgetItem::background() const
    address = self.uglySide.call(
        'ritual_ZNK16QTableWidgetItem10backgroundEv',
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def foreground(self) -> QBrush:
    """
    Calls Qt's 'QBrush QTableWidgetItem::foreground() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#foreground

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QTableWidgetItem::foreground() const
    address = self.uglySide.call(
        'ritual_ZNK16QTableWidgetItem10foregroundEv',
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def checkState(self) -> Qt.CheckState:
    """
    Calls Qt's 'Qt::CheckState QTableWidgetItem::checkState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#checkState

    Returns
    -------

    Qt.CheckState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.CheckState(number)'
      gives.
    """
    #  Qt::CheckState QTableWidgetItem::checkState() const
    return Qt.CheckState(self.uglySide.call(
        'ritual_ZNK16QTableWidgetItem10checkStateEv',
    ))

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QTableWidgetItem::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QTableWidgetItem::sizeHint() const
    address = self.uglySide.call('ritual_ZNK16QTableWidgetItem8sizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(int)
  def data(self, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant QTableWidgetItem::data(int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#data

    Parameters
    ----------

    role : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QTableWidgetItem::data(int role) const
    address = self.uglySide.call('ritual_ZNK16QTableWidgetItem4dataEi', role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def type(self) -> int:
    """
    Calls Qt's 'int QTableWidgetItem::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#type
    """
    #  int QTableWidgetItem::type() const
    return self.uglySide.call('ritual_ZNK16QTableWidgetItem4typeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setSelected(self, select: bool) -> None:
    """
    Calls Qt's 'void QTableWidgetItem::setSelected(bool select)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#setSelected

    Parameters
    ----------

    select : bool
      Passed on as it is.
    """
    #  void QTableWidgetItem::setSelected(bool select)
    self.uglySide.call('ritual_ZN16QTableWidgetItem11setSelectedEb', select)

  @overload(Qt.ItemFlags)
  def setFlags(self, flags: Qt.ItemFlags) -> None:
    """
    Calls Qt's 'void QTableWidgetItem::setFlags(Qt::ItemFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#setFlags

    Parameters
    ----------

    flags : Qt.ItemFlags
      Passed on as its number.
    """
    #  void QTableWidgetItem::setFlags(Qt::ItemFlags flags)
    self.uglySide.call(
        'ritual_ZN16QTableWidgetItem8setFlagsE6QFlagsIN2Qt8ItemFlagEE',
        flags.value,
    )

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QTableWidgetItem::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTableWidgetItem::setText(const QString &text)
    self.uglySide.call(
        'ritual_ZN16QTableWidgetItem7setTextERK7QString', text,
    )

  @overload(QIcon)
  def setIcon(self, icon: QIcon) -> None:
    """
    Calls Qt's 'void QTableWidgetItem::setIcon(const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#setIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QTableWidgetItem::setIcon(const QIcon &icon)
    self.uglySide.call(
        'ritual_ZN16QTableWidgetItem7setIconERK5QIcon', self._valueOf(icon),
    )

  @overload(str)
  def setStatusTip(self, statusTip: str) -> None:
    """
    Calls Qt's 'void QTableWidgetItem::setStatusTip(const QString
    &statusTip)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#setStatusTip

    Parameters
    ----------

    statusTip : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTableWidgetItem::setStatusTip(const QString &statusTip)
    self.uglySide.call(
        'ritual_ZN16QTableWidgetItem12setStatusTipERK7QString', statusTip,
    )

  @overload(str)
  def setToolTip(self, toolTip: str) -> None:
    """
    Calls Qt's 'void QTableWidgetItem::setToolTip(const QString &toolTip)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#setToolTip

    Parameters
    ----------

    toolTip : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTableWidgetItem::setToolTip(const QString &toolTip)
    self.uglySide.call(
        'ritual_ZN16QTableWidgetItem10setToolTipERK7QString', toolTip,
    )

  @overload(str)
  def setWhatsThis(self, whatsThis: str) -> None:
    """
    Calls Qt's 'void QTableWidgetItem::setWhatsThis(const QString
    &whatsThis)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#setWhatsThis

    Parameters
    ----------

    whatsThis : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTableWidgetItem::setWhatsThis(const QString &whatsThis)
    self.uglySide.call(
        'ritual_ZN16QTableWidgetItem12setWhatsThisERK7QString', whatsThis,
    )

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QTableWidgetItem::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QTableWidgetItem::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN16QTableWidgetItem7setFontERK5QFont', self._valueOf(font),
    )

  @overload(int)
  def setTextAlignment(self, alignment: int) -> None:
    """
    Calls Qt's 'void QTableWidgetItem::setTextAlignment(int alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidgetitem.html#setTextAlignment

    Parameters
    ----------

    alignment : int
      Passed on as it is.
    """
    #  void QTableWidgetItem::setTextAlignment(int alignment)
    self.uglySide.call(
        'ritual_ZN16QTableWidgetItem16setTextAlignmentEi', alignment,
    )

  @overload(Qt.AlignmentFlag)
  def setTextAlignment(self, alignment: Qt.AlignmentFlag) -> None:
    """
    Calls Qt's 'void QTableWidgetItem::setTextAlignment(Qt::AlignmentFlag
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidgetitem.html#setTextAlignment

    Parameters
    ----------

    alignment : Qt.AlignmentFlag
      Passed on as its number.
    """
    #  void QTableWidgetItem::setTextAlignment(Qt::AlignmentFlag alignment)
    self.uglySide.call(
        'ritual_ZN16QTableWidgetItem16setTextAlignmentEN2Qt13AlignmentFlagE',
        alignment.value,
    )

  @overload(QBrush)
  def setBackground(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QTableWidgetItem::setBackground(const QBrush &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidgetitem.html#setBackground

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QTableWidgetItem::setBackground(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN16QTableWidgetItem13setBackgroundERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QBrush)
  def setForeground(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QTableWidgetItem::setForeground(const QBrush &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidgetitem.html#setForeground

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QTableWidgetItem::setForeground(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN16QTableWidgetItem13setForegroundERK6QBrush',
        self._valueOf(brush),
    )

  @overload(Qt.CheckState)
  def setCheckState(self, state: Qt.CheckState) -> None:
    """
    Calls Qt's 'void QTableWidgetItem::setCheckState(Qt::CheckState state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidgetitem.html#setCheckState

    Parameters
    ----------

    state : Qt.CheckState
      Passed on as its number.
    """
    #  void QTableWidgetItem::setCheckState(Qt::CheckState state)
    self.uglySide.call(
        'ritual_ZN16QTableWidgetItem13setCheckStateEN2Qt10CheckStateE',
        state.value,
    )

  @overload(QSize)
  def setSizeHint(self, size: QSize) -> None:
    """
    Calls Qt's 'void QTableWidgetItem::setSizeHint(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#setSizeHint

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QTableWidgetItem::setSizeHint(const QSize &size)
    self.uglySide.call(
        'ritual_ZN16QTableWidgetItem11setSizeHintERK5QSize',
        self._valueOf(size),
    )

  @overload(int, QVariant)
  def setData(self, role: int, value: QVariant) -> None:
    """
    Calls Qt's 'void QTableWidgetItem::setData(int role, const QVariant
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#setData

    Parameters
    ----------

    role : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QTableWidgetItem::setData(int role, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN16QTableWidgetItem7setDataEiRK8QVariant',
        role, self._valueOf(value),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __lt__(self, other: QTableWidgetItem) -> bool:
    """
    Calls Qt's 'bool QTableWidgetItem::operator<(const QTableWidgetItem
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablewidgetitem.html#operator<

    Parameters
    ----------

    other : QTableWidgetItem
      Passed on as a value: Qt reads the C++ QTableWidgetItem, which stays
      Python's own.
    """
    #  bool QTableWidgetItem::operator<(const QTableWidgetItem &other) const
    return self.uglySide.call(
        'ritual_ZNK16QTableWidgetItemltERKS_', self._valueOf(other),
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
    Notes what was given, for Qt's 'QTableWidgetItem::QTableWidgetItem(int
    type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidgetitem.html#QTableWidgetItem

    Parameters
    ----------

    type : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QTableWidgetItem::QTableWidgetItem(int type)
    self._noteCreation(QTableWidgetItem, lambda: Rituals.call(
        'ritual_ZN16QTableWidgetItemC1Ei', type,
    ))

  @overload(str)
  @overload(str, int)
  def __init__(self, text: str, type: int = 0) -> None:
    """
    Notes what was given, for Qt's 'QTableWidgetItem::QTableWidgetItem(const
    QString &text, int type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidgetitem.html#QTableWidgetItem

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    type : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QTableWidgetItem::QTableWidgetItem(const QString &text, int type)
    self._noteCreation(QTableWidgetItem, lambda: Rituals.call(
        'ritual_ZN16QTableWidgetItemC1ERK7QStringi', text, type,
    ))

  @overload(QIcon, str)
  @overload(QIcon, str, int)
  def __init__(self, icon: QIcon, text: str, type: int = 0) -> None:
    """
    Notes what was given, for Qt's 'QTableWidgetItem::QTableWidgetItem(const
    QIcon &icon, const QString &text, int type)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidgetitem.html#QTableWidgetItem

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    type : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QTableWidgetItem::QTableWidgetItem(const QIcon &icon, const QString
    #      &text, int type)
    self._noteCreation(QTableWidgetItem, lambda: Rituals.call(
        'ritual_ZN16QTableWidgetItemC1ERK5QIconRK7QStringi',
        self._valueOf(icon), text, type,
    ))

  @overload(THIS)
  def __init__(self, other: QTableWidgetItem) -> None:
    """
    Notes what was given, for Qt's 'QTableWidgetItem::QTableWidgetItem(const
    QTableWidgetItem &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablewidgetitem.html#QTableWidgetItem

    Parameters
    ----------

    other : QTableWidgetItem
      Passed on as a value: Qt reads the C++ QTableWidgetItem, which stays
      Python's own.
    """
    #  QTableWidgetItem::QTableWidgetItem(const QTableWidgetItem &other)
    self._noteCreation(QTableWidgetItem, lambda: Rituals.call(
        'ritual_ZN16QTableWidgetItemC1ERKS_', self._valueOf(other),
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
