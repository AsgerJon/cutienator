"""
QWebEngineNotification binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebenginenotification.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtGui import QImage

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineNotification(QObject):
  """
  The cute side of Qt's QWebEngineNotification: a plain Python object
  standing in front of one C++ QWebEngineNotification.

  It is built on the cute 'QObject', as Qt's QWebEngineNotification is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebEngineNotification that has a ritual and that
  Python can call so far, 14 names in all: 'metaObject', 'tr', 'matches',
  'origin', 'icon', 'title', 'message', 'tag', 'language', 'direction',
  'show', 'click', 'close', 'closed'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebEngineNotification::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QWebEngineNotification::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWebEngineNotification::~QWebEngineNotification()': the destructor:
    Python never removes a C++ QWebEngineNotification.
  - Qt's 'QWebEngineNotificationPrivate *QWebEngineNotification::d_func()':
    gives 'QWebEngineNotificationPrivate', which has no cute class yet.
  - Qt's 'const QWebEngineNotificationPrivate
    *QWebEngineNotification::d_func() const': gives
    'QWebEngineNotificationPrivate', which has no cute class yet.
  - Qt's 'QWebEngineNotification::QWebEngineNotification(const
    QSharedPointer<QtWebEngineCore::UserNotificationController>
    &controller)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 24 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QWebEngineNotification is created at the first use, not by
    'QWebEngineNotification(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineNotification.
  - Qt tells when it has removed the C++ QWebEngineNotification. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWebEngineNotification that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QWebEngineNotification::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginenotification.html#tr

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
    #  QString QWebEngineNotification::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QWebEngineNotification2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineNotification'

  #  A C++ QWebEngineNotification Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebEngineNotification'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWebEngineNotification::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenotification.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebEngineNotification::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QWebEngineNotification10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(THIS)
  @overload(NoneType)
  def matches(self, other: Optional[QWebEngineNotification]) -> bool:
    """
    Calls Qt's 'bool QWebEngineNotification::matches(const
    QWebEngineNotification *other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenotification.html#matches

    Parameters
    ----------

    other : Optional[QWebEngineNotification]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWebEngineNotification::matches(const QWebEngineNotification
    #      *other) const
    return self.uglySide.call(
        'ritual_ZNK22QWebEngineNotification7matchesEPKS_',
        self._addressOf(other),
    )

  def origin(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineNotification::origin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginenotification.html#origin

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineNotification::origin() const
    address = self.uglySide.call(
        'ritual_ZNK22QWebEngineNotification6originEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def icon(self) -> QImage:
    """
    Calls Qt's 'QImage QWebEngineNotification::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginenotification.html#icon

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QWebEngineNotification::icon() const
    address = self.uglySide.call('ritual_ZNK22QWebEngineNotification4iconEv')
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def title(self) -> str:
    """
    Calls Qt's 'QString QWebEngineNotification::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginenotification.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineNotification::title() const
    return self.uglySide.call('ritual_ZNK22QWebEngineNotification5titleEv')

  def message(self) -> str:
    """
    Calls Qt's 'QString QWebEngineNotification::message() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenotification.html#message

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineNotification::message() const
    return self.uglySide.call('ritual_ZNK22QWebEngineNotification7messageEv')

  def tag(self) -> str:
    """
    Calls Qt's 'QString QWebEngineNotification::tag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginenotification.html#tag

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineNotification::tag() const
    return self.uglySide.call('ritual_ZNK22QWebEngineNotification3tagEv')

  def language(self) -> str:
    """
    Calls Qt's 'QString QWebEngineNotification::language() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenotification.html#language

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineNotification::language() const
    return self.uglySide.call(
        'ritual_ZNK22QWebEngineNotification8languageEv',
    )

  def direction(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QWebEngineNotification::direction()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginenotification.html#direction

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QWebEngineNotification::direction() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK22QWebEngineNotification9directionEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QWebEngineNotification::QWebEngineNotification(const
    QSharedPointer<QtWebEngineCore::UserNotificationController>
    &controller)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebEngineNotification.__init__' has no cute function yet. Qt's "
        "'QWebEngineNotification::QWebEngineNotification(const "
        "QSharedPointer<QtWebEngineCore::UserNotificationController> "
        "&controller)': takes a type Python has no way to hand over yet.")

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
    Calls Qt's 'void QWebEngineNotification::show() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginenotification.html#show
    """
    #  void QWebEngineNotification::show() const
    self.uglySide.call('ritual_ZNK22QWebEngineNotification4showEv')

  def click(self) -> None:
    """
    Calls Qt's 'void QWebEngineNotification::click() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginenotification.html#click
    """
    #  void QWebEngineNotification::click() const
    self.uglySide.call('ritual_ZNK22QWebEngineNotification5clickEv')

  def close(self) -> None:
    """
    Calls Qt's 'void QWebEngineNotification::close() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginenotification.html#close
    """
    #  void QWebEngineNotification::close() const
    self.uglySide.call('ritual_ZNK22QWebEngineNotification5closeEv')

  def closed(self) -> None:
    """
    Calls Qt's 'void QWebEngineNotification::closed()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginenotification.html#closed
    """
    #  void QWebEngineNotification::closed()
    self.uglySide.call('ritual_ZN22QWebEngineNotification6closedEv')
