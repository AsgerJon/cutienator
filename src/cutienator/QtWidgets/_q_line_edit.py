"""
QLineEdit binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qlineedit.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMargins, QMetaObject, QPoint, QSize
  from ..QtCore import QTimerEvent, QVariant
  from ..QtGui import QAction, QIcon, QValidator
  from . import QCompleter, QMenu
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QCompleter = WAIT['QCompleter']
  QEvent = WAIT['QEvent']
  QIcon = WAIT['QIcon']
  QMargins = WAIT['QMargins']
  QPoint = WAIT['QPoint']
  QTimerEvent = WAIT['QTimerEvent']
  QValidator = WAIT['QValidator']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLineEdit(QWidget):
  """
  The cute side of Qt's QLineEdit: a plain Python object standing in front of
  one C++ QLineEdit.

  It is built on the cute 'QWidget', as Qt's QLineEdit is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLineEdit that has a ritual and that Python can call
  so far, 69 names in all: 'metaObject', 'tr', 'text', 'displayText',
  'placeholderText', 'setPlaceholderText', 'maxLength', 'setMaxLength',
  'setFrame', 'hasFrame', 'setClearButtonEnabled', 'isClearButtonEnabled',
  'echoMode', 'setEchoMode', 'isReadOnly', 'setReadOnly', 'setValidator',
  'validator', 'setCompleter', 'completer', 'sizeHint', 'minimumSizeHint',
  'cursorPosition', 'setCursorPosition', 'cursorPositionAt', 'setAlignment',
  'alignment', 'cursorForward', 'cursorBackward', 'cursorWordForward',
  'cursorWordBackward', 'backspace', 'del_', 'home', 'end', 'isModified',
  'setModified', 'setSelection', 'hasSelectedText', 'selectedText',
  'selectionStart', 'selectionEnd', 'selectionLength', 'isUndoAvailable',
  'isRedoAvailable', 'setDragEnabled', 'dragEnabled', 'setCursorMoveStyle',
  'cursorMoveStyle', 'inputMask', 'setInputMask', 'hasAcceptableInput',
  'setTextMargins', 'textMargins', 'addAction', 'setText', 'clear',
  'selectAll', 'undo', 'redo', 'cut', 'copy', 'paste', 'deselect', 'insert',
  'createStandardContextMenu', 'inputMethodQuery', 'timerEvent', 'event'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLineEdit::~QLineEdit()': the destructor: Python never removes a
    C++ QLineEdit.

  What has no ritual
  ------------------

  33 of the 108 functions Qt declares: 18 protected; 7 a signal; 3 private; 2
  takes or gives a type that cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QLineEdit is created at the first use, not by 'QLineEdit(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLineEdit.
  - Qt tells when it has removed the C++ QLineEdit. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QLineEdit, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ActionPosition(CuteNum):
    """
    The enum 'QLineEdit::ActionPosition' of Qt, with the 2 names Qt gives in
    it.
    """

    LeadingPosition = Kee[int](0)
    TrailingPosition = Kee[int](1)

  class EchoMode(CuteNum):
    """
    The enum 'QLineEdit::EchoMode' of Qt, with the 4 names Qt gives in it.
    """

    Normal = Kee[int](0)
    NoEcho = Kee[int](1)
    Password = Kee[int](2)
    PasswordEchoOnEdit = Kee[int](3)

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
    Calls Qt's 'QString QLineEdit::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#tr

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
    #  QString QLineEdit::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QLineEdit2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLineEdit'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QLineEdit::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLineEdit::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QLineEdit10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QLineEdit::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLineEdit::text() const
    return self.uglySide.call('ritual_ZNK9QLineEdit4textEv')

  def displayText(self) -> str:
    """
    Calls Qt's 'QString QLineEdit::displayText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#displayText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLineEdit::displayText() const
    return self.uglySide.call('ritual_ZNK9QLineEdit11displayTextEv')

  def placeholderText(self) -> str:
    """
    Calls Qt's 'QString QLineEdit::placeholderText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#placeholderText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLineEdit::placeholderText() const
    return self.uglySide.call('ritual_ZNK9QLineEdit15placeholderTextEv')

  def maxLength(self) -> int:
    """
    Calls Qt's 'int QLineEdit::maxLength() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#maxLength
    """
    #  int QLineEdit::maxLength() const
    return self.uglySide.call('ritual_ZNK9QLineEdit9maxLengthEv')

  def hasFrame(self) -> bool:
    """
    Calls Qt's 'bool QLineEdit::hasFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#hasFrame
    """
    #  bool QLineEdit::hasFrame() const
    return self.uglySide.call('ritual_ZNK9QLineEdit8hasFrameEv')

  def isClearButtonEnabled(self) -> bool:
    """
    Calls Qt's 'bool QLineEdit::isClearButtonEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineedit.html#isClearButtonEnabled
    """
    #  bool QLineEdit::isClearButtonEnabled() const
    return self.uglySide.call('ritual_ZNK9QLineEdit20isClearButtonEnabledEv')

  def echoMode(self) -> EchoMode:
    """
    Calls Qt's 'EchoMode QLineEdit::echoMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#echoMode

    Returns
    -------

    EchoMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'EchoMode(number)' gives.
    """
    #  EchoMode QLineEdit::echoMode() const
    return QLineEdit.EchoMode(self.uglySide.call(
        'ritual_ZNK9QLineEdit8echoModeEv',
    ))

  def isReadOnly(self) -> bool:
    """
    Calls Qt's 'bool QLineEdit::isReadOnly() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#isReadOnly
    """
    #  bool QLineEdit::isReadOnly() const
    return self.uglySide.call('ritual_ZNK9QLineEdit10isReadOnlyEv')

  def validator(self) -> Optional[QValidator]:
    """
    Calls Qt's 'const QValidator *QLineEdit::validator() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#validator

    Returns
    -------

    Optional[QValidator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QValidator *QLineEdit::validator() const
    address = self.uglySide.call('ritual_ZNK9QLineEdit9validatorEv')
    from ..QtGui import QValidator
    return QValidator._cuteAt(address)

  def completer(self) -> Optional[QCompleter]:
    """
    Calls Qt's 'QCompleter *QLineEdit::completer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#completer

    Returns
    -------

    Optional[QCompleter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCompleter *QLineEdit::completer() const
    address = self.uglySide.call('ritual_ZNK9QLineEdit9completerEv')
    from . import QCompleter
    return QCompleter._cuteAt(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QLineEdit::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QLineEdit::sizeHint() const
    address = self.uglySide.call('ritual_ZNK9QLineEdit8sizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QLineEdit::minimumSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QLineEdit::minimumSizeHint() const
    address = self.uglySide.call('ritual_ZNK9QLineEdit15minimumSizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def cursorPosition(self) -> int:
    """
    Calls Qt's 'int QLineEdit::cursorPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#cursorPosition
    """
    #  int QLineEdit::cursorPosition() const
    return self.uglySide.call('ritual_ZNK9QLineEdit14cursorPositionEv')

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QLineEdit::alignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QLineEdit::alignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK9QLineEdit9alignmentEv',
    ))

  def isModified(self) -> bool:
    """
    Calls Qt's 'bool QLineEdit::isModified() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#isModified
    """
    #  bool QLineEdit::isModified() const
    return self.uglySide.call('ritual_ZNK9QLineEdit10isModifiedEv')

  def hasSelectedText(self) -> bool:
    """
    Calls Qt's 'bool QLineEdit::hasSelectedText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#hasSelectedText
    """
    #  bool QLineEdit::hasSelectedText() const
    return self.uglySide.call('ritual_ZNK9QLineEdit15hasSelectedTextEv')

  def selectedText(self) -> str:
    """
    Calls Qt's 'QString QLineEdit::selectedText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#selectedText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLineEdit::selectedText() const
    return self.uglySide.call('ritual_ZNK9QLineEdit12selectedTextEv')

  def selectionStart(self) -> int:
    """
    Calls Qt's 'int QLineEdit::selectionStart() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#selectionStart
    """
    #  int QLineEdit::selectionStart() const
    return self.uglySide.call('ritual_ZNK9QLineEdit14selectionStartEv')

  def selectionEnd(self) -> int:
    """
    Calls Qt's 'int QLineEdit::selectionEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#selectionEnd
    """
    #  int QLineEdit::selectionEnd() const
    return self.uglySide.call('ritual_ZNK9QLineEdit12selectionEndEv')

  def selectionLength(self) -> int:
    """
    Calls Qt's 'int QLineEdit::selectionLength() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#selectionLength
    """
    #  int QLineEdit::selectionLength() const
    return self.uglySide.call('ritual_ZNK9QLineEdit15selectionLengthEv')

  def isUndoAvailable(self) -> bool:
    """
    Calls Qt's 'bool QLineEdit::isUndoAvailable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#isUndoAvailable
    """
    #  bool QLineEdit::isUndoAvailable() const
    return self.uglySide.call('ritual_ZNK9QLineEdit15isUndoAvailableEv')

  def isRedoAvailable(self) -> bool:
    """
    Calls Qt's 'bool QLineEdit::isRedoAvailable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#isRedoAvailable
    """
    #  bool QLineEdit::isRedoAvailable() const
    return self.uglySide.call('ritual_ZNK9QLineEdit15isRedoAvailableEv')

  def dragEnabled(self) -> bool:
    """
    Calls Qt's 'bool QLineEdit::dragEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#dragEnabled
    """
    #  bool QLineEdit::dragEnabled() const
    return self.uglySide.call('ritual_ZNK9QLineEdit11dragEnabledEv')

  def cursorMoveStyle(self) -> Qt.CursorMoveStyle:
    """
    Calls Qt's 'Qt::CursorMoveStyle QLineEdit::cursorMoveStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#cursorMoveStyle

    Returns
    -------

    Qt.CursorMoveStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.CursorMoveStyle(number)' gives.
    """
    #  Qt::CursorMoveStyle QLineEdit::cursorMoveStyle() const
    return Qt.CursorMoveStyle(self.uglySide.call(
        'ritual_ZNK9QLineEdit15cursorMoveStyleEv',
    ))

  def inputMask(self) -> str:
    """
    Calls Qt's 'QString QLineEdit::inputMask() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#inputMask

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLineEdit::inputMask() const
    return self.uglySide.call('ritual_ZNK9QLineEdit9inputMaskEv')

  def hasAcceptableInput(self) -> bool:
    """
    Calls Qt's 'bool QLineEdit::hasAcceptableInput() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#hasAcceptableInput
    """
    #  bool QLineEdit::hasAcceptableInput() const
    return self.uglySide.call('ritual_ZNK9QLineEdit18hasAcceptableInputEv')

  def textMargins(self) -> QMargins:
    """
    Calls Qt's 'QMargins QLineEdit::textMargins() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#textMargins

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins QLineEdit::textMargins() const
    address = self.uglySide.call('ritual_ZNK9QLineEdit11textMarginsEv')
    from ..QtCore import QMargins
    return QMargins._cuteOwning(address)

  @overload(Qt.InputMethodQuery)
  def inputMethodQuery(self, a0: Qt.InputMethodQuery) -> QVariant:
    """
    Calls Qt's 'QVariant QLineEdit::inputMethodQuery(Qt::InputMethodQuery a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#inputMethodQuery

    Parameters
    ----------

    a0 : Qt.InputMethodQuery
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QLineEdit::inputMethodQuery(Qt::InputMethodQuery a0) const
    address = self.uglySide.call(
        'ritual_ZNK9QLineEdit16inputMethodQueryEN2Qt16InputMethodQueryE',
        a0.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(Qt.InputMethodQuery, QVariant)
  def inputMethodQuery(
      self,
      property: Qt.InputMethodQuery,
      argument: QVariant,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QLineEdit::inputMethodQuery(Qt::InputMethodQuery
    property, QVariant argument) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#inputMethodQuery

    Parameters
    ----------

    property : Qt.InputMethodQuery
      Passed on as its number.

    argument : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QLineEdit::inputMethodQuery(Qt::InputMethodQuery property,
    #      QVariant argument) const
    address = self.uglySide.call(
        'ritual_ZNK9QLineEdit16inputMethodQueryEN2Qt16InputMethodQueryE8QVa'
        'riant',
        property.value, self._valueOf(argument),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setPlaceholderText(self, a0: str) -> None:
    """
    Calls Qt's 'void QLineEdit::setPlaceholderText(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#setPlaceholderText

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLineEdit::setPlaceholderText(const QString &a0)
    self.uglySide.call(
        'ritual_ZN9QLineEdit18setPlaceholderTextERK7QString', a0,
    )

  @overload(int)
  def setMaxLength(self, a0: int) -> None:
    """
    Calls Qt's 'void QLineEdit::setMaxLength(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#setMaxLength

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QLineEdit::setMaxLength(int a0)
    self.uglySide.call('ritual_ZN9QLineEdit12setMaxLengthEi', a0)

  @overload(bool)
  def setFrame(self, a0: bool) -> None:
    """
    Calls Qt's 'void QLineEdit::setFrame(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#setFrame

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QLineEdit::setFrame(bool a0)
    self.uglySide.call('ritual_ZN9QLineEdit8setFrameEb', a0)

  @overload(bool)
  def setClearButtonEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QLineEdit::setClearButtonEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineedit.html#setClearButtonEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QLineEdit::setClearButtonEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN9QLineEdit21setClearButtonEnabledEb', enable,
    )

  @overload(EchoMode)
  def setEchoMode(self, a0: EchoMode) -> None:
    """
    Calls Qt's 'void QLineEdit::setEchoMode(EchoMode a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#setEchoMode

    Parameters
    ----------

    a0 : EchoMode
      Passed on as its number.
    """
    #  void QLineEdit::setEchoMode(EchoMode a0)
    self.uglySide.call(
        'ritual_ZN9QLineEdit11setEchoModeENS_8EchoModeE', a0.value,
    )

  @overload(bool)
  def setReadOnly(self, a0: bool) -> None:
    """
    Calls Qt's 'void QLineEdit::setReadOnly(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#setReadOnly

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QLineEdit::setReadOnly(bool a0)
    self.uglySide.call('ritual_ZN9QLineEdit11setReadOnlyEb', a0)

  @overload(QValidator)
  @overload(NoneType)
  def setValidator(self, a0: Optional[QValidator]) -> None:
    """
    Calls Qt's 'void QLineEdit::setValidator(const QValidator *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#setValidator

    Parameters
    ----------

    a0 : Optional[QValidator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLineEdit::setValidator(const QValidator *a0)
    self.uglySide.call(
        'ritual_ZN9QLineEdit12setValidatorEPK10QValidator',
        self._addressOf(a0),
    )

  @overload(QCompleter)
  @overload(NoneType)
  def setCompleter(self, completer: Optional[QCompleter]) -> None:
    """
    Calls Qt's 'void QLineEdit::setCompleter(QCompleter *completer)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#setCompleter

    Parameters
    ----------

    completer : Optional[QCompleter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLineEdit::setCompleter(QCompleter *completer)
    self.uglySide.call(
        'ritual_ZN9QLineEdit12setCompleterEP10QCompleter',
        self._addressOf(completer),
    )

  @overload(int)
  def setCursorPosition(self, a0: int) -> None:
    """
    Calls Qt's 'void QLineEdit::setCursorPosition(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#setCursorPosition

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QLineEdit::setCursorPosition(int a0)
    self.uglySide.call('ritual_ZN9QLineEdit17setCursorPositionEi', a0)

  @overload(Qt.Alignment)
  def setAlignment(self, flag: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QLineEdit::setAlignment(Qt::Alignment flag)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#setAlignment

    Parameters
    ----------

    flag : Qt.Alignment
      Passed on as its number.
    """
    #  void QLineEdit::setAlignment(Qt::Alignment flag)
    self.uglySide.call(
        'ritual_ZN9QLineEdit12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE',
        flag.value,
    )

  @overload(bool)
  def setModified(self, a0: bool) -> None:
    """
    Calls Qt's 'void QLineEdit::setModified(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#setModified

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QLineEdit::setModified(bool a0)
    self.uglySide.call('ritual_ZN9QLineEdit11setModifiedEb', a0)

  @overload(int, int)
  def setSelection(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QLineEdit::setSelection(int a0, int a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#setSelection

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QLineEdit::setSelection(int a0, int a1)
    self.uglySide.call('ritual_ZN9QLineEdit12setSelectionEii', a0, a1)

  @overload(bool)
  def setDragEnabled(self, b: bool) -> None:
    """
    Calls Qt's 'void QLineEdit::setDragEnabled(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#setDragEnabled

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QLineEdit::setDragEnabled(bool b)
    self.uglySide.call('ritual_ZN9QLineEdit14setDragEnabledEb', b)

  @overload(Qt.CursorMoveStyle)
  def setCursorMoveStyle(self, style: Qt.CursorMoveStyle) -> None:
    """
    Calls Qt's 'void QLineEdit::setCursorMoveStyle(Qt::CursorMoveStyle
    style)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#setCursorMoveStyle

    Parameters
    ----------

    style : Qt.CursorMoveStyle
      Passed on as its number.
    """
    #  void QLineEdit::setCursorMoveStyle(Qt::CursorMoveStyle style)
    self.uglySide.call(
        'ritual_ZN9QLineEdit18setCursorMoveStyleEN2Qt15CursorMoveStyleE',
        style.value,
    )

  @overload(str)
  def setInputMask(self, inputMask: str) -> None:
    """
    Calls Qt's 'void QLineEdit::setInputMask(const QString &inputMask)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#setInputMask

    Parameters
    ----------

    inputMask : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLineEdit::setInputMask(const QString &inputMask)
    self.uglySide.call(
        'ritual_ZN9QLineEdit12setInputMaskERK7QString', inputMask,
    )

  @overload(int, int, int, int)
  def setTextMargins(
      self,
      left: int,
      top: int,
      right: int,
      bottom: int,
  ) -> None:
    """
    Calls Qt's 'void QLineEdit::setTextMargins(int left, int top, int right,
    int bottom)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#setTextMargins

    Parameters
    ----------

    left : int
      Passed on as it is.

    top : int
      Passed on as it is.

    right : int
      Passed on as it is.

    bottom : int
      Passed on as it is.
    """
    #  void QLineEdit::setTextMargins(int left, int top, int right, int
    #      bottom)
    self.uglySide.call(
        'ritual_ZN9QLineEdit14setTextMarginsEiiii', left, top, right, bottom,
    )

  @overload(QMargins)
  def setTextMargins(self, margins: QMargins) -> None:
    """
    Calls Qt's 'void QLineEdit::setTextMargins(const QMargins &margins)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#setTextMargins

    Parameters
    ----------

    margins : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.
    """
    #  void QLineEdit::setTextMargins(const QMargins &margins)
    self.uglySide.call(
        'ritual_ZN9QLineEdit14setTextMarginsERK8QMargins',
        self._valueOf(margins),
    )

  @overload(str)
  def setText(self, a0: str) -> None:
    """
    Calls Qt's 'void QLineEdit::setText(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#setText

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLineEdit::setText(const QString &a0)
    self.uglySide.call('ritual_ZN9QLineEdit7setTextERK7QString', a0)

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
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QLineEdit::QLineEdit(QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#QLineEdit

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLineEdit::QLineEdit(QWidget *parent)
    self._noteCreation(QLineEdit, lambda: Rituals.call(
        'ritual_ZN9QLineEditC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(str)
  @overload(str, QWidget)
  @overload(str, NoneType)
  def __init__(self, a0: str, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QLineEdit::QLineEdit(const QString &a0,
    QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#QLineEdit

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLineEdit::QLineEdit(const QString &a0, QWidget *parent)
    self._noteCreation(QLineEdit, lambda: Rituals.call(
        'ritual_ZN9QLineEditC1ERK7QStringP7QWidget',
        a0, self._addressOf(parent),
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

  @overload(QPoint)
  def cursorPositionAt(self, pos: QPoint) -> int:
    """
    Calls Qt's 'int QLineEdit::cursorPositionAt(const QPoint &pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#cursorPositionAt

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  int QLineEdit::cursorPositionAt(const QPoint &pos)
    return self.uglySide.call(
        'ritual_ZN9QLineEdit16cursorPositionAtERK6QPoint',
        self._valueOf(pos),
    )

  @overload(bool)
  @overload(bool, int)
  def cursorForward(self, mark: bool, steps: int = 1) -> None:
    """
    Calls Qt's 'void QLineEdit::cursorForward(bool mark, int steps)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#cursorForward

    Parameters
    ----------

    mark : bool
      Passed on as it is.

    steps : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QLineEdit::cursorForward(bool mark, int steps)
    self.uglySide.call('ritual_ZN9QLineEdit13cursorForwardEbi', mark, steps)

  @overload(bool)
  @overload(bool, int)
  def cursorBackward(self, mark: bool, steps: int = 1) -> None:
    """
    Calls Qt's 'void QLineEdit::cursorBackward(bool mark, int steps)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#cursorBackward

    Parameters
    ----------

    mark : bool
      Passed on as it is.

    steps : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QLineEdit::cursorBackward(bool mark, int steps)
    self.uglySide.call('ritual_ZN9QLineEdit14cursorBackwardEbi', mark, steps)

  @overload(bool)
  def cursorWordForward(self, mark: bool) -> None:
    """
    Calls Qt's 'void QLineEdit::cursorWordForward(bool mark)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#cursorWordForward

    Parameters
    ----------

    mark : bool
      Passed on as it is.
    """
    #  void QLineEdit::cursorWordForward(bool mark)
    self.uglySide.call('ritual_ZN9QLineEdit17cursorWordForwardEb', mark)

  @overload(bool)
  def cursorWordBackward(self, mark: bool) -> None:
    """
    Calls Qt's 'void QLineEdit::cursorWordBackward(bool mark)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#cursorWordBackward

    Parameters
    ----------

    mark : bool
      Passed on as it is.
    """
    #  void QLineEdit::cursorWordBackward(bool mark)
    self.uglySide.call('ritual_ZN9QLineEdit18cursorWordBackwardEb', mark)

  def backspace(self) -> None:
    """
    Calls Qt's 'void QLineEdit::backspace()'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#backspace
    """
    #  void QLineEdit::backspace()
    self.uglySide.call('ritual_ZN9QLineEdit9backspaceEv')

  def del_(self) -> None:
    """
    Calls Qt's 'void QLineEdit::del()'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#del
    """
    #  void QLineEdit::del()
    self.uglySide.call('ritual_ZN9QLineEdit3delEv')

  @overload(bool)
  def home(self, mark: bool) -> None:
    """
    Calls Qt's 'void QLineEdit::home(bool mark)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#home

    Parameters
    ----------

    mark : bool
      Passed on as it is.
    """
    #  void QLineEdit::home(bool mark)
    self.uglySide.call('ritual_ZN9QLineEdit4homeEb', mark)

  @overload(bool)
  def end(self, mark: bool) -> None:
    """
    Calls Qt's 'void QLineEdit::end(bool mark)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#end

    Parameters
    ----------

    mark : bool
      Passed on as it is.
    """
    #  void QLineEdit::end(bool mark)
    self.uglySide.call('ritual_ZN9QLineEdit3endEb', mark)

  @overload(QAction, ActionPosition)
  @overload(NoneType, ActionPosition)
  def addAction(
      self,
      action: Optional[QAction],
      position: ActionPosition,
  ) -> None:
    """
    Calls Qt's 'void QLineEdit::addAction(QAction *action, ActionPosition
    position)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#addAction

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    position : ActionPosition
      Passed on as its number.
    """
    #  void QLineEdit::addAction(QAction *action, ActionPosition position)
    self.uglySide.call(
        'ritual_ZN9QLineEdit9addActionEP7QActionNS_14ActionPositionE',
        self._addressOf(action), position.value,
    )

  @overload(QIcon, ActionPosition)
  def addAction(
      self,
      icon: QIcon,
      position: ActionPosition,
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QLineEdit::addAction(const QIcon &icon,
    ActionPosition position)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#addAction

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    position : ActionPosition
      Passed on as its number.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QLineEdit::addAction(const QIcon &icon, ActionPosition
    #      position)
    address = self.uglySide.call(
        'ritual_ZN9QLineEdit9addActionERK5QIconNS_14ActionPositionE',
        self._valueOf(icon), position.value,
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def clear(self) -> None:
    """
    Calls Qt's 'void QLineEdit::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#clear
    """
    #  void QLineEdit::clear()
    self.uglySide.call('ritual_ZN9QLineEdit5clearEv')

  def selectAll(self) -> None:
    """
    Calls Qt's 'void QLineEdit::selectAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#selectAll
    """
    #  void QLineEdit::selectAll()
    self.uglySide.call('ritual_ZN9QLineEdit9selectAllEv')

  def undo(self) -> None:
    """
    Calls Qt's 'void QLineEdit::undo()'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#undo
    """
    #  void QLineEdit::undo()
    self.uglySide.call('ritual_ZN9QLineEdit4undoEv')

  def redo(self) -> None:
    """
    Calls Qt's 'void QLineEdit::redo()'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#redo
    """
    #  void QLineEdit::redo()
    self.uglySide.call('ritual_ZN9QLineEdit4redoEv')

  def cut(self) -> None:
    """
    Calls Qt's 'void QLineEdit::cut()'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#cut
    """
    #  void QLineEdit::cut()
    self.uglySide.call('ritual_ZN9QLineEdit3cutEv')

  def copy(self) -> None:
    """
    Calls Qt's 'void QLineEdit::copy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#copy
    """
    #  void QLineEdit::copy() const
    self.uglySide.call('ritual_ZNK9QLineEdit4copyEv')

  def paste(self) -> None:
    """
    Calls Qt's 'void QLineEdit::paste()'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#paste
    """
    #  void QLineEdit::paste()
    self.uglySide.call('ritual_ZN9QLineEdit5pasteEv')

  def deselect(self) -> None:
    """
    Calls Qt's 'void QLineEdit::deselect()'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#deselect
    """
    #  void QLineEdit::deselect()
    self.uglySide.call('ritual_ZN9QLineEdit8deselectEv')

  @overload(str)
  def insert(self, a0: str) -> None:
    """
    Calls Qt's 'void QLineEdit::insert(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#insert

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLineEdit::insert(const QString &a0)
    self.uglySide.call('ritual_ZN9QLineEdit6insertERK7QString', a0)

  def createStandardContextMenu(self) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QLineEdit::createStandardContextMenu()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlineedit.html#createStandardContextMenu

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QLineEdit::createStandardContextMenu()
    address = self.uglySide.call(
        'ritual_ZN9QLineEdit25createStandardContextMenuEv',
    )
    from . import QMenu
    return QMenu._cuteAt(address)

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, a0: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QLineEdit::timerEvent(QTimerEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#timerEvent

    Parameters
    ----------

    a0 : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLineEdit::timerEvent(QTimerEvent *a0)
    self.uglySide.call(
        'ritual_ZN9QLineEdit10timerEventEP11QTimerEvent',
        self._addressOf(a0),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QLineEdit::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlineedit.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QLineEdit::event(QEvent *a0)
    return self.uglySide.call(
        'ritual_ZN9QLineEdit5eventEP6QEvent', self._addressOf(a0),
    )
