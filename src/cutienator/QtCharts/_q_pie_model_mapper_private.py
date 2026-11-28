"""
QPieModelMapperPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qpiemodelmapper_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QPieModelMapperPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QModelIndex
  from . import QPieModelMapper, QPieSlice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QPieModelMapper = WAIT['QtCharts:QPieModelMapper']
  QPieSlice = WAIT['QtCharts:QPieSlice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPieModelMapperPrivate(QObject):
  """
  The cute side of Qt's QPieModelMapperPrivate: a plain Python object
  standing in front of one C++ QPieModelMapperPrivate.

  It is built on the cute 'QObject', as Qt's QPieModelMapperPrivate is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPieModelMapperPrivate that has a ritual and that
  Python can call so far, 24 names in all: 'metaObject', 'tr',
  'modelUpdated', 'modelRowsAdded', 'modelRowsRemoved', 'modelColumnsAdded',
  'modelColumnsRemoved', 'handleModelDestroyed', 'slicesAdded',
  'slicesRemoved', 'sliceLabelChanged', 'sliceValueChanged',
  'handleSeriesDestroyed', 'initializePieFromModel', 'pieSlice',
  'isLabelIndex', 'isValueIndex', 'valueModelIndex', 'labelModelIndex',
  'insertData', 'removeData', 'blockModelSignals', 'blockSeriesSignals',
  'q_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPieModelMapperPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QPieModelMapperPrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QPieModelMapper *QPieModelMapperPrivate::q_func() const':
    takes in Python what 'QPieModelMapper *QPieModelMapperPrivate::q_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 30 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPieModelMapperPrivate is created at the first use, not by
    'QPieModelMapperPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPieModelMapperPrivate.
  - Qt tells when it has removed the C++ QPieModelMapperPrivate. Every call
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
    Calls Qt's 'QString QPieModelMapperPrivate::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#tr

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
    #  QString QPieModelMapperPrivate::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QPieModelMapperPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPieModelMapperPrivate'
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
    Calls Qt's 'const QMetaObject *QPieModelMapperPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPieModelMapperPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QPieModelMapperPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QModelIndex)
  def pieSlice(self, index: QModelIndex) -> Optional[QPieSlice]:
    """
    Calls Qt's 'QPieSlice *QPieModelMapperPrivate::pieSlice(QModelIndex
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#pieSlice

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QPieSlice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSlice *QPieModelMapperPrivate::pieSlice(QModelIndex index) const
    address = self.uglySide.call(
        'ritual_ZNK22QPieModelMapperPrivate8pieSliceE11QModelIndex',
        self._valueOf(index),
    )
    from . import QPieSlice
    return QPieSlice._cuteAt(address)

  @overload(QModelIndex)
  def isLabelIndex(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QPieModelMapperPrivate::isLabelIndex(QModelIndex index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#isLabelIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QPieModelMapperPrivate::isLabelIndex(QModelIndex index) const
    return self.uglySide.call(
        'ritual_ZNK22QPieModelMapperPrivate12isLabelIndexE11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def isValueIndex(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QPieModelMapperPrivate::isValueIndex(QModelIndex index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#isValueIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QPieModelMapperPrivate::isValueIndex(QModelIndex index) const
    return self.uglySide.call(
        'ritual_ZNK22QPieModelMapperPrivate12isValueIndexE11QModelIndex',
        self._valueOf(index),
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

  @overload(QPieModelMapper)
  @overload(NoneType)
  def __init__(self, q: Optional[QPieModelMapper]) -> None:
    """
    Notes what was given, for Qt's
    'QPieModelMapperPrivate::QPieModelMapperPrivate(QPieModelMapper *q)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#QPieModelMapperPrivate

    Parameters
    ----------

    q : Optional[QPieModelMapper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPieModelMapperPrivate::QPieModelMapperPrivate(QPieModelMapper *q)
    self._noteCreation(QPieModelMapperPrivate, lambda: Rituals.call(
        'ritual_ZN22QPieModelMapperPrivateC1EP15QPieModelMapper',
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
    Calls Qt's 'void QPieModelMapperPrivate::modelUpdated(QModelIndex
    topLeft, QModelIndex bottomRight)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#modelUpdated

    Parameters
    ----------

    topLeft : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    bottomRight : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QPieModelMapperPrivate::modelUpdated(QModelIndex topLeft,
    #      QModelIndex bottomRight)
    self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate12modelUpdatedE11QModelIndexS0_',
        self._valueOf(topLeft), self._valueOf(bottomRight),
    )

  @overload(QModelIndex, int, int)
  def modelRowsAdded(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QPieModelMapperPrivate::modelRowsAdded(QModelIndex
    parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#modelRowsAdded

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
    #  void QPieModelMapperPrivate::modelRowsAdded(QModelIndex parent, int
    #      start, int end)
    self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate14modelRowsAddedE11QModelIndexii',
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
    Calls Qt's 'void QPieModelMapperPrivate::modelRowsRemoved(QModelIndex
    parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#modelRowsRemoved

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
    #  void QPieModelMapperPrivate::modelRowsRemoved(QModelIndex parent, int
    #      start, int end)
    self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate16modelRowsRemovedE11QModelIndexi'
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
    Calls Qt's 'void QPieModelMapperPrivate::modelColumnsAdded(QModelIndex
    parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#modelColumnsAdded

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
    #  void QPieModelMapperPrivate::modelColumnsAdded(QModelIndex parent, int
    #      start, int end)
    self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate17modelColumnsAddedE11QModelIndex'
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
    Calls Qt's 'void QPieModelMapperPrivate::modelColumnsRemoved(QModelIndex
    parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#modelColumnsRemoved

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
    #  void QPieModelMapperPrivate::modelColumnsRemoved(QModelIndex parent,
    #      int start, int end)
    self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate19modelColumnsRemovedE11QModelInd'
        'exii',
        self._valueOf(parent), start, end,
    )

  def handleModelDestroyed(self) -> None:
    """
    Calls Qt's 'void QPieModelMapperPrivate::handleModelDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#handleModelDestroyed
    """
    #  void QPieModelMapperPrivate::handleModelDestroyed()
    self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate20handleModelDestroyedEv',
    )

  @overload(QList[QPieSlice])
  def slicesAdded(self, slices: QList[QPieSlice]) -> None:
    """
    Calls Qt's 'void QPieModelMapperPrivate::slicesAdded(const
    QList<QPieSlice *> &slices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#slicesAdded

    Parameters
    ----------

    slices : QList[QPieSlice]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPieModelMapperPrivate::slicesAdded(const QList<QPieSlice *>
    #      &slices)
    self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate11slicesAddedERK5QListIP9QPieSlic'
        'eE',
        self._valueOf(slices),
    )

  @overload(QList[QPieSlice])
  def slicesRemoved(self, slices: QList[QPieSlice]) -> None:
    """
    Calls Qt's 'void QPieModelMapperPrivate::slicesRemoved(const
    QList<QPieSlice *> &slices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#slicesRemoved

    Parameters
    ----------

    slices : QList[QPieSlice]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPieModelMapperPrivate::slicesRemoved(const QList<QPieSlice *>
    #      &slices)
    self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate13slicesRemovedERK5QListIP9QPieSl'
        'iceE',
        self._valueOf(slices),
    )

  def sliceLabelChanged(self) -> None:
    """
    Calls Qt's 'void QPieModelMapperPrivate::sliceLabelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#sliceLabelChanged
    """
    #  void QPieModelMapperPrivate::sliceLabelChanged()
    self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate17sliceLabelChangedEv',
    )

  def sliceValueChanged(self) -> None:
    """
    Calls Qt's 'void QPieModelMapperPrivate::sliceValueChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#sliceValueChanged
    """
    #  void QPieModelMapperPrivate::sliceValueChanged()
    self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate17sliceValueChangedEv',
    )

  def handleSeriesDestroyed(self) -> None:
    """
    Calls Qt's 'void QPieModelMapperPrivate::handleSeriesDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#handleSeriesDestroyed
    """
    #  void QPieModelMapperPrivate::handleSeriesDestroyed()
    self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate21handleSeriesDestroyedEv',
    )

  def initializePieFromModel(self) -> None:
    """
    Calls Qt's 'void QPieModelMapperPrivate::initializePieFromModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#initializePieFromModel
    """
    #  void QPieModelMapperPrivate::initializePieFromModel()
    self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate22initializePieFromModelEv',
    )

  @overload(int)
  def valueModelIndex(self, slicePos: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QPieModelMapperPrivate::valueModelIndex(int
    slicePos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#valueModelIndex

    Parameters
    ----------

    slicePos : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QPieModelMapperPrivate::valueModelIndex(int slicePos)
    address = self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate15valueModelIndexEi', slicePos,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int)
  def labelModelIndex(self, slicePos: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QPieModelMapperPrivate::labelModelIndex(int
    slicePos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#labelModelIndex

    Parameters
    ----------

    slicePos : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QPieModelMapperPrivate::labelModelIndex(int slicePos)
    address = self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate15labelModelIndexEi', slicePos,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int, int)
  def insertData(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QPieModelMapperPrivate::insertData(int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#insertData

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QPieModelMapperPrivate::insertData(int start, int end)
    self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate10insertDataEii', start, end,
    )

  @overload(int, int)
  def removeData(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QPieModelMapperPrivate::removeData(int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#removeData

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QPieModelMapperPrivate::removeData(int start, int end)
    self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate10removeDataEii', start, end,
    )

  @overload()
  @overload(bool)
  def blockModelSignals(self, block: bool = True) -> None:
    """
    Calls Qt's 'void QPieModelMapperPrivate::blockModelSignals(bool block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#blockModelSignals

    Parameters
    ----------

    block : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QPieModelMapperPrivate::blockModelSignals(bool block)
    self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate17blockModelSignalsEb', block,
    )

  @overload()
  @overload(bool)
  def blockSeriesSignals(self, block: bool = True) -> None:
    """
    Calls Qt's 'void QPieModelMapperPrivate::blockSeriesSignals(bool block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#blockSeriesSignals

    Parameters
    ----------

    block : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QPieModelMapperPrivate::blockSeriesSignals(bool block)
    self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate18blockSeriesSignalsEb', block,
    )

  def q_func(self) -> Optional[QPieModelMapper]:
    """
    Calls Qt's 'QPieModelMapper *QPieModelMapperPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#q_func

    Returns
    -------

    Optional[QPieModelMapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieModelMapper *QPieModelMapperPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate6q_funcEv',
    )
    from . import QPieModelMapper
    return QPieModelMapper._cuteAt(address)
