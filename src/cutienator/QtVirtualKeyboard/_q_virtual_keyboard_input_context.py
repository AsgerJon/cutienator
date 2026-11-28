"""
QVirtualKeyboardInputContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/qvirtualkeyboardinputcontext.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF, QRectF
  from . import QVirtualKeyboardInputContextPrivate
  from . import QVirtualKeyboardInputEngine, QVirtualKeyboardObserver
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVirtualKeyboardInputContext(QObject):
  """
  The cute side of Qt's QVirtualKeyboardInputContext: a plain Python object
  standing in front of one C++ QVirtualKeyboardInputContext.

  It is built on the cute 'QObject', as Qt's QVirtualKeyboardInputContext is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QVirtualKeyboardInputContext that has a ritual and
  that Python can call so far, 45 names in all: 'metaObject', 'tr', 'd_func',
  'isShiftActive', 'isCapsLockActive', 'isUppercase', 'anchorPosition',
  'cursorPosition', 'inputMethodHints', 'preeditText', 'surroundingText',
  'selectedText', 'anchorRectangle', 'cursorRectangle', 'isAnimating',
  'setAnimating', 'locale', 'inputItem', 'inputEngine',
  'isSelectionControlVisible', 'anchorRectIntersectsClipRect',
  'cursorRectIntersectsClipRect', 'priv', 'keyboardObserver', 'sendKeyClick',
  'commit', 'clear', 'setSelectionOnFocusObject', 'preeditTextChanged',
  'inputMethodHintsChanged', 'surroundingTextChanged', 'selectedTextChanged',
  'anchorPositionChanged', 'cursorPositionChanged', 'anchorRectangleChanged',
  'cursorRectangleChanged', 'shiftActiveChanged', 'capsLockActiveChanged',
  'uppercaseChanged', 'animatingChanged', 'localeChanged',
  'inputItemChanged', 'selectionControlVisibleChanged',
  'anchorRectIntersectsClipRectChanged',
  'cursorRectIntersectsClipRectChanged'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QVirtualKeyboardInputContext::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QVirtualKeyboardInputContext::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QVirtualKeyboardInputContextPrivate
    *QVirtualKeyboardInputContext::d_func() const': takes in Python what
    'QVirtualKeyboardInputContextPrivate
    *QVirtualKeyboardInputContext::d_func()' takes.
  - Qt's 'void QVirtualKeyboardInputContext::qt_qmlMarker_singleton()': one
    of Qt's own inner workings.
  - Qt's 'QVirtualKeyboardInputContext::~QVirtualKeyboardInputContext()': the
    destructor: Python never removes a C++ QVirtualKeyboardInputContext.
  - Qt's 'void QVirtualKeyboardInputContext::setPreeditText(const QString
    &text, QList<QInputMethodEvent::Attribute> attributes, int replaceFrom,
    int replaceLength)': takes a type Python has no way to hand over yet.
  - Qt's 'QList<QInputMethodEvent::Attribute>
    QVirtualKeyboardInputContext::preeditTextAttributes() const': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 58 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QVirtualKeyboardInputContext is created at the first use, not by
    'QVirtualKeyboardInputContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVirtualKeyboardInputContext.
  - Qt tells when it has removed the C++ QVirtualKeyboardInputContext. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QVirtualKeyboardInputContext that has no cute function
    yet, 'preeditTextAttributes', 'setPreeditText', holds a function that
    raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QVirtualKeyboardInputContext::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#tr

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
    #  QString QVirtualKeyboardInputContext::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QVirtualKeyboardInputContext2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVirtualKeyboardInputContext'

  #  A C++ QVirtualKeyboardInputContext Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVirtualKeyboardInputContext'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QVirtualKeyboardInputContext::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QVirtualKeyboardInputContext::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QVirtualKeyboardInputContext10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isShiftActive(self) -> bool:
    """
    Calls Qt's 'bool QVirtualKeyboardInputContext::isShiftActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#isShiftActive
    """
    #  bool QVirtualKeyboardInputContext::isShiftActive() const
    return self.uglySide.call(
        'ritual_ZNK28QVirtualKeyboardInputContext13isShiftActiveEv',
    )

  def isCapsLockActive(self) -> bool:
    """
    Calls Qt's 'bool QVirtualKeyboardInputContext::isCapsLockActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#isCapsLockActive
    """
    #  bool QVirtualKeyboardInputContext::isCapsLockActive() const
    return self.uglySide.call(
        'ritual_ZNK28QVirtualKeyboardInputContext16isCapsLockActiveEv',
    )

  def isUppercase(self) -> bool:
    """
    Calls Qt's 'bool QVirtualKeyboardInputContext::isUppercase() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#isUppercase
    """
    #  bool QVirtualKeyboardInputContext::isUppercase() const
    return self.uglySide.call(
        'ritual_ZNK28QVirtualKeyboardInputContext11isUppercaseEv',
    )

  def anchorPosition(self) -> int:
    """
    Calls Qt's 'int QVirtualKeyboardInputContext::anchorPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#anchorPosition
    """
    #  int QVirtualKeyboardInputContext::anchorPosition() const
    return self.uglySide.call(
        'ritual_ZNK28QVirtualKeyboardInputContext14anchorPositionEv',
    )

  def cursorPosition(self) -> int:
    """
    Calls Qt's 'int QVirtualKeyboardInputContext::cursorPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#cursorPosition
    """
    #  int QVirtualKeyboardInputContext::cursorPosition() const
    return self.uglySide.call(
        'ritual_ZNK28QVirtualKeyboardInputContext14cursorPositionEv',
    )

  def inputMethodHints(self) -> Qt.InputMethodHints:
    """
    Calls Qt's 'Qt::InputMethodHints
    QVirtualKeyboardInputContext::inputMethodHints() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#inputMethodHints

    Returns
    -------

    Qt.InputMethodHints
      The value standing for the combination Qt gave back.
    """
    #  Qt::InputMethodHints QVirtualKeyboardInputContext::inputMethodHints()
    #      const
    return Qt.InputMethodHints(self.uglySide.call(
        'ritual_ZNK28QVirtualKeyboardInputContext16inputMethodHintsEv',
    ))

  def preeditText(self) -> str:
    """
    Calls Qt's 'QString QVirtualKeyboardInputContext::preeditText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#preeditText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QVirtualKeyboardInputContext::preeditText() const
    return self.uglySide.call(
        'ritual_ZNK28QVirtualKeyboardInputContext11preeditTextEv',
    )

  def surroundingText(self) -> str:
    """
    Calls Qt's 'QString QVirtualKeyboardInputContext::surroundingText()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#surroundingText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QVirtualKeyboardInputContext::surroundingText() const
    return self.uglySide.call(
        'ritual_ZNK28QVirtualKeyboardInputContext15surroundingTextEv',
    )

  def selectedText(self) -> str:
    """
    Calls Qt's 'QString QVirtualKeyboardInputContext::selectedText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#selectedText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QVirtualKeyboardInputContext::selectedText() const
    return self.uglySide.call(
        'ritual_ZNK28QVirtualKeyboardInputContext12selectedTextEv',
    )

  def anchorRectangle(self) -> QRectF:
    """
    Calls Qt's 'QRectF QVirtualKeyboardInputContext::anchorRectangle()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#anchorRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QVirtualKeyboardInputContext::anchorRectangle() const
    address = self.uglySide.call(
        'ritual_ZNK28QVirtualKeyboardInputContext15anchorRectangleEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def cursorRectangle(self) -> QRectF:
    """
    Calls Qt's 'QRectF QVirtualKeyboardInputContext::cursorRectangle()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#cursorRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QVirtualKeyboardInputContext::cursorRectangle() const
    address = self.uglySide.call(
        'ritual_ZNK28QVirtualKeyboardInputContext15cursorRectangleEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def isAnimating(self) -> bool:
    """
    Calls Qt's 'bool QVirtualKeyboardInputContext::isAnimating() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#isAnimating
    """
    #  bool QVirtualKeyboardInputContext::isAnimating() const
    return self.uglySide.call(
        'ritual_ZNK28QVirtualKeyboardInputContext11isAnimatingEv',
    )

  def locale(self) -> str:
    """
    Calls Qt's 'QString QVirtualKeyboardInputContext::locale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#locale

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QVirtualKeyboardInputContext::locale() const
    return self.uglySide.call(
        'ritual_ZNK28QVirtualKeyboardInputContext6localeEv',
    )

  def inputItem(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QVirtualKeyboardInputContext::inputItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#inputItem

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QVirtualKeyboardInputContext::inputItem() const
    address = self.uglySide.call(
        'ritual_ZNK28QVirtualKeyboardInputContext9inputItemEv',
    )
    return QObject._cuteAt(address)

  def inputEngine(self) -> Optional[QVirtualKeyboardInputEngine]:
    """
    Calls Qt's 'QVirtualKeyboardInputEngine
    *QVirtualKeyboardInputContext::inputEngine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#inputEngine

    Returns
    -------

    Optional[QVirtualKeyboardInputEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVirtualKeyboardInputEngine
    #      *QVirtualKeyboardInputContext::inputEngine() const
    address = self.uglySide.call(
        'ritual_ZNK28QVirtualKeyboardInputContext11inputEngineEv',
    )
    from . import QVirtualKeyboardInputEngine
    return QVirtualKeyboardInputEngine._cuteAt(address)

  def isSelectionControlVisible(self) -> bool:
    """
    Calls Qt's 'bool
    QVirtualKeyboardInputContext::isSelectionControlVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html
    """
    #  bool QVirtualKeyboardInputContext::isSelectionControlVisible() const
    return self.uglySide.call(
        'ritual_ZNK28QVirtualKeyboardInputContext25isSelectionControlVisibl'
        'eEv',
    )

  def anchorRectIntersectsClipRect(self) -> bool:
    """
    Calls Qt's 'bool
    QVirtualKeyboardInputContext::anchorRectIntersectsClipRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html
    """
    #  bool QVirtualKeyboardInputContext::anchorRectIntersectsClipRect()
    #      const
    return self.uglySide.call(
        'ritual_ZNK28QVirtualKeyboardInputContext28anchorRectIntersectsClip'
        'RectEv',
    )

  def cursorRectIntersectsClipRect(self) -> bool:
    """
    Calls Qt's 'bool
    QVirtualKeyboardInputContext::cursorRectIntersectsClipRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html
    """
    #  bool QVirtualKeyboardInputContext::cursorRectIntersectsClipRect()
    #      const
    return self.uglySide.call(
        'ritual_ZNK28QVirtualKeyboardInputContext28cursorRectIntersectsClip'
        'RectEv',
    )

  def priv(self) -> Optional[QVirtualKeyboardInputContextPrivate]:
    """
    Calls Qt's 'QVirtualKeyboardInputContextPrivate
    *QVirtualKeyboardInputContext::priv() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#priv

    Returns
    -------

    Optional[QVirtualKeyboardInputContextPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVirtualKeyboardInputContextPrivate
    #      *QVirtualKeyboardInputContext::priv() const
    address = self.uglySide.call(
        'ritual_ZNK28QVirtualKeyboardInputContext4privEv',
    )
    from . import QVirtualKeyboardInputContextPrivate
    return QVirtualKeyboardInputContextPrivate._cuteAt(address)

  def keyboardObserver(self) -> Optional[QVirtualKeyboardObserver]:
    """
    Calls Qt's 'QVirtualKeyboardObserver
    *QVirtualKeyboardInputContext::keyboardObserver() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#keyboardObserver

    Returns
    -------

    Optional[QVirtualKeyboardObserver]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVirtualKeyboardObserver
    #      *QVirtualKeyboardInputContext::keyboardObserver() const
    address = self.uglySide.call(
        'ritual_ZNK28QVirtualKeyboardInputContext16keyboardObserverEv',
    )
    from . import QVirtualKeyboardObserver
    return QVirtualKeyboardObserver._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAnimating(self, isAnimating: bool) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContext::setAnimating(bool
    isAnimating)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#setAnimating

    Parameters
    ----------

    isAnimating : bool
      Passed on as it is.
    """
    #  void QVirtualKeyboardInputContext::setAnimating(bool isAnimating)
    self.uglySide.call(
        'ritual_ZN28QVirtualKeyboardInputContext12setAnimatingEb',
        isAnimating,
    )

  @overload(QPointF, QPointF)
  def setSelectionOnFocusObject(
      self,
      anchorPos: QPointF,
      cursorPos: QPointF,
  ) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContext::setSelectionOnFocusObject(const QPointF
    &anchorPos, const QPointF &cursorPos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html

    Parameters
    ----------

    anchorPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    cursorPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QVirtualKeyboardInputContext::setSelectionOnFocusObject(const
    #      QPointF &anchorPos, const QPointF &cursorPos)
    self.uglySide.call(
        'ritual_ZN28QVirtualKeyboardInputContext25setSelectionOnFocusObject'
        'ERK7QPointFS2_',
        self._valueOf(anchorPos, 'QPointF'), self._valueOf(cursorPos,
        'QPointF'),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QVirtualKeyboardInputContext::QVirtualKeyboardInputContext(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QVirtualKeyboardInputContext::QVirtualKeyboardInputContext(QObject
    #      *parent)
    self._noteCreation(QVirtualKeyboardInputContext, lambda: Rituals.call(
        'ritual_ZN28QVirtualKeyboardInputContextC1EP7QObject',
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

  def d_func(self) -> Optional[QVirtualKeyboardInputContextPrivate]:
    """
    Calls Qt's 'QVirtualKeyboardInputContextPrivate
    *QVirtualKeyboardInputContext::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#d_func

    Returns
    -------

    Optional[QVirtualKeyboardInputContextPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVirtualKeyboardInputContextPrivate
    #      *QVirtualKeyboardInputContext::d_func()
    address = self.uglySide.call(
        'ritual_ZN28QVirtualKeyboardInputContext6d_funcEv',
    )
    from . import QVirtualKeyboardInputContextPrivate
    return QVirtualKeyboardInputContextPrivate._cuteAt(address)

  @overload(int, str)
  @overload(int, str, int)
  def sendKeyClick(self, key: int, text: str, modifiers: int = 0) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContext::sendKeyClick(int key,
    const QString &text, int modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#sendKeyClick

    Parameters
    ----------

    key : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.

    modifiers : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QVirtualKeyboardInputContext::sendKeyClick(int key, const QString
    #      &text, int modifiers)
    self.uglySide.call(
        'ritual_ZN28QVirtualKeyboardInputContext12sendKeyClickEiRK7QStringi',
        key, text, modifiers,
    )

  @overload()
  def commit(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContext::commit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#commit
    """
    #  void QVirtualKeyboardInputContext::commit()
    self.uglySide.call('ritual_ZN28QVirtualKeyboardInputContext6commitEv')

  @overload(str)
  @overload(str, int)
  @overload(str, int, int)
  def commit(
      self,
      text: str,
      replaceFrom: int = 0,
      replaceLength: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContext::commit(const QString
    &text, int replaceFrom, int replaceLength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#commit

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    replaceFrom : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    replaceLength : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QVirtualKeyboardInputContext::commit(const QString &text, int
    #      replaceFrom, int replaceLength)
    self.uglySide.call(
        'ritual_ZN28QVirtualKeyboardInputContext6commitERK7QStringii',
        text, replaceFrom, replaceLength,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContext::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#clear
    """
    #  void QVirtualKeyboardInputContext::clear()
    self.uglySide.call('ritual_ZN28QVirtualKeyboardInputContext5clearEv')

  def preeditTextChanged(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContext::preeditTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html
    """
    #  void QVirtualKeyboardInputContext::preeditTextChanged()
    self.uglySide.call(
        'ritual_ZN28QVirtualKeyboardInputContext18preeditTextChangedEv',
    )

  def inputMethodHintsChanged(self) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContext::inputMethodHintsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html
    """
    #  void QVirtualKeyboardInputContext::inputMethodHintsChanged()
    self.uglySide.call(
        'ritual_ZN28QVirtualKeyboardInputContext23inputMethodHintsChangedEv',
    )

  def surroundingTextChanged(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContext::surroundingTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html
    """
    #  void QVirtualKeyboardInputContext::surroundingTextChanged()
    self.uglySide.call(
        'ritual_ZN28QVirtualKeyboardInputContext22surroundingTextChangedEv',
    )

  def selectedTextChanged(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContext::selectedTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html
    """
    #  void QVirtualKeyboardInputContext::selectedTextChanged()
    self.uglySide.call(
        'ritual_ZN28QVirtualKeyboardInputContext19selectedTextChangedEv',
    )

  def anchorPositionChanged(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContext::anchorPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html
    """
    #  void QVirtualKeyboardInputContext::anchorPositionChanged()
    self.uglySide.call(
        'ritual_ZN28QVirtualKeyboardInputContext21anchorPositionChangedEv',
    )

  def cursorPositionChanged(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContext::cursorPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html
    """
    #  void QVirtualKeyboardInputContext::cursorPositionChanged()
    self.uglySide.call(
        'ritual_ZN28QVirtualKeyboardInputContext21cursorPositionChangedEv',
    )

  def anchorRectangleChanged(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContext::anchorRectangleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html
    """
    #  void QVirtualKeyboardInputContext::anchorRectangleChanged()
    self.uglySide.call(
        'ritual_ZN28QVirtualKeyboardInputContext22anchorRectangleChangedEv',
    )

  def cursorRectangleChanged(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContext::cursorRectangleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html
    """
    #  void QVirtualKeyboardInputContext::cursorRectangleChanged()
    self.uglySide.call(
        'ritual_ZN28QVirtualKeyboardInputContext22cursorRectangleChangedEv',
    )

  def shiftActiveChanged(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContext::shiftActiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html
    """
    #  void QVirtualKeyboardInputContext::shiftActiveChanged()
    self.uglySide.call(
        'ritual_ZN28QVirtualKeyboardInputContext18shiftActiveChangedEv',
    )

  def capsLockActiveChanged(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContext::capsLockActiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html
    """
    #  void QVirtualKeyboardInputContext::capsLockActiveChanged()
    self.uglySide.call(
        'ritual_ZN28QVirtualKeyboardInputContext21capsLockActiveChangedEv',
    )

  def uppercaseChanged(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContext::uppercaseChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#uppercaseChanged
    """
    #  void QVirtualKeyboardInputContext::uppercaseChanged()
    self.uglySide.call(
        'ritual_ZN28QVirtualKeyboardInputContext16uppercaseChangedEv',
    )

  def animatingChanged(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContext::animatingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#animatingChanged
    """
    #  void QVirtualKeyboardInputContext::animatingChanged()
    self.uglySide.call(
        'ritual_ZN28QVirtualKeyboardInputContext16animatingChangedEv',
    )

  def localeChanged(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContext::localeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#localeChanged
    """
    #  void QVirtualKeyboardInputContext::localeChanged()
    self.uglySide.call(
        'ritual_ZN28QVirtualKeyboardInputContext13localeChangedEv',
    )

  def inputItemChanged(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardInputContext::inputItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html#inputItemChanged
    """
    #  void QVirtualKeyboardInputContext::inputItemChanged()
    self.uglySide.call(
        'ritual_ZN28QVirtualKeyboardInputContext16inputItemChangedEv',
    )

  def selectionControlVisibleChanged(self) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContext::selectionControlVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html
    """
    #  void QVirtualKeyboardInputContext::selectionControlVisibleChanged()
    self.uglySide.call(
        'ritual_ZN28QVirtualKeyboardInputContext30selectionControlVisibleCh'
        'angedEv',
    )

  def anchorRectIntersectsClipRectChanged(self) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContext::anchorRectIntersectsClipRectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html
    """
    #  void
    #      QVirtualKeyboardInputContext::anchorRectIntersectsClipRectChanged(
    #      )
    self.uglySide.call(
        'ritual_ZN28QVirtualKeyboardInputContext35anchorRectIntersectsClipR'
        'ectChangedEv',
    )

  def cursorRectIntersectsClipRectChanged(self) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardInputContext::cursorRectIntersectsClipRectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardinputcontext.html
    """
    #  void
    #      QVirtualKeyboardInputContext::cursorRectIntersectsClipRectChanged(
    #      )
    self.uglySide.call(
        'ritual_ZN28QVirtualKeyboardInputContext35cursorRectIntersectsClipR'
        'ectChangedEv',
    )

  @staticmethod
  def preeditTextAttributes(*__, **_) -> Never:
    """
    Qt's 'QList<QInputMethodEvent::Attribute>
    QVirtualKeyboardInputContext::preeditTextAttributes() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QVirtualKeyboardInputContext.preeditTextAttributes' has no cute "
        "function yet. Qt's 'QList<QInputMethodEvent::Attribute> "
        "QVirtualKeyboardInputContext::preeditTextAttributes() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def setPreeditText(*__, **_) -> Never:
    """
    Qt's 'void QVirtualKeyboardInputContext::setPreeditText(const QString
    &text, QList<QInputMethodEvent::Attribute> attributes, int replaceFrom,
    int replaceLength)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QVirtualKeyboardInputContext.setPreeditText' has no cute function "
        "yet. Qt's 'void QVirtualKeyboardInputContext::setPreeditText(const "
        "QString &text, QList<QInputMethodEvent::Attribute> attributes, int "
        "replaceFrom, int replaceLength)': takes a type Python has no way "
        "to hand over yet.")
