"""
QLegendMarker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qlegendmarker.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QLegend

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QBrush, QFont, QPen
  from . import QAbstractSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QFont = WAIT['QFont']
  QPen = WAIT['QPen']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLegendMarker(QObject):
  """
  The cute side of Qt's QLegendMarker: a plain Python object standing in
  front of one C++ QLegendMarker.

  It is built on the cute 'QObject', as Qt's QLegendMarker is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLegendMarker that has a ritual and that Python can
  call so far, 27 names in all: 'metaObject', 'tr', 'type', 'label',
  'setLabel', 'labelBrush', 'setLabelBrush', 'font', 'setFont', 'pen',
  'setPen', 'brush', 'setBrush', 'isVisible', 'setVisible', 'shape',
  'setShape', 'series', 'clicked', 'hovered', 'labelChanged',
  'labelBrushChanged', 'fontChanged', 'penChanged', 'brushChanged',
  'visibleChanged', 'shapeChanged'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QLegendMarker::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QLegendMarker::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QLegendMarker::~QLegendMarker()': the destructor: Python never
    removes a C++ QLegendMarker.
  - Qt's 'QLegendMarker::QLegendMarker(QLegendMarkerPrivate &d, QObject
    *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 35 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QLegendMarker is created at the first use, not by
    'QLegendMarker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLegendMarker.
  - Qt tells when it has removed the C++ QLegendMarker. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QLegendMarker that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QLegendMarker, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class LegendMarkerType(CuteNum):
    """
    The enum 'QLegendMarker::LegendMarkerType' of Qt, with the 6 names Qt
    gives in it.
    """

    LegendMarkerTypeArea = Kee[int](0)
    LegendMarkerTypeBar = Kee[int](1)
    LegendMarkerTypePie = Kee[int](2)
    LegendMarkerTypeXY = Kee[int](3)
    LegendMarkerTypeBoxPlot = Kee[int](4)
    LegendMarkerTypeCandlestick = Kee[int](5)

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
    Calls Qt's 'QString QLegendMarker::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#tr

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
    #  QString QLegendMarker::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QLegendMarker2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLegendMarker'

  #  A C++ QLegendMarker Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLegendMarker'

  #  The functions Qt calls itself that QLegendMarker is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'type': (
          ('_ZN13QLegendMarker4typeEv',
           ('int', 'enum', 'QtCharts:QLegendMarker.LegendMarkerType'),
           ()),
      ),
      'series': (
          ('_ZN13QLegendMarker6seriesEv',
           ('address', 'address', 'QtCharts:QAbstractSeries'),
           ()),
      ),
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
    Calls Qt's 'const QMetaObject *QLegendMarker::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLegendMarker::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QLegendMarker10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def label(self) -> str:
    """
    Calls Qt's 'QString QLegendMarker::label() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#label

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLegendMarker::label() const
    return self.uglySide.call('ritual_ZNK13QLegendMarker5labelEv')

  def labelBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QLegendMarker::labelBrush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#labelBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QLegendMarker::labelBrush() const
    address = self.uglySide.call('ritual_ZNK13QLegendMarker10labelBrushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QLegendMarker::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QLegendMarker::font() const
    address = self.uglySide.call('ritual_ZNK13QLegendMarker4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def pen(self) -> QPen:
    """
    Calls Qt's 'QPen QLegendMarker::pen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#pen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QLegendMarker::pen() const
    address = self.uglySide.call('ritual_ZNK13QLegendMarker3penEv')
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def brush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QLegendMarker::brush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#brush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QLegendMarker::brush() const
    address = self.uglySide.call('ritual_ZNK13QLegendMarker5brushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QLegendMarker::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#isVisible
    """
    #  bool QLegendMarker::isVisible() const
    return self.uglySide.call('ritual_ZNK13QLegendMarker9isVisibleEv')

  def shape(self) -> QLegend.MarkerShape:
    """
    Calls Qt's 'QLegend::MarkerShape QLegendMarker::shape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#shape

    Returns
    -------

    QLegend.MarkerShape
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QLegend.MarkerShape(number)' gives.
    """
    #  QLegend::MarkerShape QLegendMarker::shape() const
    return QLegend.MarkerShape(self.uglySide.call(
        'ritual_ZNK13QLegendMarker5shapeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setLabel(self, label: str) -> None:
    """
    Calls Qt's 'void QLegendMarker::setLabel(const QString &label)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#setLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLegendMarker::setLabel(const QString &label)
    self.uglySide.call('ritual_ZN13QLegendMarker8setLabelERK7QString', label)

  @overload(QBrush)
  def setLabelBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QLegendMarker::setLabelBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#setLabelBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QLegendMarker::setLabelBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN13QLegendMarker13setLabelBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QLegendMarker::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QLegendMarker::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN13QLegendMarker7setFontERK5QFont', self._valueOf(font),
    )

  @overload(QPen)
  def setPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QLegendMarker::setPen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#setPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QLegendMarker::setPen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN13QLegendMarker6setPenERK4QPen', self._valueOf(pen),
    )

  @overload(QBrush)
  def setBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QLegendMarker::setBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#setBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QLegendMarker::setBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN13QLegendMarker8setBrushERK6QBrush', self._valueOf(brush),
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QLegendMarker::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QLegendMarker::setVisible(bool visible)
    self.uglySide.call('ritual_ZN13QLegendMarker10setVisibleEb', visible)

  @overload(QLegend.MarkerShape)
  def setShape(self, shape: QLegend.MarkerShape) -> None:
    """
    Calls Qt's 'void QLegendMarker::setShape(QLegend::MarkerShape shape)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#setShape

    Parameters
    ----------

    shape : QLegend.MarkerShape
      Passed on as its number.
    """
    #  void QLegendMarker::setShape(QLegend::MarkerShape shape)
    self.uglySide.call(
        'ritual_ZN13QLegendMarker8setShapeEN7QLegend11MarkerShapeE',
        shape.value,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QLegendMarker::QLegendMarker(QLegendMarkerPrivate &d, QObject
    *parent)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLegendMarker.__init__' has no cute function yet. Qt's "
        "'QLegendMarker::QLegendMarker(QLegendMarkerPrivate &d, QObject "
        "*parent)': takes a type Python has no way to hand over yet.")

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

  def type(self) -> LegendMarkerType:
    """
    Calls Qt's 'LegendMarkerType QLegendMarker::type()'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#type

    Returns
    -------

    LegendMarkerType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LegendMarkerType(number)'
      gives.
    """
    #  LegendMarkerType QLegendMarker::type()
    return QLegendMarker.LegendMarkerType(self.uglySide.call(
        'ritual_ZN13QLegendMarker4typeEv',
    ))

  def series(self) -> Optional[QAbstractSeries]:
    """
    Calls Qt's 'QAbstractSeries *QLegendMarker::series()'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#series

    Returns
    -------

    Optional[QAbstractSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractSeries *QLegendMarker::series()
    address = self.uglySide.call('ritual_ZN13QLegendMarker6seriesEv')
    from . import QAbstractSeries
    return QAbstractSeries._cuteAt(address)

  def clicked(self) -> None:
    """
    Calls Qt's 'void QLegendMarker::clicked()'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#clicked
    """
    #  void QLegendMarker::clicked()
    self.uglySide.call('ritual_ZN13QLegendMarker7clickedEv')

  @overload(bool)
  def hovered(self, status: bool) -> None:
    """
    Calls Qt's 'void QLegendMarker::hovered(bool status)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#hovered

    Parameters
    ----------

    status : bool
      Passed on as it is.
    """
    #  void QLegendMarker::hovered(bool status)
    self.uglySide.call('ritual_ZN13QLegendMarker7hoveredEb', status)

  def labelChanged(self) -> None:
    """
    Calls Qt's 'void QLegendMarker::labelChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#labelChanged
    """
    #  void QLegendMarker::labelChanged()
    self.uglySide.call('ritual_ZN13QLegendMarker12labelChangedEv')

  def labelBrushChanged(self) -> None:
    """
    Calls Qt's 'void QLegendMarker::labelBrushChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlegendmarker.html#labelBrushChanged
    """
    #  void QLegendMarker::labelBrushChanged()
    self.uglySide.call('ritual_ZN13QLegendMarker17labelBrushChangedEv')

  def fontChanged(self) -> None:
    """
    Calls Qt's 'void QLegendMarker::fontChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#fontChanged
    """
    #  void QLegendMarker::fontChanged()
    self.uglySide.call('ritual_ZN13QLegendMarker11fontChangedEv')

  def penChanged(self) -> None:
    """
    Calls Qt's 'void QLegendMarker::penChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#penChanged
    """
    #  void QLegendMarker::penChanged()
    self.uglySide.call('ritual_ZN13QLegendMarker10penChangedEv')

  def brushChanged(self) -> None:
    """
    Calls Qt's 'void QLegendMarker::brushChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#brushChanged
    """
    #  void QLegendMarker::brushChanged()
    self.uglySide.call('ritual_ZN13QLegendMarker12brushChangedEv')

  def visibleChanged(self) -> None:
    """
    Calls Qt's 'void QLegendMarker::visibleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#visibleChanged
    """
    #  void QLegendMarker::visibleChanged()
    self.uglySide.call('ritual_ZN13QLegendMarker14visibleChangedEv')

  def shapeChanged(self) -> None:
    """
    Calls Qt's 'void QLegendMarker::shapeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarker.html#shapeChanged
    """
    #  void QLegendMarker::shapeChanged()
    self.uglySide.call('ritual_ZN13QLegendMarker12shapeChangedEv')


#  Qt's 'QList<QLegendMarker *>': the list of QLegendMarker, which
#  'QList[QLegendMarker]' gives. It is made here, so that there is one as
#  soon as there can be a QLegendMarker.
QList.createKind(
    QLegendMarker, 'address',
    make='ritual_list_make_QLegendMarker_ptr',
    add='ritual_list_add_QLegendMarker_ptr',
    size='ritual_list_size_QLegendMarker_ptr',
    at='ritual_list_at_QLegendMarker_ptr',
    drop='ritual_list_drop_QLegendMarker_ptr',
)
