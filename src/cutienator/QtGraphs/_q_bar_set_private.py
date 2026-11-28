"""
QBarSetPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qbarset_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QBarSetPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList, QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF
  from . import QBarSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']


class QBarSetPrivate(QObjectPrivate):
  """
  The cute side of Qt's QBarSetPrivate: a plain Python object standing in
  front of one C++ QBarSetPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QBarSetPrivate is built
  on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBarSetPrivate that has a ritual and that Python can
  call so far, 12 names in all: 'q_func', 'append', 'insert', 'remove',
  'replace', 'pos', 'value', 'setVisualsDirty', 'visualsDirty',
  'setLabelsDirty', 'labelsDirty', 'isBarSelected'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QBarSet *QBarSetPrivate::q_func() const': takes in Python
    what 'QBarSet *QBarSetPrivate::q_func()' takes.
  - Qt's 'QBarSetPrivate::~QBarSetPrivate()': the destructor: Python never
    removes a C++ QBarSetPrivate.
  - Qt's 'void QBarSetPrivate::append(const QList<qreal> &values)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QBarSetPrivate::setBarSelected(qsizetype index, bool selected,
    bool &callSignal)': takes a number to change where it is.

  What to expect
  --------------

  - The C++ QBarSetPrivate is created at the first use, not by
    'QBarSetPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBarSetPrivate.
  - Each name of Qt's QBarSetPrivate that has no cute function yet,
    'setBarSelected', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBarSetPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def pos(self, index: int) -> float:
    """
    Calls Qt's 'qreal QBarSetPrivate::pos(qsizetype index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#pos

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  qreal QBarSetPrivate::pos(qsizetype index) const
    return self.uglySide.call('ritual_ZNK14QBarSetPrivate3posEx', index)

  @overload(int)
  def value(self, index: int) -> float:
    """
    Calls Qt's 'qreal QBarSetPrivate::value(qsizetype index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#value

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  qreal QBarSetPrivate::value(qsizetype index) const
    return self.uglySide.call('ritual_ZNK14QBarSetPrivate5valueEx', index)

  def visualsDirty(self) -> bool:
    """
    Calls Qt's 'bool QBarSetPrivate::visualsDirty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#visualsDirty
    """
    #  bool QBarSetPrivate::visualsDirty() const
    return self.uglySide.call('ritual_ZNK14QBarSetPrivate12visualsDirtyEv')

  def labelsDirty(self) -> bool:
    """
    Calls Qt's 'bool QBarSetPrivate::labelsDirty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#labelsDirty
    """
    #  bool QBarSetPrivate::labelsDirty() const
    return self.uglySide.call('ritual_ZNK14QBarSetPrivate11labelsDirtyEv')

  @overload(int)
  def isBarSelected(self, index: int) -> bool:
    """
    Calls Qt's 'bool QBarSetPrivate::isBarSelected(qsizetype index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#isBarSelected

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QBarSetPrivate::isBarSelected(qsizetype index) const
    return self.uglySide.call(
        'ritual_ZNK14QBarSetPrivate13isBarSelectedEx', index,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setVisualsDirty(self, dirty: bool) -> None:
    """
    Calls Qt's 'void QBarSetPrivate::setVisualsDirty(bool dirty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarsetprivate.html#setVisualsDirty

    Parameters
    ----------

    dirty : bool
      Passed on as it is.
    """
    #  void QBarSetPrivate::setVisualsDirty(bool dirty)
    self.uglySide.call('ritual_ZN14QBarSetPrivate15setVisualsDirtyEb', dirty)

  @overload(bool)
  def setLabelsDirty(self, dirty: bool) -> None:
    """
    Calls Qt's 'void QBarSetPrivate::setLabelsDirty(bool dirty)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#setLabelsDirty

    Parameters
    ----------

    dirty : bool
      Passed on as it is.
    """
    #  void QBarSetPrivate::setLabelsDirty(bool dirty)
    self.uglySide.call('ritual_ZN14QBarSetPrivate14setLabelsDirtyEb', dirty)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def __init__(self, label: str) -> None:
    """
    Notes what was given, for Qt's 'QBarSetPrivate::QBarSetPrivate(const
    QString &label)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#QBarSetPrivate

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QBarSetPrivate::QBarSetPrivate(const QString &label)
    self._noteCreation(QBarSetPrivate, lambda: Rituals.call(
        'ritual_ZN14QBarSetPrivateC1ERK7QString', label,
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

  def q_func(self) -> Optional[QBarSet]:
    """
    Calls Qt's 'QBarSet *QBarSetPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#q_func

    Returns
    -------

    Optional[QBarSet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBarSet *QBarSetPrivate::q_func()
    address = self.uglySide.call('ritual_ZN14QBarSetPrivate6q_funcEv')
    from . import QBarSet
    return QBarSet._cuteAt(address)

  @overload(QPointF)
  def append(self, value: QPointF) -> None:
    """
    Calls Qt's 'void QBarSetPrivate::append(QPointF value)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#append

    Parameters
    ----------

    value : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QBarSetPrivate::append(QPointF value)
    self.uglySide.call(
        'ritual_ZN14QBarSetPrivate6appendE7QPointF',
        self._valueOf(value, 'QPointF'),
    )

  @overload(QList[QPointF])
  def append(self, values: QList[QPointF]) -> None:
    """
    Calls Qt's 'void QBarSetPrivate::append(const QList<QPointF> &values)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#append

    Parameters
    ----------

    values : QList[QPointF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBarSetPrivate::append(const QList<QPointF> &values)
    self.uglySide.call(
        'ritual_ZN14QBarSetPrivate6appendERK5QListI7QPointFE',
        self._valueOf(values),
    )

  @overload(int, float)
  def insert(self, index: int, value: float) -> None:
    """
    Calls Qt's 'void QBarSetPrivate::insert(qsizetype index, qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void QBarSetPrivate::insert(qsizetype index, qreal value)
    self.uglySide.call('ritual_ZN14QBarSetPrivate6insertExd', index, value)

  @overload(int, QPointF)
  def insert(self, index: int, value: QPointF) -> None:
    """
    Calls Qt's 'void QBarSetPrivate::insert(qsizetype index, QPointF value)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QBarSetPrivate::insert(qsizetype index, QPointF value)
    self.uglySide.call(
        'ritual_ZN14QBarSetPrivate6insertEx7QPointF',
        index, self._valueOf(value, 'QPointF'),
    )

  @overload(int, int)
  def remove(self, index: int, count: int) -> int:
    """
    Calls Qt's 'qsizetype QBarSetPrivate::remove(qsizetype index, qsizetype
    count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#remove

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  qsizetype QBarSetPrivate::remove(qsizetype index, qsizetype count)
    return self.uglySide.call(
        'ritual_ZN14QBarSetPrivate6removeExx', index, count,
    )

  @overload(int, float)
  def replace(self, index: int, value: float) -> None:
    """
    Calls Qt's 'void QBarSetPrivate::replace(qsizetype index, qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#replace

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void QBarSetPrivate::replace(qsizetype index, qreal value)
    self.uglySide.call('ritual_ZN14QBarSetPrivate7replaceExd', index, value)

  @staticmethod
  def setBarSelected(*__, **_) -> Never:
    """
    Qt's 'void QBarSetPrivate::setBarSelected(qsizetype index, bool selected,
    bool &callSignal)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QBarSetPrivate.setBarSelected' has no cute function yet. Qt's "
        "'void QBarSetPrivate::setBarSelected(qsizetype index, bool "
        "selected, bool &callSignal)': takes a number to change where it is."
    )
