"""
QVirtualKeyboardInputContextPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboardinputcontext_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QVirtualKeyboardInputContextPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject, QStringList
from ..QtGui import QInputMethod
from . import QtVirtualKeyboard

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QPointF, QRectF, QUrl
  from ..QtGui import QInputMethodEvent
  from . import QVirtualKeyboardInputContext, QVirtualKeyboardObserver
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QInputMethodEvent = WAIT['QInputMethodEvent']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QUrl = WAIT['QUrl']
  QVirtualKeyboardInputContext = WAIT['QVirtualKeyboardInputContext']
  QVirtualKeyboardObserver = WAIT['QVirtualKeyboardObserver']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVirtualKeyboardInputContextPrivate(QObject):
  """
  The cute side of Qt's QVirtualKeyboardInputContextPrivate: a plain Python
  object standing in front of one C++ QVirtualKeyboardInputContextPrivate.

  It is built on the cute 'QObject', as Qt's
  QVirtualKeyboardInputContextPrivate is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QVirtualKeyboardInputContextPrivate that has a
  ritual and that Python can call so far, 44 names in all: 'metaObject',
  'tr', 'q_func', 'init', 'focus', 'setFocus', 'keyboardRectangle',
  'setKeyboardRectangle', 'previewRectangle', 'setPreviewRectangle',
  'previewVisible', 'setPreviewVisible', 'locale', 'setLocale', 'inputItem',
  'shiftHandler', 'shadow', 'setKeyboardObserver', 'fileExists',
  'hasEnterKeyAction', 'registerInputPanel', 'contains',
  'keyboardFunctionKey', 'focusChanged', 'keyboardRectangleChanged',
  'previewRectangleChanged', 'previewVisibleChanged', 'localeChanged',
  'inputItemChanged', 'navigationKeyPressed', 'navigationKeyReleased',
  'hideInputPanel', 'updateAvailableLocales', 'forceCursorPosition',
  'onInputItemChanged', 'sendInputMethodEvent', 'reset', 'commit', 'update',
  'invokeAction', 'maybeCloseOnReturn', 'filterEvent', 'isEmptyState',
  'updateSelectionControlVisible'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QVirtualKeyboardInputContextPrivate::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QVirtualKeyboardInputContextPrivate::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QVirtualKeyboardInputContext
    *QVirtualKeyboardInputContextPrivate::q_func() const': takes in Python
    what 'QVirtualKeyboardInputContext
    *QVirtualKeyboardInputContextPrivate::q_func()' takes.
  - Qt's 'void
    QVirtualKeyboardInputContextPrivate::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'QVirtualKeyboardInputContextPrivate::
    ~QVirtualKeyboardInputContextPrivate()': the destructor: Python never
    removes a C++ QVirtualKeyboardInputContextPrivate.
  - Qt's 'void QVirtualKeyboardInputContextPrivate::sendPreedit(const QString
    &text, const QList<QInputMethodEvent::Attribute> &attributes, int
    replaceFrom, int replaceLength)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QVirtualKeyboardInputContextPrivate::addSelectionAttribute(
    QList<QInputMethodEvent::Attribute> &attributes)': takes a type Python
    has no way to hand over yet.
  - Qt's 'bool QVirtualKeyboardInputContextPrivate::testAttribute(const
    QList<QInputMethodEvent::Attribute> &attributes,
    QInputMethodEvent::AttributeType attributeType) const': takes a type
    Python has no way to hand over yet.
  - Qt's 'int QVirtualKeyboardInputContextPrivate::findAttribute(const
    QList<QInputMethodEvent::Attribute> &attributes,
    QInputMethodEvent::AttributeType attributeType) const': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QVirtualKeyboardInputContextPrivate::setState(const State
    &state)': takes a type Python has no way to hand over yet.
  - Qt's 'void QVirtualKeyboardInputContextPrivate::clearState(const State
    &state)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QVirtualKeyboardInputContextPrivate::testState(const State
    &state) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 59 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QVirtualKeyboardInputContextPrivate is created at the first use,
    not by 'QVirtualKeyboardInputContextPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVirtualKeyboardInputContextPrivate.
  - Qt tells when it has removed the C++ QVirtualKeyboardInputContextPrivate.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QVirtualKeyboardInputContextPrivate that has no cute
    function yet, 'addSelectionAttribute', 'clearState', 'findAttribute',
    'sendPreedit', 'setState', 'testAttribute', 'testState', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QVirtualKeyboardInputContextPrivate, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class State(CuteFlags, scoped=True):
    """
    The flags enum 'QVirtualKeyboardInputContextPrivate::State' of Qt, with
    the 6 names Qt gives in it. Qt names the type of its combinations
    'QVirtualKeyboardInputContextPrivate::StateFlags'. C++ keeps these names
    inside the enum, so the class that holds the enum does not have them.
    """

    Reselect = 0x1
    InputMethodEvent = 0x2
    KeyEvent = 0x4
    InputMethodClick = 0x8
    SyncShadowInput = 0x10
    SetFocus = 0x20

  StateFlags = State

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
    Calls Qt's 'QString QVirtualKeyboardInputContextPrivate::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html#tr

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
    #  QString QVirtualKeyboardInputContextPrivate::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVirtualKeyboardInputContextPrivate'

  #  A C++ QVirtualKeyboardInputContextPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVirtualKeyboardInputContextPrivate'

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
    *QVirtualKeyboardInputContextPrivate::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QVirtualKeyboardInputContextPrivate::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK35QVirtualKeyboardInputContextPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def focus(self) -> bool:
    """
    Calls Qt's 'bool QVirtualKeyboardInputContextPrivate::focus() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html#focus
    """
    #  bool QVirtualKeyboardInputContextPrivate::focus() const
    return self.uglySide.call(
        'ritual_ZNK35QVirtualKeyboardInputContextPrivate5focusEv',
    )

  def keyboardRectangle(self) -> QRectF:
    """
    Calls Qt's 'QRectF
    QVirtualKeyboardInputContextPrivate::keyboardRectangle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QVirtualKeyboardInputContextPrivate::keyboardRectangle() const
    address = self.uglySide.call(
        'ritual_ZNK35QVirtualKeyboardInputContextPrivate17keyboardRectangle'
        'Ev',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def previewRectangle(self) -> QRectF:
    """
    Calls Qt's 'QRectF
    QVirtualKeyboardInputContextPrivate::previewRectangle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QVirtualKeyboardInputContextPrivate::previewRectangle() const
    address = self.uglySide.call(
        'ritual_ZNK35QVirtualKeyboardInputContextPrivate16previewRectangleE'
        'v',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def previewVisible(self) -> bool:
    """
    Calls Qt's 'bool QVirtualKeyboardInputContextPrivate::previewVisible()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html
    """
    #  bool QVirtualKeyboardInputContextPrivate::previewVisible() const
    return self.uglySide.call(
        'ritual_ZNK35QVirtualKeyboardInputContextPrivate14previewVisibleEv',
    )

  def locale(self) -> str:
    """
    Calls Qt's 'QString QVirtualKeyboardInputContextPrivate::locale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html#locale

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QVirtualKeyboardInputContextPrivate::locale() const
    return self.uglySide.call(
        'ritual_ZNK35QVirtualKeyboardInputContextPrivate6localeEv',
    )

  def inputItem(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QVirtualKeyboardInputContextPrivate::inputItem()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html#inputItem

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QVirtualKeyboardInputContextPrivate::inputItem() const
    address = self.uglySide.call(
        'ritual_ZNK35QVirtualKeyboardInputContextPrivate9inputItemEv',
    )
    return QObject._cuteAt(address)

  def shiftHandler(self) -> Optional[QtVirtualKeyboard.ShiftHandler]:
    """
    Calls Qt's 'QtVirtualKeyboard::ShiftHandler
    *QVirtualKeyboardInputContextPrivate::shiftHandler() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html

    Returns
    -------

    Optional[QtVirtualKeyboard.ShiftHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtVirtualKeyboard::ShiftHandler
    #      *QVirtualKeyboardInputContextPrivate::shiftHandler() const
    address = self.uglySide.call(
        'ritual_ZNK35QVirtualKeyboardInputContextPrivate12shiftHandlerEv',
    )
    return QtVirtualKeyboard.ShiftHandler._cuteAt(address)

  def shadow(self) -> Optional[QtVirtualKeyboard.ShadowInputContext]:
    """
    Calls Qt's 'QtVirtualKeyboard::ShadowInputContext
    *QVirtualKeyboardInputContextPrivate::shadow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html#shadow

    Returns
    -------

    Optional[QtVirtualKeyboard.ShadowInputContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtVirtualKeyboard::ShadowInputContext
    #      *QVirtualKeyboardInputContextPrivate::shadow() const
    address = self.uglySide.call(
        'ritual_ZNK35QVirtualKeyboardInputContextPrivate6shadowEv',
    )
    return QtVirtualKeyboard.ShadowInputContext._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  def hasEnterKeyAction(self, item: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool
    QVirtualKeyboardInputContextPrivate::hasEnterKeyAction(QObject *item)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html

    Parameters
    ----------

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QVirtualKeyboardInputContextPrivate::hasEnterKeyAction(QObject
    #      *item) const
    return self.uglySide.call(
        'ritual_ZNK35QVirtualKeyboardInputContextPrivate17hasEnterKeyAction'
        'EP7QObject',
        self._addressOf(item, 'QObject'),
    )

  @overload(QPointF)
  def contains(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QVirtualKeyboardInputContextPrivate::contains(const
    QPointF &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html#contains

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QVirtualKeyboardInputContextPrivate::contains(const QPointF
    #      &point) const
    return self.uglySide.call(
        'ritual_ZNK35QVirtualKeyboardInputContextPrivate8containsERK7QPoint'
        'F',
        self._valueOf(point, 'QPointF'),
    )

  @overload(QtVirtualKeyboard.KeyboardFunction)
  def keyboardFunctionKey(
      self,
      keyboardFunction: QtVirtualKeyboard.KeyboardFunction,
  ) -> QtVirtualKeyboard.KeyboardFunctionKey:
    """
    Calls Qt's 'QtVirtualKeyboard::KeyboardFunctionKey
    QVirtualKeyboardInputContextPrivate::keyboardFunctionKey(
    QtVirtualKeyboard::KeyboardFunction keyboardFunction) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html

    Parameters
    ----------

    keyboardFunction : QtVirtualKeyboard.KeyboardFunction
      Passed on as its number.

    Returns
    -------

    QtVirtualKeyboard.KeyboardFunctionKey
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtVirtualKeyboard.KeyboardFunctionKey(number)' gives.
    """
    #  QtVirtualKeyboard::KeyboardFunctionKey
    #      QVirtualKeyboardInputContextPrivate::keyboardFunctionKey(
    #      QtVirtualKeyboard::KeyboardFunction keyboardFunction) const
    return QtVirtualKeyboard.KeyboardFunctionKey(self.uglySide.call(
        'ritual_ZNK35QVirtualKeyboardInputContextPrivate19keyboardFunctionK'
        'eyEN17QtVirtualKeyboard16KeyboardFunctionE',
        keyboardFunction.value,
    ))

  def isEmptyState(self) -> bool:
    """
    Calls Qt's 'bool QVirtualKeyboardInputContextPrivate::isEmptyState()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html
    """
    #  bool QVirtualKeyboardInputContextPrivate::isEmptyState() const
    return self.uglySide.call(
        'ritual_ZNK35QVirtualKeyboardInputContextPrivate12isEmptyStateEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setFocus(self, focus: bool) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContextPrivate::setFocus(bool
    focus)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html#setFocus

    Parameters
    ----------

    focus : bool
      Passed on as it is.
    """
    #  void QVirtualKeyboardInputContextPrivate::setFocus(bool focus)
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate8setFocusEb', focus,
    )

  @overload(QRectF)
  def setKeyboardRectangle(self, rectangle: QRectF) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContextPrivate::setKeyboardRectangle(QRectF
    rectangle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html

    Parameters
    ----------

    rectangle : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QVirtualKeyboardInputContextPrivate::setKeyboardRectangle(QRectF
    #      rectangle)
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate20setKeyboardRectang'
        'leE6QRectF',
        self._valueOf(rectangle),
    )

  @overload(QRectF)
  def setPreviewRectangle(self, rectangle: QRectF) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContextPrivate::setPreviewRectangle(QRectF
    rectangle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html

    Parameters
    ----------

    rectangle : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QVirtualKeyboardInputContextPrivate::setPreviewRectangle(QRectF
    #      rectangle)
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate19setPreviewRectangl'
        'eE6QRectF',
        self._valueOf(rectangle),
    )

  @overload(bool)
  def setPreviewVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContextPrivate::setPreviewVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QVirtualKeyboardInputContextPrivate::setPreviewVisible(bool
    #      visible)
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate17setPreviewVisibleE'
        'b',
        visible,
    )

  @overload(str)
  def setLocale(self, locale: str) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContextPrivate::setLocale(const
    QString &locale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html#setLocale

    Parameters
    ----------

    locale : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QVirtualKeyboardInputContextPrivate::setLocale(const QString
    #      &locale)
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate9setLocaleERK7QStrin'
        'g',
        locale,
    )

  @overload(QVirtualKeyboardObserver)
  @overload(NoneType)
  def setKeyboardObserver(
      self,
      keyboardObserver: Optional[QVirtualKeyboardObserver],
  ) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContextPrivate::setKeyboardObserver(
    QVirtualKeyboardObserver *keyboardObserver)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html

    Parameters
    ----------

    keyboardObserver : Optional[QVirtualKeyboardObserver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVirtualKeyboardInputContextPrivate::setKeyboardObserver(
    #      QVirtualKeyboardObserver *keyboardObserver)
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate19setKeyboardObserve'
        'rEP24QVirtualKeyboardObserver',
        self._addressOf(keyboardObserver),
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

  @overload(QVirtualKeyboardInputContext)
  @overload(NoneType)
  def __init__(self, q_ptr: Optional[QVirtualKeyboardInputContext]) -> None:
    """
    Notes what was given, for Qt's 'QVirtualKeyboardInputContextPrivate::
    QVirtualKeyboardInputContextPrivate(QVirtualKeyboardInputContext
    *q_ptr)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html

    Parameters
    ----------

    q_ptr : Optional[QVirtualKeyboardInputContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QVirtualKeyboardInputContextPrivate::
    #      QVirtualKeyboardInputContextPrivate(QVirtualKeyboardInputContext
    #      *q_ptr)
    self._noteCreation(
        QVirtualKeyboardInputContextPrivate, lambda: Rituals.call(
            'ritual_ZN35QVirtualKeyboardInputContextPrivateC1EP28QVirtualKe'
            'yboardInputContext',
            self._addressOf(q_ptr),
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

  def q_func(self) -> Optional[QVirtualKeyboardInputContext]:
    """
    Calls Qt's 'QVirtualKeyboardInputContext
    *QVirtualKeyboardInputContextPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html#q_func

    Returns
    -------

    Optional[QVirtualKeyboardInputContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVirtualKeyboardInputContext
    #      *QVirtualKeyboardInputContextPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate6q_funcEv',
    )
    from . import QVirtualKeyboardInputContext
    return QVirtualKeyboardInputContext._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContextPrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html#init
    """
    #  void QVirtualKeyboardInputContextPrivate::init()
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate4initEv',
    )

  @overload(QUrl)
  def fileExists(self, fileUrl: QUrl) -> bool:
    """
    Calls Qt's 'bool QVirtualKeyboardInputContextPrivate::fileExists(const
    QUrl &fileUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html

    Parameters
    ----------

    fileUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QVirtualKeyboardInputContextPrivate::fileExists(const QUrl
    #      &fileUrl)
    return self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate10fileExistsERK4QUrl',
        self._valueOf(fileUrl),
    )

  @overload(QObject)
  @overload(NoneType)
  def registerInputPanel(self, inputPanel: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContextPrivate::registerInputPanel(QObject
    *inputPanel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html

    Parameters
    ----------

    inputPanel : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVirtualKeyboardInputContextPrivate::registerInputPanel(QObject
    #      *inputPanel)
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate18registerInputPanel'
        'EP7QObject',
        self._addressOf(inputPanel, 'QObject'),
    )

  def focusChanged(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContextPrivate::focusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html
    """
    #  void QVirtualKeyboardInputContextPrivate::focusChanged()
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate12focusChangedEv',
    )

  def keyboardRectangleChanged(self) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContextPrivate::keyboardRectangleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html
    """
    #  void QVirtualKeyboardInputContextPrivate::keyboardRectangleChanged()
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate24keyboardRectangleC'
        'hangedEv',
    )

  def previewRectangleChanged(self) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContextPrivate::previewRectangleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html
    """
    #  void QVirtualKeyboardInputContextPrivate::previewRectangleChanged()
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate23previewRectangleCh'
        'angedEv',
    )

  def previewVisibleChanged(self) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContextPrivate::previewVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html
    """
    #  void QVirtualKeyboardInputContextPrivate::previewVisibleChanged()
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate21previewVisibleChan'
        'gedEv',
    )

  def localeChanged(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContextPrivate::localeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html
    """
    #  void QVirtualKeyboardInputContextPrivate::localeChanged()
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate13localeChangedEv',
    )

  def inputItemChanged(self) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContextPrivate::inputItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html
    """
    #  void QVirtualKeyboardInputContextPrivate::inputItemChanged()
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate16inputItemChangedEv',
    )

  @overload(int, bool)
  def navigationKeyPressed(self, key: int, isAutoRepeat: bool) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContextPrivate::navigationKeyPressed(int key, bool
    isAutoRepeat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html

    Parameters
    ----------

    key : int
      Passed on as it is.

    isAutoRepeat : bool
      Passed on as it is.
    """
    #  void QVirtualKeyboardInputContextPrivate::navigationKeyPressed(int
    #      key, bool isAutoRepeat)
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate20navigationKeyPress'
        'edEib',
        key, isAutoRepeat,
    )

  @overload(int, bool)
  def navigationKeyReleased(self, key: int, isAutoRepeat: bool) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContextPrivate::navigationKeyReleased(int key, bool
    isAutoRepeat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html

    Parameters
    ----------

    key : int
      Passed on as it is.

    isAutoRepeat : bool
      Passed on as it is.
    """
    #  void QVirtualKeyboardInputContextPrivate::navigationKeyReleased(int
    #      key, bool isAutoRepeat)
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate21navigationKeyRelea'
        'sedEib',
        key, isAutoRepeat,
    )

  def hideInputPanel(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContextPrivate::hideInputPanel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html
    """
    #  void QVirtualKeyboardInputContextPrivate::hideInputPanel()
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate14hideInputPanelEv',
    )

  @overload(QStringList)
  def updateAvailableLocales(self, availableLocales: QStringList) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContextPrivate::updateAvailableLocales(const
    QStringList &availableLocales)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html

    Parameters
    ----------

    availableLocales : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QVirtualKeyboardInputContextPrivate::updateAvailableLocales(const
    #      QStringList &availableLocales)
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate22updateAvailableLoc'
        'alesERK5QListI7QStringE',
        self._valueOf(availableLocales),
    )

  @overload(int, int)
  def forceCursorPosition(
      self,
      anchorPosition: int,
      cursorPosition: int,
  ) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContextPrivate::forceCursorPosition(int
    anchorPosition, int cursorPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html

    Parameters
    ----------

    anchorPosition : int
      Passed on as it is.

    cursorPosition : int
      Passed on as it is.
    """
    #  void QVirtualKeyboardInputContextPrivate::forceCursorPosition(int
    #      anchorPosition, int cursorPosition)
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate19forceCursorPositio'
        'nEii',
        anchorPosition, cursorPosition,
    )

  def onInputItemChanged(self) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContextPrivate::onInputItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html
    """
    #  void QVirtualKeyboardInputContextPrivate::onInputItemChanged()
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate18onInputItemChanged'
        'Ev',
    )

  @overload(QInputMethodEvent)
  @overload(NoneType)
  def sendInputMethodEvent(self, event: Optional[QInputMethodEvent]) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContextPrivate::sendInputMethodEvent(
    QInputMethodEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html

    Parameters
    ----------

    event : Optional[QInputMethodEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVirtualKeyboardInputContextPrivate::sendInputMethodEvent(
    #      QInputMethodEvent *event)
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate20sendInputMethodEve'
        'ntEP17QInputMethodEvent',
        self._addressOf(event),
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContextPrivate::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html#reset
    """
    #  void QVirtualKeyboardInputContextPrivate::reset()
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate5resetEv',
    )

  def commit(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContextPrivate::commit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html#commit
    """
    #  void QVirtualKeyboardInputContextPrivate::commit()
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate6commitEv',
    )

  @overload(Qt.InputMethodQueries)
  def update(self, queries: Qt.InputMethodQueries) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContextPrivate::update(Qt::InputMethodQueries
    queries)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html#update

    Parameters
    ----------

    queries : Qt.InputMethodQueries
      Passed on as its number.
    """
    #  void
    #      QVirtualKeyboardInputContextPrivate::update(Qt::InputMethodQueries
    #      queries)
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate6updateE6QFlagsIN2Qt'
        '16InputMethodQueryEE',
        queries.value,
    )

  @overload(QInputMethod.Action, int)
  def invokeAction(
      self,
      action: QInputMethod.Action,
      cursorPosition: int,
  ) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContextPrivate::invokeAction(QInputMethod::Action
    action, int cursorPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html

    Parameters
    ----------

    action : QInputMethod.Action
      Passed on as its number.

    cursorPosition : int
      Passed on as it is.
    """
    #  void QVirtualKeyboardInputContextPrivate::invokeAction(QInputMethod::
    #      Action action, int cursorPosition)
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate12invokeActionEN12QI'
        'nputMethod6ActionEi',
        action.value, cursorPosition,
    )

  def maybeCloseOnReturn(self) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContextPrivate::maybeCloseOnReturn()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html
    """
    #  void QVirtualKeyboardInputContextPrivate::maybeCloseOnReturn()
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate18maybeCloseOnReturn'
        'Ev',
    )

  @overload(QEvent)
  @overload(NoneType)
  def filterEvent(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QVirtualKeyboardInputContextPrivate::filterEvent(const
    QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QVirtualKeyboardInputContextPrivate::filterEvent(const QEvent
    #      *event)
    return self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate11filterEventEPK6QEv'
        'ent',
        self._addressOf(event),
    )

  @overload(bool)
  def updateSelectionControlVisible(self, inputPanelVisible: bool) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContextPrivate::updateSelectionControlVisible(bool
    inputPanelVisible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontextprivate.html

    Parameters
    ----------

    inputPanelVisible : bool
      Passed on as it is.
    """
    #  void QVirtualKeyboardInputContextPrivate::
    #      updateSelectionControlVisible(bool inputPanelVisible)
    self.uglySide.call(
        'ritual_ZN35QVirtualKeyboardInputContextPrivate29updateSelectionCon'
        'trolVisibleEb',
        inputPanelVisible,
    )

  @staticmethod
  def addSelectionAttribute(*__, **_) -> Never:
    """
    Qt's 'void QVirtualKeyboardInputContextPrivate::addSelectionAttribute(
    QList<QInputMethodEvent::Attribute> &attributes)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QVirtualKeyboardInputContextPrivate.addSelectionAttribute' has no "
        "cute function yet. Qt's 'void "
        "QVirtualKeyboardInputContextPrivate::addSelectionAttribute(QList<QI"
        "nputMethodEvent::Attribute> &attributes)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def clearState(*__, **_) -> Never:
    """
    Qt's 'void QVirtualKeyboardInputContextPrivate::clearState(const State
    &state)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QVirtualKeyboardInputContextPrivate.clearState' has no cute "
        "function yet. Qt's 'void "
        "QVirtualKeyboardInputContextPrivate::clearState(const State "
        "&state)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def findAttribute(*__, **_) -> Never:
    """
    Qt's 'int QVirtualKeyboardInputContextPrivate::findAttribute(const
    QList<QInputMethodEvent::Attribute> &attributes,
    QInputMethodEvent::AttributeType attributeType) const': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QVirtualKeyboardInputContextPrivate.findAttribute' has no cute "
        "function yet. Qt's 'int "
        "QVirtualKeyboardInputContextPrivate::findAttribute(const "
        "QList<QInputMethodEvent::Attribute> &attributes, "
        "QInputMethodEvent::AttributeType attributeType) const': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def sendPreedit(*__, **_) -> Never:
    """
    Qt's 'void QVirtualKeyboardInputContextPrivate::sendPreedit(const QString
    &text, const QList<QInputMethodEvent::Attribute> &attributes, int
    replaceFrom, int replaceLength)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QVirtualKeyboardInputContextPrivate.sendPreedit' has no cute "
        "function yet. Qt's 'void "
        "QVirtualKeyboardInputContextPrivate::sendPreedit(const QString "
        "&text, const QList<QInputMethodEvent::Attribute> &attributes, int "
        "replaceFrom, int replaceLength)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def setState(*__, **_) -> Never:
    """
    Qt's 'void QVirtualKeyboardInputContextPrivate::setState(const State
    &state)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QVirtualKeyboardInputContextPrivate.setState' has no cute "
        "function yet. Qt's 'void "
        "QVirtualKeyboardInputContextPrivate::setState(const State "
        "&state)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def testAttribute(*__, **_) -> Never:
    """
    Qt's 'bool QVirtualKeyboardInputContextPrivate::testAttribute(const
    QList<QInputMethodEvent::Attribute> &attributes,
    QInputMethodEvent::AttributeType attributeType) const': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QVirtualKeyboardInputContextPrivate.testAttribute' has no cute "
        "function yet. Qt's 'bool "
        "QVirtualKeyboardInputContextPrivate::testAttribute(const "
        "QList<QInputMethodEvent::Attribute> &attributes, "
        "QInputMethodEvent::AttributeType attributeType) const': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def testState(*__, **_) -> Never:
    """
    Qt's 'bool QVirtualKeyboardInputContextPrivate::testState(const State
    &state) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QVirtualKeyboardInputContextPrivate.testState' has no cute "
        "function yet. Qt's 'bool "
        "QVirtualKeyboardInputContextPrivate::testState(const State &state) "
        "const': takes a type Python has no way to hand over yet.")
