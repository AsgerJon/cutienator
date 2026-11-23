"""
QInputMethod binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qinputmethod.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QLocale, QMetaObject, QRectF, QVariant
  from . import QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QTransform = WAIT['QTransform']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QInputMethod(QObject):
  """
  The cute side of Qt's QInputMethod: a plain Python object standing in front
  of one C++ QInputMethod.

  It is built on the cute 'QObject', as Qt's QInputMethod is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QInputMethod that has a ritual and that Python can
  call so far, 22 names in all: 'metaObject', 'tr', 'inputItemTransform',
  'setInputItemTransform', 'inputItemRectangle', 'setInputItemRectangle',
  'cursorRectangle', 'anchorRectangle', 'keyboardRectangle',
  'inputItemClipRectangle', 'isVisible', 'setVisible', 'isAnimating',
  'locale', 'inputDirection', 'queryFocusObject', 'show', 'hide', 'update',
  'reset', 'commit', 'invokeAction'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QInputMethod::~QInputMethod()': the destructor: Python never
    removes a C++ QInputMethod.

  What has no ritual
  ------------------

  14 of the 38 functions Qt declares: 8 a signal; 4 takes or gives a type
  that cannot be passed yet; 1 a template; 1 declared and nowhere to be
  found.

  What to expect
  --------------

  - The C++ QInputMethod is created at the first use, not by
    'QInputMethod(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QInputMethod.
  - Qt tells when it has removed the C++ QInputMethod. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QInputMethod, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Action(CuteNum):
    """
    The enum 'QInputMethod::Action' of Qt, with the 2 names Qt gives in it.
    """

    Click = Kee[int](0)
    ContextMenu = Kee[int](1)

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
    Calls Qt's 'QString QInputMethod::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethod.html#tr

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
    #  QString QInputMethod::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QInputMethod2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(Qt.InputMethodQuery, QVariant)
  def queryFocusObject(
      query: Qt.InputMethodQuery,
      argument: QVariant,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QInputMethod::queryFocusObject(Qt::InputMethodQuery
    query, const QVariant &argument)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethod.html#queryFocusObject

    Parameters
    ----------

    query : Qt.InputMethodQuery
      Passed on as its number.

    argument : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QInputMethod::queryFocusObject(Qt::InputMethodQuery query,
    #      const QVariant &argument)
    address = Rituals.call(
        'ritual_ZN12QInputMethod16queryFocusObjectEN2Qt16InputMethodQueryER'
        'K8QVariant',
        query.value, CuteMixin._valueOf(argument),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QInputMethod'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QInputMethod::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethod.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QInputMethod::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QInputMethod10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def inputItemTransform(self) -> QTransform:
    """
    Calls Qt's 'QTransform QInputMethod::inputItemTransform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethod.html#inputItemTransform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QInputMethod::inputItemTransform() const
    address = self.uglySide.call(
        'ritual_ZNK12QInputMethod18inputItemTransformEv',
    )
    from . import QTransform
    return QTransform._cuteOwning(address)

  def inputItemRectangle(self) -> QRectF:
    """
    Calls Qt's 'QRectF QInputMethod::inputItemRectangle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethod.html#inputItemRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QInputMethod::inputItemRectangle() const
    address = self.uglySide.call(
        'ritual_ZNK12QInputMethod18inputItemRectangleEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def cursorRectangle(self) -> QRectF:
    """
    Calls Qt's 'QRectF QInputMethod::cursorRectangle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethod.html#cursorRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QInputMethod::cursorRectangle() const
    address = self.uglySide.call(
        'ritual_ZNK12QInputMethod15cursorRectangleEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def anchorRectangle(self) -> QRectF:
    """
    Calls Qt's 'QRectF QInputMethod::anchorRectangle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethod.html#anchorRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QInputMethod::anchorRectangle() const
    address = self.uglySide.call(
        'ritual_ZNK12QInputMethod15anchorRectangleEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def keyboardRectangle(self) -> QRectF:
    """
    Calls Qt's 'QRectF QInputMethod::keyboardRectangle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethod.html#keyboardRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QInputMethod::keyboardRectangle() const
    address = self.uglySide.call(
        'ritual_ZNK12QInputMethod17keyboardRectangleEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def inputItemClipRectangle(self) -> QRectF:
    """
    Calls Qt's 'QRectF QInputMethod::inputItemClipRectangle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethod.html#inputItemClipRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QInputMethod::inputItemClipRectangle() const
    address = self.uglySide.call(
        'ritual_ZNK12QInputMethod22inputItemClipRectangleEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QInputMethod::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethod.html#isVisible
    """
    #  bool QInputMethod::isVisible() const
    return self.uglySide.call('ritual_ZNK12QInputMethod9isVisibleEv')

  def isAnimating(self) -> bool:
    """
    Calls Qt's 'bool QInputMethod::isAnimating() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethod.html#isAnimating
    """
    #  bool QInputMethod::isAnimating() const
    return self.uglySide.call('ritual_ZNK12QInputMethod11isAnimatingEv')

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QInputMethod::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethod.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QInputMethod::locale() const
    address = self.uglySide.call('ritual_ZNK12QInputMethod6localeEv')
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  def inputDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QInputMethod::inputDirection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethod.html#inputDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QInputMethod::inputDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK12QInputMethod14inputDirectionEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTransform)
  def setInputItemTransform(self, transform: QTransform) -> None:
    """
    Calls Qt's 'void QInputMethod::setInputItemTransform(const QTransform
    &transform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethod.html#setInputItemTransform

    Parameters
    ----------

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QInputMethod::setInputItemTransform(const QTransform &transform)
    self.uglySide.call(
        'ritual_ZN12QInputMethod21setInputItemTransformERK10QTransform',
        self._valueOf(transform),
    )

  @overload(QRectF)
  def setInputItemRectangle(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QInputMethod::setInputItemRectangle(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethod.html#setInputItemRectangle

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QInputMethod::setInputItemRectangle(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN12QInputMethod21setInputItemRectangleERK6QRectF',
        self._valueOf(rect),
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QInputMethod::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethod.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QInputMethod::setVisible(bool visible)
    self.uglySide.call('ritual_ZN12QInputMethod10setVisibleEb', visible)

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
    Notes what was given, for Qt's 'QInputMethod::QInputMethod()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethod.html#QInputMethod
    """
    #  QInputMethod::QInputMethod()
    self._noteCreation(QInputMethod, lambda: Rituals.call(
        'ritual_ZN12QInputMethodC1Ev',
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

  def show(self) -> None:
    """
    Calls Qt's 'void QInputMethod::show()'.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethod.html#show
    """
    #  void QInputMethod::show()
    self.uglySide.call('ritual_ZN12QInputMethod4showEv')

  def hide(self) -> None:
    """
    Calls Qt's 'void QInputMethod::hide()'.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethod.html#hide
    """
    #  void QInputMethod::hide()
    self.uglySide.call('ritual_ZN12QInputMethod4hideEv')

  @overload(Qt.InputMethodQueries)
  def update(self, queries: Qt.InputMethodQueries) -> None:
    """
    Calls Qt's 'void QInputMethod::update(Qt::InputMethodQueries queries)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethod.html#update

    Parameters
    ----------

    queries : Qt.InputMethodQueries
      Passed on as its number.
    """
    #  void QInputMethod::update(Qt::InputMethodQueries queries)
    self.uglySide.call(
        'ritual_ZN12QInputMethod6updateE6QFlagsIN2Qt16InputMethodQueryEE',
        queries.value,
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QInputMethod::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethod.html#reset
    """
    #  void QInputMethod::reset()
    self.uglySide.call('ritual_ZN12QInputMethod5resetEv')

  def commit(self) -> None:
    """
    Calls Qt's 'void QInputMethod::commit()'.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethod.html#commit
    """
    #  void QInputMethod::commit()
    self.uglySide.call('ritual_ZN12QInputMethod6commitEv')

  @overload(Action, int)
  def invokeAction(self, a: Action, cursorPosition: int) -> None:
    """
    Calls Qt's 'void QInputMethod::invokeAction(Action a, int
    cursorPosition)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethod.html#invokeAction

    Parameters
    ----------

    a : Action
      Passed on as its number.

    cursorPosition : int
      Passed on as it is.
    """
    #  void QInputMethod::invokeAction(Action a, int cursorPosition)
    self.uglySide.call(
        'ritual_ZN12QInputMethod12invokeActionENS_6ActionEi',
        a.value, cursorPosition,
    )
