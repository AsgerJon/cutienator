"""
QBoxPlotModelMapperPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qboxplotmodelmapper_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QBoxPlotModelMapperPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QModelIndex
  from . import QBoxPlotModelMapper, QBoxSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBoxPlotModelMapper = WAIT['QBoxPlotModelMapper']
  QBoxSet = WAIT['QBoxSet']
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBoxPlotModelMapperPrivate(QObject):
  """
  The cute side of Qt's QBoxPlotModelMapperPrivate: a plain Python object
  standing in front of one C++ QBoxPlotModelMapperPrivate.

  It is built on the cute 'QObject', as Qt's QBoxPlotModelMapperPrivate is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBoxPlotModelMapperPrivate that has a ritual and
  that Python can call so far, 21 names in all: 'metaObject', 'tr',
  'modelUpdated', 'modelHeaderDataUpdated', 'modelRowsAdded',
  'modelRowsRemoved', 'modelColumnsAdded', 'modelColumnsRemoved',
  'handleModelDestroyed', 'boxSetsAdded', 'boxSetsRemoved',
  'boxValueChanged', 'handleSeriesDestroyed', 'initializeBoxFromModel',
  'boxSet', 'boxModelIndex', 'insertData', 'removeData', 'blockModelSignals',
  'blockSeriesSignals', 'q_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBoxPlotModelMapperPrivate::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QBoxPlotModelMapperPrivate::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QBoxPlotModelMapper *QBoxPlotModelMapperPrivate::q_func()
    const': takes in Python what 'QBoxPlotModelMapper
    *QBoxPlotModelMapperPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QBoxPlotModelMapperPrivate is created at the first use, not by
    'QBoxPlotModelMapperPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBoxPlotModelMapperPrivate.
  - Qt tells when it has removed the C++ QBoxPlotModelMapperPrivate. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QBoxPlotModelMapperPrivate::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxplotmodelmapperprivate.html#tr

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
    #  QString QBoxPlotModelMapperPrivate::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QBoxPlotModelMapperPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBoxPlotModelMapperPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBoxPlotModelMapperPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapperprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBoxPlotModelMapperPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QBoxPlotModelMapperPrivate10metaObjectEv',
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

  @overload(QBoxPlotModelMapper)
  @overload(NoneType)
  def __init__(self, q: Optional[QBoxPlotModelMapper]) -> None:
    """
    Notes what was given, for Qt's
    'QBoxPlotModelMapperPrivate::QBoxPlotModelMapperPrivate(
    QBoxPlotModelMapper *q)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapperprivate.html

    Parameters
    ----------

    q : Optional[QBoxPlotModelMapper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QBoxPlotModelMapperPrivate::QBoxPlotModelMapperPrivate(
    #      QBoxPlotModelMapper *q)
    self._noteCreation(QBoxPlotModelMapperPrivate, lambda: Rituals.call(
        'ritual_ZN26QBoxPlotModelMapperPrivateC1EP19QBoxPlotModelMapper',
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
    Calls Qt's 'void QBoxPlotModelMapperPrivate::modelUpdated(QModelIndex
    topLeft, QModelIndex bottomRight)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapperprivate.html#modelUpdated

    Parameters
    ----------

    topLeft : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    bottomRight : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QBoxPlotModelMapperPrivate::modelUpdated(QModelIndex topLeft,
    #      QModelIndex bottomRight)
    self.uglySide.call(
        'ritual_ZN26QBoxPlotModelMapperPrivate12modelUpdatedE11QModelIndexS'
        '0_',
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
    QBoxPlotModelMapperPrivate::modelHeaderDataUpdated(Qt::Orientation
    orientation, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapperprivate.html

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void
    #      QBoxPlotModelMapperPrivate::modelHeaderDataUpdated(Qt::Orientation
    #      orientation, int first, int last)
    self.uglySide.call(
        'ritual_ZN26QBoxPlotModelMapperPrivate22modelHeaderDataUpdatedEN2Qt'
        '11OrientationEii',
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
    Calls Qt's 'void QBoxPlotModelMapperPrivate::modelRowsAdded(QModelIndex
    parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapperprivate.html#modelRowsAdded

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
    #  void QBoxPlotModelMapperPrivate::modelRowsAdded(QModelIndex parent,
    #      int start, int end)
    self.uglySide.call(
        'ritual_ZN26QBoxPlotModelMapperPrivate14modelRowsAddedE11QModelInde'
        'xii',
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
    Calls Qt's 'void QBoxPlotModelMapperPrivate::modelRowsRemoved(QModelIndex
    parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapperprivate.html#modelRowsRemoved

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
    #  void QBoxPlotModelMapperPrivate::modelRowsRemoved(QModelIndex parent,
    #      int start, int end)
    self.uglySide.call(
        'ritual_ZN26QBoxPlotModelMapperPrivate16modelRowsRemovedE11QModelIn'
        'dexii',
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
    Calls Qt's 'void
    QBoxPlotModelMapperPrivate::modelColumnsAdded(QModelIndex parent, int
    start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapperprivate.html#modelColumnsAdded

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
    #  void QBoxPlotModelMapperPrivate::modelColumnsAdded(QModelIndex parent,
    #      int start, int end)
    self.uglySide.call(
        'ritual_ZN26QBoxPlotModelMapperPrivate17modelColumnsAddedE11QModelI'
        'ndexii',
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
    QBoxPlotModelMapperPrivate::modelColumnsRemoved(QModelIndex parent, int
    start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapperprivate.html

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
    #  void QBoxPlotModelMapperPrivate::modelColumnsRemoved(QModelIndex
    #      parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN26QBoxPlotModelMapperPrivate19modelColumnsRemovedE11QMode'
        'lIndexii',
        self._valueOf(parent), start, end,
    )

  def handleModelDestroyed(self) -> None:
    """
    Calls Qt's 'void QBoxPlotModelMapperPrivate::handleModelDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapperprivate.html
    """
    #  void QBoxPlotModelMapperPrivate::handleModelDestroyed()
    self.uglySide.call(
        'ritual_ZN26QBoxPlotModelMapperPrivate20handleModelDestroyedEv',
    )

  @overload(QList[QBoxSet])
  def boxSetsAdded(self, sets: QList[QBoxSet]) -> None:
    """
    Calls Qt's 'void QBoxPlotModelMapperPrivate::boxSetsAdded(const
    QList<QBoxSet *> &sets)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapperprivate.html#boxSetsAdded

    Parameters
    ----------

    sets : QList[QBoxSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBoxPlotModelMapperPrivate::boxSetsAdded(const QList<QBoxSet *>
    #      &sets)
    self.uglySide.call(
        'ritual_ZN26QBoxPlotModelMapperPrivate12boxSetsAddedERK5QListIP7QBo'
        'xSetE',
        self._valueOf(sets),
    )

  @overload(QList[QBoxSet])
  def boxSetsRemoved(self, sets: QList[QBoxSet]) -> None:
    """
    Calls Qt's 'void QBoxPlotModelMapperPrivate::boxSetsRemoved(const
    QList<QBoxSet *> &sets)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapperprivate.html#boxSetsRemoved

    Parameters
    ----------

    sets : QList[QBoxSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBoxPlotModelMapperPrivate::boxSetsRemoved(const QList<QBoxSet *>
    #      &sets)
    self.uglySide.call(
        'ritual_ZN26QBoxPlotModelMapperPrivate14boxSetsRemovedERK5QListIP7Q'
        'BoxSetE',
        self._valueOf(sets),
    )

  @overload(int)
  def boxValueChanged(self, index: int) -> None:
    """
    Calls Qt's 'void QBoxPlotModelMapperPrivate::boxValueChanged(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapperprivate.html#boxValueChanged

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QBoxPlotModelMapperPrivate::boxValueChanged(int index)
    self.uglySide.call(
        'ritual_ZN26QBoxPlotModelMapperPrivate15boxValueChangedEi', index,
    )

  def handleSeriesDestroyed(self) -> None:
    """
    Calls Qt's 'void QBoxPlotModelMapperPrivate::handleSeriesDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapperprivate.html
    """
    #  void QBoxPlotModelMapperPrivate::handleSeriesDestroyed()
    self.uglySide.call(
        'ritual_ZN26QBoxPlotModelMapperPrivate21handleSeriesDestroyedEv',
    )

  def initializeBoxFromModel(self) -> None:
    """
    Calls Qt's 'void QBoxPlotModelMapperPrivate::initializeBoxFromModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapperprivate.html
    """
    #  void QBoxPlotModelMapperPrivate::initializeBoxFromModel()
    self.uglySide.call(
        'ritual_ZN26QBoxPlotModelMapperPrivate22initializeBoxFromModelEv',
    )

  @overload(QModelIndex)
  def boxSet(self, index: QModelIndex) -> Optional[QBoxSet]:
    """
    Calls Qt's 'QBoxSet *QBoxPlotModelMapperPrivate::boxSet(QModelIndex
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapperprivate.html#boxSet

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QBoxSet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBoxSet *QBoxPlotModelMapperPrivate::boxSet(QModelIndex index)
    address = self.uglySide.call(
        'ritual_ZN26QBoxPlotModelMapperPrivate6boxSetE11QModelIndex',
        self._valueOf(index),
    )
    from . import QBoxSet
    return QBoxSet._cuteAt(address)

  @overload(int, int)
  def boxModelIndex(self, boxSection: int, posInBox: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QBoxPlotModelMapperPrivate::boxModelIndex(int
    boxSection, int posInBox)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapperprivate.html#boxModelIndex

    Parameters
    ----------

    boxSection : int
      Passed on as it is.

    posInBox : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QBoxPlotModelMapperPrivate::boxModelIndex(int boxSection,
    #      int posInBox)
    address = self.uglySide.call(
        'ritual_ZN26QBoxPlotModelMapperPrivate13boxModelIndexEii',
        boxSection, posInBox,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int, int)
  def insertData(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QBoxPlotModelMapperPrivate::insertData(int start, int
    end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapperprivate.html#insertData

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QBoxPlotModelMapperPrivate::insertData(int start, int end)
    self.uglySide.call(
        'ritual_ZN26QBoxPlotModelMapperPrivate10insertDataEii', start, end,
    )

  @overload(int, int)
  def removeData(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QBoxPlotModelMapperPrivate::removeData(int start, int
    end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapperprivate.html#removeData

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QBoxPlotModelMapperPrivate::removeData(int start, int end)
    self.uglySide.call(
        'ritual_ZN26QBoxPlotModelMapperPrivate10removeDataEii', start, end,
    )

  @overload()
  @overload(bool)
  def blockModelSignals(self, block: bool = True) -> None:
    """
    Calls Qt's 'void QBoxPlotModelMapperPrivate::blockModelSignals(bool
    block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapperprivate.html#blockModelSignals

    Parameters
    ----------

    block : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QBoxPlotModelMapperPrivate::blockModelSignals(bool block)
    self.uglySide.call(
        'ritual_ZN26QBoxPlotModelMapperPrivate17blockModelSignalsEb', block,
    )

  @overload()
  @overload(bool)
  def blockSeriesSignals(self, block: bool = True) -> None:
    """
    Calls Qt's 'void QBoxPlotModelMapperPrivate::blockSeriesSignals(bool
    block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapperprivate.html#blockSeriesSignals

    Parameters
    ----------

    block : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QBoxPlotModelMapperPrivate::blockSeriesSignals(bool block)
    self.uglySide.call(
        'ritual_ZN26QBoxPlotModelMapperPrivate18blockSeriesSignalsEb', block,
    )

  def q_func(self) -> Optional[QBoxPlotModelMapper]:
    """
    Calls Qt's 'QBoxPlotModelMapper *QBoxPlotModelMapperPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxplotmodelmapperprivate.html#q_func

    Returns
    -------

    Optional[QBoxPlotModelMapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBoxPlotModelMapper *QBoxPlotModelMapperPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN26QBoxPlotModelMapperPrivate6q_funcEv',
    )
    from . import QBoxPlotModelMapper
    return QBoxPlotModelMapper._cuteAt(address)
