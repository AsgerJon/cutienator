"""
Qt3DExtras::QSpriteGrid binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qspritegrid.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSpriteGrid(Qt3DExtras.QAbstractSpriteSheet):
  """
  The cute side of Qt's Qt3DExtras::QSpriteGrid: a plain Python object
  standing in front of one C++ Qt3DExtras::QSpriteGrid.

  It is built on the cute 'Qt3DExtras::QAbstractSpriteSheet', as Qt's
  Qt3DExtras::QSpriteGrid is built on Qt's Qt3DExtras::QAbstractSpriteSheet,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QSpriteGrid that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'rows',
  'columns', 'setRows', 'setColumns', 'rowsChanged', 'columnsChanged',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QSpriteGrid::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QSpriteGrid::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QSpriteGrid::~QSpriteGrid()': the destructor: Python
    never removes a C++ Qt3DExtras::QSpriteGrid.
  - Qt's 'const QSpriteGridPrivate *Qt3DExtras::QSpriteGrid::d_func() const':
    takes in Python what 'QSpriteGridPrivate
    *Qt3DExtras::QSpriteGrid::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QSpriteGrid is created at the first use, not by
    'Qt3DExtras::QSpriteGrid(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QSpriteGrid.
  - Qt tells when it has removed the C++ Qt3DExtras::QSpriteGrid. Every call
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
    Calls Qt's 'QString Qt3DExtras::QSpriteGrid::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qspritegrid.html#tr

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
    #  QString Qt3DExtras::QSpriteGrid::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras11QSpriteGrid2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QSpriteGrid'

  #  A C++ Qt3DExtras::QSpriteGrid Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QSpriteGrid'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DExtras::QSpriteGrid::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritegrid.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QSpriteGrid::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras11QSpriteGrid10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rows(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QSpriteGrid::rows() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qspritegrid.html#rows
    """
    #  int Qt3DExtras::QSpriteGrid::rows() const
    return self.uglySide.call('ritual_ZNK10Qt3DExtras11QSpriteGrid4rowsEv')

  def columns(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QSpriteGrid::columns() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritegrid.html#columns
    """
    #  int Qt3DExtras::QSpriteGrid::columns() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras11QSpriteGrid7columnsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setRows(self, rows: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSpriteGrid::setRows(int rows)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritegrid.html#setRows

    Parameters
    ----------

    rows : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QSpriteGrid::setRows(int rows)
    self.uglySide.call('ritual_ZN10Qt3DExtras11QSpriteGrid7setRowsEi', rows)

  @overload(int)
  def setColumns(self, columns: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSpriteGrid::setColumns(int columns)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritegrid.html#setColumns

    Parameters
    ----------

    columns : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QSpriteGrid::setColumns(int columns)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras11QSpriteGrid10setColumnsEi', columns,
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DExtras::QSpriteGrid::QSpriteGrid(Qt3DCore::QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritegrid.html#QSpriteGrid

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QSpriteGrid::QSpriteGrid(Qt3DCore::QNode *parent)
    self._noteCreation(QSpriteGrid, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras11QSpriteGridC1EPN8Qt3DCore5QNodeE',
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

  @overload(int)
  def rowsChanged(self, rows: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSpriteGrid::rowsChanged(int rows)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritegrid.html#rowsChanged

    Parameters
    ----------

    rows : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QSpriteGrid::rowsChanged(int rows)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras11QSpriteGrid11rowsChangedEi', rows,
    )

  @overload(int)
  def columnsChanged(self, columns: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSpriteGrid::columnsChanged(int columns)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritegrid.html#columnsChanged

    Parameters
    ----------

    columns : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QSpriteGrid::columnsChanged(int columns)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras11QSpriteGrid14columnsChangedEi', columns,
    )

  def d_func(self) -> Optional[Qt3DExtras.QSpriteGridPrivate]:
    """
    Calls Qt's 'QSpriteGridPrivate *Qt3DExtras::QSpriteGrid::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qspritegrid.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QSpriteGridPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSpriteGridPrivate *Qt3DExtras::QSpriteGrid::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras11QSpriteGrid6d_funcEv',
    )
    return Qt3DExtras.QSpriteGridPrivate._cuteAt(address)
