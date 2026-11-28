"""
QQuickInputMethod binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickinputmethod_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickInputMethod to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtGui import QInputMethod

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QLocale, QMetaObject, QRectF
  from ..QtGui import QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickInputMethod(QObject):
  """
  The cute side of Qt's QQuickInputMethod: a plain Python object standing in
  front of one C++ QQuickInputMethod.

  It is built on the cute 'QObject', as Qt's QQuickInputMethod is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickInputMethod that has a ritual and that Python
  can call so far, 29 names in all: 'metaObject', 'tr', 'anchorRectangle',
  'cursorRectangle', 'inputDirection', 'inputItemClipRectangle',
  'inputItemRectangle', 'setInputItemRectangle', 'inputItemTransform',
  'setInputItemTransform', 'isAnimating', 'isVisible', 'setVisible',
  'keyboardRectangle', 'locale', 'anchorRectangleChanged',
  'animatingChanged', 'cursorRectangleChanged', 'inputDirectionChanged',
  'inputItemClipRectangleChanged', 'keyboardRectangleChanged',
  'localeChanged', 'visibleChanged', 'commit', 'hide', 'invokeAction',
  'reset', 'show', 'update'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickInputMethod::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickInputMethod::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickInputMethod::qt_qmlMarker_singleton()': one of Qt's own
    inner workings.

  What has no ritual
  ------------------

  2 of the 35 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickInputMethod is created at the first use, not by
    'QQuickInputMethod(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickInputMethod.
  - Qt tells when it has removed the C++ QQuickInputMethod. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickInputMethod::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickinputmethod.html#tr

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
    #  QString QQuickInputMethod::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickInputMethod2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickInputMethod'

  #  A C++ QQuickInputMethod Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickInputMethod'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickInputMethod::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickinputmethod.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickInputMethod::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickInputMethod10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def anchorRectangle(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickInputMethod::anchorRectangle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickinputmethod.html#anchorRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickInputMethod::anchorRectangle() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickInputMethod15anchorRectangleEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def cursorRectangle(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickInputMethod::cursorRectangle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickinputmethod.html#cursorRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickInputMethod::cursorRectangle() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickInputMethod15cursorRectangleEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def inputDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QQuickInputMethod::inputDirection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickinputmethod.html#inputDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QQuickInputMethod::inputDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK17QQuickInputMethod14inputDirectionEv',
    ))

  def inputItemClipRectangle(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickInputMethod::inputItemClipRectangle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickinputmethod.html#inputItemClipRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickInputMethod::inputItemClipRectangle() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickInputMethod22inputItemClipRectangleEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def inputItemRectangle(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickInputMethod::inputItemRectangle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickinputmethod.html#inputItemRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickInputMethod::inputItemRectangle() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickInputMethod18inputItemRectangleEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def inputItemTransform(self) -> QTransform:
    """
    Calls Qt's 'QTransform QQuickInputMethod::inputItemTransform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickinputmethod.html#inputItemTransform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QQuickInputMethod::inputItemTransform() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickInputMethod18inputItemTransformEv',
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  def isAnimating(self) -> bool:
    """
    Calls Qt's 'bool QQuickInputMethod::isAnimating() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickinputmethod.html#isAnimating
    """
    #  bool QQuickInputMethod::isAnimating() const
    return self.uglySide.call('ritual_ZNK17QQuickInputMethod11isAnimatingEv')

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QQuickInputMethod::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickinputmethod.html#isVisible
    """
    #  bool QQuickInputMethod::isVisible() const
    return self.uglySide.call('ritual_ZNK17QQuickInputMethod9isVisibleEv')

  def keyboardRectangle(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickInputMethod::keyboardRectangle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickinputmethod.html#keyboardRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickInputMethod::keyboardRectangle() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickInputMethod17keyboardRectangleEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QQuickInputMethod::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickinputmethod.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QQuickInputMethod::locale() const
    address = self.uglySide.call('ritual_ZNK17QQuickInputMethod6localeEv')
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setInputItemRectangle(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QQuickInputMethod::setInputItemRectangle(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickinputmethod.html#setInputItemRectangle

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickInputMethod::setInputItemRectangle(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN17QQuickInputMethod21setInputItemRectangleERK6QRectF',
        self._valueOf(rect),
    )

  @overload(QTransform)
  def setInputItemTransform(self, transform: QTransform) -> None:
    """
    Calls Qt's 'void QQuickInputMethod::setInputItemTransform(const
    QTransform &transform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickinputmethod.html#setInputItemTransform

    Parameters
    ----------

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QQuickInputMethod::setInputItemTransform(const QTransform
    #      &transform)
    self.uglySide.call(
        'ritual_ZN17QQuickInputMethod21setInputItemTransformERK10QTransform',
        self._valueOf(transform),
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QQuickInputMethod::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickinputmethod.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QQuickInputMethod::setVisible(bool visible)
    self.uglySide.call('ritual_ZN17QQuickInputMethod10setVisibleEb', visible)

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
    'QQuickInputMethod::QQuickInputMethod(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickinputmethod.html#QQuickInputMethod

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickInputMethod::QQuickInputMethod(QObject *parent)
    self._noteCreation(QQuickInputMethod, lambda: Rituals.call(
        'ritual_ZN17QQuickInputMethodC1EP7QObject',
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

  def anchorRectangleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickInputMethod::anchorRectangleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickinputmethod.html#anchorRectangleChanged
    """
    #  void QQuickInputMethod::anchorRectangleChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickInputMethod22anchorRectangleChangedEv',
    )

  def animatingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickInputMethod::animatingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickinputmethod.html#animatingChanged
    """
    #  void QQuickInputMethod::animatingChanged()
    self.uglySide.call('ritual_ZN17QQuickInputMethod16animatingChangedEv')

  def cursorRectangleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickInputMethod::cursorRectangleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickinputmethod.html#cursorRectangleChanged
    """
    #  void QQuickInputMethod::cursorRectangleChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickInputMethod22cursorRectangleChangedEv',
    )

  @overload(Qt.LayoutDirection)
  def inputDirectionChanged(self, newDirection: Qt.LayoutDirection) -> None:
    """
    Calls Qt's 'void
    QQuickInputMethod::inputDirectionChanged(Qt::LayoutDirection
    newDirection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickinputmethod.html#inputDirectionChanged

    Parameters
    ----------

    newDirection : Qt.LayoutDirection
      Passed on as its number.
    """
    #  void QQuickInputMethod::inputDirectionChanged(Qt::LayoutDirection
    #      newDirection)
    self.uglySide.call(
        'ritual_ZN17QQuickInputMethod21inputDirectionChangedEN2Qt15LayoutDi'
        'rectionE',
        newDirection.value,
    )

  def inputItemClipRectangleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickInputMethod::inputItemClipRectangleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickinputmethod.html
    """
    #  void QQuickInputMethod::inputItemClipRectangleChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickInputMethod29inputItemClipRectangleChangedEv',
    )

  def keyboardRectangleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickInputMethod::keyboardRectangleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickinputmethod.html#keyboardRectangleChanged
    """
    #  void QQuickInputMethod::keyboardRectangleChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickInputMethod24keyboardRectangleChangedEv',
    )

  def localeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickInputMethod::localeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickinputmethod.html#localeChanged
    """
    #  void QQuickInputMethod::localeChanged()
    self.uglySide.call('ritual_ZN17QQuickInputMethod13localeChangedEv')

  def visibleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickInputMethod::visibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickinputmethod.html#visibleChanged
    """
    #  void QQuickInputMethod::visibleChanged()
    self.uglySide.call('ritual_ZN17QQuickInputMethod14visibleChangedEv')

  def commit(self) -> None:
    """
    Calls Qt's 'void QQuickInputMethod::commit()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickinputmethod.html#commit
    """
    #  void QQuickInputMethod::commit()
    self.uglySide.call('ritual_ZN17QQuickInputMethod6commitEv')

  def hide(self) -> None:
    """
    Calls Qt's 'void QQuickInputMethod::hide()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickinputmethod.html#hide
    """
    #  void QQuickInputMethod::hide()
    self.uglySide.call('ritual_ZN17QQuickInputMethod4hideEv')

  @overload(QInputMethod.Action, int)
  def invokeAction(
      self,
      a: QInputMethod.Action,
      cursorPosition: int,
  ) -> None:
    """
    Calls Qt's 'void QQuickInputMethod::invokeAction(QInputMethod::Action a,
    int cursorPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickinputmethod.html#invokeAction

    Parameters
    ----------

    a : QInputMethod.Action
      Passed on as its number.

    cursorPosition : int
      Passed on as it is.
    """
    #  void QQuickInputMethod::invokeAction(QInputMethod::Action a, int
    #      cursorPosition)
    self.uglySide.call(
        'ritual_ZN17QQuickInputMethod12invokeActionEN12QInputMethod6ActionE'
        'i',
        a.value, cursorPosition,
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuickInputMethod::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickinputmethod.html#reset
    """
    #  void QQuickInputMethod::reset()
    self.uglySide.call('ritual_ZN17QQuickInputMethod5resetEv')

  def show(self) -> None:
    """
    Calls Qt's 'void QQuickInputMethod::show()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickinputmethod.html#show
    """
    #  void QQuickInputMethod::show()
    self.uglySide.call('ritual_ZN17QQuickInputMethod4showEv')

  @overload(Qt.InputMethodQueries)
  def update(self, queries: Qt.InputMethodQueries) -> None:
    """
    Calls Qt's 'void QQuickInputMethod::update(Qt::InputMethodQueries
    queries)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickinputmethod.html#update

    Parameters
    ----------

    queries : Qt.InputMethodQueries
      Passed on as its number.
    """
    #  void QQuickInputMethod::update(Qt::InputMethodQueries queries)
    self.uglySide.call(
        'ritual_ZN17QQuickInputMethod6updateE6QFlagsIN2Qt16InputMethodQuery'
        'EE',
        queries.value,
    )
