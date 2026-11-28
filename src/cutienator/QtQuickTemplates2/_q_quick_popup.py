"""
QQuickPopup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopup_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickPopup to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject
from ..QtGui import QAccessible
from ..QtQml import QQmlParserStatus
from ..QtQuick import QQuickAttachedPropertyPropagatorTarget, QQuickItem
from ..QtQuick import QQuickSafeAreaAttachable, QtPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QLocale, QMarginsF, QMetaObject, QPointF
  from ..QtCore import QRectF, QSizeF, QVariant
  from ..QtGui import QDragEnterEvent, QDragLeaveEvent, QDragMoveEvent
  from ..QtGui import QDropEvent, QFocusEvent, QFont, QKeyEvent, QMouseEvent
  from ..QtGui import QTouchEvent, QWheelEvent
  from ..QtQuick import QQuickTransition, QQuickWindow
  from . import QQuickPopupPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDragEnterEvent = WAIT['QDragEnterEvent']
  QDragLeaveEvent = WAIT['QDragLeaveEvent']
  QDragMoveEvent = WAIT['QDragMoveEvent']
  QDropEvent = WAIT['QDropEvent']
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QFont = WAIT['QFont']
  QKeyEvent = WAIT['QKeyEvent']
  QLocale = WAIT['QLocale']
  QMarginsF = WAIT['QMarginsF']
  QMetaObject = WAIT['QMetaObject']
  QMouseEvent = WAIT['QMouseEvent']
  QPointF = WAIT['QPointF']
  QQuickTransition = WAIT['QQuickTransition']
  QQuickWindow = WAIT['QQuickWindow']
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']
  QTouchEvent = WAIT['QTouchEvent']
  QVariant = WAIT['QVariant']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPopup(QObject, QQmlParserStatus, QQuickSafeAreaAttachable, QQuickAttachedPropertyPropagatorTarget):
  """
  The cute side of Qt's QQuickPopup: a plain Python object standing in front
  of one C++ QQuickPopup.

  It is built on the cute 'QObject', as Qt's QQuickPopup is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QQuickPopup is built on Qt's
  QQmlParserStatus too, and has everything that class has. It is built on the
  cute 'QQuickSafeAreaAttachable' as well, as Qt's QQuickPopup is built on
  Qt's QQuickSafeAreaAttachable too, and has everything that class has. It is
  built on the cute 'QQuickAttachedPropertyPropagatorTarget' as well, as Qt's
  QQuickPopup is built on Qt's QQuickAttachedPropertyPropagatorTarget too,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPopup that has a ritual and that Python can
  call so far, 237 names in all: 'metaObject', 'tr', 'x', 'setX', 'y',
  'setY', 'position', 'setPosition', 'z', 'setZ', 'resetZ', 'width',
  'setWidth', 'resetWidth', 'height', 'setHeight', 'resetHeight',
  'implicitWidth', 'setImplicitWidth', 'implicitHeight', 'setImplicitHeight',
  'contentWidth', 'setContentWidth', 'contentHeight', 'setContentHeight',
  'availableWidth', 'availableHeight', 'margins', 'setMargins',
  'resetMargins', 'topMargin', 'setTopMargin', 'resetTopMargin',
  'leftMargin', 'setLeftMargin', 'resetLeftMargin', 'rightMargin',
  'setRightMargin', 'resetRightMargin', 'bottomMargin', 'setBottomMargin',
  'resetBottomMargin', 'padding', 'setPadding', 'resetPadding', 'topPadding',
  'setTopPadding', 'resetTopPadding', 'leftPadding', 'setLeftPadding',
  'resetLeftPadding', 'rightPadding', 'setRightPadding', 'resetRightPadding',
  'bottomPadding', 'setBottomPadding', 'resetBottomPadding', 'locale',
  'setLocale', 'resetLocale', 'font', 'setFont', 'resetFont', 'window',
  'popupItem', 'parentItem', 'setParentItem', 'resetParentItem',
  'background', 'setBackground', 'contentItem', 'setContentItem', 'clip',
  'setClip', 'hasFocus', 'setFocus', 'hasActiveFocus', 'isModal', 'setModal',
  'dim', 'setDim', 'resetDim', 'isVisible', 'setVisible', 'opacity',
  'setOpacity', 'scale', 'setScale', 'closePolicy', 'setClosePolicy',
  'resetClosePolicy', 'transformOrigin', 'setTransformOrigin', 'enter',
  'setEnter', 'exit', 'setExit', 'filtersChildMouseEvents',
  'setFiltersChildMouseEvents', 'forceActiveFocus', 'spacing', 'setSpacing',
  'resetSpacing', 'isOpened', 'isMirrored', 'isEnabled', 'setEnabled',
  'horizontalPadding', 'setHorizontalPadding', 'resetHorizontalPadding',
  'verticalPadding', 'setVerticalPadding', 'resetVerticalPadding',
  'implicitContentWidth', 'implicitContentHeight', 'implicitBackgroundWidth',
  'implicitBackgroundHeight', 'topInset', 'setTopInset', 'resetTopInset',
  'leftInset', 'setLeftInset', 'resetLeftInset', 'rightInset',
  'setRightInset', 'resetRightInset', 'bottomInset', 'setBottomInset',
  'resetBottomInset', 'popupType', 'setPopupType', 'open', 'close', 'opened',
  'closed', 'aboutToShow', 'aboutToHide', 'xChanged', 'yChanged', 'zChanged',
  'widthChanged', 'heightChanged', 'implicitWidthChanged',
  'implicitHeightChanged', 'contentWidthChanged', 'contentHeightChanged',
  'availableWidthChanged', 'availableHeightChanged', 'marginsChanged',
  'topMarginChanged', 'leftMarginChanged', 'rightMarginChanged',
  'bottomMarginChanged', 'paddingChanged', 'topPaddingChanged',
  'leftPaddingChanged', 'rightPaddingChanged', 'bottomPaddingChanged',
  'fontChanged', 'localeChanged', 'parentChanged', 'backgroundChanged',
  'contentItemChanged', 'contentChildrenChanged', 'clipChanged',
  'focusChanged', 'activeFocusChanged', 'modalChanged', 'dimChanged',
  'visibleChanged', 'opacityChanged', 'scaleChanged', 'closePolicyChanged',
  'enterChanged', 'exitChanged', 'windowChanged', 'spacingChanged',
  'openedChanged', 'mirroredChanged', 'enabledChanged', 'paletteChanged',
  'paletteCreated', 'horizontalPaddingChanged', 'verticalPaddingChanged',
  'implicitContentWidthChanged', 'implicitContentHeightChanged',
  'implicitBackgroundWidthChanged', 'implicitBackgroundHeightChanged',
  'topInsetChanged', 'leftInsetChanged', 'rightInsetChanged',
  'bottomInsetChanged', 'popupTypeChanged', 'classBegin',
  'componentComplete', 'isComponentComplete', 'childMouseEventFilter',
  'focusInEvent', 'focusOutEvent', 'keyPressEvent', 'keyReleaseEvent',
  'mousePressEvent', 'mouseMoveEvent', 'mouseReleaseEvent',
  'mouseDoubleClickEvent', 'mouseUngrabEvent', 'overlayEvent', 'touchEvent',
  'touchUngrabEvent', 'wheelEvent', 'dragEnterEvent', 'dragMoveEvent',
  'dragLeaveEvent', 'dropEvent', 'contentItemChange', 'contentSizeChange',
  'fontChange', 'geometryChange', 'localeChange', 'itemChange',
  'marginsChange', 'paddingChange', 'spacingChange', 'insetChange',
  'defaultFont', 'effectiveAccessibleRole', 'accessibleRole',
  'accessibilityActiveChanged', 'accessibleName', 'maybeSetAccessibleName',
  'accessibleProperty', 'setAccessibleProperty', 'findParentItem',
  'safeAreaAttachmentItem', 'attacheeItem', 'attachedParent', 'd_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPopup::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickPopup::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickPopup::~QQuickPopup()': the destructor: Python never removes
    a C++ QQuickPopup.
  - Qt's 'void QQuickPopup::setWindowModality(const Qt::WindowModality
    modality)': takes a type Python has no way to hand over yet.
  - Qt's 'QQuickPopup::QQuickPopup(QQuickPopupPrivate &dd, QObject *parent)':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickPopupPrivate *QQuickPopup::d_func() const': takes in
    Python what 'QQuickPopupPrivate *QQuickPopup::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 248 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickPopup is created at the first use, not by
    'QQuickPopup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPopup.
  - Qt tells when it has removed the C++ QQuickPopup. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QQuickPopup that has no cute function yet,
    'setWindowModality', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QQuickPopup, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ClosePolicyFlag(CuteFlags):
    """
    The flags enum 'QQuickPopup::ClosePolicyFlag' of Qt, with the 7 names Qt
    gives in it. Qt names the type of its combinations
    'QQuickPopup::ClosePolicy'.
    """

    NoAutoClose = 0x0
    CloseOnPressOutside = 0x1
    CloseOnPressOutsideParent = 0x2
    CloseOnReleaseOutside = 0x4
    CloseOnReleaseOutsideParent = 0x8
    CloseOnEscape = 0x10
    CloseMultiple = 0x20

  ClosePolicy = ClosePolicyFlag

  class PopupType(CuteNum):
    """
    The enum 'QQuickPopup::PopupType' of Qt, with the 3 names Qt gives in it.
    """

    Item = Kee[int](0)
    Window = Kee[int](1)
    Native = Kee[int](2)

  class TransformOrigin(CuteNum):
    """
    The enum 'QQuickPopup::TransformOrigin' of Qt, with the 9 names Qt gives
    in it.
    """

    TopLeft = Kee[int](0)
    Top = Kee[int](1)
    TopRight = Kee[int](2)
    Left = Kee[int](3)
    Center = Kee[int](4)
    Right = Kee[int](5)
    BottomLeft = Kee[int](6)
    Bottom = Kee[int](7)
    BottomRight = Kee[int](8)

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
    Calls Qt's 'QString QQuickPopup::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#tr

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
    #  QString QQuickPopup::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QQuickPopup2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPopup'

  #  Qt's QQuickPopup is built on more than one class. The part of a C++
  #  QQuickPopup that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQuickPopup_QQmlParserStatus',
      'QQuickSafeAreaAttachable':
          'ritual_cast_QQuickPopup_QQuickSafeAreaAttachable',
      'QQuickAttachedPropertyPropagatorTarget':
          'ritual_cast_QQuickPopup_QQuickAttachedPropertyPropagatorTarget',
  }

  #  A C++ QQuickPopup Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPopup'

  #  The functions Qt calls itself that QQuickPopup is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'isVisible': (
          ('_ZNK11QQuickPopup9isVisibleEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setVisible': (
          ('_ZN11QQuickPopup10setVisibleEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setOpacity': (
          ('_ZN11QQuickPopup10setOpacityEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'childMouseEventFilter': (
          ('_ZN11QQuickPopup21childMouseEventFilterEP10QQuickItemP6QEvent',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'focusInEvent': (
          ('_ZN11QQuickPopup12focusInEventEP11QFocusEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QFocusEvent'),
           )),
      ),
      'focusOutEvent': (
          ('_ZN11QQuickPopup13focusOutEventEP11QFocusEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QFocusEvent'),
           )),
      ),
      'keyPressEvent': (
          ('_ZN11QQuickPopup13keyPressEventEP9QKeyEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QKeyEvent'),
           )),
      ),
      'keyReleaseEvent': (
          ('_ZN11QQuickPopup15keyReleaseEventEP9QKeyEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QKeyEvent'),
           )),
      ),
      'mousePressEvent': (
          ('_ZN11QQuickPopup15mousePressEventEP11QMouseEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
           )),
      ),
      'mouseMoveEvent': (
          ('_ZN11QQuickPopup14mouseMoveEventEP11QMouseEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
           )),
      ),
      'mouseReleaseEvent': (
          ('_ZN11QQuickPopup17mouseReleaseEventEP11QMouseEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
           )),
      ),
      'mouseDoubleClickEvent': (
          ('_ZN11QQuickPopup21mouseDoubleClickEventEP11QMouseEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
           )),
      ),
      'mouseUngrabEvent': (
          ('_ZN11QQuickPopup16mouseUngrabEventEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'overlayEvent': (
          ('_ZN11QQuickPopup12overlayEventEP10QQuickItemP6QEvent',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'touchEvent': (
          ('_ZN11QQuickPopup10touchEventEP11QTouchEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QTouchEvent'),
           )),
      ),
      'touchUngrabEvent': (
          ('_ZN11QQuickPopup16touchUngrabEventEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'wheelEvent': (
          ('_ZN11QQuickPopup10wheelEventEP11QWheelEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QWheelEvent'),
           )),
      ),
      'dragEnterEvent': (
          ('_ZN11QQuickPopup14dragEnterEventEP15QDragEnterEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QDragEnterEvent'),
           )),
      ),
      'dragMoveEvent': (
          ('_ZN11QQuickPopup13dragMoveEventEP14QDragMoveEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QDragMoveEvent'),
           )),
      ),
      'dragLeaveEvent': (
          ('_ZN11QQuickPopup14dragLeaveEventEP15QDragLeaveEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QDragLeaveEvent'),
           )),
      ),
      'dropEvent': (
          ('_ZN11QQuickPopup9dropEventEP10QDropEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QDropEvent'),
           )),
      ),
      'contentItemChange': (
          ('_ZN11QQuickPopup17contentItemChangeEP10QQuickItemS1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'contentSizeChange': (
          ('_ZN11QQuickPopup17contentSizeChangeERK6QSizeFS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QSizeF'),
               ('address', 'value', 'QtCore:QSizeF'),
           )),
      ),
      'fontChange': (
          ('_ZN11QQuickPopup10fontChangeERK5QFontS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QFont'),
               ('address', 'value', 'QtGui:QFont'),
           )),
      ),
      'geometryChange': (
          ('_ZN11QQuickPopup14geometryChangeERK6QRectFS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'localeChange': (
          ('_ZN11QQuickPopup12localeChangeERK7QLocaleS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QLocale'),
               ('address', 'value', 'QtCore:QLocale'),
           )),
      ),
      'itemChange': (
          ('_ZN11QQuickPopup10itemChangeEN10QQuickItem10ItemChangeERKNS0_14'
           'ItemChangeDataE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQuick:QQuickItem.ItemChange'),
               ('address', 'value', 'QtQuick:QQuickItem.ItemChangeData'),
           )),
      ),
      'marginsChange': (
          ('_ZN11QQuickPopup13marginsChangeERK9QMarginsFS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QMarginsF'),
               ('address', 'value', 'QtCore:QMarginsF'),
           )),
      ),
      'paddingChange': (
          ('_ZN11QQuickPopup13paddingChangeERK9QMarginsFS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QMarginsF'),
               ('address', 'value', 'QtCore:QMarginsF'),
           )),
      ),
      'spacingChange': (
          ('_ZN11QQuickPopup13spacingChangeEdd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
               ('double', 'number', ''),
           )),
      ),
      'insetChange': (
          ('_ZN11QQuickPopup11insetChangeERK9QMarginsFS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QMarginsF'),
               ('address', 'value', 'QtCore:QMarginsF'),
           )),
      ),
      'defaultFont': (
          ('_ZNK11QQuickPopup11defaultFontEv',
           ('address', 'value', 'QtGui:QFont'),
           ()),
      ),
      'accessibleRole': (
          ('_ZNK11QQuickPopup14accessibleRoleEv',
           ('int', 'enum', 'QtGui:QAccessible.Role'),
           ()),
      ),
      'accessibilityActiveChanged': (
          ('_ZN11QQuickPopup26accessibilityActiveChangedEb',
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
    Calls Qt's 'const QMetaObject *QQuickPopup::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPopup::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QQuickPopup10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def x(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#x
    """
    #  qreal QQuickPopup::x() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#y
    """
    #  qreal QQuickPopup::y() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup1yEv')

  def position(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickPopup::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#position

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickPopup::position() const
    address = self.uglySide.call('ritual_ZNK11QQuickPopup8positionEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def z(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::z() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#z
    """
    #  qreal QQuickPopup::z() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup1zEv')

  def width(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#width
    """
    #  qreal QQuickPopup::width() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup5widthEv')

  def height(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#height
    """
    #  qreal QQuickPopup::height() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup6heightEv')

  def implicitWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::implicitWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#implicitWidth
    """
    #  qreal QQuickPopup::implicitWidth() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup13implicitWidthEv')

  def implicitHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::implicitHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#implicitHeight
    """
    #  qreal QQuickPopup::implicitHeight() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup14implicitHeightEv')

  def contentWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::contentWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#contentWidth
    """
    #  qreal QQuickPopup::contentWidth() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup12contentWidthEv')

  def contentHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::contentHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#contentHeight
    """
    #  qreal QQuickPopup::contentHeight() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup13contentHeightEv')

  def availableWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::availableWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#availableWidth
    """
    #  qreal QQuickPopup::availableWidth() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup14availableWidthEv')

  def availableHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::availableHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#availableHeight
    """
    #  qreal QQuickPopup::availableHeight() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup15availableHeightEv')

  def margins(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::margins() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#margins
    """
    #  qreal QQuickPopup::margins() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup7marginsEv')

  def topMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::topMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#topMargin
    """
    #  qreal QQuickPopup::topMargin() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup9topMarginEv')

  def leftMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::leftMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#leftMargin
    """
    #  qreal QQuickPopup::leftMargin() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup10leftMarginEv')

  def rightMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::rightMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#rightMargin
    """
    #  qreal QQuickPopup::rightMargin() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup11rightMarginEv')

  def bottomMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::bottomMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#bottomMargin
    """
    #  qreal QQuickPopup::bottomMargin() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup12bottomMarginEv')

  def padding(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::padding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#padding
    """
    #  qreal QQuickPopup::padding() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup7paddingEv')

  def topPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::topPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#topPadding
    """
    #  qreal QQuickPopup::topPadding() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup10topPaddingEv')

  def leftPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::leftPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#leftPadding
    """
    #  qreal QQuickPopup::leftPadding() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup11leftPaddingEv')

  def rightPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::rightPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#rightPadding
    """
    #  qreal QQuickPopup::rightPadding() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup12rightPaddingEv')

  def bottomPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::bottomPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#bottomPadding
    """
    #  qreal QQuickPopup::bottomPadding() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup13bottomPaddingEv')

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QQuickPopup::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QQuickPopup::locale() const
    address = self.uglySide.call('ritual_ZNK11QQuickPopup6localeEv')
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickPopup::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickPopup::font() const
    address = self.uglySide.call('ritual_ZNK11QQuickPopup4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def window(self) -> Optional[QQuickWindow]:
    """
    Calls Qt's 'QQuickWindow *QQuickPopup::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#window

    Returns
    -------

    Optional[QQuickWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWindow *QQuickPopup::window() const
    address = self.uglySide.call('ritual_ZNK11QQuickPopup6windowEv')
    from ..QtQuick import QQuickWindow
    return QQuickWindow._cuteAt(address)

  def popupItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPopup::popupItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#popupItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPopup::popupItem() const
    address = self.uglySide.call('ritual_ZNK11QQuickPopup9popupItemEv')
    return QQuickItem._cuteAt(address)

  def parentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPopup::parentItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#parentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPopup::parentItem() const
    address = self.uglySide.call('ritual_ZNK11QQuickPopup10parentItemEv')
    return QQuickItem._cuteAt(address)

  def background(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPopup::background() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#background

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPopup::background() const
    address = self.uglySide.call('ritual_ZNK11QQuickPopup10backgroundEv')
    return QQuickItem._cuteAt(address)

  def contentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPopup::contentItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#contentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPopup::contentItem() const
    address = self.uglySide.call('ritual_ZNK11QQuickPopup11contentItemEv')
    return QQuickItem._cuteAt(address)

  def clip(self) -> bool:
    """
    Calls Qt's 'bool QQuickPopup::clip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#clip
    """
    #  bool QQuickPopup::clip() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup4clipEv')

  def hasFocus(self) -> bool:
    """
    Calls Qt's 'bool QQuickPopup::hasFocus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#hasFocus
    """
    #  bool QQuickPopup::hasFocus() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup8hasFocusEv')

  def hasActiveFocus(self) -> bool:
    """
    Calls Qt's 'bool QQuickPopup::hasActiveFocus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#hasActiveFocus
    """
    #  bool QQuickPopup::hasActiveFocus() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup14hasActiveFocusEv')

  def isModal(self) -> bool:
    """
    Calls Qt's 'bool QQuickPopup::isModal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#isModal
    """
    #  bool QQuickPopup::isModal() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup7isModalEv')

  def dim(self) -> bool:
    """
    Calls Qt's 'bool QQuickPopup::dim() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#dim
    """
    #  bool QQuickPopup::dim() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup3dimEv')

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QQuickPopup::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#isVisible
    """
    #  bool QQuickPopup::isVisible() const
    ritual = 'ritual_ZNK11QQuickPopup9isVisibleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QQuickPopup9isVisibleEv'
    return self.uglySide.call(ritual)

  def opacity(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::opacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#opacity
    """
    #  qreal QQuickPopup::opacity() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup7opacityEv')

  def scale(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::scale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#scale
    """
    #  qreal QQuickPopup::scale() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup5scaleEv')

  def closePolicy(self) -> ClosePolicy:
    """
    Calls Qt's 'ClosePolicy QQuickPopup::closePolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#closePolicy

    Returns
    -------

    ClosePolicy
      The value standing for the combination Qt gave back.
    """
    #  ClosePolicy QQuickPopup::closePolicy() const
    return QQuickPopup.ClosePolicy(self.uglySide.call(
        'ritual_ZNK11QQuickPopup11closePolicyEv',
    ))

  def transformOrigin(self) -> TransformOrigin:
    """
    Calls Qt's 'TransformOrigin QQuickPopup::transformOrigin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#transformOrigin

    Returns
    -------

    TransformOrigin
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TransformOrigin(number)'
      gives.
    """
    #  TransformOrigin QQuickPopup::transformOrigin() const
    return QQuickPopup.TransformOrigin(self.uglySide.call(
        'ritual_ZNK11QQuickPopup15transformOriginEv',
    ))

  def enter(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQuickPopup::enter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#enter

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickPopup::enter() const
    address = self.uglySide.call('ritual_ZNK11QQuickPopup5enterEv')
    from ..QtQuick import QQuickTransition
    return QQuickTransition._cuteAt(address)

  def exit(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQuickPopup::exit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#exit

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickPopup::exit() const
    address = self.uglySide.call('ritual_ZNK11QQuickPopup4exitEv')
    from ..QtQuick import QQuickTransition
    return QQuickTransition._cuteAt(address)

  def filtersChildMouseEvents(self) -> bool:
    """
    Calls Qt's 'bool QQuickPopup::filtersChildMouseEvents() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#filtersChildMouseEvents
    """
    #  bool QQuickPopup::filtersChildMouseEvents() const
    return self.uglySide.call(
        'ritual_ZNK11QQuickPopup23filtersChildMouseEventsEv',
    )

  def spacing(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::spacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#spacing
    """
    #  qreal QQuickPopup::spacing() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup7spacingEv')

  def isOpened(self) -> bool:
    """
    Calls Qt's 'bool QQuickPopup::isOpened() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#isOpened
    """
    #  bool QQuickPopup::isOpened() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup8isOpenedEv')

  def isMirrored(self) -> bool:
    """
    Calls Qt's 'bool QQuickPopup::isMirrored() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#isMirrored
    """
    #  bool QQuickPopup::isMirrored() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup10isMirroredEv')

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickPopup::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#isEnabled
    """
    #  bool QQuickPopup::isEnabled() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup9isEnabledEv')

  def horizontalPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::horizontalPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#horizontalPadding
    """
    #  qreal QQuickPopup::horizontalPadding() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup17horizontalPaddingEv')

  def verticalPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::verticalPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#verticalPadding
    """
    #  qreal QQuickPopup::verticalPadding() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup15verticalPaddingEv')

  def implicitContentWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::implicitContentWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#implicitContentWidth
    """
    #  qreal QQuickPopup::implicitContentWidth() const
    return self.uglySide.call(
        'ritual_ZNK11QQuickPopup20implicitContentWidthEv',
    )

  def implicitContentHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::implicitContentHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#implicitContentHeight
    """
    #  qreal QQuickPopup::implicitContentHeight() const
    return self.uglySide.call(
        'ritual_ZNK11QQuickPopup21implicitContentHeightEv',
    )

  def implicitBackgroundWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::implicitBackgroundWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#implicitBackgroundWidth
    """
    #  qreal QQuickPopup::implicitBackgroundWidth() const
    return self.uglySide.call(
        'ritual_ZNK11QQuickPopup23implicitBackgroundWidthEv',
    )

  def implicitBackgroundHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::implicitBackgroundHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#implicitBackgroundHeight
    """
    #  qreal QQuickPopup::implicitBackgroundHeight() const
    return self.uglySide.call(
        'ritual_ZNK11QQuickPopup24implicitBackgroundHeightEv',
    )

  def topInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::topInset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#topInset
    """
    #  qreal QQuickPopup::topInset() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup8topInsetEv')

  def leftInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::leftInset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#leftInset
    """
    #  qreal QQuickPopup::leftInset() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup9leftInsetEv')

  def rightInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::rightInset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#rightInset
    """
    #  qreal QQuickPopup::rightInset() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup10rightInsetEv')

  def bottomInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickPopup::bottomInset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#bottomInset
    """
    #  qreal QQuickPopup::bottomInset() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup11bottomInsetEv')

  def popupType(self) -> PopupType:
    """
    Calls Qt's 'PopupType QQuickPopup::popupType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#popupType

    Returns
    -------

    PopupType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PopupType(number)' gives.
    """
    #  PopupType QQuickPopup::popupType() const
    return QQuickPopup.PopupType(self.uglySide.call(
        'ritual_ZNK11QQuickPopup9popupTypeEv',
    ))

  def isComponentComplete(self) -> bool:
    """
    Calls Qt's 'bool QQuickPopup::isComponentComplete() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#isComponentComplete
    """
    #  bool QQuickPopup::isComponentComplete() const
    return self.uglySide.call(
        'ritual_ZNK11QQuickPopup19isComponentCompleteEv',
    )

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickPopup::defaultFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickPopup::defaultFont() const
    ritual = 'ritual_ZNK11QQuickPopup11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QQuickPopup11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def effectiveAccessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickPopup::effectiveAccessibleRole()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#effectiveAccessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickPopup::effectiveAccessibleRole() const
    return QAccessible.Role(self.uglySide.call(
        'ritual_ZNK11QQuickPopup23effectiveAccessibleRoleEv',
    ))

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickPopup::accessibleRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickPopup::accessibleRole() const
    ritual = 'ritual_ZNK11QQuickPopup14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QQuickPopup14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  def accessibleName(self) -> str:
    """
    Calls Qt's 'QString QQuickPopup::accessibleName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#accessibleName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickPopup::accessibleName() const
    return self.uglySide.call('ritual_ZNK11QQuickPopup14accessibleNameEv')

  def findParentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPopup::findParentItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#findParentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPopup::findParentItem() const
    address = self.uglySide.call('ritual_ZNK11QQuickPopup14findParentItemEv')
    return QQuickItem._cuteAt(address)

  def attacheeItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPopup::attacheeItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#attacheeItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPopup::attacheeItem() const
    ritual = 'ritual_ZNK11QQuickPopup12attacheeItemEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QQuickPopup12attacheeItemEv'
    address = self.uglySide.call(ritual)
    return QQuickItem._cuteAt(address)

  @overload(QMetaObject)
  @overload(NoneType)
  def attachedParent(
      self,
      attachedType: Optional[QMetaObject],
  ) -> Optional[QtPrivate.QQuickAttachedPropertyPropagator]:
    """
    Calls Qt's 'QtPrivate::QQuickAttachedPropertyPropagator
    *QQuickPopup::attachedParent(const QMetaObject *attachedType) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#attachedParent

    Parameters
    ----------

    attachedType : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QtPrivate.QQuickAttachedPropertyPropagator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtPrivate::QQuickAttachedPropertyPropagator
    #      *QQuickPopup::attachedParent(const QMetaObject *attachedType)
    #      const
    ritual = 'ritual_ZNK11QQuickPopup14attachedParentEPK11QMetaObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QQuickPopup14attachedParentEPK11QMetaObject'
    address = self.uglySide.call(
        ritual, self._addressOf(attachedType, 'QMetaObject'),
    )
    return QtPrivate.QQuickAttachedPropertyPropagator._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, x: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setX(qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QQuickPopup::setX(qreal x)
    self.uglySide.call('ritual_ZN11QQuickPopup4setXEd', x)

  @overload(float)
  def setY(self, y: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setY(qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QQuickPopup::setY(qreal y)
    self.uglySide.call('ritual_ZN11QQuickPopup4setYEd', y)

  @overload(QPointF)
  def setPosition(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QQuickPopup::setPosition(const QPointF &pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setPosition

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickPopup::setPosition(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN11QQuickPopup11setPositionERK7QPointF',
        self._valueOf(pos, 'QPointF'),
    )

  @overload(float)
  def setZ(self, z: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setZ(qreal z)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setZ

    Parameters
    ----------

    z : float
      Passed on as it is.
    """
    #  void QQuickPopup::setZ(qreal z)
    self.uglySide.call('ritual_ZN11QQuickPopup4setZEd', z)

  @overload(float)
  def setWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setWidth(qreal width)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuickPopup::setWidth(qreal width)
    self.uglySide.call('ritual_ZN11QQuickPopup8setWidthEd', width)

  @overload(float)
  def setHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setHeight(qreal height)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QQuickPopup::setHeight(qreal height)
    self.uglySide.call('ritual_ZN11QQuickPopup9setHeightEd', height)

  @overload(float)
  def setImplicitWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setImplicitWidth(qreal width)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setImplicitWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuickPopup::setImplicitWidth(qreal width)
    self.uglySide.call('ritual_ZN11QQuickPopup16setImplicitWidthEd', width)

  @overload(float)
  def setImplicitHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setImplicitHeight(qreal height)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setImplicitHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QQuickPopup::setImplicitHeight(qreal height)
    self.uglySide.call('ritual_ZN11QQuickPopup17setImplicitHeightEd', height)

  @overload(float)
  def setContentWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setContentWidth(qreal width)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setContentWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuickPopup::setContentWidth(qreal width)
    self.uglySide.call('ritual_ZN11QQuickPopup15setContentWidthEd', width)

  @overload(float)
  def setContentHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setContentHeight(qreal height)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setContentHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QQuickPopup::setContentHeight(qreal height)
    self.uglySide.call('ritual_ZN11QQuickPopup16setContentHeightEd', height)

  @overload(float)
  def setMargins(self, margins: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setMargins(qreal margins)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setMargins

    Parameters
    ----------

    margins : float
      Passed on as it is.
    """
    #  void QQuickPopup::setMargins(qreal margins)
    self.uglySide.call('ritual_ZN11QQuickPopup10setMarginsEd', margins)

  @overload(float)
  def setTopMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setTopMargin(qreal margin)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setTopMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QQuickPopup::setTopMargin(qreal margin)
    self.uglySide.call('ritual_ZN11QQuickPopup12setTopMarginEd', margin)

  @overload(float)
  def setLeftMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setLeftMargin(qreal margin)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setLeftMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QQuickPopup::setLeftMargin(qreal margin)
    self.uglySide.call('ritual_ZN11QQuickPopup13setLeftMarginEd', margin)

  @overload(float)
  def setRightMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setRightMargin(qreal margin)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setRightMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QQuickPopup::setRightMargin(qreal margin)
    self.uglySide.call('ritual_ZN11QQuickPopup14setRightMarginEd', margin)

  @overload(float)
  def setBottomMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setBottomMargin(qreal margin)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setBottomMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QQuickPopup::setBottomMargin(qreal margin)
    self.uglySide.call('ritual_ZN11QQuickPopup15setBottomMarginEd', margin)

  @overload(float)
  def setPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setPadding(qreal padding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickPopup::setPadding(qreal padding)
    self.uglySide.call('ritual_ZN11QQuickPopup10setPaddingEd', padding)

  @overload(float)
  def setTopPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setTopPadding(qreal padding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setTopPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickPopup::setTopPadding(qreal padding)
    self.uglySide.call('ritual_ZN11QQuickPopup13setTopPaddingEd', padding)

  @overload(float)
  def setLeftPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setLeftPadding(qreal padding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setLeftPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickPopup::setLeftPadding(qreal padding)
    self.uglySide.call('ritual_ZN11QQuickPopup14setLeftPaddingEd', padding)

  @overload(float)
  def setRightPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setRightPadding(qreal padding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setRightPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickPopup::setRightPadding(qreal padding)
    self.uglySide.call('ritual_ZN11QQuickPopup15setRightPaddingEd', padding)

  @overload(float)
  def setBottomPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setBottomPadding(qreal padding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setBottomPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickPopup::setBottomPadding(qreal padding)
    self.uglySide.call('ritual_ZN11QQuickPopup16setBottomPaddingEd', padding)

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QQuickPopup::setLocale(const QLocale &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QQuickPopup::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN11QQuickPopup9setLocaleERK7QLocale', self._valueOf(locale),
    )

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickPopup::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickPopup::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN11QQuickPopup7setFontERK5QFont', self._valueOf(font),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setParentItem(self, parent: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickPopup::setParentItem(QQuickItem *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setParentItem

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopup::setParentItem(QQuickItem *parent)
    self.uglySide.call(
        'ritual_ZN11QQuickPopup13setParentItemEP10QQuickItem',
        self._addressOf(parent),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setBackground(self, background: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickPopup::setBackground(QQuickItem *background)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setBackground

    Parameters
    ----------

    background : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopup::setBackground(QQuickItem *background)
    self.uglySide.call(
        'ritual_ZN11QQuickPopup13setBackgroundEP10QQuickItem',
        self._addressOf(background),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setContentItem(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickPopup::setContentItem(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setContentItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopup::setContentItem(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN11QQuickPopup14setContentItemEP10QQuickItem',
        self._addressOf(item),
    )

  @overload(bool)
  def setClip(self, clip: bool) -> None:
    """
    Calls Qt's 'void QQuickPopup::setClip(bool clip)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setClip

    Parameters
    ----------

    clip : bool
      Passed on as it is.
    """
    #  void QQuickPopup::setClip(bool clip)
    self.uglySide.call('ritual_ZN11QQuickPopup7setClipEb', clip)

  @overload(bool)
  def setFocus(self, focus: bool) -> None:
    """
    Calls Qt's 'void QQuickPopup::setFocus(bool focus)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setFocus

    Parameters
    ----------

    focus : bool
      Passed on as it is.
    """
    #  void QQuickPopup::setFocus(bool focus)
    self.uglySide.call('ritual_ZN11QQuickPopup8setFocusEb', focus)

  @overload(bool)
  def setModal(self, modal: bool) -> None:
    """
    Calls Qt's 'void QQuickPopup::setModal(bool modal)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setModal

    Parameters
    ----------

    modal : bool
      Passed on as it is.
    """
    #  void QQuickPopup::setModal(bool modal)
    self.uglySide.call('ritual_ZN11QQuickPopup8setModalEb', modal)

  @overload(bool)
  def setDim(self, dim: bool) -> None:
    """
    Calls Qt's 'void QQuickPopup::setDim(bool dim)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setDim

    Parameters
    ----------

    dim : bool
      Passed on as it is.
    """
    #  void QQuickPopup::setDim(bool dim)
    self.uglySide.call('ritual_ZN11QQuickPopup6setDimEb', dim)

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QQuickPopup::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QQuickPopup::setVisible(bool visible)
    ritual = 'ritual_ZN11QQuickPopup10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup10setVisibleEb'
    self.uglySide.call(ritual, visible)

  @overload(float)
  def setOpacity(self, opacity: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setOpacity(qreal opacity)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setOpacity

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QQuickPopup::setOpacity(qreal opacity)
    ritual = 'ritual_ZN11QQuickPopup10setOpacityEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup10setOpacityEd'
    self.uglySide.call(ritual, opacity)

  @overload(float)
  def setScale(self, scale: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setScale(qreal scale)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setScale

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void QQuickPopup::setScale(qreal scale)
    self.uglySide.call('ritual_ZN11QQuickPopup8setScaleEd', scale)

  @overload(ClosePolicy)
  def setClosePolicy(self, policy: ClosePolicy) -> None:
    """
    Calls Qt's 'void QQuickPopup::setClosePolicy(ClosePolicy policy)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setClosePolicy

    Parameters
    ----------

    policy : ClosePolicy
      Passed on as its number.
    """
    #  void QQuickPopup::setClosePolicy(ClosePolicy policy)
    self.uglySide.call(
        'ritual_ZN11QQuickPopup14setClosePolicyE6QFlagsINS_15ClosePolicyFla'
        'gEE',
        policy.value,
    )

  @overload(TransformOrigin)
  def setTransformOrigin(self, a0: TransformOrigin) -> None:
    """
    Calls Qt's 'void QQuickPopup::setTransformOrigin(TransformOrigin a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#setTransformOrigin

    Parameters
    ----------

    a0 : TransformOrigin
      Passed on as its number.
    """
    #  void QQuickPopup::setTransformOrigin(TransformOrigin a0)
    self.uglySide.call(
        'ritual_ZN11QQuickPopup18setTransformOriginENS_15TransformOriginE',
        a0.value,
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def setEnter(self, transition: Optional[QQuickTransition]) -> None:
    """
    Calls Qt's 'void QQuickPopup::setEnter(QQuickTransition *transition)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setEnter

    Parameters
    ----------

    transition : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopup::setEnter(QQuickTransition *transition)
    self.uglySide.call(
        'ritual_ZN11QQuickPopup8setEnterEP16QQuickTransition',
        self._addressOf(transition),
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def setExit(self, transition: Optional[QQuickTransition]) -> None:
    """
    Calls Qt's 'void QQuickPopup::setExit(QQuickTransition *transition)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setExit

    Parameters
    ----------

    transition : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopup::setExit(QQuickTransition *transition)
    self.uglySide.call(
        'ritual_ZN11QQuickPopup7setExitEP16QQuickTransition',
        self._addressOf(transition),
    )

  @overload(bool)
  def setFiltersChildMouseEvents(self, filter: bool) -> None:
    """
    Calls Qt's 'void QQuickPopup::setFiltersChildMouseEvents(bool filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#setFiltersChildMouseEvents

    Parameters
    ----------

    filter : bool
      Passed on as it is.
    """
    #  void QQuickPopup::setFiltersChildMouseEvents(bool filter)
    self.uglySide.call(
        'ritual_ZN11QQuickPopup26setFiltersChildMouseEventsEb', filter,
    )

  @overload(float)
  def setSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setSpacing(qreal spacing)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QQuickPopup::setSpacing(qreal spacing)
    self.uglySide.call('ritual_ZN11QQuickPopup10setSpacingEd', spacing)

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickPopup::setEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickPopup::setEnabled(bool enabled)
    self.uglySide.call('ritual_ZN11QQuickPopup10setEnabledEb', enabled)

  @overload(float)
  def setHorizontalPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setHorizontalPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#setHorizontalPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickPopup::setHorizontalPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN11QQuickPopup20setHorizontalPaddingEd', padding,
    )

  @overload(float)
  def setVerticalPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setVerticalPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#setVerticalPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickPopup::setVerticalPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN11QQuickPopup18setVerticalPaddingEd', padding,
    )

  @overload(float)
  def setTopInset(self, inset: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setTopInset(qreal inset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setTopInset

    Parameters
    ----------

    inset : float
      Passed on as it is.
    """
    #  void QQuickPopup::setTopInset(qreal inset)
    self.uglySide.call('ritual_ZN11QQuickPopup11setTopInsetEd', inset)

  @overload(float)
  def setLeftInset(self, inset: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setLeftInset(qreal inset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setLeftInset

    Parameters
    ----------

    inset : float
      Passed on as it is.
    """
    #  void QQuickPopup::setLeftInset(qreal inset)
    self.uglySide.call('ritual_ZN11QQuickPopup12setLeftInsetEd', inset)

  @overload(float)
  def setRightInset(self, inset: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setRightInset(qreal inset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setRightInset

    Parameters
    ----------

    inset : float
      Passed on as it is.
    """
    #  void QQuickPopup::setRightInset(qreal inset)
    self.uglySide.call('ritual_ZN11QQuickPopup13setRightInsetEd', inset)

  @overload(float)
  def setBottomInset(self, inset: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::setBottomInset(qreal inset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setBottomInset

    Parameters
    ----------

    inset : float
      Passed on as it is.
    """
    #  void QQuickPopup::setBottomInset(qreal inset)
    self.uglySide.call('ritual_ZN11QQuickPopup14setBottomInsetEd', inset)

  @overload(PopupType)
  def setPopupType(self, a0: PopupType) -> None:
    """
    Calls Qt's 'void QQuickPopup::setPopupType(PopupType a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#setPopupType

    Parameters
    ----------

    a0 : PopupType
      Passed on as its number.
    """
    #  void QQuickPopup::setPopupType(PopupType a0)
    self.uglySide.call(
        'ritual_ZN11QQuickPopup12setPopupTypeENS_9PopupTypeE', a0.value,
    )

  @overload(str, QVariant)
  @overload(NoneType, QVariant)
  def setAccessibleProperty(
      self,
      propertyName: Optional[str],
      value: QVariant,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickPopup::setAccessibleProperty(const char
    *propertyName, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#setAccessibleProperty

    Parameters
    ----------

    propertyName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QQuickPopup::setAccessibleProperty(const char *propertyName,
    #      const QVariant &value)
    return self.uglySide.call(
        'ritual_ZN11QQuickPopup21setAccessiblePropertyEPKcRK8QVariant',
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickPopup::QQuickPopup(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#QQuickPopup

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPopup::QQuickPopup(QObject *parent)
    self._noteCreation(QQuickPopup, lambda: Rituals.call(
        'ritual_ZN11QQuickPopupC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def resetZ(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetZ()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#resetZ
    """
    #  void QQuickPopup::resetZ()
    self.uglySide.call('ritual_ZN11QQuickPopup6resetZEv')

  def resetWidth(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetWidth()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#resetWidth
    """
    #  void QQuickPopup::resetWidth()
    self.uglySide.call('ritual_ZN11QQuickPopup10resetWidthEv')

  def resetHeight(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetHeight()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#resetHeight
    """
    #  void QQuickPopup::resetHeight()
    self.uglySide.call('ritual_ZN11QQuickPopup11resetHeightEv')

  def resetMargins(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetMargins()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#resetMargins
    """
    #  void QQuickPopup::resetMargins()
    self.uglySide.call('ritual_ZN11QQuickPopup12resetMarginsEv')

  def resetTopMargin(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetTopMargin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#resetTopMargin
    """
    #  void QQuickPopup::resetTopMargin()
    self.uglySide.call('ritual_ZN11QQuickPopup14resetTopMarginEv')

  def resetLeftMargin(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetLeftMargin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#resetLeftMargin
    """
    #  void QQuickPopup::resetLeftMargin()
    self.uglySide.call('ritual_ZN11QQuickPopup15resetLeftMarginEv')

  def resetRightMargin(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetRightMargin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#resetRightMargin
    """
    #  void QQuickPopup::resetRightMargin()
    self.uglySide.call('ritual_ZN11QQuickPopup16resetRightMarginEv')

  def resetBottomMargin(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetBottomMargin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#resetBottomMargin
    """
    #  void QQuickPopup::resetBottomMargin()
    self.uglySide.call('ritual_ZN11QQuickPopup17resetBottomMarginEv')

  def resetPadding(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetPadding()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#resetPadding
    """
    #  void QQuickPopup::resetPadding()
    self.uglySide.call('ritual_ZN11QQuickPopup12resetPaddingEv')

  def resetTopPadding(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetTopPadding()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#resetTopPadding
    """
    #  void QQuickPopup::resetTopPadding()
    self.uglySide.call('ritual_ZN11QQuickPopup15resetTopPaddingEv')

  def resetLeftPadding(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetLeftPadding()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#resetLeftPadding
    """
    #  void QQuickPopup::resetLeftPadding()
    self.uglySide.call('ritual_ZN11QQuickPopup16resetLeftPaddingEv')

  def resetRightPadding(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetRightPadding()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#resetRightPadding
    """
    #  void QQuickPopup::resetRightPadding()
    self.uglySide.call('ritual_ZN11QQuickPopup17resetRightPaddingEv')

  def resetBottomPadding(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetBottomPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#resetBottomPadding
    """
    #  void QQuickPopup::resetBottomPadding()
    self.uglySide.call('ritual_ZN11QQuickPopup18resetBottomPaddingEv')

  def resetLocale(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetLocale()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#resetLocale
    """
    #  void QQuickPopup::resetLocale()
    self.uglySide.call('ritual_ZN11QQuickPopup11resetLocaleEv')

  def resetFont(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetFont()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#resetFont
    """
    #  void QQuickPopup::resetFont()
    self.uglySide.call('ritual_ZN11QQuickPopup9resetFontEv')

  def resetParentItem(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetParentItem()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#resetParentItem
    """
    #  void QQuickPopup::resetParentItem()
    self.uglySide.call('ritual_ZN11QQuickPopup15resetParentItemEv')

  def resetDim(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetDim()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#resetDim
    """
    #  void QQuickPopup::resetDim()
    self.uglySide.call('ritual_ZN11QQuickPopup8resetDimEv')

  def resetClosePolicy(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetClosePolicy()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#resetClosePolicy
    """
    #  void QQuickPopup::resetClosePolicy()
    self.uglySide.call('ritual_ZN11QQuickPopup16resetClosePolicyEv')

  @overload()
  @overload(Qt.FocusReason)
  def forceActiveFocus(
      self,
      reason: Qt.FocusReason = Qt.FocusReason.OtherFocusReason,
  ) -> None:
    """
    Calls Qt's 'void QQuickPopup::forceActiveFocus(Qt::FocusReason reason)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#forceActiveFocus

    Parameters
    ----------

    reason : Qt.FocusReason
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.FocusReason.OtherFocusReason.
    """
    #  void QQuickPopup::forceActiveFocus(Qt::FocusReason reason)
    self.uglySide.call(
        'ritual_ZN11QQuickPopup16forceActiveFocusEN2Qt11FocusReasonE',
        reason.value,
    )

  def resetSpacing(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetSpacing()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#resetSpacing
    """
    #  void QQuickPopup::resetSpacing()
    self.uglySide.call('ritual_ZN11QQuickPopup12resetSpacingEv')

  def resetHorizontalPadding(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetHorizontalPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#resetHorizontalPadding
    """
    #  void QQuickPopup::resetHorizontalPadding()
    self.uglySide.call('ritual_ZN11QQuickPopup22resetHorizontalPaddingEv')

  def resetVerticalPadding(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetVerticalPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#resetVerticalPadding
    """
    #  void QQuickPopup::resetVerticalPadding()
    self.uglySide.call('ritual_ZN11QQuickPopup20resetVerticalPaddingEv')

  def resetTopInset(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetTopInset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#resetTopInset
    """
    #  void QQuickPopup::resetTopInset()
    self.uglySide.call('ritual_ZN11QQuickPopup13resetTopInsetEv')

  def resetLeftInset(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetLeftInset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#resetLeftInset
    """
    #  void QQuickPopup::resetLeftInset()
    self.uglySide.call('ritual_ZN11QQuickPopup14resetLeftInsetEv')

  def resetRightInset(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetRightInset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#resetRightInset
    """
    #  void QQuickPopup::resetRightInset()
    self.uglySide.call('ritual_ZN11QQuickPopup15resetRightInsetEv')

  def resetBottomInset(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::resetBottomInset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#resetBottomInset
    """
    #  void QQuickPopup::resetBottomInset()
    self.uglySide.call('ritual_ZN11QQuickPopup16resetBottomInsetEv')

  def open(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::open()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#open
    """
    #  void QQuickPopup::open()
    self.uglySide.call('ritual_ZN11QQuickPopup4openEv')

  def close(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#close
    """
    #  void QQuickPopup::close()
    self.uglySide.call('ritual_ZN11QQuickPopup5closeEv')

  def opened(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::opened()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#opened
    """
    #  void QQuickPopup::opened()
    self.uglySide.call('ritual_ZN11QQuickPopup6openedEv')

  def closed(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::closed()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#closed
    """
    #  void QQuickPopup::closed()
    self.uglySide.call('ritual_ZN11QQuickPopup6closedEv')

  def aboutToShow(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::aboutToShow()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#aboutToShow
    """
    #  void QQuickPopup::aboutToShow()
    self.uglySide.call('ritual_ZN11QQuickPopup11aboutToShowEv')

  def aboutToHide(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::aboutToHide()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#aboutToHide
    """
    #  void QQuickPopup::aboutToHide()
    self.uglySide.call('ritual_ZN11QQuickPopup11aboutToHideEv')

  def xChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::xChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#xChanged
    """
    #  void QQuickPopup::xChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup8xChangedEv')

  def yChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::yChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#yChanged
    """
    #  void QQuickPopup::yChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup8yChangedEv')

  def zChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::zChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#zChanged
    """
    #  void QQuickPopup::zChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup8zChangedEv')

  def widthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::widthChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#widthChanged
    """
    #  void QQuickPopup::widthChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup12widthChangedEv')

  def heightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::heightChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#heightChanged
    """
    #  void QQuickPopup::heightChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup13heightChangedEv')

  def implicitWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::implicitWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#implicitWidthChanged
    """
    #  void QQuickPopup::implicitWidthChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup20implicitWidthChangedEv')

  def implicitHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::implicitHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#implicitHeightChanged
    """
    #  void QQuickPopup::implicitHeightChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup21implicitHeightChangedEv')

  def contentWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::contentWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#contentWidthChanged
    """
    #  void QQuickPopup::contentWidthChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup19contentWidthChangedEv')

  def contentHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::contentHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#contentHeightChanged
    """
    #  void QQuickPopup::contentHeightChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup20contentHeightChangedEv')

  def availableWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::availableWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#availableWidthChanged
    """
    #  void QQuickPopup::availableWidthChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup21availableWidthChangedEv')

  def availableHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::availableHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#availableHeightChanged
    """
    #  void QQuickPopup::availableHeightChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup22availableHeightChangedEv')

  def marginsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::marginsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#marginsChanged
    """
    #  void QQuickPopup::marginsChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup14marginsChangedEv')

  def topMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::topMarginChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#topMarginChanged
    """
    #  void QQuickPopup::topMarginChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup16topMarginChangedEv')

  def leftMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::leftMarginChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#leftMarginChanged
    """
    #  void QQuickPopup::leftMarginChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup17leftMarginChangedEv')

  def rightMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::rightMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#rightMarginChanged
    """
    #  void QQuickPopup::rightMarginChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup18rightMarginChangedEv')

  def bottomMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::bottomMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#bottomMarginChanged
    """
    #  void QQuickPopup::bottomMarginChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup19bottomMarginChangedEv')

  def paddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::paddingChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#paddingChanged
    """
    #  void QQuickPopup::paddingChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup14paddingChangedEv')

  def topPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::topPaddingChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#topPaddingChanged
    """
    #  void QQuickPopup::topPaddingChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup17topPaddingChangedEv')

  def leftPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::leftPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#leftPaddingChanged
    """
    #  void QQuickPopup::leftPaddingChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup18leftPaddingChangedEv')

  def rightPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::rightPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#rightPaddingChanged
    """
    #  void QQuickPopup::rightPaddingChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup19rightPaddingChangedEv')

  def bottomPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::bottomPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#bottomPaddingChanged
    """
    #  void QQuickPopup::bottomPaddingChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup20bottomPaddingChangedEv')

  def fontChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::fontChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#fontChanged
    """
    #  void QQuickPopup::fontChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup11fontChangedEv')

  def localeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::localeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#localeChanged
    """
    #  void QQuickPopup::localeChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup13localeChangedEv')

  def parentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::parentChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#parentChanged
    """
    #  void QQuickPopup::parentChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup13parentChangedEv')

  def backgroundChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::backgroundChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#backgroundChanged
    """
    #  void QQuickPopup::backgroundChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup17backgroundChangedEv')

  def contentItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::contentItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#contentItemChanged
    """
    #  void QQuickPopup::contentItemChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup18contentItemChangedEv')

  def contentChildrenChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::contentChildrenChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#contentChildrenChanged
    """
    #  void QQuickPopup::contentChildrenChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup22contentChildrenChangedEv')

  def clipChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::clipChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#clipChanged
    """
    #  void QQuickPopup::clipChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup11clipChangedEv')

  def focusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::focusChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#focusChanged
    """
    #  void QQuickPopup::focusChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup12focusChangedEv')

  def activeFocusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::activeFocusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#activeFocusChanged
    """
    #  void QQuickPopup::activeFocusChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup18activeFocusChangedEv')

  def modalChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::modalChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#modalChanged
    """
    #  void QQuickPopup::modalChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup12modalChangedEv')

  def dimChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::dimChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#dimChanged
    """
    #  void QQuickPopup::dimChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup10dimChangedEv')

  def visibleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::visibleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#visibleChanged
    """
    #  void QQuickPopup::visibleChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup14visibleChangedEv')

  def opacityChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::opacityChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#opacityChanged
    """
    #  void QQuickPopup::opacityChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup14opacityChangedEv')

  def scaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::scaleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#scaleChanged
    """
    #  void QQuickPopup::scaleChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup12scaleChangedEv')

  def closePolicyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::closePolicyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#closePolicyChanged
    """
    #  void QQuickPopup::closePolicyChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup18closePolicyChangedEv')

  def enterChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::enterChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#enterChanged
    """
    #  void QQuickPopup::enterChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup12enterChangedEv')

  def exitChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::exitChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#exitChanged
    """
    #  void QQuickPopup::exitChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup11exitChangedEv')

  @overload(QQuickWindow)
  @overload(NoneType)
  def windowChanged(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QQuickPopup::windowChanged(QQuickWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#windowChanged

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopup::windowChanged(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN11QQuickPopup13windowChangedEP12QQuickWindow',
        self._addressOf(window),
    )

  def spacingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::spacingChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#spacingChanged
    """
    #  void QQuickPopup::spacingChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup14spacingChangedEv')

  def openedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::openedChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#openedChanged
    """
    #  void QQuickPopup::openedChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup13openedChangedEv')

  def mirroredChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::mirroredChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#mirroredChanged
    """
    #  void QQuickPopup::mirroredChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup15mirroredChangedEv')

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::enabledChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#enabledChanged
    """
    #  void QQuickPopup::enabledChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup14enabledChangedEv')

  def paletteChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::paletteChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#paletteChanged
    """
    #  void QQuickPopup::paletteChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup14paletteChangedEv')

  def paletteCreated(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::paletteCreated()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#paletteCreated
    """
    #  void QQuickPopup::paletteCreated()
    self.uglySide.call('ritual_ZN11QQuickPopup14paletteCreatedEv')

  def horizontalPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::horizontalPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#horizontalPaddingChanged
    """
    #  void QQuickPopup::horizontalPaddingChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup24horizontalPaddingChangedEv')

  def verticalPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::verticalPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#verticalPaddingChanged
    """
    #  void QQuickPopup::verticalPaddingChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup22verticalPaddingChangedEv')

  def implicitContentWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::implicitContentWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#implicitContentWidthChanged
    """
    #  void QQuickPopup::implicitContentWidthChanged()
    self.uglySide.call(
        'ritual_ZN11QQuickPopup27implicitContentWidthChangedEv',
    )

  def implicitContentHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::implicitContentHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#implicitContentHeightChanged
    """
    #  void QQuickPopup::implicitContentHeightChanged()
    self.uglySide.call(
        'ritual_ZN11QQuickPopup28implicitContentHeightChangedEv',
    )

  def implicitBackgroundWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::implicitBackgroundWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#implicitBackgroundWidthChanged
    """
    #  void QQuickPopup::implicitBackgroundWidthChanged()
    self.uglySide.call(
        'ritual_ZN11QQuickPopup30implicitBackgroundWidthChangedEv',
    )

  def implicitBackgroundHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::implicitBackgroundHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#implicitBackgroundHeightChanged
    """
    #  void QQuickPopup::implicitBackgroundHeightChanged()
    self.uglySide.call(
        'ritual_ZN11QQuickPopup31implicitBackgroundHeightChangedEv',
    )

  def topInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::topInsetChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#topInsetChanged
    """
    #  void QQuickPopup::topInsetChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup15topInsetChangedEv')

  def leftInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::leftInsetChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#leftInsetChanged
    """
    #  void QQuickPopup::leftInsetChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup16leftInsetChangedEv')

  def rightInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::rightInsetChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#rightInsetChanged
    """
    #  void QQuickPopup::rightInsetChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup17rightInsetChangedEv')

  def bottomInsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::bottomInsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#bottomInsetChanged
    """
    #  void QQuickPopup::bottomInsetChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup18bottomInsetChangedEv')

  def popupTypeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::popupTypeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#popupTypeChanged
    """
    #  void QQuickPopup::popupTypeChanged()
    self.uglySide.call('ritual_ZN11QQuickPopup16popupTypeChangedEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#classBegin
    """
    #  void QQuickPopup::classBegin()
    ritual = 'ritual_ZN11QQuickPopup10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::componentComplete()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#componentComplete
    """
    #  void QQuickPopup::componentComplete()
    ritual = 'ritual_ZN11QQuickPopup17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem, QEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def childMouseEventFilter(
      self,
      child: Optional[QQuickItem],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickPopup::childMouseEventFilter(QQuickItem *child,
    QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#childMouseEventFilter

    Parameters
    ----------

    child : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickPopup::childMouseEventFilter(QQuickItem *child, QEvent
    #      *event)
    ritual = (
        'ritual_ZN11QQuickPopup21childMouseEventFilterEP10QQuickItemP6QEven'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QQuickPopup21childMouseEventFilterEP10QQuickItemP'
          '6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(child), self._addressOf(event),
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopup::focusInEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopup::focusInEvent(QFocusEvent *event)
    ritual = 'ritual_ZN11QQuickPopup12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup12focusInEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopup::focusOutEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#focusOutEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopup::focusOutEvent(QFocusEvent *event)
    ritual = 'ritual_ZN11QQuickPopup13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup13focusOutEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopup::keyPressEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopup::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN11QQuickPopup13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopup::keyReleaseEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopup::keyReleaseEvent(QKeyEvent *event)
    ritual = 'ritual_ZN11QQuickPopup15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup15keyReleaseEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopup::mousePressEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopup::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN11QQuickPopup15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopup::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopup::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN11QQuickPopup14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopup::mouseReleaseEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopup::mouseReleaseEvent(QMouseEvent *event)
    ritual = 'ritual_ZN11QQuickPopup17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup17mouseReleaseEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopup::mouseDoubleClickEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopup::mouseDoubleClickEvent(QMouseEvent *event)
    ritual = 'ritual_ZN11QQuickPopup21mouseDoubleClickEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QQuickPopup21mouseDoubleClickEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def mouseUngrabEvent(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::mouseUngrabEvent()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#mouseUngrabEvent
    """
    #  void QQuickPopup::mouseUngrabEvent()
    ritual = 'ritual_ZN11QQuickPopup16mouseUngrabEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup16mouseUngrabEventEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem, QEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def overlayEvent(
      self,
      item: Optional[QQuickItem],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickPopup::overlayEvent(QQuickItem *item, QEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#overlayEvent

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickPopup::overlayEvent(QQuickItem *item, QEvent *event)
    ritual = 'ritual_ZN11QQuickPopup12overlayEventEP10QQuickItemP6QEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QQuickPopup12overlayEventEP10QQuickItemP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(item), self._addressOf(event),
    )

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopup::touchEvent(QTouchEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#touchEvent

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopup::touchEvent(QTouchEvent *event)
    ritual = 'ritual_ZN11QQuickPopup10touchEventEP11QTouchEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup10touchEventEP11QTouchEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def touchUngrabEvent(self) -> None:
    """
    Calls Qt's 'void QQuickPopup::touchUngrabEvent()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#touchUngrabEvent
    """
    #  void QQuickPopup::touchUngrabEvent()
    ritual = 'ritual_ZN11QQuickPopup16touchUngrabEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup16touchUngrabEventEv'
    self.uglySide.call(ritual)

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopup::wheelEvent(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopup::wheelEvent(QWheelEvent *event)
    ritual = 'ritual_ZN11QQuickPopup10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragEnterEvent)
  @overload(NoneType)
  def dragEnterEvent(self, event: Optional[QDragEnterEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopup::dragEnterEvent(QDragEnterEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#dragEnterEvent

    Parameters
    ----------

    event : Optional[QDragEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopup::dragEnterEvent(QDragEnterEvent *event)
    ritual = 'ritual_ZN11QQuickPopup14dragEnterEventEP15QDragEnterEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QQuickPopup14dragEnterEventEP15QDragEnterEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def dragMoveEvent(self, event: Optional[QDragMoveEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopup::dragMoveEvent(QDragMoveEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#dragMoveEvent

    Parameters
    ----------

    event : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopup::dragMoveEvent(QDragMoveEvent *event)
    ritual = 'ritual_ZN11QQuickPopup13dragMoveEventEP14QDragMoveEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup13dragMoveEventEP14QDragMoveEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragLeaveEvent)
  @overload(NoneType)
  def dragLeaveEvent(self, event: Optional[QDragLeaveEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopup::dragLeaveEvent(QDragLeaveEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#dragLeaveEvent

    Parameters
    ----------

    event : Optional[QDragLeaveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopup::dragLeaveEvent(QDragLeaveEvent *event)
    ritual = 'ritual_ZN11QQuickPopup14dragLeaveEventEP15QDragLeaveEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QQuickPopup14dragLeaveEventEP15QDragLeaveEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDropEvent)
  @overload(NoneType)
  def dropEvent(self, event: Optional[QDropEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopup::dropEvent(QDropEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#dropEvent

    Parameters
    ----------

    event : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopup::dropEvent(QDropEvent *event)
    ritual = 'ritual_ZN11QQuickPopup9dropEventEP10QDropEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup9dropEventEP10QDropEvent'
    self.uglySide.call(ritual, self._addressOf(event))

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
    Calls Qt's 'void QQuickPopup::contentItemChange(QQuickItem *newItem,
    QQuickItem *oldItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#contentItemChange

    Parameters
    ----------

    newItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopup::contentItemChange(QQuickItem *newItem, QQuickItem
    #      *oldItem)
    ritual = 'ritual_ZN11QQuickPopup17contentItemChangeEP10QQuickItemS1_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QQuickPopup17contentItemChangeEP10QQuickItemS1_')
    self.uglySide.call(
        ritual, self._addressOf(newItem), self._addressOf(oldItem),
    )

  @overload(QSizeF, QSizeF)
  def contentSizeChange(self, newSize: QSizeF, oldSize: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickPopup::contentSizeChange(const QSizeF &newSize,
    const QSizeF &oldSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#contentSizeChange

    Parameters
    ----------

    newSize : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    oldSize : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickPopup::contentSizeChange(const QSizeF &newSize, const
    #      QSizeF &oldSize)
    ritual = 'ritual_ZN11QQuickPopup17contentSizeChangeERK6QSizeFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup17contentSizeChangeERK6QSizeFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newSize), self._valueOf(oldSize),
    )

  @overload(QFont, QFont)
  def fontChange(self, newFont: QFont, oldFont: QFont) -> None:
    """
    Calls Qt's 'void QQuickPopup::fontChange(const QFont &newFont, const
    QFont &oldFont)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#fontChange

    Parameters
    ----------

    newFont : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    oldFont : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickPopup::fontChange(const QFont &newFont, const QFont
    #      &oldFont)
    ritual = 'ritual_ZN11QQuickPopup10fontChangeERK5QFontS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup10fontChangeERK5QFontS2_'
    self.uglySide.call(
        ritual, self._valueOf(newFont), self._valueOf(oldFont),
    )

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickPopup::geometryChange(const QRectF &newGeometry,
    const QRectF &oldGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickPopup::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN11QQuickPopup14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QLocale, QLocale)
  def localeChange(self, newLocale: QLocale, oldLocale: QLocale) -> None:
    """
    Calls Qt's 'void QQuickPopup::localeChange(const QLocale &newLocale,
    const QLocale &oldLocale)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#localeChange

    Parameters
    ----------

    newLocale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    oldLocale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QQuickPopup::localeChange(const QLocale &newLocale, const QLocale
    #      &oldLocale)
    ritual = 'ritual_ZN11QQuickPopup12localeChangeERK7QLocaleS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup12localeChangeERK7QLocaleS2_'
    self.uglySide.call(
        ritual, self._valueOf(newLocale), self._valueOf(oldLocale),
    )

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      data: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickPopup::itemChange(QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    data : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickPopup::itemChange(QQuickItem::ItemChange change, const
    #      QQuickItem::ItemChangeData &data)
    ritual = (
        'ritual_ZN11QQuickPopup10itemChangeEN10QQuickItem10ItemChangeERKNS0'
        '_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QQuickPopup10itemChangeEN10QQuickItem10ItemChange'
          'ERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(data))

  @overload(QMarginsF, QMarginsF)
  def marginsChange(
      self,
      newMargins: QMarginsF,
      oldMargins: QMarginsF,
  ) -> None:
    """
    Calls Qt's 'void QQuickPopup::marginsChange(const QMarginsF &newMargins,
    const QMarginsF &oldMargins)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#marginsChange

    Parameters
    ----------

    newMargins : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.

    oldMargins : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.
    """
    #  void QQuickPopup::marginsChange(const QMarginsF &newMargins, const
    #      QMarginsF &oldMargins)
    ritual = 'ritual_ZN11QQuickPopup13marginsChangeERK9QMarginsFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup13marginsChangeERK9QMarginsFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newMargins), self._valueOf(oldMargins),
    )

  @overload(QMarginsF, QMarginsF)
  def paddingChange(
      self,
      newPadding: QMarginsF,
      oldPadding: QMarginsF,
  ) -> None:
    """
    Calls Qt's 'void QQuickPopup::paddingChange(const QMarginsF &newPadding,
    const QMarginsF &oldPadding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#paddingChange

    Parameters
    ----------

    newPadding : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.

    oldPadding : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.
    """
    #  void QQuickPopup::paddingChange(const QMarginsF &newPadding, const
    #      QMarginsF &oldPadding)
    ritual = 'ritual_ZN11QQuickPopup13paddingChangeERK9QMarginsFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup13paddingChangeERK9QMarginsFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newPadding), self._valueOf(oldPadding),
    )

  @overload(float, float)
  def spacingChange(self, newSpacing: float, oldSpacing: float) -> None:
    """
    Calls Qt's 'void QQuickPopup::spacingChange(qreal newSpacing, qreal
    oldSpacing)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#spacingChange

    Parameters
    ----------

    newSpacing : float
      Passed on as it is.

    oldSpacing : float
      Passed on as it is.
    """
    #  void QQuickPopup::spacingChange(qreal newSpacing, qreal oldSpacing)
    ritual = 'ritual_ZN11QQuickPopup13spacingChangeEdd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup13spacingChangeEdd'
    self.uglySide.call(ritual, newSpacing, oldSpacing)

  @overload(QMarginsF, QMarginsF)
  def insetChange(self, newInset: QMarginsF, oldInset: QMarginsF) -> None:
    """
    Calls Qt's 'void QQuickPopup::insetChange(const QMarginsF &newInset,
    const QMarginsF &oldInset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#insetChange

    Parameters
    ----------

    newInset : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.

    oldInset : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.
    """
    #  void QQuickPopup::insetChange(const QMarginsF &newInset, const
    #      QMarginsF &oldInset)
    ritual = 'ritual_ZN11QQuickPopup11insetChangeERK9QMarginsFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup11insetChangeERK9QMarginsFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newInset), self._valueOf(oldInset),
    )

  @overload(bool)
  def accessibilityActiveChanged(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickPopup::accessibilityActiveChanged(bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#accessibilityActiveChanged

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickPopup::accessibilityActiveChanged(bool active)
    ritual = 'ritual_ZN11QQuickPopup26accessibilityActiveChangedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup26accessibilityActiveChangedEb'
    self.uglySide.call(ritual, active)

  @overload(str)
  def maybeSetAccessibleName(self, name: str) -> None:
    """
    Calls Qt's 'void QQuickPopup::maybeSetAccessibleName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#maybeSetAccessibleName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickPopup::maybeSetAccessibleName(const QString &name)
    self.uglySide.call(
        'ritual_ZN11QQuickPopup22maybeSetAccessibleNameERK7QString', name,
    )

  @overload(str)
  @overload(NoneType)
  def accessibleProperty(self, propertyName: Optional[str]) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickPopup::accessibleProperty(const char
    *propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#accessibleProperty

    Parameters
    ----------

    propertyName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickPopup::accessibleProperty(const char *propertyName)
    address = self.uglySide.call(
        'ritual_ZN11QQuickPopup18accessiblePropertyEPKc',
        self._bytesOf(propertyName),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def safeAreaAttachmentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPopup::safeAreaAttachmentItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopup.html#safeAreaAttachmentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPopup::safeAreaAttachmentItem()
    ritual = 'ritual_ZN11QQuickPopup22safeAreaAttachmentItemEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickPopup22safeAreaAttachmentItemEv'
    address = self.uglySide.call(ritual)
    return QQuickItem._cuteAt(address)

  def d_func(self) -> Optional[QQuickPopupPrivate]:
    """
    Calls Qt's 'QQuickPopupPrivate *QQuickPopup::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopup.html#d_func

    Returns
    -------

    Optional[QQuickPopupPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPopupPrivate *QQuickPopup::d_func()
    address = self.uglySide.call('ritual_ZN11QQuickPopup6d_funcEv')
    from . import QQuickPopupPrivate
    return QQuickPopupPrivate._cuteAt(address)

  @staticmethod
  def setWindowModality(*__, **_) -> Never:
    """
    Qt's 'void QQuickPopup::setWindowModality(const Qt::WindowModality
    modality)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickPopup.setWindowModality' has no cute function yet. Qt's "
        "'void QQuickPopup::setWindowModality(const Qt::WindowModality "
        "modality)': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<QQuickPopup *>': the list of QQuickPopup, which
#  'QList[QQuickPopup]' gives. It is made here, so that there is one as soon
#  as there can be a QQuickPopup.
QList.createKind(
    QQuickPopup, 'address',
    make='ritual_list_make_QQuickPopup_ptr',
    add='ritual_list_add_QQuickPopup_ptr',
    size='ritual_list_size_QQuickPopup_ptr',
    at='ritual_list_at_QQuickPopup_ptr',
    drop='ritual_list_drop_QQuickPopup_ptr',
)
