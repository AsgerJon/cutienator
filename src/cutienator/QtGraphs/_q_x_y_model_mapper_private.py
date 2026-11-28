"""
QXYModelMapperPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qxymodelmapper_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QXYModelMapperPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QModelIndex
  from . import QXYModelMapper
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']


class QXYModelMapperPrivate(QObjectPrivate):
  """
  The cute side of Qt's QXYModelMapperPrivate: a plain Python object standing
  in front of one C++ QXYModelMapperPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QXYModelMapperPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QXYModelMapperPrivate that has a ritual and that
  Python can call so far, 17 names in all: 'q_func', 'onModelRowsAdded',
  'onModelRowsRemoved', 'onModelColumnsAdded', 'onModelColumnsRemoved',
  'handleModelDestroyed', 'onPointAdded', 'onPointRemoved',
  'onPointsRemoved', 'onPointReplaced', 'handleSeriesDestroyed',
  'xModelIndex', 'yModelIndex', 'blockModelSignals', 'blockSeriesSignals',
  'valueFromModel', 'setValueToModel'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QXYModelMapper *QXYModelMapperPrivate::q_func() const': takes
    in Python what 'QXYModelMapper *QXYModelMapperPrivate::q_func()' takes.
  - Qt's 'QXYModelMapperPrivate::~QXYModelMapperPrivate()': the destructor:
    Python never removes a C++ QXYModelMapperPrivate.

  What has no ritual
  ------------------

  8 of the 28 functions Qt declares: 4 forbidden; 4 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QXYModelMapperPrivate is created at the first use, not by
    'QXYModelMapperPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QXYModelMapperPrivate.
  - Each name of Qt's QXYModelMapperPrivate that has no cute function yet,
    'initializeXYFromModel', 'insertData', 'onModelUpdated', 'removeData',
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
  __qt_class__ = 'QXYModelMapperPrivate'
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

  @overload(QModelIndex, float)
  def setValueToModel(self, index: QModelIndex, value: float) -> None:
    """
    Calls Qt's 'void QXYModelMapperPrivate::setValueToModel(QModelIndex
    index, qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#setValueToModel

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    value : float
      Passed on as it is.
    """
    #  void QXYModelMapperPrivate::setValueToModel(QModelIndex index, qreal
    #      value)
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate15setValueToModelE11QModelIndexd',
        self._valueOf(index), value,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QXYModelMapperPrivate::QXYModelMapperPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#QXYModelMapperPrivate
    """
    #  QXYModelMapperPrivate::QXYModelMapperPrivate()
    self._noteCreation(QXYModelMapperPrivate, lambda: Rituals.call(
        'ritual_ZN21QXYModelMapperPrivateC1Ev',
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

  def q_func(self) -> Optional[QXYModelMapper]:
    """
    Calls Qt's 'QXYModelMapper *QXYModelMapperPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qxymodelmapperprivate.html#q_func

    Returns
    -------

    Optional[QXYModelMapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXYModelMapper *QXYModelMapperPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QXYModelMapperPrivate6q_funcEv')
    from . import QXYModelMapper
    return QXYModelMapper._cuteAt(address)

  @overload(QModelIndex, int, int)
  def onModelRowsAdded(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QXYModelMapperPrivate::onModelRowsAdded(QModelIndex
    parent, qsizetype start, qsizetype end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#onModelRowsAdded

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
    #  void QXYModelMapperPrivate::onModelRowsAdded(QModelIndex parent,
    #      qsizetype start, qsizetype end)
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate16onModelRowsAddedE11QModelIndexxx',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def onModelRowsRemoved(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QXYModelMapperPrivate::onModelRowsRemoved(QModelIndex
    parent, qsizetype start, qsizetype end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#onModelRowsRemoved

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
    #  void QXYModelMapperPrivate::onModelRowsRemoved(QModelIndex parent,
    #      qsizetype start, qsizetype end)
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate18onModelRowsRemovedE11QModelIndex'
        'xx',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def onModelColumnsAdded(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QXYModelMapperPrivate::onModelColumnsAdded(QModelIndex
    parent, qsizetype start, qsizetype end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#onModelColumnsAdded

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
    #  void QXYModelMapperPrivate::onModelColumnsAdded(QModelIndex parent,
    #      qsizetype start, qsizetype end)
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate19onModelColumnsAddedE11QModelInde'
        'xxx',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def onModelColumnsRemoved(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QXYModelMapperPrivate::onModelColumnsRemoved(QModelIndex
    parent, qsizetype start, qsizetype end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#onModelColumnsRemoved

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
    #  void QXYModelMapperPrivate::onModelColumnsRemoved(QModelIndex parent,
    #      qsizetype start, qsizetype end)
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate21onModelColumnsRemovedE11QModelIn'
        'dexxx',
        self._valueOf(parent), start, end,
    )

  def handleModelDestroyed(self) -> None:
    """
    Calls Qt's 'void QXYModelMapperPrivate::handleModelDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#handleModelDestroyed
    """
    #  void QXYModelMapperPrivate::handleModelDestroyed()
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate20handleModelDestroyedEv',
    )

  @overload(int)
  def onPointAdded(self, pointIndex: int) -> None:
    """
    Calls Qt's 'void QXYModelMapperPrivate::onPointAdded(qsizetype
    pointIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#onPointAdded

    Parameters
    ----------

    pointIndex : int
      Passed on as it is.
    """
    #  void QXYModelMapperPrivate::onPointAdded(qsizetype pointIndex)
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate12onPointAddedEx', pointIndex,
    )

  @overload(int)
  def onPointRemoved(self, pointIndex: int) -> None:
    """
    Calls Qt's 'void QXYModelMapperPrivate::onPointRemoved(qsizetype
    pointIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#onPointRemoved

    Parameters
    ----------

    pointIndex : int
      Passed on as it is.
    """
    #  void QXYModelMapperPrivate::onPointRemoved(qsizetype pointIndex)
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate14onPointRemovedEx', pointIndex,
    )

  @overload(int, int)
  def onPointsRemoved(self, pointIndex: int, count: int) -> None:
    """
    Calls Qt's 'void QXYModelMapperPrivate::onPointsRemoved(qsizetype
    pointIndex, qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#onPointsRemoved

    Parameters
    ----------

    pointIndex : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QXYModelMapperPrivate::onPointsRemoved(qsizetype pointIndex,
    #      qsizetype count)
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate15onPointsRemovedExx',
        pointIndex, count,
    )

  @overload(int)
  def onPointReplaced(self, pointIndex: int) -> None:
    """
    Calls Qt's 'void QXYModelMapperPrivate::onPointReplaced(qsizetype
    pointIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#onPointReplaced

    Parameters
    ----------

    pointIndex : int
      Passed on as it is.
    """
    #  void QXYModelMapperPrivate::onPointReplaced(qsizetype pointIndex)
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate15onPointReplacedEx', pointIndex,
    )

  def handleSeriesDestroyed(self) -> None:
    """
    Calls Qt's 'void QXYModelMapperPrivate::handleSeriesDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#handleSeriesDestroyed
    """
    #  void QXYModelMapperPrivate::handleSeriesDestroyed()
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate21handleSeriesDestroyedEv',
    )

  @overload(int)
  def xModelIndex(self, xIndex: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QXYModelMapperPrivate::xModelIndex(qsizetype
    xIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#xModelIndex

    Parameters
    ----------

    xIndex : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QXYModelMapperPrivate::xModelIndex(qsizetype xIndex)
    address = self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate11xModelIndexEx', xIndex,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int)
  def yModelIndex(self, yIndex: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QXYModelMapperPrivate::yModelIndex(qsizetype
    yIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#yModelIndex

    Parameters
    ----------

    yIndex : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QXYModelMapperPrivate::yModelIndex(qsizetype yIndex)
    address = self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate11yModelIndexEx', yIndex,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload()
  @overload(bool)
  def blockModelSignals(self, block: bool = True) -> None:
    """
    Calls Qt's 'void QXYModelMapperPrivate::blockModelSignals(bool block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#blockModelSignals

    Parameters
    ----------

    block : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QXYModelMapperPrivate::blockModelSignals(bool block)
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate17blockModelSignalsEb', block,
    )

  @overload()
  @overload(bool)
  def blockSeriesSignals(self, block: bool = True) -> None:
    """
    Calls Qt's 'void QXYModelMapperPrivate::blockSeriesSignals(bool block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#blockSeriesSignals

    Parameters
    ----------

    block : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QXYModelMapperPrivate::blockSeriesSignals(bool block)
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate18blockSeriesSignalsEb', block,
    )

  @overload(QModelIndex)
  def valueFromModel(self, index: QModelIndex) -> float:
    """
    Calls Qt's 'qreal QXYModelMapperPrivate::valueFromModel(QModelIndex
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#valueFromModel

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  qreal QXYModelMapperPrivate::valueFromModel(QModelIndex index)
    return self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate14valueFromModelE11QModelIndex',
        self._valueOf(index),
    )

  @staticmethod
  def initializeXYFromModel(*__, **_) -> Never:
    """
    Qt's 'void QXYModelMapperPrivate::initializeXYFromModel()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier
    'QGraphs2DXYModelMappeInitXYFromModel'.
    """
    raise NotImplementedError(
        "'QXYModelMapperPrivate.initializeXYFromModel' has no cute function "
        "yet. Qt's 'void QXYModelMapperPrivate::initializeXYFromModel()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'QGraphs2DXYModelMappeInitXYFromModel'.")

  @staticmethod
  def insertData(*__, **_) -> Never:
    """
    Qt's 'void QXYModelMapperPrivate::insertData(int start, int end)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'QGraphs2DXYModelMappeInsertData'.
    """
    raise NotImplementedError(
        "'QXYModelMapperPrivate.insertData' has no cute function yet. Qt's "
        "'void QXYModelMapperPrivate::insertData(int start, int end)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'QGraphs2DXYModelMappeInsertData'.")

  @staticmethod
  def onModelUpdated(*__, **_) -> Never:
    """
    Qt's 'void QXYModelMapperPrivate::onModelUpdated(QModelIndex topLeft,
    QModelIndex bottomRight)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: use of undeclared
    identifier 'QGraphs2DXYModelMapperOnModelUpdated'.
    """
    raise NotImplementedError(
        "'QXYModelMapperPrivate.onModelUpdated' has no cute function yet. "
        "Qt's 'void QXYModelMapperPrivate::onModelUpdated(QModelIndex "
        "topLeft, QModelIndex bottomRight)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier "
        "'QGraphs2DXYModelMapperOnModelUpdated'.")

  @staticmethod
  def removeData(*__, **_) -> Never:
    """
    Qt's 'void QXYModelMapperPrivate::removeData(int start, int end)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'QGraphs2DXYModelMappeRemoveData'.
    """
    raise NotImplementedError(
        "'QXYModelMapperPrivate.removeData' has no cute function yet. Qt's "
        "'void QXYModelMapperPrivate::removeData(int start, int end)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'QGraphs2DXYModelMappeRemoveData'.")
