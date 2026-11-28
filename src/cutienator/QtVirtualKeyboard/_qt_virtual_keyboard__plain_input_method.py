"""
QtVirtualKeyboard::PlainInputMethod binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/plaininputmethod_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtVirtualKeyboard::PlainInputMethod to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QVirtualKeyboardAbstractInputMethod
from . import QVirtualKeyboardInputEngine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PlainInputMethod(QVirtualKeyboardAbstractInputMethod):
  """
  The cute side of Qt's QtVirtualKeyboard::PlainInputMethod: a plain Python
  object standing in front of one C++ QtVirtualKeyboard::PlainInputMethod.

  It is built on the cute 'QVirtualKeyboardAbstractInputMethod', as Qt's
  QtVirtualKeyboard::PlainInputMethod is built on Qt's
  QVirtualKeyboardAbstractInputMethod, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtVirtualKeyboard::PlainInputMethod that has a
  ritual and that Python can call so far, 7 names in all: 'metaObject', 'tr',
  'setInputMode', 'setTextCase', 'keyEvent', 'reset', 'update'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtVirtualKeyboard::PlainInputMethod::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtVirtualKeyboard::PlainInputMethod::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QtVirtualKeyboard::PlainInputMethod::~PlainInputMethod()': the
    destructor: Python never removes a C++
    QtVirtualKeyboard::PlainInputMethod.
  - Qt's 'QList<QVirtualKeyboardInputEngine::InputMode>
    QtVirtualKeyboard::PlainInputMethod::inputModes(const QString &locale)':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QtVirtualKeyboard::PlainInputMethod is created at the first use,
    not by 'QtVirtualKeyboard::PlainInputMethod(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtVirtualKeyboard::PlainInputMethod.
  - Qt tells when it has removed the C++ QtVirtualKeyboard::PlainInputMethod.
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
    Calls Qt's 'QString QtVirtualKeyboard::PlainInputMethod::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-plaininputmethod.html#tr

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
    #  QString QtVirtualKeyboard::PlainInputMethod::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN17QtVirtualKeyboard16PlainInputMethod2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtVirtualKeyboard::PlainInputMethod'

  #  A C++ QtVirtualKeyboard::PlainInputMethod Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtVirtualKeyboard_PlainInputMethod'

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
    *QtVirtualKeyboard::PlainInputMethod::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-plaininputmethod.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtVirtualKeyboard::PlainInputMethod::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard16PlainInputMethod10metaObjectEv',
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
    Calls Qt's 'bool QtVirtualKeyboard::PlainInputMethod::setInputMode(const
    QString &locale, QVirtualKeyboardInputEngine::InputMode inputMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-plaininputmethod.html

    Parameters
    ----------

    locale : str
      Passed on as it is: a QString is made of it for the call.

    inputMode : QVirtualKeyboardInputEngine.InputMode
      Passed on as its number.
    """
    #  bool QtVirtualKeyboard::PlainInputMethod::setInputMode(const QString
    #      &locale, QVirtualKeyboardInputEngine::InputMode inputMode)
    ritual = (
        'ritual_ZN17QtVirtualKeyboard16PlainInputMethod12setInputModeERK7QS'
        'tringN27QVirtualKeyboardInputEngine9InputModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard16PlainInputMethod12setInputMode'
          'ERK7QStringN27QVirtualKeyboardInputEngine9InputModeE')
    return self.uglySide.call(ritual, locale, inputMode.value)

  @overload(QVirtualKeyboardInputEngine.TextCase)
  def setTextCase(
      self,
      textCase: QVirtualKeyboardInputEngine.TextCase,
  ) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::PlainInputMethod::setTextCase(
    QVirtualKeyboardInputEngine::TextCase textCase)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-plaininputmethod.html

    Parameters
    ----------

    textCase : QVirtualKeyboardInputEngine.TextCase
      Passed on as its number.
    """
    #  bool QtVirtualKeyboard::PlainInputMethod::setTextCase(
    #      QVirtualKeyboardInputEngine::TextCase textCase)
    ritual = (
        'ritual_ZN17QtVirtualKeyboard16PlainInputMethod11setTextCaseEN27QVi'
        'rtualKeyboardInputEngine8TextCaseE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard16PlainInputMethod11setTextCaseE'
          'N27QVirtualKeyboardInputEngine8TextCaseE')
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
    'QtVirtualKeyboard::PlainInputMethod::PlainInputMethod(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-plaininputmethod.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QtVirtualKeyboard::PlainInputMethod::PlainInputMethod(QObject *parent)
    self._noteCreation(PlainInputMethod, lambda: Rituals.call(
        'ritual_ZN17QtVirtualKeyboard16PlainInputMethodC1EP7QObject',
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

  @overload(Qt.Key, str, Qt.KeyboardModifiers)
  def keyEvent(
      self,
      key: Qt.Key,
      text: str,
      modifiers: Qt.KeyboardModifiers,
  ) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::PlainInputMethod::keyEvent(Qt::Key
    key, const QString &text, Qt::KeyboardModifiers modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-plaininputmethod.html#keyEvent

    Parameters
    ----------

    key : Qt.Key
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  bool QtVirtualKeyboard::PlainInputMethod::keyEvent(Qt::Key key, const
    #      QString &text, Qt::KeyboardModifiers modifiers)
    ritual = (
        'ritual_ZN17QtVirtualKeyboard16PlainInputMethod8keyEventEN2Qt3KeyER'
        'K7QString6QFlagsINS1_16KeyboardModifierEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard16PlainInputMethod8keyEventEN2Qt'
          '3KeyERK7QString6QFlagsINS1_16KeyboardModifierEE')
    return self.uglySide.call(ritual, key.value, text, modifiers.value)

  def reset(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::PlainInputMethod::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-plaininputmethod.html#reset
    """
    #  void QtVirtualKeyboard::PlainInputMethod::reset()
    ritual = 'ritual_ZN17QtVirtualKeyboard16PlainInputMethod5resetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QtVirtualKeyboard16PlainInputMethod5resetEv'
    self.uglySide.call(ritual)

  def update(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::PlainInputMethod::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-plaininputmethod.html#update
    """
    #  void QtVirtualKeyboard::PlainInputMethod::update()
    ritual = 'ritual_ZN17QtVirtualKeyboard16PlainInputMethod6updateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QtVirtualKeyboard16PlainInputMethod6updateEv'
    self.uglySide.call(ritual)
