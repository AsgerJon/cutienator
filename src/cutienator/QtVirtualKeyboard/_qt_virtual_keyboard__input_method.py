"""
QtVirtualKeyboard::InputMethod binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/inputmethod_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtVirtualKeyboard::InputMethod to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QMap, QObject
from . import QVirtualKeyboardAbstractInputMethod
from . import QVirtualKeyboardInputEngine, QVirtualKeyboardSelectionListModel
from . import QtVirtualKeyboard

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QVirtualKeyboardTrace
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']
  QVirtualKeyboardTrace = WAIT['QVirtualKeyboardTrace']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class InputMethod(QVirtualKeyboardAbstractInputMethod):
  """
  The cute side of Qt's QtVirtualKeyboard::InputMethod: a plain Python object
  standing in front of one C++ QtVirtualKeyboard::InputMethod.

  It is built on the cute 'QVirtualKeyboardAbstractInputMethod', as Qt's
  QtVirtualKeyboard::InputMethod is built on Qt's
  QVirtualKeyboardAbstractInputMethod, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtVirtualKeyboard::InputMethod that has a ritual and
  that Python can call so far, 15 names in all: 'metaObject', 'tr', 'd_func',
  'setInputMode', 'setTextCase', 'keyEvent', 'selectionListItemCount',
  'selectionListData', 'selectionListItemSelected', 'traceBegin', 'traceEnd',
  'clickPreeditText', 'reset', 'update', 'clearInputMode'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtVirtualKeyboard::InputMethod::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QtVirtualKeyboard::InputMethod::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const InputMethodPrivate *QtVirtualKeyboard::InputMethod::d_func()
    const': takes in Python what 'InputMethodPrivate
    *QtVirtualKeyboard::InputMethod::d_func()' takes.
  - Qt's 'QtVirtualKeyboard::InputMethod::~InputMethod()': the destructor:
    Python never removes a C++ QtVirtualKeyboard::InputMethod.
  - Qt's 'QList<QVirtualKeyboardInputEngine::InputMode>
    QtVirtualKeyboard::InputMethod::inputModes(const QString &locale)': gives
    a type Python has no way to take yet.
  - Qt's 'QList<QVirtualKeyboardSelectionListModel::Type>
    QtVirtualKeyboard::InputMethod::selectionLists()': gives a type Python
    has no way to take yet.
  - Qt's 'QList<QVirtualKeyboardInputEngine::PatternRecognitionMode>
    QtVirtualKeyboard::InputMethod::patternRecognitionModes() const': gives a
    type Python has no way to take yet.
  - Qt's 'bool QtVirtualKeyboard::InputMethod::reselect(int cursorPosition,
    const QVirtualKeyboardInputEngine::ReselectFlags &reselectFlags)': takes
    a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QtVirtualKeyboard::InputMethod is created at the first use, not
    by 'QtVirtualKeyboard::InputMethod(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtVirtualKeyboard::InputMethod.
  - Qt tells when it has removed the C++ QtVirtualKeyboard::InputMethod.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QtVirtualKeyboard::InputMethod::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-inputmethod.html#tr

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
    #  QString QtVirtualKeyboard::InputMethod::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN17QtVirtualKeyboard11InputMethod2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtVirtualKeyboard::InputMethod'

  #  A C++ QtVirtualKeyboard::InputMethod Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtVirtualKeyboard_InputMethod'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QtVirtualKeyboard::InputMethod::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-inputmethod.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtVirtualKeyboard::InputMethod::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard11InputMethod10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, QVirtualKeyboardInputEngine.InputMode)
  def setInputMode(
      self,
      locale: str,
      inputMode: QVirtualKeyboardInputEngine.InputMode,
  ) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::InputMethod::setInputMode(const
    QString &locale, QVirtualKeyboardInputEngine::InputMode inputMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-inputmethod.html#setInputMode

    Parameters
    ----------

    locale : str
      Passed on as it is: a QString is made of it for the call.

    inputMode : QVirtualKeyboardInputEngine.InputMode
      Passed on as its number.
    """
    #  bool QtVirtualKeyboard::InputMethod::setInputMode(const QString
    #      &locale, QVirtualKeyboardInputEngine::InputMode inputMode)
    ritual = (
        'ritual_ZN17QtVirtualKeyboard11InputMethod12setInputModeERK7QString'
        'N27QVirtualKeyboardInputEngine9InputModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard11InputMethod12setInputModeERK7Q'
          'StringN27QVirtualKeyboardInputEngine9InputModeE')
    return self.uglySide.call(ritual, locale, inputMode.value)

  @overload(QVirtualKeyboardInputEngine.TextCase)
  def setTextCase(
      self,
      textCase: QVirtualKeyboardInputEngine.TextCase,
  ) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::InputMethod::setTextCase(
    QVirtualKeyboardInputEngine::TextCase textCase)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-inputmethod.html#setTextCase

    Parameters
    ----------

    textCase : QVirtualKeyboardInputEngine.TextCase
      Passed on as its number.
    """
    #  bool QtVirtualKeyboard::InputMethod::setTextCase(
    #      QVirtualKeyboardInputEngine::TextCase textCase)
    ritual = (
        'ritual_ZN17QtVirtualKeyboard11InputMethod11setTextCaseEN27QVirtual'
        'KeyboardInputEngine8TextCaseE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard11InputMethod11setTextCaseEN27QV'
          'irtualKeyboardInputEngine8TextCaseE')
    return self.uglySide.call(ritual, textCase.value)

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
    Notes what was given, for Qt's
    'QtVirtualKeyboard::InputMethod::InputMethod(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-inputmethod.html#InputMethod

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QtVirtualKeyboard::InputMethod::InputMethod(QObject *parent)
    self._noteCreation(InputMethod, lambda: Rituals.call(
        'ritual_ZN17QtVirtualKeyboard11InputMethodC1EP7QObject',
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

  def d_func(self) -> Optional[QtVirtualKeyboard.InputMethodPrivate]:
    """
    Calls Qt's 'InputMethodPrivate
    *QtVirtualKeyboard::InputMethod::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-inputmethod.html#d_func

    Returns
    -------

    Optional[QtVirtualKeyboard.InputMethodPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  InputMethodPrivate *QtVirtualKeyboard::InputMethod::d_func()
    address = self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard11InputMethod6d_funcEv',
    )
    return QtVirtualKeyboard.InputMethodPrivate._cuteAt(address)

  @overload(Qt.Key, str, Qt.KeyboardModifiers)
  def keyEvent(
      self,
      key: Qt.Key,
      text: str,
      modifiers: Qt.KeyboardModifiers,
  ) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::InputMethod::keyEvent(Qt::Key key,
    const QString &text, Qt::KeyboardModifiers modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-inputmethod.html#keyEvent

    Parameters
    ----------

    key : Qt.Key
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  bool QtVirtualKeyboard::InputMethod::keyEvent(Qt::Key key, const
    #      QString &text, Qt::KeyboardModifiers modifiers)
    ritual = (
        'ritual_ZN17QtVirtualKeyboard11InputMethod8keyEventEN2Qt3KeyERK7QSt'
        'ring6QFlagsINS1_16KeyboardModifierEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard11InputMethod8keyEventEN2Qt3KeyE'
          'RK7QString6QFlagsINS1_16KeyboardModifierEE')
    return self.uglySide.call(ritual, key.value, text, modifiers.value)

  @overload(QVirtualKeyboardSelectionListModel.Type)
  def selectionListItemCount(
      self,
      type: QVirtualKeyboardSelectionListModel.Type,
  ) -> int:
    """
    Calls Qt's 'int QtVirtualKeyboard::InputMethod::selectionListItemCount(
    QVirtualKeyboardSelectionListModel::Type type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-inputmethod.html

    Parameters
    ----------

    type : QVirtualKeyboardSelectionListModel.Type
      Passed on as its number.
    """
    #  int QtVirtualKeyboard::InputMethod::selectionListItemCount(
    #      QVirtualKeyboardSelectionListModel::Type type)
    ritual = (
        'ritual_ZN17QtVirtualKeyboard11InputMethod22selectionListItemCountE'
        'N34QVirtualKeyboardSelectionListModel4TypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard11InputMethod22selectionListItem'
          'CountEN34QVirtualKeyboardSelectionListModel4TypeE')
    return self.uglySide.call(ritual, type.value)

  @overload(
      QVirtualKeyboardSelectionListModel.Type, int,
      QVirtualKeyboardSelectionListModel.Role,
  )
  def selectionListData(
      self,
      type: QVirtualKeyboardSelectionListModel.Type,
      index: int,
      role: QVirtualKeyboardSelectionListModel.Role,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QtVirtualKeyboard::InputMethod::selectionListData(
    QVirtualKeyboardSelectionListModel::Type type, int index,
    QVirtualKeyboardSelectionListModel::Role role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-inputmethod.html

    Parameters
    ----------

    type : QVirtualKeyboardSelectionListModel.Type
      Passed on as its number.

    index : int
      Passed on as it is.

    role : QVirtualKeyboardSelectionListModel.Role
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QtVirtualKeyboard::InputMethod::selectionListData(
    #      QVirtualKeyboardSelectionListModel::Type type, int index,
    #      QVirtualKeyboardSelectionListModel::Role role)
    ritual = (
        'ritual_ZN17QtVirtualKeyboard11InputMethod17selectionListDataEN34QV'
        'irtualKeyboardSelectionListModel4TypeEiNS1_4RoleE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard11InputMethod17selectionListData'
          'EN34QVirtualKeyboardSelectionListModel4TypeEiNS1_4RoleE')
    address = self.uglySide.call(ritual, type.value, index, role.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QVirtualKeyboardSelectionListModel.Type, int)
  def selectionListItemSelected(
      self,
      type: QVirtualKeyboardSelectionListModel.Type,
      index: int,
  ) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::InputMethod::selectionListItemSelected(
    QVirtualKeyboardSelectionListModel::Type type, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-inputmethod.html

    Parameters
    ----------

    type : QVirtualKeyboardSelectionListModel.Type
      Passed on as its number.

    index : int
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::InputMethod::selectionListItemSelected(
    #      QVirtualKeyboardSelectionListModel::Type type, int index)
    ritual = (
        'ritual_ZN17QtVirtualKeyboard11InputMethod25selectionListItemSelect'
        'edEN34QVirtualKeyboardSelectionListModel4TypeEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard11InputMethod25selectionListItem'
          'SelectedEN34QVirtualKeyboardSelectionListModel4TypeEi')
    self.uglySide.call(ritual, type.value, index)

  @overload(
      int, QVirtualKeyboardInputEngine.PatternRecognitionMode, QMap[str,
      QVariant], QMap[str, QVariant],
  )
  def traceBegin(
      self,
      traceId: int,
      patternRecognitionMode: QVirtualKeyboardInputEngine.PatternRecognitionMode,
      traceCaptureDeviceInfo: QMap[str, QVariant],
      traceScreenInfo: QMap[str, QVariant],
  ) -> Optional[QVirtualKeyboardTrace]:
    """
    Calls Qt's 'QVirtualKeyboardTrace
    *QtVirtualKeyboard::InputMethod::traceBegin(int traceId,
    QVirtualKeyboardInputEngine::PatternRecognitionMode
    patternRecognitionMode, const QVariantMap &traceCaptureDeviceInfo, const
    QVariantMap &traceScreenInfo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-inputmethod.html#traceBegin

    Parameters
    ----------

    traceId : int
      Passed on as it is.

    patternRecognitionMode : QVirtualKeyboardInputEngine.PatternRecognitionMode
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
    #  QVirtualKeyboardTrace *QtVirtualKeyboard::InputMethod::traceBegin(int
    #      traceId, QVirtualKeyboardInputEngine::PatternRecognitionMode
    #      patternRecognitionMode, const QVariantMap &traceCaptureDeviceInfo,
    #      const QVariantMap &traceScreenInfo)
    address = self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard11InputMethod10traceBeginEiN27QVirtual'
        'KeyboardInputEngine22PatternRecognitionModeERK4QMapI7QString8QVari'
        'antES8_',
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
    QtVirtualKeyboard::InputMethod::traceEnd(QVirtualKeyboardTrace *trace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-inputmethod.html#traceEnd

    Parameters
    ----------

    trace : Optional[QVirtualKeyboardTrace]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QtVirtualKeyboard::InputMethod::traceEnd(QVirtualKeyboardTrace
    #      *trace)
    ritual = (
        'ritual_ZN17QtVirtualKeyboard11InputMethod8traceEndEP21QVirtualKeyb'
        'oardTrace')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard11InputMethod8traceEndEP21QVirtu'
          'alKeyboardTrace')
    return self.uglySide.call(ritual, self._addressOf(trace))

  @overload(int)
  def clickPreeditText(self, cursorPosition: int) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::InputMethod::clickPreeditText(int
    cursorPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-inputmethod.html

    Parameters
    ----------

    cursorPosition : int
      Passed on as it is.
    """
    #  bool QtVirtualKeyboard::InputMethod::clickPreeditText(int
    #      cursorPosition)
    ritual = 'ritual_ZN17QtVirtualKeyboard11InputMethod16clickPreeditTextEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard11InputMethod16clickPreeditTextE'
          'i')
    return self.uglySide.call(ritual, cursorPosition)

  def reset(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::InputMethod::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-inputmethod.html#reset
    """
    #  void QtVirtualKeyboard::InputMethod::reset()
    ritual = 'ritual_ZN17QtVirtualKeyboard11InputMethod5resetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QtVirtualKeyboard11InputMethod5resetEv'
    self.uglySide.call(ritual)

  def update(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::InputMethod::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-inputmethod.html#update
    """
    #  void QtVirtualKeyboard::InputMethod::update()
    ritual = 'ritual_ZN17QtVirtualKeyboard11InputMethod6updateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QtVirtualKeyboard11InputMethod6updateEv'
    self.uglySide.call(ritual)

  def clearInputMode(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::InputMethod::clearInputMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-inputmethod.html#clearInputMode
    """
    #  void QtVirtualKeyboard::InputMethod::clearInputMode()
    ritual = 'ritual_ZN17QtVirtualKeyboard11InputMethod14clearInputModeEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard11InputMethod14clearInputModeEv')
    self.uglySide.call(ritual)
