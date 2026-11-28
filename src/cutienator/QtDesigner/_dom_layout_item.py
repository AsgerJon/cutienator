"""
DomLayoutItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomLayoutItem to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import DomLayout, DomSpacer, DomWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomLayout = WAIT['DomLayout']
  DomSpacer = WAIT['DomSpacer']
  DomWidget = WAIT['DomWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DomLayoutItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomLayoutItem: a plain Python object standing in
  front of one C++ DomLayoutItem.

  What exists
  -----------

  Every function of Qt's DomLayoutItem that has a ritual and that Python can
  call so far, 31 names in all: 'hasAttributeRow', 'attributeRow',
  'setAttributeRow', 'clearAttributeRow', 'hasAttributeColumn',
  'attributeColumn', 'setAttributeColumn', 'clearAttributeColumn',
  'hasAttributeRowSpan', 'attributeRowSpan', 'setAttributeRowSpan',
  'clearAttributeRowSpan', 'hasAttributeColSpan', 'attributeColSpan',
  'setAttributeColSpan', 'clearAttributeColSpan', 'hasAttributeAlignment',
  'attributeAlignment', 'setAttributeAlignment', 'clearAttributeAlignment',
  'kind', 'elementWidget', 'takeElementWidget', 'setElementWidget',
  'elementLayout', 'takeElementLayout', 'setElementLayout', 'elementSpacer',
  'takeElementSpacer', 'setElementSpacer', 'clear'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomLayoutItem::~DomLayoutItem()': the destructor: Python never
    removes a C++ DomLayoutItem.
  - Qt's 'void DomLayoutItem::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomLayoutItem::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 39 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomLayoutItem is created at the first use, not by
    'DomLayoutItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomLayoutItem.
  - Each name of Qt's DomLayoutItem that has no cute function yet, 'read',
    'write', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside DomLayoutItem, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Kind(CuteNum):
    """
    The enum 'DomLayoutItem::Kind' of Qt, with the 4 names Qt gives in it.
    """

    Unknown = Kee[int](0)
    Widget = Kee[int](1)
    Layout = Kee[int](2)
    Spacer = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DomLayoutItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeRow(self) -> bool:
    """
    Calls Qt's 'bool DomLayoutItem::hasAttributeRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/domlayoutitem.html#hasAttributeRow
    """
    #  bool DomLayoutItem::hasAttributeRow() const
    return self.uglySide.call('ritual_ZNK13DomLayoutItem15hasAttributeRowEv')

  def attributeRow(self) -> int:
    """
    Calls Qt's 'int DomLayoutItem::attributeRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/domlayoutitem.html#attributeRow
    """
    #  int DomLayoutItem::attributeRow() const
    return self.uglySide.call('ritual_ZNK13DomLayoutItem12attributeRowEv')

  def hasAttributeColumn(self) -> bool:
    """
    Calls Qt's 'bool DomLayoutItem::hasAttributeColumn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutitem.html#hasAttributeColumn
    """
    #  bool DomLayoutItem::hasAttributeColumn() const
    return self.uglySide.call(
        'ritual_ZNK13DomLayoutItem18hasAttributeColumnEv',
    )

  def attributeColumn(self) -> int:
    """
    Calls Qt's 'int DomLayoutItem::attributeColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/domlayoutitem.html#attributeColumn
    """
    #  int DomLayoutItem::attributeColumn() const
    return self.uglySide.call('ritual_ZNK13DomLayoutItem15attributeColumnEv')

  def hasAttributeRowSpan(self) -> bool:
    """
    Calls Qt's 'bool DomLayoutItem::hasAttributeRowSpan() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutitem.html#hasAttributeRowSpan
    """
    #  bool DomLayoutItem::hasAttributeRowSpan() const
    return self.uglySide.call(
        'ritual_ZNK13DomLayoutItem19hasAttributeRowSpanEv',
    )

  def attributeRowSpan(self) -> int:
    """
    Calls Qt's 'int DomLayoutItem::attributeRowSpan() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutitem.html#attributeRowSpan
    """
    #  int DomLayoutItem::attributeRowSpan() const
    return self.uglySide.call(
        'ritual_ZNK13DomLayoutItem16attributeRowSpanEv',
    )

  def hasAttributeColSpan(self) -> bool:
    """
    Calls Qt's 'bool DomLayoutItem::hasAttributeColSpan() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutitem.html#hasAttributeColSpan
    """
    #  bool DomLayoutItem::hasAttributeColSpan() const
    return self.uglySide.call(
        'ritual_ZNK13DomLayoutItem19hasAttributeColSpanEv',
    )

  def attributeColSpan(self) -> int:
    """
    Calls Qt's 'int DomLayoutItem::attributeColSpan() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutitem.html#attributeColSpan
    """
    #  int DomLayoutItem::attributeColSpan() const
    return self.uglySide.call(
        'ritual_ZNK13DomLayoutItem16attributeColSpanEv',
    )

  def hasAttributeAlignment(self) -> bool:
    """
    Calls Qt's 'bool DomLayoutItem::hasAttributeAlignment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutitem.html#hasAttributeAlignment
    """
    #  bool DomLayoutItem::hasAttributeAlignment() const
    return self.uglySide.call(
        'ritual_ZNK13DomLayoutItem21hasAttributeAlignmentEv',
    )

  def attributeAlignment(self) -> str:
    """
    Calls Qt's 'QString DomLayoutItem::attributeAlignment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutitem.html#attributeAlignment

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomLayoutItem::attributeAlignment() const
    return self.uglySide.call(
        'ritual_ZNK13DomLayoutItem18attributeAlignmentEv',
    )

  def kind(self) -> Kind:
    """
    Calls Qt's 'Kind DomLayoutItem::kind() const'.

    Qt's own words: https://doc.qt.io/qt-6/domlayoutitem.html#kind

    Returns
    -------

    Kind
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Kind(number)' gives.
    """
    #  Kind DomLayoutItem::kind() const
    return DomLayoutItem.Kind(self.uglySide.call(
        'ritual_ZNK13DomLayoutItem4kindEv',
    ))

  def elementWidget(self) -> Optional[DomWidget]:
    """
    Calls Qt's 'DomWidget *DomLayoutItem::elementWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/domlayoutitem.html#elementWidget

    Returns
    -------

    Optional[DomWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomWidget *DomLayoutItem::elementWidget() const
    address = self.uglySide.call(
        'ritual_ZNK13DomLayoutItem13elementWidgetEv',
    )
    from . import DomWidget
    return DomWidget._cuteAt(address)

  def elementLayout(self) -> Optional[DomLayout]:
    """
    Calls Qt's 'DomLayout *DomLayoutItem::elementLayout() const'.

    Qt's own words: https://doc.qt.io/qt-6/domlayoutitem.html#elementLayout

    Returns
    -------

    Optional[DomLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomLayout *DomLayoutItem::elementLayout() const
    address = self.uglySide.call(
        'ritual_ZNK13DomLayoutItem13elementLayoutEv',
    )
    from . import DomLayout
    return DomLayout._cuteAt(address)

  def elementSpacer(self) -> Optional[DomSpacer]:
    """
    Calls Qt's 'DomSpacer *DomLayoutItem::elementSpacer() const'.

    Qt's own words: https://doc.qt.io/qt-6/domlayoutitem.html#elementSpacer

    Returns
    -------

    Optional[DomSpacer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomSpacer *DomLayoutItem::elementSpacer() const
    address = self.uglySide.call(
        'ritual_ZNK13DomLayoutItem13elementSpacerEv',
    )
    from . import DomSpacer
    return DomSpacer._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setAttributeRow(self, a: int) -> None:
    """
    Calls Qt's 'void DomLayoutItem::setAttributeRow(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domlayoutitem.html#setAttributeRow

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomLayoutItem::setAttributeRow(int a)
    self.uglySide.call('ritual_ZN13DomLayoutItem15setAttributeRowEi', a)

  @overload(int)
  def setAttributeColumn(self, a: int) -> None:
    """
    Calls Qt's 'void DomLayoutItem::setAttributeColumn(int a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutitem.html#setAttributeColumn

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomLayoutItem::setAttributeColumn(int a)
    self.uglySide.call('ritual_ZN13DomLayoutItem18setAttributeColumnEi', a)

  @overload(int)
  def setAttributeRowSpan(self, a: int) -> None:
    """
    Calls Qt's 'void DomLayoutItem::setAttributeRowSpan(int a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutitem.html#setAttributeRowSpan

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomLayoutItem::setAttributeRowSpan(int a)
    self.uglySide.call('ritual_ZN13DomLayoutItem19setAttributeRowSpanEi', a)

  @overload(int)
  def setAttributeColSpan(self, a: int) -> None:
    """
    Calls Qt's 'void DomLayoutItem::setAttributeColSpan(int a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutitem.html#setAttributeColSpan

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomLayoutItem::setAttributeColSpan(int a)
    self.uglySide.call('ritual_ZN13DomLayoutItem19setAttributeColSpanEi', a)

  @overload(str)
  def setAttributeAlignment(self, a: str) -> None:
    """
    Calls Qt's 'void DomLayoutItem::setAttributeAlignment(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutitem.html#setAttributeAlignment

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomLayoutItem::setAttributeAlignment(const QString &a)
    self.uglySide.call(
        'ritual_ZN13DomLayoutItem21setAttributeAlignmentERK7QString', a,
    )

  @overload(DomWidget)
  @overload(NoneType)
  def setElementWidget(self, a: Optional[DomWidget]) -> None:
    """
    Calls Qt's 'void DomLayoutItem::setElementWidget(DomWidget *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutitem.html#setElementWidget

    Parameters
    ----------

    a : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomLayoutItem::setElementWidget(DomWidget *a)
    self.uglySide.call(
        'ritual_ZN13DomLayoutItem16setElementWidgetEP9DomWidget',
        self._addressOf(a),
    )

  @overload(DomLayout)
  @overload(NoneType)
  def setElementLayout(self, a: Optional[DomLayout]) -> None:
    """
    Calls Qt's 'void DomLayoutItem::setElementLayout(DomLayout *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutitem.html#setElementLayout

    Parameters
    ----------

    a : Optional[DomLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomLayoutItem::setElementLayout(DomLayout *a)
    self.uglySide.call(
        'ritual_ZN13DomLayoutItem16setElementLayoutEP9DomLayout',
        self._addressOf(a),
    )

  @overload(DomSpacer)
  @overload(NoneType)
  def setElementSpacer(self, a: Optional[DomSpacer]) -> None:
    """
    Calls Qt's 'void DomLayoutItem::setElementSpacer(DomSpacer *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutitem.html#setElementSpacer

    Parameters
    ----------

    a : Optional[DomSpacer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomLayoutItem::setElementSpacer(DomSpacer *a)
    self.uglySide.call(
        'ritual_ZN13DomLayoutItem16setElementSpacerEP9DomSpacer',
        self._addressOf(a),
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
    Notes what was given, for Qt's 'DomLayoutItem::DomLayoutItem()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/domlayoutitem.html#DomLayoutItem
    """
    #  DomLayoutItem::DomLayoutItem()
    self._noteCreation(DomLayoutItem, lambda: Rituals.call(
        'ritual_ZN13DomLayoutItemC1Ev',
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

  def clearAttributeRow(self) -> None:
    """
    Calls Qt's 'void DomLayoutItem::clearAttributeRow()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutitem.html#clearAttributeRow
    """
    #  void DomLayoutItem::clearAttributeRow()
    self.uglySide.call('ritual_ZN13DomLayoutItem17clearAttributeRowEv')

  def clearAttributeColumn(self) -> None:
    """
    Calls Qt's 'void DomLayoutItem::clearAttributeColumn()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutitem.html#clearAttributeColumn
    """
    #  void DomLayoutItem::clearAttributeColumn()
    self.uglySide.call('ritual_ZN13DomLayoutItem20clearAttributeColumnEv')

  def clearAttributeRowSpan(self) -> None:
    """
    Calls Qt's 'void DomLayoutItem::clearAttributeRowSpan()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutitem.html#clearAttributeRowSpan
    """
    #  void DomLayoutItem::clearAttributeRowSpan()
    self.uglySide.call('ritual_ZN13DomLayoutItem21clearAttributeRowSpanEv')

  def clearAttributeColSpan(self) -> None:
    """
    Calls Qt's 'void DomLayoutItem::clearAttributeColSpan()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutitem.html#clearAttributeColSpan
    """
    #  void DomLayoutItem::clearAttributeColSpan()
    self.uglySide.call('ritual_ZN13DomLayoutItem21clearAttributeColSpanEv')

  def clearAttributeAlignment(self) -> None:
    """
    Calls Qt's 'void DomLayoutItem::clearAttributeAlignment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutitem.html#clearAttributeAlignment
    """
    #  void DomLayoutItem::clearAttributeAlignment()
    self.uglySide.call('ritual_ZN13DomLayoutItem23clearAttributeAlignmentEv')

  def takeElementWidget(self) -> Optional[DomWidget]:
    """
    Calls Qt's 'DomWidget *DomLayoutItem::takeElementWidget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutitem.html#takeElementWidget

    Returns
    -------

    Optional[DomWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomWidget *DomLayoutItem::takeElementWidget()
    address = self.uglySide.call(
        'ritual_ZN13DomLayoutItem17takeElementWidgetEv',
    )
    from . import DomWidget
    return DomWidget._cuteAt(address)

  def takeElementLayout(self) -> Optional[DomLayout]:
    """
    Calls Qt's 'DomLayout *DomLayoutItem::takeElementLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutitem.html#takeElementLayout

    Returns
    -------

    Optional[DomLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomLayout *DomLayoutItem::takeElementLayout()
    address = self.uglySide.call(
        'ritual_ZN13DomLayoutItem17takeElementLayoutEv',
    )
    from . import DomLayout
    return DomLayout._cuteAt(address)

  def takeElementSpacer(self) -> Optional[DomSpacer]:
    """
    Calls Qt's 'DomSpacer *DomLayoutItem::takeElementSpacer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutitem.html#takeElementSpacer

    Returns
    -------

    Optional[DomSpacer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomSpacer *DomLayoutItem::takeElementSpacer()
    address = self.uglySide.call(
        'ritual_ZN13DomLayoutItem17takeElementSpacerEv',
    )
    from . import DomSpacer
    return DomSpacer._cuteAt(address)

  def clear(self) -> None:
    """
    Calls Qt's 'void DomLayoutItem::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/domlayoutitem.html#clear
    """
    #  void DomLayoutItem::clear()
    self.uglySide.call('ritual_ZN13DomLayoutItem5clearEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomLayoutItem::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomLayoutItem.read' has no cute function yet. Qt's 'void "
        "DomLayoutItem::read(QXmlStreamReader &reader)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomLayoutItem::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomLayoutItem.write' has no cute function yet. Qt's 'void "
        "DomLayoutItem::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<DomLayoutItem *>': the list of DomLayoutItem, which
#  'QList[DomLayoutItem]' gives. It is made here, so that there is one as
#  soon as there can be a DomLayoutItem.
QList.createKind(
    DomLayoutItem, 'address',
    make='ritual_list_make_DomLayoutItem_ptr',
    add='ritual_list_add_DomLayoutItem_ptr',
    size='ritual_list_size_DomLayoutItem_ptr',
    at='ritual_list_at_DomLayoutItem_ptr',
    drop='ritual_list_drop_DomLayoutItem_ptr',
)
