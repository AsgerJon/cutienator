"""
QAbstractAxis binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qabstractaxis.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtGui import QColor, QFont
  from ..QtQml import QQmlComponent
  from . import QAbstractAxisPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QFont = WAIT['QFont']
  QQmlComponent = WAIT['QQmlComponent']
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
  call so far, 56 names in all: 'metaObject', 'tr', 'd_func', 'type',
  'isVisible', 'setVisible', 'show', 'hide', 'isLineVisible',
  'setLineVisible', 'isGridVisible', 'setGridVisible', 'isSubGridVisible',
  'setSubGridVisible', 'labelsVisible', 'setLabelsVisible', 'setLabelsAngle',
  'labelsAngle', 'labelDelegate', 'setLabelDelegate', 'isTitleVisible',
  'setTitleVisible', 'setTitleColor', 'titleColor', 'setTitleFont',
  'titleFont', 'setTitleText', 'titleText', 'alignment', 'setAlignment',
  'textElideMode', 'setTextElideMode', 'setSubColor', 'subColor', 'setColor',
  'color', 'setMin', 'setMax', 'setRange', 'visibleChanged',
  'lineVisibleChanged', 'labelsVisibleChanged', 'labelsAngleChanged',
  'labelDelegateChanged', 'gridVisibleChanged', 'subGridVisibleChanged',
  'titleTextChanged', 'titleColorChanged', 'titleVisibleChanged',
  'titleFontChanged', 'alignmentChanged', 'textElideModeChanged',
  'subColorChanged', 'colorChanged', 'update', 'rangeChanged'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractAxis::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QAbstractAxis::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QAbstractAxis::qt_qmlMarker_foreign()': one of Qt's own inner
    workings.
  - Qt's 'void QAbstractAxis::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'const QAbstractAxisPrivate *QAbstractAxis::d_func() const': takes
    in Python what 'QAbstractAxisPrivate *QAbstractAxis::d_func()' takes.
  - Qt's 'QAbstractAxis::QAbstractAxis(QAbstractAxisPrivate &dd, QObject
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QAbstractAxis::~QAbstractAxis()': the destructor: Python never
    removes a C++ QAbstractAxis.

  What has no ritual
  ------------------

  4 of the 67 functions Qt declares: 2 not a gap; 2 forbidden.

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

  class AxisType(CuteFlags, scoped=True):
    """
    The flags enum 'QAbstractAxis::AxisType' of Qt, with the 4 names Qt gives
    in it. Qt names the type of its combinations 'QAbstractAxis::AxisTypes'.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Value = 0x0
    BarCategory = 0x1
    DateTime = 0x2
    LogValue = 0x3

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
  __qt_part__ = 'QtGraphs'

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
           ('int', 'enum', 'QtGraphs:QAbstractAxis.AxisType'),
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

  def isGridVisible(self) -> bool:
    """
    Calls Qt's 'bool QAbstractAxis::isGridVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#isGridVisible
    """
    #  bool QAbstractAxis::isGridVisible() const
    return self.uglySide.call('ritual_ZNK13QAbstractAxis13isGridVisibleEv')

  def isSubGridVisible(self) -> bool:
    """
    Calls Qt's 'bool QAbstractAxis::isSubGridVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#isSubGridVisible
    """
    #  bool QAbstractAxis::isSubGridVisible() const
    return self.uglySide.call(
        'ritual_ZNK13QAbstractAxis16isSubGridVisibleEv',
    )

  def labelsVisible(self) -> bool:
    """
    Calls Qt's 'bool QAbstractAxis::labelsVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#labelsVisible
    """
    #  bool QAbstractAxis::labelsVisible() const
    return self.uglySide.call('ritual_ZNK13QAbstractAxis13labelsVisibleEv')

  def labelsAngle(self) -> float:
    """
    Calls Qt's 'qreal QAbstractAxis::labelsAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#labelsAngle
    """
    #  qreal QAbstractAxis::labelsAngle() const
    return self.uglySide.call('ritual_ZNK13QAbstractAxis11labelsAngleEv')

  def labelDelegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QAbstractAxis::labelDelegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#labelDelegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QAbstractAxis::labelDelegate() const
    address = self.uglySide.call(
        'ritual_ZNK13QAbstractAxis13labelDelegateEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def isTitleVisible(self) -> bool:
    """
    Calls Qt's 'bool QAbstractAxis::isTitleVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#isTitleVisible
    """
    #  bool QAbstractAxis::isTitleVisible() const
    return self.uglySide.call('ritual_ZNK13QAbstractAxis14isTitleVisibleEv')

  def titleColor(self) -> QColor:
    """
    Calls Qt's 'QColor QAbstractAxis::titleColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#titleColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAbstractAxis::titleColor() const
    address = self.uglySide.call('ritual_ZNK13QAbstractAxis10titleColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

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

  def textElideMode(self) -> Qt.TextElideMode:
    """
    Calls Qt's 'Qt::TextElideMode QAbstractAxis::textElideMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#textElideMode

    Returns
    -------

    Qt.TextElideMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TextElideMode(number)'
      gives.
    """
    #  Qt::TextElideMode QAbstractAxis::textElideMode() const
    return Qt.TextElideMode(self.uglySide.call(
        'ritual_ZNK13QAbstractAxis13textElideModeEv',
    ))

  def subColor(self) -> QColor:
    """
    Calls Qt's 'QColor QAbstractAxis::subColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#subColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAbstractAxis::subColor() const
    address = self.uglySide.call('ritual_ZNK13QAbstractAxis8subColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QAbstractAxis::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QAbstractAxis::color() const
    address = self.uglySide.call('ritual_ZNK13QAbstractAxis5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

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

  @overload()
  @overload(bool)
  def setGridVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setGridVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setGridVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QAbstractAxis::setGridVisible(bool visible)
    self.uglySide.call('ritual_ZN13QAbstractAxis14setGridVisibleEb', visible)

  @overload()
  @overload(bool)
  def setSubGridVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setSubGridVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#setSubGridVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QAbstractAxis::setSubGridVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis17setSubGridVisibleEb', visible,
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

  @overload(float)
  def setLabelsAngle(self, angle: float) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setLabelsAngle(qreal angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setLabelsAngle

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QAbstractAxis::setLabelsAngle(qreal angle)
    self.uglySide.call('ritual_ZN13QAbstractAxis14setLabelsAngleEd', angle)

  @overload(QQmlComponent)
  @overload(NoneType)
  def setLabelDelegate(
      self,
      newLabelDelegate: Optional[QQmlComponent],
  ) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setLabelDelegate(QQmlComponent
    *newLabelDelegate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#setLabelDelegate

    Parameters
    ----------

    newLabelDelegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractAxis::setLabelDelegate(QQmlComponent *newLabelDelegate)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis16setLabelDelegateEP13QQmlComponent',
        self._addressOf(newLabelDelegate),
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

  @overload(QColor)
  def setTitleColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setTitleColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setTitleColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstractAxis::setTitleColor(QColor color)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis13setTitleColorE6QColor',
        self._valueOf(color),
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

  @overload(Qt.Alignment)
  def setAlignment(self, alignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setAlignment(Qt::Alignment alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setAlignment

    Parameters
    ----------

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QAbstractAxis::setAlignment(Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis12setAlignmentE6QFlagsIN2Qt13AlignmentFlag'
        'EE',
        alignment.value,
    )

  @overload(Qt.TextElideMode)
  def setTextElideMode(self, elideMode: Qt.TextElideMode) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setTextElideMode(Qt::TextElideMode
    elideMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#setTextElideMode

    Parameters
    ----------

    elideMode : Qt.TextElideMode
      Passed on as its number.
    """
    #  void QAbstractAxis::setTextElideMode(Qt::TextElideMode elideMode)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis16setTextElideModeEN2Qt13TextElideModeE',
        elideMode.value,
    )

  @overload(QColor)
  def setSubColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setSubColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setSubColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstractAxis::setSubColor(QColor color)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis11setSubColorE6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstractAxis::setColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstractAxis::setColor(QColor color)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis8setColorE6QColor', self._valueOf(color),
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
    Qt's 'QAbstractAxis::QAbstractAxis(QAbstractAxisPrivate &dd, QObject
    *parent)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractAxis.__init__' has no cute function yet. Qt's "
        "'QAbstractAxis::QAbstractAxis(QAbstractAxisPrivate &dd, QObject "
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

  def d_func(self) -> Optional[QAbstractAxisPrivate]:
    """
    Calls Qt's 'QAbstractAxisPrivate *QAbstractAxis::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#d_func

    Returns
    -------

    Optional[QAbstractAxisPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxisPrivate *QAbstractAxis::d_func()
    address = self.uglySide.call('ritual_ZN13QAbstractAxis6d_funcEv')
    from . import QAbstractAxisPrivate
    return QAbstractAxisPrivate._cuteAt(address)

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

  @overload(float)
  def labelsAngleChanged(self, angle: float) -> None:
    """
    Calls Qt's 'void QAbstractAxis::labelsAngleChanged(qreal angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#labelsAngleChanged

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QAbstractAxis::labelsAngleChanged(qreal angle)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis18labelsAngleChangedEd', angle,
    )

  def labelDelegateChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractAxis::labelDelegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#labelDelegateChanged
    """
    #  void QAbstractAxis::labelDelegateChanged()
    self.uglySide.call('ritual_ZN13QAbstractAxis20labelDelegateChangedEv')

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
  def subGridVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAbstractAxis::subGridVisibleChanged(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#subGridVisibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAbstractAxis::subGridVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis21subGridVisibleChangedEb', visible,
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

  @overload(QColor)
  def titleColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QAbstractAxis::titleColorChanged(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#titleColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstractAxis::titleColorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis17titleColorChangedE6QColor',
        self._valueOf(color),
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

  @overload(Qt.Alignment)
  def alignmentChanged(self, alignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QAbstractAxis::alignmentChanged(Qt::Alignment
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#alignmentChanged

    Parameters
    ----------

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QAbstractAxis::alignmentChanged(Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis16alignmentChangedE6QFlagsIN2Qt13Alignment'
        'FlagEE',
        alignment.value,
    )

  @overload(Qt.TextElideMode)
  def textElideModeChanged(self, elideMode: Qt.TextElideMode) -> None:
    """
    Calls Qt's 'void QAbstractAxis::textElideModeChanged(Qt::TextElideMode
    elideMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractaxis.html#textElideModeChanged

    Parameters
    ----------

    elideMode : Qt.TextElideMode
      Passed on as its number.
    """
    #  void QAbstractAxis::textElideModeChanged(Qt::TextElideMode elideMode)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis20textElideModeChangedEN2Qt13TextElideMode'
        'E',
        elideMode.value,
    )

  @overload(QColor)
  def subColorChanged(self, newColor: QColor) -> None:
    """
    Calls Qt's 'void QAbstractAxis::subColorChanged(QColor newColor)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#subColorChanged

    Parameters
    ----------

    newColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstractAxis::subColorChanged(QColor newColor)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis15subColorChangedE6QColor',
        self._valueOf(newColor),
    )

  @overload(QColor)
  def colorChanged(self, newColor: QColor) -> None:
    """
    Calls Qt's 'void QAbstractAxis::colorChanged(QColor newColor)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#colorChanged

    Parameters
    ----------

    newColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QAbstractAxis::colorChanged(QColor newColor)
    self.uglySide.call(
        'ritual_ZN13QAbstractAxis12colorChangedE6QColor',
        self._valueOf(newColor),
    )

  def update(self) -> None:
    """
    Calls Qt's 'void QAbstractAxis::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#update
    """
    #  void QAbstractAxis::update()
    self.uglySide.call('ritual_ZN13QAbstractAxis6updateEv')

  @overload(float, float)
  def rangeChanged(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QAbstractAxis::rangeChanged(qreal min, qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractaxis.html#rangeChanged

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QAbstractAxis::rangeChanged(qreal min, qreal max)
    self.uglySide.call('ritual_ZN13QAbstractAxis12rangeChangedEdd', min, max)
