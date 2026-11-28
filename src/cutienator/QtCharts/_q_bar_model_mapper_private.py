"""
QBarModelMapperPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qbarmodelmapper_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QBarModelMapperPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QModelIndex
  from . import QBarModelMapper, QBarSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBarModelMapper = WAIT['QtCharts:QBarModelMapper']
  QBarSet = WAIT['QtCharts:QBarSet']
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBarModelMapperPrivate(QObject):
  """
  The cute side of Qt's QBarModelMapperPrivate: a plain Python object
  standing in front of one C++ QBarModelMapperPrivate.

  It is built on the cute 'QObject', as Qt's QBarModelMapperPrivate is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBarModelMapperPrivate that has a ritual and that
  Python can call so far, 24 names in all: 'metaObject', 'tr',
  'modelUpdated', 'modelHeaderDataUpdated', 'modelRowsAdded',
  'modelRowsRemoved', 'modelColumnsAdded', 'modelColumnsRemoved',
  'handleModelDestroyed', 'barSetsAdded', 'barSetsRemoved', 'valuesAdded',
  'valuesRemoved', 'barLabelChanged', 'barValueChanged',
  'handleSeriesDestroyed', 'initializeBarFromModel', 'barSet',
  'barModelIndex', 'insertData', 'removeData', 'blockModelSignals',
  'blockSeriesSignals', 'q_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBarModelMapperPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QBarModelMapperPrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QBarModelMapper *QBarModelMapperPrivate::q_func() const':
    takes in Python what 'QBarModelMapper *QBarModelMapperPrivate::q_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 30 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QBarModelMapperPrivate is created at the first use, not by
    'QBarModelMapperPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBarModelMapperPrivate.
  - Qt tells when it has removed the C++ QBarModelMapperPrivate. Every call
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
    Calls Qt's 'QString QBarModelMapperPrivate::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#tr

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
    #  QString QBarModelMapperPrivate::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QBarModelMapperPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBarModelMapperPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtCharts'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBarModelMapperPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBarModelMapperPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QBarModelMapperPrivate10metaObjectEv',
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

  @overload(QBarModelMapper)
  @overload(NoneType)
  def __init__(self, q: Optional[QBarModelMapper]) -> None:
    """
    Notes what was given, for Qt's
    'QBarModelMapperPrivate::QBarModelMapperPrivate(QBarModelMapper *q)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#QBarModelMapperPrivate

    Parameters
    ----------

    q : Optional[QBarModelMapper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QBarModelMapperPrivate::QBarModelMapperPrivate(QBarModelMapper *q)
    self._noteCreation(QBarModelMapperPrivate, lambda: Rituals.call(
        'ritual_ZN22QBarModelMapperPrivateC1EP15QBarModelMapper',
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

  @overload(QModelIndex, QModelIndex)
  def modelUpdated(
      self,
      topLeft: QModelIndex,
      bottomRight: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QBarModelMapperPrivate::modelUpdated(QModelIndex
    topLeft, QModelIndex bottomRight)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#modelUpdated

    Parameters
    ----------

    topLeft : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    bottomRight : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QBarModelMapperPrivate::modelUpdated(QModelIndex topLeft,
    #      QModelIndex bottomRight)
    self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate12modelUpdatedE11QModelIndexS0_',
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
    QBarModelMapperPrivate::modelHeaderDataUpdated(Qt::Orientation
    orientation, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#modelHeaderDataUpdated

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QBarModelMapperPrivate::modelHeaderDataUpdated(Qt::Orientation
    #      orientation, int first, int last)
    self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate22modelHeaderDataUpdatedEN2Qt11Or'
        'ientationEii',
        orientation.value, first, last,
    )

  @overload(QModelIndex, int, int)
  def modelRowsAdded(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QBarModelMapperPrivate::modelRowsAdded(QModelIndex
    parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#modelRowsAdded

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
    #  void QBarModelMapperPrivate::modelRowsAdded(QModelIndex parent, int
    #      start, int end)
    self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate14modelRowsAddedE11QModelIndexii',
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
    Calls Qt's 'void QBarModelMapperPrivate::modelRowsRemoved(QModelIndex
    parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#modelRowsRemoved

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
    #  void QBarModelMapperPrivate::modelRowsRemoved(QModelIndex parent, int
    #      start, int end)
    self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate16modelRowsRemovedE11QModelIndexi'
        'i',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def modelColumnsAdded(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QBarModelMapperPrivate::modelColumnsAdded(QModelIndex
    parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#modelColumnsAdded

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
    #  void QBarModelMapperPrivate::modelColumnsAdded(QModelIndex parent, int
    #      start, int end)
    self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate17modelColumnsAddedE11QModelIndex'
        'ii',
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
    Calls Qt's 'void QBarModelMapperPrivate::modelColumnsRemoved(QModelIndex
    parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#modelColumnsRemoved

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
    #  void QBarModelMapperPrivate::modelColumnsRemoved(QModelIndex parent,
    #      int start, int end)
    self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate19modelColumnsRemovedE11QModelInd'
        'exii',
        self._valueOf(parent), start, end,
    )

  def handleModelDestroyed(self) -> None:
    """
    Calls Qt's 'void QBarModelMapperPrivate::handleModelDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#handleModelDestroyed
    """
    #  void QBarModelMapperPrivate::handleModelDestroyed()
    self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate20handleModelDestroyedEv',
    )

  @overload(QList[QBarSet])
  def barSetsAdded(self, sets: QList[QBarSet]) -> None:
    """
    Calls Qt's 'void QBarModelMapperPrivate::barSetsAdded(const QList<QBarSet
    *> &sets)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#barSetsAdded

    Parameters
    ----------

    sets : QList[QBarSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBarModelMapperPrivate::barSetsAdded(const QList<QBarSet *>
    #      &sets)
    self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate12barSetsAddedERK5QListIP7QBarSet'
        'E',
        self._valueOf(sets),
    )

  @overload(QList[QBarSet])
  def barSetsRemoved(self, sets: QList[QBarSet]) -> None:
    """
    Calls Qt's 'void QBarModelMapperPrivate::barSetsRemoved(const
    QList<QBarSet *> &sets)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#barSetsRemoved

    Parameters
    ----------

    sets : QList[QBarSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBarModelMapperPrivate::barSetsRemoved(const QList<QBarSet *>
    #      &sets)
    self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate14barSetsRemovedERK5QListIP7QBarS'
        'etE',
        self._valueOf(sets),
    )

  @overload(int, int)
  def valuesAdded(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QBarModelMapperPrivate::valuesAdded(int index, int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#valuesAdded

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QBarModelMapperPrivate::valuesAdded(int index, int count)
    self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate11valuesAddedEii', index, count,
    )

  @overload(int, int)
  def valuesRemoved(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QBarModelMapperPrivate::valuesRemoved(int index, int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#valuesRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QBarModelMapperPrivate::valuesRemoved(int index, int count)
    self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate13valuesRemovedEii', index, count,
    )

  def barLabelChanged(self) -> None:
    """
    Calls Qt's 'void QBarModelMapperPrivate::barLabelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#barLabelChanged
    """
    #  void QBarModelMapperPrivate::barLabelChanged()
    self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate15barLabelChangedEv',
    )

  @overload(int)
  def barValueChanged(self, index: int) -> None:
    """
    Calls Qt's 'void QBarModelMapperPrivate::barValueChanged(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#barValueChanged

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QBarModelMapperPrivate::barValueChanged(int index)
    self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate15barValueChangedEi', index,
    )

  def handleSeriesDestroyed(self) -> None:
    """
    Calls Qt's 'void QBarModelMapperPrivate::handleSeriesDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#handleSeriesDestroyed
    """
    #  void QBarModelMapperPrivate::handleSeriesDestroyed()
    self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate21handleSeriesDestroyedEv',
    )

  def initializeBarFromModel(self) -> None:
    """
    Calls Qt's 'void QBarModelMapperPrivate::initializeBarFromModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#initializeBarFromModel
    """
    #  void QBarModelMapperPrivate::initializeBarFromModel()
    self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate22initializeBarFromModelEv',
    )

  @overload(QModelIndex)
  def barSet(self, index: QModelIndex) -> Optional[QBarSet]:
    """
    Calls Qt's 'QBarSet *QBarModelMapperPrivate::barSet(QModelIndex index)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#barSet

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QBarSet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBarSet *QBarModelMapperPrivate::barSet(QModelIndex index)
    address = self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate6barSetE11QModelIndex',
        self._valueOf(index),
    )
    from . import QBarSet
    return QBarSet._cuteAt(address)

  @overload(int, int)
  def barModelIndex(self, barSection: int, posInBar: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QBarModelMapperPrivate::barModelIndex(int
    barSection, int posInBar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#barModelIndex

    Parameters
    ----------

    barSection : int
      Passed on as it is.

    posInBar : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QBarModelMapperPrivate::barModelIndex(int barSection, int
    #      posInBar)
    address = self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate13barModelIndexEii',
        barSection, posInBar,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int, int)
  def insertData(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QBarModelMapperPrivate::insertData(int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#insertData

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QBarModelMapperPrivate::insertData(int start, int end)
    self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate10insertDataEii', start, end,
    )

  @overload(int, int)
  def removeData(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QBarModelMapperPrivate::removeData(int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#removeData

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QBarModelMapperPrivate::removeData(int start, int end)
    self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate10removeDataEii', start, end,
    )

  @overload()
  @overload(bool)
  def blockModelSignals(self, block: bool = True) -> None:
    """
    Calls Qt's 'void QBarModelMapperPrivate::blockModelSignals(bool block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#blockModelSignals

    Parameters
    ----------

    block : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QBarModelMapperPrivate::blockModelSignals(bool block)
    self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate17blockModelSignalsEb', block,
    )

  @overload()
  @overload(bool)
  def blockSeriesSignals(self, block: bool = True) -> None:
    """
    Calls Qt's 'void QBarModelMapperPrivate::blockSeriesSignals(bool block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#blockSeriesSignals

    Parameters
    ----------

    block : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QBarModelMapperPrivate::blockSeriesSignals(bool block)
    self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate18blockSeriesSignalsEb', block,
    )

  def q_func(self) -> Optional[QBarModelMapper]:
    """
    Calls Qt's 'QBarModelMapper *QBarModelMapperPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#q_func

    Returns
    -------

    Optional[QBarModelMapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBarModelMapper *QBarModelMapperPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate6q_funcEv',
    )
    from . import QBarModelMapper
    return QBarModelMapper._cuteAt(address)
