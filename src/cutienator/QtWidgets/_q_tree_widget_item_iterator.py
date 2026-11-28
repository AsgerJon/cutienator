"""
QTreeWidgetItemIterator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qtreewidgetitemiterator.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QTreeWidget, QTreeWidgetItem, QTreeWidgetItemIteratorPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTreeWidget = WAIT['QTreeWidget']
  QTreeWidgetItem = WAIT['QTreeWidgetItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTreeWidgetItemIterator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTreeWidgetItemIterator: a plain Python object
  standing in front of one C++ QTreeWidgetItemIterator.

  C++ hands a QTreeWidgetItemIterator around as a copy, so every C++
  QTreeWidgetItemIterator behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTreeWidgetItemIterator that has a ritual and that
  Python can call so far, 4 names in all: '__iadd__', '__isub__',
  'matchesFlags', 'd_func'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTreeWidgetItemIterator::~QTreeWidgetItemIterator()': the
    destructor: Python removes its C++ QTreeWidgetItemIterator by it, and has
    no other use for it.
  - Qt's 'QTreeWidgetItemIterator &QTreeWidgetItemIterator::operator=(const
    QTreeWidgetItemIterator &it)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QTreeWidgetItemIterator &QTreeWidgetItemIterator::operator++()': an
    operator Python has no name for.
  - Qt's 'const QTreeWidgetItemIterator
    QTreeWidgetItemIterator::operator++(int a0)': an operator Python has no
    name for.
  - Qt's 'QTreeWidgetItemIterator &QTreeWidgetItemIterator::operator--()': an
    operator Python has no name for.
  - Qt's 'const QTreeWidgetItemIterator
    QTreeWidgetItemIterator::operator--(int a0)': an operator Python has no
    name for.
  - Qt's 'QTreeWidgetItem *QTreeWidgetItemIterator::operator*() const': an
    operator Python has no name for.
  - Qt's 'const QTreeWidgetItemIteratorPrivate
    *QTreeWidgetItemIterator::d_func() const': takes in Python what
    'QTreeWidgetItemIteratorPrivate *QTreeWidgetItemIterator::d_func()'
    takes.

  What to expect
  --------------

  - The C++ QTreeWidgetItemIterator is created at the first use, not by
    'QTreeWidgetItemIterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTreeWidgetItemIterator back gives a copy the ritual
    made for Python, in a new cute QTreeWidgetItemIterator.
  """

  #  The enums Qt writes inside QTreeWidgetItemIterator, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class IteratorFlag(CuteFlags):
    """
    The flags enum 'QTreeWidgetItemIterator::IteratorFlag' of Qt, with the 20
    names Qt gives in it. Qt names the type of its combinations
    'QTreeWidgetItemIterator::IteratorFlags'.
    """

    All = 0x0
    Hidden = 0x1
    NotHidden = 0x2
    Selected = 0x4
    Unselected = 0x8
    Selectable = 0x10
    NotSelectable = 0x20
    DragEnabled = 0x40
    DragDisabled = 0x80
    DropEnabled = 0x100
    DropDisabled = 0x200
    HasChildren = 0x400
    NoChildren = 0x800
    Checked = 0x1000
    NotChecked = 0x2000
    Enabled = 0x4000
    Disabled = 0x8000
    Editable = 0x10000
    NotEditable = 0x20000
    UserFlag = 0x1000000

  IteratorFlags = IteratorFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTreeWidgetItemIterator'

  #  Qt's '~QTreeWidgetItemIterator()'. Naming it makes this a value class:
  #  Python owns every C++ QTreeWidgetItemIterator behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QTreeWidgetItemIteratorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  def matchesFlags(self, item: Optional[QTreeWidgetItem]) -> bool:
    """
    Calls Qt's 'bool QTreeWidgetItemIterator::matchesFlags(const
    QTreeWidgetItem *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitemiterator.html#matchesFlags

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QTreeWidgetItemIterator::matchesFlags(const QTreeWidgetItem
    #      *item) const
    return self.uglySide.call(
        'ritual_ZNK23QTreeWidgetItemIterator12matchesFlagsEPK15QTreeWidgetI'
        'tem',
        self._addressOf(item),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def __iadd__(self, n: int) -> QTreeWidgetItemIterator:
    """
    Calls Qt's 'QTreeWidgetItemIterator
    &QTreeWidgetItemIterator::operator+=(int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitemiterator.html#operator+=

    Parameters
    ----------

    n : int
      Passed on as it is.
    """
    #  QTreeWidgetItemIterator &QTreeWidgetItemIterator::operator+=(int n)
    self.uglySide.call('ritual_ZN23QTreeWidgetItemIteratorpLEi', n)
    return self

  @overload.fallback
  def __iadd__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(int)
  def __isub__(self, n: int) -> QTreeWidgetItemIterator:
    """
    Calls Qt's 'QTreeWidgetItemIterator
    &QTreeWidgetItemIterator::operator-=(int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitemiterator.html#operator-=

    Parameters
    ----------

    n : int
      Passed on as it is.
    """
    #  QTreeWidgetItemIterator &QTreeWidgetItemIterator::operator-=(int n)
    self.uglySide.call('ritual_ZN23QTreeWidgetItemIteratormIEi', n)
    return self

  @overload.fallback
  def __isub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __init__(self, it: QTreeWidgetItemIterator) -> None:
    """
    Notes what was given, for Qt's
    'QTreeWidgetItemIterator::QTreeWidgetItemIterator(const
    QTreeWidgetItemIterator &it)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitemiterator.html

    Parameters
    ----------

    it : QTreeWidgetItemIterator
      Passed on as a value: Qt reads the C++ QTreeWidgetItemIterator, which
      stays Python's own.
    """
    #  QTreeWidgetItemIterator::QTreeWidgetItemIterator(const
    #      QTreeWidgetItemIterator &it)
    self._noteCreation(QTreeWidgetItemIterator, lambda: Rituals.call(
        'ritual_ZN23QTreeWidgetItemIteratorC1ERKS_', self._valueOf(it),
    ))

  @overload(QTreeWidget)
  @overload(NoneType)
  @overload(QTreeWidget, IteratorFlags)
  @overload(NoneType, IteratorFlags)
  def __init__(
      self,
      widget: Optional[QTreeWidget],
      flags: IteratorFlags = IteratorFlags.All,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QTreeWidgetItemIterator::QTreeWidgetItemIterator(QTreeWidget *widget,
    IteratorFlags flags)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitemiterator.html

    Parameters
    ----------

    widget : Optional[QTreeWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : IteratorFlags
      Passed on as its number. May be left out, as in Qt: it is then
      IteratorFlags.All.
    """
    #  QTreeWidgetItemIterator::QTreeWidgetItemIterator(QTreeWidget *widget,
    #      IteratorFlags flags)
    self._noteCreation(QTreeWidgetItemIterator, lambda: Rituals.call(
        'ritual_ZN23QTreeWidgetItemIteratorC1EP11QTreeWidget6QFlagsINS_12It'
        'eratorFlagEE',
        self._addressOf(widget), flags.value,
    ))

  @overload(QTreeWidgetItem)
  @overload(QTreeWidgetItem, IteratorFlags)
  def __init__(
      self,
      item: Optional[QTreeWidgetItem],
      flags: IteratorFlags = IteratorFlags.All,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QTreeWidgetItemIterator::QTreeWidgetItemIterator(QTreeWidgetItem *item,
    IteratorFlags flags)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitemiterator.html

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : IteratorFlags
      Passed on as its number. May be left out, as in Qt: it is then
      IteratorFlags.All.
    """
    #  QTreeWidgetItemIterator::QTreeWidgetItemIterator(QTreeWidgetItem
    #      *item, IteratorFlags flags)
    self._noteCreation(QTreeWidgetItemIterator, lambda: Rituals.call(
        'ritual_ZN23QTreeWidgetItemIteratorC1EP15QTreeWidgetItem6QFlagsINS_'
        '12IteratorFlagEE',
        self._addressOf(item), flags.value,
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

  def d_func(self) -> Optional[QTreeWidgetItemIteratorPrivate]:
    """
    Calls Qt's 'QTreeWidgetItemIteratorPrivate
    *QTreeWidgetItemIterator::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitemiterator.html#d_func

    Returns
    -------

    Optional[QTreeWidgetItemIteratorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItemIteratorPrivate *QTreeWidgetItemIterator::d_func()
    address = self.uglySide.call(
        'ritual_ZN23QTreeWidgetItemIterator6d_funcEv',
    )
    from . import QTreeWidgetItemIteratorPrivate
    return QTreeWidgetItemIteratorPrivate._cuteAt(address)
