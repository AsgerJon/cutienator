"""
QItemSelectionRange binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qitemselectionmodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAbstractItemModel, QModelIndex, QPersistentModelIndex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']


class QItemSelectionRange(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QItemSelectionRange: a plain Python object standing
  in front of one C++ QItemSelectionRange.

  C++ hands a QItemSelectionRange around as a copy, so every C++
  QItemSelectionRange behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QItemSelectionRange that has a ritual and that
  Python can call so far, 15 names in all: 'top', 'left', 'bottom', 'right',
  'width', 'height', 'topLeft', 'bottomRight', 'parent', 'model', 'contains',
  'intersects', 'intersected', 'isValid', 'isEmpty'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QItemSelectionRange::~QItemSelectionRange()': the destructor:
    Python removes its C++ QItemSelectionRange by it, and has no other use
    for it.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QItemSelectionRange is created at the first use, not by
    'QItemSelectionRange(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QItemSelectionRange back gives a copy the ritual made
    for Python, in a new cute QItemSelectionRange.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QItemSelectionRange'

  #  Qt's '~QItemSelectionRange()'. Naming it makes this a value class:
  #  Python owns every C++ QItemSelectionRange behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QItemSelectionRangeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def top(self) -> int:
    """
    Calls Qt's 'int QItemSelectionRange::top() const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselectionrange.html#top
    """
    #  int QItemSelectionRange::top() const
    return self.uglySide.call('ritual_ZNK19QItemSelectionRange3topEv')

  def left(self) -> int:
    """
    Calls Qt's 'int QItemSelectionRange::left() const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselectionrange.html#left
    """
    #  int QItemSelectionRange::left() const
    return self.uglySide.call('ritual_ZNK19QItemSelectionRange4leftEv')

  def bottom(self) -> int:
    """
    Calls Qt's 'int QItemSelectionRange::bottom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselectionrange.html#bottom
    """
    #  int QItemSelectionRange::bottom() const
    return self.uglySide.call('ritual_ZNK19QItemSelectionRange6bottomEv')

  def right(self) -> int:
    """
    Calls Qt's 'int QItemSelectionRange::right() const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselectionrange.html#right
    """
    #  int QItemSelectionRange::right() const
    return self.uglySide.call('ritual_ZNK19QItemSelectionRange5rightEv')

  def width(self) -> int:
    """
    Calls Qt's 'int QItemSelectionRange::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselectionrange.html#width
    """
    #  int QItemSelectionRange::width() const
    return self.uglySide.call('ritual_ZNK19QItemSelectionRange5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QItemSelectionRange::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselectionrange.html#height
    """
    #  int QItemSelectionRange::height() const
    return self.uglySide.call('ritual_ZNK19QItemSelectionRange6heightEv')

  def topLeft(self) -> QPersistentModelIndex:
    """
    Calls Qt's 'const QPersistentModelIndex &QItemSelectionRange::topLeft()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselectionrange.html#topLeft

    Returns
    -------

    QPersistentModelIndex
      A new cute QPersistentModelIndex around the copy Qt gave back. Python
      owns it.
    """
    #  const QPersistentModelIndex &QItemSelectionRange::topLeft() const
    address = self.uglySide.call('ritual_ZNK19QItemSelectionRange7topLeftEv')
    from . import QPersistentModelIndex
    return QPersistentModelIndex._cuteOwning(address)

  def bottomRight(self) -> QPersistentModelIndex:
    """
    Calls Qt's 'const QPersistentModelIndex
    &QItemSelectionRange::bottomRight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionrange.html#bottomRight

    Returns
    -------

    QPersistentModelIndex
      A new cute QPersistentModelIndex around the copy Qt gave back. Python
      owns it.
    """
    #  const QPersistentModelIndex &QItemSelectionRange::bottomRight() const
    address = self.uglySide.call(
        'ritual_ZNK19QItemSelectionRange11bottomRightEv',
    )
    from . import QPersistentModelIndex
    return QPersistentModelIndex._cuteOwning(address)

  def parent(self) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QItemSelectionRange::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselectionrange.html#parent

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QItemSelectionRange::parent() const
    address = self.uglySide.call('ritual_ZNK19QItemSelectionRange6parentEv')
    from . import QModelIndex
    return QModelIndex._cuteOwning(address)

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'const QAbstractItemModel *QItemSelectionRange::model()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselectionrange.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QAbstractItemModel *QItemSelectionRange::model() const
    address = self.uglySide.call('ritual_ZNK19QItemSelectionRange5modelEv')
    from . import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  @overload(QModelIndex)
  def contains(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QItemSelectionRange::contains(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselectionrange.html#contains

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QItemSelectionRange::contains(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK19QItemSelectionRange8containsERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(int, int, QModelIndex)
  def contains(
      self,
      row: int,
      column: int,
      parentIndex: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool QItemSelectionRange::contains(int row, int column, const
    QModelIndex &parentIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselectionrange.html#contains

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    parentIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QItemSelectionRange::contains(int row, int column, const
    #      QModelIndex &parentIndex) const
    return self.uglySide.call(
        'ritual_ZNK19QItemSelectionRange8containsEiiRK11QModelIndex',
        row, column, self._valueOf(parentIndex),
    )

  @overload(THIS)
  def intersects(self, other: QItemSelectionRange) -> bool:
    """
    Calls Qt's 'bool QItemSelectionRange::intersects(const
    QItemSelectionRange &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionrange.html#intersects

    Parameters
    ----------

    other : QItemSelectionRange
      Passed on as a value: Qt reads the C++ QItemSelectionRange, which stays
      Python's own.
    """
    #  bool QItemSelectionRange::intersects(const QItemSelectionRange &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QItemSelectionRange10intersectsERKS_',
        self._valueOf(other),
    )

  @overload(THIS)
  def intersected(self, other: QItemSelectionRange) -> QItemSelectionRange:
    """
    Calls Qt's 'QItemSelectionRange QItemSelectionRange::intersected(const
    QItemSelectionRange &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionrange.html#intersected

    Parameters
    ----------

    other : QItemSelectionRange
      Passed on as a value: Qt reads the C++ QItemSelectionRange, which stays
      Python's own.

    Returns
    -------

    QItemSelectionRange
      A new cute QItemSelectionRange around the copy Qt gave back. Python
      owns it.
    """
    #  QItemSelectionRange QItemSelectionRange::intersected(const
    #      QItemSelectionRange &other) const
    address = self.uglySide.call(
        'ritual_ZNK19QItemSelectionRange11intersectedERKS_',
        self._valueOf(other),
    )
    return QItemSelectionRange._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QItemSelectionRange::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselectionrange.html#isValid
    """
    #  bool QItemSelectionRange::isValid() const
    return self.uglySide.call('ritual_ZNK19QItemSelectionRange7isValidEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QItemSelectionRange::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qitemselectionrange.html#isEmpty
    """
    #  bool QItemSelectionRange::isEmpty() const
    return self.uglySide.call('ritual_ZNK19QItemSelectionRange7isEmptyEv')

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QItemSelectionRange::QItemSelectionRange()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionrange.html#QItemSelectionRange
    """
    #  QItemSelectionRange::QItemSelectionRange()
    self._noteCreation(QItemSelectionRange, lambda: Rituals.call(
        'ritual_ZN19QItemSelectionRangeC1Ev',
    ))

  @overload(QModelIndex, QModelIndex)
  def __init__(self, topL: QModelIndex, bottomR: QModelIndex) -> None:
    """
    Notes what was given, for Qt's
    'QItemSelectionRange::QItemSelectionRange(const QModelIndex &topL, const
    QModelIndex &bottomR)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionrange.html#QItemSelectionRange

    Parameters
    ----------

    topL : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    bottomR : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  QItemSelectionRange::QItemSelectionRange(const QModelIndex &topL,
    #      const QModelIndex &bottomR)
    self._noteCreation(QItemSelectionRange, lambda: Rituals.call(
        'ritual_ZN19QItemSelectionRangeC1ERK11QModelIndexS2_',
        self._valueOf(topL), self._valueOf(bottomR),
    ))

  @overload(QModelIndex)
  def __init__(self, index: QModelIndex) -> None:
    """
    Notes what was given, for Qt's
    'QItemSelectionRange::QItemSelectionRange(const QModelIndex &index)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemselectionrange.html#QItemSelectionRange

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  QItemSelectionRange::QItemSelectionRange(const QModelIndex &index)
    self._noteCreation(QItemSelectionRange, lambda: Rituals.call(
        'ritual_ZN19QItemSelectionRangeC1ERK11QModelIndex',
        self._valueOf(index),
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
