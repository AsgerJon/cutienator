"""
QQuickComboBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcombobox_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickComboBox to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickControl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QLocale, QMetaObject, QVariant
  from ..QtGui import QFocusEvent, QFont, QInputMethodEvent, QKeyEvent
  from ..QtGui import QValidator, QWheelEvent
  from ..QtQml import QQmlComponent
  from ..QtQmlModels import QQmlInstanceModel
  from . import QQuickPopup
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QFont = WAIT['QFont']
  QInputMethodEvent = WAIT['QInputMethodEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QLocale = WAIT['QLocale']
  QQmlComponent = WAIT['QQmlComponent']
  QQuickPopup = WAIT['QQuickPopup']
  QValidator = WAIT['QValidator']
  QVariant = WAIT['QVariant']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickComboBox(QQuickControl):
  """
  The cute side of Qt's QQuickComboBox: a plain Python object standing in
  front of one C++ QQuickComboBox.

  It is built on the cute 'QQuickControl', as Qt's QQuickComboBox is built on
  Qt's QQuickControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickComboBox that has a ritual and that Python can
  call so far, 104 names in all: 'metaObject', 'tr', 'count', 'model',
  'setModel', 'delegateModel', 'isPressed', 'setPressed', 'highlightedIndex',
  'currentIndex', 'setCurrentIndex', 'currentText', 'displayText',
  'setDisplayText', 'resetDisplayText', 'textRole', 'setTextRole',
  'valueRole', 'setValueRole', 'delegate', 'setDelegate', 'indicator',
  'setIndicator', 'popup', 'setPopup', 'textAt', 'find', 'isFlat', 'setFlat',
  'isDown', 'setDown', 'resetDown', 'isEditable', 'setEditable', 'editText',
  'setEditText', 'resetEditText', 'validator', 'setValidator',
  'inputMethodHints', 'setInputMethodHints', 'isInputMethodComposing',
  'hasAcceptableInput', 'implicitIndicatorWidth', 'implicitIndicatorHeight',
  'currentValue', 'setCurrentValue', 'valueAt', 'indexOfValue',
  'selectTextByMouse', 'setSelectTextByMouse', 'implicitContentWidthPolicy',
  'setImplicitContentWidthPolicy', 'highlightOnHover', 'setHighlightOnHover',
  'incrementCurrentIndex', 'decrementCurrentIndex', 'selectAll', 'activated',
  'highlighted', 'countChanged', 'modelChanged', 'delegateModelChanged',
  'pressedChanged', 'highlightedIndexChanged', 'currentIndexChanged',
  'currentTextChanged', 'displayTextChanged', 'textRoleChanged',
  'delegateChanged', 'indicatorChanged', 'popupChanged', 'flatChanged',
  'accepted', 'downChanged', 'editableChanged', 'editTextChanged',
  'validatorChanged', 'inputMethodHintsChanged',
  'inputMethodComposingChanged', 'acceptableInputChanged',
  'implicitIndicatorWidthChanged', 'implicitIndicatorHeightChanged',
  'valueRoleChanged', 'currentValueChanged', 'selectTextByMouseChanged',
  'implicitContentWidthPolicyChanged', 'highlightOnHoverChanged',
  'eventFilter', 'focusInEvent', 'focusOutEvent', 'inputMethodEvent',
  'keyPressEvent', 'keyReleaseEvent', 'wheelEvent', 'event',
  'componentComplete', 'itemChange', 'fontChange', 'contentItemChange',
  'localeChange', 'defaultFont', 'accessibleRole',
  'accessibilityActiveChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickComboBox::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickComboBox::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickComboBox::~QQuickComboBox()': the destructor: Python never
    removes a C++ QQuickComboBox.
  - Qt's 'QQuickComboBoxPrivate *QQuickComboBox::d_func()': gives
    'QQuickComboBoxPrivate', which has no cute class yet.
  - Qt's 'const QQuickComboBoxPrivate *QQuickComboBox::d_func() const': gives
    'QQuickComboBoxPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 114 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickComboBox is created at the first use, not by
    'QQuickComboBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickComboBox.
  - Qt tells when it has removed the C++ QQuickComboBox. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickComboBox, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ImplicitContentWidthPolicy(CuteNum):
    """
    The enum 'QQuickComboBox::ImplicitContentWidthPolicy' of Qt, with the 3
    names Qt gives in it.
    """

    ContentItemImplicitWidth = Kee[int](0)
    WidestText = Kee[int](1)
    WidestTextWhenCompleted = Kee[int](2)

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
    Calls Qt's 'QString QQuickComboBox::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#tr

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
    #  QString QQuickComboBox::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickComboBox2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickComboBox'

  #  A C++ QQuickComboBox Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickComboBox'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickComboBox::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickComboBox::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickComboBox10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QQuickComboBox::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#count
    """
    #  int QQuickComboBox::count() const
    return self.uglySide.call('ritual_ZNK14QQuickComboBox5countEv')

  def model(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickComboBox::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#model

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickComboBox::model() const
    address = self.uglySide.call('ritual_ZNK14QQuickComboBox5modelEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def delegateModel(self) -> Optional[QQmlInstanceModel]:
    """
    Calls Qt's 'QQmlInstanceModel *QQuickComboBox::delegateModel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#delegateModel

    Returns
    -------

    Optional[QQmlInstanceModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlInstanceModel *QQuickComboBox::delegateModel() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickComboBox13delegateModelEv',
    )
    from ..QtQmlModels import QQmlInstanceModel
    return QQmlInstanceModel._cuteAt(address)

  def isPressed(self) -> bool:
    """
    Calls Qt's 'bool QQuickComboBox::isPressed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#isPressed
    """
    #  bool QQuickComboBox::isPressed() const
    return self.uglySide.call('ritual_ZNK14QQuickComboBox9isPressedEv')

  def highlightedIndex(self) -> int:
    """
    Calls Qt's 'int QQuickComboBox::highlightedIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#highlightedIndex
    """
    #  int QQuickComboBox::highlightedIndex() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickComboBox16highlightedIndexEv',
    )

  def currentIndex(self) -> int:
    """
    Calls Qt's 'int QQuickComboBox::currentIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#currentIndex
    """
    #  int QQuickComboBox::currentIndex() const
    return self.uglySide.call('ritual_ZNK14QQuickComboBox12currentIndexEv')

  def currentText(self) -> str:
    """
    Calls Qt's 'QString QQuickComboBox::currentText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#currentText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickComboBox::currentText() const
    return self.uglySide.call('ritual_ZNK14QQuickComboBox11currentTextEv')

  def displayText(self) -> str:
    """
    Calls Qt's 'QString QQuickComboBox::displayText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#displayText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickComboBox::displayText() const
    return self.uglySide.call('ritual_ZNK14QQuickComboBox11displayTextEv')

  def textRole(self) -> str:
    """
    Calls Qt's 'QString QQuickComboBox::textRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#textRole

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickComboBox::textRole() const
    return self.uglySide.call('ritual_ZNK14QQuickComboBox8textRoleEv')

  def valueRole(self) -> str:
    """
    Calls Qt's 'QString QQuickComboBox::valueRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#valueRole

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickComboBox::valueRole() const
    return self.uglySide.call('ritual_ZNK14QQuickComboBox9valueRoleEv')

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickComboBox::delegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickComboBox::delegate() const
    address = self.uglySide.call('ritual_ZNK14QQuickComboBox8delegateEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def indicator(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickComboBox::indicator() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#indicator

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickComboBox::indicator() const
    address = self.uglySide.call('ritual_ZNK14QQuickComboBox9indicatorEv')
    return QQuickItem._cuteAt(address)

  def popup(self) -> Optional[QQuickPopup]:
    """
    Calls Qt's 'QQuickPopup *QQuickComboBox::popup() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#popup

    Returns
    -------

    Optional[QQuickPopup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPopup *QQuickComboBox::popup() const
    address = self.uglySide.call('ritual_ZNK14QQuickComboBox5popupEv')
    from . import QQuickPopup
    return QQuickPopup._cuteAt(address)

  @overload(int)
  def textAt(self, index: int) -> str:
    """
    Calls Qt's 'QString QQuickComboBox::textAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#textAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickComboBox::textAt(int index) const
    return self.uglySide.call('ritual_ZNK14QQuickComboBox6textAtEi', index)

  @overload(str)
  @overload(str, Qt.MatchFlags)
  def find(
      self,
      text: str,
      flags: Qt.MatchFlags = Qt.MatchFlags.MatchExactly,
  ) -> int:
    """
    Calls Qt's 'int QQuickComboBox::find(const QString &text, Qt::MatchFlags
    flags) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#find

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    flags : Qt.MatchFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.MatchFlags.MatchExactly.
    """
    #  int QQuickComboBox::find(const QString &text, Qt::MatchFlags flags)
    #      const
    return self.uglySide.call(
        'ritual_ZNK14QQuickComboBox4findERK7QString6QFlagsIN2Qt9MatchFlagEE',
        text, flags.value,
    )

  def isFlat(self) -> bool:
    """
    Calls Qt's 'bool QQuickComboBox::isFlat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#isFlat
    """
    #  bool QQuickComboBox::isFlat() const
    return self.uglySide.call('ritual_ZNK14QQuickComboBox6isFlatEv')

  def isDown(self) -> bool:
    """
    Calls Qt's 'bool QQuickComboBox::isDown() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#isDown
    """
    #  bool QQuickComboBox::isDown() const
    return self.uglySide.call('ritual_ZNK14QQuickComboBox6isDownEv')

  def isEditable(self) -> bool:
    """
    Calls Qt's 'bool QQuickComboBox::isEditable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#isEditable
    """
    #  bool QQuickComboBox::isEditable() const
    return self.uglySide.call('ritual_ZNK14QQuickComboBox10isEditableEv')

  def editText(self) -> str:
    """
    Calls Qt's 'QString QQuickComboBox::editText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#editText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickComboBox::editText() const
    return self.uglySide.call('ritual_ZNK14QQuickComboBox8editTextEv')

  def validator(self) -> Optional[QValidator]:
    """
    Calls Qt's 'QValidator *QQuickComboBox::validator() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#validator

    Returns
    -------

    Optional[QValidator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValidator *QQuickComboBox::validator() const
    address = self.uglySide.call('ritual_ZNK14QQuickComboBox9validatorEv')
    from ..QtGui import QValidator
    return QValidator._cuteAt(address)

  def inputMethodHints(self) -> Qt.InputMethodHints:
    """
    Calls Qt's 'Qt::InputMethodHints QQuickComboBox::inputMethodHints()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#inputMethodHints

    Returns
    -------

    Qt.InputMethodHints
      The value standing for the combination Qt gave back.
    """
    #  Qt::InputMethodHints QQuickComboBox::inputMethodHints() const
    return Qt.InputMethodHints(self.uglySide.call(
        'ritual_ZNK14QQuickComboBox16inputMethodHintsEv',
    ))

  def isInputMethodComposing(self) -> bool:
    """
    Calls Qt's 'bool QQuickComboBox::isInputMethodComposing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#isInputMethodComposing
    """
    #  bool QQuickComboBox::isInputMethodComposing() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickComboBox22isInputMethodComposingEv',
    )

  def hasAcceptableInput(self) -> bool:
    """
    Calls Qt's 'bool QQuickComboBox::hasAcceptableInput() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#hasAcceptableInput
    """
    #  bool QQuickComboBox::hasAcceptableInput() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickComboBox18hasAcceptableInputEv',
    )

  def implicitIndicatorWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickComboBox::implicitIndicatorWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#implicitIndicatorWidth
    """
    #  qreal QQuickComboBox::implicitIndicatorWidth() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickComboBox22implicitIndicatorWidthEv',
    )

  def implicitIndicatorHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickComboBox::implicitIndicatorHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#implicitIndicatorHeight
    """
    #  qreal QQuickComboBox::implicitIndicatorHeight() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickComboBox23implicitIndicatorHeightEv',
    )

  def currentValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickComboBox::currentValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#currentValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickComboBox::currentValue() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickComboBox12currentValueEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def valueAt(self, index: int) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickComboBox::valueAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#valueAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickComboBox::valueAt(int index) const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickComboBox7valueAtEi', index,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QVariant)
  def indexOfValue(self, value: QVariant) -> int:
    """
    Calls Qt's 'int QQuickComboBox::indexOfValue(const QVariant &value)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#indexOfValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  int QQuickComboBox::indexOfValue(const QVariant &value) const
    return self.uglySide.call(
        'ritual_ZNK14QQuickComboBox12indexOfValueERK8QVariant',
        self._valueOf(value),
    )

  def selectTextByMouse(self) -> bool:
    """
    Calls Qt's 'bool QQuickComboBox::selectTextByMouse() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#selectTextByMouse
    """
    #  bool QQuickComboBox::selectTextByMouse() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickComboBox17selectTextByMouseEv',
    )

  def implicitContentWidthPolicy(self) -> ImplicitContentWidthPolicy:
    """
    Calls Qt's 'ImplicitContentWidthPolicy
    QQuickComboBox::implicitContentWidthPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#implicitContentWidthPolicy

    Returns
    -------

    ImplicitContentWidthPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'ImplicitContentWidthPolicy(number)' gives.
    """
    #  ImplicitContentWidthPolicy
    #      QQuickComboBox::implicitContentWidthPolicy() const
    return QQuickComboBox.ImplicitContentWidthPolicy(self.uglySide.call(
        'ritual_ZNK14QQuickComboBox26implicitContentWidthPolicyEv',
    ))

  def highlightOnHover(self) -> bool:
    """
    Calls Qt's 'bool QQuickComboBox::highlightOnHover() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#highlightOnHover
    """
    #  bool QQuickComboBox::highlightOnHover() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickComboBox16highlightOnHoverEv',
    )

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickComboBox::defaultFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickComboBox::defaultFont() const
    ritual = 'ritual_ZNK14QQuickComboBox11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickComboBox11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickComboBox::accessibleRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickComboBox::accessibleRole() const
    ritual = 'ritual_ZNK14QQuickComboBox14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickComboBox14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setModel(self, model: QVariant) -> None:
    """
    Calls Qt's 'void QQuickComboBox::setModel(const QVariant &model)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#setModel

    Parameters
    ----------

    model : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickComboBox::setModel(const QVariant &model)
    self.uglySide.call(
        'ritual_ZN14QQuickComboBox8setModelERK8QVariant',
        self._valueOf(model),
    )

  @overload(bool)
  def setPressed(self, pressed: bool) -> None:
    """
    Calls Qt's 'void QQuickComboBox::setPressed(bool pressed)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#setPressed

    Parameters
    ----------

    pressed : bool
      Passed on as it is.
    """
    #  void QQuickComboBox::setPressed(bool pressed)
    self.uglySide.call('ritual_ZN14QQuickComboBox10setPressedEb', pressed)

  @overload(int)
  def setCurrentIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QQuickComboBox::setCurrentIndex(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#setCurrentIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQuickComboBox::setCurrentIndex(int index)
    self.uglySide.call('ritual_ZN14QQuickComboBox15setCurrentIndexEi', index)

  @overload(str)
  def setDisplayText(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickComboBox::setDisplayText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#setDisplayText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickComboBox::setDisplayText(const QString &text)
    self.uglySide.call(
        'ritual_ZN14QQuickComboBox14setDisplayTextERK7QString', text,
    )

  @overload(str)
  def setTextRole(self, role: str) -> None:
    """
    Calls Qt's 'void QQuickComboBox::setTextRole(const QString &role)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#setTextRole

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickComboBox::setTextRole(const QString &role)
    self.uglySide.call(
        'ritual_ZN14QQuickComboBox11setTextRoleERK7QString', role,
    )

  @overload(str)
  def setValueRole(self, role: str) -> None:
    """
    Calls Qt's 'void QQuickComboBox::setValueRole(const QString &role)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#setValueRole

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickComboBox::setValueRole(const QString &role)
    self.uglySide.call(
        'ritual_ZN14QQuickComboBox12setValueRoleERK7QString', role,
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, delegate: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickComboBox::setDelegate(QQmlComponent *delegate)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#setDelegate

    Parameters
    ----------

    delegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickComboBox::setDelegate(QQmlComponent *delegate)
    self.uglySide.call(
        'ritual_ZN14QQuickComboBox11setDelegateEP13QQmlComponent',
        self._addressOf(delegate),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setIndicator(self, indicator: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickComboBox::setIndicator(QQuickItem *indicator)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#setIndicator

    Parameters
    ----------

    indicator : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickComboBox::setIndicator(QQuickItem *indicator)
    self.uglySide.call(
        'ritual_ZN14QQuickComboBox12setIndicatorEP10QQuickItem',
        self._addressOf(indicator),
    )

  @overload(QQuickPopup)
  @overload(NoneType)
  def setPopup(self, popup: Optional[QQuickPopup]) -> None:
    """
    Calls Qt's 'void QQuickComboBox::setPopup(QQuickPopup *popup)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#setPopup

    Parameters
    ----------

    popup : Optional[QQuickPopup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickComboBox::setPopup(QQuickPopup *popup)
    self.uglySide.call(
        'ritual_ZN14QQuickComboBox8setPopupEP11QQuickPopup',
        self._addressOf(popup),
    )

  @overload(bool)
  def setFlat(self, flat: bool) -> None:
    """
    Calls Qt's 'void QQuickComboBox::setFlat(bool flat)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#setFlat

    Parameters
    ----------

    flat : bool
      Passed on as it is.
    """
    #  void QQuickComboBox::setFlat(bool flat)
    self.uglySide.call('ritual_ZN14QQuickComboBox7setFlatEb', flat)

  @overload(bool)
  def setDown(self, down: bool) -> None:
    """
    Calls Qt's 'void QQuickComboBox::setDown(bool down)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#setDown

    Parameters
    ----------

    down : bool
      Passed on as it is.
    """
    #  void QQuickComboBox::setDown(bool down)
    self.uglySide.call('ritual_ZN14QQuickComboBox7setDownEb', down)

  @overload(bool)
  def setEditable(self, editable: bool) -> None:
    """
    Calls Qt's 'void QQuickComboBox::setEditable(bool editable)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#setEditable

    Parameters
    ----------

    editable : bool
      Passed on as it is.
    """
    #  void QQuickComboBox::setEditable(bool editable)
    self.uglySide.call('ritual_ZN14QQuickComboBox11setEditableEb', editable)

  @overload(str)
  def setEditText(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickComboBox::setEditText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#setEditText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickComboBox::setEditText(const QString &text)
    self.uglySide.call(
        'ritual_ZN14QQuickComboBox11setEditTextERK7QString', text,
    )

  @overload(QValidator)
  @overload(NoneType)
  def setValidator(self, validator: Optional[QValidator]) -> None:
    """
    Calls Qt's 'void QQuickComboBox::setValidator(QValidator *validator)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#setValidator

    Parameters
    ----------

    validator : Optional[QValidator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickComboBox::setValidator(QValidator *validator)
    self.uglySide.call(
        'ritual_ZN14QQuickComboBox12setValidatorEP10QValidator',
        self._addressOf(validator),
    )

  @overload(Qt.InputMethodHints)
  def setInputMethodHints(self, hints: Qt.InputMethodHints) -> None:
    """
    Calls Qt's 'void QQuickComboBox::setInputMethodHints(Qt::InputMethodHints
    hints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#setInputMethodHints

    Parameters
    ----------

    hints : Qt.InputMethodHints
      Passed on as its number.
    """
    #  void QQuickComboBox::setInputMethodHints(Qt::InputMethodHints hints)
    self.uglySide.call(
        'ritual_ZN14QQuickComboBox19setInputMethodHintsE6QFlagsIN2Qt15Input'
        'MethodHintEE',
        hints.value,
    )

  @overload(QVariant)
  def setCurrentValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QQuickComboBox::setCurrentValue(const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#setCurrentValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickComboBox::setCurrentValue(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN14QQuickComboBox15setCurrentValueERK8QVariant',
        self._valueOf(value),
    )

  @overload(bool)
  def setSelectTextByMouse(self, canSelect: bool) -> None:
    """
    Calls Qt's 'void QQuickComboBox::setSelectTextByMouse(bool canSelect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#setSelectTextByMouse

    Parameters
    ----------

    canSelect : bool
      Passed on as it is.
    """
    #  void QQuickComboBox::setSelectTextByMouse(bool canSelect)
    self.uglySide.call(
        'ritual_ZN14QQuickComboBox20setSelectTextByMouseEb', canSelect,
    )

  @overload(ImplicitContentWidthPolicy)
  def setImplicitContentWidthPolicy(
      self,
      policy: ImplicitContentWidthPolicy,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickComboBox::setImplicitContentWidthPolicy(ImplicitContentWidthPolicy
    policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#setImplicitContentWidthPolicy

    Parameters
    ----------

    policy : ImplicitContentWidthPolicy
      Passed on as its number.
    """
    #  void QQuickComboBox::setImplicitContentWidthPolicy(
    #      ImplicitContentWidthPolicy policy)
    self.uglySide.call(
        'ritual_ZN14QQuickComboBox29setImplicitContentWidthPolicyENS_26Impl'
        'icitContentWidthPolicyE',
        policy.value,
    )

  @overload(bool)
  def setHighlightOnHover(self, value: bool) -> None:
    """
    Calls Qt's 'void QQuickComboBox::setHighlightOnHover(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#setHighlightOnHover

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QQuickComboBox::setHighlightOnHover(bool value)
    self.uglySide.call(
        'ritual_ZN14QQuickComboBox19setHighlightOnHoverEb', value,
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
    Notes what was given, for Qt's 'QQuickComboBox::QQuickComboBox(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#QQuickComboBox

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickComboBox::QQuickComboBox(QQuickItem *parent)
    self._noteCreation(QQuickComboBox, lambda: Rituals.call(
        'ritual_ZN14QQuickComboBoxC1EP10QQuickItem', self._addressOf(parent),
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

  def resetDisplayText(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::resetDisplayText()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#resetDisplayText
    """
    #  void QQuickComboBox::resetDisplayText()
    self.uglySide.call('ritual_ZN14QQuickComboBox16resetDisplayTextEv')

  def resetDown(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::resetDown()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#resetDown
    """
    #  void QQuickComboBox::resetDown()
    self.uglySide.call('ritual_ZN14QQuickComboBox9resetDownEv')

  def resetEditText(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::resetEditText()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#resetEditText
    """
    #  void QQuickComboBox::resetEditText()
    self.uglySide.call('ritual_ZN14QQuickComboBox13resetEditTextEv')

  def incrementCurrentIndex(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::incrementCurrentIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#incrementCurrentIndex
    """
    #  void QQuickComboBox::incrementCurrentIndex()
    self.uglySide.call('ritual_ZN14QQuickComboBox21incrementCurrentIndexEv')

  def decrementCurrentIndex(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::decrementCurrentIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#decrementCurrentIndex
    """
    #  void QQuickComboBox::decrementCurrentIndex()
    self.uglySide.call('ritual_ZN14QQuickComboBox21decrementCurrentIndexEv')

  def selectAll(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::selectAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#selectAll
    """
    #  void QQuickComboBox::selectAll()
    self.uglySide.call('ritual_ZN14QQuickComboBox9selectAllEv')

  @overload(int)
  def activated(self, index: int) -> None:
    """
    Calls Qt's 'void QQuickComboBox::activated(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#activated

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQuickComboBox::activated(int index)
    self.uglySide.call('ritual_ZN14QQuickComboBox9activatedEi', index)

  @overload(int)
  def highlighted(self, index: int) -> None:
    """
    Calls Qt's 'void QQuickComboBox::highlighted(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#highlighted

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQuickComboBox::highlighted(int index)
    self.uglySide.call('ritual_ZN14QQuickComboBox11highlightedEi', index)

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::countChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#countChanged
    """
    #  void QQuickComboBox::countChanged()
    self.uglySide.call('ritual_ZN14QQuickComboBox12countChangedEv')

  def modelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::modelChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#modelChanged
    """
    #  void QQuickComboBox::modelChanged()
    self.uglySide.call('ritual_ZN14QQuickComboBox12modelChangedEv')

  def delegateModelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::delegateModelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#delegateModelChanged
    """
    #  void QQuickComboBox::delegateModelChanged()
    self.uglySide.call('ritual_ZN14QQuickComboBox20delegateModelChangedEv')

  def pressedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::pressedChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#pressedChanged
    """
    #  void QQuickComboBox::pressedChanged()
    self.uglySide.call('ritual_ZN14QQuickComboBox14pressedChangedEv')

  def highlightedIndexChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::highlightedIndexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#highlightedIndexChanged
    """
    #  void QQuickComboBox::highlightedIndexChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickComboBox23highlightedIndexChangedEv',
    )

  def currentIndexChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::currentIndexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#currentIndexChanged
    """
    #  void QQuickComboBox::currentIndexChanged()
    self.uglySide.call('ritual_ZN14QQuickComboBox19currentIndexChangedEv')

  def currentTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::currentTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#currentTextChanged
    """
    #  void QQuickComboBox::currentTextChanged()
    self.uglySide.call('ritual_ZN14QQuickComboBox18currentTextChangedEv')

  def displayTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::displayTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#displayTextChanged
    """
    #  void QQuickComboBox::displayTextChanged()
    self.uglySide.call('ritual_ZN14QQuickComboBox18displayTextChangedEv')

  def textRoleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::textRoleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#textRoleChanged
    """
    #  void QQuickComboBox::textRoleChanged()
    self.uglySide.call('ritual_ZN14QQuickComboBox15textRoleChangedEv')

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#delegateChanged
    """
    #  void QQuickComboBox::delegateChanged()
    self.uglySide.call('ritual_ZN14QQuickComboBox15delegateChangedEv')

  def indicatorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::indicatorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#indicatorChanged
    """
    #  void QQuickComboBox::indicatorChanged()
    self.uglySide.call('ritual_ZN14QQuickComboBox16indicatorChangedEv')

  def popupChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::popupChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#popupChanged
    """
    #  void QQuickComboBox::popupChanged()
    self.uglySide.call('ritual_ZN14QQuickComboBox12popupChangedEv')

  def flatChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::flatChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#flatChanged
    """
    #  void QQuickComboBox::flatChanged()
    self.uglySide.call('ritual_ZN14QQuickComboBox11flatChangedEv')

  def accepted(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::accepted()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#accepted
    """
    #  void QQuickComboBox::accepted()
    self.uglySide.call('ritual_ZN14QQuickComboBox8acceptedEv')

  def downChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::downChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#downChanged
    """
    #  void QQuickComboBox::downChanged()
    self.uglySide.call('ritual_ZN14QQuickComboBox11downChangedEv')

  def editableChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::editableChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#editableChanged
    """
    #  void QQuickComboBox::editableChanged()
    self.uglySide.call('ritual_ZN14QQuickComboBox15editableChangedEv')

  def editTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::editTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#editTextChanged
    """
    #  void QQuickComboBox::editTextChanged()
    self.uglySide.call('ritual_ZN14QQuickComboBox15editTextChangedEv')

  def validatorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::validatorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#validatorChanged
    """
    #  void QQuickComboBox::validatorChanged()
    self.uglySide.call('ritual_ZN14QQuickComboBox16validatorChangedEv')

  def inputMethodHintsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::inputMethodHintsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#inputMethodHintsChanged
    """
    #  void QQuickComboBox::inputMethodHintsChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickComboBox23inputMethodHintsChangedEv',
    )

  def inputMethodComposingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::inputMethodComposingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#inputMethodComposingChanged
    """
    #  void QQuickComboBox::inputMethodComposingChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickComboBox27inputMethodComposingChangedEv',
    )

  def acceptableInputChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::acceptableInputChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#acceptableInputChanged
    """
    #  void QQuickComboBox::acceptableInputChanged()
    self.uglySide.call('ritual_ZN14QQuickComboBox22acceptableInputChangedEv')

  def implicitIndicatorWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::implicitIndicatorWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#implicitIndicatorWidthChanged
    """
    #  void QQuickComboBox::implicitIndicatorWidthChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickComboBox29implicitIndicatorWidthChangedEv',
    )

  def implicitIndicatorHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::implicitIndicatorHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#implicitIndicatorHeightChanged
    """
    #  void QQuickComboBox::implicitIndicatorHeightChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickComboBox30implicitIndicatorHeightChangedEv',
    )

  def valueRoleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::valueRoleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#valueRoleChanged
    """
    #  void QQuickComboBox::valueRoleChanged()
    self.uglySide.call('ritual_ZN14QQuickComboBox16valueRoleChangedEv')

  def currentValueChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::currentValueChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#currentValueChanged
    """
    #  void QQuickComboBox::currentValueChanged()
    self.uglySide.call('ritual_ZN14QQuickComboBox19currentValueChangedEv')

  def selectTextByMouseChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::selectTextByMouseChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#selectTextByMouseChanged
    """
    #  void QQuickComboBox::selectTextByMouseChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickComboBox24selectTextByMouseChangedEv',
    )

  def implicitContentWidthPolicyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::implicitContentWidthPolicyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html
    """
    #  void QQuickComboBox::implicitContentWidthPolicyChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickComboBox33implicitContentWidthPolicyChangedEv',
    )

  def highlightOnHoverChanged(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::highlightOnHoverChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#highlightOnHoverChanged
    """
    #  void QQuickComboBox::highlightOnHoverChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickComboBox23highlightOnHoverChangedEv',
    )

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      object: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickComboBox::eventFilter(QObject *object, QEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#eventFilter

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickComboBox::eventFilter(QObject *object, QEvent *event)
    ritual = 'ritual_ZN14QQuickComboBox11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickComboBox11eventFilterEP7QObjectP6QEvent'
    return self.uglySide.call(
        ritual, self._addressOf(object, 'QObject'), self._addressOf(event),
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickComboBox::focusInEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickComboBox::focusInEvent(QFocusEvent *event)
    ritual = 'ritual_ZN14QQuickComboBox12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickComboBox12focusInEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickComboBox::focusOutEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#focusOutEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickComboBox::focusOutEvent(QFocusEvent *event)
    ritual = 'ritual_ZN14QQuickComboBox13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickComboBox13focusOutEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QInputMethodEvent)
  @overload(NoneType)
  def inputMethodEvent(self, event: Optional[QInputMethodEvent]) -> None:
    """
    Calls Qt's 'void QQuickComboBox::inputMethodEvent(QInputMethodEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#inputMethodEvent

    Parameters
    ----------

    event : Optional[QInputMethodEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickComboBox::inputMethodEvent(QInputMethodEvent *event)
    ritual = (
        'ritual_ZN14QQuickComboBox16inputMethodEventEP17QInputMethodEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickComboBox16inputMethodEventEP17QInputMethodE'
          'vent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickComboBox::keyPressEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickComboBox::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN14QQuickComboBox13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickComboBox13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickComboBox::keyReleaseEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickComboBox::keyReleaseEvent(QKeyEvent *event)
    ritual = 'ritual_ZN14QQuickComboBox15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickComboBox15keyReleaseEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QQuickComboBox::wheelEvent(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickComboBox::wheelEvent(QWheelEvent *event)
    ritual = 'ritual_ZN14QQuickComboBox10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickComboBox10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickComboBox::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickComboBox::event(QEvent *e)
    ritual = 'ritual_ZN14QQuickComboBox5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickComboBox5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickComboBox::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#componentComplete
    """
    #  void QQuickComboBox::componentComplete()
    ritual = 'ritual_ZN14QQuickComboBox17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickComboBox17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickComboBox::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickComboBox::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN14QQuickComboBox10itemChangeEN10QQuickItem10ItemChangeERK'
        'NS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickComboBox10itemChangeEN10QQuickItem10ItemCha'
          'ngeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  @overload(QFont, QFont)
  def fontChange(self, newFont: QFont, oldFont: QFont) -> None:
    """
    Calls Qt's 'void QQuickComboBox::fontChange(const QFont &newFont, const
    QFont &oldFont)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#fontChange

    Parameters
    ----------

    newFont : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    oldFont : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickComboBox::fontChange(const QFont &newFont, const QFont
    #      &oldFont)
    ritual = 'ritual_ZN14QQuickComboBox10fontChangeERK5QFontS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickComboBox10fontChangeERK5QFontS2_'
    self.uglySide.call(
        ritual, self._valueOf(newFont), self._valueOf(oldFont),
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
    Calls Qt's 'void QQuickComboBox::contentItemChange(QQuickItem *newItem,
    QQuickItem *oldItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#contentItemChange

    Parameters
    ----------

    newItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickComboBox::contentItemChange(QQuickItem *newItem, QQuickItem
    #      *oldItem)
    ritual = 'ritual_ZN14QQuickComboBox17contentItemChangeEP10QQuickItemS1_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickComboBox17contentItemChangeEP10QQuickItemS1'
          '_')
    self.uglySide.call(
        ritual, self._addressOf(newItem), self._addressOf(oldItem),
    )

  @overload(QLocale, QLocale)
  def localeChange(self, newLocale: QLocale, oldLocale: QLocale) -> None:
    """
    Calls Qt's 'void QQuickComboBox::localeChange(const QLocale &newLocale,
    const QLocale &oldLocale)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcombobox.html#localeChange

    Parameters
    ----------

    newLocale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    oldLocale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QQuickComboBox::localeChange(const QLocale &newLocale, const
    #      QLocale &oldLocale)
    ritual = 'ritual_ZN14QQuickComboBox12localeChangeERK7QLocaleS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickComboBox12localeChangeERK7QLocaleS2_'
    self.uglySide.call(
        ritual, self._valueOf(newLocale), self._valueOf(oldLocale),
    )

  @overload(bool)
  def accessibilityActiveChanged(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickComboBox::accessibilityActiveChanged(bool
    active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcombobox.html#accessibilityActiveChanged

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickComboBox::accessibilityActiveChanged(bool active)
    ritual = 'ritual_ZN14QQuickComboBox26accessibilityActiveChangedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickComboBox26accessibilityActiveChangedEb'
    self.uglySide.call(ritual, active)
