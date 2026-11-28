"""
QQuickDoubleSpinBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdoublespinbox_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickDoubleSpinBox to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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


class QQuickDoubleSpinBox(QQuickControl):
  """
  The cute side of Qt's QQuickDoubleSpinBox: a plain Python object standing
  in front of one C++ QQuickDoubleSpinBox.

  It is built on the cute 'QQuickControl', as Qt's QQuickDoubleSpinBox is
  built on Qt's QQuickControl, and has everything that class has. Qt's
  QQuickDoubleSpinBox is built on Qt's
  QQuickAbstractSpinBox<QQuickDoubleSpinBox, double> as well, which is not
  reflected.

  What exists
  -----------

  Every function of Qt's QQuickDoubleSpinBox that has a ritual and that
  Python can call so far, 44 names in all: 'metaObject', 'tr', 'setFrom',
  'setTo', 'setValue', 'setStepSize', 'decimals', 'setDecimals',
  'textFromValue', 'valueFromText', 'setWrap', 'increase', 'decrease',
  'fromChanged', 'toChanged', 'valueChanged', 'stepSizeChanged',
  'decimalsChanged', 'editableChanged', 'validatorChanged',
  'textFromValueChanged', 'valueFromTextChanged', 'valueModified',
  'inputMethodHintsChanged', 'inputMethodComposingChanged', 'wrapChanged',
  'displayTextChanged', 'focusInEvent', 'hoverEnterEvent', 'hoverMoveEvent',
  'hoverLeaveEvent', 'keyPressEvent', 'keyReleaseEvent', 'timerEvent',
  'wheelEvent', 'classBegin', 'componentComplete', 'itemChange',
  'contentItemChange', 'localeChange', 'defaultFont', 'accessibleRole',
  'accessibilityActiveChanged', 'd_base_func'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickDoubleSpinBox::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickDoubleSpinBox::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickDoubleSpinBox::~QQuickDoubleSpinBox()': the destructor:
    Python never removes a C++ QQuickDoubleSpinBox.
  - Qt's 'QQuickDoubleSpinBoxPrivate *QQuickDoubleSpinBox::d_func()': gives
    'QQuickDoubleSpinBoxPrivate', which has no cute class yet.
  - Qt's 'const QQuickDoubleSpinBoxPrivate *QQuickDoubleSpinBox::d_func()
    const': gives 'QQuickDoubleSpinBoxPrivate', which has no cute class yet.
  - Qt's 'const QQuickControlPrivate *QQuickDoubleSpinBox::d_base_func()
    const': takes in Python what 'QQuickControlPrivate
    *QQuickDoubleSpinBox::d_base_func()' takes.

  What has no ritual
  ------------------

  4 of the 55 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickDoubleSpinBox is created at the first use, not by
    'QQuickDoubleSpinBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDoubleSpinBox.
  - Qt tells when it has removed the C++ QQuickDoubleSpinBox. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickDoubleSpinBox::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdoublespinbox.html#tr

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
    #  QString QQuickDoubleSpinBox::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickDoubleSpinBox2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDoubleSpinBox'

  #  A C++ QQuickDoubleSpinBox Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickDoubleSpinBox'

  #  The functions Qt calls itself that QQuickDoubleSpinBox is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'increase': (
          ('_ZN19QQuickDoubleSpinBox8increaseEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'decrease': (
          ('_ZN19QQuickDoubleSpinBox8decreaseEv',
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
    Calls Qt's 'const QMetaObject *QQuickDoubleSpinBox::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickDoubleSpinBox::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickDoubleSpinBox10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def decimals(self) -> int:
    """
    Calls Qt's 'int QQuickDoubleSpinBox::decimals() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdoublespinbox.html#decimals
    """
    #  int QQuickDoubleSpinBox::decimals() const
    return self.uglySide.call('ritual_ZNK19QQuickDoubleSpinBox8decimalsEv')

  def textFromValue(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQuickDoubleSpinBox::textFromValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#textFromValue

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQuickDoubleSpinBox::textFromValue() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickDoubleSpinBox13textFromValueEv',
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def valueFromText(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQuickDoubleSpinBox::valueFromText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#valueFromText

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQuickDoubleSpinBox::valueFromText() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickDoubleSpinBox13valueFromTextEv',
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickDoubleSpinBox::defaultFont() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickDoubleSpinBox::defaultFont() const
    ritual = 'ritual_ZNK19QQuickDoubleSpinBox11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickDoubleSpinBox11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickDoubleSpinBox::accessibleRole()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickDoubleSpinBox::accessibleRole() const
    ritual = 'ritual_ZNK19QQuickDoubleSpinBox14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickDoubleSpinBox14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setFrom(self, from_: float) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::setFrom(double from)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdoublespinbox.html#setFrom

    Parameters
    ----------

    from_ : float
      Passed on as it is.
    """
    #  void QQuickDoubleSpinBox::setFrom(double from)
    self.uglySide.call('ritual_ZN19QQuickDoubleSpinBox7setFromEd', from_)

  @overload(float)
  def setTo(self, to: float) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::setTo(double to)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdoublespinbox.html#setTo

    Parameters
    ----------

    to : float
      Passed on as it is.
    """
    #  void QQuickDoubleSpinBox::setTo(double to)
    self.uglySide.call('ritual_ZN19QQuickDoubleSpinBox5setToEd', to)

  @overload(float)
  def setValue(self, value: float) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::setValue(double value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdoublespinbox.html#setValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QQuickDoubleSpinBox::setValue(double value)
    self.uglySide.call('ritual_ZN19QQuickDoubleSpinBox8setValueEd', value)

  @overload(float)
  def setStepSize(self, step: float) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::setStepSize(double step)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#setStepSize

    Parameters
    ----------

    step : float
      Passed on as it is.
    """
    #  void QQuickDoubleSpinBox::setStepSize(double step)
    self.uglySide.call('ritual_ZN19QQuickDoubleSpinBox11setStepSizeEd', step)

  @overload(int)
  def setDecimals(self, prec: int) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::setDecimals(int prec)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#setDecimals

    Parameters
    ----------

    prec : int
      Passed on as it is.
    """
    #  void QQuickDoubleSpinBox::setDecimals(int prec)
    self.uglySide.call('ritual_ZN19QQuickDoubleSpinBox11setDecimalsEi', prec)

  @overload(bool)
  def setWrap(self, wrap: bool) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::setWrap(bool wrap)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdoublespinbox.html#setWrap

    Parameters
    ----------

    wrap : bool
      Passed on as it is.
    """
    #  void QQuickDoubleSpinBox::setWrap(bool wrap)
    self.uglySide.call('ritual_ZN19QQuickDoubleSpinBox7setWrapEb', wrap)

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
    'QQuickDoubleSpinBox::QQuickDoubleSpinBox(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#QQuickDoubleSpinBox

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickDoubleSpinBox::QQuickDoubleSpinBox(QQuickItem *parent)
    self._noteCreation(QQuickDoubleSpinBox, lambda: Rituals.call(
        'ritual_ZN19QQuickDoubleSpinBoxC1EP10QQuickItem',
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

  def increase(self) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::increase()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdoublespinbox.html#increase
    """
    #  void QQuickDoubleSpinBox::increase()
    ritual = 'ritual_ZN19QQuickDoubleSpinBox8increaseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickDoubleSpinBox8increaseEv'
    self.uglySide.call(ritual)

  def decrease(self) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::decrease()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdoublespinbox.html#decrease
    """
    #  void QQuickDoubleSpinBox::decrease()
    ritual = 'ritual_ZN19QQuickDoubleSpinBox8decreaseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickDoubleSpinBox8decreaseEv'
    self.uglySide.call(ritual)

  def fromChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::fromChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#fromChanged
    """
    #  void QQuickDoubleSpinBox::fromChanged()
    self.uglySide.call('ritual_ZN19QQuickDoubleSpinBox11fromChangedEv')

  def toChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::toChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdoublespinbox.html#toChanged
    """
    #  void QQuickDoubleSpinBox::toChanged()
    self.uglySide.call('ritual_ZN19QQuickDoubleSpinBox9toChangedEv')

  def valueChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::valueChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#valueChanged
    """
    #  void QQuickDoubleSpinBox::valueChanged()
    self.uglySide.call('ritual_ZN19QQuickDoubleSpinBox12valueChangedEv')

  def stepSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::stepSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#stepSizeChanged
    """
    #  void QQuickDoubleSpinBox::stepSizeChanged()
    self.uglySide.call('ritual_ZN19QQuickDoubleSpinBox15stepSizeChangedEv')

  def decimalsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::decimalsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#decimalsChanged
    """
    #  void QQuickDoubleSpinBox::decimalsChanged()
    self.uglySide.call('ritual_ZN19QQuickDoubleSpinBox15decimalsChangedEv')

  def editableChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::editableChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#editableChanged
    """
    #  void QQuickDoubleSpinBox::editableChanged()
    self.uglySide.call('ritual_ZN19QQuickDoubleSpinBox15editableChangedEv')

  def validatorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::validatorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#validatorChanged
    """
    #  void QQuickDoubleSpinBox::validatorChanged()
    self.uglySide.call('ritual_ZN19QQuickDoubleSpinBox16validatorChangedEv')

  def textFromValueChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::textFromValueChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#textFromValueChanged
    """
    #  void QQuickDoubleSpinBox::textFromValueChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickDoubleSpinBox20textFromValueChangedEv',
    )

  def valueFromTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::valueFromTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#valueFromTextChanged
    """
    #  void QQuickDoubleSpinBox::valueFromTextChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickDoubleSpinBox20valueFromTextChangedEv',
    )

  def valueModified(self) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::valueModified()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#valueModified
    """
    #  void QQuickDoubleSpinBox::valueModified()
    self.uglySide.call('ritual_ZN19QQuickDoubleSpinBox13valueModifiedEv')

  def inputMethodHintsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::inputMethodHintsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#inputMethodHintsChanged
    """
    #  void QQuickDoubleSpinBox::inputMethodHintsChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickDoubleSpinBox23inputMethodHintsChangedEv',
    )

  def inputMethodComposingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::inputMethodComposingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html
    """
    #  void QQuickDoubleSpinBox::inputMethodComposingChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickDoubleSpinBox27inputMethodComposingChangedEv',
    )

  def wrapChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::wrapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#wrapChanged
    """
    #  void QQuickDoubleSpinBox::wrapChanged()
    self.uglySide.call('ritual_ZN19QQuickDoubleSpinBox11wrapChangedEv')

  def displayTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::displayTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#displayTextChanged
    """
    #  void QQuickDoubleSpinBox::displayTextChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickDoubleSpinBox18displayTextChangedEv',
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::focusInEvent(QFocusEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDoubleSpinBox::focusInEvent(QFocusEvent *event)
    ritual = 'ritual_ZN19QQuickDoubleSpinBox12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickDoubleSpinBox12focusInEventEP11QFocusEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::hoverEnterEvent(QHoverEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDoubleSpinBox::hoverEnterEvent(QHoverEvent *event)
    ritual = 'ritual_ZN19QQuickDoubleSpinBox15hoverEnterEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickDoubleSpinBox15hoverEnterEventEP11QHoverEve'
          'nt')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::hoverMoveEvent(QHoverEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDoubleSpinBox::hoverMoveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN19QQuickDoubleSpinBox14hoverMoveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickDoubleSpinBox14hoverMoveEventEP11QHoverEven'
          't')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::hoverLeaveEvent(QHoverEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDoubleSpinBox::hoverLeaveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN19QQuickDoubleSpinBox15hoverLeaveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickDoubleSpinBox15hoverLeaveEventEP11QHoverEve'
          'nt')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::keyPressEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDoubleSpinBox::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN19QQuickDoubleSpinBox13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickDoubleSpinBox13keyPressEventEP9QKeyEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::keyReleaseEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDoubleSpinBox::keyReleaseEvent(QKeyEvent *event)
    ritual = 'ritual_ZN19QQuickDoubleSpinBox15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickDoubleSpinBox15keyReleaseEventEP9QKeyEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::timerEvent(QTimerEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDoubleSpinBox::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN19QQuickDoubleSpinBox10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickDoubleSpinBox10timerEventEP11QTimerEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::wheelEvent(QWheelEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDoubleSpinBox::wheelEvent(QWheelEvent *event)
    ritual = 'ritual_ZN19QQuickDoubleSpinBox10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickDoubleSpinBox10wheelEventEP11QWheelEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#classBegin
    """
    #  void QQuickDoubleSpinBox::classBegin()
    ritual = 'ritual_ZN19QQuickDoubleSpinBox10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickDoubleSpinBox10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#componentComplete
    """
    #  void QQuickDoubleSpinBox::componentComplete()
    ritual = 'ritual_ZN19QQuickDoubleSpinBox17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickDoubleSpinBox17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickDoubleSpinBox::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN19QQuickDoubleSpinBox10itemChangeEN10QQuickItem10ItemChan'
        'geERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickDoubleSpinBox10itemChangeEN10QQuickItem10It'
          'emChangeERKNS0_14ItemChangeDataE')
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
    Calls Qt's 'void QQuickDoubleSpinBox::contentItemChange(QQuickItem
    *newItem, QQuickItem *oldItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#contentItemChange

    Parameters
    ----------

    newItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDoubleSpinBox::contentItemChange(QQuickItem *newItem,
    #      QQuickItem *oldItem)
    ritual = (
        'ritual_ZN19QQuickDoubleSpinBox17contentItemChangeEP10QQuickItemS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickDoubleSpinBox17contentItemChangeEP10QQuickI'
          'temS1_')
    self.uglySide.call(
        ritual, self._addressOf(newItem), self._addressOf(oldItem),
    )

  @overload(QLocale, QLocale)
  def localeChange(self, newLocale: QLocale, oldLocale: QLocale) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::localeChange(const QLocale
    &newLocale, const QLocale &oldLocale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#localeChange

    Parameters
    ----------

    newLocale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    oldLocale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QQuickDoubleSpinBox::localeChange(const QLocale &newLocale, const
    #      QLocale &oldLocale)
    ritual = 'ritual_ZN19QQuickDoubleSpinBox12localeChangeERK7QLocaleS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickDoubleSpinBox12localeChangeERK7QLocaleS2_')
    self.uglySide.call(
        ritual, self._valueOf(newLocale), self._valueOf(oldLocale),
    )

  @overload(bool)
  def accessibilityActiveChanged(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickDoubleSpinBox::accessibilityActiveChanged(bool
    active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickDoubleSpinBox::accessibilityActiveChanged(bool active)
    ritual = 'ritual_ZN19QQuickDoubleSpinBox26accessibilityActiveChangedEb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickDoubleSpinBox26accessibilityActiveChangedEb')
    self.uglySide.call(ritual, active)

  def d_base_func(self) -> Optional[QQuickControlPrivate]:
    """
    Calls Qt's 'QQuickControlPrivate *QQuickDoubleSpinBox::d_base_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdoublespinbox.html#d_base_func

    Returns
    -------

    Optional[QQuickControlPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickControlPrivate *QQuickDoubleSpinBox::d_base_func()
    address = self.uglySide.call(
        'ritual_ZN19QQuickDoubleSpinBox11d_base_funcEv',
    )
    from . import QQuickControlPrivate
    return QQuickControlPrivate._cuteAt(address)
