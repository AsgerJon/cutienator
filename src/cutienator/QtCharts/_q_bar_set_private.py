"""
QBarSetPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qbarset_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QBarSetPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF
  from . import QBarSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBarSet = WAIT['QtCharts:QBarSet']
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBarSetPrivate(QObject):
  """
  The cute side of Qt's QBarSetPrivate: a plain Python object standing in
  front of one C++ QBarSetPrivate.

  It is built on the cute 'QObject', as Qt's QBarSetPrivate is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBarSetPrivate that has a ritual and that Python can
  call so far, 17 names in all: 'metaObject', 'tr', 'append', 'insert',
  'remove', 'replace', 'pos', 'value', 'setVisualsDirty', 'visualsDirty',
  'setLabelsDirty', 'labelsDirty', 'isBarSelected', 'updatedBars',
  'valueChanged', 'valueAdded', 'valueRemoved'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBarSetPrivate::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QBarSetPrivate::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QBarSetPrivate::~QBarSetPrivate()': the destructor: Python never
    removes a C++ QBarSetPrivate.
  - Qt's 'void QBarSetPrivate::append(const QList<qreal> &values)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QBarSetPrivate::setBarSelected(int index, bool selected, bool
    &callSignal)': takes a number to change where it is.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

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
  - Qt tells when it has removed the C++ QBarSetPrivate. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QBarSetPrivate that has no cute function yet,
    'setBarSelected', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString QBarSetPrivate::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#tr

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
    #  QString QBarSetPrivate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QBarSetPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBarSetPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtCharts'

  #  A C++ QBarSetPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBarSetPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBarSetPrivate::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBarSetPrivate::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QBarSetPrivate10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Calls Qt's 'bool QBarSetPrivate::isBarSelected(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#isBarSelected

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QBarSetPrivate::isBarSelected(int index) const
    return self.uglySide.call(
        'ritual_ZNK14QBarSetPrivate13isBarSelectedEi', index,
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

  @overload(str, QBarSet)
  @overload(str, NoneType)
  def __init__(self, label: str, parent: Optional[QBarSet]) -> None:
    """
    Notes what was given, for Qt's 'QBarSetPrivate::QBarSetPrivate(const
    QString label, QBarSet *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#QBarSetPrivate

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QBarSetPrivate::QBarSetPrivate(const QString label, QBarSet *parent)
    self._noteCreation(QBarSetPrivate, lambda: Rituals.call(
        'ritual_ZN14QBarSetPrivateC1E7QStringP7QBarSet',
        label, self._addressOf(parent),
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
    Calls Qt's 'void QBarSetPrivate::insert(const int index, const qreal
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void QBarSetPrivate::insert(const int index, const qreal value)
    self.uglySide.call('ritual_ZN14QBarSetPrivate6insertEid', index, value)

  @overload(int, QPointF)
  def insert(self, index: int, value: QPointF) -> None:
    """
    Calls Qt's 'void QBarSetPrivate::insert(const int index, const QPointF
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QBarSetPrivate::insert(const int index, const QPointF value)
    self.uglySide.call(
        'ritual_ZN14QBarSetPrivate6insertEi7QPointF',
        index, self._valueOf(value, 'QPointF'),
    )

  @overload(int, int)
  def remove(self, index: int, count: int) -> int:
    """
    Calls Qt's 'int QBarSetPrivate::remove(const int index, const int
    count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#remove

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  int QBarSetPrivate::remove(const int index, const int count)
    return self.uglySide.call(
        'ritual_ZN14QBarSetPrivate6removeEii', index, count,
    )

  @overload(int, float)
  def replace(self, index: int, value: float) -> None:
    """
    Calls Qt's 'void QBarSetPrivate::replace(const int index, const qreal
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#replace

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void QBarSetPrivate::replace(const int index, const qreal value)
    self.uglySide.call('ritual_ZN14QBarSetPrivate7replaceEid', index, value)

  @overload(int)
  def pos(self, index: int) -> float:
    """
    Calls Qt's 'qreal QBarSetPrivate::pos(const int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#pos

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  qreal QBarSetPrivate::pos(const int index)
    return self.uglySide.call('ritual_ZN14QBarSetPrivate3posEi', index)

  @overload(int)
  def value(self, index: int) -> float:
    """
    Calls Qt's 'qreal QBarSetPrivate::value(const int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#value

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  qreal QBarSetPrivate::value(const int index)
    return self.uglySide.call('ritual_ZN14QBarSetPrivate5valueEi', index)

  def updatedBars(self) -> None:
    """
    Calls Qt's 'void QBarSetPrivate::updatedBars()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#updatedBars
    """
    #  void QBarSetPrivate::updatedBars()
    self.uglySide.call('ritual_ZN14QBarSetPrivate11updatedBarsEv')

  @overload(int)
  def valueChanged(self, index: int) -> None:
    """
    Calls Qt's 'void QBarSetPrivate::valueChanged(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#valueChanged

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QBarSetPrivate::valueChanged(int index)
    self.uglySide.call('ritual_ZN14QBarSetPrivate12valueChangedEi', index)

  @overload(int, int)
  def valueAdded(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QBarSetPrivate::valueAdded(int index, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#valueAdded

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QBarSetPrivate::valueAdded(int index, int count)
    self.uglySide.call(
        'ritual_ZN14QBarSetPrivate10valueAddedEii', index, count,
    )

  @overload(int, int)
  def valueRemoved(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QBarSetPrivate::valueRemoved(int index, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarsetprivate.html#valueRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QBarSetPrivate::valueRemoved(int index, int count)
    self.uglySide.call(
        'ritual_ZN14QBarSetPrivate12valueRemovedEii', index, count,
    )

  @staticmethod
  def setBarSelected(*__, **_) -> Never:
    """
    Qt's 'void QBarSetPrivate::setBarSelected(int index, bool selected, bool
    &callSignal)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QBarSetPrivate.setBarSelected' has no cute function yet. Qt's "
        "'void QBarSetPrivate::setBarSelected(int index, bool selected, "
        "bool &callSignal)': takes a number to change where it is.")
