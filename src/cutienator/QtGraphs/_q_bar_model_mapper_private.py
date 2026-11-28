"""
QBarModelMapperPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qbarmodelmapper_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QBarModelMapperPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QModelIndex
  from . import QBarModelMapper, QBarSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']


class QBarModelMapperPrivate(QObjectPrivate):
  """
  The cute side of Qt's QBarModelMapperPrivate: a plain Python object
  standing in front of one C++ QBarModelMapperPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QBarModelMapperPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBarModelMapperPrivate that has a ritual and that
  Python can call so far, 9 names in all: 'q_func', 'barModelIndex',
  'blockSeriesSignals', 'blockModelSignals', 'barSet', 'modelUpdated',
  'modelHeaderDataUpdated', 'handleModelDestroyed', 'handleSeriesDestroyed'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QBarModelMapper *QBarModelMapperPrivate::q_func() const':
    takes in Python what 'QBarModelMapper *QBarModelMapperPrivate::q_func()'
    takes.
  - Qt's 'QBarModelMapperPrivate::~QBarModelMapperPrivate()': the destructor:
    Python never removes a C++ QBarModelMapperPrivate.

  What has no ritual
  ------------------

  17 of the 29 functions Qt declares: 12 leans on 'QBarModelMapperPrivate; 4
  forbidden; 1 Qt's library has no name for it, and its code in Qt's source
  does not compile apart from its file.

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
  - Each name of Qt's QBarModelMapperPrivate that has no cute function yet,
    'barSetsAdded', 'barSetsRemoved', 'handleBarLabelChanged',
    'handleBarValueChanged', 'handleValuesAdded', 'initializeBarsFromModel',
    'insertData', 'modelColumnsAdded', 'modelColumnsRemoved',
    'modelRowsAdded', 'modelRowsRemoved', 'removeData', 'valuesRemoved',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBarModelMapperPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QBarModelMapperPrivate::QBarModelMapperPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#QBarModelMapperPrivate
    """
    #  QBarModelMapperPrivate::QBarModelMapperPrivate()
    self._noteCreation(QBarModelMapperPrivate, lambda: Rituals.call(
        'ritual_ZN22QBarModelMapperPrivateC1Ev',
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

  @overload(int, int)
  def barModelIndex(self, barSection: int, posInBar: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QBarModelMapperPrivate::barModelIndex(qsizetype
    barSection, qsizetype posInBar)'.

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
    #  QModelIndex QBarModelMapperPrivate::barModelIndex(qsizetype
    #      barSection, qsizetype posInBar)
    address = self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate13barModelIndexExx',
        barSection, posInBar,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload()
  @overload(bool)
  def blockSeriesSignals(self, block: bool = True) -> None:
    """
    Calls Qt's 'void QBarModelMapperPrivate::blockSeriesSignals(const bool
    block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#blockSeriesSignals

    Parameters
    ----------

    block : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QBarModelMapperPrivate::blockSeriesSignals(const bool block)
    self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate18blockSeriesSignalsEb', block,
    )

  @overload()
  @overload(bool)
  def blockModelSignals(self, block: bool = True) -> None:
    """
    Calls Qt's 'void QBarModelMapperPrivate::blockModelSignals(const bool
    block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarmodelmapperprivate.html#blockModelSignals

    Parameters
    ----------

    block : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QBarModelMapperPrivate::blockModelSignals(const bool block)
    self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate17blockModelSignalsEb', block,
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
    orientation, qsizetype first, qsizetype last)'.

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
    #      orientation, qsizetype first, qsizetype last)
    self.uglySide.call(
        'ritual_ZN22QBarModelMapperPrivate22modelHeaderDataUpdatedEN2Qt11Or'
        'ientationExx',
        orientation.value, first, last,
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

  @staticmethod
  def barSetsAdded(*__, **_) -> Never:
    """
    Qt's 'void QBarModelMapperPrivate::barSetsAdded(const QList<QBarSet *>
    &sets)': leans on 'QBarModelMapperPrivate::initializeBarsFromModel()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QBarModelMapperPrivate.barSetsAdded' has no cute function yet. "
        "Qt's 'void QBarModelMapperPrivate::barSetsAdded(const "
        "QList<QBarSet *> &sets)': leans on "
        "'QBarModelMapperPrivate::initializeBarsFromModel()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def barSetsRemoved(*__, **_) -> Never:
    """
    Qt's 'void QBarModelMapperPrivate::barSetsRemoved(const QList<QBarSet *>
    &sets)': leans on 'QBarModelMapperPrivate::initializeBarsFromModel()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QBarModelMapperPrivate.barSetsRemoved' has no cute function yet. "
        "Qt's 'void QBarModelMapperPrivate::barSetsRemoved(const "
        "QList<QBarSet *> &sets)': leans on "
        "'QBarModelMapperPrivate::initializeBarsFromModel()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def handleBarLabelChanged(*__, **_) -> Never:
    """
    Qt's 'void QBarModelMapperPrivate::handleBarLabelChanged(QBarSet *set)':
    leans on 'QBarModelMapperPrivate::initializeBarsFromModel()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QBarModelMapperPrivate.handleBarLabelChanged' has no cute "
        "function yet. Qt's 'void "
        "QBarModelMapperPrivate::handleBarLabelChanged(QBarSet *set)': "
        "leans on 'QBarModelMapperPrivate::initializeBarsFromModel()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def handleBarValueChanged(*__, **_) -> Never:
    """
    Qt's 'void QBarModelMapperPrivate::handleBarValueChanged(QBarSet *set,
    qsizetype index)': leans on
    'QBarModelMapperPrivate::initializeBarsFromModel()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QBarModelMapperPrivate.handleBarValueChanged' has no cute "
        "function yet. Qt's 'void "
        "QBarModelMapperPrivate::handleBarValueChanged(QBarSet *set, "
        "qsizetype index)': leans on "
        "'QBarModelMapperPrivate::initializeBarsFromModel()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def handleValuesAdded(*__, **_) -> Never:
    """
    Qt's 'void QBarModelMapperPrivate::handleValuesAdded(QBarSet *set,
    qsizetype index, qsizetype count)': leans on
    'QBarModelMapperPrivate::initializeBarsFromModel()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QBarModelMapperPrivate.handleValuesAdded' has no cute function "
        "yet. Qt's 'void QBarModelMapperPrivate::handleValuesAdded(QBarSet "
        "*set, qsizetype index, qsizetype count)': leans on "
        "'QBarModelMapperPrivate::initializeBarsFromModel()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def initializeBarsFromModel(*__, **_) -> Never:
    """
    Qt's 'void QBarModelMapperPrivate::initializeBarsFromModel()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'QGraphs2DBarModelMapperInitBarsFromModel'.
    """
    raise NotImplementedError(
        "'QBarModelMapperPrivate.initializeBarsFromModel' has no cute "
        "function yet. Qt's 'void "
        "QBarModelMapperPrivate::initializeBarsFromModel()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'QGraphs2DBarModelMapperInitBarsFromModel'.")

  @staticmethod
  def insertData(*__, **_) -> Never:
    """
    Qt's 'void QBarModelMapperPrivate::insertData(qsizetype start, qsizetype
    end)': leans on 'QBarModelMapperPrivate::initializeBarsFromModel()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QBarModelMapperPrivate.insertData' has no cute function yet. Qt's "
        "'void QBarModelMapperPrivate::insertData(qsizetype start, "
        "qsizetype end)': leans on "
        "'QBarModelMapperPrivate::initializeBarsFromModel()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def modelColumnsAdded(*__, **_) -> Never:
    """
    Qt's 'void QBarModelMapperPrivate::modelColumnsAdded(QModelIndex parent,
    qsizetype start, qsizetype end)': leans on
    'QBarModelMapperPrivate::initializeBarsFromModel()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QBarModelMapperPrivate.modelColumnsAdded' has no cute function "
        "yet. Qt's 'void "
        "QBarModelMapperPrivate::modelColumnsAdded(QModelIndex parent, "
        "qsizetype start, qsizetype end)': leans on "
        "'QBarModelMapperPrivate::initializeBarsFromModel()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def modelColumnsRemoved(*__, **_) -> Never:
    """
    Qt's 'void QBarModelMapperPrivate::modelColumnsRemoved(QModelIndex
    parent, qsizetype start, qsizetype end)': leans on
    'QBarModelMapperPrivate::initializeBarsFromModel()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QBarModelMapperPrivate.modelColumnsRemoved' has no cute function "
        "yet. Qt's 'void "
        "QBarModelMapperPrivate::modelColumnsRemoved(QModelIndex parent, "
        "qsizetype start, qsizetype end)': leans on "
        "'QBarModelMapperPrivate::initializeBarsFromModel()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def modelRowsAdded(*__, **_) -> Never:
    """
    Qt's 'void QBarModelMapperPrivate::modelRowsAdded(QModelIndex parent,
    qsizetype start, qsizetype end)': leans on
    'QBarModelMapperPrivate::initializeBarsFromModel()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QBarModelMapperPrivate.modelRowsAdded' has no cute function yet. "
        "Qt's 'void QBarModelMapperPrivate::modelRowsAdded(QModelIndex "
        "parent, qsizetype start, qsizetype end)': leans on "
        "'QBarModelMapperPrivate::initializeBarsFromModel()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def modelRowsRemoved(*__, **_) -> Never:
    """
    Qt's 'void QBarModelMapperPrivate::modelRowsRemoved(QModelIndex parent,
    qsizetype start, qsizetype end)': leans on
    'QBarModelMapperPrivate::initializeBarsFromModel()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QBarModelMapperPrivate.modelRowsRemoved' has no cute function "
        "yet. Qt's 'void "
        "QBarModelMapperPrivate::modelRowsRemoved(QModelIndex parent, "
        "qsizetype start, qsizetype end)': leans on "
        "'QBarModelMapperPrivate::initializeBarsFromModel()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def removeData(*__, **_) -> Never:
    """
    Qt's 'void QBarModelMapperPrivate::removeData(qsizetype start, qsizetype
    end)': leans on 'QBarModelMapperPrivate::initializeBarsFromModel()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QBarModelMapperPrivate.removeData' has no cute function yet. Qt's "
        "'void QBarModelMapperPrivate::removeData(qsizetype start, "
        "qsizetype end)': leans on "
        "'QBarModelMapperPrivate::initializeBarsFromModel()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def valuesRemoved(*__, **_) -> Never:
    """
    Qt's 'void QBarModelMapperPrivate::valuesRemoved(qsizetype index,
    qsizetype count)': leans on
    'QBarModelMapperPrivate::initializeBarsFromModel()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QBarModelMapperPrivate.valuesRemoved' has no cute function yet. "
        "Qt's 'void QBarModelMapperPrivate::valuesRemoved(qsizetype index, "
        "qsizetype count)': leans on "
        "'QBarModelMapperPrivate::initializeBarsFromModel()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
