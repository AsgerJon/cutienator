"""
QCandlestickModelMapperPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qcandlestickmodelmapper_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QCandlestickModelMapperPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QModelIndex
  from . import QCandlestickModelMapper, QCandlestickSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCandlestickModelMapper = WAIT['QCandlestickModelMapper']
  QCandlestickSet = WAIT['QCandlestickSet']
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCandlestickModelMapperPrivate(QObject):
  """
  The cute side of Qt's QCandlestickModelMapperPrivate: a plain Python object
  standing in front of one C++ QCandlestickModelMapperPrivate.

  It is built on the cute 'QObject', as Qt's QCandlestickModelMapperPrivate
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCandlestickModelMapperPrivate that has a ritual and
  that Python can call so far, 28 names in all: 'metaObject', 'tr',
  'timestampChanged', 'openChanged', 'highChanged', 'lowChanged',
  'closeChanged', 'firstSetSectionChanged', 'lastSetSectionChanged',
  'initializeCandlestickFromModel', 'modelDataUpdated',
  'modelHeaderDataUpdated', 'modelRowsInserted', 'modelRowsRemoved',
  'modelColumnsInserted', 'modelColumnsRemoved', 'modelDestroyed',
  'candlestickSetsAdded', 'candlestickSetsRemoved', 'candlestickSetChanged',
  'seriesDestroyed', 'candlestickSet', 'candlestickModelIndex', 'insertData',
  'removeData', 'blockModelSignals', 'blockSeriesSignals', 'q_func'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCandlestickModelMapperPrivate::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QCandlestickModelMapperPrivate::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QCandlestickModelMapper
    *QCandlestickModelMapperPrivate::q_func() const': takes in Python what
    'QCandlestickModelMapper *QCandlestickModelMapperPrivate::q_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 34 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QCandlestickModelMapperPrivate is created at the first use, not
    by 'QCandlestickModelMapperPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCandlestickModelMapperPrivate.
  - Qt tells when it has removed the C++ QCandlestickModelMapperPrivate.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QCandlestickModelMapperPrivate::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html#tr

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
    #  QString QCandlestickModelMapperPrivate::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN30QCandlestickModelMapperPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCandlestickModelMapperPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QCandlestickModelMapperPrivate::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCandlestickModelMapperPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK30QCandlestickModelMapperPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(QCandlestickModelMapper)
  @overload(NoneType)
  def __init__(self, q: Optional[QCandlestickModelMapper]) -> None:
    """
    Notes what was given, for Qt's
    'QCandlestickModelMapperPrivate::QCandlestickModelMapperPrivate(
    QCandlestickModelMapper *q)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html

    Parameters
    ----------

    q : Optional[QCandlestickModelMapper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QCandlestickModelMapperPrivate::QCandlestickModelMapperPrivate(
    #      QCandlestickModelMapper *q)
    self._noteCreation(QCandlestickModelMapperPrivate, lambda: Rituals.call(
        'ritual_ZN30QCandlestickModelMapperPrivateC1EP23QCandlestickModelMa'
        'pper',
        self._addressOf(q),
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

  def timestampChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickModelMapperPrivate::timestampChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html
    """
    #  void QCandlestickModelMapperPrivate::timestampChanged()
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate16timestampChangedEv',
    )

  def openChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickModelMapperPrivate::openChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html#openChanged
    """
    #  void QCandlestickModelMapperPrivate::openChanged()
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate11openChangedEv',
    )

  def highChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickModelMapperPrivate::highChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html#highChanged
    """
    #  void QCandlestickModelMapperPrivate::highChanged()
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate11highChangedEv',
    )

  def lowChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickModelMapperPrivate::lowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html#lowChanged
    """
    #  void QCandlestickModelMapperPrivate::lowChanged()
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate10lowChangedEv',
    )

  def closeChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickModelMapperPrivate::closeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html#closeChanged
    """
    #  void QCandlestickModelMapperPrivate::closeChanged()
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate12closeChangedEv',
    )

  def firstSetSectionChanged(self) -> None:
    """
    Calls Qt's 'void
    QCandlestickModelMapperPrivate::firstSetSectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html
    """
    #  void QCandlestickModelMapperPrivate::firstSetSectionChanged()
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate22firstSetSectionChangedE'
        'v',
    )

  def lastSetSectionChanged(self) -> None:
    """
    Calls Qt's 'void
    QCandlestickModelMapperPrivate::lastSetSectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html
    """
    #  void QCandlestickModelMapperPrivate::lastSetSectionChanged()
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate21lastSetSectionChangedEv',
    )

  def initializeCandlestickFromModel(self) -> None:
    """
    Calls Qt's 'void
    QCandlestickModelMapperPrivate::initializeCandlestickFromModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html
    """
    #  void QCandlestickModelMapperPrivate::initializeCandlestickFromModel()
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate30initializeCandlestickFr'
        'omModelEv',
    )

  @overload(QModelIndex, QModelIndex)
  def modelDataUpdated(
      self,
      topLeft: QModelIndex,
      bottomRight: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void
    QCandlestickModelMapperPrivate::modelDataUpdated(QModelIndex topLeft,
    QModelIndex bottomRight)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html

    Parameters
    ----------

    topLeft : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    bottomRight : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QCandlestickModelMapperPrivate::modelDataUpdated(QModelIndex
    #      topLeft, QModelIndex bottomRight)
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate16modelDataUpdatedE11QMod'
        'elIndexS0_',
        self._valueOf(topLeft), self._valueOf(bottomRight),
    )

  @overload(Qt.Orientation, int, int)
  def modelHeaderDataUpdated(
      self,
      orientation: Qt.Orientation,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void
    QCandlestickModelMapperPrivate::modelHeaderDataUpdated(Qt::Orientation
    orientation, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QCandlestickModelMapperPrivate::modelHeaderDataUpdated(Qt::
    #      Orientation orientation, int first, int last)
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate22modelHeaderDataUpdatedE'
        'N2Qt11OrientationEii',
        orientation.value, first, last,
    )

  @overload(QModelIndex, int, int)
  def modelRowsInserted(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QCandlestickModelMapperPrivate::modelRowsInserted(QModelIndex parent, int
    start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QCandlestickModelMapperPrivate::modelRowsInserted(QModelIndex
    #      parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate17modelRowsInsertedE11QMo'
        'delIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def modelRowsRemoved(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QCandlestickModelMapperPrivate::modelRowsRemoved(QModelIndex parent, int
    start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QCandlestickModelMapperPrivate::modelRowsRemoved(QModelIndex
    #      parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate16modelRowsRemovedE11QMod'
        'elIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def modelColumnsInserted(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QCandlestickModelMapperPrivate::modelColumnsInserted(QModelIndex parent,
    int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QCandlestickModelMapperPrivate::modelColumnsInserted(QModelIndex
    #      parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate20modelColumnsInsertedE11'
        'QModelIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def modelColumnsRemoved(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void
    QCandlestickModelMapperPrivate::modelColumnsRemoved(QModelIndex parent,
    int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QCandlestickModelMapperPrivate::modelColumnsRemoved(QModelIndex
    #      parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate19modelColumnsRemovedE11Q'
        'ModelIndexii',
        self._valueOf(parent), start, end,
    )

  def modelDestroyed(self) -> None:
    """
    Calls Qt's 'void QCandlestickModelMapperPrivate::modelDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html#modelDestroyed
    """
    #  void QCandlestickModelMapperPrivate::modelDestroyed()
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate14modelDestroyedEv',
    )

  @overload(QList[QCandlestickSet])
  def candlestickSetsAdded(self, sets: QList[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void
    QCandlestickModelMapperPrivate::candlestickSetsAdded(const
    QList<QCandlestickSet *> &sets)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html

    Parameters
    ----------

    sets : QList[QCandlestickSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QCandlestickModelMapperPrivate::candlestickSetsAdded(const
    #      QList<QCandlestickSet *> &sets)
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate20candlestickSetsAddedERK'
        '5QListIP15QCandlestickSetE',
        self._valueOf(sets),
    )

  @overload(QList[QCandlestickSet])
  def candlestickSetsRemoved(self, sets: QList[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void
    QCandlestickModelMapperPrivate::candlestickSetsRemoved(const
    QList<QCandlestickSet *> &sets)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html

    Parameters
    ----------

    sets : QList[QCandlestickSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QCandlestickModelMapperPrivate::candlestickSetsRemoved(const
    #      QList<QCandlestickSet *> &sets)
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate22candlestickSetsRemovedE'
        'RK5QListIP15QCandlestickSetE',
        self._valueOf(sets),
    )

  def candlestickSetChanged(self) -> None:
    """
    Calls Qt's 'void
    QCandlestickModelMapperPrivate::candlestickSetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html
    """
    #  void QCandlestickModelMapperPrivate::candlestickSetChanged()
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate21candlestickSetChangedEv',
    )

  def seriesDestroyed(self) -> None:
    """
    Calls Qt's 'void QCandlestickModelMapperPrivate::seriesDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html
    """
    #  void QCandlestickModelMapperPrivate::seriesDestroyed()
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate15seriesDestroyedEv',
    )

  @overload(QModelIndex)
  def candlestickSet(self, index: QModelIndex) -> Optional[QCandlestickSet]:
    """
    Calls Qt's 'QCandlestickSet
    *QCandlestickModelMapperPrivate::candlestickSet(QModelIndex index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html#candlestickSet

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QCandlestickSet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCandlestickSet
    #      *QCandlestickModelMapperPrivate::candlestickSet(QModelIndex index)
    address = self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate14candlestickSetE11QModel'
        'Index',
        self._valueOf(index),
    )
    from . import QCandlestickSet
    return QCandlestickSet._cuteAt(address)

  @overload(int, int)
  def candlestickModelIndex(self, section: int, pos: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex
    QCandlestickModelMapperPrivate::candlestickModelIndex(int section, int
    pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html

    Parameters
    ----------

    section : int
      Passed on as it is.

    pos : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QCandlestickModelMapperPrivate::candlestickModelIndex(int
    #      section, int pos)
    address = self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate21candlestickModelIndexEi'
        'i',
        section, pos,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int, int)
  def insertData(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QCandlestickModelMapperPrivate::insertData(int start,
    int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html#insertData

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QCandlestickModelMapperPrivate::insertData(int start, int end)
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate10insertDataEii',
        start, end,
    )

  @overload(int, int)
  def removeData(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QCandlestickModelMapperPrivate::removeData(int start,
    int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html#removeData

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QCandlestickModelMapperPrivate::removeData(int start, int end)
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate10removeDataEii',
        start, end,
    )

  @overload()
  @overload(bool)
  def blockModelSignals(self, block: bool = True) -> None:
    """
    Calls Qt's 'void QCandlestickModelMapperPrivate::blockModelSignals(bool
    block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html

    Parameters
    ----------

    block : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QCandlestickModelMapperPrivate::blockModelSignals(bool block)
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate17blockModelSignalsEb',
        block,
    )

  @overload()
  @overload(bool)
  def blockSeriesSignals(self, block: bool = True) -> None:
    """
    Calls Qt's 'void QCandlestickModelMapperPrivate::blockSeriesSignals(bool
    block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html

    Parameters
    ----------

    block : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QCandlestickModelMapperPrivate::blockSeriesSignals(bool block)
    self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate18blockSeriesSignalsEb',
        block,
    )

  def q_func(self) -> Optional[QCandlestickModelMapper]:
    """
    Calls Qt's 'QCandlestickModelMapper
    *QCandlestickModelMapperPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickmodelmapperprivate.html#q_func

    Returns
    -------

    Optional[QCandlestickModelMapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCandlestickModelMapper *QCandlestickModelMapperPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN30QCandlestickModelMapperPrivate6q_funcEv',
    )
    from . import QCandlestickModelMapper
    return QCandlestickModelMapper._cuteAt(address)
