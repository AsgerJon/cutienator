"""
QBarSet binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qbarset.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QBrush, QColor, QFont, QPen
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QColor = WAIT['QColor']
  QFont = WAIT['QFont']
  QPen = WAIT['QPen']

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
  so far, 51 names in all: 'metaObject', 'tr', 'setLabel', 'label', 'append',
  'insert', 'remove', 'replace', 'at', '__getitem__', 'count', 'sum',
  'setPen', 'pen', 'setBrush', 'brush', 'setLabelBrush', 'labelBrush',
  'setLabelFont', 'labelFont', 'color', 'setColor', 'borderColor',
  'setBorderColor', 'labelColor', 'setLabelColor', 'selectedColor',
  'setSelectedColor', 'isBarSelected', 'selectBar', 'deselectBar',
  'setBarSelected', 'selectAllBars', 'deselectAllBars', 'clicked', 'hovered',
  'pressed', 'released', 'doubleClicked', 'penChanged', 'brushChanged',
  'labelChanged', 'labelBrushChanged', 'labelFontChanged', 'colorChanged',
  'borderColorChanged', 'labelColorChanged', 'selectedColorChanged',
  'valuesAdded', 'valuesRemoved', 'valueChanged'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBarSet::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QBarSet::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.
  - Qt's 'QBarSet::~QBarSet()': the destructor: Python never removes a C++
    QBarSet.
  - Qt's 'void QBarSet::append(const QList<qreal> &values)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QBarSet &QBarSet::operator<<(const qreal &value)': gives a type
    Python has no way to take yet.
  - Qt's 'void QBarSet::selectBars(const QList<int> &indexes)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QBarSet::deselectBars(const QList<int> &indexes)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QBarSet::toggleSelection(const QList<int> &indexes)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QList<int> QBarSet::selectedBars() const': gives a type Python has
    no way to take yet.
  - Qt's 'void QBarSet::selectedBarsChanged(const QList<int> &indexes)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 66 functions Qt declares: 2 not a gap; 2 forbidden.

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
  __qt_part__ = 'QtCharts'

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
    Calls Qt's 'qreal QBarSet::at(const int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#at

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  qreal QBarSet::at(const int index) const
    return self.uglySide.call('ritual_ZNK7QBarSet2atEi', index)

  def count(self) -> int:
    """
    Calls Qt's 'int QBarSet::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#count
    """
    #  int QBarSet::count() const
    return self.uglySide.call('ritual_ZNK7QBarSet5countEv')

  def sum(self) -> float:
    """
    Calls Qt's 'qreal QBarSet::sum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#sum
    """
    #  qreal QBarSet::sum() const
    return self.uglySide.call('ritual_ZNK7QBarSet3sumEv')

  def pen(self) -> QPen:
    """
    Calls Qt's 'QPen QBarSet::pen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#pen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QBarSet::pen() const
    address = self.uglySide.call('ritual_ZNK7QBarSet3penEv')
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def brush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QBarSet::brush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#brush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QBarSet::brush() const
    address = self.uglySide.call('ritual_ZNK7QBarSet5brushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def labelBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QBarSet::labelBrush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#labelBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QBarSet::labelBrush() const
    address = self.uglySide.call('ritual_ZNK7QBarSet10labelBrushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def labelFont(self) -> QFont:
    """
    Calls Qt's 'QFont QBarSet::labelFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#labelFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QBarSet::labelFont() const
    address = self.uglySide.call('ritual_ZNK7QBarSet9labelFontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

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

  @overload(int)
  def isBarSelected(self, index: int) -> bool:
    """
    Calls Qt's 'bool QBarSet::isBarSelected(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#isBarSelected

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QBarSet::isBarSelected(int index) const
    return self.uglySide.call('ritual_ZNK7QBarSet13isBarSelectedEi', index)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setLabel(self, label: str) -> None:
    """
    Calls Qt's 'void QBarSet::setLabel(const QString label)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#setLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBarSet::setLabel(const QString label)
    self.uglySide.call('ritual_ZN7QBarSet8setLabelE7QString', label)

  @overload(QPen)
  def setPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QBarSet::setPen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#setPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QBarSet::setPen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN7QBarSet6setPenERK4QPen', self._valueOf(pen),
    )

  @overload(QBrush)
  def setBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QBarSet::setBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#setBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QBarSet::setBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN7QBarSet8setBrushERK6QBrush', self._valueOf(brush),
    )

  @overload(QBrush)
  def setLabelBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QBarSet::setLabelBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#setLabelBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QBarSet::setLabelBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN7QBarSet13setLabelBrushERK6QBrush', self._valueOf(brush),
    )

  @overload(QFont)
  def setLabelFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QBarSet::setLabelFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#setLabelFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QBarSet::setLabelFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN7QBarSet12setLabelFontERK5QFont', self._valueOf(font),
    )

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
    Calls Qt's 'void QBarSet::setSelectedColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#setSelectedColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QBarSet::setSelectedColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN7QBarSet16setSelectedColorERK6QColor',
        self._valueOf(color),
    )

  @overload(int, bool)
  def setBarSelected(self, index: int, selected: bool) -> None:
    """
    Calls Qt's 'void QBarSet::setBarSelected(int index, bool selected)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#setBarSelected

    Parameters
    ----------

    index : int
      Passed on as it is.

    selected : bool
      Passed on as it is.
    """
    #  void QBarSet::setBarSelected(int index, bool selected)
    self.uglySide.call(
        'ritual_ZN7QBarSet14setBarSelectedEib', index, selected,
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
    Calls Qt's 'qreal QBarSet::operator[](const int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#operator[]

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  qreal QBarSet::operator[](const int index) const
    return self.uglySide.call('ritual_ZNK7QBarSetixEi', index)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(self, label: str, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QBarSet::QBarSet(const QString label,
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
    #  QBarSet::QBarSet(const QString label, QObject *parent)
    self._noteCreation(QBarSet, lambda: Rituals.call(
        'ritual_ZN7QBarSetC1E7QStringP7QObject',
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

  @overload(float)
  def append(self, value: float) -> None:
    """
    Calls Qt's 'void QBarSet::append(const qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#append

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QBarSet::append(const qreal value)
    self.uglySide.call('ritual_ZN7QBarSet6appendEd', value)

  @overload(int, float)
  def insert(self, index: int, value: float) -> None:
    """
    Calls Qt's 'void QBarSet::insert(const int index, const qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void QBarSet::insert(const int index, const qreal value)
    self.uglySide.call('ritual_ZN7QBarSet6insertEid', index, value)

  @overload(int)
  @overload(int, int)
  def remove(self, index: int, count: int = 1) -> None:
    """
    Calls Qt's 'void QBarSet::remove(const int index, const int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#remove

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QBarSet::remove(const int index, const int count)
    self.uglySide.call('ritual_ZN7QBarSet6removeEii', index, count)

  @overload(int, float)
  def replace(self, index: int, value: float) -> None:
    """
    Calls Qt's 'void QBarSet::replace(const int index, const qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#replace

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void QBarSet::replace(const int index, const qreal value)
    self.uglySide.call('ritual_ZN7QBarSet7replaceEid', index, value)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QBarSet::color()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QBarSet::color()
    address = self.uglySide.call('ritual_ZN7QBarSet5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def borderColor(self) -> QColor:
    """
    Calls Qt's 'QColor QBarSet::borderColor()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#borderColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QBarSet::borderColor()
    address = self.uglySide.call('ritual_ZN7QBarSet11borderColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def labelColor(self) -> QColor:
    """
    Calls Qt's 'QColor QBarSet::labelColor()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#labelColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QBarSet::labelColor()
    address = self.uglySide.call('ritual_ZN7QBarSet10labelColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(int)
  def selectBar(self, index: int) -> None:
    """
    Calls Qt's 'void QBarSet::selectBar(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#selectBar

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QBarSet::selectBar(int index)
    self.uglySide.call('ritual_ZN7QBarSet9selectBarEi', index)

  @overload(int)
  def deselectBar(self, index: int) -> None:
    """
    Calls Qt's 'void QBarSet::deselectBar(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#deselectBar

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QBarSet::deselectBar(int index)
    self.uglySide.call('ritual_ZN7QBarSet11deselectBarEi', index)

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

  @overload(int)
  def clicked(self, index: int) -> None:
    """
    Calls Qt's 'void QBarSet::clicked(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#clicked

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QBarSet::clicked(int index)
    self.uglySide.call('ritual_ZN7QBarSet7clickedEi', index)

  @overload(bool, int)
  def hovered(self, status: bool, index: int) -> None:
    """
    Calls Qt's 'void QBarSet::hovered(bool status, int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#hovered

    Parameters
    ----------

    status : bool
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QBarSet::hovered(bool status, int index)
    self.uglySide.call('ritual_ZN7QBarSet7hoveredEbi', status, index)

  @overload(int)
  def pressed(self, index: int) -> None:
    """
    Calls Qt's 'void QBarSet::pressed(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#pressed

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QBarSet::pressed(int index)
    self.uglySide.call('ritual_ZN7QBarSet7pressedEi', index)

  @overload(int)
  def released(self, index: int) -> None:
    """
    Calls Qt's 'void QBarSet::released(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#released

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QBarSet::released(int index)
    self.uglySide.call('ritual_ZN7QBarSet8releasedEi', index)

  @overload(int)
  def doubleClicked(self, index: int) -> None:
    """
    Calls Qt's 'void QBarSet::doubleClicked(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#doubleClicked

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QBarSet::doubleClicked(int index)
    self.uglySide.call('ritual_ZN7QBarSet13doubleClickedEi', index)

  def penChanged(self) -> None:
    """
    Calls Qt's 'void QBarSet::penChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#penChanged
    """
    #  void QBarSet::penChanged()
    self.uglySide.call('ritual_ZN7QBarSet10penChangedEv')

  def brushChanged(self) -> None:
    """
    Calls Qt's 'void QBarSet::brushChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#brushChanged
    """
    #  void QBarSet::brushChanged()
    self.uglySide.call('ritual_ZN7QBarSet12brushChangedEv')

  def labelChanged(self) -> None:
    """
    Calls Qt's 'void QBarSet::labelChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#labelChanged
    """
    #  void QBarSet::labelChanged()
    self.uglySide.call('ritual_ZN7QBarSet12labelChangedEv')

  def labelBrushChanged(self) -> None:
    """
    Calls Qt's 'void QBarSet::labelBrushChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#labelBrushChanged
    """
    #  void QBarSet::labelBrushChanged()
    self.uglySide.call('ritual_ZN7QBarSet17labelBrushChangedEv')

  def labelFontChanged(self) -> None:
    """
    Calls Qt's 'void QBarSet::labelFontChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#labelFontChanged
    """
    #  void QBarSet::labelFontChanged()
    self.uglySide.call('ritual_ZN7QBarSet16labelFontChangedEv')

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

  @overload(QColor)
  def selectedColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QBarSet::selectedColorChanged(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#selectedColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QBarSet::selectedColorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN7QBarSet20selectedColorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(int, int)
  def valuesAdded(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QBarSet::valuesAdded(int index, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#valuesAdded

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QBarSet::valuesAdded(int index, int count)
    self.uglySide.call('ritual_ZN7QBarSet11valuesAddedEii', index, count)

  @overload(int, int)
  def valuesRemoved(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QBarSet::valuesRemoved(int index, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#valuesRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QBarSet::valuesRemoved(int index, int count)
    self.uglySide.call('ritual_ZN7QBarSet13valuesRemovedEii', index, count)

  @overload(int)
  def valueChanged(self, index: int) -> None:
    """
    Calls Qt's 'void QBarSet::valueChanged(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarset.html#valueChanged

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QBarSet::valueChanged(int index)
    self.uglySide.call('ritual_ZN7QBarSet12valueChangedEi', index)

  @staticmethod
  def deselectBars(*__, **_) -> Never:
    """
    Qt's 'void QBarSet::deselectBars(const QList<int> &indexes)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBarSet.deselectBars' has no cute function yet. Qt's 'void "
        "QBarSet::deselectBars(const QList<int> &indexes)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def selectBars(*__, **_) -> Never:
    """
    Qt's 'void QBarSet::selectBars(const QList<int> &indexes)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBarSet.selectBars' has no cute function yet. Qt's 'void "
        "QBarSet::selectBars(const QList<int> &indexes)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def selectedBars(*__, **_) -> Never:
    """
    Qt's 'QList<int> QBarSet::selectedBars() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QBarSet.selectedBars' has no cute function yet. Qt's 'QList<int> "
        "QBarSet::selectedBars() const': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def selectedBarsChanged(*__, **_) -> Never:
    """
    Qt's 'void QBarSet::selectedBarsChanged(const QList<int> &indexes)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBarSet.selectedBarsChanged' has no cute function yet. Qt's 'void "
        "QBarSet::selectedBarsChanged(const QList<int> &indexes)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def toggleSelection(*__, **_) -> Never:
    """
    Qt's 'void QBarSet::toggleSelection(const QList<int> &indexes)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QBarSet.toggleSelection' has no cute function yet. Qt's 'void "
        "QBarSet::toggleSelection(const QList<int> &indexes)': takes a type "
        "Python has no way to hand over yet.")


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
