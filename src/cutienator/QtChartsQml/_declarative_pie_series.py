"""
DeclarativePieSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtChartsQml/6.12.0/QtChartsQml/private/declarativepieseries_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means DeclarativePieSeries to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList
from ..QtQml import QQmlParserStatus
from ..QtCharts import QPieSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtCharts import QPieSlice
  from . import DeclarativePieSlice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPieSlice = WAIT['QtCharts:QPieSlice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DeclarativePieSeries(QPieSeries, QQmlParserStatus):
  """
  The cute side of Qt's DeclarativePieSeries: a plain Python object standing
  in front of one C++ DeclarativePieSeries.

  It is built on the cute 'QPieSeries', as Qt's DeclarativePieSeries is built
  on Qt's QPieSeries, and has everything that class has. It is built on the
  cute 'QQmlParserStatus' as well, as Qt's DeclarativePieSeries is built on
  Qt's QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's DeclarativePieSeries that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'at', 'find',
  'append', 'remove', 'clear', 'classBegin', 'componentComplete',
  'sliceAdded', 'sliceRemoved', 'handleAdded', 'handleRemoved'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *DeclarativePieSeries::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int DeclarativePieSeries::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlListProperty<QObject> DeclarativePieSeries::seriesChildren()':
    gives a type Python has no way to take yet.
  - Qt's 'void
    DeclarativePieSeries::appendSeriesChildren(QQmlListProperty<QObject>
    *list, QObject *element)': names 'QQmlListProperty<QObject>', which has
    no cute class yet.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 2 not a gap; 1 leans on
  'DeclarativePieSeries; 1 leans on 'vtable for DeclarativePieSeries', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken.

  What to expect
  --------------

  - The C++ DeclarativePieSeries is created at the first use, not by
    'DeclarativePieSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DeclarativePieSeries.
  - Qt tells when it has removed the C++ DeclarativePieSeries. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's DeclarativePieSeries that has no cute function yet,
    '__init__', 'appendSeriesChildren', 'seriesChildren', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DeclarativePieSeries'

  #  Qt's DeclarativePieSeries is built on more than one class. The part of a
  #  C++ DeclarativePieSeries that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_DeclarativePieSeries_QQmlParserStatus',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *DeclarativePieSeries::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativepieseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *DeclarativePieSeries::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20DeclarativePieSeries10metaObjectEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'DeclarativePieSeries::DeclarativePieSeries(QQuickItem *parent)':
    leans on 'vtable for DeclarativePieSeries', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'DeclarativePieSeries.__init__' has no cute function yet. Qt's "
        "'DeclarativePieSeries::DeclarativePieSeries(QQuickItem *parent)': "
        "leans on 'vtable for DeclarativePieSeries', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  @overload(int)
  def at(self, index: int) -> Optional[QPieSlice]:
    """
    Calls Qt's 'QPieSlice *DeclarativePieSeries::at(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativepieseries.html#at

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QPieSlice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSlice *DeclarativePieSeries::at(int index)
    address = self.uglySide.call(
        'ritual_ZN20DeclarativePieSeries2atEi', index,
    )
    from ..QtCharts import QPieSlice
    return QPieSlice._cuteAt(address)

  @overload(str)
  def find(self, label: str) -> Optional[QPieSlice]:
    """
    Calls Qt's 'QPieSlice *DeclarativePieSeries::find(QString label)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativepieseries.html#find

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QPieSlice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSlice *DeclarativePieSeries::find(QString label)
    address = self.uglySide.call(
        'ritual_ZN20DeclarativePieSeries4findE7QString', label,
    )
    from ..QtCharts import QPieSlice
    return QPieSlice._cuteAt(address)

  @overload(str, float)
  def append(
      self,
      label: str,
      value: float,
  ) -> Optional[DeclarativePieSlice]:
    """
    Calls Qt's 'DeclarativePieSlice *DeclarativePieSeries::append(QString
    label, qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativepieseries.html#append

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.

    value : float
      Passed on as it is.

    Returns
    -------

    Optional[DeclarativePieSlice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DeclarativePieSlice *DeclarativePieSeries::append(QString label, qreal
    #      value)
    address = self.uglySide.call(
        'ritual_ZN20DeclarativePieSeries6appendE7QStringd', label, value,
    )
    from . import DeclarativePieSlice
    return DeclarativePieSlice._cuteAt(address)

  @overload(QPieSlice)
  @overload(NoneType)
  def remove(self, slice: Optional[QPieSlice]) -> bool:
    """
    Calls Qt's 'bool DeclarativePieSeries::remove(QPieSlice *slice)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativepieseries.html#remove

    Parameters
    ----------

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool DeclarativePieSeries::remove(QPieSlice *slice)
    return self.uglySide.call(
        'ritual_ZN20DeclarativePieSeries6removeEP9QPieSlice',
        self._addressOf(slice),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void DeclarativePieSeries::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativepieseries.html#clear
    """
    #  void DeclarativePieSeries::clear()
    self.uglySide.call('ritual_ZN20DeclarativePieSeries5clearEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void DeclarativePieSeries::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativepieseries.html#classBegin
    """
    #  void DeclarativePieSeries::classBegin()
    ritual = 'ritual_ZN20DeclarativePieSeries10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20DeclarativePieSeries10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void DeclarativePieSeries::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativepieseries.html#componentComplete
    """
    #  void DeclarativePieSeries::componentComplete()
    ritual = 'ritual_ZN20DeclarativePieSeries17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20DeclarativePieSeries17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QPieSlice)
  @overload(NoneType)
  def sliceAdded(self, slice: Optional[QPieSlice]) -> None:
    """
    Calls Qt's 'void DeclarativePieSeries::sliceAdded(QPieSlice *slice)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativepieseries.html#sliceAdded

    Parameters
    ----------

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativePieSeries::sliceAdded(QPieSlice *slice)
    self.uglySide.call(
        'ritual_ZN20DeclarativePieSeries10sliceAddedEP9QPieSlice',
        self._addressOf(slice),
    )

  @overload(QPieSlice)
  @overload(NoneType)
  def sliceRemoved(self, slice: Optional[QPieSlice]) -> None:
    """
    Calls Qt's 'void DeclarativePieSeries::sliceRemoved(QPieSlice *slice)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativepieseries.html#sliceRemoved

    Parameters
    ----------

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativePieSeries::sliceRemoved(QPieSlice *slice)
    self.uglySide.call(
        'ritual_ZN20DeclarativePieSeries12sliceRemovedEP9QPieSlice',
        self._addressOf(slice),
    )

  @overload(QList[QPieSlice])
  def handleAdded(self, slices: QList[QPieSlice]) -> None:
    """
    Calls Qt's 'void DeclarativePieSeries::handleAdded(const QList<QPieSlice
    *> &slices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativepieseries.html#handleAdded

    Parameters
    ----------

    slices : QList[QPieSlice]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DeclarativePieSeries::handleAdded(const QList<QPieSlice *>
    #      &slices)
    self.uglySide.call(
        'ritual_ZN20DeclarativePieSeries11handleAddedERK5QListIP9QPieSliceE',
        self._valueOf(slices),
    )

  @overload(QList[QPieSlice])
  def handleRemoved(self, slices: QList[QPieSlice]) -> None:
    """
    Calls Qt's 'void DeclarativePieSeries::handleRemoved(const
    QList<QPieSlice *> &slices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativepieseries.html#handleRemoved

    Parameters
    ----------

    slices : QList[QPieSlice]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DeclarativePieSeries::handleRemoved(const QList<QPieSlice *>
    #      &slices)
    self.uglySide.call(
        'ritual_ZN20DeclarativePieSeries13handleRemovedERK5QListIP9QPieSlic'
        'eE',
        self._valueOf(slices),
    )

  @staticmethod
  def appendSeriesChildren(*__, **_) -> Never:
    """
    Qt's 'void
    DeclarativePieSeries::appendSeriesChildren(QQmlListProperty<QObject>
    *list, QObject *element)': names 'QQmlListProperty<QObject>', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'DeclarativePieSeries.appendSeriesChildren' has no cute function "
        "yet. Qt's 'void "
        "DeclarativePieSeries::appendSeriesChildren(QQmlListProperty<QObject"
        "> *list, QObject *element)': names 'QQmlListProperty<QObject>', "
        "which has no cute class yet.")

  @staticmethod
  def seriesChildren(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> DeclarativePieSeries::seriesChildren()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'DeclarativePieSeries.seriesChildren' has no cute function yet. "
        "Qt's 'QQmlListProperty<QObject> "
        "DeclarativePieSeries::seriesChildren()': gives a type Python has "
        "no way to take yet.")
