"""
QBarSet binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qbarset.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtGui import QColor
  from . import QBarSetPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBarSet(QObject):
  """
  The cute side of Qt's QBarSet: a plain Python object standing in front of
  one C++ QBarSet.

  It is built on the cute 'QObject', as Qt's QBarSet is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBarSet that has a ritual and that Python can call
  so far, 47 names in all: 'metaObject', 'tr', 'd_func', 'setLabel', 'label',
  'append', 'insert', 'remove', 'replace', 'at', 'count', 'sum', 'clear',
  '__getitem__', 'color', 'setColor', 'borderColor', 'setBorderColor',
  'labelColor', 'setLabelColor', 'selectedColor', 'setSelectedColor',
  'values', 'setValues', 'borderWidth', 'setBorderWidth', 'isBarSelected',
  'selectBar', 'deselectBar', 'setBarSelected', 'selectAllBars',
  'deselectAllBars', 'update', 'labelChanged', 'colorChanged',
  'borderColorChanged', 'labelColorChanged', 'valuesChanged',
  'selectedColorChanged', 'countChanged', 'borderWidthChanged',
  'valuesAdded', 'valuesRemoved', 'valueChanged', 'updatedBars',
  'valueAdded', 'valueRemoved'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBarSet::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QBarSet::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.
  - Qt's 'const QBarSetPrivate *QBarSet::d_func() const': takes in Python
    what 'QBarSetPrivate *QBarSet::d_func()' takes.
  - Qt's 'QBarSet::~QBarSet()': the destructor: Python never removes a C++
    QBarSet.
  - Qt's 'void QBarSet::append(const QList<qreal> &values)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QBarSet &QBarSet::operator<<(qreal value)': gives a type Python has
    no way to take yet.
  - Qt's 'void QBarSet::selectBars(const QList<qsizetype> &indexes)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QBarSet::deselectBars(const QList<qsizetype> &indexes)': takes
    a type Python has no way to hand over yet.
  - Qt's 'void QBarSet::toggleSelection(const QList<qsizetype> &indexes)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QList<qsizetype> QBarSet::selectedBars() const': gives a type
    Python has no way to take yet.
  - Qt's 'void QBarSet::selectedBarsChanged(const QList<qsizetype>
    &indexes)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 64 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QBarSet is created at the first use, not by 'QBarSet(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBarSet.
  - Qt tells when it has removed the C++ QBarSet. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QBarSet that has no cute function yet, 'deselectBars',
    'selectBars', 'selectedBars', 'selectedBarsChanged', 'toggleSelection',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
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
    Calls Qt's 'QString QBarSet::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#tr

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
    #  QString QBarSet::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7QBarSet2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBarSet'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QBarSet Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBarSet'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBarSet::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBarSet::metaObject() const
    address = self.uglySide.call('ritual_ZNK7QBarSet10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def label(self) -> str:
    """
    Calls Qt's 'QString QBarSet::label() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#label

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBarSet::label() const
    return self.uglySide.call('ritual_ZNK7QBarSet5labelEv')

  @overload(int)
  def at(self, index: int) -> float:
    """
    Calls Qt's 'qreal QBarSet::at(qsizetype index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#at

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  qreal QBarSet::at(qsizetype index) const
    return self.uglySide.call('ritual_ZNK7QBarSet2atEx', index)

  def count(self) -> int:
    """
    Calls Qt's 'qsizetype QBarSet::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#count
    """
    #  qsizetype QBarSet::count() const
    return self.uglySide.call('ritual_ZNK7QBarSet5countEv')

  def sum(self) -> float:
    """
    Calls Qt's 'qreal QBarSet::sum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#sum
    """
    #  qreal QBarSet::sum() const
    return self.uglySide.call('ritual_ZNK7QBarSet3sumEv')

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QBarSet::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QBarSet::color() const
    address = self.uglySide.call('ritual_ZNK7QBarSet5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def borderColor(self) -> QColor:
    """
    Calls Qt's 'QColor QBarSet::borderColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#borderColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QBarSet::borderColor() const
    address = self.uglySide.call('ritual_ZNK7QBarSet11borderColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def labelColor(self) -> QColor:
    """
    Calls Qt's 'QColor QBarSet::labelColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#labelColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QBarSet::labelColor() const
    address = self.uglySide.call('ritual_ZNK7QBarSet10labelColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def selectedColor(self) -> QColor:
    """
    Calls Qt's 'QColor QBarSet::selectedColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#selectedColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QBarSet::selectedColor() const
    address = self.uglySide.call('ritual_ZNK7QBarSet13selectedColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def values(self) -> QList[QVariant]:
    """
    Calls Qt's 'QVariantList QBarSet::values() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#values

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QVariantList QBarSet::values() const
    address = self.uglySide.call('ritual_ZNK7QBarSet6valuesEv')
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)

  def borderWidth(self) -> float:
    """
    Calls Qt's 'qreal QBarSet::borderWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#borderWidth
    """
    #  qreal QBarSet::borderWidth() const
    return self.uglySide.call('ritual_ZNK7QBarSet11borderWidthEv')

  @overload(int)
  def isBarSelected(self, index: int) -> bool:
    """
    Calls Qt's 'bool QBarSet::isBarSelected(qsizetype index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#isBarSelected

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QBarSet::isBarSelected(qsizetype index) const
    return self.uglySide.call('ritual_ZNK7QBarSet13isBarSelectedEx', index)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setLabel(self, label: str) -> None:
    """
    Calls Qt's 'void QBarSet::setLabel(const QString &label)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#setLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBarSet::setLabel(const QString &label)
    self.uglySide.call('ritual_ZN7QBarSet8setLabelERK7QString', label)

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QBarSet::setColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QBarSet::setColor(QColor color)
    self.uglySide.call(
        'ritual_ZN7QBarSet8setColorE6QColor', self._valueOf(color),
    )

  @overload(QColor)
  def setBorderColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QBarSet::setBorderColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#setBorderColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QBarSet::setBorderColor(QColor color)
    self.uglySide.call(
        'ritual_ZN7QBarSet14setBorderColorE6QColor', self._valueOf(color),
    )

  @overload(QColor)
  def setLabelColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QBarSet::setLabelColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#setLabelColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QBarSet::setLabelColor(QColor color)
    self.uglySide.call(
        'ritual_ZN7QBarSet13setLabelColorE6QColor', self._valueOf(color),
    )

  @overload(QColor)
  def setSelectedColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QBarSet::setSelectedColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#setSelectedColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QBarSet::setSelectedColor(QColor color)
    self.uglySide.call(
        'ritual_ZN7QBarSet16setSelectedColorE6QColor', self._valueOf(color),
    )

  @overload(QList[QVariant])
  def setValues(self, values: QList[QVariant]) -> None:
    """
    Calls Qt's 'void QBarSet::setValues(const QVariantList &values)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#setValues

    Parameters
    ----------

    values : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBarSet::setValues(const QVariantList &values)
    self.uglySide.call(
        'ritual_ZN7QBarSet9setValuesERK5QListI8QVariantE',
        self._valueOf(values),
    )

  @overload(float)
  def setBorderWidth(self, borderWidth: float) -> None:
    """
    Calls Qt's 'void QBarSet::setBorderWidth(qreal borderWidth)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#setBorderWidth

    Parameters
    ----------

    borderWidth : float
      Passed on as it is.
    """
    #  void QBarSet::setBorderWidth(qreal borderWidth)
    self.uglySide.call('ritual_ZN7QBarSet14setBorderWidthEd', borderWidth)

  @overload(int, bool)
  def setBarSelected(self, index: int, selected: bool) -> None:
    """
    Calls Qt's 'void QBarSet::setBarSelected(qsizetype index, bool
    selected)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#setBarSelected

    Parameters
    ----------

    index : int
      Passed on as it is.

    selected : bool
      Passed on as it is.
    """
    #  void QBarSet::setBarSelected(qsizetype index, bool selected)
    self.uglySide.call(
        'ritual_ZN7QBarSet14setBarSelectedExb', index, selected,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def __getitem__(self, index: int) -> float:
    """
    Calls Qt's 'qreal QBarSet::operator[](qsizetype index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#operator[]

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  qreal QBarSet::operator[](qsizetype index) const
    return self.uglySide.call('ritual_ZNK7QBarSetixEx', index)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QBarSet::QBarSet(QObject *parent)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#QBarSet

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBarSet::QBarSet(QObject *parent)
    self._noteCreation(QBarSet, lambda: Rituals.call(
        'ritual_ZN7QBarSetC1EP7QObject', self._addressOf(parent, 'QObject'),
    ))

  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(self, label: str, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QBarSet::QBarSet(const QString &label,
    QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#QBarSet

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBarSet::QBarSet(const QString &label, QObject *parent)
    self._noteCreation(QBarSet, lambda: Rituals.call(
        'ritual_ZN7QBarSetC1ERK7QStringP7QObject',
        label, self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QBarSetPrivate]:
    """
    Calls Qt's 'QBarSetPrivate *QBarSet::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#d_func

    Returns
    -------

    Optional[QBarSetPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBarSetPrivate *QBarSet::d_func()
    address = self.uglySide.call('ritual_ZN7QBarSet6d_funcEv')
    from . import QBarSetPrivate
    return QBarSetPrivate._cuteAt(address)

  @overload(float)
  def append(self, value: float) -> None:
    """
    Calls Qt's 'void QBarSet::append(qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#append

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QBarSet::append(qreal value)
    self.uglySide.call('ritual_ZN7QBarSet6appendEd', value)

  @overload(int, float)
  def insert(self, index: int, value: float) -> None:
    """
    Calls Qt's 'void QBarSet::insert(qsizetype index, qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void QBarSet::insert(qsizetype index, qreal value)
    self.uglySide.call('ritual_ZN7QBarSet6insertExd', index, value)

  @overload(int)
  @overload(int, int)
  def remove(self, index: int, count: int = 1) -> None:
    """
    Calls Qt's 'void QBarSet::remove(qsizetype index, qsizetype count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#remove

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QBarSet::remove(qsizetype index, qsizetype count)
    self.uglySide.call('ritual_ZN7QBarSet6removeExx', index, count)

  @overload(int, float)
  def replace(self, index: int, value: float) -> None:
    """
    Calls Qt's 'void QBarSet::replace(qsizetype index, qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#replace

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void QBarSet::replace(qsizetype index, qreal value)
    self.uglySide.call('ritual_ZN7QBarSet7replaceExd', index, value)

  def clear(self) -> None:
    """
    Calls Qt's 'void QBarSet::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#clear
    """
    #  void QBarSet::clear()
    self.uglySide.call('ritual_ZN7QBarSet5clearEv')

  @overload(int)
  def selectBar(self, index: int) -> None:
    """
    Calls Qt's 'void QBarSet::selectBar(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#selectBar

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QBarSet::selectBar(qsizetype index)
    self.uglySide.call('ritual_ZN7QBarSet9selectBarEx', index)

  @overload(int)
  def deselectBar(self, index: int) -> None:
    """
    Calls Qt's 'void QBarSet::deselectBar(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#deselectBar

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QBarSet::deselectBar(qsizetype index)
    self.uglySide.call('ritual_ZN7QBarSet11deselectBarEx', index)

  def selectAllBars(self) -> None:
    """
    Calls Qt's 'void QBarSet::selectAllBars()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#selectAllBars
    """
    #  void QBarSet::selectAllBars()
    self.uglySide.call('ritual_ZN7QBarSet13selectAllBarsEv')

  def deselectAllBars(self) -> None:
    """
    Calls Qt's 'void QBarSet::deselectAllBars()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#deselectAllBars
    """
    #  void QBarSet::deselectAllBars()
    self.uglySide.call('ritual_ZN7QBarSet15deselectAllBarsEv')

  def update(self) -> None:
    """
    Calls Qt's 'void QBarSet::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#update
    """
    #  void QBarSet::update()
    self.uglySide.call('ritual_ZN7QBarSet6updateEv')

  def labelChanged(self) -> None:
    """
    Calls Qt's 'void QBarSet::labelChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#labelChanged
    """
    #  void QBarSet::labelChanged()
    self.uglySide.call('ritual_ZN7QBarSet12labelChangedEv')

  @overload(QColor)
  def colorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QBarSet::colorChanged(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#colorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QBarSet::colorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN7QBarSet12colorChangedE6QColor', self._valueOf(color),
    )

  @overload(QColor)
  def borderColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QBarSet::borderColorChanged(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#borderColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QBarSet::borderColorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN7QBarSet18borderColorChangedE6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def labelColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QBarSet::labelColorChanged(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#labelColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QBarSet::labelColorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN7QBarSet17labelColorChangedE6QColor', self._valueOf(color),
    )

  def valuesChanged(self) -> None:
    """
    Calls Qt's 'void QBarSet::valuesChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#valuesChanged
    """
    #  void QBarSet::valuesChanged()
    self.uglySide.call('ritual_ZN7QBarSet13valuesChangedEv')

  @overload(QColor)
  def selectedColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QBarSet::selectedColorChanged(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#selectedColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QBarSet::selectedColorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN7QBarSet20selectedColorChangedE6QColor',
        self._valueOf(color),
    )

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QBarSet::countChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#countChanged
    """
    #  void QBarSet::countChanged()
    self.uglySide.call('ritual_ZN7QBarSet12countChangedEv')

  @overload(float)
  def borderWidthChanged(self, width: float) -> None:
    """
    Calls Qt's 'void QBarSet::borderWidthChanged(qreal width)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#borderWidthChanged

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QBarSet::borderWidthChanged(qreal width)
    self.uglySide.call('ritual_ZN7QBarSet18borderWidthChangedEd', width)

  @overload(int, int)
  def valuesAdded(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QBarSet::valuesAdded(qsizetype index, qsizetype count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#valuesAdded

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QBarSet::valuesAdded(qsizetype index, qsizetype count)
    self.uglySide.call('ritual_ZN7QBarSet11valuesAddedExx', index, count)

  @overload(int, int)
  def valuesRemoved(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QBarSet::valuesRemoved(qsizetype index, qsizetype
    count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#valuesRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QBarSet::valuesRemoved(qsizetype index, qsizetype count)
    self.uglySide.call('ritual_ZN7QBarSet13valuesRemovedExx', index, count)

  @overload(int)
  def valueChanged(self, index: int) -> None:
    """
    Calls Qt's 'void QBarSet::valueChanged(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#valueChanged

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QBarSet::valueChanged(qsizetype index)
    self.uglySide.call('ritual_ZN7QBarSet12valueChangedEx', index)

  def updatedBars(self) -> None:
    """
    Calls Qt's 'void QBarSet::updatedBars()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#updatedBars
    """
    #  void QBarSet::updatedBars()
    self.uglySide.call('ritual_ZN7QBarSet11updatedBarsEv')

  @overload(int, int)
  def valueAdded(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QBarSet::valueAdded(qsizetype index, qsizetype count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#valueAdded

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QBarSet::valueAdded(qsizetype index, qsizetype count)
    self.uglySide.call('ritual_ZN7QBarSet10valueAddedExx', index, count)

  @overload(int, int)
  def valueRemoved(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QBarSet::valueRemoved(qsizetype index, qsizetype
    count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#valueRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QBarSet::valueRemoved(qsizetype index, qsizetype count)
    self.uglySide.call('ritual_ZN7QBarSet12valueRemovedExx', index, count)

  @staticmethod
  def deselectBars(*__, **_) -> Never:
    """
    Qt's 'void QBarSet::deselectBars(const QList<qsizetype> &indexes)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBarSet.deselectBars' has no cute function yet. Qt's 'void "
        "QBarSet::deselectBars(const QList<qsizetype> &indexes)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def selectBars(*__, **_) -> Never:
    """
    Qt's 'void QBarSet::selectBars(const QList<qsizetype> &indexes)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBarSet.selectBars' has no cute function yet. Qt's 'void "
        "QBarSet::selectBars(const QList<qsizetype> &indexes)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def selectedBars(*__, **_) -> Never:
    """
    Qt's 'QList<qsizetype> QBarSet::selectedBars() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QBarSet.selectedBars' has no cute function yet. Qt's "
        "'QList<qsizetype> QBarSet::selectedBars() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def selectedBarsChanged(*__, **_) -> Never:
    """
    Qt's 'void QBarSet::selectedBarsChanged(const QList<qsizetype>
    &indexes)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBarSet.selectedBarsChanged' has no cute function yet. Qt's 'void "
        "QBarSet::selectedBarsChanged(const QList<qsizetype> &indexes)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def toggleSelection(*__, **_) -> Never:
    """
    Qt's 'void QBarSet::toggleSelection(const QList<qsizetype> &indexes)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBarSet.toggleSelection' has no cute function yet. Qt's 'void "
        "QBarSet::toggleSelection(const QList<qsizetype> &indexes)': takes "
        "a type Python has no way to hand over yet.")


#  Qt's 'QList<QBarSet *>': the list of QBarSet, which 'QList[QBarSet]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QBarSet.
QList.createKind(
    QBarSet, 'address',
    make='ritual_list_make_QBarSet_ptr',
    add='ritual_list_add_QBarSet_ptr',
    size='ritual_list_size_QBarSet_ptr',
    at='ritual_list_at_QBarSet_ptr',
    drop='ritual_list_drop_QBarSet_ptr',
)
