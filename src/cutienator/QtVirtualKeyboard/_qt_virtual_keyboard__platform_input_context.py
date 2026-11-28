"""
QtVirtualKeyboard::PlatformInputContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/platforminputcontext_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtVirtualKeyboard::PlatformInputContext to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtGui import QInputMethod, QPlatformInputContext

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QLocale, QMetaObject, QRectF, QVariant
  from ..QtGui import QKeyEvent
  from . import QVirtualKeyboardInputContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QLocale = WAIT['QLocale']
  QVirtualKeyboardInputContext = WAIT['QVirtualKeyboardInputContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PlatformInputContext(QPlatformInputContext):
  """
  The cute side of Qt's QtVirtualKeyboard::PlatformInputContext: a plain
  Python object standing in front of one C++
  QtVirtualKeyboard::PlatformInputContext.

  It is built on the cute 'QPlatformInputContext', as Qt's
  QtVirtualKeyboard::PlatformInputContext is built on Qt's
  QPlatformInputContext, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtVirtualKeyboard::PlatformInputContext that has a
  ritual and that Python can call so far, 28 names in all: 'metaObject',
  'tr', 'isValid', 'reset', 'commit', 'update', 'invokeAction',
  'keyboardRect', 'isAnimating', 'showInputPanel', 'hideInputPanel',
  'isInputPanelVisible', 'locale', 'setLocale', 'inputDirection',
  'setInputDirection', 'focusObject', 'setFocusObject', 'inputContext',
  'eventFilter', 'focusObjectChanged', 'sendEvent', 'sendKeyEvent',
  'inputMethodQuery', 'setInputContext', 'evaluateInputPanelVisible',
  'keyboardRectangleChanged', 'updateInputPanelVisible'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtVirtualKeyboard::PlatformInputContext::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtVirtualKeyboard::PlatformInputContext::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QtVirtualKeyboard::PlatformInputContext::~PlatformInputContext()':
    the destructor: Python never removes a C++
    QtVirtualKeyboard::PlatformInputContext.

  What has no ritual
  ------------------

  2 of the 34 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QtVirtualKeyboard::PlatformInputContext is created at the first
    use, not by 'QtVirtualKeyboard::PlatformInputContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtVirtualKeyboard::PlatformInputContext.
  - Qt tells when it has removed the C++
    QtVirtualKeyboard::PlatformInputContext. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
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
    Calls Qt's 'QString QtVirtualKeyboard::PlatformInputContext::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html#tr

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
    #  QString QtVirtualKeyboard::PlatformInputContext::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QtVirtualKeyboard20PlatformInputContext2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtVirtualKeyboard::PlatformInputContext'

  #  A C++ QtVirtualKeyboard::PlatformInputContext Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtVirtualKeyboard_PlatformInputContext'

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
    *QtVirtualKeyboard::PlatformInputContext::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtVirtualKeyboard::PlatformInputContext::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard20PlatformInputContext10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::PlatformInputContext::isValid()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html
    """
    #  bool QtVirtualKeyboard::PlatformInputContext::isValid() const
    ritual = 'ritual_ZNK17QtVirtualKeyboard20PlatformInputContext7isValidEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QtVirtualKeyboard20PlatformInputContext7isValidE'
          'v')
    return self.uglySide.call(ritual)

  def keyboardRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF
    QtVirtualKeyboard::PlatformInputContext::keyboardRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QtVirtualKeyboard::PlatformInputContext::keyboardRect() const
    ritual = (
        'ritual_ZNK17QtVirtualKeyboard20PlatformInputContext12keyboardRectE'
        'v')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QtVirtualKeyboard20PlatformInputContext12keyboar'
          'dRectEv')
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def isAnimating(self) -> bool:
    """
    Calls Qt's 'bool QtVirtualKeyboard::PlatformInputContext::isAnimating()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html
    """
    #  bool QtVirtualKeyboard::PlatformInputContext::isAnimating() const
    ritual = (
        'ritual_ZNK17QtVirtualKeyboard20PlatformInputContext11isAnimatingEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QtVirtualKeyboard20PlatformInputContext11isAnima'
          'tingEv')
    return self.uglySide.call(ritual)

  def isInputPanelVisible(self) -> bool:
    """
    Calls Qt's 'bool
    QtVirtualKeyboard::PlatformInputContext::isInputPanelVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html
    """
    #  bool QtVirtualKeyboard::PlatformInputContext::isInputPanelVisible()
    #      const
    ritual = (
        'ritual_ZNK17QtVirtualKeyboard20PlatformInputContext19isInputPanelV'
        'isibleEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QtVirtualKeyboard20PlatformInputContext19isInput'
          'PanelVisibleEv')
    return self.uglySide.call(ritual)

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QtVirtualKeyboard::PlatformInputContext::locale()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QtVirtualKeyboard::PlatformInputContext::locale() const
    ritual = 'ritual_ZNK17QtVirtualKeyboard20PlatformInputContext6localeEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QtVirtualKeyboard20PlatformInputContext6localeEv')
    address = self.uglySide.call(ritual)
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  def inputDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection
    QtVirtualKeyboard::PlatformInputContext::inputDirection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection
    #      QtVirtualKeyboard::PlatformInputContext::inputDirection() const
    ritual = (
        'ritual_ZNK17QtVirtualKeyboard20PlatformInputContext14inputDirectio'
        'nEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QtVirtualKeyboard20PlatformInputContext14inputDi'
          'rectionEv')
    return Qt.LayoutDirection(self.uglySide.call(ritual))

  def inputContext(self) -> Optional[QVirtualKeyboardInputContext]:
    """
    Calls Qt's 'QVirtualKeyboardInputContext
    *QtVirtualKeyboard::PlatformInputContext::inputContext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html

    Returns
    -------

    Optional[QVirtualKeyboardInputContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVirtualKeyboardInputContext
    #      *QtVirtualKeyboard::PlatformInputContext::inputContext() const
    address = self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard20PlatformInputContext12inputContextE'
        'v',
    )
    from . import QVirtualKeyboardInputContext
    return QVirtualKeyboardInputContext._cuteAt(address)

  def evaluateInputPanelVisible(self) -> bool:
    """
    Calls Qt's 'bool
    QtVirtualKeyboard::PlatformInputContext::evaluateInputPanelVisible()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html
    """
    #  bool QtVirtualKeyboard::PlatformInputContext::
    #      evaluateInputPanelVisible() const
    return self.uglySide.call(
        'ritual_ZNK17QtVirtualKeyboard20PlatformInputContext25evaluateInput'
        'PanelVisibleEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::PlatformInputContext::setLocale(QLocale locale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QtVirtualKeyboard::PlatformInputContext::setLocale(QLocale
    #      locale)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard20PlatformInputContext9setLocaleE7QLoc'
        'ale',
        self._valueOf(locale),
    )

  @overload(Qt.LayoutDirection)
  def setInputDirection(self, direction: Qt.LayoutDirection) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::PlatformInputContext::setInputDirection(Qt::
    LayoutDirection direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html

    Parameters
    ----------

    direction : Qt.LayoutDirection
      Passed on as its number.
    """
    #  void QtVirtualKeyboard::PlatformInputContext::setInputDirection(Qt::
    #      LayoutDirection direction)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard20PlatformInputContext17setInputDirect'
        'ionEN2Qt15LayoutDirectionE',
        direction.value,
    )

  @overload(QObject)
  @overload(NoneType)
  def setFocusObject(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::PlatformInputContext::setFocusObject(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtVirtualKeyboard::PlatformInputContext::setFocusObject(QObject
    #      *object)
    ritual = (
        'ritual_ZN17QtVirtualKeyboard20PlatformInputContext14setFocusObject'
        'EP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard20PlatformInputContext14setFocus'
          'ObjectEP7QObject')
    self.uglySide.call(ritual, self._addressOf(object, 'QObject'))

  @overload(QVirtualKeyboardInputContext)
  @overload(NoneType)
  def setInputContext(
      self,
      context: Optional[QVirtualKeyboardInputContext],
  ) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::PlatformInputContext::setInputContext(
    QVirtualKeyboardInputContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html

    Parameters
    ----------

    context : Optional[QVirtualKeyboardInputContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtVirtualKeyboard::PlatformInputContext::setInputContext(
    #      QVirtualKeyboardInputContext *context)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard20PlatformInputContext15setInputContex'
        'tEP28QVirtualKeyboardInputContext',
        self._addressOf(context),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QtVirtualKeyboard::PlatformInputContext::PlatformInputContext()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html
    """
    #  QtVirtualKeyboard::PlatformInputContext::PlatformInputContext()
    self._noteCreation(PlatformInputContext, lambda: Rituals.call(
        'ritual_ZN17QtVirtualKeyboard20PlatformInputContextC1Ev',
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

  def reset(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::PlatformInputContext::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html#reset
    """
    #  void QtVirtualKeyboard::PlatformInputContext::reset()
    ritual = 'ritual_ZN17QtVirtualKeyboard20PlatformInputContext5resetEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard20PlatformInputContext5resetEv')
    self.uglySide.call(ritual)

  def commit(self) -> None:
    """
    Calls Qt's 'void QtVirtualKeyboard::PlatformInputContext::commit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html#commit
    """
    #  void QtVirtualKeyboard::PlatformInputContext::commit()
    ritual = 'ritual_ZN17QtVirtualKeyboard20PlatformInputContext6commitEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard20PlatformInputContext6commitEv')
    self.uglySide.call(ritual)

  @overload(Qt.InputMethodQueries)
  def update(self, queries: Qt.InputMethodQueries) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::PlatformInputContext::update(Qt::InputMethodQueries
    queries)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html#update

    Parameters
    ----------

    queries : Qt.InputMethodQueries
      Passed on as its number.
    """
    #  void QtVirtualKeyboard::PlatformInputContext::update(Qt::
    #      InputMethodQueries queries)
    ritual = (
        'ritual_ZN17QtVirtualKeyboard20PlatformInputContext6updateE6QFlagsI'
        'N2Qt16InputMethodQueryEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard20PlatformInputContext6updateE6Q'
          'FlagsIN2Qt16InputMethodQueryEE')
    self.uglySide.call(ritual, queries.value)

  @overload(QInputMethod.Action, int)
  def invokeAction(
      self,
      action: QInputMethod.Action,
      cursorPosition: int,
  ) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::PlatformInputContext::invokeAction(QInputMethod::
    Action action, int cursorPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html

    Parameters
    ----------

    action : QInputMethod.Action
      Passed on as its number.

    cursorPosition : int
      Passed on as it is.
    """
    #  void QtVirtualKeyboard::PlatformInputContext::invokeAction(
    #      QInputMethod::Action action, int cursorPosition)
    ritual = (
        'ritual_ZN17QtVirtualKeyboard20PlatformInputContext12invokeActionEN'
        '12QInputMethod6ActionEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard20PlatformInputContext12invokeAc'
          'tionEN12QInputMethod6ActionEi')
    self.uglySide.call(ritual, action.value, cursorPosition)

  def showInputPanel(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::PlatformInputContext::showInputPanel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html
    """
    #  void QtVirtualKeyboard::PlatformInputContext::showInputPanel()
    ritual = (
        'ritual_ZN17QtVirtualKeyboard20PlatformInputContext14showInputPanel'
        'Ev')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard20PlatformInputContext14showInpu'
          'tPanelEv')
    self.uglySide.call(ritual)

  def hideInputPanel(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::PlatformInputContext::hideInputPanel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html
    """
    #  void QtVirtualKeyboard::PlatformInputContext::hideInputPanel()
    ritual = (
        'ritual_ZN17QtVirtualKeyboard20PlatformInputContext14hideInputPanel'
        'Ev')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard20PlatformInputContext14hideInpu'
          'tPanelEv')
    self.uglySide.call(ritual)

  def focusObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject
    *QtVirtualKeyboard::PlatformInputContext::focusObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QtVirtualKeyboard::PlatformInputContext::focusObject()
    address = self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard20PlatformInputContext11focusObjectEv',
    )
    return QObject._cuteAt(address)

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
    Calls Qt's 'bool
    QtVirtualKeyboard::PlatformInputContext::eventFilter(QObject *object,
    QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QtVirtualKeyboard::PlatformInputContext::eventFilter(QObject
    #      *object, QEvent *event)
    ritual = (
        'ritual_ZN17QtVirtualKeyboard20PlatformInputContext11eventFilterEP7'
        'QObjectP6QEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QtVirtualKeyboard20PlatformInputContext11eventFil'
          'terEP7QObjectP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(object, 'QObject'), self._addressOf(event),
    )

  def focusObjectChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::PlatformInputContext::focusObjectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html
    """
    #  void QtVirtualKeyboard::PlatformInputContext::focusObjectChanged()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard20PlatformInputContext18focusObjectCha'
        'ngedEv',
    )

  @overload(QEvent)
  @overload(NoneType)
  def sendEvent(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::PlatformInputContext::sendEvent(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtVirtualKeyboard::PlatformInputContext::sendEvent(QEvent *event)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard20PlatformInputContext9sendEventEP6QEv'
        'ent',
        self._addressOf(event),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def sendKeyEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::PlatformInputContext::sendKeyEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtVirtualKeyboard::PlatformInputContext::sendKeyEvent(QKeyEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard20PlatformInputContext12sendKeyEventEP'
        '9QKeyEvent',
        self._addressOf(event),
    )

  @overload(Qt.InputMethodQuery)
  def inputMethodQuery(self, query: Qt.InputMethodQuery) -> QVariant:
    """
    Calls Qt's 'QVariant
    QtVirtualKeyboard::PlatformInputContext::inputMethodQuery(Qt::
    InputMethodQuery query)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html

    Parameters
    ----------

    query : Qt.InputMethodQuery
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant
    #      QtVirtualKeyboard::PlatformInputContext::inputMethodQuery(Qt::
    #      InputMethodQuery query)
    address = self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard20PlatformInputContext16inputMethodQue'
        'ryEN2Qt16InputMethodQueryE',
        query.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def keyboardRectangleChanged(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::PlatformInputContext::keyboardRectangleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html
    """
    #  void
    #      QtVirtualKeyboard::PlatformInputContext::keyboardRectangleChanged(
    #      )
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard20PlatformInputContext24keyboardRectan'
        'gleChangedEv',
    )

  def updateInputPanelVisible(self) -> None:
    """
    Calls Qt's 'void
    QtVirtualKeyboard::PlatformInputContext::updateInputPanelVisible()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtvirtualkeyboard-platforminputcontext.html
    """
    #  void
    #      QtVirtualKeyboard::PlatformInputContext::updateInputPanelVisible()
    self.uglySide.call(
        'ritual_ZN17QtVirtualKeyboard20PlatformInputContext23updateInputPan'
        'elVisibleEv',
    )
