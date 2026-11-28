"""
QVCandlestickModelMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qvcandlestickmodelmapper.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QCandlestickModelMapper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVCandlestickModelMapper(QCandlestickModelMapper):
  """
  The cute side of Qt's QVCandlestickModelMapper: a plain Python object
  standing in front of one C++ QVCandlestickModelMapper.

  It is built on the cute 'QCandlestickModelMapper', as Qt's
  QVCandlestickModelMapper is built on Qt's QCandlestickModelMapper, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QVCandlestickModelMapper that has a ritual and that
  Python can call so far, 24 names in all: 'metaObject', 'tr', 'orientation',
  'setTimestampRow', 'timestampRow', 'setOpenRow', 'openRow', 'setHighRow',
  'highRow', 'setLowRow', 'lowRow', 'setCloseRow', 'closeRow',
  'setFirstSetColumn', 'firstSetColumn', 'setLastSetColumn', 'lastSetColumn',
  'timestampRowChanged', 'openRowChanged', 'highRowChanged', 'lowRowChanged',
  'closeRowChanged', 'firstSetColumnChanged', 'lastSetColumnChanged'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QVCandlestickModelMapper::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QVCandlestickModelMapper::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QVCandlestickModelMapper is created at the first use, not by
    'QVCandlestickModelMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVCandlestickModelMapper.
  - Qt tells when it has removed the C++ QVCandlestickModelMapper. Every call
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
    Calls Qt's 'QString QVCandlestickModelMapper::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#tr

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
    #  QString QVCandlestickModelMapper::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QVCandlestickModelMapper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVCandlestickModelMapper'

  #  A C++ QVCandlestickModelMapper Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVCandlestickModelMapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QVCandlestickModelMapper::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QVCandlestickModelMapper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QVCandlestickModelMapper10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QVCandlestickModelMapper::orientation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QVCandlestickModelMapper::orientation() const
    ritual = 'ritual_ZNK24QVCandlestickModelMapper11orientationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QVCandlestickModelMapper11orientationEv'
    return Qt.Orientation(self.uglySide.call(ritual))

  def timestampRow(self) -> int:
    """
    Calls Qt's 'int QVCandlestickModelMapper::timestampRow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#timestampRow
    """
    #  int QVCandlestickModelMapper::timestampRow() const
    return self.uglySide.call(
        'ritual_ZNK24QVCandlestickModelMapper12timestampRowEv',
    )

  def openRow(self) -> int:
    """
    Calls Qt's 'int QVCandlestickModelMapper::openRow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#openRow
    """
    #  int QVCandlestickModelMapper::openRow() const
    return self.uglySide.call(
        'ritual_ZNK24QVCandlestickModelMapper7openRowEv',
    )

  def highRow(self) -> int:
    """
    Calls Qt's 'int QVCandlestickModelMapper::highRow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#highRow
    """
    #  int QVCandlestickModelMapper::highRow() const
    return self.uglySide.call(
        'ritual_ZNK24QVCandlestickModelMapper7highRowEv',
    )

  def lowRow(self) -> int:
    """
    Calls Qt's 'int QVCandlestickModelMapper::lowRow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#lowRow
    """
    #  int QVCandlestickModelMapper::lowRow() const
    return self.uglySide.call(
        'ritual_ZNK24QVCandlestickModelMapper6lowRowEv',
    )

  def closeRow(self) -> int:
    """
    Calls Qt's 'int QVCandlestickModelMapper::closeRow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#closeRow
    """
    #  int QVCandlestickModelMapper::closeRow() const
    return self.uglySide.call(
        'ritual_ZNK24QVCandlestickModelMapper8closeRowEv',
    )

  def firstSetColumn(self) -> int:
    """
    Calls Qt's 'int QVCandlestickModelMapper::firstSetColumn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#firstSetColumn
    """
    #  int QVCandlestickModelMapper::firstSetColumn() const
    return self.uglySide.call(
        'ritual_ZNK24QVCandlestickModelMapper14firstSetColumnEv',
    )

  def lastSetColumn(self) -> int:
    """
    Calls Qt's 'int QVCandlestickModelMapper::lastSetColumn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#lastSetColumn
    """
    #  int QVCandlestickModelMapper::lastSetColumn() const
    return self.uglySide.call(
        'ritual_ZNK24QVCandlestickModelMapper13lastSetColumnEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setTimestampRow(self, timestampRow: int) -> None:
    """
    Calls Qt's 'void QVCandlestickModelMapper::setTimestampRow(int
    timestampRow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#setTimestampRow

    Parameters
    ----------

    timestampRow : int
      Passed on as it is.
    """
    #  void QVCandlestickModelMapper::setTimestampRow(int timestampRow)
    self.uglySide.call(
        'ritual_ZN24QVCandlestickModelMapper15setTimestampRowEi',
        timestampRow,
    )

  @overload(int)
  def setOpenRow(self, openRow: int) -> None:
    """
    Calls Qt's 'void QVCandlestickModelMapper::setOpenRow(int openRow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#setOpenRow

    Parameters
    ----------

    openRow : int
      Passed on as it is.
    """
    #  void QVCandlestickModelMapper::setOpenRow(int openRow)
    self.uglySide.call(
        'ritual_ZN24QVCandlestickModelMapper10setOpenRowEi', openRow,
    )

  @overload(int)
  def setHighRow(self, highRow: int) -> None:
    """
    Calls Qt's 'void QVCandlestickModelMapper::setHighRow(int highRow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#setHighRow

    Parameters
    ----------

    highRow : int
      Passed on as it is.
    """
    #  void QVCandlestickModelMapper::setHighRow(int highRow)
    self.uglySide.call(
        'ritual_ZN24QVCandlestickModelMapper10setHighRowEi', highRow,
    )

  @overload(int)
  def setLowRow(self, lowRow: int) -> None:
    """
    Calls Qt's 'void QVCandlestickModelMapper::setLowRow(int lowRow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#setLowRow

    Parameters
    ----------

    lowRow : int
      Passed on as it is.
    """
    #  void QVCandlestickModelMapper::setLowRow(int lowRow)
    self.uglySide.call(
        'ritual_ZN24QVCandlestickModelMapper9setLowRowEi', lowRow,
    )

  @overload(int)
  def setCloseRow(self, closeRow: int) -> None:
    """
    Calls Qt's 'void QVCandlestickModelMapper::setCloseRow(int closeRow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#setCloseRow

    Parameters
    ----------

    closeRow : int
      Passed on as it is.
    """
    #  void QVCandlestickModelMapper::setCloseRow(int closeRow)
    self.uglySide.call(
        'ritual_ZN24QVCandlestickModelMapper11setCloseRowEi', closeRow,
    )

  @overload(int)
  def setFirstSetColumn(self, firstSetColumn: int) -> None:
    """
    Calls Qt's 'void QVCandlestickModelMapper::setFirstSetColumn(int
    firstSetColumn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#setFirstSetColumn

    Parameters
    ----------

    firstSetColumn : int
      Passed on as it is.
    """
    #  void QVCandlestickModelMapper::setFirstSetColumn(int firstSetColumn)
    self.uglySide.call(
        'ritual_ZN24QVCandlestickModelMapper17setFirstSetColumnEi',
        firstSetColumn,
    )

  @overload(int)
  def setLastSetColumn(self, lastSetColumn: int) -> None:
    """
    Calls Qt's 'void QVCandlestickModelMapper::setLastSetColumn(int
    lastSetColumn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#setLastSetColumn

    Parameters
    ----------

    lastSetColumn : int
      Passed on as it is.
    """
    #  void QVCandlestickModelMapper::setLastSetColumn(int lastSetColumn)
    self.uglySide.call(
        'ritual_ZN24QVCandlestickModelMapper16setLastSetColumnEi',
        lastSetColumn,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QVCandlestickModelMapper::QVCandlestickModelMapper(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QVCandlestickModelMapper::QVCandlestickModelMapper(QObject *parent)
    self._noteCreation(QVCandlestickModelMapper, lambda: Rituals.call(
        'ritual_ZN24QVCandlestickModelMapperC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def timestampRowChanged(self) -> None:
    """
    Calls Qt's 'void QVCandlestickModelMapper::timestampRowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#timestampRowChanged
    """
    #  void QVCandlestickModelMapper::timestampRowChanged()
    self.uglySide.call(
        'ritual_ZN24QVCandlestickModelMapper19timestampRowChangedEv',
    )

  def openRowChanged(self) -> None:
    """
    Calls Qt's 'void QVCandlestickModelMapper::openRowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#openRowChanged
    """
    #  void QVCandlestickModelMapper::openRowChanged()
    self.uglySide.call(
        'ritual_ZN24QVCandlestickModelMapper14openRowChangedEv',
    )

  def highRowChanged(self) -> None:
    """
    Calls Qt's 'void QVCandlestickModelMapper::highRowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#highRowChanged
    """
    #  void QVCandlestickModelMapper::highRowChanged()
    self.uglySide.call(
        'ritual_ZN24QVCandlestickModelMapper14highRowChangedEv',
    )

  def lowRowChanged(self) -> None:
    """
    Calls Qt's 'void QVCandlestickModelMapper::lowRowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#lowRowChanged
    """
    #  void QVCandlestickModelMapper::lowRowChanged()
    self.uglySide.call(
        'ritual_ZN24QVCandlestickModelMapper13lowRowChangedEv',
    )

  def closeRowChanged(self) -> None:
    """
    Calls Qt's 'void QVCandlestickModelMapper::closeRowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#closeRowChanged
    """
    #  void QVCandlestickModelMapper::closeRowChanged()
    self.uglySide.call(
        'ritual_ZN24QVCandlestickModelMapper15closeRowChangedEv',
    )

  def firstSetColumnChanged(self) -> None:
    """
    Calls Qt's 'void QVCandlestickModelMapper::firstSetColumnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html
    """
    #  void QVCandlestickModelMapper::firstSetColumnChanged()
    self.uglySide.call(
        'ritual_ZN24QVCandlestickModelMapper21firstSetColumnChangedEv',
    )

  def lastSetColumnChanged(self) -> None:
    """
    Calls Qt's 'void QVCandlestickModelMapper::lastSetColumnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvcandlestickmodelmapper.html#lastSetColumnChanged
    """
    #  void QVCandlestickModelMapper::lastSetColumnChanged()
    self.uglySide.call(
        'ritual_ZN24QVCandlestickModelMapper20lastSetColumnChangedEv',
    )
