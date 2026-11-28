"""
QDockAreaLayoutItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qdockarealayout_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QDockAreaLayoutItem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QDockAreaLayoutInfo, QLayoutItem, QPlaceHolderItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDockAreaLayoutInfo = WAIT['QDockAreaLayoutInfo']
  QLayoutItem = WAIT['QLayoutItem']
  QPlaceHolderItem = WAIT['QPlaceHolderItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDockAreaLayoutItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDockAreaLayoutItem: a plain Python object standing
  in front of one C++ QDockAreaLayoutItem.

  C++ hands a QDockAreaLayoutItem around as a copy, so every C++
  QDockAreaLayoutItem behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDockAreaLayoutItem that has a ritual and that
  Python can call so far, 2 names in all: 'skip', 'expansive'. It can be made
  from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDockAreaLayoutItem::~QDockAreaLayoutItem()': the destructor:
    Python removes its C++ QDockAreaLayoutItem by it, and has no other use
    for it.
  - Qt's 'QDockAreaLayoutItem &QDockAreaLayoutItem::operator=(const
    QDockAreaLayoutItem &other)': assignment: Python binds a name and has no
    operator for it.

  What has no ritual
  ------------------

  6 of the 14 functions Qt declares: 4 leans on 'QDockWidgetGroupWindow; 2
  cannot be called and cannot be called through the meta-object and cannot be
  copied.

  What to expect
  --------------

  - The C++ QDockAreaLayoutItem is created at the first use, not by
    'QDockAreaLayoutItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDockAreaLayoutItem back gives a copy the ritual made
    for Python, in a new cute QDockAreaLayoutItem.
  - Each name of Qt's QDockAreaLayoutItem that has no cute function yet,
    'hasFixedSize', 'maximumSize', 'minimumSize', 'sizeHint', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QDockAreaLayoutItem, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class ItemFlags(CuteNum):
    """
    The enum 'QDockAreaLayoutItem::ItemFlags' of Qt, with the 3 names Qt
    gives in it.
    """

    NoFlags = Kee[int](0)
    GapItem = Kee[int](1)
    KeepSize = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDockAreaLayoutItem'

  #  Qt's '~QDockAreaLayoutItem()'. Naming it makes this a value class:
  #  Python owns every C++ QDockAreaLayoutItem behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QDockAreaLayoutItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def skip(self) -> bool:
    """
    Calls Qt's 'bool QDockAreaLayoutItem::skip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockarealayoutitem.html#skip
    """
    #  bool QDockAreaLayoutItem::skip() const
    return self.uglySide.call('ritual_ZNK19QDockAreaLayoutItem4skipEv')

  @overload(Qt.Orientation)
  def expansive(self, o: Qt.Orientation) -> bool:
    """
    Calls Qt's 'bool QDockAreaLayoutItem::expansive(Qt::Orientation o)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockarealayoutitem.html#expansive

    Parameters
    ----------

    o : Qt.Orientation
      Passed on as its number.
    """
    #  bool QDockAreaLayoutItem::expansive(Qt::Orientation o) const
    return self.uglySide.call(
        'ritual_ZNK19QDockAreaLayoutItem9expansiveEN2Qt11OrientationE',
        o.value,
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(QLayoutItem)
  @overload(NoneType)
  def __init__(self, _widgetItem: Optional[QLayoutItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QDockAreaLayoutItem::QDockAreaLayoutItem(QLayoutItem *_widgetItem)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockarealayoutitem.html#QDockAreaLayoutItem

    Parameters
    ----------

    _widgetItem : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDockAreaLayoutItem::QDockAreaLayoutItem(QLayoutItem *_widgetItem)
    self._noteCreation(QDockAreaLayoutItem, lambda: Rituals.call(
        'ritual_ZN19QDockAreaLayoutItemC1EP11QLayoutItem',
        self._addressOf(_widgetItem, 'QLayoutItem'),
    ))

  @overload(QDockAreaLayoutInfo)
  def __init__(self, _subinfo: Optional[QDockAreaLayoutInfo]) -> None:
    """
    Notes what was given, for Qt's
    'QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutInfo
    *_subinfo)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockarealayoutitem.html#QDockAreaLayoutItem

    Parameters
    ----------

    _subinfo : Optional[QDockAreaLayoutInfo]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutInfo
    #      *_subinfo)
    self._noteCreation(QDockAreaLayoutItem, lambda: Rituals.call(
        'ritual_ZN19QDockAreaLayoutItemC1EP19QDockAreaLayoutInfo',
        self._addressOf(_subinfo),
    ))

  @overload(QPlaceHolderItem)
  def __init__(self, _placeHolderItem: Optional[QPlaceHolderItem]) -> None:
    """
    Notes what was given, for Qt's
    'QDockAreaLayoutItem::QDockAreaLayoutItem(QPlaceHolderItem
    *_placeHolderItem)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockarealayoutitem.html#QDockAreaLayoutItem

    Parameters
    ----------

    _placeHolderItem : Optional[QPlaceHolderItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDockAreaLayoutItem::QDockAreaLayoutItem(QPlaceHolderItem
    #      *_placeHolderItem)
    self._noteCreation(QDockAreaLayoutItem, lambda: Rituals.call(
        'ritual_ZN19QDockAreaLayoutItemC1EP16QPlaceHolderItem',
        self._addressOf(_placeHolderItem),
    ))

  @overload(THIS)
  def __init__(self, other: QDockAreaLayoutItem) -> None:
    """
    Notes what was given, for Qt's
    'QDockAreaLayoutItem::QDockAreaLayoutItem(const QDockAreaLayoutItem
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdockarealayoutitem.html#QDockAreaLayoutItem

    Parameters
    ----------

    other : QDockAreaLayoutItem
      Passed on as a value: Qt reads the C++ QDockAreaLayoutItem, which stays
      Python's own.
    """
    #  QDockAreaLayoutItem::QDockAreaLayoutItem(const QDockAreaLayoutItem
    #      &other)
    self._noteCreation(QDockAreaLayoutItem, lambda: Rituals.call(
        'ritual_ZN19QDockAreaLayoutItemC1ERKS_', self._valueOf(other),
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

  @staticmethod
  def hasFixedSize(*__, **_) -> Never:
    """
    Qt's 'bool QDockAreaLayoutItem::hasFixedSize(Qt::Orientation o) const':
    leans on 'QDockWidgetGroupWindow::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutItem.hasFixedSize' has no cute function yet. Qt's "
        "'bool QDockAreaLayoutItem::hasFixedSize(Qt::Orientation o) const': "
        "leans on 'QDockWidgetGroupWindow::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def maximumSize(*__, **_) -> Never:
    """
    Qt's 'QSize QDockAreaLayoutItem::maximumSize() const': leans on
    'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutItem.maximumSize' has no cute function yet. Qt's "
        "'QSize QDockAreaLayoutItem::maximumSize() const': leans on "
        "'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def minimumSize(*__, **_) -> Never:
    """
    Qt's 'QSize QDockAreaLayoutItem::minimumSize() const': leans on
    'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutItem.minimumSize' has no cute function yet. Qt's "
        "'QSize QDockAreaLayoutItem::minimumSize() const': leans on "
        "'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def sizeHint(*__, **_) -> Never:
    """
    Qt's 'QSize QDockAreaLayoutItem::sizeHint() const': leans on
    'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDockAreaLayoutItem.sizeHint' has no cute function yet. Qt's "
        "'QSize QDockAreaLayoutItem::sizeHint() const': leans on "
        "'QDockWidgetGroupWindow::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
