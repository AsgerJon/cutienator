"""
QPieModelMapperPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qpiemodelmapper_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QPieModelMapperPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList, QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QModelIndex
  from . import QPieModelMapper, QPieSlice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QPieSlice = WAIT['QtGraphs:QPieSlice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPieModelMapperPrivate(QObjectPrivate):
  """
  The cute side of Qt's QPieModelMapperPrivate: a plain Python object
  standing in front of one C++ QPieModelMapperPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QPieModelMapperPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPieModelMapperPrivate that has a ritual and that
  Python can call so far, 15 names in all: 'q_func', 'onSliceLabelChanged',
  'onSliceValueChanged', 'onModelUpdated', 'handleModelDestroyed',
  'onSlicesAdded', 'onSlicesRemoved', 'handleSeriesDestroyed', 'pieSlice',
  'isLabelIndex', 'isValueIndex', 'valueModelIndex', 'labelModelIndex',
  'blockModelSignals', 'blockSeriesSignals'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPieModelMapper *QPieModelMapperPrivate::q_func() const':
    takes in Python what 'QPieModelMapper *QPieModelMapperPrivate::q_func()'
    takes.
  - Qt's 'QPieModelMapperPrivate::~QPieModelMapperPrivate()': the destructor:
    Python never removes a C++ QPieModelMapperPrivate.

  What has no ritual
  ------------------

  11 of the 29 functions Qt declares: 4 forbidden; 4 leans on
  'QPieModelMapperPrivate; 3 Qt's library has no name for it, and its code in
  Qt's source does not compile apart from its file.

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
  - Each name of Qt's QPieModelMapperPrivate that has no cute function yet,
    'initializePieFromModel', 'insertData', 'onModelColumnsAdded',
    'onModelColumnsRemoved', 'onModelRowsAdded', 'onModelRowsRemoved',
    'removeData', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPieModelMapperPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QPieModelMapperPrivate::QPieModelMapperPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#QPieModelMapperPrivate
    """
    #  QPieModelMapperPrivate::QPieModelMapperPrivate()
    self._noteCreation(QPieModelMapperPrivate, lambda: Rituals.call(
        'ritual_ZN22QPieModelMapperPrivateC1Ev',
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

  @overload(QPieSlice)
  @overload(NoneType)
  def onSliceLabelChanged(self, slice: Optional[QPieSlice]) -> None:
    """
    Calls Qt's 'void QPieModelMapperPrivate::onSliceLabelChanged(const
    QPieSlice *slice)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#onSliceLabelChanged

    Parameters
    ----------

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPieModelMapperPrivate::onSliceLabelChanged(const QPieSlice
    #      *slice)
    self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate19onSliceLabelChangedEPK9QPieSlic'
        'e',
        self._addressOf(slice),
    )

  @overload(QPieSlice)
  @overload(NoneType)
  def onSliceValueChanged(self, slice: Optional[QPieSlice]) -> None:
    """
    Calls Qt's 'void QPieModelMapperPrivate::onSliceValueChanged(const
    QPieSlice *slice)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#onSliceValueChanged

    Parameters
    ----------

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPieModelMapperPrivate::onSliceValueChanged(const QPieSlice
    #      *slice)
    self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate19onSliceValueChangedEPK9QPieSlic'
        'e',
        self._addressOf(slice),
    )

  @overload(QModelIndex, QModelIndex)
  def onModelUpdated(
      self,
      topLeft: QModelIndex,
      bottomRight: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QPieModelMapperPrivate::onModelUpdated(QModelIndex
    topLeft, QModelIndex bottomRight)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#onModelUpdated

    Parameters
    ----------

    topLeft : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    bottomRight : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QPieModelMapperPrivate::onModelUpdated(QModelIndex topLeft,
    #      QModelIndex bottomRight)
    self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate14onModelUpdatedE11QModelIndexS0_',
        self._valueOf(topLeft), self._valueOf(bottomRight),
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
  def onSlicesAdded(self, slices: QList[QPieSlice]) -> None:
    """
    Calls Qt's 'void QPieModelMapperPrivate::onSlicesAdded(const
    QList<QPieSlice *> &slices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#onSlicesAdded

    Parameters
    ----------

    slices : QList[QPieSlice]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPieModelMapperPrivate::onSlicesAdded(const QList<QPieSlice *>
    #      &slices)
    self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate13onSlicesAddedERK5QListIP9QPieSl'
        'iceE',
        self._valueOf(slices),
    )

  @overload(QList[QPieSlice])
  def onSlicesRemoved(self, slices: QList[QPieSlice]) -> None:
    """
    Calls Qt's 'void QPieModelMapperPrivate::onSlicesRemoved(const
    QList<QPieSlice *> &slices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#onSlicesRemoved

    Parameters
    ----------

    slices : QList[QPieSlice]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPieModelMapperPrivate::onSlicesRemoved(const QList<QPieSlice *>
    #      &slices)
    self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate15onSlicesRemovedERK5QListIP9QPie'
        'SliceE',
        self._valueOf(slices),
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

  @overload(int)
  def valueModelIndex(self, sliceIndex: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QPieModelMapperPrivate::valueModelIndex(qsizetype
    sliceIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#valueModelIndex

    Parameters
    ----------

    sliceIndex : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QPieModelMapperPrivate::valueModelIndex(qsizetype
    #      sliceIndex)
    address = self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate15valueModelIndexEx', sliceIndex,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int)
  def labelModelIndex(self, sliceIndex: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QPieModelMapperPrivate::labelModelIndex(qsizetype
    sliceIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpiemodelmapperprivate.html#labelModelIndex

    Parameters
    ----------

    sliceIndex : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QPieModelMapperPrivate::labelModelIndex(qsizetype
    #      sliceIndex)
    address = self.uglySide.call(
        'ritual_ZN22QPieModelMapperPrivate15labelModelIndexEx', sliceIndex,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

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

  @staticmethod
  def initializePieFromModel(*__, **_) -> Never:
    """
    Qt's 'void QPieModelMapperPrivate::initializePieFromModel()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'QGraphs2DPieModelMapperInitPieFromModel'.
    """
    raise NotImplementedError(
        "'QPieModelMapperPrivate.initializePieFromModel' has no cute "
        "function yet. Qt's 'void "
        "QPieModelMapperPrivate::initializePieFromModel()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'QGraphs2DPieModelMapperInitPieFromModel'.")

  @staticmethod
  def insertData(*__, **_) -> Never:
    """
    Qt's 'void QPieModelMapperPrivate::insertData(qsizetype start, qsizetype
    end)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'QGraphs2DPieModelMapperInsertData'.
    """
    raise NotImplementedError(
        "'QPieModelMapperPrivate.insertData' has no cute function yet. Qt's "
        "'void QPieModelMapperPrivate::insertData(qsizetype start, "
        "qsizetype end)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'QGraphs2DPieModelMapperInsertData'.")

  @staticmethod
  def onModelColumnsAdded(*__, **_) -> Never:
    """
    Qt's 'void QPieModelMapperPrivate::onModelColumnsAdded(QModelIndex
    parent, qsizetype start, qsizetype end)': leans on
    'QPieModelMapperPrivate::insertData(long long, long long)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QPieModelMapperPrivate.onModelColumnsAdded' has no cute function "
        "yet. Qt's 'void "
        "QPieModelMapperPrivate::onModelColumnsAdded(QModelIndex parent, "
        "qsizetype start, qsizetype end)': leans on "
        "'QPieModelMapperPrivate::insertData(long long, long long)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def onModelColumnsRemoved(*__, **_) -> Never:
    """
    Qt's 'void QPieModelMapperPrivate::onModelColumnsRemoved(QModelIndex
    parent, qsizetype start, qsizetype end)': leans on
    'QPieModelMapperPrivate::removeData(long long, long long)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QPieModelMapperPrivate.onModelColumnsRemoved' has no cute "
        "function yet. Qt's 'void "
        "QPieModelMapperPrivate::onModelColumnsRemoved(QModelIndex parent, "
        "qsizetype start, qsizetype end)': leans on "
        "'QPieModelMapperPrivate::removeData(long long, long long)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def onModelRowsAdded(*__, **_) -> Never:
    """
    Qt's 'void QPieModelMapperPrivate::onModelRowsAdded(QModelIndex parent,
    qsizetype start, qsizetype end)': leans on
    'QPieModelMapperPrivate::insertData(long long, long long)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QPieModelMapperPrivate.onModelRowsAdded' has no cute function "
        "yet. Qt's 'void "
        "QPieModelMapperPrivate::onModelRowsAdded(QModelIndex parent, "
        "qsizetype start, qsizetype end)': leans on "
        "'QPieModelMapperPrivate::insertData(long long, long long)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def onModelRowsRemoved(*__, **_) -> Never:
    """
    Qt's 'void QPieModelMapperPrivate::onModelRowsRemoved(QModelIndex parent,
    qsizetype start, qsizetype end)': leans on
    'QPieModelMapperPrivate::removeData(long long, long long)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QPieModelMapperPrivate.onModelRowsRemoved' has no cute function "
        "yet. Qt's 'void "
        "QPieModelMapperPrivate::onModelRowsRemoved(QModelIndex parent, "
        "qsizetype start, qsizetype end)': leans on "
        "'QPieModelMapperPrivate::removeData(long long, long long)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def removeData(*__, **_) -> Never:
    """
    Qt's 'void QPieModelMapperPrivate::removeData(qsizetype start, qsizetype
    end)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'QGraphs2DPieModelMapperRemoveData'.
    """
    raise NotImplementedError(
        "'QPieModelMapperPrivate.removeData' has no cute function yet. Qt's "
        "'void QPieModelMapperPrivate::removeData(qsizetype start, "
        "qsizetype end)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'QGraphs2DPieModelMapperRemoveData'.")
