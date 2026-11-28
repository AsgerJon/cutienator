"""
qdesigner_internal::TableWidgetContents binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::TableWidgetContents to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtWidgets import QTableWidget, QTableWidgetItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTableWidget = WAIT['QTableWidget']
  QTableWidgetItem = WAIT['QTableWidgetItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class TableWidgetContents(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qdesigner_internal::TableWidgetContents: a plain
  Python object standing in front of one C++
  qdesigner_internal::TableWidgetContents.

  C++ hands a qdesigner_internal::TableWidgetContents around as a copy, so
  every C++ qdesigner_internal::TableWidgetContents behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::TableWidgetContents that has a
  ritual and that Python can call so far, 8 names in all: 'clear',
  'fromTableWidget', 'applyToTableWidget', 'nonEmpty', 'defaultHeaderText',
  'insertHeaderItem', '__eq__', '__ne__'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::TableWidgetContents::~TableWidgetContents()':
    the destructor: Python removes its C++
    qdesigner_internal::TableWidgetContents by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ qdesigner_internal::TableWidgetContents is created at the first
    use, not by 'qdesigner_internal::TableWidgetContents(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::TableWidgetContents back gives a
    copy the ritual made for Python, in a new cute
    qdesigner_internal::TableWidgetContents.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QTableWidgetItem, int)
  @overload(NoneType, int)
  def nonEmpty(item: Optional[QTableWidgetItem], headerColumn: int) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::TableWidgetContents::nonEmpty(const
    QTableWidgetItem *item, int headerColumn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-tablewidgetcontents.html

    Parameters
    ----------

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    headerColumn : int
      Passed on as it is.
    """
    #  bool qdesigner_internal::TableWidgetContents::nonEmpty(const
    #      QTableWidgetItem *item, int headerColumn)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal19TableWidgetContents8nonEmptyEPK16QT'
        'ableWidgetItemi',
        CuteMixin._addressOf(item), headerColumn,
    )

  @staticmethod
  @overload(int)
  def defaultHeaderText(i: int) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::TableWidgetContents::defaultHeaderText(int i)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-tablewidgetcontents.html

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::TableWidgetContents::defaultHeaderText(int
    #      i)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal19TableWidgetContents17defaultHeaderT'
        'extEi',
        i,
    )

  @staticmethod
  @overload(
      QTableWidgetItem, int, WAIT['qdesigner_internal.ListContents'], bool,
  )
  @overload(QTableWidgetItem, int, NoneType, bool)
  @overload(NoneType, int, WAIT['qdesigner_internal.ListContents'], bool)
  @overload(NoneType, int, NoneType, bool)
  def insertHeaderItem(
      item: Optional[QTableWidgetItem],
      i: int,
      header: Optional[qdesigner_internal.ListContents],
      editor: bool,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::TableWidgetContents::insertHeaderItem(const
    QTableWidgetItem *item, int i, ListContents *header, bool editor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-tablewidgetcontents.html

    Parameters
    ----------

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    i : int
      Passed on as it is.

    header : Optional[qdesigner_internal.ListContents]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    editor : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::TableWidgetContents::insertHeaderItem(const
    #      QTableWidgetItem *item, int i, ListContents *header, bool editor)
    Rituals.call(
        'ritual_ZN18qdesigner_internal19TableWidgetContents16insertHeaderIt'
        'emEPK16QTableWidgetItemiPNS_12ListContentsEb',
        CuteMixin._addressOf(item), i, CuteMixin._addressOf(header), editor,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::TableWidgetContents'

  #  Qt's '~qdesigner_internal::TableWidgetContents()'. Naming it makes this
  #  a value class: Python owns every C++
  #  qdesigner_internal::TableWidgetContents behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN18qdesigner_internal19TableWidgetContentsD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: TableWidgetContents) -> bool:
    """
    Calls Qt's 'bool operator==(const TableWidgetContents &lhs, const
    TableWidgetContents &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-tablewidgetcontents.html

    Parameters
    ----------

    rhs : TableWidgetContents
      Passed on as a value: Qt reads the C++
      qdesigner_internal::TableWidgetContents, which stays Python's own.
    """
    #  bool operator==(const TableWidgetContents &lhs, const
    #      TableWidgetContents &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internaleqERKNS_19TableWidgetContentsES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: TableWidgetContents) -> bool:
    """
    Calls Qt's 'bool operator!=(const TableWidgetContents &lhs, const
    TableWidgetContents &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-tablewidgetcontents.html

    Parameters
    ----------

    rhs : TableWidgetContents
      Passed on as a value: Qt reads the C++
      qdesigner_internal::TableWidgetContents, which stays Python's own.
    """
    #  bool operator!=(const TableWidgetContents &lhs, const
    #      TableWidgetContents &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internalneERKNS_19TableWidgetContentsES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::TableWidgetContents::TableWidgetContents()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-tablewidgetcontents.html
    """
    #  qdesigner_internal::TableWidgetContents::TableWidgetContents()
    self._noteCreation(TableWidgetContents, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal19TableWidgetContentsC1Ev',
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

  def clear(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::TableWidgetContents::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-tablewidgetcontents.html#clear
    """
    #  void qdesigner_internal::TableWidgetContents::clear()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal19TableWidgetContents5clearEv',
    )

  @overload(QTableWidget, bool)
  @overload(NoneType, bool)
  def fromTableWidget(
      self,
      tableWidget: Optional[QTableWidget],
      editor: bool,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::TableWidgetContents::fromTableWidget(const
    QTableWidget *tableWidget, bool editor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-tablewidgetcontents.html

    Parameters
    ----------

    tableWidget : Optional[QTableWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    editor : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::TableWidgetContents::fromTableWidget(const
    #      QTableWidget *tableWidget, bool editor)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal19TableWidgetContents15fromTableWidge'
        'tEPK12QTableWidgetb',
        self._addressOf(tableWidget), editor,
    )

  @overload(QTableWidget, WAIT['qdesigner_internal.DesignerIconCache'], bool)
  @overload(QTableWidget, NoneType, bool)
  @overload(NoneType, WAIT['qdesigner_internal.DesignerIconCache'], bool)
  @overload(NoneType, NoneType, bool)
  def applyToTableWidget(
      self,
      tableWidget: Optional[QTableWidget],
      iconCache: Optional[qdesigner_internal.DesignerIconCache],
      editor: bool,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::TableWidgetContents::applyToTableWidget(QTableWidget
    *tableWidget, DesignerIconCache *iconCache, bool editor) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-tablewidgetcontents.html

    Parameters
    ----------

    tableWidget : Optional[QTableWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    iconCache : Optional[qdesigner_internal.DesignerIconCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    editor : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::TableWidgetContents::applyToTableWidget(
    #      QTableWidget *tableWidget, DesignerIconCache *iconCache, bool
    #      editor) const
    self.uglySide.call(
        'ritual_ZNK18qdesigner_internal19TableWidgetContents18applyToTableW'
        'idgetEP12QTableWidgetPNS_17DesignerIconCacheEb',
        self._addressOf(tableWidget), self._addressOf(iconCache), editor,
    )
