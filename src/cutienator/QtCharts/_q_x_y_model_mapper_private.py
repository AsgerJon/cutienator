"""
QXYModelMapperPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qxymodelmapper_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QXYModelMapperPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QModelIndex
  from . import QXYModelMapper
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QXYModelMapper = WAIT['QtCharts:QXYModelMapper']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QXYModelMapperPrivate(QObject):
  """
  The cute side of Qt's QXYModelMapperPrivate: a plain Python object standing
  in front of one C++ QXYModelMapperPrivate.

  It is built on the cute 'QObject', as Qt's QXYModelMapperPrivate is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QXYModelMapperPrivate that has a ritual and that
  Python can call so far, 23 names in all: 'metaObject', 'tr',
  'modelUpdated', 'modelRowsAdded', 'modelRowsRemoved', 'modelColumnsAdded',
  'modelColumnsRemoved', 'handleModelDestroyed', 'handlePointAdded',
  'handlePointRemoved', 'handlePointsRemoved', 'handlePointReplaced',
  'handleSeriesDestroyed', 'initializeXYFromModel', 'xModelIndex',
  'yModelIndex', 'insertData', 'removeData', 'blockModelSignals',
  'blockSeriesSignals', 'valueFromModel', 'setValueToModel', 'q_func'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QXYModelMapperPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QXYModelMapperPrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QXYModelMapper *QXYModelMapperPrivate::q_func() const': takes
    in Python what 'QXYModelMapper *QXYModelMapperPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

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
  - Qt tells when it has removed the C++ QXYModelMapperPrivate. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QXYModelMapperPrivate::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qxymodelmapperprivate.html#tr

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
    #  QString QXYModelMapperPrivate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QXYModelMapperPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXYModelMapperPrivate'
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
    Calls Qt's 'const QMetaObject *QXYModelMapperPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QXYModelMapperPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QXYModelMapperPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(QXYModelMapper)
  @overload(NoneType)
  def __init__(self, q: Optional[QXYModelMapper]) -> None:
    """
    Notes what was given, for Qt's
    'QXYModelMapperPrivate::QXYModelMapperPrivate(QXYModelMapper *q)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#QXYModelMapperPrivate

    Parameters
    ----------

    q : Optional[QXYModelMapper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QXYModelMapperPrivate::QXYModelMapperPrivate(QXYModelMapper *q)
    self._noteCreation(QXYModelMapperPrivate, lambda: Rituals.call(
        'ritual_ZN21QXYModelMapperPrivateC1EP14QXYModelMapper',
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
    Calls Qt's 'void QXYModelMapperPrivate::modelUpdated(QModelIndex topLeft,
    QModelIndex bottomRight)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#modelUpdated

    Parameters
    ----------

    topLeft : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    bottomRight : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QXYModelMapperPrivate::modelUpdated(QModelIndex topLeft,
    #      QModelIndex bottomRight)
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate12modelUpdatedE11QModelIndexS0_',
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
    Calls Qt's 'void QXYModelMapperPrivate::modelRowsAdded(QModelIndex
    parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#modelRowsAdded

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
    #  void QXYModelMapperPrivate::modelRowsAdded(QModelIndex parent, int
    #      start, int end)
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate14modelRowsAddedE11QModelIndexii',
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
    Calls Qt's 'void QXYModelMapperPrivate::modelRowsRemoved(QModelIndex
    parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#modelRowsRemoved

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
    #  void QXYModelMapperPrivate::modelRowsRemoved(QModelIndex parent, int
    #      start, int end)
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate16modelRowsRemovedE11QModelIndexii',
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
    Calls Qt's 'void QXYModelMapperPrivate::modelColumnsAdded(QModelIndex
    parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#modelColumnsAdded

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
    #  void QXYModelMapperPrivate::modelColumnsAdded(QModelIndex parent, int
    #      start, int end)
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate17modelColumnsAddedE11QModelIndexi'
        'i',
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
    Calls Qt's 'void QXYModelMapperPrivate::modelColumnsRemoved(QModelIndex
    parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#modelColumnsRemoved

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
    #  void QXYModelMapperPrivate::modelColumnsRemoved(QModelIndex parent,
    #      int start, int end)
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate19modelColumnsRemovedE11QModelInde'
        'xii',
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
  def handlePointAdded(self, pointPos: int) -> None:
    """
    Calls Qt's 'void QXYModelMapperPrivate::handlePointAdded(int pointPos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#handlePointAdded

    Parameters
    ----------

    pointPos : int
      Passed on as it is.
    """
    #  void QXYModelMapperPrivate::handlePointAdded(int pointPos)
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate16handlePointAddedEi', pointPos,
    )

  @overload(int)
  def handlePointRemoved(self, pointPos: int) -> None:
    """
    Calls Qt's 'void QXYModelMapperPrivate::handlePointRemoved(int
    pointPos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#handlePointRemoved

    Parameters
    ----------

    pointPos : int
      Passed on as it is.
    """
    #  void QXYModelMapperPrivate::handlePointRemoved(int pointPos)
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate18handlePointRemovedEi', pointPos,
    )

  @overload(int, int)
  def handlePointsRemoved(self, pointPos: int, count: int) -> None:
    """
    Calls Qt's 'void QXYModelMapperPrivate::handlePointsRemoved(int pointPos,
    int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#handlePointsRemoved

    Parameters
    ----------

    pointPos : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QXYModelMapperPrivate::handlePointsRemoved(int pointPos, int
    #      count)
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate19handlePointsRemovedEii',
        pointPos, count,
    )

  @overload(int)
  def handlePointReplaced(self, pointPos: int) -> None:
    """
    Calls Qt's 'void QXYModelMapperPrivate::handlePointReplaced(int
    pointPos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#handlePointReplaced

    Parameters
    ----------

    pointPos : int
      Passed on as it is.
    """
    #  void QXYModelMapperPrivate::handlePointReplaced(int pointPos)
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate19handlePointReplacedEi', pointPos,
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

  def initializeXYFromModel(self) -> None:
    """
    Calls Qt's 'void QXYModelMapperPrivate::initializeXYFromModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#initializeXYFromModel
    """
    #  void QXYModelMapperPrivate::initializeXYFromModel()
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate21initializeXYFromModelEv',
    )

  @overload(int)
  def xModelIndex(self, xPos: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QXYModelMapperPrivate::xModelIndex(int xPos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#xModelIndex

    Parameters
    ----------

    xPos : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QXYModelMapperPrivate::xModelIndex(int xPos)
    address = self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate11xModelIndexEi', xPos,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int)
  def yModelIndex(self, yPos: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QXYModelMapperPrivate::yModelIndex(int yPos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#yModelIndex

    Parameters
    ----------

    yPos : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QXYModelMapperPrivate::yModelIndex(int yPos)
    address = self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate11yModelIndexEi', yPos,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int, int)
  def insertData(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QXYModelMapperPrivate::insertData(int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#insertData

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QXYModelMapperPrivate::insertData(int start, int end)
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate10insertDataEii', start, end,
    )

  @overload(int, int)
  def removeData(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QXYModelMapperPrivate::removeData(int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxymodelmapperprivate.html#removeData

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QXYModelMapperPrivate::removeData(int start, int end)
    self.uglySide.call(
        'ritual_ZN21QXYModelMapperPrivate10removeDataEii', start, end,
    )

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
