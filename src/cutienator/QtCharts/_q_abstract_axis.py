"""
QAbstractAxis binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qabstractaxis.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtGui import QBrush, QColor, QFont, QPen
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QColor = WAIT['QColor']
  QFont = WAIT['QFont']
  QPen = WAIT['QPen']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractAxis(QObject):
  """
  The cute side of Qt's QAbstractAxis: a plain Python object standing in
  front of one C++ QAbstractAxis.

  It is built on the cute 'QObject', as Qt's QAbstractAxis is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractAxis that has a ritual and that Python can
  call so far, 93 names in all: 'metaObject', 'tr', 'type', 'isVisible',
  'setVisible', 'show', 'hide', 'isLineVisible', 'setLineVisible',
  'setLinePen', 'linePen', 'setLinePenColor', 'linePenColor',
  'isGridLineVisible', 'setGridLineVisible', 'setGridLinePen', 'gridLinePen',
  'isMinorGridLineVisible', 'setMinorGridLineVisible', 'setMinorGridLinePen',
  'minorGridLinePen', 'setGridLineColor', 'gridLineColor',
  'setMinorGridLineColor', 'minorGridLineColor', 'labelsVisible',
  'setLabelsVisible', 'setLabelsBrush', 'labelsBrush', 'setLabelsFont',
  'labelsFont', 'setLabelsAngle', 'labelsAngle', 'setLabelsColor',
  'labelsColor', 'isTitleVisible', 'setTitleVisible', 'setTitleBrush',
  'titleBrush', 'setTitleFont', 'titleFont', 'setTitleText', 'titleText',
  'shadesVisible', 'setShadesVisible', 'setShadesPen', 'shadesPen',
  'setShadesBrush', 'shadesBrush', 'setShadesColor', 'shadesColor',
  'setShadesBorderColor', 'shadesBorderColor', 'orientation', 'alignment',
  'setMin', 'setMax', 'setRange', 'setReverse', 'isReverse',
  'setLabelsEditable', 'labelsEditable', 'labelsTruncated',
  'setTruncateLabels', 'truncateLabels', 'visibleChanged', 'linePenChanged',
  'lineVisibleChanged', 'labelsVisibleChanged', 'labelsBrushChanged',
  'labelsFontChanged', 'labelsAngleChanged', 'gridLinePenChanged',
  'gridVisibleChanged', 'minorGridVisibleChanged', 'minorGridLinePenChanged',
  'gridLineColorChanged', 'minorGridLineColorChanged', 'colorChanged',
  'labelsColorChanged', 'titleTextChanged', 'titleBrushChanged',
  'titleVisibleChanged', 'titleFontChanged', 'shadesVisibleChanged',
  'shadesColorChanged', 'shadesBorderColorChanged', 'shadesPenChanged',
  'shadesBrushChanged', 'reverseChanged', 'labelsEditableChanged',
  'labelsTruncatedChanged', 'truncateLabelsChanged'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractAxis::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QAbstractAxis::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractAxis::QAbstractAxis(QAbstractAxisPrivate &d, QObject
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QAbstractAxis::~QAbstractAxis()': the destructor: Python never
    removes a C++ QAbstractAxis.

  What has no ritual
  ------------------

  4 of the 101 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QAbstractAxis is created at the first use, not by
    'QAbstractAxis(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractAxis.
  - Qt tells when it has removed the C++ QAbstractAxis. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractAxis that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QAbstractAxis, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AxisType(CuteFlags):
    """
    The flags enum 'QAbstractAxis::AxisType' of Qt, with the 7 names Qt gives
    in it. Qt names the type of its combinations 'QAbstractAxis::AxisTypes'.
    """

    AxisTypeNoAxis = 0x0
    AxisTypeValue = 0x1
    AxisTypeBarCategory = 0x2
    AxisTypeCategory = 0x4
    AxisTypeDateTime = 0x8
    AxisTypeLogValue = 0x10
    AxisTypeColor = 0x20

  AxisTypes = AxisType

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
    Calls Qt's 'QString QAbstractAxis::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#tr

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
    #  QString QAbstractAxis::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QAbstractAxis2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractAxis'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtCharts'

  #  A C++ QAbstractAxis Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractAxis'

  #  The functions Qt calls itself that QAbstractAxis is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'type': (
          ('_ZNK13QAbstractAxis4typeEv',
           ('int', 'enum', 'QtCharts:QAbstractAxis.AxisType'),
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
    Calls Qt's 'const QMetaObject *QAbstractAxis::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractAxis::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QAbstractAxis10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> AxisType:
    """
    Calls Qt's 'AxisType QAbstractAxis::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#type

    Returns
    -------

    AxisType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AxisType(number)' gives.
    """
    #  AxisType QAbstractAxis::type() const
    return QAbstractAxis.AxisType(self.uglySide.call(
        'ritual_ZNK13QAbstractAxis4typeEv',
    ))

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QAbstractAxis::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#isVisible
    """
    #  bool QAbstractAxis::isVisible() const
    return self.uglySide.call('ritual_ZNK13QAbstractAxis9isVisibleEv')

  def isLineVisible(self) -> bool:
    """
    Calls Qt's 'bool QAbstractAxis::isLineVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#isLineVisible
    """
    #  bool QAbstractAxis::isLineVisible() const
    return self.uglySide.call('ritual_ZNK13QAbstractAxis13isLineVisibleEv')

  def linePen(self) -> QPen:
    """
    Calls Qt's 'QPen QAbstractAxis::linePen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#linePen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QAbstractAxis::linePen() const
    address = self.uglySide.call('ritual_ZNK13QAbstractAxis7linePenEv')
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def linePenColor(self) -> QColor:
    """
    Calls Qt's 'QColor QAbstractAxis::linePenColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#linePenColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAbstractAxis::linePenColor() const
    address = self.uglySide.call('ritual_ZNK13QAbstractAxis12linePenColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def isGridLineVisible(self) -> bool:
    """
    Calls Qt's 'bool QAbstractAxis::isGridLineVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#isGridLineVisible
    """
    #  bool QAbstractAxis::isGridLineVisible() const
    return self.uglySide.call(
        'ritual_ZNK13QAbstractAxis17isGridLineVisibleEv',
    )

  def gridLinePen(self) -> QPen:
    """
    Calls Qt's 'QPen QAbstractAxis::gridLinePen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#gridLinePen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QAbstractAxis::gridLinePen() const
    address = self.uglySide.call('ritual_ZNK13QAbstractAxis11gridLinePenEv')
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def isMinorGridLineVisible(self) -> bool:
    """
    Calls Qt's 'bool QAbstractAxis::isMinorGridLineVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#isMinorGridLineVisible
    """
    #  bool QAbstractAxis::isMinorGridLineVisible() const
    return self.uglySide.call(
        'ritual_ZNK13QAbstractAxis22isMinorGridLineVisibleEv',
    )

  def minorGridLinePen(self) -> QPen:
    """
    Calls Qt's 'QPen QAbstractAxis::minorGridLinePen() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#minorGridLinePen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QAbstractAxis::minorGridLinePen() const
    address = self.uglySide.call(
        'ritual_ZNK13QAbstractAxis16minorGridLinePenEv',
    )
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def labelsVisible(self) -> bool:
    """
    Calls Qt's 'bool QAbstractAxis::labelsVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#labelsVisible
    """
    #  bool QAbstractAxis::labelsVisible() const
    return self.uglySide.call('ritual_ZNK13QAbstractAxis13labelsVisibleEv')

  def labelsBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QAbstractAxis::labelsBrush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#labelsBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QAbstractAxis::labelsBrush() const
    address = self.uglySide.call('ritual_ZNK13QAbstractAxis11labelsBrushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def labelsFont(self) -> QFont:
    """
    Calls Qt's 'QFont QAbstractAxis::labelsFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#labelsFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QAbstractAxis::labelsFont() const
    address = self.uglySide.call('ritual_ZNK13QAbstractAxis10labelsFontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def labelsAngle(self) -> int:
    """
    Calls Qt's 'int QAbstractAxis::labelsAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#labelsAngle
    """
    #  int QAbstractAxis::labelsAngle() const
    return self.uglySide.call('ritual_ZNK13QAbstractAxis11labelsAngleEv')

  def labelsColor(self) -> QColor:
    """
    Calls Qt's 'QColor QAbstractAxis::labelsColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#labelsColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAbstractAxis::labelsColor() const
    address = self.uglySide.call('ritual_ZNK13QAbstractAxis11labelsColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def isTitleVisible(self) -> bool:
    """
    Calls Qt's 'bool QAbstractAxis::isTitleVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#isTitleVisible
    """
    #  bool QAbstractAxis::isTitleVisible() const
    return self.uglySide.call('ritual_ZNK13QAbstractAxis14isTitleVisibleEv')

  def titleBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QAbstractAxis::titleBrush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#titleBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QAbstractAxis::titleBrush() const
    address = self.uglySide.call('ritual_ZNK13QAbstractAxis10titleBrushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def titleFont(self) -> QFont:
    """
    Calls Qt's 'QFont QAbstractAxis::titleFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#titleFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QAbstractAxis::titleFont() const
    address = self.uglySide.call('ritual_ZNK13QAbstractAxis9titleFontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def titleText(self) -> str:
    """
    Calls Qt's 'QString QAbstractAxis::titleText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#titleText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractAxis::titleText() const
    return self.uglySide.call('ritual_ZNK13QAbstractAxis9titleTextEv')

  def shadesVisible(self) -> bool:
    """
    Calls Qt's 'bool QAbstractAxis::shadesVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#shadesVisible
    """
    #  bool QAbstractAxis::shadesVisible() const
    return self.uglySide.call('ritual_ZNK13QAbstractAxis13shadesVisibleEv')

  def shadesPen(self) -> QPen:
    """
    Calls Qt's 'QPen QAbstractAxis::shadesPen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#shadesPen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QAbstractAxis::shadesPen() const
    address = self.uglySide.call('ritual_ZNK13QAbstractAxis9shadesPenEv')
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def shadesBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QAbstractAxis::shadesBrush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#shadesBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QAbstractAxis::shadesBrush() const
    address = self.uglySide.call('ritual_ZNK13QAbstractAxis11shadesBrushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def shadesColor(self) -> QColor:
    """
    Calls Qt's 'QColor QAbstractAxis::shadesColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#shadesColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAbstractAxis::shadesColor() const
    address = self.uglySide.call('ritual_ZNK13QAbstractAxis11shadesColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def shadesBorderColor(self) -> QColor:
    """
    Calls Qt's 'QColor QAbstractAxis::shadesBorderColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#shadesBorderColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAbstractAxis::shadesBorderColor() const
    address = self.uglySide.call(
        'ritual_ZNK13QAbstractAxis17shadesBorderColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QAbstractAxis::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QAbstractAxis::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK13QAbstractAxis11orientationEv',
    ))

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QAbstractAxis::alignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QAbstractAxis::alignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK13QAbstractAxis9alignmentEv',
    ))

  def isReverse(self) -> bool:
    """
    Calls Qt's 'bool QAbstractAxis::isReverse() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#isReverse
    """
    #  bool QAbstractAxis::isReverse() const
    return self.uglySide.call('ritual_ZNK13QAbstractAxis9isReverseEv')

  def labelsEditable(self) -> bool:
    """
    Calls Qt's 'bool QAbstractAxis::labelsEditable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#labelsEditable
    """
    #  bool QAbstractAxis::labelsEditable() const
    return self.uglySide.call('ritual_ZNK13QAbstractAxis14labelsEditableEv')

  def labelsTruncated(self) -> bool:
    """
    Calls Qt's 'bool QAbstractAxis::labelsTruncated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#labelsTruncated
    """
    #  bool QAbstractAxis::labelsTruncated() const
    return self.uglySide.call('ritual_ZNK13QAbstractAxis15labelsTruncatedEv')

  def truncateLabels(self) -> bool:
    """
    Calls Qt's 'bool QAbstractAxis::truncateLabels() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#truncateLabels
    """
    #  bool QAbstractAxis::truncateLabels() const
    return self.uglySide.call('ritual_ZNK13QAbstractAxis14truncateLabelsEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(bool)
  def setVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QAbstractAxis::setVisible(bool visible)
    self.uglySide.call('ritual_ZN13QAbstractAxis10setVisibleEb', visible)

  @overload()
  @overload(bool)
  def setLineVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setLineVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setLineVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QAbstractAxis::setLineVisible(bool visible)
    self.uglySide.call('ritual_ZN13QAbstractAxis14setLineVisibleEb', visible)

  @overload(QPen)
  def setLinePen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setLinePen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setLinePen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QAbstractAxis::setLinePen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis10setLinePenERK4QPen', self._valueOf(pen),
    )

  @overload(QColor)
  def setLinePenColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setLinePenColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setLinePenColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstractAxis::setLinePenColor(QColor color)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis15setLinePenColorE6QColor',
        self._valueOf(color),
    )

  @overload()
  @overload(bool)
  def setGridLineVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setGridLineVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#setGridLineVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QAbstractAxis::setGridLineVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis18setGridLineVisibleEb', visible,
    )

  @overload(QPen)
  def setGridLinePen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setGridLinePen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setGridLinePen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QAbstractAxis::setGridLinePen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis14setGridLinePenERK4QPen',
        self._valueOf(pen),
    )

  @overload()
  @overload(bool)
  def setMinorGridLineVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setMinorGridLineVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#setMinorGridLineVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QAbstractAxis::setMinorGridLineVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis23setMinorGridLineVisibleEb', visible,
    )

  @overload(QPen)
  def setMinorGridLinePen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setMinorGridLinePen(const QPen &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#setMinorGridLinePen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QAbstractAxis::setMinorGridLinePen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis19setMinorGridLinePenERK4QPen',
        self._valueOf(pen),
    )

  @overload(QColor)
  def setGridLineColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setGridLineColor(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#setGridLineColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstractAxis::setGridLineColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis16setGridLineColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setMinorGridLineColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setMinorGridLineColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#setMinorGridLineColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstractAxis::setMinorGridLineColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis21setMinorGridLineColorERK6QColor',
        self._valueOf(color),
    )

  @overload()
  @overload(bool)
  def setLabelsVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setLabelsVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#setLabelsVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QAbstractAxis::setLabelsVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis16setLabelsVisibleEb', visible,
    )

  @overload(QBrush)
  def setLabelsBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setLabelsBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setLabelsBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QAbstractAxis::setLabelsBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis14setLabelsBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QFont)
  def setLabelsFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setLabelsFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setLabelsFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QAbstractAxis::setLabelsFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis13setLabelsFontERK5QFont',
        self._valueOf(font),
    )

  @overload(int)
  def setLabelsAngle(self, angle: int) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setLabelsAngle(int angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setLabelsAngle

    Parameters
    ----------

    angle : int
      Passed on as it is.
    """
    #  void QAbstractAxis::setLabelsAngle(int angle)
    self.uglySide.call('ritual_ZN13QAbstractAxis14setLabelsAngleEi', angle)

  @overload(QColor)
  def setLabelsColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setLabelsColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setLabelsColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstractAxis::setLabelsColor(QColor color)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis14setLabelsColorE6QColor',
        self._valueOf(color),
    )

  @overload()
  @overload(bool)
  def setTitleVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setTitleVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setTitleVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QAbstractAxis::setTitleVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis15setTitleVisibleEb', visible,
    )

  @overload(QBrush)
  def setTitleBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setTitleBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setTitleBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QAbstractAxis::setTitleBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis13setTitleBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QFont)
  def setTitleFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setTitleFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setTitleFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QAbstractAxis::setTitleFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis12setTitleFontERK5QFont',
        self._valueOf(font),
    )

  @overload(str)
  def setTitleText(self, title: str) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setTitleText(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setTitleText

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractAxis::setTitleText(const QString &title)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis12setTitleTextERK7QString', title,
    )

  @overload()
  @overload(bool)
  def setShadesVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setShadesVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#setShadesVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QAbstractAxis::setShadesVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis16setShadesVisibleEb', visible,
    )

  @overload(QPen)
  def setShadesPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setShadesPen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setShadesPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QAbstractAxis::setShadesPen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis12setShadesPenERK4QPen', self._valueOf(pen),
    )

  @overload(QBrush)
  def setShadesBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setShadesBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setShadesBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QAbstractAxis::setShadesBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis14setShadesBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QColor)
  def setShadesColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setShadesColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setShadesColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstractAxis::setShadesColor(QColor color)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis14setShadesColorE6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setShadesBorderColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setShadesBorderColor(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#setShadesBorderColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstractAxis::setShadesBorderColor(QColor color)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis20setShadesBorderColorE6QColor',
        self._valueOf(color),
    )

  @overload(QVariant)
  def setMin(self, min: QVariant) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setMin(const QVariant &min)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setMin

    Parameters
    ----------

    min : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAbstractAxis::setMin(const QVariant &min)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis6setMinERK8QVariant', self._valueOf(min),
    )

  @overload(QVariant)
  def setMax(self, max: QVariant) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setMax(const QVariant &max)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setMax

    Parameters
    ----------

    max : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAbstractAxis::setMax(const QVariant &max)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis6setMaxERK8QVariant', self._valueOf(max),
    )

  @overload(QVariant, QVariant)
  def setRange(self, min: QVariant, max: QVariant) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setRange(const QVariant &min, const
    QVariant &max)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setRange

    Parameters
    ----------

    min : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    max : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAbstractAxis::setRange(const QVariant &min, const QVariant &max)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis8setRangeERK8QVariantS2_',
        self._valueOf(min), self._valueOf(max),
    )

  @overload()
  @overload(bool)
  def setReverse(self, reverse: bool = True) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setReverse(bool reverse)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setReverse

    Parameters
    ----------

    reverse : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QAbstractAxis::setReverse(bool reverse)
    self.uglySide.call('ritual_ZN13QAbstractAxis10setReverseEb', reverse)

  @overload()
  @overload(bool)
  def setLabelsEditable(self, editable: bool = True) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setLabelsEditable(bool editable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#setLabelsEditable

    Parameters
    ----------

    editable : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QAbstractAxis::setLabelsEditable(bool editable)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis17setLabelsEditableEb', editable,
    )

  @overload()
  @overload(bool)
  def setTruncateLabels(self, truncateLabels: bool = True) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setTruncateLabels(bool truncateLabels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#setTruncateLabels

    Parameters
    ----------

    truncateLabels : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QAbstractAxis::setTruncateLabels(bool truncateLabels)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis17setTruncateLabelsEb', truncateLabels,
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
    Qt's 'QAbstractAxis::QAbstractAxis(QAbstractAxisPrivate &d, QObject
    *parent)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractAxis.__init__' has no cute function yet. Qt's "
        "'QAbstractAxis::QAbstractAxis(QAbstractAxisPrivate &d, QObject "
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

  def show(self) -> None:
    """
    Calls Qt's 'void QAbstractAxis::show()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#show
    """
    #  void QAbstractAxis::show()
    self.uglySide.call('ritual_ZN13QAbstractAxis4showEv')

  def hide(self) -> None:
    """
    Calls Qt's 'void QAbstractAxis::hide()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#hide
    """
    #  void QAbstractAxis::hide()
    self.uglySide.call('ritual_ZN13QAbstractAxis4hideEv')

  def gridLineColor(self) -> QColor:
    """
    Calls Qt's 'QColor QAbstractAxis::gridLineColor()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#gridLineColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAbstractAxis::gridLineColor()
    address = self.uglySide.call('ritual_ZN13QAbstractAxis13gridLineColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def minorGridLineColor(self) -> QColor:
    """
    Calls Qt's 'QColor QAbstractAxis::minorGridLineColor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#minorGridLineColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAbstractAxis::minorGridLineColor()
    address = self.uglySide.call(
        'ritual_ZN13QAbstractAxis18minorGridLineColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(bool)
  def visibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAbstractAxis::visibleChanged(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#visibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAbstractAxis::visibleChanged(bool visible)
    self.uglySide.call('ritual_ZN13QAbstractAxis14visibleChangedEb', visible)

  @overload(QPen)
  def linePenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QAbstractAxis::linePenChanged(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#linePenChanged

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QAbstractAxis::linePenChanged(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis14linePenChangedERK4QPen',
        self._valueOf(pen),
    )

  @overload(bool)
  def lineVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAbstractAxis::lineVisibleChanged(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#lineVisibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAbstractAxis::lineVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis18lineVisibleChangedEb', visible,
    )

  @overload(bool)
  def labelsVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAbstractAxis::labelsVisibleChanged(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#labelsVisibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAbstractAxis::labelsVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis20labelsVisibleChangedEb', visible,
    )

  @overload(QBrush)
  def labelsBrushChanged(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QAbstractAxis::labelsBrushChanged(const QBrush &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#labelsBrushChanged

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QAbstractAxis::labelsBrushChanged(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis18labelsBrushChangedERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QFont)
  def labelsFontChanged(self, pen: QFont) -> None:
    """
    Calls Qt's 'void QAbstractAxis::labelsFontChanged(const QFont &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#labelsFontChanged

    Parameters
    ----------

    pen : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QAbstractAxis::labelsFontChanged(const QFont &pen)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis17labelsFontChangedERK5QFont',
        self._valueOf(pen),
    )

  @overload(int)
  def labelsAngleChanged(self, angle: int) -> None:
    """
    Calls Qt's 'void QAbstractAxis::labelsAngleChanged(int angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#labelsAngleChanged

    Parameters
    ----------

    angle : int
      Passed on as it is.
    """
    #  void QAbstractAxis::labelsAngleChanged(int angle)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis18labelsAngleChangedEi', angle,
    )

  @overload(QPen)
  def gridLinePenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QAbstractAxis::gridLinePenChanged(const QPen &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#gridLinePenChanged

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QAbstractAxis::gridLinePenChanged(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis18gridLinePenChangedERK4QPen',
        self._valueOf(pen),
    )

  @overload(bool)
  def gridVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAbstractAxis::gridVisibleChanged(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#gridVisibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAbstractAxis::gridVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis18gridVisibleChangedEb', visible,
    )

  @overload(bool)
  def minorGridVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAbstractAxis::minorGridVisibleChanged(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#minorGridVisibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAbstractAxis::minorGridVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis23minorGridVisibleChangedEb', visible,
    )

  @overload(QPen)
  def minorGridLinePenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QAbstractAxis::minorGridLinePenChanged(const QPen
    &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#minorGridLinePenChanged

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QAbstractAxis::minorGridLinePenChanged(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis23minorGridLinePenChangedERK4QPen',
        self._valueOf(pen),
    )

  @overload(QColor)
  def gridLineColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstractAxis::gridLineColorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#gridLineColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstractAxis::gridLineColorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis20gridLineColorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def minorGridLineColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstractAxis::minorGridLineColorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#minorGridLineColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstractAxis::minorGridLineColorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis25minorGridLineColorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def colorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstractAxis::colorChanged(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#colorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstractAxis::colorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis12colorChangedE6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def labelsColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstractAxis::labelsColorChanged(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#labelsColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstractAxis::labelsColorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis18labelsColorChangedE6QColor',
        self._valueOf(color),
    )

  @overload(str)
  def titleTextChanged(self, title: str) -> None:
    """
    Calls Qt's 'void QAbstractAxis::titleTextChanged(const QString &title)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#titleTextChanged

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractAxis::titleTextChanged(const QString &title)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis16titleTextChangedERK7QString', title,
    )

  @overload(QBrush)
  def titleBrushChanged(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QAbstractAxis::titleBrushChanged(const QBrush &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#titleBrushChanged

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QAbstractAxis::titleBrushChanged(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis17titleBrushChangedERK6QBrush',
        self._valueOf(brush),
    )

  @overload(bool)
  def titleVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAbstractAxis::titleVisibleChanged(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#titleVisibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAbstractAxis::titleVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis19titleVisibleChangedEb', visible,
    )

  @overload(QFont)
  def titleFontChanged(self, font: QFont) -> None:
    """
    Calls Qt's 'void QAbstractAxis::titleFontChanged(const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#titleFontChanged

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QAbstractAxis::titleFontChanged(const QFont &font)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis16titleFontChangedERK5QFont',
        self._valueOf(font),
    )

  @overload(bool)
  def shadesVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAbstractAxis::shadesVisibleChanged(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#shadesVisibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAbstractAxis::shadesVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis20shadesVisibleChangedEb', visible,
    )

  @overload(QColor)
  def shadesColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstractAxis::shadesColorChanged(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#shadesColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstractAxis::shadesColorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis18shadesColorChangedE6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def shadesBorderColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstractAxis::shadesBorderColorChanged(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#shadesBorderColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstractAxis::shadesBorderColorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis24shadesBorderColorChangedE6QColor',
        self._valueOf(color),
    )

  @overload(QPen)
  def shadesPenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QAbstractAxis::shadesPenChanged(const QPen &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#shadesPenChanged

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QAbstractAxis::shadesPenChanged(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis16shadesPenChangedERK4QPen',
        self._valueOf(pen),
    )

  @overload(QBrush)
  def shadesBrushChanged(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QAbstractAxis::shadesBrushChanged(const QBrush &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#shadesBrushChanged

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QAbstractAxis::shadesBrushChanged(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis18shadesBrushChangedERK6QBrush',
        self._valueOf(brush),
    )

  @overload(bool)
  def reverseChanged(self, reverse: bool) -> None:
    """
    Calls Qt's 'void QAbstractAxis::reverseChanged(bool reverse)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#reverseChanged

    Parameters
    ----------

    reverse : bool
      Passed on as it is.
    """
    #  void QAbstractAxis::reverseChanged(bool reverse)
    self.uglySide.call('ritual_ZN13QAbstractAxis14reverseChangedEb', reverse)

  @overload(bool)
  def labelsEditableChanged(self, editable: bool) -> None:
    """
    Calls Qt's 'void QAbstractAxis::labelsEditableChanged(bool editable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#labelsEditableChanged

    Parameters
    ----------

    editable : bool
      Passed on as it is.
    """
    #  void QAbstractAxis::labelsEditableChanged(bool editable)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis21labelsEditableChangedEb', editable,
    )

  @overload(bool)
  def labelsTruncatedChanged(self, labelsTruncated: bool) -> None:
    """
    Calls Qt's 'void QAbstractAxis::labelsTruncatedChanged(bool
    labelsTruncated)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#labelsTruncatedChanged

    Parameters
    ----------

    labelsTruncated : bool
      Passed on as it is.
    """
    #  void QAbstractAxis::labelsTruncatedChanged(bool labelsTruncated)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis22labelsTruncatedChangedEb',
        labelsTruncated,
    )

  @overload(bool)
  def truncateLabelsChanged(self, truncateLabels: bool) -> None:
    """
    Calls Qt's 'void QAbstractAxis::truncateLabelsChanged(bool
    truncateLabels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#truncateLabelsChanged

    Parameters
    ----------

    truncateLabels : bool
      Passed on as it is.
    """
    #  void QAbstractAxis::truncateLabelsChanged(bool truncateLabels)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis21truncateLabelsChangedEb', truncateLabels,
    )


#  Qt's 'QList<QAbstractAxis *>': the list of QAbstractAxis, which
#  'QList[QAbstractAxis]' gives. It is made here, so that there is one as
#  soon as there can be a QAbstractAxis.
QList.createKind(
    QAbstractAxis, 'address',
    make='ritual_list_make_QAbstractAxis_ptr',
    add='ritual_list_add_QAbstractAxis_ptr',
    size='ritual_list_size_QAbstractAxis_ptr',
    at='ritual_list_at_QAbstractAxis_ptr',
    drop='ritual_list_drop_QAbstractAxis_ptr',
)
