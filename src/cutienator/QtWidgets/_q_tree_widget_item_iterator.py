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

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QTreeWidgetItemIteratorIteratorFlag

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QTreeWidget, QTreeWidgetItem
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

  No function of Qt's QTreeWidgetItemIterator yet. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTreeWidgetItemIterator::~QTreeWidgetItemIterator()': the
    destructor: Python removes its C++ QTreeWidgetItemIterator by it, and has
    no other use for it.
  - Qt's 'const QTreeWidgetItemIterator
    QTreeWidgetItemIterator::operator++(int a0)': an operator, which is not
    reflected yet.
  - Qt's 'const QTreeWidgetItemIterator
    QTreeWidgetItemIterator::operator--(int a0)': an operator, which is not
    reflected yet.
  - Qt's 'QTreeWidgetItem *QTreeWidgetItemIterator::operator*() const': an
    operator, which is not reflected yet.

  What has no ritual
  ------------------

  8 of the 15 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet; 3 private.

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

  #  The enums Qt writes inside QTreeWidgetItemIterator, and the names Qt has
  #  for the combinations of its flags enums.
  IteratorFlag = QTreeWidgetItemIteratorIteratorFlag
  IteratorFlags = QTreeWidgetItemIteratorIteratorFlag

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
