"""
QHCandlestickModelMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qhcandlestickmodelmapper.h, Qt 6.12.0. Changes made here are
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


class QHCandlestickModelMapper(QCandlestickModelMapper):
  """
  The cute side of Qt's QHCandlestickModelMapper: a plain Python object
  standing in front of one C++ QHCandlestickModelMapper.

  It is built on the cute 'QCandlestickModelMapper', as Qt's
  QHCandlestickModelMapper is built on Qt's QCandlestickModelMapper, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QHCandlestickModelMapper that has a ritual and that
  Python can call so far, 24 names in all: 'metaObject', 'tr', 'orientation',
  'setTimestampColumn', 'timestampColumn', 'setOpenColumn', 'openColumn',
  'setHighColumn', 'highColumn', 'setLowColumn', 'lowColumn',
  'setCloseColumn', 'closeColumn', 'setFirstSetRow', 'firstSetRow',
  'setLastSetRow', 'lastSetRow', 'timestampColumnChanged',
  'openColumnChanged', 'highColumnChanged', 'lowColumnChanged',
  'closeColumnChanged', 'firstSetRowChanged', 'lastSetRowChanged'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHCandlestickModelMapper::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QHCandlestickModelMapper::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QHCandlestickModelMapper is created at the first use, not by
    'QHCandlestickModelMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHCandlestickModelMapper.
  - Qt tells when it has removed the C++ QHCandlestickModelMapper. Every call
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
    Calls Qt's 'QString QHCandlestickModelMapper::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#tr

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
    #  QString QHCandlestickModelMapper::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QHCandlestickModelMapper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHCandlestickModelMapper'

  #  A C++ QHCandlestickModelMapper Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHCandlestickModelMapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHCandlestickModelMapper::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHCandlestickModelMapper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QHCandlestickModelMapper10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QHCandlestickModelMapper::orientation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QHCandlestickModelMapper::orientation() const
    ritual = 'ritual_ZNK24QHCandlestickModelMapper11orientationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QHCandlestickModelMapper11orientationEv'
    return Qt.Orientation(self.uglySide.call(ritual))

  def timestampColumn(self) -> int:
    """
    Calls Qt's 'int QHCandlestickModelMapper::timestampColumn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#timestampColumn
    """
    #  int QHCandlestickModelMapper::timestampColumn() const
    return self.uglySide.call(
        'ritual_ZNK24QHCandlestickModelMapper15timestampColumnEv',
    )

  def openColumn(self) -> int:
    """
    Calls Qt's 'int QHCandlestickModelMapper::openColumn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#openColumn
    """
    #  int QHCandlestickModelMapper::openColumn() const
    return self.uglySide.call(
        'ritual_ZNK24QHCandlestickModelMapper10openColumnEv',
    )

  def highColumn(self) -> int:
    """
    Calls Qt's 'int QHCandlestickModelMapper::highColumn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#highColumn
    """
    #  int QHCandlestickModelMapper::highColumn() const
    return self.uglySide.call(
        'ritual_ZNK24QHCandlestickModelMapper10highColumnEv',
    )

  def lowColumn(self) -> int:
    """
    Calls Qt's 'int QHCandlestickModelMapper::lowColumn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#lowColumn
    """
    #  int QHCandlestickModelMapper::lowColumn() const
    return self.uglySide.call(
        'ritual_ZNK24QHCandlestickModelMapper9lowColumnEv',
    )

  def closeColumn(self) -> int:
    """
    Calls Qt's 'int QHCandlestickModelMapper::closeColumn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#closeColumn
    """
    #  int QHCandlestickModelMapper::closeColumn() const
    return self.uglySide.call(
        'ritual_ZNK24QHCandlestickModelMapper11closeColumnEv',
    )

  def firstSetRow(self) -> int:
    """
    Calls Qt's 'int QHCandlestickModelMapper::firstSetRow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#firstSetRow
    """
    #  int QHCandlestickModelMapper::firstSetRow() const
    return self.uglySide.call(
        'ritual_ZNK24QHCandlestickModelMapper11firstSetRowEv',
    )

  def lastSetRow(self) -> int:
    """
    Calls Qt's 'int QHCandlestickModelMapper::lastSetRow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#lastSetRow
    """
    #  int QHCandlestickModelMapper::lastSetRow() const
    return self.uglySide.call(
        'ritual_ZNK24QHCandlestickModelMapper10lastSetRowEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setTimestampColumn(self, timestampColumn: int) -> None:
    """
    Calls Qt's 'void QHCandlestickModelMapper::setTimestampColumn(int
    timestampColumn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#setTimestampColumn

    Parameters
    ----------

    timestampColumn : int
      Passed on as it is.
    """
    #  void QHCandlestickModelMapper::setTimestampColumn(int timestampColumn)
    self.uglySide.call(
        'ritual_ZN24QHCandlestickModelMapper18setTimestampColumnEi',
        timestampColumn,
    )

  @overload(int)
  def setOpenColumn(self, openColumn: int) -> None:
    """
    Calls Qt's 'void QHCandlestickModelMapper::setOpenColumn(int
    openColumn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#setOpenColumn

    Parameters
    ----------

    openColumn : int
      Passed on as it is.
    """
    #  void QHCandlestickModelMapper::setOpenColumn(int openColumn)
    self.uglySide.call(
        'ritual_ZN24QHCandlestickModelMapper13setOpenColumnEi', openColumn,
    )

  @overload(int)
  def setHighColumn(self, highColumn: int) -> None:
    """
    Calls Qt's 'void QHCandlestickModelMapper::setHighColumn(int
    highColumn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#setHighColumn

    Parameters
    ----------

    highColumn : int
      Passed on as it is.
    """
    #  void QHCandlestickModelMapper::setHighColumn(int highColumn)
    self.uglySide.call(
        'ritual_ZN24QHCandlestickModelMapper13setHighColumnEi', highColumn,
    )

  @overload(int)
  def setLowColumn(self, lowColumn: int) -> None:
    """
    Calls Qt's 'void QHCandlestickModelMapper::setLowColumn(int lowColumn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#setLowColumn

    Parameters
    ----------

    lowColumn : int
      Passed on as it is.
    """
    #  void QHCandlestickModelMapper::setLowColumn(int lowColumn)
    self.uglySide.call(
        'ritual_ZN24QHCandlestickModelMapper12setLowColumnEi', lowColumn,
    )

  @overload(int)
  def setCloseColumn(self, closeColumn: int) -> None:
    """
    Calls Qt's 'void QHCandlestickModelMapper::setCloseColumn(int
    closeColumn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#setCloseColumn

    Parameters
    ----------

    closeColumn : int
      Passed on as it is.
    """
    #  void QHCandlestickModelMapper::setCloseColumn(int closeColumn)
    self.uglySide.call(
        'ritual_ZN24QHCandlestickModelMapper14setCloseColumnEi', closeColumn,
    )

  @overload(int)
  def setFirstSetRow(self, firstSetRow: int) -> None:
    """
    Calls Qt's 'void QHCandlestickModelMapper::setFirstSetRow(int
    firstSetRow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#setFirstSetRow

    Parameters
    ----------

    firstSetRow : int
      Passed on as it is.
    """
    #  void QHCandlestickModelMapper::setFirstSetRow(int firstSetRow)
    self.uglySide.call(
        'ritual_ZN24QHCandlestickModelMapper14setFirstSetRowEi', firstSetRow,
    )

  @overload(int)
  def setLastSetRow(self, lastSetRow: int) -> None:
    """
    Calls Qt's 'void QHCandlestickModelMapper::setLastSetRow(int
    lastSetRow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#setLastSetRow

    Parameters
    ----------

    lastSetRow : int
      Passed on as it is.
    """
    #  void QHCandlestickModelMapper::setLastSetRow(int lastSetRow)
    self.uglySide.call(
        'ritual_ZN24QHCandlestickModelMapper13setLastSetRowEi', lastSetRow,
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
    'QHCandlestickModelMapper::QHCandlestickModelMapper(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHCandlestickModelMapper::QHCandlestickModelMapper(QObject *parent)
    self._noteCreation(QHCandlestickModelMapper, lambda: Rituals.call(
        'ritual_ZN24QHCandlestickModelMapperC1EP7QObject',
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

  def timestampColumnChanged(self) -> None:
    """
    Calls Qt's 'void QHCandlestickModelMapper::timestampColumnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html
    """
    #  void QHCandlestickModelMapper::timestampColumnChanged()
    self.uglySide.call(
        'ritual_ZN24QHCandlestickModelMapper22timestampColumnChangedEv',
    )

  def openColumnChanged(self) -> None:
    """
    Calls Qt's 'void QHCandlestickModelMapper::openColumnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#openColumnChanged
    """
    #  void QHCandlestickModelMapper::openColumnChanged()
    self.uglySide.call(
        'ritual_ZN24QHCandlestickModelMapper17openColumnChangedEv',
    )

  def highColumnChanged(self) -> None:
    """
    Calls Qt's 'void QHCandlestickModelMapper::highColumnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#highColumnChanged
    """
    #  void QHCandlestickModelMapper::highColumnChanged()
    self.uglySide.call(
        'ritual_ZN24QHCandlestickModelMapper17highColumnChangedEv',
    )

  def lowColumnChanged(self) -> None:
    """
    Calls Qt's 'void QHCandlestickModelMapper::lowColumnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#lowColumnChanged
    """
    #  void QHCandlestickModelMapper::lowColumnChanged()
    self.uglySide.call(
        'ritual_ZN24QHCandlestickModelMapper16lowColumnChangedEv',
    )

  def closeColumnChanged(self) -> None:
    """
    Calls Qt's 'void QHCandlestickModelMapper::closeColumnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#closeColumnChanged
    """
    #  void QHCandlestickModelMapper::closeColumnChanged()
    self.uglySide.call(
        'ritual_ZN24QHCandlestickModelMapper18closeColumnChangedEv',
    )

  def firstSetRowChanged(self) -> None:
    """
    Calls Qt's 'void QHCandlestickModelMapper::firstSetRowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#firstSetRowChanged
    """
    #  void QHCandlestickModelMapper::firstSetRowChanged()
    self.uglySide.call(
        'ritual_ZN24QHCandlestickModelMapper18firstSetRowChangedEv',
    )

  def lastSetRowChanged(self) -> None:
    """
    Calls Qt's 'void QHCandlestickModelMapper::lastSetRowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhcandlestickmodelmapper.html#lastSetRowChanged
    """
    #  void QHCandlestickModelMapper::lastSetRowChanged()
    self.uglySide.call(
        'ritual_ZN24QHCandlestickModelMapper17lastSetRowChangedEv',
    )
