"""
QVirtualKeyboardInputEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/qvirtualkeyboardinputengine.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QMap, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QTimerEvent, QVariant
  from . import QVirtualKeyboardAbstractInputMethod
  from . import QVirtualKeyboardInputContext
  from . import QVirtualKeyboardSelectionListModel, QVirtualKeyboardTrace
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTimerEvent = WAIT['QTimerEvent']
  QVariant = WAIT['QVariant']
  QVirtualKeyboardAbstractInputMethod = WAIT['QVirtualKeyboardAbstractInputMethod']
  QVirtualKeyboardInputContext = WAIT['QVirtualKeyboardInputContext']
  QVirtualKeyboardTrace = WAIT['QVirtualKeyboardTrace']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVirtualKeyboardInputEngine(QObject):
  """
  The cute side of Qt's QVirtualKeyboardInputEngine: a plain Python object
  standing in front of one C++ QVirtualKeyboardInputEngine.

  It is built on the cute 'QObject', as Qt's QVirtualKeyboardInputEngine is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QVirtualKeyboardInputEngine that has a ritual and
  that Python can call so far, 36 names in all: 'metaObject', 'tr', 'init',
  'virtualKeyPress', 'virtualKeyCancel', 'virtualKeyRelease',
  'virtualKeyClick', 'inputContext', 'activeKey', 'previousKey',
  'inputMethod', 'setInputMethod', 'inputMode', 'setInputMode',
  'wordCandidateListModel', 'wordCandidateListVisibleHint', 'traceBegin',
  'traceEnd', 'clickPreeditText', 'virtualKeyClicked', 'activeKeyChanged',
  'previousKeyChanged', 'inputMethodChanged', 'inputMethodReset',
  'inputMethodUpdate', 'inputModesChanged', 'inputModeChanged',
  'patternRecognitionModesChanged', 'wordCandidateListModelChanged',
  'wordCandidateListVisibleHintChanged', 'reset', 'update', 'shiftChanged',
  'updateSelectionListModels', 'updateInputModes', 'timerEvent'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QVirtualKeyboardInputEngine::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QVirtualKeyboardInputEngine::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QVirtualKeyboardInputEnginePrivate
    *QVirtualKeyboardInputEngine::d_func()': gives
    'QVirtualKeyboardInputEnginePrivate', which has no cute class yet.
  - Qt's 'const QVirtualKeyboardInputEnginePrivate
    *QVirtualKeyboardInputEngine::d_func() const': gives
    'QVirtualKeyboardInputEnginePrivate', which has no cute class yet.
  - Qt's 'void QVirtualKeyboardInputEngine::qt_qmlMarker_uncreatable()': one
    of Qt's own inner workings.
  - Qt's 'QVirtualKeyboardInputEngine::~QVirtualKeyboardInputEngine()': the
    destructor: Python never removes a C++ QVirtualKeyboardInputEngine.
  - Qt's 'QList<int> QVirtualKeyboardInputEngine::inputModes() const': gives
    a type Python has no way to take yet.
  - Qt's 'QList<int> QVirtualKeyboardInputEngine::patternRecognitionModes()
    const': gives a type Python has no way to take yet.
  - Qt's 'bool QVirtualKeyboardInputEngine::reselect(int cursorPosition,
    const ReselectFlags &reselectFlags)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  4 of the 50 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QVirtualKeyboardInputEngine is created at the first use, not by
    'QVirtualKeyboardInputEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVirtualKeyboardInputEngine.
  - Qt tells when it has removed the C++ QVirtualKeyboardInputEngine. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QVirtualKeyboardInputEngine that has no cute function
    yet, 'inputModes', 'patternRecognitionModes', 'reselect', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QVirtualKeyboardInputEngine, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class InputMode(CuteNum, scoped=True):
    """
    The enum 'QVirtualKeyboardInputEngine::InputMode' of Qt, with the 21
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Latin = Kee[int](0)
    Numeric = Kee[int](1)
    Dialable = Kee[int](2)
    Pinyin = Kee[int](3)
    Cangjie = Kee[int](4)
    Zhuyin = Kee[int](5)
    Hangul = Kee[int](6)
    Hiragana = Kee[int](7)
    Katakana = Kee[int](8)
    FullwidthLatin = Kee[int](9)
    Greek = Kee[int](10)
    Cyrillic = Kee[int](11)
    Arabic = Kee[int](12)
    Hebrew = Kee[int](13)
    ChineseHandwriting = Kee[int](14)
    JapaneseHandwriting = Kee[int](15)
    KoreanHandwriting = Kee[int](16)
    Thai = Kee[int](17)
    Stroke = Kee[int](18)
    Romaji = Kee[int](19)
    HiraganaFlick = Kee[int](20)

  class PatternRecognitionMode(CuteNum, scoped=True):
    """
    The enum 'QVirtualKeyboardInputEngine::PatternRecognitionMode' of Qt,
    with the 4 names Qt gives in it. C++ keeps these names inside the enum,
    so the class that holds the enum does not have them.
    """

    NULL = Kee[int](0)
    PatternRecognitionDisabled = Kee[int](0)
    Handwriting = Kee[int](1)
    HandwritingRecoginition = Kee[int](1)

  class ReselectFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QVirtualKeyboardInputEngine::ReselectFlag' of Qt, with
    the 3 names Qt gives in it. Qt names the type of its combinations
    'QVirtualKeyboardInputEngine::ReselectFlags'. C++ keeps these names
    inside the enum, so the class that holds the enum does not have them.
    """

    WordBeforeCursor = 0x1
    WordAfterCursor = 0x2
    WordAtCursor = 0x3

  ReselectFlags = ReselectFlag

  class TextCase(CuteNum, scoped=True):
    """
    The enum 'QVirtualKeyboardInputEngine::TextCase' of Qt, with the 2 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Lower = Kee[int](0)
    Upper = Kee[int](1)

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
    Calls Qt's 'QString QVirtualKeyboardInputEngine::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#tr

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
    #  QString QVirtualKeyboardInputEngine::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QVirtualKeyboardInputEngine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVirtualKeyboardInputEngine'

  #  A C++ QVirtualKeyboardInputEngine Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVirtualKeyboardInputEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QVirtualKeyboardInputEngine::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QVirtualKeyboardInputEngine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QVirtualKeyboardInputEngine10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def inputContext(self) -> Optional[QVirtualKeyboardInputContext]:
    """
    Calls Qt's 'QVirtualKeyboardInputContext
    *QVirtualKeyboardInputEngine::inputContext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#inputContext

    Returns
    -------

    Optional[QVirtualKeyboardInputContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVirtualKeyboardInputContext
    #      *QVirtualKeyboardInputEngine::inputContext() const
    address = self.uglySide.call(
        'ritual_ZNK27QVirtualKeyboardInputEngine12inputContextEv',
    )
    from . import QVirtualKeyboardInputContext
    return QVirtualKeyboardInputContext._cuteAt(address)

  def activeKey(self) -> Qt.Key:
    """
    Calls Qt's 'Qt::Key QVirtualKeyboardInputEngine::activeKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#activeKey

    Returns
    -------

    Qt.Key
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Key(number)' gives.
    """
    #  Qt::Key QVirtualKeyboardInputEngine::activeKey() const
    return Qt.Key(self.uglySide.call(
        'ritual_ZNK27QVirtualKeyboardInputEngine9activeKeyEv',
    ))

  def previousKey(self) -> Qt.Key:
    """
    Calls Qt's 'Qt::Key QVirtualKeyboardInputEngine::previousKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#previousKey

    Returns
    -------

    Qt.Key
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Key(number)' gives.
    """
    #  Qt::Key QVirtualKeyboardInputEngine::previousKey() const
    return Qt.Key(self.uglySide.call(
        'ritual_ZNK27QVirtualKeyboardInputEngine11previousKeyEv',
    ))

  def inputMethod(self) -> Optional[QVirtualKeyboardAbstractInputMethod]:
    """
    Calls Qt's 'QVirtualKeyboardAbstractInputMethod
    *QVirtualKeyboardInputEngine::inputMethod() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#inputMethod

    Returns
    -------

    Optional[QVirtualKeyboardAbstractInputMethod]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVirtualKeyboardAbstractInputMethod
    #      *QVirtualKeyboardInputEngine::inputMethod() const
    address = self.uglySide.call(
        'ritual_ZNK27QVirtualKeyboardInputEngine11inputMethodEv',
    )
    from . import QVirtualKeyboardAbstractInputMethod
    return QVirtualKeyboardAbstractInputMethod._cuteAt(address)

  def inputMode(self) -> InputMode:
    """
    Calls Qt's 'InputMode QVirtualKeyboardInputEngine::inputMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#inputMode

    Returns
    -------

    InputMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'InputMode(number)' gives.
    """
    #  InputMode QVirtualKeyboardInputEngine::inputMode() const
    return QVirtualKeyboardInputEngine.InputMode(self.uglySide.call(
        'ritual_ZNK27QVirtualKeyboardInputEngine9inputModeEv',
    ))

  def wordCandidateListModel(
      self,
  ) -> Optional[QVirtualKeyboardSelectionListModel]:
    """
    Calls Qt's 'QVirtualKeyboardSelectionListModel
    *QVirtualKeyboardInputEngine::wordCandidateListModel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html

    Returns
    -------

    Optional[QVirtualKeyboardSelectionListModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVirtualKeyboardSelectionListModel
    #      *QVirtualKeyboardInputEngine::wordCandidateListModel() const
    address = self.uglySide.call(
        'ritual_ZNK27QVirtualKeyboardInputEngine22wordCandidateListModelEv',
    )
    from . import QVirtualKeyboardSelectionListModel
    return QVirtualKeyboardSelectionListModel._cuteAt(address)

  def wordCandidateListVisibleHint(self) -> bool:
    """
    Calls Qt's 'bool
    QVirtualKeyboardInputEngine::wordCandidateListVisibleHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html
    """
    #  bool QVirtualKeyboardInputEngine::wordCandidateListVisibleHint() const
    return self.uglySide.call(
        'ritual_ZNK27QVirtualKeyboardInputEngine28wordCandidateListVisibleH'
        'intEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVirtualKeyboardAbstractInputMethod)
  @overload(NoneType)
  def setInputMethod(
      self,
      inputMethod: Optional[QVirtualKeyboardAbstractInputMethod],
  ) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputEngine::setInputMethod(
    QVirtualKeyboardAbstractInputMethod *inputMethod)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#setInputMethod

    Parameters
    ----------

    inputMethod : Optional[QVirtualKeyboardAbstractInputMethod]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVirtualKeyboardInputEngine::setInputMethod(
    #      QVirtualKeyboardAbstractInputMethod *inputMethod)
    self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine14setInputMethodEP35QVirtual'
        'KeyboardAbstractInputMethod',
        self._addressOf(inputMethod),
    )

  @overload(InputMode)
  def setInputMode(self, inputMode: InputMode) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputEngine::setInputMode(InputMode
    inputMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#setInputMode

    Parameters
    ----------

    inputMode : InputMode
      Passed on as its number.
    """
    #  void QVirtualKeyboardInputEngine::setInputMode(InputMode inputMode)
    self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine12setInputModeENS_9InputMode'
        'E',
        inputMode.value,
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
  @overload(QVirtualKeyboardInputContext)
  @overload(NoneType)
  def __init__(
      self,
      parent: Optional[QVirtualKeyboardInputContext] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QVirtualKeyboardInputEngine::QVirtualKeyboardInputEngine(
    QVirtualKeyboardInputContext *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html

    Parameters
    ----------

    parent : Optional[QVirtualKeyboardInputContext]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QVirtualKeyboardInputEngine::QVirtualKeyboardInputEngine(
    #      QVirtualKeyboardInputContext *parent)
    self._noteCreation(QVirtualKeyboardInputEngine, lambda: Rituals.call(
        'ritual_ZN27QVirtualKeyboardInputEngineC1EP28QVirtualKeyboardInputC'
        'ontext',
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

  def init(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputEngine::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#init
    """
    #  void QVirtualKeyboardInputEngine::init()
    self.uglySide.call('ritual_ZN27QVirtualKeyboardInputEngine4initEv')

  @overload(Qt.Key, str, Qt.KeyboardModifiers, bool)
  def virtualKeyPress(
      self,
      key: Qt.Key,
      text: str,
      modifiers: Qt.KeyboardModifiers,
      repeat: bool,
  ) -> bool:
    """
    Calls Qt's 'bool QVirtualKeyboardInputEngine::virtualKeyPress(Qt::Key
    key, const QString &text, Qt::KeyboardModifiers modifiers, bool repeat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#virtualKeyPress

    Parameters
    ----------

    key : Qt.Key
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    repeat : bool
      Passed on as it is.
    """
    #  bool QVirtualKeyboardInputEngine::virtualKeyPress(Qt::Key key, const
    #      QString &text, Qt::KeyboardModifiers modifiers, bool repeat)
    return self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine15virtualKeyPressEN2Qt3KeyER'
        'K7QString6QFlagsINS0_16KeyboardModifierEEb',
        key.value, text, modifiers.value, repeat,
    )

  def virtualKeyCancel(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputEngine::virtualKeyCancel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#virtualKeyCancel
    """
    #  void QVirtualKeyboardInputEngine::virtualKeyCancel()
    self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine16virtualKeyCancelEv',
    )

  @overload(Qt.Key, str, Qt.KeyboardModifiers)
  def virtualKeyRelease(
      self,
      key: Qt.Key,
      text: str,
      modifiers: Qt.KeyboardModifiers,
  ) -> bool:
    """
    Calls Qt's 'bool QVirtualKeyboardInputEngine::virtualKeyRelease(Qt::Key
    key, const QString &text, Qt::KeyboardModifiers modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#virtualKeyRelease

    Parameters
    ----------

    key : Qt.Key
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  bool QVirtualKeyboardInputEngine::virtualKeyRelease(Qt::Key key, const
    #      QString &text, Qt::KeyboardModifiers modifiers)
    return self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine17virtualKeyReleaseEN2Qt3Key'
        'ERK7QString6QFlagsINS0_16KeyboardModifierEE',
        key.value, text, modifiers.value,
    )

  @overload(Qt.Key, str, Qt.KeyboardModifiers)
  def virtualKeyClick(
      self,
      key: Qt.Key,
      text: str,
      modifiers: Qt.KeyboardModifiers,
  ) -> bool:
    """
    Calls Qt's 'bool QVirtualKeyboardInputEngine::virtualKeyClick(Qt::Key
    key, const QString &text, Qt::KeyboardModifiers modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#virtualKeyClick

    Parameters
    ----------

    key : Qt.Key
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  bool QVirtualKeyboardInputEngine::virtualKeyClick(Qt::Key key, const
    #      QString &text, Qt::KeyboardModifiers modifiers)
    return self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine15virtualKeyClickEN2Qt3KeyER'
        'K7QString6QFlagsINS0_16KeyboardModifierEE',
        key.value, text, modifiers.value,
    )

  @overload(
      int, PatternRecognitionMode, QMap[str, QVariant], QMap[str, QVariant],
  )
  def traceBegin(
      self,
      traceId: int,
      patternRecognitionMode: PatternRecognitionMode,
      traceCaptureDeviceInfo: QMap[str, QVariant],
      traceScreenInfo: QMap[str, QVariant],
  ) -> Optional[QVirtualKeyboardTrace]:
    """
    Calls Qt's 'QVirtualKeyboardTrace
    *QVirtualKeyboardInputEngine::traceBegin(int traceId,
    PatternRecognitionMode patternRecognitionMode, const QVariantMap
    &traceCaptureDeviceInfo, const QVariantMap &traceScreenInfo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#traceBegin

    Parameters
    ----------

    traceId : int
      Passed on as it is.

    patternRecognitionMode : PatternRecognitionMode
      Passed on as its number.

    traceCaptureDeviceInfo : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    traceScreenInfo : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Optional[QVirtualKeyboardTrace]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVirtualKeyboardTrace *QVirtualKeyboardInputEngine::traceBegin(int
    #      traceId, PatternRecognitionMode patternRecognitionMode, const
    #      QVariantMap &traceCaptureDeviceInfo, const QVariantMap
    #      &traceScreenInfo)
    address = self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine10traceBeginEiNS_22PatternRe'
        'cognitionModeERK4QMapI7QString8QVariantES6_',
        traceId, patternRecognitionMode.value,
        self._valueOf(traceCaptureDeviceInfo),
        self._valueOf(traceScreenInfo),
    )
    from . import QVirtualKeyboardTrace
    return QVirtualKeyboardTrace._cuteAt(address)

  @overload(QVirtualKeyboardTrace)
  @overload(NoneType)
  def traceEnd(self, trace: Optional[QVirtualKeyboardTrace]) -> bool:
    """
    Calls Qt's 'bool
    QVirtualKeyboardInputEngine::traceEnd(QVirtualKeyboardTrace *trace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#traceEnd

    Parameters
    ----------

    trace : Optional[QVirtualKeyboardTrace]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QVirtualKeyboardInputEngine::traceEnd(QVirtualKeyboardTrace
    #      *trace)
    return self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine8traceEndEP21QVirtualKeyboar'
        'dTrace',
        self._addressOf(trace),
    )

  @overload(int)
  def clickPreeditText(self, cursorPosition: int) -> bool:
    """
    Calls Qt's 'bool QVirtualKeyboardInputEngine::clickPreeditText(int
    cursorPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#clickPreeditText

    Parameters
    ----------

    cursorPosition : int
      Passed on as it is.
    """
    #  bool QVirtualKeyboardInputEngine::clickPreeditText(int cursorPosition)
    return self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine16clickPreeditTextEi',
        cursorPosition,
    )

  @overload(Qt.Key, str, Qt.KeyboardModifiers, bool)
  def virtualKeyClicked(
      self,
      key: Qt.Key,
      text: str,
      modifiers: Qt.KeyboardModifiers,
      isAutoRepeat: bool,
  ) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputEngine::virtualKeyClicked(Qt::Key
    key, const QString &text, Qt::KeyboardModifiers modifiers, bool
    isAutoRepeat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#virtualKeyClicked

    Parameters
    ----------

    key : Qt.Key
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    isAutoRepeat : bool
      Passed on as it is.
    """
    #  void QVirtualKeyboardInputEngine::virtualKeyClicked(Qt::Key key, const
    #      QString &text, Qt::KeyboardModifiers modifiers, bool isAutoRepeat)
    self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine17virtualKeyClickedEN2Qt3Key'
        'ERK7QString6QFlagsINS0_16KeyboardModifierEEb',
        key.value, text, modifiers.value, isAutoRepeat,
    )

  @overload(Qt.Key)
  def activeKeyChanged(self, key: Qt.Key) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputEngine::activeKeyChanged(Qt::Key
    key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#activeKeyChanged

    Parameters
    ----------

    key : Qt.Key
      Passed on as its number.
    """
    #  void QVirtualKeyboardInputEngine::activeKeyChanged(Qt::Key key)
    self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine16activeKeyChangedEN2Qt3KeyE',
        key.value,
    )

  @overload(Qt.Key)
  def previousKeyChanged(self, key: Qt.Key) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputEngine::previousKeyChanged(Qt::Key
    key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html

    Parameters
    ----------

    key : Qt.Key
      Passed on as its number.
    """
    #  void QVirtualKeyboardInputEngine::previousKeyChanged(Qt::Key key)
    self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine18previousKeyChangedEN2Qt3Ke'
        'yE',
        key.value,
    )

  def inputMethodChanged(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputEngine::inputMethodChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html
    """
    #  void QVirtualKeyboardInputEngine::inputMethodChanged()
    self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine18inputMethodChangedEv',
    )

  def inputMethodReset(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputEngine::inputMethodReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#inputMethodReset
    """
    #  void QVirtualKeyboardInputEngine::inputMethodReset()
    self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine16inputMethodResetEv',
    )

  def inputMethodUpdate(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputEngine::inputMethodUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#inputMethodUpdate
    """
    #  void QVirtualKeyboardInputEngine::inputMethodUpdate()
    self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine17inputMethodUpdateEv',
    )

  def inputModesChanged(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputEngine::inputModesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#inputModesChanged
    """
    #  void QVirtualKeyboardInputEngine::inputModesChanged()
    self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine17inputModesChangedEv',
    )

  def inputModeChanged(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputEngine::inputModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#inputModeChanged
    """
    #  void QVirtualKeyboardInputEngine::inputModeChanged()
    self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine16inputModeChangedEv',
    )

  def patternRecognitionModesChanged(self) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputEngine::patternRecognitionModesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html
    """
    #  void QVirtualKeyboardInputEngine::patternRecognitionModesChanged()
    self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine30patternRecognitionModesCha'
        'ngedEv',
    )

  def wordCandidateListModelChanged(self) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputEngine::wordCandidateListModelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html
    """
    #  void QVirtualKeyboardInputEngine::wordCandidateListModelChanged()
    self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine29wordCandidateListModelChan'
        'gedEv',
    )

  def wordCandidateListVisibleHintChanged(self) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputEngine::wordCandidateListVisibleHintChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html
    """
    #  void
    #      QVirtualKeyboardInputEngine::wordCandidateListVisibleHintChanged()
    self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine35wordCandidateListVisibleHi'
        'ntChangedEv',
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputEngine::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#reset
    """
    #  void QVirtualKeyboardInputEngine::reset()
    self.uglySide.call('ritual_ZN27QVirtualKeyboardInputEngine5resetEv')

  def update(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputEngine::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#update
    """
    #  void QVirtualKeyboardInputEngine::update()
    self.uglySide.call('ritual_ZN27QVirtualKeyboardInputEngine6updateEv')

  def shiftChanged(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputEngine::shiftChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#shiftChanged
    """
    #  void QVirtualKeyboardInputEngine::shiftChanged()
    self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine12shiftChangedEv',
    )

  def updateSelectionListModels(self) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputEngine::updateSelectionListModels()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html
    """
    #  void QVirtualKeyboardInputEngine::updateSelectionListModels()
    self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine25updateSelectionListModelsE'
        'v',
    )

  def updateInputModes(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputEngine::updateInputModes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#updateInputModes
    """
    #  void QVirtualKeyboardInputEngine::updateInputModes()
    self.uglySide.call(
        'ritual_ZN27QVirtualKeyboardInputEngine16updateInputModesEv',
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, timerEvent: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputEngine::timerEvent(QTimerEvent
    *timerEvent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputengine.html#timerEvent

    Parameters
    ----------

    timerEvent : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVirtualKeyboardInputEngine::timerEvent(QTimerEvent *timerEvent)
    ritual = (
        'ritual_ZN27QVirtualKeyboardInputEngine10timerEventEP11QTimerEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QVirtualKeyboardInputEngine10timerEventEP11QTimer'
          'Event')
    self.uglySide.call(ritual, self._addressOf(timerEvent))

  @staticmethod
  def inputModes(*__, **_) -> Never:
    """
    Qt's 'QList<int> QVirtualKeyboardInputEngine::inputModes() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVirtualKeyboardInputEngine.inputModes' has no cute function yet. "
        "Qt's 'QList<int> QVirtualKeyboardInputEngine::inputModes() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def patternRecognitionModes(*__, **_) -> Never:
    """
    Qt's 'QList<int> QVirtualKeyboardInputEngine::patternRecognitionModes()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVirtualKeyboardInputEngine.patternRecognitionModes' has no cute "
        "function yet. Qt's 'QList<int> "
        "QVirtualKeyboardInputEngine::patternRecognitionModes() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def reselect(*__, **_) -> Never:
    """
    Qt's 'bool QVirtualKeyboardInputEngine::reselect(int cursorPosition,
    const ReselectFlags &reselectFlags)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QVirtualKeyboardInputEngine.reselect' has no cute function yet. "
        "Qt's 'bool QVirtualKeyboardInputEngine::reselect(int "
        "cursorPosition, const ReselectFlags &reselectFlags)': takes a type "
        "Python has no way to hand over yet.")
