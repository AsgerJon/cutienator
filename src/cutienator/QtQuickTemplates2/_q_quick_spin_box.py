"""
QQuickSpinBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickspinbox_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickSpinBox to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickControl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QLocale, QMetaObject, QTimerEvent
  from ..QtGui import QFocusEvent, QFont, QHoverEvent, QKeyEvent, QWheelEvent
  from ..QtQml import QJSValue
  from . import QQuickControlPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFocusEvent = WAIT['QFocusEvent']
  QHoverEvent = WAIT['QHoverEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QLocale = WAIT['QLocale']
  QTimerEvent = WAIT['QTimerEvent']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSpinBox(QQuickControl):
  """
  The cute side of Qt's QQuickSpinBox: a plain Python object standing in
  front of one C++ QQuickSpinBox.

  It is built on the cute 'QQuickControl', as Qt's QQuickSpinBox is built on
  Qt's QQuickControl, and has everything that class has. Qt's QQuickSpinBox
  is built on Qt's QQuickAbstractSpinBox<QQuickSpinBox, int> as well, which
  is not reflected.

  What exists
  -----------

  Every function of Qt's QQuickSpinBox that has a ritual and that Python can
  call so far, 44 names in all: 'metaObject', 'tr', 'setFrom', 'setTo',
  'setValue', 'setStepSize', 'isLive', 'setLive', 'textFromValue',
  'valueFromText', 'setWrap', 'increase', 'decrease', 'fromChanged',
  'toChanged', 'valueChanged', 'stepSizeChanged', 'editableChanged',
  'liveChanged', 'validatorChanged', 'textFromValueChanged',
  'valueFromTextChanged', 'valueModified', 'inputMethodHintsChanged',
  'inputMethodComposingChanged', 'wrapChanged', 'displayTextChanged',
  'focusInEvent', 'hoverEnterEvent', 'hoverMoveEvent', 'hoverLeaveEvent',
  'keyPressEvent', 'keyReleaseEvent', 'timerEvent', 'wheelEvent',
  'classBegin', 'componentComplete', 'itemChange', 'contentItemChange',
  'localeChange', 'defaultFont', 'accessibleRole',
  'accessibilityActiveChanged', 'd_base_func'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSpinBox::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickSpinBox::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickSpinBox::~QQuickSpinBox()': the destructor: Python never
    removes a C++ QQuickSpinBox.
  - Qt's 'QQuickSpinBoxPrivate *QQuickSpinBox::d_func()': gives
    'QQuickSpinBoxPrivate', which has no cute class yet.
  - Qt's 'const QQuickSpinBoxPrivate *QQuickSpinBox::d_func() const': gives
    'QQuickSpinBoxPrivate', which has no cute class yet.
  - Qt's 'const QQuickControlPrivate *QQuickSpinBox::d_base_func() const':
    takes in Python what 'QQuickControlPrivate *QQuickSpinBox::d_base_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 55 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickSpinBox is created at the first use, not by
    'QQuickSpinBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSpinBox.
  - Qt tells when it has removed the C++ QQuickSpinBox. Every call on the
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
    Calls Qt's 'QString QQuickSpinBox::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#tr

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
    #  QString QQuickSpinBox::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QQuickSpinBox2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSpinBox'

  #  A C++ QQuickSpinBox Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickSpinBox'

  #  The functions Qt calls itself that QQuickSpinBox is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'increase': (
          ('_ZN13QQuickSpinBox8increaseEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'decrease': (
          ('_ZN13QQuickSpinBox8decreaseEv',
           ('nothing', 'nothing', ''),
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
    Calls Qt's 'const QMetaObject *QQuickSpinBox::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSpinBox::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QQuickSpinBox10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isLive(self) -> bool:
    """
    Calls Qt's 'bool QQuickSpinBox::isLive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#isLive
    """
    #  bool QQuickSpinBox::isLive() const
    return self.uglySide.call('ritual_ZNK13QQuickSpinBox6isLiveEv')

  def textFromValue(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQuickSpinBox::textFromValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#textFromValue

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQuickSpinBox::textFromValue() const
    address = self.uglySide.call(
        'ritual_ZNK13QQuickSpinBox13textFromValueEv',
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def valueFromText(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQuickSpinBox::valueFromText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#valueFromText

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQuickSpinBox::valueFromText() const
    address = self.uglySide.call(
        'ritual_ZNK13QQuickSpinBox13valueFromTextEv',
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickSpinBox::defaultFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickSpinBox::defaultFont() const
    ritual = 'ritual_ZNK13QQuickSpinBox11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQuickSpinBox11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickSpinBox::accessibleRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickSpinBox::accessibleRole() const
    ritual = 'ritual_ZNK13QQuickSpinBox14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQuickSpinBox14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setFrom(self, from_: int) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::setFrom(int from)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#setFrom

    Parameters
    ----------

    from_ : int
      Passed on as it is.
    """
    #  void QQuickSpinBox::setFrom(int from)
    self.uglySide.call('ritual_ZN13QQuickSpinBox7setFromEi', from_)

  @overload(int)
  def setTo(self, to: int) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::setTo(int to)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#setTo

    Parameters
    ----------

    to : int
      Passed on as it is.
    """
    #  void QQuickSpinBox::setTo(int to)
    self.uglySide.call('ritual_ZN13QQuickSpinBox5setToEi', to)

  @overload(int)
  def setValue(self, value: int) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::setValue(int value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#setValue

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QQuickSpinBox::setValue(int value)
    self.uglySide.call('ritual_ZN13QQuickSpinBox8setValueEi', value)

  @overload(int)
  def setStepSize(self, step: int) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::setStepSize(int step)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#setStepSize

    Parameters
    ----------

    step : int
      Passed on as it is.
    """
    #  void QQuickSpinBox::setStepSize(int step)
    self.uglySide.call('ritual_ZN13QQuickSpinBox11setStepSizeEi', step)

  @overload(bool)
  def setLive(self, live: bool) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::setLive(bool live)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#setLive

    Parameters
    ----------

    live : bool
      Passed on as it is.
    """
    #  void QQuickSpinBox::setLive(bool live)
    self.uglySide.call('ritual_ZN13QQuickSpinBox7setLiveEb', live)

  @overload(bool)
  def setWrap(self, wrap: bool) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::setWrap(bool wrap)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#setWrap

    Parameters
    ----------

    wrap : bool
      Passed on as it is.
    """
    #  void QQuickSpinBox::setWrap(bool wrap)
    self.uglySide.call('ritual_ZN13QQuickSpinBox7setWrapEb', wrap)

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
    Notes what was given, for Qt's 'QQuickSpinBox::QQuickSpinBox(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#QQuickSpinBox

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSpinBox::QQuickSpinBox(QQuickItem *parent)
    self._noteCreation(QQuickSpinBox, lambda: Rituals.call(
        'ritual_ZN13QQuickSpinBoxC1EP10QQuickItem', self._addressOf(parent),
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

  def increase(self) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::increase()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#increase
    """
    #  void QQuickSpinBox::increase()
    ritual = 'ritual_ZN13QQuickSpinBox8increaseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickSpinBox8increaseEv'
    self.uglySide.call(ritual)

  def decrease(self) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::decrease()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#decrease
    """
    #  void QQuickSpinBox::decrease()
    ritual = 'ritual_ZN13QQuickSpinBox8decreaseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickSpinBox8decreaseEv'
    self.uglySide.call(ritual)

  def fromChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::fromChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#fromChanged
    """
    #  void QQuickSpinBox::fromChanged()
    self.uglySide.call('ritual_ZN13QQuickSpinBox11fromChangedEv')

  def toChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::toChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#toChanged
    """
    #  void QQuickSpinBox::toChanged()
    self.uglySide.call('ritual_ZN13QQuickSpinBox9toChangedEv')

  def valueChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::valueChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#valueChanged
    """
    #  void QQuickSpinBox::valueChanged()
    self.uglySide.call('ritual_ZN13QQuickSpinBox12valueChangedEv')

  def stepSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::stepSizeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#stepSizeChanged
    """
    #  void QQuickSpinBox::stepSizeChanged()
    self.uglySide.call('ritual_ZN13QQuickSpinBox15stepSizeChangedEv')

  def editableChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::editableChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#editableChanged
    """
    #  void QQuickSpinBox::editableChanged()
    self.uglySide.call('ritual_ZN13QQuickSpinBox15editableChangedEv')

  def liveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::liveChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#liveChanged
    """
    #  void QQuickSpinBox::liveChanged()
    self.uglySide.call('ritual_ZN13QQuickSpinBox11liveChangedEv')

  def validatorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::validatorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspinbox.html#validatorChanged
    """
    #  void QQuickSpinBox::validatorChanged()
    self.uglySide.call('ritual_ZN13QQuickSpinBox16validatorChangedEv')

  def textFromValueChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::textFromValueChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspinbox.html#textFromValueChanged
    """
    #  void QQuickSpinBox::textFromValueChanged()
    self.uglySide.call('ritual_ZN13QQuickSpinBox20textFromValueChangedEv')

  def valueFromTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::valueFromTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspinbox.html#valueFromTextChanged
    """
    #  void QQuickSpinBox::valueFromTextChanged()
    self.uglySide.call('ritual_ZN13QQuickSpinBox20valueFromTextChangedEv')

  def valueModified(self) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::valueModified()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#valueModified
    """
    #  void QQuickSpinBox::valueModified()
    self.uglySide.call('ritual_ZN13QQuickSpinBox13valueModifiedEv')

  def inputMethodHintsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::inputMethodHintsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspinbox.html#inputMethodHintsChanged
    """
    #  void QQuickSpinBox::inputMethodHintsChanged()
    self.uglySide.call('ritual_ZN13QQuickSpinBox23inputMethodHintsChangedEv')

  def inputMethodComposingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::inputMethodComposingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspinbox.html#inputMethodComposingChanged
    """
    #  void QQuickSpinBox::inputMethodComposingChanged()
    self.uglySide.call(
        'ritual_ZN13QQuickSpinBox27inputMethodComposingChangedEv',
    )

  def wrapChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::wrapChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#wrapChanged
    """
    #  void QQuickSpinBox::wrapChanged()
    self.uglySide.call('ritual_ZN13QQuickSpinBox11wrapChangedEv')

  def displayTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::displayTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspinbox.html#displayTextChanged
    """
    #  void QQuickSpinBox::displayTextChanged()
    self.uglySide.call('ritual_ZN13QQuickSpinBox18displayTextChangedEv')

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::focusInEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSpinBox::focusInEvent(QFocusEvent *event)
    ritual = 'ritual_ZN13QQuickSpinBox12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickSpinBox12focusInEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::hoverEnterEvent(QHoverEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSpinBox::hoverEnterEvent(QHoverEvent *event)
    ritual = 'ritual_ZN13QQuickSpinBox15hoverEnterEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickSpinBox15hoverEnterEventEP11QHoverEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::hoverMoveEvent(QHoverEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSpinBox::hoverMoveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN13QQuickSpinBox14hoverMoveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickSpinBox14hoverMoveEventEP11QHoverEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::hoverLeaveEvent(QHoverEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSpinBox::hoverLeaveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN13QQuickSpinBox15hoverLeaveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickSpinBox15hoverLeaveEventEP11QHoverEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::keyPressEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSpinBox::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN13QQuickSpinBox13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickSpinBox13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::keyReleaseEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSpinBox::keyReleaseEvent(QKeyEvent *event)
    ritual = 'ritual_ZN13QQuickSpinBox15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickSpinBox15keyReleaseEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSpinBox::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN13QQuickSpinBox10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickSpinBox10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::wheelEvent(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSpinBox::wheelEvent(QWheelEvent *event)
    ritual = 'ritual_ZN13QQuickSpinBox10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickSpinBox10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#classBegin
    """
    #  void QQuickSpinBox::classBegin()
    ritual = 'ritual_ZN13QQuickSpinBox10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickSpinBox10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspinbox.html#componentComplete
    """
    #  void QQuickSpinBox::componentComplete()
    ritual = 'ritual_ZN13QQuickSpinBox17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickSpinBox17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickSpinBox::itemChange(ItemChange change, const ItemChangeData
    #      &value)
    ritual = (
        'ritual_ZN13QQuickSpinBox10itemChangeEN10QQuickItem10ItemChangeERKN'
        'S0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QQuickSpinBox10itemChangeEN10QQuickItem10ItemChan'
          'geERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

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
    Calls Qt's 'void QQuickSpinBox::contentItemChange(QQuickItem *newItem,
    QQuickItem *oldItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspinbox.html#contentItemChange

    Parameters
    ----------

    newItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSpinBox::contentItemChange(QQuickItem *newItem, QQuickItem
    #      *oldItem)
    ritual = 'ritual_ZN13QQuickSpinBox17contentItemChangeEP10QQuickItemS1_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QQuickSpinBox17contentItemChangeEP10QQuickItemS1_')
    self.uglySide.call(
        ritual, self._addressOf(newItem), self._addressOf(oldItem),
    )

  @overload(QLocale, QLocale)
  def localeChange(self, newLocale: QLocale, oldLocale: QLocale) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::localeChange(const QLocale &newLocale,
    const QLocale &oldLocale)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#localeChange

    Parameters
    ----------

    newLocale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    oldLocale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QQuickSpinBox::localeChange(const QLocale &newLocale, const
    #      QLocale &oldLocale)
    ritual = 'ritual_ZN13QQuickSpinBox12localeChangeERK7QLocaleS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickSpinBox12localeChangeERK7QLocaleS2_'
    self.uglySide.call(
        ritual, self._valueOf(newLocale), self._valueOf(oldLocale),
    )

  @overload(bool)
  def accessibilityActiveChanged(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickSpinBox::accessibilityActiveChanged(bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickspinbox.html#accessibilityActiveChanged

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickSpinBox::accessibilityActiveChanged(bool active)
    ritual = 'ritual_ZN13QQuickSpinBox26accessibilityActiveChangedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickSpinBox26accessibilityActiveChangedEb'
    self.uglySide.call(ritual, active)

  def d_base_func(self) -> Optional[QQuickControlPrivate]:
    """
    Calls Qt's 'QQuickControlPrivate *QQuickSpinBox::d_base_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickspinbox.html#d_base_func

    Returns
    -------

    Optional[QQuickControlPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickControlPrivate *QQuickSpinBox::d_base_func()
    address = self.uglySide.call('ritual_ZN13QQuickSpinBox11d_base_funcEv')
    from . import QQuickControlPrivate
    return QQuickControlPrivate._cuteAt(address)
