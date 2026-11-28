"""
QQuickIconLabel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickiconlabel_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickIconLabel to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF
  from ..QtGui import QColor, QFont
  from . import QQuickIconLabelPrivate
  from ..QtQuickTemplates2 import QQuickIcon
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QFont = WAIT['QFont']
  QQuickIcon = WAIT['QQuickIcon']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickIconLabel(QQuickItem):
  """
  The cute side of Qt's QQuickIconLabel: a plain Python object standing in
  front of one C++ QQuickIconLabel.

  It is built on the cute 'QQuickItem', as Qt's QQuickIconLabel is built on
  Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickIconLabel that has a ritual and that Python
  can call so far, 36 names in all: 'metaObject', 'tr', 'icon', 'setIcon',
  'defaultIconColor', 'setDefaultIconColor', 'text', 'setText', 'font',
  'setFont', 'color', 'setColor', 'display', 'setDisplay', 'spacing',
  'setSpacing', 'isMirrored', 'setMirrored', 'alignment', 'setAlignment',
  'topPadding', 'setTopPadding', 'resetTopPadding', 'leftPadding',
  'setLeftPadding', 'resetLeftPadding', 'rightPadding', 'setRightPadding',
  'resetRightPadding', 'bottomPadding', 'setBottomPadding',
  'resetBottomPadding', 'defaultIconColorChanged', 'componentComplete',
  'geometryChange', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickIconLabel::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickIconLabel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickIconLabel::~QQuickIconLabel()': the destructor: Python never
    removes a C++ QQuickIconLabel.
  - Qt's 'QQuickIconLabel::QQuickIconLabel(QQuickIconLabelPrivate &dd,
    QQuickItem *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickIconLabelPrivate *QQuickIconLabel::d_func() const':
    takes in Python what 'QQuickIconLabelPrivate *QQuickIconLabel::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 46 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickIconLabel is created at the first use, not by
    'QQuickIconLabel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickIconLabel.
  - Qt tells when it has removed the C++ QQuickIconLabel. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickIconLabel, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Display(CuteNum):
    """
    The enum 'QQuickIconLabel::Display' of Qt, with the 4 names Qt gives in
    it.
    """

    IconOnly = Kee[int](0)
    TextOnly = Kee[int](1)
    TextBesideIcon = Kee[int](2)
    TextUnderIcon = Kee[int](3)

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
    Calls Qt's 'QString QQuickIconLabel::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#tr

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
    #  QString QQuickIconLabel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickIconLabel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickIconLabel'

  #  A C++ QQuickIconLabel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickIconLabel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickIconLabel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickIconLabel::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickIconLabel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def icon(self) -> QQuickIcon:
    """
    Calls Qt's 'QQuickIcon QQuickIconLabel::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#icon

    Returns
    -------

    QQuickIcon
      A new cute QQuickIcon around the copy Qt gave back. Python owns it.
    """
    #  QQuickIcon QQuickIconLabel::icon() const
    address = self.uglySide.call('ritual_ZNK15QQuickIconLabel4iconEv')
    from ..QtQuickTemplates2 import QQuickIcon
    return QQuickIcon._cuteOwning(address)

  def defaultIconColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickIconLabel::defaultIconColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabel.html#defaultIconColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickIconLabel::defaultIconColor() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickIconLabel16defaultIconColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QQuickIconLabel::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickIconLabel::text() const
    return self.uglySide.call('ritual_ZNK15QQuickIconLabel4textEv')

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickIconLabel::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickIconLabel::font() const
    address = self.uglySide.call('ritual_ZNK15QQuickIconLabel4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickIconLabel::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickIconLabel::color() const
    address = self.uglySide.call('ritual_ZNK15QQuickIconLabel5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def display(self) -> Display:
    """
    Calls Qt's 'Display QQuickIconLabel::display() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#display

    Returns
    -------

    Display
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Display(number)' gives.
    """
    #  Display QQuickIconLabel::display() const
    return QQuickIconLabel.Display(self.uglySide.call(
        'ritual_ZNK15QQuickIconLabel7displayEv',
    ))

  def spacing(self) -> float:
    """
    Calls Qt's 'qreal QQuickIconLabel::spacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#spacing
    """
    #  qreal QQuickIconLabel::spacing() const
    return self.uglySide.call('ritual_ZNK15QQuickIconLabel7spacingEv')

  def isMirrored(self) -> bool:
    """
    Calls Qt's 'bool QQuickIconLabel::isMirrored() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#isMirrored
    """
    #  bool QQuickIconLabel::isMirrored() const
    return self.uglySide.call('ritual_ZNK15QQuickIconLabel10isMirroredEv')

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QQuickIconLabel::alignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QQuickIconLabel::alignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK15QQuickIconLabel9alignmentEv',
    ))

  def topPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickIconLabel::topPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#topPadding
    """
    #  qreal QQuickIconLabel::topPadding() const
    return self.uglySide.call('ritual_ZNK15QQuickIconLabel10topPaddingEv')

  def leftPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickIconLabel::leftPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#leftPadding
    """
    #  qreal QQuickIconLabel::leftPadding() const
    return self.uglySide.call('ritual_ZNK15QQuickIconLabel11leftPaddingEv')

  def rightPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickIconLabel::rightPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#rightPadding
    """
    #  qreal QQuickIconLabel::rightPadding() const
    return self.uglySide.call('ritual_ZNK15QQuickIconLabel12rightPaddingEv')

  def bottomPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickIconLabel::bottomPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#bottomPadding
    """
    #  qreal QQuickIconLabel::bottomPadding() const
    return self.uglySide.call('ritual_ZNK15QQuickIconLabel13bottomPaddingEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickIcon)
  def setIcon(self, icon: QQuickIcon) -> None:
    """
    Calls Qt's 'void QQuickIconLabel::setIcon(const QQuickIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#setIcon

    Parameters
    ----------

    icon : QQuickIcon
      Passed on as a value: Qt reads the C++ QQuickIcon, which stays Python's
      own.
    """
    #  void QQuickIconLabel::setIcon(const QQuickIcon &icon)
    self.uglySide.call(
        'ritual_ZN15QQuickIconLabel7setIconERK10QQuickIcon',
        self._valueOf(icon),
    )

  @overload(QColor)
  def setDefaultIconColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickIconLabel::setDefaultIconColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabel.html#setDefaultIconColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickIconLabel::setDefaultIconColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN15QQuickIconLabel19setDefaultIconColorERK6QColor',
        self._valueOf(color),
    )

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickIconLabel::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickIconLabel::setText(const QString &text)
    self.uglySide.call('ritual_ZN15QQuickIconLabel7setTextERK7QString', text)

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickIconLabel::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickIconLabel::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN15QQuickIconLabel7setFontERK5QFont', self._valueOf(font),
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickIconLabel::setColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickIconLabel::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN15QQuickIconLabel8setColorERK6QColor',
        self._valueOf(color),
    )

  @overload(Display)
  def setDisplay(self, display: Display) -> None:
    """
    Calls Qt's 'void QQuickIconLabel::setDisplay(Display display)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#setDisplay

    Parameters
    ----------

    display : Display
      Passed on as its number.
    """
    #  void QQuickIconLabel::setDisplay(Display display)
    self.uglySide.call(
        'ritual_ZN15QQuickIconLabel10setDisplayENS_7DisplayE', display.value,
    )

  @overload(float)
  def setSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QQuickIconLabel::setSpacing(qreal spacing)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#setSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QQuickIconLabel::setSpacing(qreal spacing)
    self.uglySide.call('ritual_ZN15QQuickIconLabel10setSpacingEd', spacing)

  @overload(bool)
  def setMirrored(self, mirrored: bool) -> None:
    """
    Calls Qt's 'void QQuickIconLabel::setMirrored(bool mirrored)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#setMirrored

    Parameters
    ----------

    mirrored : bool
      Passed on as it is.
    """
    #  void QQuickIconLabel::setMirrored(bool mirrored)
    self.uglySide.call('ritual_ZN15QQuickIconLabel11setMirroredEb', mirrored)

  @overload(Qt.Alignment)
  def setAlignment(self, alignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QQuickIconLabel::setAlignment(Qt::Alignment alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#setAlignment

    Parameters
    ----------

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QQuickIconLabel::setAlignment(Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN15QQuickIconLabel12setAlignmentE6QFlagsIN2Qt13AlignmentFl'
        'agEE',
        alignment.value,
    )

  @overload(float)
  def setTopPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickIconLabel::setTopPadding(qreal padding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#setTopPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickIconLabel::setTopPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN15QQuickIconLabel13setTopPaddingEd', padding,
    )

  @overload(float)
  def setLeftPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickIconLabel::setLeftPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabel.html#setLeftPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickIconLabel::setLeftPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN15QQuickIconLabel14setLeftPaddingEd', padding,
    )

  @overload(float)
  def setRightPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickIconLabel::setRightPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabel.html#setRightPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickIconLabel::setRightPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN15QQuickIconLabel15setRightPaddingEd', padding,
    )

  @overload(float)
  def setBottomPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickIconLabel::setBottomPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabel.html#setBottomPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickIconLabel::setBottomPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN15QQuickIconLabel16setBottomPaddingEd', padding,
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

  @overload()
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickIconLabel::QQuickIconLabel(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabel.html#QQuickIconLabel

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickIconLabel::QQuickIconLabel(QQuickItem *parent)
    self._noteCreation(QQuickIconLabel, lambda: Rituals.call(
        'ritual_ZN15QQuickIconLabelC1EP10QQuickItem',
        self._addressOf(parent),
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

  def resetTopPadding(self) -> None:
    """
    Calls Qt's 'void QQuickIconLabel::resetTopPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabel.html#resetTopPadding
    """
    #  void QQuickIconLabel::resetTopPadding()
    self.uglySide.call('ritual_ZN15QQuickIconLabel15resetTopPaddingEv')

  def resetLeftPadding(self) -> None:
    """
    Calls Qt's 'void QQuickIconLabel::resetLeftPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabel.html#resetLeftPadding
    """
    #  void QQuickIconLabel::resetLeftPadding()
    self.uglySide.call('ritual_ZN15QQuickIconLabel16resetLeftPaddingEv')

  def resetRightPadding(self) -> None:
    """
    Calls Qt's 'void QQuickIconLabel::resetRightPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabel.html#resetRightPadding
    """
    #  void QQuickIconLabel::resetRightPadding()
    self.uglySide.call('ritual_ZN15QQuickIconLabel17resetRightPaddingEv')

  def resetBottomPadding(self) -> None:
    """
    Calls Qt's 'void QQuickIconLabel::resetBottomPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabel.html#resetBottomPadding
    """
    #  void QQuickIconLabel::resetBottomPadding()
    self.uglySide.call('ritual_ZN15QQuickIconLabel18resetBottomPaddingEv')

  def defaultIconColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickIconLabel::defaultIconColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabel.html#defaultIconColorChanged
    """
    #  void QQuickIconLabel::defaultIconColorChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickIconLabel23defaultIconColorChangedEv',
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickIconLabel::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabel.html#componentComplete
    """
    #  void QQuickIconLabel::componentComplete()
    ritual = 'ritual_ZN15QQuickIconLabel17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickIconLabel17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickIconLabel::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickiconlabel.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickIconLabel::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN15QQuickIconLabel14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickIconLabel14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def d_func(self) -> Optional[QQuickIconLabelPrivate]:
    """
    Calls Qt's 'QQuickIconLabelPrivate *QQuickIconLabel::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickiconlabel.html#d_func

    Returns
    -------

    Optional[QQuickIconLabelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickIconLabelPrivate *QQuickIconLabel::d_func()
    address = self.uglySide.call('ritual_ZN15QQuickIconLabel6d_funcEv')
    from . import QQuickIconLabelPrivate
    return QQuickIconLabelPrivate._cuteAt(address)
