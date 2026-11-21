"""
QListWidgetItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qlistwidget.h, Qt 6.12.0. Changes made here are lost.
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
  from . import QListWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QFont = WAIT['QFont']
  QIcon = WAIT['QIcon']
  QListWidget = WAIT['QListWidget']
  QSize = WAIT['QSize']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QListWidgetItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QListWidgetItem: a plain Python object standing in
  front of one C++ QListWidgetItem.

  C++ hands a QListWidgetItem around as a copy, so every C++ QListWidgetItem
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QListWidgetItem that has a ritual and that Python
  can call so far, 33 names in all: 'clone', 'listWidget', 'setSelected',
  'isSelected', 'setHidden', 'isHidden', 'flags', 'setFlags', 'text',
  'setText', 'icon', 'setIcon', 'statusTip', 'setStatusTip', 'toolTip',
  'setToolTip', 'whatsThis', 'setWhatsThis', 'font', 'setFont',
  'textAlignment', 'setTextAlignment', 'background', 'setBackground',
  'foreground', 'setForeground', 'checkState', 'setCheckState', 'sizeHint',
  'setSizeHint', 'data', 'setData', 'type'. It can be made from Python, in 4
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QListWidgetItem::~QListWidgetItem()': the destructor: Python
    removes its C++ QListWidgetItem by it, and has no other use for it.
  - Qt's 'void QListWidgetItem::setTextAlignment(Qt::Alignment alignment)':
    takes in Python what 'void
    QListWidgetItem::setTextAlignment(Qt::AlignmentFlag alignment)' takes.
  - Qt's 'bool QListWidgetItem::operator<(const QListWidgetItem &other)
    const': an operator, which is not reflected yet.

  What has no ritual
  ------------------

  4 of the 45 functions Qt declares: 3 takes or gives a type that cannot be
  passed yet; 1 private.

  What to expect
  --------------

  - The C++ QListWidgetItem is created at the first use, not by
    'QListWidgetItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QListWidgetItem back gives a copy the ritual made for
    Python, in a new cute QListWidgetItem.
  """

  #  The enums Qt writes inside QListWidgetItem, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ItemType(CuteNum):
    """
    The enum 'QListWidgetItem::ItemType' of Qt, with the 2 names Qt gives in
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
  __qt_class__ = 'QListWidgetItem'

  #  Qt's '~QListWidgetItem()'. Naming it makes this a value class: Python
  #  owns every C++ QListWidgetItem behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QListWidgetItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QListWidgetItem]:
    """
    Calls Qt's 'QListWidgetItem *QListWidgetItem::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#clone

    Returns
    -------

    Optional[QListWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QListWidgetItem *QListWidgetItem::clone() const
    address = self.uglySide.call('ritual_ZNK15QListWidgetItem5cloneEv')
    return QListWidgetItem._cuteAt(address)

  def listWidget(self) -> Optional[QListWidget]:
    """
    Calls Qt's 'QListWidget *QListWidgetItem::listWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#listWidget

    Returns
    -------

    Optional[QListWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QListWidget *QListWidgetItem::listWidget() const
    address = self.uglySide.call('ritual_ZNK15QListWidgetItem10listWidgetEv')
    from . import QListWidget
    return QListWidget._cuteAt(address)

  def isSelected(self) -> bool:
    """
    Calls Qt's 'bool QListWidgetItem::isSelected() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#isSelected
    """
    #  bool QListWidgetItem::isSelected() const
    return self.uglySide.call('ritual_ZNK15QListWidgetItem10isSelectedEv')

  def isHidden(self) -> bool:
    """
    Calls Qt's 'bool QListWidgetItem::isHidden() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#isHidden
    """
    #  bool QListWidgetItem::isHidden() const
    return self.uglySide.call('ritual_ZNK15QListWidgetItem8isHiddenEv')

  def flags(self) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QListWidgetItem::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#flags

    Returns
    -------

    Qt.ItemFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::ItemFlags QListWidgetItem::flags() const
    return Qt.ItemFlags(self.uglySide.call(
        'ritual_ZNK15QListWidgetItem5flagsEv',
    ))

  def text(self) -> str:
    """
    Calls Qt's 'QString QListWidgetItem::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QListWidgetItem::text() const
    return self.uglySide.call('ritual_ZNK15QListWidgetItem4textEv')

  def icon(self) -> QIcon:
    """
    Calls Qt's 'QIcon QListWidgetItem::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#icon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QListWidgetItem::icon() const
    address = self.uglySide.call('ritual_ZNK15QListWidgetItem4iconEv')
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  def statusTip(self) -> str:
    """
    Calls Qt's 'QString QListWidgetItem::statusTip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#statusTip

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QListWidgetItem::statusTip() const
    return self.uglySide.call('ritual_ZNK15QListWidgetItem9statusTipEv')

  def toolTip(self) -> str:
    """
    Calls Qt's 'QString QListWidgetItem::toolTip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#toolTip

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QListWidgetItem::toolTip() const
    return self.uglySide.call('ritual_ZNK15QListWidgetItem7toolTipEv')

  def whatsThis(self) -> str:
    """
    Calls Qt's 'QString QListWidgetItem::whatsThis() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#whatsThis

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QListWidgetItem::whatsThis() const
    return self.uglySide.call('ritual_ZNK15QListWidgetItem9whatsThisEv')

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QListWidgetItem::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QListWidgetItem::font() const
    address = self.uglySide.call('ritual_ZNK15QListWidgetItem4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def textAlignment(self) -> int:
    """
    Calls Qt's 'int QListWidgetItem::textAlignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#textAlignment
    """
    #  int QListWidgetItem::textAlignment() const
    return self.uglySide.call('ritual_ZNK15QListWidgetItem13textAlignmentEv')

  def background(self) -> QBrush:
    """
    Calls Qt's 'QBrush QListWidgetItem::background() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#background

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QListWidgetItem::background() const
    address = self.uglySide.call('ritual_ZNK15QListWidgetItem10backgroundEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def foreground(self) -> QBrush:
    """
    Calls Qt's 'QBrush QListWidgetItem::foreground() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#foreground

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QListWidgetItem::foreground() const
    address = self.uglySide.call('ritual_ZNK15QListWidgetItem10foregroundEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def checkState(self) -> Qt.CheckState:
    """
    Calls Qt's 'Qt::CheckState QListWidgetItem::checkState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#checkState

    Returns
    -------

    Qt.CheckState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.CheckState(number)'
      gives.
    """
    #  Qt::CheckState QListWidgetItem::checkState() const
    return Qt.CheckState(self.uglySide.call(
        'ritual_ZNK15QListWidgetItem10checkStateEv',
    ))

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QListWidgetItem::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QListWidgetItem::sizeHint() const
    address = self.uglySide.call('ritual_ZNK15QListWidgetItem8sizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(int)
  def data(self, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant QListWidgetItem::data(int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#data

    Parameters
    ----------

    role : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QListWidgetItem::data(int role) const
    address = self.uglySide.call('ritual_ZNK15QListWidgetItem4dataEi', role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def type(self) -> int:
    """
    Calls Qt's 'int QListWidgetItem::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#type
    """
    #  int QListWidgetItem::type() const
    return self.uglySide.call('ritual_ZNK15QListWidgetItem4typeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setSelected(self, select: bool) -> None:
    """
    Calls Qt's 'void QListWidgetItem::setSelected(bool select)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#setSelected

    Parameters
    ----------

    select : bool
      Passed on as it is.
    """
    #  void QListWidgetItem::setSelected(bool select)
    self.uglySide.call('ritual_ZN15QListWidgetItem11setSelectedEb', select)

  @overload(bool)
  def setHidden(self, hide: bool) -> None:
    """
    Calls Qt's 'void QListWidgetItem::setHidden(bool hide)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#setHidden

    Parameters
    ----------

    hide : bool
      Passed on as it is.
    """
    #  void QListWidgetItem::setHidden(bool hide)
    self.uglySide.call('ritual_ZN15QListWidgetItem9setHiddenEb', hide)

  @overload(Qt.ItemFlags)
  def setFlags(self, flags: Qt.ItemFlags) -> None:
    """
    Calls Qt's 'void QListWidgetItem::setFlags(Qt::ItemFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#setFlags

    Parameters
    ----------

    flags : Qt.ItemFlags
      Passed on as its number.
    """
    #  void QListWidgetItem::setFlags(Qt::ItemFlags flags)
    self.uglySide.call(
        'ritual_ZN15QListWidgetItem8setFlagsE6QFlagsIN2Qt8ItemFlagEE',
        flags.value,
    )

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QListWidgetItem::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QListWidgetItem::setText(const QString &text)
    self.uglySide.call('ritual_ZN15QListWidgetItem7setTextERK7QString', text)

  @overload(QIcon)
  def setIcon(self, icon: QIcon) -> None:
    """
    Calls Qt's 'void QListWidgetItem::setIcon(const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#setIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QListWidgetItem::setIcon(const QIcon &icon)
    self.uglySide.call(
        'ritual_ZN15QListWidgetItem7setIconERK5QIcon', self._valueOf(icon),
    )

  @overload(str)
  def setStatusTip(self, statusTip: str) -> None:
    """
    Calls Qt's 'void QListWidgetItem::setStatusTip(const QString
    &statusTip)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#setStatusTip

    Parameters
    ----------

    statusTip : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QListWidgetItem::setStatusTip(const QString &statusTip)
    self.uglySide.call(
        'ritual_ZN15QListWidgetItem12setStatusTipERK7QString', statusTip,
    )

  @overload(str)
  def setToolTip(self, toolTip: str) -> None:
    """
    Calls Qt's 'void QListWidgetItem::setToolTip(const QString &toolTip)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#setToolTip

    Parameters
    ----------

    toolTip : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QListWidgetItem::setToolTip(const QString &toolTip)
    self.uglySide.call(
        'ritual_ZN15QListWidgetItem10setToolTipERK7QString', toolTip,
    )

  @overload(str)
  def setWhatsThis(self, whatsThis: str) -> None:
    """
    Calls Qt's 'void QListWidgetItem::setWhatsThis(const QString
    &whatsThis)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#setWhatsThis

    Parameters
    ----------

    whatsThis : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QListWidgetItem::setWhatsThis(const QString &whatsThis)
    self.uglySide.call(
        'ritual_ZN15QListWidgetItem12setWhatsThisERK7QString', whatsThis,
    )

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QListWidgetItem::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QListWidgetItem::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN15QListWidgetItem7setFontERK5QFont', self._valueOf(font),
    )

  @overload(int)
  def setTextAlignment(self, alignment: int) -> None:
    """
    Calls Qt's 'void QListWidgetItem::setTextAlignment(int alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistwidgetitem.html#setTextAlignment

    Parameters
    ----------

    alignment : int
      Passed on as it is.
    """
    #  void QListWidgetItem::setTextAlignment(int alignment)
    self.uglySide.call(
        'ritual_ZN15QListWidgetItem16setTextAlignmentEi', alignment,
    )

  @overload(Qt.AlignmentFlag)
  def setTextAlignment(self, alignment: Qt.AlignmentFlag) -> None:
    """
    Calls Qt's 'void QListWidgetItem::setTextAlignment(Qt::AlignmentFlag
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistwidgetitem.html#setTextAlignment

    Parameters
    ----------

    alignment : Qt.AlignmentFlag
      Passed on as its number.
    """
    #  void QListWidgetItem::setTextAlignment(Qt::AlignmentFlag alignment)
    self.uglySide.call(
        'ritual_ZN15QListWidgetItem16setTextAlignmentEN2Qt13AlignmentFlagE',
        alignment.value,
    )

  @overload(QBrush)
  def setBackground(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QListWidgetItem::setBackground(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#setBackground

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QListWidgetItem::setBackground(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN15QListWidgetItem13setBackgroundERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QBrush)
  def setForeground(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QListWidgetItem::setForeground(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#setForeground

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QListWidgetItem::setForeground(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN15QListWidgetItem13setForegroundERK6QBrush',
        self._valueOf(brush),
    )

  @overload(Qt.CheckState)
  def setCheckState(self, state: Qt.CheckState) -> None:
    """
    Calls Qt's 'void QListWidgetItem::setCheckState(Qt::CheckState state)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#setCheckState

    Parameters
    ----------

    state : Qt.CheckState
      Passed on as its number.
    """
    #  void QListWidgetItem::setCheckState(Qt::CheckState state)
    self.uglySide.call(
        'ritual_ZN15QListWidgetItem13setCheckStateEN2Qt10CheckStateE',
        state.value,
    )

  @overload(QSize)
  def setSizeHint(self, size: QSize) -> None:
    """
    Calls Qt's 'void QListWidgetItem::setSizeHint(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#setSizeHint

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QListWidgetItem::setSizeHint(const QSize &size)
    self.uglySide.call(
        'ritual_ZN15QListWidgetItem11setSizeHintERK5QSize',
        self._valueOf(size),
    )

  @overload(int, QVariant)
  def setData(self, role: int, value: QVariant) -> None:
    """
    Calls Qt's 'void QListWidgetItem::setData(int role, const QVariant
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidgetitem.html#setData

    Parameters
    ----------

    role : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QListWidgetItem::setData(int role, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN15QListWidgetItem7setDataEiRK8QVariant',
        role, self._valueOf(value),
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
  @overload(QListWidget)
  @overload(NoneType)
  @overload(QListWidget, int)
  @overload(NoneType, int)
  def __init__(
      self,
      listview: Optional[QListWidget] = None,
      type: int = 0,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QListWidgetItem::QListWidgetItem(QListWidget *listview, int type)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistwidgetitem.html#QListWidgetItem

    Parameters
    ----------

    listview : Optional[QListWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    type : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QListWidgetItem::QListWidgetItem(QListWidget *listview, int type)
    self._noteCreation(QListWidgetItem, lambda: Rituals.call(
        'ritual_ZN15QListWidgetItemC1EP11QListWidgeti',
        self._addressOf(listview), type,
    ))

  @overload(str)
  @overload(str, QListWidget)
  @overload(str, NoneType)
  @overload(str, QListWidget, int)
  @overload(str, NoneType, int)
  def __init__(
      self,
      text: str,
      listview: Optional[QListWidget] = None,
      type: int = 0,
  ) -> None:
    """
    Notes what was given, for Qt's 'QListWidgetItem::QListWidgetItem(const
    QString &text, QListWidget *listview, int type)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistwidgetitem.html#QListWidgetItem

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    listview : Optional[QListWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    type : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QListWidgetItem::QListWidgetItem(const QString &text, QListWidget
    #      *listview, int type)
    self._noteCreation(QListWidgetItem, lambda: Rituals.call(
        'ritual_ZN15QListWidgetItemC1ERK7QStringP11QListWidgeti',
        text, self._addressOf(listview), type,
    ))

  @overload(QIcon, str)
  @overload(QIcon, str, QListWidget)
  @overload(QIcon, str, NoneType)
  @overload(QIcon, str, QListWidget, int)
  @overload(QIcon, str, NoneType, int)
  def __init__(
      self,
      icon: QIcon,
      text: str,
      listview: Optional[QListWidget] = None,
      type: int = 0,
  ) -> None:
    """
    Notes what was given, for Qt's 'QListWidgetItem::QListWidgetItem(const
    QIcon &icon, const QString &text, QListWidget *listview, int type)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistwidgetitem.html#QListWidgetItem

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    listview : Optional[QListWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    type : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QListWidgetItem::QListWidgetItem(const QIcon &icon, const QString
    #      &text, QListWidget *listview, int type)
    self._noteCreation(QListWidgetItem, lambda: Rituals.call(
        'ritual_ZN15QListWidgetItemC1ERK5QIconRK7QStringP11QListWidgeti',
        self._valueOf(icon), text, self._addressOf(listview), type,
    ))

  @overload(THIS)
  def __init__(self, other: QListWidgetItem) -> None:
    """
    Notes what was given, for Qt's 'QListWidgetItem::QListWidgetItem(const
    QListWidgetItem &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistwidgetitem.html#QListWidgetItem

    Parameters
    ----------

    other : QListWidgetItem
      Passed on as a value: Qt reads the C++ QListWidgetItem, which stays
      Python's own.
    """
    #  QListWidgetItem::QListWidgetItem(const QListWidgetItem &other)
    self._noteCreation(QListWidgetItem, lambda: Rituals.call(
        'ritual_ZN15QListWidgetItemC1ERKS_', self._valueOf(other),
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
