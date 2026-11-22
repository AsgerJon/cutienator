"""
QInputDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qinputdialog.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QDialog, QLineEdit, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSize

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QInputDialog(QDialog):
  """
  The cute side of Qt's QInputDialog: a plain Python object standing in front
  of one C++ QInputDialog.

  It is built on the cute 'QDialog', as Qt's QInputDialog is built on Qt's
  QDialog, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QInputDialog that has a ritual and that Python can
  call so far, 45 names in all: 'metaObject', 'tr', 'setInputMode',
  'inputMode', 'setLabelText', 'labelText', 'setOption', 'testOption',
  'setOptions', 'options', 'setTextValue', 'textValue', 'setTextEchoMode',
  'textEchoMode', 'setComboBoxEditable', 'isComboBoxEditable', 'setIntValue',
  'intValue', 'setIntMinimum', 'intMinimum', 'setIntMaximum', 'intMaximum',
  'setIntRange', 'setIntStep', 'intStep', 'setDoubleValue', 'doubleValue',
  'setDoubleMinimum', 'doubleMinimum', 'setDoubleMaximum', 'doubleMaximum',
  'setDoubleRange', 'setDoubleDecimals', 'doubleDecimals', 'setOkButtonText',
  'okButtonText', 'setCancelButtonText', 'cancelButtonText', 'open',
  'minimumSizeHint', 'sizeHint', 'setVisible', 'setDoubleStep', 'doubleStep',
  'done'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QInputDialog::~QInputDialog()': the destructor: Python never
    removes a C++ QInputDialog.
  - Qt's 'QString QInputDialog::getText(QWidget *parent, const QString
    &title, const QString &label, QLineEdit::EchoMode echo, const QString
    &text, bool *ok, Qt::WindowFlags flags, Qt::InputMethodHints
    inputMethodHints)': takes a number to change where it is.
  - Qt's 'QString QInputDialog::getMultiLineText(QWidget *parent, const
    QString &title, const QString &label, const QString &text, bool *ok,
    Qt::WindowFlags flags, Qt::InputMethodHints inputMethodHints)': takes a
    number to change where it is.
  - Qt's 'int QInputDialog::getInt(QWidget *parent, const QString &title,
    const QString &label, int value, int minValue, int maxValue, int step,
    bool *ok, Qt::WindowFlags flags)': takes a number to change where it is.
  - Qt's 'double QInputDialog::getDouble(QWidget *parent, const QString
    &title, const QString &label, double value, double minValue, double
    maxValue, int decimals, bool *ok, Qt::WindowFlags flags, double step)':
    takes a number to change where it is.

  What has no ritual
  ------------------

  17 of the 68 functions Qt declares: 6 a signal; 5 takes or gives a type
  that cannot be passed yet; 3 private; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QInputDialog is created at the first use, not by
    'QInputDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QInputDialog.
  - Qt tells when it has removed the C++ QInputDialog. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QInputDialog, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class InputDialogOption(CuteFlags):
    """
    The flags enum 'QInputDialog::InputDialogOption' of Qt, with the 3 names
    Qt gives in it. Qt names the type of its combinations
    'QInputDialog::InputDialogOptions'.
    """

    NoButtons = 0x1
    UseListViewForComboBoxItems = 0x2
    UsePlainTextEditForTextInput = 0x4

  InputDialogOptions = InputDialogOption

  class InputMode(CuteNum):
    """
    The enum 'QInputDialog::InputMode' of Qt, with the 3 names Qt gives in
    it.
    """

    TextInput = Kee[int](0)
    IntInput = Kee[int](1)
    DoubleInput = Kee[int](2)

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
    Calls Qt's 'QString QInputDialog::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#tr

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
    #  QString QInputDialog::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QInputDialog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QInputDialog'

  #  A C++ QInputDialog Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QInputDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QInputDialog::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QInputDialog::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QInputDialog10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def inputMode(self) -> InputMode:
    """
    Calls Qt's 'InputMode QInputDialog::inputMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#inputMode

    Returns
    -------

    InputMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'InputMode(number)' gives.
    """
    #  InputMode QInputDialog::inputMode() const
    return QInputDialog.InputMode(self.uglySide.call(
        'ritual_ZNK12QInputDialog9inputModeEv',
    ))

  def labelText(self) -> str:
    """
    Calls Qt's 'QString QInputDialog::labelText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#labelText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QInputDialog::labelText() const
    return self.uglySide.call('ritual_ZNK12QInputDialog9labelTextEv')

  @overload(InputDialogOption)
  def testOption(self, option: InputDialogOption) -> bool:
    """
    Calls Qt's 'bool QInputDialog::testOption(InputDialogOption option)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#testOption

    Parameters
    ----------

    option : InputDialogOption
      Passed on as its number.
    """
    #  bool QInputDialog::testOption(InputDialogOption option) const
    return self.uglySide.call(
        'ritual_ZNK12QInputDialog10testOptionENS_17InputDialogOptionE',
        option.value,
    )

  def options(self) -> InputDialogOptions:
    """
    Calls Qt's 'InputDialogOptions QInputDialog::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#options

    Returns
    -------

    InputDialogOptions
      The value standing for the combination Qt gave back.
    """
    #  InputDialogOptions QInputDialog::options() const
    return QInputDialog.InputDialogOptions(self.uglySide.call(
        'ritual_ZNK12QInputDialog7optionsEv',
    ))

  def textValue(self) -> str:
    """
    Calls Qt's 'QString QInputDialog::textValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#textValue

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QInputDialog::textValue() const
    return self.uglySide.call('ritual_ZNK12QInputDialog9textValueEv')

  def textEchoMode(self) -> QLineEdit.EchoMode:
    """
    Calls Qt's 'QLineEdit::EchoMode QInputDialog::textEchoMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#textEchoMode

    Returns
    -------

    QLineEdit.EchoMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QLineEdit.EchoMode(number)' gives.
    """
    #  QLineEdit::EchoMode QInputDialog::textEchoMode() const
    return QLineEdit.EchoMode(self.uglySide.call(
        'ritual_ZNK12QInputDialog12textEchoModeEv',
    ))

  def isComboBoxEditable(self) -> bool:
    """
    Calls Qt's 'bool QInputDialog::isComboBoxEditable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputdialog.html#isComboBoxEditable
    """
    #  bool QInputDialog::isComboBoxEditable() const
    return self.uglySide.call(
        'ritual_ZNK12QInputDialog18isComboBoxEditableEv',
    )

  def intValue(self) -> int:
    """
    Calls Qt's 'int QInputDialog::intValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#intValue
    """
    #  int QInputDialog::intValue() const
    return self.uglySide.call('ritual_ZNK12QInputDialog8intValueEv')

  def intMinimum(self) -> int:
    """
    Calls Qt's 'int QInputDialog::intMinimum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#intMinimum
    """
    #  int QInputDialog::intMinimum() const
    return self.uglySide.call('ritual_ZNK12QInputDialog10intMinimumEv')

  def intMaximum(self) -> int:
    """
    Calls Qt's 'int QInputDialog::intMaximum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#intMaximum
    """
    #  int QInputDialog::intMaximum() const
    return self.uglySide.call('ritual_ZNK12QInputDialog10intMaximumEv')

  def intStep(self) -> int:
    """
    Calls Qt's 'int QInputDialog::intStep() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#intStep
    """
    #  int QInputDialog::intStep() const
    return self.uglySide.call('ritual_ZNK12QInputDialog7intStepEv')

  def doubleValue(self) -> float:
    """
    Calls Qt's 'double QInputDialog::doubleValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#doubleValue
    """
    #  double QInputDialog::doubleValue() const
    return self.uglySide.call('ritual_ZNK12QInputDialog11doubleValueEv')

  def doubleMinimum(self) -> float:
    """
    Calls Qt's 'double QInputDialog::doubleMinimum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#doubleMinimum
    """
    #  double QInputDialog::doubleMinimum() const
    return self.uglySide.call('ritual_ZNK12QInputDialog13doubleMinimumEv')

  def doubleMaximum(self) -> float:
    """
    Calls Qt's 'double QInputDialog::doubleMaximum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#doubleMaximum
    """
    #  double QInputDialog::doubleMaximum() const
    return self.uglySide.call('ritual_ZNK12QInputDialog13doubleMaximumEv')

  def doubleDecimals(self) -> int:
    """
    Calls Qt's 'int QInputDialog::doubleDecimals() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#doubleDecimals
    """
    #  int QInputDialog::doubleDecimals() const
    return self.uglySide.call('ritual_ZNK12QInputDialog14doubleDecimalsEv')

  def okButtonText(self) -> str:
    """
    Calls Qt's 'QString QInputDialog::okButtonText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#okButtonText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QInputDialog::okButtonText() const
    return self.uglySide.call('ritual_ZNK12QInputDialog12okButtonTextEv')

  def cancelButtonText(self) -> str:
    """
    Calls Qt's 'QString QInputDialog::cancelButtonText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#cancelButtonText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QInputDialog::cancelButtonText() const
    return self.uglySide.call('ritual_ZNK12QInputDialog16cancelButtonTextEv')

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QInputDialog::minimumSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QInputDialog::minimumSizeHint() const
    ritual = 'ritual_ZNK12QInputDialog15minimumSizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QInputDialog15minimumSizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QInputDialog::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QInputDialog::sizeHint() const
    ritual = 'ritual_ZNK12QInputDialog8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QInputDialog8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def doubleStep(self) -> float:
    """
    Calls Qt's 'double QInputDialog::doubleStep() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#doubleStep
    """
    #  double QInputDialog::doubleStep() const
    return self.uglySide.call('ritual_ZNK12QInputDialog10doubleStepEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(InputMode)
  def setInputMode(self, mode: InputMode) -> None:
    """
    Calls Qt's 'void QInputDialog::setInputMode(InputMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#setInputMode

    Parameters
    ----------

    mode : InputMode
      Passed on as its number.
    """
    #  void QInputDialog::setInputMode(InputMode mode)
    self.uglySide.call(
        'ritual_ZN12QInputDialog12setInputModeENS_9InputModeE', mode.value,
    )

  @overload(str)
  def setLabelText(self, text: str) -> None:
    """
    Calls Qt's 'void QInputDialog::setLabelText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#setLabelText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QInputDialog::setLabelText(const QString &text)
    self.uglySide.call(
        'ritual_ZN12QInputDialog12setLabelTextERK7QString', text,
    )

  @overload(InputDialogOption)
  @overload(InputDialogOption, bool)
  def setOption(self, option: InputDialogOption, on: bool = True) -> None:
    """
    Calls Qt's 'void QInputDialog::setOption(InputDialogOption option, bool
    on)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#setOption

    Parameters
    ----------

    option : InputDialogOption
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QInputDialog::setOption(InputDialogOption option, bool on)
    self.uglySide.call(
        'ritual_ZN12QInputDialog9setOptionENS_17InputDialogOptionEb',
        option.value, on,
    )

  @overload(InputDialogOptions)
  def setOptions(self, options: InputDialogOptions) -> None:
    """
    Calls Qt's 'void QInputDialog::setOptions(InputDialogOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#setOptions

    Parameters
    ----------

    options : InputDialogOptions
      Passed on as its number.
    """
    #  void QInputDialog::setOptions(InputDialogOptions options)
    self.uglySide.call(
        'ritual_ZN12QInputDialog10setOptionsE6QFlagsINS_17InputDialogOption'
        'EE',
        options.value,
    )

  @overload(str)
  def setTextValue(self, text: str) -> None:
    """
    Calls Qt's 'void QInputDialog::setTextValue(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#setTextValue

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QInputDialog::setTextValue(const QString &text)
    self.uglySide.call(
        'ritual_ZN12QInputDialog12setTextValueERK7QString', text,
    )

  @overload(QLineEdit.EchoMode)
  def setTextEchoMode(self, mode: QLineEdit.EchoMode) -> None:
    """
    Calls Qt's 'void QInputDialog::setTextEchoMode(QLineEdit::EchoMode
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#setTextEchoMode

    Parameters
    ----------

    mode : QLineEdit.EchoMode
      Passed on as its number.
    """
    #  void QInputDialog::setTextEchoMode(QLineEdit::EchoMode mode)
    self.uglySide.call(
        'ritual_ZN12QInputDialog15setTextEchoModeEN9QLineEdit8EchoModeE',
        mode.value,
    )

  @overload(bool)
  def setComboBoxEditable(self, editable: bool) -> None:
    """
    Calls Qt's 'void QInputDialog::setComboBoxEditable(bool editable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputdialog.html#setComboBoxEditable

    Parameters
    ----------

    editable : bool
      Passed on as it is.
    """
    #  void QInputDialog::setComboBoxEditable(bool editable)
    self.uglySide.call(
        'ritual_ZN12QInputDialog19setComboBoxEditableEb', editable,
    )

  @overload(int)
  def setIntValue(self, value: int) -> None:
    """
    Calls Qt's 'void QInputDialog::setIntValue(int value)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#setIntValue

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QInputDialog::setIntValue(int value)
    self.uglySide.call('ritual_ZN12QInputDialog11setIntValueEi', value)

  @overload(int)
  def setIntMinimum(self, min: int) -> None:
    """
    Calls Qt's 'void QInputDialog::setIntMinimum(int min)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#setIntMinimum

    Parameters
    ----------

    min : int
      Passed on as it is.
    """
    #  void QInputDialog::setIntMinimum(int min)
    self.uglySide.call('ritual_ZN12QInputDialog13setIntMinimumEi', min)

  @overload(int)
  def setIntMaximum(self, max: int) -> None:
    """
    Calls Qt's 'void QInputDialog::setIntMaximum(int max)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#setIntMaximum

    Parameters
    ----------

    max : int
      Passed on as it is.
    """
    #  void QInputDialog::setIntMaximum(int max)
    self.uglySide.call('ritual_ZN12QInputDialog13setIntMaximumEi', max)

  @overload(int, int)
  def setIntRange(self, min: int, max: int) -> None:
    """
    Calls Qt's 'void QInputDialog::setIntRange(int min, int max)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#setIntRange

    Parameters
    ----------

    min : int
      Passed on as it is.

    max : int
      Passed on as it is.
    """
    #  void QInputDialog::setIntRange(int min, int max)
    self.uglySide.call('ritual_ZN12QInputDialog11setIntRangeEii', min, max)

  @overload(int)
  def setIntStep(self, step: int) -> None:
    """
    Calls Qt's 'void QInputDialog::setIntStep(int step)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#setIntStep

    Parameters
    ----------

    step : int
      Passed on as it is.
    """
    #  void QInputDialog::setIntStep(int step)
    self.uglySide.call('ritual_ZN12QInputDialog10setIntStepEi', step)

  @overload(float)
  def setDoubleValue(self, value: float) -> None:
    """
    Calls Qt's 'void QInputDialog::setDoubleValue(double value)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#setDoubleValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QInputDialog::setDoubleValue(double value)
    self.uglySide.call('ritual_ZN12QInputDialog14setDoubleValueEd', value)

  @overload(float)
  def setDoubleMinimum(self, min: float) -> None:
    """
    Calls Qt's 'void QInputDialog::setDoubleMinimum(double min)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#setDoubleMinimum

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void QInputDialog::setDoubleMinimum(double min)
    self.uglySide.call('ritual_ZN12QInputDialog16setDoubleMinimumEd', min)

  @overload(float)
  def setDoubleMaximum(self, max: float) -> None:
    """
    Calls Qt's 'void QInputDialog::setDoubleMaximum(double max)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#setDoubleMaximum

    Parameters
    ----------

    max : float
      Passed on as it is.
    """
    #  void QInputDialog::setDoubleMaximum(double max)
    self.uglySide.call('ritual_ZN12QInputDialog16setDoubleMaximumEd', max)

  @overload(float, float)
  def setDoubleRange(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QInputDialog::setDoubleRange(double min, double max)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#setDoubleRange

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QInputDialog::setDoubleRange(double min, double max)
    self.uglySide.call(
        'ritual_ZN12QInputDialog14setDoubleRangeEdd', min, max,
    )

  @overload(int)
  def setDoubleDecimals(self, decimals: int) -> None:
    """
    Calls Qt's 'void QInputDialog::setDoubleDecimals(int decimals)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputdialog.html#setDoubleDecimals

    Parameters
    ----------

    decimals : int
      Passed on as it is.
    """
    #  void QInputDialog::setDoubleDecimals(int decimals)
    self.uglySide.call(
        'ritual_ZN12QInputDialog17setDoubleDecimalsEi', decimals,
    )

  @overload(str)
  def setOkButtonText(self, text: str) -> None:
    """
    Calls Qt's 'void QInputDialog::setOkButtonText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#setOkButtonText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QInputDialog::setOkButtonText(const QString &text)
    self.uglySide.call(
        'ritual_ZN12QInputDialog15setOkButtonTextERK7QString', text,
    )

  @overload(str)
  def setCancelButtonText(self, text: str) -> None:
    """
    Calls Qt's 'void QInputDialog::setCancelButtonText(const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputdialog.html#setCancelButtonText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QInputDialog::setCancelButtonText(const QString &text)
    self.uglySide.call(
        'ritual_ZN12QInputDialog19setCancelButtonTextERK7QString', text,
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QInputDialog::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QInputDialog::setVisible(bool visible)
    ritual = 'ritual_ZN12QInputDialog10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QInputDialog10setVisibleEb'
    self.uglySide.call(ritual, visible)

  @overload(float)
  def setDoubleStep(self, step: float) -> None:
    """
    Calls Qt's 'void QInputDialog::setDoubleStep(double step)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#setDoubleStep

    Parameters
    ----------

    step : float
      Passed on as it is.
    """
    #  void QInputDialog::setDoubleStep(double step)
    self.uglySide.call('ritual_ZN12QInputDialog13setDoubleStepEd', step)

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
  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def __init__(
      self,
      parent: Optional[QWidget] = None,
      flags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's 'QInputDialog::QInputDialog(QWidget
    *parent, Qt::WindowFlags flags)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#QInputDialog

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    flags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QInputDialog::QInputDialog(QWidget *parent, Qt::WindowFlags flags)
    self._noteCreation(QInputDialog, lambda: Rituals.call(
        'ritual_ZN12QInputDialogC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE',
        self._addressOf(parent), flags.value,
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

  @overload(QObject, str)
  @overload(QObject, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def open(self, receiver: Optional[QObject], member: Optional[str]) -> None:
    """
    Calls Qt's 'void QInputDialog::open(QObject *receiver, const char
    *member)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#open

    Parameters
    ----------

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QInputDialog::open(QObject *receiver, const char *member)
    self.uglySide.call(
        'ritual_ZN12QInputDialog4openEP7QObjectPKc',
        self._addressOf(receiver), self._bytesOf(member),
    )

  @overload(int)
  def done(self, result: int) -> None:
    """
    Calls Qt's 'void QInputDialog::done(int result)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdialog.html#done

    Parameters
    ----------

    result : int
      Passed on as it is.
    """
    #  void QInputDialog::done(int result)
    ritual = 'ritual_ZN12QInputDialog4doneEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QInputDialog4doneEi'
    self.uglySide.call(ritual, result)
