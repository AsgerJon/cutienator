"""
QQuickTextField binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktextfield_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickTextField to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtQuick import QQuickItem, QQuickTextInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMarginsF, QMetaObject, QRectF, QTimerEvent
  from ..QtGui import QColor, QFocusEvent, QFont, QHoverEvent, QMouseEvent
  from ..QtQuick import QQuickMouseEvent, QSGNode
  from . import QQuickTextFieldPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QFocusEvent = WAIT['QFocusEvent']
  QFont = WAIT['QFont']
  QHoverEvent = WAIT['QHoverEvent']
  QMarginsF = WAIT['QMarginsF']
  QMouseEvent = WAIT['QMouseEvent']
  QQuickMouseEvent = WAIT['QQuickMouseEvent']
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTextField(QQuickTextInput):
  """
  The cute side of Qt's QQuickTextField: a plain Python object standing in
  front of one C++ QQuickTextField.

  It is built on the cute 'QQuickTextInput', as Qt's QQuickTextField is built
  on Qt's QQuickTextInput, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTextField that has a ritual and that Python
  can call so far, 65 names in all: 'metaObject', 'tr', 'font', 'setFont',
  'background', 'setBackground', 'placeholderText', 'setPlaceholderText',
  'focusReason', 'setFocusReason', 'isHovered', 'setHovered',
  'isHoverEnabled', 'setHoverEnabled', 'resetHoverEnabled',
  'placeholderTextColor', 'setPlaceholderTextColor',
  'implicitBackgroundWidth', 'implicitBackgroundHeight', 'topInset',
  'setTopInset', 'resetTopInset', 'leftInset', 'setLeftInset',
  'resetLeftInset', 'rightInset', 'setRightInset', 'resetRightInset',
  'bottomInset', 'setBottomInset', 'resetBottomInset', 'fontChanged',
  'implicitWidthChanged3', 'implicitHeightChanged3', 'backgroundChanged',
  'placeholderTextChanged', 'focusReasonChanged', 'pressAndHold', 'pressed',
  'released', 'hoveredChanged', 'hoverEnabledChanged',
  'placeholderTextColorChanged', 'implicitBackgroundWidthChanged',
  'implicitBackgroundHeightChanged', 'topInsetChanged', 'leftInsetChanged',
  'rightInsetChanged', 'bottomInsetChanged', 'classBegin',
  'componentComplete', 'itemChange', 'geometryChange', 'insetChange',
  'updatePaintNode', 'focusInEvent', 'focusOutEvent', 'hoverEnterEvent',
  'hoverLeaveEvent', 'mousePressEvent', 'mouseMoveEvent',
  'mouseReleaseEvent', 'mouseDoubleClickEvent', 'timerEvent', 'd_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTextField::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickTextField::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickTextField::~QQuickTextField()': the destructor: Python never
    removes a C++ QQuickTextField.
  - Qt's 'const QQuickTextFieldPrivate *QQuickTextField::d_func() const':
    takes in Python what 'QQuickTextFieldPrivate *QQuickTextField::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 74 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickTextField is created at the first use, not by
    'QQuickTextField(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTextField.
  - Qt tells when it has removed the C++ QQuickTextField. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickTextField::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#tr

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
    #  QString QQuickTextField::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickTextField2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTextField'

  #  A C++ QQuickTextField Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTextField'

  #  The functions Qt calls itself that QQuickTextField is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'insetChange': (
          ('_ZN15QQuickTextField11insetChangeERK9QMarginsFS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QMarginsF'),
               ('address', 'value', 'QtCore:QMarginsF'),
           )),
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
    Calls Qt's 'const QMetaObject *QQuickTextField::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTextField::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickTextField10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickTextField::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickTextField::font() const
    address = self.uglySide.call('ritual_ZNK15QQuickTextField4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def background(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickTextField::background() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#background

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickTextField::background() const
    address = self.uglySide.call('ritual_ZNK15QQuickTextField10backgroundEv')
    return QQuickItem._cuteAt(address)

  def placeholderText(self) -> str:
    """
    Calls Qt's 'QString QQuickTextField::placeholderText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#placeholderText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextField::placeholderText() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTextField15placeholderTextEv',
    )

  def focusReason(self) -> Qt.FocusReason:
    """
    Calls Qt's 'Qt::FocusReason QQuickTextField::focusReason() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#focusReason

    Returns
    -------

    Qt.FocusReason
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.FocusReason(number)'
      gives.
    """
    #  Qt::FocusReason QQuickTextField::focusReason() const
    return Qt.FocusReason(self.uglySide.call(
        'ritual_ZNK15QQuickTextField11focusReasonEv',
    ))

  def isHovered(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextField::isHovered() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#isHovered
    """
    #  bool QQuickTextField::isHovered() const
    return self.uglySide.call('ritual_ZNK15QQuickTextField9isHoveredEv')

  def isHoverEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextField::isHoverEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#isHoverEnabled
    """
    #  bool QQuickTextField::isHoverEnabled() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTextField14isHoverEnabledEv',
    )

  def placeholderTextColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickTextField::placeholderTextColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#placeholderTextColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickTextField::placeholderTextColor() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickTextField20placeholderTextColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def implicitBackgroundWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextField::implicitBackgroundWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#implicitBackgroundWidth
    """
    #  qreal QQuickTextField::implicitBackgroundWidth() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTextField23implicitBackgroundWidthEv',
    )

  def implicitBackgroundHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextField::implicitBackgroundHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#implicitBackgroundHeight
    """
    #  qreal QQuickTextField::implicitBackgroundHeight() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTextField24implicitBackgroundHeightEv',
    )

  def topInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextField::topInset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#topInset
    """
    #  qreal QQuickTextField::topInset() const
    return self.uglySide.call('ritual_ZNK15QQuickTextField8topInsetEv')

  def leftInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextField::leftInset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#leftInset
    """
    #  qreal QQuickTextField::leftInset() const
    return self.uglySide.call('ritual_ZNK15QQuickTextField9leftInsetEv')

  def rightInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextField::rightInset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#rightInset
    """
    #  qreal QQuickTextField::rightInset() const
    return self.uglySide.call('ritual_ZNK15QQuickTextField10rightInsetEv')

  def bottomInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextField::bottomInset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#bottomInset
    """
    #  qreal QQuickTextField::bottomInset() const
    return self.uglySide.call('ritual_ZNK15QQuickTextField11bottomInsetEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickTextField::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickTextField::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN15QQuickTextField7setFontERK5QFont', self._valueOf(font),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setBackground(self, background: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickTextField::setBackground(QQuickItem *background)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#setBackground

    Parameters
    ----------

    background : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextField::setBackground(QQuickItem *background)
    self.uglySide.call(
        'ritual_ZN15QQuickTextField13setBackgroundEP10QQuickItem',
        self._addressOf(background),
    )

  @overload(str)
  def setPlaceholderText(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickTextField::setPlaceholderText(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#setPlaceholderText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextField::setPlaceholderText(const QString &text)
    self.uglySide.call(
        'ritual_ZN15QQuickTextField18setPlaceholderTextERK7QString', text,
    )

  @overload(Qt.FocusReason)
  def setFocusReason(self, reason: Qt.FocusReason) -> None:
    """
    Calls Qt's 'void QQuickTextField::setFocusReason(Qt::FocusReason
    reason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#setFocusReason

    Parameters
    ----------

    reason : Qt.FocusReason
      Passed on as its number.
    """
    #  void QQuickTextField::setFocusReason(Qt::FocusReason reason)
    self.uglySide.call(
        'ritual_ZN15QQuickTextField14setFocusReasonEN2Qt11FocusReasonE',
        reason.value,
    )

  @overload(bool)
  def setHovered(self, hovered: bool) -> None:
    """
    Calls Qt's 'void QQuickTextField::setHovered(bool hovered)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#setHovered

    Parameters
    ----------

    hovered : bool
      Passed on as it is.
    """
    #  void QQuickTextField::setHovered(bool hovered)
    self.uglySide.call('ritual_ZN15QQuickTextField10setHoveredEb', hovered)

  @overload(bool)
  def setHoverEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickTextField::setHoverEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#setHoverEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickTextField::setHoverEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN15QQuickTextField15setHoverEnabledEb', enabled,
    )

  @overload(QColor)
  def setPlaceholderTextColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickTextField::setPlaceholderTextColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#setPlaceholderTextColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickTextField::setPlaceholderTextColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN15QQuickTextField23setPlaceholderTextColorERK6QColor',
        self._valueOf(color),
    )

  @overload(float)
  def setTopInset(self, inset: float) -> None:
    """
    Calls Qt's 'void QQuickTextField::setTopInset(qreal inset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#setTopInset

    Parameters
    ----------

    inset : float
      Passed on as it is.
    """
    #  void QQuickTextField::setTopInset(qreal inset)
    self.uglySide.call('ritual_ZN15QQuickTextField11setTopInsetEd', inset)

  @overload(float)
  def setLeftInset(self, inset: float) -> None:
    """
    Calls Qt's 'void QQuickTextField::setLeftInset(qreal inset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#setLeftInset

    Parameters
    ----------

    inset : float
      Passed on as it is.
    """
    #  void QQuickTextField::setLeftInset(qreal inset)
    self.uglySide.call('ritual_ZN15QQuickTextField12setLeftInsetEd', inset)

  @overload(float)
  def setRightInset(self, inset: float) -> None:
    """
    Calls Qt's 'void QQuickTextField::setRightInset(qreal inset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#setRightInset

    Parameters
    ----------

    inset : float
      Passed on as it is.
    """
    #  void QQuickTextField::setRightInset(qreal inset)
    self.uglySide.call('ritual_ZN15QQuickTextField13setRightInsetEd', inset)

  @overload(float)
  def setBottomInset(self, inset: float) -> None:
    """
    Calls Qt's 'void QQuickTextField::setBottomInset(qreal inset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#setBottomInset

    Parameters
    ----------

    inset : float
      Passed on as it is.
    """
    #  void QQuickTextField::setBottomInset(qreal inset)
    self.uglySide.call('ritual_ZN15QQuickTextField14setBottomInsetEd', inset)

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
    'QQuickTextField::QQuickTextField(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#QQuickTextField

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTextField::QQuickTextField(QQuickItem *parent)
    self._noteCreation(QQuickTextField, lambda: Rituals.call(
        'ritual_ZN15QQuickTextFieldC1EP10QQuickItem',
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

  def resetHoverEnabled(self) -> None:
    """
    Calls Qt's 'void QQuickTextField::resetHoverEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#resetHoverEnabled
    """
    #  void QQuickTextField::resetHoverEnabled()
    self.uglySide.call('ritual_ZN15QQuickTextField17resetHoverEnabledEv')

  def resetTopInset(self) -> None:
    """
    Calls Qt's 'void QQuickTextField::resetTopInset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#resetTopInset
    """
    #  void QQuickTextField::resetTopInset()
    self.uglySide.call('ritual_ZN15QQuickTextField13resetTopInsetEv')

  def resetLeftInset(self) -> None:
    """
    Calls Qt's 'void QQuickTextField::resetLeftInset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#resetLeftInset
    """
    #  void QQuickTextField::resetLeftInset()
    self.uglySide.call('ritual_ZN15QQuickTextField14resetLeftInsetEv')

  def resetRightInset(self) -> None:
    """
    Calls Qt's 'void QQuickTextField::resetRightInset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#resetRightInset
    """
    #  void QQuickTextField::resetRightInset()
    self.uglySide.call('ritual_ZN15QQuickTextField15resetRightInsetEv')

  def resetBottomInset(self) -> None:
    """
    Calls Qt's 'void QQuickTextField::resetBottomInset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#resetBottomInset
    """
    #  void QQuickTextField::resetBottomInset()
    self.uglySide.call('ritual_ZN15QQuickTextField16resetBottomInsetEv')

  def fontChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextField::fontChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#fontChanged
    """
    #  void QQuickTextField::fontChanged()
    self.uglySide.call('ritual_ZN15QQuickTextField11fontChangedEv')

  def implicitWidthChanged3(self) -> None:
    """
    Calls Qt's 'void QQuickTextField::implicitWidthChanged3()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#implicitWidthChanged3
    """
    #  void QQuickTextField::implicitWidthChanged3()
    self.uglySide.call('ritual_ZN15QQuickTextField21implicitWidthChanged3Ev')

  def implicitHeightChanged3(self) -> None:
    """
    Calls Qt's 'void QQuickTextField::implicitHeightChanged3()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#implicitHeightChanged3
    """
    #  void QQuickTextField::implicitHeightChanged3()
    self.uglySide.call(
        'ritual_ZN15QQuickTextField22implicitHeightChanged3Ev',
    )

  def backgroundChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextField::backgroundChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#backgroundChanged
    """
    #  void QQuickTextField::backgroundChanged()
    self.uglySide.call('ritual_ZN15QQuickTextField17backgroundChangedEv')

  def placeholderTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextField::placeholderTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#placeholderTextChanged
    """
    #  void QQuickTextField::placeholderTextChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickTextField22placeholderTextChangedEv',
    )

  def focusReasonChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextField::focusReasonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#focusReasonChanged
    """
    #  void QQuickTextField::focusReasonChanged()
    self.uglySide.call('ritual_ZN15QQuickTextField18focusReasonChangedEv')

  @overload(QQuickMouseEvent)
  @overload(NoneType)
  def pressAndHold(self, event: Optional[QQuickMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextField::pressAndHold(QQuickMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#pressAndHold

    Parameters
    ----------

    event : Optional[QQuickMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextField::pressAndHold(QQuickMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN15QQuickTextField12pressAndHoldEP16QQuickMouseEvent',
        self._addressOf(event),
    )

  @overload(QQuickMouseEvent)
  @overload(NoneType)
  def pressed(self, event: Optional[QQuickMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextField::pressed(QQuickMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#pressed

    Parameters
    ----------

    event : Optional[QQuickMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextField::pressed(QQuickMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN15QQuickTextField7pressedEP16QQuickMouseEvent',
        self._addressOf(event),
    )

  @overload(QQuickMouseEvent)
  @overload(NoneType)
  def released(self, event: Optional[QQuickMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextField::released(QQuickMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#released

    Parameters
    ----------

    event : Optional[QQuickMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextField::released(QQuickMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN15QQuickTextField8releasedEP16QQuickMouseEvent',
        self._addressOf(event),
    )

  def hoveredChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextField::hoveredChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#hoveredChanged
    """
    #  void QQuickTextField::hoveredChanged()
    self.uglySide.call('ritual_ZN15QQuickTextField14hoveredChangedEv')

  def hoverEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextField::hoverEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#hoverEnabledChanged
    """
    #  void QQuickTextField::hoverEnabledChanged()
    self.uglySide.call('ritual_ZN15QQuickTextField19hoverEnabledChangedEv')

  def placeholderTextColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextField::placeholderTextColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#placeholderTextColorChanged
    """
    #  void QQuickTextField::placeholderTextColorChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickTextField27placeholderTextColorChangedEv',
    )

  def implicitBackgroundWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextField::implicitBackgroundWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html
    """
    #  void QQuickTextField::implicitBackgroundWidthChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickTextField30implicitBackgroundWidthChangedEv',
    )

  def implicitBackgroundHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextField::implicitBackgroundHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html
    """
    #  void QQuickTextField::implicitBackgroundHeightChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickTextField31implicitBackgroundHeightChangedEv',
    )

  def topInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextField::topInsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#topInsetChanged
    """
    #  void QQuickTextField::topInsetChanged()
    self.uglySide.call('ritual_ZN15QQuickTextField15topInsetChangedEv')

  def leftInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextField::leftInsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#leftInsetChanged
    """
    #  void QQuickTextField::leftInsetChanged()
    self.uglySide.call('ritual_ZN15QQuickTextField16leftInsetChangedEv')

  def rightInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextField::rightInsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#rightInsetChanged
    """
    #  void QQuickTextField::rightInsetChanged()
    self.uglySide.call('ritual_ZN15QQuickTextField17rightInsetChangedEv')

  def bottomInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextField::bottomInsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#bottomInsetChanged
    """
    #  void QQuickTextField::bottomInsetChanged()
    self.uglySide.call('ritual_ZN15QQuickTextField18bottomInsetChangedEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickTextField::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#classBegin
    """
    #  void QQuickTextField::classBegin()
    ritual = 'ritual_ZN15QQuickTextField10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickTextField10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickTextField::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#componentComplete
    """
    #  void QQuickTextField::componentComplete()
    ritual = 'ritual_ZN15QQuickTextField17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickTextField17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickTextField::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickTextField::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN15QQuickTextField10itemChangeEN10QQuickItem10ItemChangeER'
        'KNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickTextField10itemChangeEN10QQuickItem10ItemCh'
          'angeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickTextField::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickTextField::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN15QQuickTextField14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickTextField14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QMarginsF, QMarginsF)
  def insetChange(self, newInset: QMarginsF, oldInset: QMarginsF) -> None:
    """
    Calls Qt's 'void QQuickTextField::insetChange(const QMarginsF &newInset,
    const QMarginsF &oldInset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#insetChange

    Parameters
    ----------

    newInset : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.

    oldInset : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.
    """
    #  void QQuickTextField::insetChange(const QMarginsF &newInset, const
    #      QMarginsF &oldInset)
    ritual = 'ritual_ZN15QQuickTextField11insetChangeERK9QMarginsFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickTextField11insetChangeERK9QMarginsFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newInset), self._valueOf(oldInset),
    )

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      oldNode: Optional[QSGNode],
      data: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickTextField::updatePaintNode(QSGNode *oldNode,
    UpdatePaintNodeData *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#updatePaintNode

    Parameters
    ----------

    oldNode : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    data : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickTextField::updatePaintNode(QSGNode *oldNode,
    #      UpdatePaintNodeData *data)
    ritual = (
        'ritual_ZN15QQuickTextField15updatePaintNodeEP7QSGNodePN10QQuickIte'
        'm19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickTextField15updatePaintNodeEP7QSGNodePN10QQu'
          'ickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(oldNode, 'QSGNode'), self._addressOf(data),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextField::focusInEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextField::focusInEvent(QFocusEvent *event)
    ritual = 'ritual_ZN15QQuickTextField12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickTextField12focusInEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextField::focusOutEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#focusOutEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextField::focusOutEvent(QFocusEvent *event)
    ritual = 'ritual_ZN15QQuickTextField13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickTextField13focusOutEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextField::hoverEnterEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextField::hoverEnterEvent(QHoverEvent *event)
    ritual = 'ritual_ZN15QQuickTextField15hoverEnterEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickTextField15hoverEnterEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextField::hoverLeaveEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextField::hoverLeaveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN15QQuickTextField15hoverLeaveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickTextField15hoverLeaveEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextField::mousePressEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextField::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN15QQuickTextField15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickTextField15mousePressEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextField::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextField::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN15QQuickTextField14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickTextField14mouseMoveEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextField::mouseReleaseEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextField::mouseReleaseEvent(QMouseEvent *event)
    ritual = 'ritual_ZN15QQuickTextField17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickTextField17mouseReleaseEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextField::mouseDoubleClickEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfield.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextField::mouseDoubleClickEvent(QMouseEvent *event)
    ritual = (
        'ritual_ZN15QQuickTextField21mouseDoubleClickEventEP11QMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickTextField21mouseDoubleClickEventEP11QMouseE'
          'vent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextField::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextField::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN15QQuickTextField10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickTextField10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def d_func(self) -> Optional[QQuickTextFieldPrivate]:
    """
    Calls Qt's 'QQuickTextFieldPrivate *QQuickTextField::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfield.html#d_func

    Returns
    -------

    Optional[QQuickTextFieldPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextFieldPrivate *QQuickTextField::d_func()
    address = self.uglySide.call('ritual_ZN15QQuickTextField6d_funcEv')
    from . import QQuickTextFieldPrivate
    return QQuickTextFieldPrivate._cuteAt(address)
