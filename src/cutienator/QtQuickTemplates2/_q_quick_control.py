"""
QQuickControl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcontrol_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickControl to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QLocale, QMarginsF, QMetaObject, QRectF, QVariant
  from ..QtGui import QFocusEvent, QFont, QHoverEvent, QMouseEvent
  from ..QtGui import QTouchEvent, QWheelEvent
  from . import QQuickControlPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFocusEvent = WAIT['QFocusEvent']
  QFont = WAIT['QFont']
  QHoverEvent = WAIT['QHoverEvent']
  QLocale = WAIT['QLocale']
  QMarginsF = WAIT['QMarginsF']
  QMouseEvent = WAIT['QMouseEvent']
  QRectF = WAIT['QRectF']
  QTouchEvent = WAIT['QTouchEvent']
  QVariant = WAIT['QVariant']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickControl(QQuickItem):
  """
  The cute side of Qt's QQuickControl: a plain Python object standing in
  front of one C++ QQuickControl.

  It is built on the cute 'QQuickItem', as Qt's QQuickControl is built on
  Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickControl that has a ritual and that Python can
  call so far, 130 names in all: 'metaObject', 'tr', 'font', 'setFont',
  'resetFont', 'availableWidth', 'availableHeight', 'padding', 'setPadding',
  'resetPadding', 'topPadding', 'setTopPadding', 'resetTopPadding',
  'leftPadding', 'setLeftPadding', 'resetLeftPadding', 'rightPadding',
  'setRightPadding', 'resetRightPadding', 'bottomPadding',
  'setBottomPadding', 'resetBottomPadding', 'spacing', 'setSpacing',
  'resetSpacing', 'locale', 'setLocale', 'resetLocale', 'isMirrored',
  'focusReason', 'setFocusReason', 'hasVisualFocus', 'isHovered',
  'setHovered', 'isHoverEnabled', 'setHoverEnabled', 'resetHoverEnabled',
  'isWheelEnabled', 'setWheelEnabled', 'background', 'setBackground',
  'contentItem', 'setContentItem', 'baselineOffset', 'setBaselineOffset',
  'resetBaselineOffset', 'horizontalPadding', 'setHorizontalPadding',
  'resetHorizontalPadding', 'verticalPadding', 'setVerticalPadding',
  'resetVerticalPadding', 'implicitContentWidth', 'implicitContentHeight',
  'implicitBackgroundWidth', 'implicitBackgroundHeight', 'topInset',
  'setTopInset', 'resetTopInset', 'leftInset', 'setLeftInset',
  'resetLeftInset', 'rightInset', 'setRightInset', 'resetRightInset',
  'bottomInset', 'setBottomInset', 'resetBottomInset', 'fontChanged',
  'availableWidthChanged', 'availableHeightChanged', 'paddingChanged',
  'topPaddingChanged', 'leftPaddingChanged', 'rightPaddingChanged',
  'bottomPaddingChanged', 'spacingChanged', 'localeChanged',
  'focusReasonChanged', 'mirroredChanged', 'visualFocusChanged',
  'hoveredChanged', 'hoverEnabledChanged', 'wheelEnabledChanged',
  'backgroundChanged', 'contentItemChanged', 'baselineOffsetChanged',
  'horizontalPaddingChanged', 'verticalPaddingChanged',
  'implicitContentWidthChanged', 'implicitContentHeightChanged',
  'implicitBackgroundWidthChanged', 'implicitBackgroundHeightChanged',
  'topInsetChanged', 'leftInsetChanged', 'rightInsetChanged',
  'bottomInsetChanged', 'defaultFont', 'classBegin', 'componentComplete',
  'itemChange', 'focusInEvent', 'focusOutEvent', 'hoverEnterEvent',
  'hoverMoveEvent', 'hoverLeaveEvent', 'mousePressEvent', 'mouseMoveEvent',
  'mouseReleaseEvent', 'mouseUngrabEvent', 'touchEvent', 'touchUngrabEvent',
  'wheelEvent', 'geometryChange', 'fontChange', 'hoverChange',
  'mirrorChange', 'spacingChange', 'paddingChange', 'contentItemChange',
  'localeChange', 'insetChange', 'enabledChange', 'accessibleRole',
  'accessibilityActiveChanged', 'accessibleName', 'maybeSetAccessibleName',
  'accessibleProperty', 'setAccessibleProperty', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickControl::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickControl::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickControl::~QQuickControl()': the destructor: Python never
    removes a C++ QQuickControl.
  - Qt's 'QQuickControl::QQuickControl(QQuickControlPrivate &dd, QQuickItem
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickControlPrivate *QQuickControl::d_func() const': takes
    in Python what 'QQuickControlPrivate *QQuickControl::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 140 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickControl is created at the first use, not by
    'QQuickControl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickControl.
  - Qt tells when it has removed the C++ QQuickControl. Every call on the
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
    Calls Qt's 'QString QQuickControl::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#tr

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
    #  QString QQuickControl::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QQuickControl2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickControl'

  #  A C++ QQuickControl Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickControl'

  #  The functions Qt calls itself that QQuickControl is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'defaultFont': (
          ('_ZNK13QQuickControl11defaultFontEv',
           ('address', 'value', 'QtGui:QFont'),
           ()),
      ),
      'fontChange': (
          ('_ZN13QQuickControl10fontChangeERK5QFontS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QFont'),
               ('address', 'value', 'QtGui:QFont'),
           )),
      ),
      'hoverChange': (
          ('_ZN13QQuickControl11hoverChangeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'mirrorChange': (
          ('_ZN13QQuickControl12mirrorChangeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'spacingChange': (
          ('_ZN13QQuickControl13spacingChangeEdd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
               ('double', 'number', ''),
           )),
      ),
      'paddingChange': (
          ('_ZN13QQuickControl13paddingChangeERK9QMarginsFS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QMarginsF'),
               ('address', 'value', 'QtCore:QMarginsF'),
           )),
      ),
      'contentItemChange': (
          ('_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'localeChange': (
          ('_ZN13QQuickControl12localeChangeERK7QLocaleS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QLocale'),
               ('address', 'value', 'QtCore:QLocale'),
           )),
      ),
      'insetChange': (
          ('_ZN13QQuickControl11insetChangeERK9QMarginsFS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QMarginsF'),
               ('address', 'value', 'QtCore:QMarginsF'),
           )),
      ),
      'enabledChange': (
          ('_ZN13QQuickControl13enabledChangeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'accessibleRole': (
          ('_ZNK13QQuickControl14accessibleRoleEv',
           ('int', 'enum', 'QtGui:QAccessible.Role'),
           ()),
      ),
      'accessibilityActiveChanged': (
          ('_ZN13QQuickControl26accessibilityActiveChangedEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
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
    Calls Qt's 'const QMetaObject *QQuickControl::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickControl::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QQuickControl10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickControl::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickControl::font() const
    address = self.uglySide.call('ritual_ZNK13QQuickControl4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def availableWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickControl::availableWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#availableWidth
    """
    #  qreal QQuickControl::availableWidth() const
    return self.uglySide.call('ritual_ZNK13QQuickControl14availableWidthEv')

  def availableHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickControl::availableHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#availableHeight
    """
    #  qreal QQuickControl::availableHeight() const
    return self.uglySide.call('ritual_ZNK13QQuickControl15availableHeightEv')

  def padding(self) -> float:
    """
    Calls Qt's 'qreal QQuickControl::padding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#padding
    """
    #  qreal QQuickControl::padding() const
    return self.uglySide.call('ritual_ZNK13QQuickControl7paddingEv')

  def topPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickControl::topPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#topPadding
    """
    #  qreal QQuickControl::topPadding() const
    return self.uglySide.call('ritual_ZNK13QQuickControl10topPaddingEv')

  def leftPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickControl::leftPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#leftPadding
    """
    #  qreal QQuickControl::leftPadding() const
    return self.uglySide.call('ritual_ZNK13QQuickControl11leftPaddingEv')

  def rightPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickControl::rightPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#rightPadding
    """
    #  qreal QQuickControl::rightPadding() const
    return self.uglySide.call('ritual_ZNK13QQuickControl12rightPaddingEv')

  def bottomPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickControl::bottomPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#bottomPadding
    """
    #  qreal QQuickControl::bottomPadding() const
    return self.uglySide.call('ritual_ZNK13QQuickControl13bottomPaddingEv')

  def spacing(self) -> float:
    """
    Calls Qt's 'qreal QQuickControl::spacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#spacing
    """
    #  qreal QQuickControl::spacing() const
    return self.uglySide.call('ritual_ZNK13QQuickControl7spacingEv')

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QQuickControl::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QQuickControl::locale() const
    address = self.uglySide.call('ritual_ZNK13QQuickControl6localeEv')
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  def isMirrored(self) -> bool:
    """
    Calls Qt's 'bool QQuickControl::isMirrored() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#isMirrored
    """
    #  bool QQuickControl::isMirrored() const
    return self.uglySide.call('ritual_ZNK13QQuickControl10isMirroredEv')

  def focusReason(self) -> Qt.FocusReason:
    """
    Calls Qt's 'Qt::FocusReason QQuickControl::focusReason() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#focusReason

    Returns
    -------

    Qt.FocusReason
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.FocusReason(number)'
      gives.
    """
    #  Qt::FocusReason QQuickControl::focusReason() const
    return Qt.FocusReason(self.uglySide.call(
        'ritual_ZNK13QQuickControl11focusReasonEv',
    ))

  def hasVisualFocus(self) -> bool:
    """
    Calls Qt's 'bool QQuickControl::hasVisualFocus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#hasVisualFocus
    """
    #  bool QQuickControl::hasVisualFocus() const
    return self.uglySide.call('ritual_ZNK13QQuickControl14hasVisualFocusEv')

  def isHovered(self) -> bool:
    """
    Calls Qt's 'bool QQuickControl::isHovered() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#isHovered
    """
    #  bool QQuickControl::isHovered() const
    return self.uglySide.call('ritual_ZNK13QQuickControl9isHoveredEv')

  def isHoverEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickControl::isHoverEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#isHoverEnabled
    """
    #  bool QQuickControl::isHoverEnabled() const
    return self.uglySide.call('ritual_ZNK13QQuickControl14isHoverEnabledEv')

  def isWheelEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickControl::isWheelEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#isWheelEnabled
    """
    #  bool QQuickControl::isWheelEnabled() const
    return self.uglySide.call('ritual_ZNK13QQuickControl14isWheelEnabledEv')

  def background(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickControl::background() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#background

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickControl::background() const
    address = self.uglySide.call('ritual_ZNK13QQuickControl10backgroundEv')
    return QQuickItem._cuteAt(address)

  def contentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickControl::contentItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#contentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickControl::contentItem() const
    address = self.uglySide.call('ritual_ZNK13QQuickControl11contentItemEv')
    return QQuickItem._cuteAt(address)

  def baselineOffset(self) -> float:
    """
    Calls Qt's 'qreal QQuickControl::baselineOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#baselineOffset
    """
    #  qreal QQuickControl::baselineOffset() const
    return self.uglySide.call('ritual_ZNK13QQuickControl14baselineOffsetEv')

  def horizontalPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickControl::horizontalPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#horizontalPadding
    """
    #  qreal QQuickControl::horizontalPadding() const
    return self.uglySide.call(
        'ritual_ZNK13QQuickControl17horizontalPaddingEv',
    )

  def verticalPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickControl::verticalPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#verticalPadding
    """
    #  qreal QQuickControl::verticalPadding() const
    return self.uglySide.call('ritual_ZNK13QQuickControl15verticalPaddingEv')

  def implicitContentWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickControl::implicitContentWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#implicitContentWidth
    """
    #  qreal QQuickControl::implicitContentWidth() const
    return self.uglySide.call(
        'ritual_ZNK13QQuickControl20implicitContentWidthEv',
    )

  def implicitContentHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickControl::implicitContentHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#implicitContentHeight
    """
    #  qreal QQuickControl::implicitContentHeight() const
    return self.uglySide.call(
        'ritual_ZNK13QQuickControl21implicitContentHeightEv',
    )

  def implicitBackgroundWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickControl::implicitBackgroundWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#implicitBackgroundWidth
    """
    #  qreal QQuickControl::implicitBackgroundWidth() const
    return self.uglySide.call(
        'ritual_ZNK13QQuickControl23implicitBackgroundWidthEv',
    )

  def implicitBackgroundHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickControl::implicitBackgroundHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#implicitBackgroundHeight
    """
    #  qreal QQuickControl::implicitBackgroundHeight() const
    return self.uglySide.call(
        'ritual_ZNK13QQuickControl24implicitBackgroundHeightEv',
    )

  def topInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickControl::topInset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#topInset
    """
    #  qreal QQuickControl::topInset() const
    return self.uglySide.call('ritual_ZNK13QQuickControl8topInsetEv')

  def leftInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickControl::leftInset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#leftInset
    """
    #  qreal QQuickControl::leftInset() const
    return self.uglySide.call('ritual_ZNK13QQuickControl9leftInsetEv')

  def rightInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickControl::rightInset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#rightInset
    """
    #  qreal QQuickControl::rightInset() const
    return self.uglySide.call('ritual_ZNK13QQuickControl10rightInsetEv')

  def bottomInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickControl::bottomInset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#bottomInset
    """
    #  qreal QQuickControl::bottomInset() const
    return self.uglySide.call('ritual_ZNK13QQuickControl11bottomInsetEv')

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickControl::defaultFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickControl::defaultFont() const
    ritual = 'ritual_ZNK13QQuickControl11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQuickControl11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickControl::accessibleRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickControl::accessibleRole() const
    ritual = 'ritual_ZNK13QQuickControl14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQuickControl14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  def accessibleName(self) -> str:
    """
    Calls Qt's 'QString QQuickControl::accessibleName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#accessibleName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickControl::accessibleName() const
    return self.uglySide.call('ritual_ZNK13QQuickControl14accessibleNameEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickControl::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickControl::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN13QQuickControl7setFontERK5QFont', self._valueOf(font),
    )

  @overload(float)
  def setPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickControl::setPadding(qreal padding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#setPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickControl::setPadding(qreal padding)
    self.uglySide.call('ritual_ZN13QQuickControl10setPaddingEd', padding)

  @overload(float)
  def setTopPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickControl::setTopPadding(qreal padding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#setTopPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickControl::setTopPadding(qreal padding)
    self.uglySide.call('ritual_ZN13QQuickControl13setTopPaddingEd', padding)

  @overload(float)
  def setLeftPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickControl::setLeftPadding(qreal padding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#setLeftPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickControl::setLeftPadding(qreal padding)
    self.uglySide.call('ritual_ZN13QQuickControl14setLeftPaddingEd', padding)

  @overload(float)
  def setRightPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickControl::setRightPadding(qreal padding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#setRightPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickControl::setRightPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN13QQuickControl15setRightPaddingEd', padding,
    )

  @overload(float)
  def setBottomPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickControl::setBottomPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#setBottomPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickControl::setBottomPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN13QQuickControl16setBottomPaddingEd', padding,
    )

  @overload(float)
  def setSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QQuickControl::setSpacing(qreal spacing)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#setSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QQuickControl::setSpacing(qreal spacing)
    self.uglySide.call('ritual_ZN13QQuickControl10setSpacingEd', spacing)

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QQuickControl::setLocale(const QLocale &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QQuickControl::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN13QQuickControl9setLocaleERK7QLocale',
        self._valueOf(locale),
    )

  @overload(Qt.FocusReason)
  def setFocusReason(self, reason: Qt.FocusReason) -> None:
    """
    Calls Qt's 'void QQuickControl::setFocusReason(Qt::FocusReason reason)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#setFocusReason

    Parameters
    ----------

    reason : Qt.FocusReason
      Passed on as its number.
    """
    #  void QQuickControl::setFocusReason(Qt::FocusReason reason)
    self.uglySide.call(
        'ritual_ZN13QQuickControl14setFocusReasonEN2Qt11FocusReasonE',
        reason.value,
    )

  @overload(bool)
  def setHovered(self, hovered: bool) -> None:
    """
    Calls Qt's 'void QQuickControl::setHovered(bool hovered)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#setHovered

    Parameters
    ----------

    hovered : bool
      Passed on as it is.
    """
    #  void QQuickControl::setHovered(bool hovered)
    self.uglySide.call('ritual_ZN13QQuickControl10setHoveredEb', hovered)

  @overload(bool)
  def setHoverEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickControl::setHoverEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#setHoverEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickControl::setHoverEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN13QQuickControl15setHoverEnabledEb', enabled,
    )

  @overload(bool)
  def setWheelEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickControl::setWheelEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#setWheelEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickControl::setWheelEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN13QQuickControl15setWheelEnabledEb', enabled,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setBackground(self, background: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickControl::setBackground(QQuickItem *background)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#setBackground

    Parameters
    ----------

    background : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickControl::setBackground(QQuickItem *background)
    self.uglySide.call(
        'ritual_ZN13QQuickControl13setBackgroundEP10QQuickItem',
        self._addressOf(background),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setContentItem(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickControl::setContentItem(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#setContentItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickControl::setContentItem(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN13QQuickControl14setContentItemEP10QQuickItem',
        self._addressOf(item),
    )

  @overload(float)
  def setBaselineOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void QQuickControl::setBaselineOffset(qreal offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#setBaselineOffset

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QQuickControl::setBaselineOffset(qreal offset)
    self.uglySide.call(
        'ritual_ZN13QQuickControl17setBaselineOffsetEd', offset,
    )

  @overload(float)
  def setHorizontalPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickControl::setHorizontalPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#setHorizontalPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickControl::setHorizontalPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN13QQuickControl20setHorizontalPaddingEd', padding,
    )

  @overload(float)
  def setVerticalPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickControl::setVerticalPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#setVerticalPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickControl::setVerticalPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN13QQuickControl18setVerticalPaddingEd', padding,
    )

  @overload(float)
  def setTopInset(self, inset: float) -> None:
    """
    Calls Qt's 'void QQuickControl::setTopInset(qreal inset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#setTopInset

    Parameters
    ----------

    inset : float
      Passed on as it is.
    """
    #  void QQuickControl::setTopInset(qreal inset)
    self.uglySide.call('ritual_ZN13QQuickControl11setTopInsetEd', inset)

  @overload(float)
  def setLeftInset(self, inset: float) -> None:
    """
    Calls Qt's 'void QQuickControl::setLeftInset(qreal inset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#setLeftInset

    Parameters
    ----------

    inset : float
      Passed on as it is.
    """
    #  void QQuickControl::setLeftInset(qreal inset)
    self.uglySide.call('ritual_ZN13QQuickControl12setLeftInsetEd', inset)

  @overload(float)
  def setRightInset(self, inset: float) -> None:
    """
    Calls Qt's 'void QQuickControl::setRightInset(qreal inset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#setRightInset

    Parameters
    ----------

    inset : float
      Passed on as it is.
    """
    #  void QQuickControl::setRightInset(qreal inset)
    self.uglySide.call('ritual_ZN13QQuickControl13setRightInsetEd', inset)

  @overload(float)
  def setBottomInset(self, inset: float) -> None:
    """
    Calls Qt's 'void QQuickControl::setBottomInset(qreal inset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#setBottomInset

    Parameters
    ----------

    inset : float
      Passed on as it is.
    """
    #  void QQuickControl::setBottomInset(qreal inset)
    self.uglySide.call('ritual_ZN13QQuickControl14setBottomInsetEd', inset)

  @overload(str, QVariant)
  @overload(NoneType, QVariant)
  def setAccessibleProperty(
      self,
      propertyName: Optional[str],
      value: QVariant,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickControl::setAccessibleProperty(const char
    *propertyName, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#setAccessibleProperty

    Parameters
    ----------

    propertyName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QQuickControl::setAccessibleProperty(const char *propertyName,
    #      const QVariant &value)
    return self.uglySide.call(
        'ritual_ZN13QQuickControl21setAccessiblePropertyEPKcRK8QVariant',
        self._bytesOf(propertyName), self._valueOf(value),
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
    Notes what was given, for Qt's 'QQuickControl::QQuickControl(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#QQuickControl

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickControl::QQuickControl(QQuickItem *parent)
    self._noteCreation(QQuickControl, lambda: Rituals.call(
        'ritual_ZN13QQuickControlC1EP10QQuickItem', self._addressOf(parent),
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

  def resetFont(self) -> None:
    """
    Calls Qt's 'void QQuickControl::resetFont()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#resetFont
    """
    #  void QQuickControl::resetFont()
    self.uglySide.call('ritual_ZN13QQuickControl9resetFontEv')

  def resetPadding(self) -> None:
    """
    Calls Qt's 'void QQuickControl::resetPadding()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#resetPadding
    """
    #  void QQuickControl::resetPadding()
    self.uglySide.call('ritual_ZN13QQuickControl12resetPaddingEv')

  def resetTopPadding(self) -> None:
    """
    Calls Qt's 'void QQuickControl::resetTopPadding()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#resetTopPadding
    """
    #  void QQuickControl::resetTopPadding()
    self.uglySide.call('ritual_ZN13QQuickControl15resetTopPaddingEv')

  def resetLeftPadding(self) -> None:
    """
    Calls Qt's 'void QQuickControl::resetLeftPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#resetLeftPadding
    """
    #  void QQuickControl::resetLeftPadding()
    self.uglySide.call('ritual_ZN13QQuickControl16resetLeftPaddingEv')

  def resetRightPadding(self) -> None:
    """
    Calls Qt's 'void QQuickControl::resetRightPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#resetRightPadding
    """
    #  void QQuickControl::resetRightPadding()
    self.uglySide.call('ritual_ZN13QQuickControl17resetRightPaddingEv')

  def resetBottomPadding(self) -> None:
    """
    Calls Qt's 'void QQuickControl::resetBottomPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#resetBottomPadding
    """
    #  void QQuickControl::resetBottomPadding()
    self.uglySide.call('ritual_ZN13QQuickControl18resetBottomPaddingEv')

  def resetSpacing(self) -> None:
    """
    Calls Qt's 'void QQuickControl::resetSpacing()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#resetSpacing
    """
    #  void QQuickControl::resetSpacing()
    self.uglySide.call('ritual_ZN13QQuickControl12resetSpacingEv')

  def resetLocale(self) -> None:
    """
    Calls Qt's 'void QQuickControl::resetLocale()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#resetLocale
    """
    #  void QQuickControl::resetLocale()
    self.uglySide.call('ritual_ZN13QQuickControl11resetLocaleEv')

  def resetHoverEnabled(self) -> None:
    """
    Calls Qt's 'void QQuickControl::resetHoverEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#resetHoverEnabled
    """
    #  void QQuickControl::resetHoverEnabled()
    self.uglySide.call('ritual_ZN13QQuickControl17resetHoverEnabledEv')

  def resetBaselineOffset(self) -> None:
    """
    Calls Qt's 'void QQuickControl::resetBaselineOffset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#resetBaselineOffset
    """
    #  void QQuickControl::resetBaselineOffset()
    self.uglySide.call('ritual_ZN13QQuickControl19resetBaselineOffsetEv')

  def resetHorizontalPadding(self) -> None:
    """
    Calls Qt's 'void QQuickControl::resetHorizontalPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#resetHorizontalPadding
    """
    #  void QQuickControl::resetHorizontalPadding()
    self.uglySide.call('ritual_ZN13QQuickControl22resetHorizontalPaddingEv')

  def resetVerticalPadding(self) -> None:
    """
    Calls Qt's 'void QQuickControl::resetVerticalPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#resetVerticalPadding
    """
    #  void QQuickControl::resetVerticalPadding()
    self.uglySide.call('ritual_ZN13QQuickControl20resetVerticalPaddingEv')

  def resetTopInset(self) -> None:
    """
    Calls Qt's 'void QQuickControl::resetTopInset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#resetTopInset
    """
    #  void QQuickControl::resetTopInset()
    self.uglySide.call('ritual_ZN13QQuickControl13resetTopInsetEv')

  def resetLeftInset(self) -> None:
    """
    Calls Qt's 'void QQuickControl::resetLeftInset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#resetLeftInset
    """
    #  void QQuickControl::resetLeftInset()
    self.uglySide.call('ritual_ZN13QQuickControl14resetLeftInsetEv')

  def resetRightInset(self) -> None:
    """
    Calls Qt's 'void QQuickControl::resetRightInset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#resetRightInset
    """
    #  void QQuickControl::resetRightInset()
    self.uglySide.call('ritual_ZN13QQuickControl15resetRightInsetEv')

  def resetBottomInset(self) -> None:
    """
    Calls Qt's 'void QQuickControl::resetBottomInset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#resetBottomInset
    """
    #  void QQuickControl::resetBottomInset()
    self.uglySide.call('ritual_ZN13QQuickControl16resetBottomInsetEv')

  def fontChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::fontChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#fontChanged
    """
    #  void QQuickControl::fontChanged()
    self.uglySide.call('ritual_ZN13QQuickControl11fontChangedEv')

  def availableWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::availableWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#availableWidthChanged
    """
    #  void QQuickControl::availableWidthChanged()
    self.uglySide.call('ritual_ZN13QQuickControl21availableWidthChangedEv')

  def availableHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::availableHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#availableHeightChanged
    """
    #  void QQuickControl::availableHeightChanged()
    self.uglySide.call('ritual_ZN13QQuickControl22availableHeightChangedEv')

  def paddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::paddingChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#paddingChanged
    """
    #  void QQuickControl::paddingChanged()
    self.uglySide.call('ritual_ZN13QQuickControl14paddingChangedEv')

  def topPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::topPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#topPaddingChanged
    """
    #  void QQuickControl::topPaddingChanged()
    self.uglySide.call('ritual_ZN13QQuickControl17topPaddingChangedEv')

  def leftPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::leftPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#leftPaddingChanged
    """
    #  void QQuickControl::leftPaddingChanged()
    self.uglySide.call('ritual_ZN13QQuickControl18leftPaddingChangedEv')

  def rightPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::rightPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#rightPaddingChanged
    """
    #  void QQuickControl::rightPaddingChanged()
    self.uglySide.call('ritual_ZN13QQuickControl19rightPaddingChangedEv')

  def bottomPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::bottomPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#bottomPaddingChanged
    """
    #  void QQuickControl::bottomPaddingChanged()
    self.uglySide.call('ritual_ZN13QQuickControl20bottomPaddingChangedEv')

  def spacingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::spacingChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#spacingChanged
    """
    #  void QQuickControl::spacingChanged()
    self.uglySide.call('ritual_ZN13QQuickControl14spacingChangedEv')

  def localeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::localeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#localeChanged
    """
    #  void QQuickControl::localeChanged()
    self.uglySide.call('ritual_ZN13QQuickControl13localeChangedEv')

  def focusReasonChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::focusReasonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#focusReasonChanged
    """
    #  void QQuickControl::focusReasonChanged()
    self.uglySide.call('ritual_ZN13QQuickControl18focusReasonChangedEv')

  def mirroredChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::mirroredChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#mirroredChanged
    """
    #  void QQuickControl::mirroredChanged()
    self.uglySide.call('ritual_ZN13QQuickControl15mirroredChangedEv')

  def visualFocusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::visualFocusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#visualFocusChanged
    """
    #  void QQuickControl::visualFocusChanged()
    self.uglySide.call('ritual_ZN13QQuickControl18visualFocusChangedEv')

  def hoveredChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::hoveredChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#hoveredChanged
    """
    #  void QQuickControl::hoveredChanged()
    self.uglySide.call('ritual_ZN13QQuickControl14hoveredChangedEv')

  def hoverEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::hoverEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#hoverEnabledChanged
    """
    #  void QQuickControl::hoverEnabledChanged()
    self.uglySide.call('ritual_ZN13QQuickControl19hoverEnabledChangedEv')

  def wheelEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::wheelEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#wheelEnabledChanged
    """
    #  void QQuickControl::wheelEnabledChanged()
    self.uglySide.call('ritual_ZN13QQuickControl19wheelEnabledChangedEv')

  def backgroundChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::backgroundChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#backgroundChanged
    """
    #  void QQuickControl::backgroundChanged()
    self.uglySide.call('ritual_ZN13QQuickControl17backgroundChangedEv')

  def contentItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::contentItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#contentItemChanged
    """
    #  void QQuickControl::contentItemChanged()
    self.uglySide.call('ritual_ZN13QQuickControl18contentItemChangedEv')

  def baselineOffsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::baselineOffsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#baselineOffsetChanged
    """
    #  void QQuickControl::baselineOffsetChanged()
    self.uglySide.call('ritual_ZN13QQuickControl21baselineOffsetChangedEv')

  def horizontalPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::horizontalPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#horizontalPaddingChanged
    """
    #  void QQuickControl::horizontalPaddingChanged()
    self.uglySide.call(
        'ritual_ZN13QQuickControl24horizontalPaddingChangedEv',
    )

  def verticalPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::verticalPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#verticalPaddingChanged
    """
    #  void QQuickControl::verticalPaddingChanged()
    self.uglySide.call('ritual_ZN13QQuickControl22verticalPaddingChangedEv')

  def implicitContentWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::implicitContentWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#implicitContentWidthChanged
    """
    #  void QQuickControl::implicitContentWidthChanged()
    self.uglySide.call(
        'ritual_ZN13QQuickControl27implicitContentWidthChangedEv',
    )

  def implicitContentHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::implicitContentHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#implicitContentHeightChanged
    """
    #  void QQuickControl::implicitContentHeightChanged()
    self.uglySide.call(
        'ritual_ZN13QQuickControl28implicitContentHeightChangedEv',
    )

  def implicitBackgroundWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::implicitBackgroundWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#implicitBackgroundWidthChanged
    """
    #  void QQuickControl::implicitBackgroundWidthChanged()
    self.uglySide.call(
        'ritual_ZN13QQuickControl30implicitBackgroundWidthChangedEv',
    )

  def implicitBackgroundHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::implicitBackgroundHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#implicitBackgroundHeightChanged
    """
    #  void QQuickControl::implicitBackgroundHeightChanged()
    self.uglySide.call(
        'ritual_ZN13QQuickControl31implicitBackgroundHeightChangedEv',
    )

  def topInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::topInsetChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#topInsetChanged
    """
    #  void QQuickControl::topInsetChanged()
    self.uglySide.call('ritual_ZN13QQuickControl15topInsetChangedEv')

  def leftInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::leftInsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#leftInsetChanged
    """
    #  void QQuickControl::leftInsetChanged()
    self.uglySide.call('ritual_ZN13QQuickControl16leftInsetChangedEv')

  def rightInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::rightInsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#rightInsetChanged
    """
    #  void QQuickControl::rightInsetChanged()
    self.uglySide.call('ritual_ZN13QQuickControl17rightInsetChangedEv')

  def bottomInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickControl::bottomInsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#bottomInsetChanged
    """
    #  void QQuickControl::bottomInsetChanged()
    self.uglySide.call('ritual_ZN13QQuickControl18bottomInsetChangedEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickControl::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#classBegin
    """
    #  void QQuickControl::classBegin()
    ritual = 'ritual_ZN13QQuickControl10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickControl::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#componentComplete
    """
    #  void QQuickControl::componentComplete()
    ritual = 'ritual_ZN13QQuickControl17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickControl::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickControl::itemChange(ItemChange change, const ItemChangeData
    #      &value)
    ritual = (
        'ritual_ZN13QQuickControl10itemChangeEN10QQuickItem10ItemChangeERKN'
        'S0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QQuickControl10itemChangeEN10QQuickItem10ItemChan'
          'geERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickControl::focusInEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickControl::focusInEvent(QFocusEvent *event)
    ritual = 'ritual_ZN13QQuickControl12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl12focusInEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickControl::focusOutEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#focusOutEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickControl::focusOutEvent(QFocusEvent *event)
    ritual = 'ritual_ZN13QQuickControl13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl13focusOutEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickControl::hoverEnterEvent(QHoverEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickControl::hoverEnterEvent(QHoverEvent *event)
    ritual = 'ritual_ZN13QQuickControl15hoverEnterEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl15hoverEnterEventEP11QHoverEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickControl::hoverMoveEvent(QHoverEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickControl::hoverMoveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN13QQuickControl14hoverMoveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl14hoverMoveEventEP11QHoverEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickControl::hoverLeaveEvent(QHoverEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickControl::hoverLeaveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN13QQuickControl15hoverLeaveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl15hoverLeaveEventEP11QHoverEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickControl::mousePressEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickControl::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN13QQuickControl15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickControl::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickControl::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN13QQuickControl14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickControl::mouseReleaseEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickControl::mouseReleaseEvent(QMouseEvent *event)
    ritual = 'ritual_ZN13QQuickControl17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QQuickControl17mouseReleaseEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def mouseUngrabEvent(self) -> None:
    """
    Calls Qt's 'void QQuickControl::mouseUngrabEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#mouseUngrabEvent
    """
    #  void QQuickControl::mouseUngrabEvent()
    ritual = 'ritual_ZN13QQuickControl16mouseUngrabEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl16mouseUngrabEventEv'
    self.uglySide.call(ritual)

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QQuickControl::touchEvent(QTouchEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#touchEvent

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickControl::touchEvent(QTouchEvent *event)
    ritual = 'ritual_ZN13QQuickControl10touchEventEP11QTouchEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl10touchEventEP11QTouchEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def touchUngrabEvent(self) -> None:
    """
    Calls Qt's 'void QQuickControl::touchUngrabEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#touchUngrabEvent
    """
    #  void QQuickControl::touchUngrabEvent()
    ritual = 'ritual_ZN13QQuickControl16touchUngrabEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl16touchUngrabEventEv'
    self.uglySide.call(ritual)

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QQuickControl::wheelEvent(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickControl::wheelEvent(QWheelEvent *event)
    ritual = 'ritual_ZN13QQuickControl10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickControl::geometryChange(const QRectF &newGeometry,
    const QRectF &oldGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickControl::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN13QQuickControl14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QFont, QFont)
  def fontChange(self, newFont: QFont, oldFont: QFont) -> None:
    """
    Calls Qt's 'void QQuickControl::fontChange(const QFont &newFont, const
    QFont &oldFont)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#fontChange

    Parameters
    ----------

    newFont : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    oldFont : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickControl::fontChange(const QFont &newFont, const QFont
    #      &oldFont)
    ritual = 'ritual_ZN13QQuickControl10fontChangeERK5QFontS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl10fontChangeERK5QFontS2_'
    self.uglySide.call(
        ritual, self._valueOf(newFont), self._valueOf(oldFont),
    )

  def hoverChange(self) -> None:
    """
    Calls Qt's 'void QQuickControl::hoverChange()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#hoverChange
    """
    #  void QQuickControl::hoverChange()
    ritual = 'ritual_ZN13QQuickControl11hoverChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl11hoverChangeEv'
    self.uglySide.call(ritual)

  def mirrorChange(self) -> None:
    """
    Calls Qt's 'void QQuickControl::mirrorChange()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#mirrorChange
    """
    #  void QQuickControl::mirrorChange()
    ritual = 'ritual_ZN13QQuickControl12mirrorChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl12mirrorChangeEv'
    self.uglySide.call(ritual)

  @overload(float, float)
  def spacingChange(self, newSpacing: float, oldSpacing: float) -> None:
    """
    Calls Qt's 'void QQuickControl::spacingChange(qreal newSpacing, qreal
    oldSpacing)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#spacingChange

    Parameters
    ----------

    newSpacing : float
      Passed on as it is.

    oldSpacing : float
      Passed on as it is.
    """
    #  void QQuickControl::spacingChange(qreal newSpacing, qreal oldSpacing)
    ritual = 'ritual_ZN13QQuickControl13spacingChangeEdd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl13spacingChangeEdd'
    self.uglySide.call(ritual, newSpacing, oldSpacing)

  @overload(QMarginsF, QMarginsF)
  def paddingChange(
      self,
      newPadding: QMarginsF,
      oldPadding: QMarginsF,
  ) -> None:
    """
    Calls Qt's 'void QQuickControl::paddingChange(const QMarginsF
    &newPadding, const QMarginsF &oldPadding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#paddingChange

    Parameters
    ----------

    newPadding : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.

    oldPadding : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.
    """
    #  void QQuickControl::paddingChange(const QMarginsF &newPadding, const
    #      QMarginsF &oldPadding)
    ritual = 'ritual_ZN13QQuickControl13paddingChangeERK9QMarginsFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl13paddingChangeERK9QMarginsFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newPadding), self._valueOf(oldPadding),
    )

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def contentItemChange(
      self,
      newItem: Optional[QQuickItem],
      oldItem: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickControl::contentItemChange(QQuickItem *newItem,
    QQuickItem *oldItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#contentItemChange

    Parameters
    ----------

    newItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickControl::contentItemChange(QQuickItem *newItem, QQuickItem
    #      *oldItem)
    ritual = 'ritual_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QQuickControl17contentItemChangeEP10QQuickItemS1_')
    self.uglySide.call(
        ritual, self._addressOf(newItem), self._addressOf(oldItem),
    )

  @overload(QLocale, QLocale)
  def localeChange(self, newLocale: QLocale, oldLocale: QLocale) -> None:
    """
    Calls Qt's 'void QQuickControl::localeChange(const QLocale &newLocale,
    const QLocale &oldLocale)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#localeChange

    Parameters
    ----------

    newLocale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    oldLocale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QQuickControl::localeChange(const QLocale &newLocale, const
    #      QLocale &oldLocale)
    ritual = 'ritual_ZN13QQuickControl12localeChangeERK7QLocaleS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl12localeChangeERK7QLocaleS2_'
    self.uglySide.call(
        ritual, self._valueOf(newLocale), self._valueOf(oldLocale),
    )

  @overload(QMarginsF, QMarginsF)
  def insetChange(self, newInset: QMarginsF, oldInset: QMarginsF) -> None:
    """
    Calls Qt's 'void QQuickControl::insetChange(const QMarginsF &newInset,
    const QMarginsF &oldInset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#insetChange

    Parameters
    ----------

    newInset : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.

    oldInset : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.
    """
    #  void QQuickControl::insetChange(const QMarginsF &newInset, const
    #      QMarginsF &oldInset)
    ritual = 'ritual_ZN13QQuickControl11insetChangeERK9QMarginsFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl11insetChangeERK9QMarginsFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newInset), self._valueOf(oldInset),
    )

  def enabledChange(self) -> None:
    """
    Calls Qt's 'void QQuickControl::enabledChange()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#enabledChange
    """
    #  void QQuickControl::enabledChange()
    ritual = 'ritual_ZN13QQuickControl13enabledChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl13enabledChangeEv'
    self.uglySide.call(ritual)

  @overload(bool)
  def accessibilityActiveChanged(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickControl::accessibilityActiveChanged(bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#accessibilityActiveChanged

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickControl::accessibilityActiveChanged(bool active)
    ritual = 'ritual_ZN13QQuickControl26accessibilityActiveChangedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickControl26accessibilityActiveChangedEb'
    self.uglySide.call(ritual, active)

  @overload(str)
  def maybeSetAccessibleName(self, name: str) -> None:
    """
    Calls Qt's 'void QQuickControl::maybeSetAccessibleName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#maybeSetAccessibleName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickControl::maybeSetAccessibleName(const QString &name)
    self.uglySide.call(
        'ritual_ZN13QQuickControl22maybeSetAccessibleNameERK7QString', name,
    )

  @overload(str)
  @overload(NoneType)
  def accessibleProperty(self, propertyName: Optional[str]) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickControl::accessibleProperty(const char
    *propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontrol.html#accessibleProperty

    Parameters
    ----------

    propertyName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickControl::accessibleProperty(const char *propertyName)
    address = self.uglySide.call(
        'ritual_ZN13QQuickControl18accessiblePropertyEPKc',
        self._bytesOf(propertyName),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def d_func(self) -> Optional[QQuickControlPrivate]:
    """
    Calls Qt's 'QQuickControlPrivate *QQuickControl::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontrol.html#d_func

    Returns
    -------

    Optional[QQuickControlPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickControlPrivate *QQuickControl::d_func()
    address = self.uglySide.call('ritual_ZN13QQuickControl6d_funcEv')
    from . import QQuickControlPrivate
    return QQuickControlPrivate._cuteAt(address)
