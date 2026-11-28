"""
QQuickTextArea binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktextarea_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickTextArea to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtQuick import QQuickItem, QQuickTextEdit

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMarginsF, QMetaObject, QPointF, QRectF, QTimerEvent
  from ..QtGui import QColor, QFocusEvent, QFont, QHoverEvent, QMouseEvent
  from ..QtQuick import QQuickMouseEvent, QSGNode
  from . import QQuickTextAreaAttached, QQuickTextAreaPrivate
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
  QPointF = WAIT['QPointF']
  QQuickMouseEvent = WAIT['QQuickMouseEvent']
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTextArea(QQuickTextEdit):
  """
  The cute side of Qt's QQuickTextArea: a plain Python object standing in
  front of one C++ QQuickTextArea.

  It is built on the cute 'QQuickTextEdit', as Qt's QQuickTextArea is built
  on Qt's QQuickTextEdit, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTextArea that has a ritual and that Python can
  call so far, 67 names in all: 'metaObject', 'tr', 'qmlAttachedProperties',
  'font', 'setFont', 'background', 'setBackground', 'placeholderText',
  'setPlaceholderText', 'focusReason', 'setFocusReason', 'contains',
  'isHovered', 'setHovered', 'isHoverEnabled', 'setHoverEnabled',
  'resetHoverEnabled', 'placeholderTextColor', 'setPlaceholderTextColor',
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

  - Qt's 'void *QQuickTextArea::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickTextArea::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickTextArea::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'QQuickTextArea::~QQuickTextArea()': the destructor: Python never
    removes a C++ QQuickTextArea.
  - Qt's 'const QQuickTextAreaPrivate *QQuickTextArea::d_func() const': takes
    in Python what 'QQuickTextAreaPrivate *QQuickTextArea::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 77 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickTextArea is created at the first use, not by
    'QQuickTextArea(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTextArea.
  - Qt tells when it has removed the C++ QQuickTextArea. Every call on the
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
    Calls Qt's 'QString QQuickTextArea::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#tr

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
    #  QString QQuickTextArea::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickTextArea2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickTextAreaAttached]:
    """
    Calls Qt's 'QQuickTextAreaAttached
    *QQuickTextArea::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickTextAreaAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextAreaAttached *QQuickTextArea::qmlAttachedProperties(QObject
    #      *object)
    address = Rituals.call(
        'ritual_ZN14QQuickTextArea21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickTextAreaAttached
    return QQuickTextAreaAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTextArea'

  #  A C++ QQuickTextArea Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTextArea'

  #  The functions Qt calls itself that QQuickTextArea is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'insetChange': (
          ('_ZN14QQuickTextArea11insetChangeERK9QMarginsFS2_',
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
    Calls Qt's 'const QMetaObject *QQuickTextArea::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTextArea::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickTextArea10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickTextArea::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickTextArea::font() const
    address = self.uglySide.call('ritual_ZNK14QQuickTextArea4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def background(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickTextArea::background() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#background

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickTextArea::background() const
    address = self.uglySide.call('ritual_ZNK14QQuickTextArea10backgroundEv')
    return QQuickItem._cuteAt(address)

  def placeholderText(self) -> str:
    """
    Calls Qt's 'QString QQuickTextArea::placeholderText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#placeholderText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextArea::placeholderText() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickTextArea15placeholderTextEv',
    )

  def focusReason(self) -> Qt.FocusReason:
    """
    Calls Qt's 'Qt::FocusReason QQuickTextArea::focusReason() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#focusReason

    Returns
    -------

    Qt.FocusReason
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.FocusReason(number)'
      gives.
    """
    #  Qt::FocusReason QQuickTextArea::focusReason() const
    return Qt.FocusReason(self.uglySide.call(
        'ritual_ZNK14QQuickTextArea11focusReasonEv',
    ))

  @overload(QPointF)
  def contains(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QQuickTextArea::contains(const QPointF &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#contains

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QQuickTextArea::contains(const QPointF &point) const
    ritual = 'ritual_ZNK14QQuickTextArea8containsERK7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickTextArea8containsERK7QPointF'
    return self.uglySide.call(ritual, self._valueOf(point, 'QPointF'))

  def isHovered(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextArea::isHovered() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#isHovered
    """
    #  bool QQuickTextArea::isHovered() const
    return self.uglySide.call('ritual_ZNK14QQuickTextArea9isHoveredEv')

  def isHoverEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextArea::isHoverEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#isHoverEnabled
    """
    #  bool QQuickTextArea::isHoverEnabled() const
    return self.uglySide.call('ritual_ZNK14QQuickTextArea14isHoverEnabledEv')

  def placeholderTextColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickTextArea::placeholderTextColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#placeholderTextColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickTextArea::placeholderTextColor() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickTextArea20placeholderTextColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def implicitBackgroundWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextArea::implicitBackgroundWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#implicitBackgroundWidth
    """
    #  qreal QQuickTextArea::implicitBackgroundWidth() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickTextArea23implicitBackgroundWidthEv',
    )

  def implicitBackgroundHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextArea::implicitBackgroundHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#implicitBackgroundHeight
    """
    #  qreal QQuickTextArea::implicitBackgroundHeight() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickTextArea24implicitBackgroundHeightEv',
    )

  def topInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextArea::topInset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#topInset
    """
    #  qreal QQuickTextArea::topInset() const
    return self.uglySide.call('ritual_ZNK14QQuickTextArea8topInsetEv')

  def leftInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextArea::leftInset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#leftInset
    """
    #  qreal QQuickTextArea::leftInset() const
    return self.uglySide.call('ritual_ZNK14QQuickTextArea9leftInsetEv')

  def rightInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextArea::rightInset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#rightInset
    """
    #  qreal QQuickTextArea::rightInset() const
    return self.uglySide.call('ritual_ZNK14QQuickTextArea10rightInsetEv')

  def bottomInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextArea::bottomInset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#bottomInset
    """
    #  qreal QQuickTextArea::bottomInset() const
    return self.uglySide.call('ritual_ZNK14QQuickTextArea11bottomInsetEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickTextArea::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickTextArea::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN14QQuickTextArea7setFontERK5QFont', self._valueOf(font),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setBackground(self, background: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickTextArea::setBackground(QQuickItem *background)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#setBackground

    Parameters
    ----------

    background : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextArea::setBackground(QQuickItem *background)
    self.uglySide.call(
        'ritual_ZN14QQuickTextArea13setBackgroundEP10QQuickItem',
        self._addressOf(background),
    )

  @overload(str)
  def setPlaceholderText(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickTextArea::setPlaceholderText(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#setPlaceholderText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextArea::setPlaceholderText(const QString &text)
    self.uglySide.call(
        'ritual_ZN14QQuickTextArea18setPlaceholderTextERK7QString', text,
    )

  @overload(Qt.FocusReason)
  def setFocusReason(self, reason: Qt.FocusReason) -> None:
    """
    Calls Qt's 'void QQuickTextArea::setFocusReason(Qt::FocusReason reason)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#setFocusReason

    Parameters
    ----------

    reason : Qt.FocusReason
      Passed on as its number.
    """
    #  void QQuickTextArea::setFocusReason(Qt::FocusReason reason)
    self.uglySide.call(
        'ritual_ZN14QQuickTextArea14setFocusReasonEN2Qt11FocusReasonE',
        reason.value,
    )

  @overload(bool)
  def setHovered(self, hovered: bool) -> None:
    """
    Calls Qt's 'void QQuickTextArea::setHovered(bool hovered)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#setHovered

    Parameters
    ----------

    hovered : bool
      Passed on as it is.
    """
    #  void QQuickTextArea::setHovered(bool hovered)
    self.uglySide.call('ritual_ZN14QQuickTextArea10setHoveredEb', hovered)

  @overload(bool)
  def setHoverEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickTextArea::setHoverEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#setHoverEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickTextArea::setHoverEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN14QQuickTextArea15setHoverEnabledEb', enabled,
    )

  @overload(QColor)
  def setPlaceholderTextColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickTextArea::setPlaceholderTextColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#setPlaceholderTextColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickTextArea::setPlaceholderTextColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN14QQuickTextArea23setPlaceholderTextColorERK6QColor',
        self._valueOf(color),
    )

  @overload(float)
  def setTopInset(self, inset: float) -> None:
    """
    Calls Qt's 'void QQuickTextArea::setTopInset(qreal inset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#setTopInset

    Parameters
    ----------

    inset : float
      Passed on as it is.
    """
    #  void QQuickTextArea::setTopInset(qreal inset)
    self.uglySide.call('ritual_ZN14QQuickTextArea11setTopInsetEd', inset)

  @overload(float)
  def setLeftInset(self, inset: float) -> None:
    """
    Calls Qt's 'void QQuickTextArea::setLeftInset(qreal inset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#setLeftInset

    Parameters
    ----------

    inset : float
      Passed on as it is.
    """
    #  void QQuickTextArea::setLeftInset(qreal inset)
    self.uglySide.call('ritual_ZN14QQuickTextArea12setLeftInsetEd', inset)

  @overload(float)
  def setRightInset(self, inset: float) -> None:
    """
    Calls Qt's 'void QQuickTextArea::setRightInset(qreal inset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#setRightInset

    Parameters
    ----------

    inset : float
      Passed on as it is.
    """
    #  void QQuickTextArea::setRightInset(qreal inset)
    self.uglySide.call('ritual_ZN14QQuickTextArea13setRightInsetEd', inset)

  @overload(float)
  def setBottomInset(self, inset: float) -> None:
    """
    Calls Qt's 'void QQuickTextArea::setBottomInset(qreal inset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#setBottomInset

    Parameters
    ----------

    inset : float
      Passed on as it is.
    """
    #  void QQuickTextArea::setBottomInset(qreal inset)
    self.uglySide.call('ritual_ZN14QQuickTextArea14setBottomInsetEd', inset)

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
    Notes what was given, for Qt's 'QQuickTextArea::QQuickTextArea(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#QQuickTextArea

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTextArea::QQuickTextArea(QQuickItem *parent)
    self._noteCreation(QQuickTextArea, lambda: Rituals.call(
        'ritual_ZN14QQuickTextAreaC1EP10QQuickItem', self._addressOf(parent),
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
    Calls Qt's 'void QQuickTextArea::resetHoverEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#resetHoverEnabled
    """
    #  void QQuickTextArea::resetHoverEnabled()
    self.uglySide.call('ritual_ZN14QQuickTextArea17resetHoverEnabledEv')

  def resetTopInset(self) -> None:
    """
    Calls Qt's 'void QQuickTextArea::resetTopInset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#resetTopInset
    """
    #  void QQuickTextArea::resetTopInset()
    self.uglySide.call('ritual_ZN14QQuickTextArea13resetTopInsetEv')

  def resetLeftInset(self) -> None:
    """
    Calls Qt's 'void QQuickTextArea::resetLeftInset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#resetLeftInset
    """
    #  void QQuickTextArea::resetLeftInset()
    self.uglySide.call('ritual_ZN14QQuickTextArea14resetLeftInsetEv')

  def resetRightInset(self) -> None:
    """
    Calls Qt's 'void QQuickTextArea::resetRightInset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#resetRightInset
    """
    #  void QQuickTextArea::resetRightInset()
    self.uglySide.call('ritual_ZN14QQuickTextArea15resetRightInsetEv')

  def resetBottomInset(self) -> None:
    """
    Calls Qt's 'void QQuickTextArea::resetBottomInset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#resetBottomInset
    """
    #  void QQuickTextArea::resetBottomInset()
    self.uglySide.call('ritual_ZN14QQuickTextArea16resetBottomInsetEv')

  def fontChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextArea::fontChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#fontChanged
    """
    #  void QQuickTextArea::fontChanged()
    self.uglySide.call('ritual_ZN14QQuickTextArea11fontChangedEv')

  def implicitWidthChanged3(self) -> None:
    """
    Calls Qt's 'void QQuickTextArea::implicitWidthChanged3()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#implicitWidthChanged3
    """
    #  void QQuickTextArea::implicitWidthChanged3()
    self.uglySide.call('ritual_ZN14QQuickTextArea21implicitWidthChanged3Ev')

  def implicitHeightChanged3(self) -> None:
    """
    Calls Qt's 'void QQuickTextArea::implicitHeightChanged3()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#implicitHeightChanged3
    """
    #  void QQuickTextArea::implicitHeightChanged3()
    self.uglySide.call('ritual_ZN14QQuickTextArea22implicitHeightChanged3Ev')

  def backgroundChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextArea::backgroundChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#backgroundChanged
    """
    #  void QQuickTextArea::backgroundChanged()
    self.uglySide.call('ritual_ZN14QQuickTextArea17backgroundChangedEv')

  def placeholderTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextArea::placeholderTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#placeholderTextChanged
    """
    #  void QQuickTextArea::placeholderTextChanged()
    self.uglySide.call('ritual_ZN14QQuickTextArea22placeholderTextChangedEv')

  def focusReasonChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextArea::focusReasonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#focusReasonChanged
    """
    #  void QQuickTextArea::focusReasonChanged()
    self.uglySide.call('ritual_ZN14QQuickTextArea18focusReasonChangedEv')

  @overload(QQuickMouseEvent)
  @overload(NoneType)
  def pressAndHold(self, event: Optional[QQuickMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextArea::pressAndHold(QQuickMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#pressAndHold

    Parameters
    ----------

    event : Optional[QQuickMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextArea::pressAndHold(QQuickMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN14QQuickTextArea12pressAndHoldEP16QQuickMouseEvent',
        self._addressOf(event),
    )

  @overload(QQuickMouseEvent)
  @overload(NoneType)
  def pressed(self, event: Optional[QQuickMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextArea::pressed(QQuickMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#pressed

    Parameters
    ----------

    event : Optional[QQuickMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextArea::pressed(QQuickMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN14QQuickTextArea7pressedEP16QQuickMouseEvent',
        self._addressOf(event),
    )

  @overload(QQuickMouseEvent)
  @overload(NoneType)
  def released(self, event: Optional[QQuickMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextArea::released(QQuickMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#released

    Parameters
    ----------

    event : Optional[QQuickMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextArea::released(QQuickMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN14QQuickTextArea8releasedEP16QQuickMouseEvent',
        self._addressOf(event),
    )

  def hoveredChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextArea::hoveredChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#hoveredChanged
    """
    #  void QQuickTextArea::hoveredChanged()
    self.uglySide.call('ritual_ZN14QQuickTextArea14hoveredChangedEv')

  def hoverEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextArea::hoverEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#hoverEnabledChanged
    """
    #  void QQuickTextArea::hoverEnabledChanged()
    self.uglySide.call('ritual_ZN14QQuickTextArea19hoverEnabledChangedEv')

  def placeholderTextColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextArea::placeholderTextColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#placeholderTextColorChanged
    """
    #  void QQuickTextArea::placeholderTextColorChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickTextArea27placeholderTextColorChangedEv',
    )

  def implicitBackgroundWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextArea::implicitBackgroundWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#implicitBackgroundWidthChanged
    """
    #  void QQuickTextArea::implicitBackgroundWidthChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickTextArea30implicitBackgroundWidthChangedEv',
    )

  def implicitBackgroundHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextArea::implicitBackgroundHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html
    """
    #  void QQuickTextArea::implicitBackgroundHeightChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickTextArea31implicitBackgroundHeightChangedEv',
    )

  def topInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextArea::topInsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#topInsetChanged
    """
    #  void QQuickTextArea::topInsetChanged()
    self.uglySide.call('ritual_ZN14QQuickTextArea15topInsetChangedEv')

  def leftInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextArea::leftInsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#leftInsetChanged
    """
    #  void QQuickTextArea::leftInsetChanged()
    self.uglySide.call('ritual_ZN14QQuickTextArea16leftInsetChangedEv')

  def rightInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextArea::rightInsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#rightInsetChanged
    """
    #  void QQuickTextArea::rightInsetChanged()
    self.uglySide.call('ritual_ZN14QQuickTextArea17rightInsetChangedEv')

  def bottomInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextArea::bottomInsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#bottomInsetChanged
    """
    #  void QQuickTextArea::bottomInsetChanged()
    self.uglySide.call('ritual_ZN14QQuickTextArea18bottomInsetChangedEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickTextArea::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#classBegin
    """
    #  void QQuickTextArea::classBegin()
    ritual = 'ritual_ZN14QQuickTextArea10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTextArea10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickTextArea::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#componentComplete
    """
    #  void QQuickTextArea::componentComplete()
    ritual = 'ritual_ZN14QQuickTextArea17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTextArea17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickTextArea::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickTextArea::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN14QQuickTextArea10itemChangeEN10QQuickItem10ItemChangeERK'
        'NS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickTextArea10itemChangeEN10QQuickItem10ItemCha'
          'ngeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickTextArea::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickTextArea::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN14QQuickTextArea14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTextArea14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QMarginsF, QMarginsF)
  def insetChange(self, newInset: QMarginsF, oldInset: QMarginsF) -> None:
    """
    Calls Qt's 'void QQuickTextArea::insetChange(const QMarginsF &newInset,
    const QMarginsF &oldInset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#insetChange

    Parameters
    ----------

    newInset : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.

    oldInset : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.
    """
    #  void QQuickTextArea::insetChange(const QMarginsF &newInset, const
    #      QMarginsF &oldInset)
    ritual = 'ritual_ZN14QQuickTextArea11insetChangeERK9QMarginsFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTextArea11insetChangeERK9QMarginsFS2_'
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
    Calls Qt's 'QSGNode *QQuickTextArea::updatePaintNode(QSGNode *oldNode,
    UpdatePaintNodeData *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#updatePaintNode

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
    #  QSGNode *QQuickTextArea::updatePaintNode(QSGNode *oldNode,
    #      UpdatePaintNodeData *data)
    ritual = (
        'ritual_ZN14QQuickTextArea15updatePaintNodeEP7QSGNodePN10QQuickItem'
        '19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickTextArea15updatePaintNodeEP7QSGNodePN10QQui'
          'ckItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(oldNode, 'QSGNode'), self._addressOf(data),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextArea::focusInEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextArea::focusInEvent(QFocusEvent *event)
    ritual = 'ritual_ZN14QQuickTextArea12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTextArea12focusInEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextArea::focusOutEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#focusOutEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextArea::focusOutEvent(QFocusEvent *event)
    ritual = 'ritual_ZN14QQuickTextArea13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTextArea13focusOutEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextArea::hoverEnterEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextArea::hoverEnterEvent(QHoverEvent *event)
    ritual = 'ritual_ZN14QQuickTextArea15hoverEnterEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickTextArea15hoverEnterEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextArea::hoverLeaveEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextArea::hoverLeaveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN14QQuickTextArea15hoverLeaveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickTextArea15hoverLeaveEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextArea::mousePressEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextArea::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN14QQuickTextArea15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickTextArea15mousePressEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextArea::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextArea::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN14QQuickTextArea14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTextArea14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextArea::mouseReleaseEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextArea::mouseReleaseEvent(QMouseEvent *event)
    ritual = 'ritual_ZN14QQuickTextArea17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickTextArea17mouseReleaseEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextArea::mouseDoubleClickEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextarea.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextArea::mouseDoubleClickEvent(QMouseEvent *event)
    ritual = (
        'ritual_ZN14QQuickTextArea21mouseDoubleClickEventEP11QMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickTextArea21mouseDoubleClickEventEP11QMouseEv'
          'ent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QQuickTextArea::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextArea::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN14QQuickTextArea10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTextArea10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def d_func(self) -> Optional[QQuickTextAreaPrivate]:
    """
    Calls Qt's 'QQuickTextAreaPrivate *QQuickTextArea::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextarea.html#d_func

    Returns
    -------

    Optional[QQuickTextAreaPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextAreaPrivate *QQuickTextArea::d_func()
    address = self.uglySide.call('ritual_ZN14QQuickTextArea6d_funcEv')
    from . import QQuickTextAreaPrivate
    return QQuickTextAreaPrivate._cuteAt(address)
