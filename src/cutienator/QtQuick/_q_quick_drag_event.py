"""
QQuickDragEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickdroparea_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickDragEvent to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QUrl, QVariant

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDragEvent(QObject):
  """
  The cute side of Qt's QQuickDragEvent: a plain Python object standing in
  front of one C++ QQuickDragEvent.

  It is built on the cute 'QObject', as Qt's QQuickDragEvent is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDragEvent that has a ritual and that Python
  can call so far, 26 names in all: 'metaObject', 'tr', 'x', 'y', 'source',
  'supportedActions', 'proposedAction', 'action', 'setAction', 'resetAction',
  'keys', 'accepted', 'setAccepted', 'hasColor', 'hasHtml', 'hasText',
  'hasUrls', 'colorData', 'html', 'text', 'urls', 'formats',
  'getDataAsString', 'getDataAsArrayBuffer', 'acceptProposedAction',
  'accept'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickDragEvent::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickDragEvent::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickDragEvent::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QQuickDragEvent::QQuickDragEvent(QQuickDropAreaPrivate *d,
    QDropEvent *event)': names 'QQuickDropAreaPrivate', which has no cute
    class yet.

  What has no ritual
  ------------------

  2 of the 33 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickDragEvent is created at the first use, not by
    'QQuickDragEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDragEvent.
  - Qt tells when it has removed the C++ QQuickDragEvent. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickDragEvent that has no cute function yet,
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
    Calls Qt's 'QString QQuickDragEvent::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragevent.html#tr

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
    #  QString QQuickDragEvent::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickDragEvent2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDragEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickDragEvent::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragevent.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickDragEvent::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickDragEvent10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def x(self) -> float:
    """
    Calls Qt's 'qreal QQuickDragEvent::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragevent.html#x
    """
    #  qreal QQuickDragEvent::x() const
    return self.uglySide.call('ritual_ZNK15QQuickDragEvent1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QQuickDragEvent::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragevent.html#y
    """
    #  qreal QQuickDragEvent::y() const
    return self.uglySide.call('ritual_ZNK15QQuickDragEvent1yEv')

  def source(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQuickDragEvent::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragevent.html#source

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickDragEvent::source() const
    address = self.uglySide.call('ritual_ZNK15QQuickDragEvent6sourceEv')
    return QObject._cuteAt(address)

  def supportedActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QQuickDragEvent::supportedActions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragevent.html#supportedActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QQuickDragEvent::supportedActions() const
    return Qt.DropActions(self.uglySide.call(
        'ritual_ZNK15QQuickDragEvent16supportedActionsEv',
    ))

  def proposedAction(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QQuickDragEvent::proposedAction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragevent.html#proposedAction

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QQuickDragEvent::proposedAction() const
    return Qt.DropActions(self.uglySide.call(
        'ritual_ZNK15QQuickDragEvent14proposedActionEv',
    ))

  def action(self) -> Qt.DropAction:
    """
    Calls Qt's 'Qt::DropAction QQuickDragEvent::action() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragevent.html#action

    Returns
    -------

    Qt.DropAction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.DropAction(number)'
      gives.
    """
    #  Qt::DropAction QQuickDragEvent::action() const
    return Qt.DropAction(self.uglySide.call(
        'ritual_ZNK15QQuickDragEvent6actionEv',
    ))

  def keys(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuickDragEvent::keys() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragevent.html#keys

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickDragEvent::keys() const
    address = self.uglySide.call('ritual_ZNK15QQuickDragEvent4keysEv')
    return QStringList._cuteOwning(address)

  def accepted(self) -> bool:
    """
    Calls Qt's 'bool QQuickDragEvent::accepted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragevent.html#accepted
    """
    #  bool QQuickDragEvent::accepted() const
    return self.uglySide.call('ritual_ZNK15QQuickDragEvent8acceptedEv')

  def hasColor(self) -> bool:
    """
    Calls Qt's 'bool QQuickDragEvent::hasColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragevent.html#hasColor
    """
    #  bool QQuickDragEvent::hasColor() const
    return self.uglySide.call('ritual_ZNK15QQuickDragEvent8hasColorEv')

  def hasHtml(self) -> bool:
    """
    Calls Qt's 'bool QQuickDragEvent::hasHtml() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragevent.html#hasHtml
    """
    #  bool QQuickDragEvent::hasHtml() const
    return self.uglySide.call('ritual_ZNK15QQuickDragEvent7hasHtmlEv')

  def hasText(self) -> bool:
    """
    Calls Qt's 'bool QQuickDragEvent::hasText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragevent.html#hasText
    """
    #  bool QQuickDragEvent::hasText() const
    return self.uglySide.call('ritual_ZNK15QQuickDragEvent7hasTextEv')

  def hasUrls(self) -> bool:
    """
    Calls Qt's 'bool QQuickDragEvent::hasUrls() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragevent.html#hasUrls
    """
    #  bool QQuickDragEvent::hasUrls() const
    return self.uglySide.call('ritual_ZNK15QQuickDragEvent7hasUrlsEv')

  def colorData(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickDragEvent::colorData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragevent.html#colorData

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickDragEvent::colorData() const
    address = self.uglySide.call('ritual_ZNK15QQuickDragEvent9colorDataEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def html(self) -> str:
    """
    Calls Qt's 'QString QQuickDragEvent::html() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragevent.html#html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickDragEvent::html() const
    return self.uglySide.call('ritual_ZNK15QQuickDragEvent4htmlEv')

  def text(self) -> str:
    """
    Calls Qt's 'QString QQuickDragEvent::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragevent.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickDragEvent::text() const
    return self.uglySide.call('ritual_ZNK15QQuickDragEvent4textEv')

  def urls(self) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl> QQuickDragEvent::urls() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragevent.html#urls

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl> QQuickDragEvent::urls() const
    address = self.uglySide.call('ritual_ZNK15QQuickDragEvent4urlsEv')
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  def formats(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuickDragEvent::formats() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragevent.html#formats

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickDragEvent::formats() const
    address = self.uglySide.call('ritual_ZNK15QQuickDragEvent7formatsEv')
    return QStringList._cuteOwning(address)

  @overload(str)
  def getDataAsString(self, format: str) -> str:
    """
    Calls Qt's 'QString QQuickDragEvent::getDataAsString(const QString
    &format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragevent.html#getDataAsString

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickDragEvent::getDataAsString(const QString &format) const
    return self.uglySide.call(
        'ritual_ZNK15QQuickDragEvent15getDataAsStringERK7QString', format,
    )

  @overload(str)
  def getDataAsArrayBuffer(self, format: str) -> QByteArray:
    """
    Calls Qt's 'QByteArray QQuickDragEvent::getDataAsArrayBuffer(const
    QString &format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragevent.html#getDataAsArrayBuffer

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QQuickDragEvent::getDataAsArrayBuffer(const QString
    #      &format) const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickDragEvent20getDataAsArrayBufferERK7QString',
        format,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.DropAction)
  def setAction(self, action: Qt.DropAction) -> None:
    """
    Calls Qt's 'void QQuickDragEvent::setAction(Qt::DropAction action)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragevent.html#setAction

    Parameters
    ----------

    action : Qt.DropAction
      Passed on as its number.
    """
    #  void QQuickDragEvent::setAction(Qt::DropAction action)
    self.uglySide.call(
        'ritual_ZN15QQuickDragEvent9setActionEN2Qt10DropActionE',
        action.value,
    )

  @overload(bool)
  def setAccepted(self, accepted: bool) -> None:
    """
    Calls Qt's 'void QQuickDragEvent::setAccepted(bool accepted)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragevent.html#setAccepted

    Parameters
    ----------

    accepted : bool
      Passed on as it is.
    """
    #  void QQuickDragEvent::setAccepted(bool accepted)
    self.uglySide.call('ritual_ZN15QQuickDragEvent11setAcceptedEb', accepted)

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
    Qt's 'QQuickDragEvent::QQuickDragEvent(QQuickDropAreaPrivate *d,
    QDropEvent *event)': names 'QQuickDropAreaPrivate', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickDragEvent.__init__' has no cute function yet. Qt's "
        "'QQuickDragEvent::QQuickDragEvent(QQuickDropAreaPrivate *d, "
        "QDropEvent *event)': names 'QQuickDropAreaPrivate', which has no "
        "cute class yet.")

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

  def resetAction(self) -> None:
    """
    Calls Qt's 'void QQuickDragEvent::resetAction()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragevent.html#resetAction
    """
    #  void QQuickDragEvent::resetAction()
    self.uglySide.call('ritual_ZN15QQuickDragEvent11resetActionEv')

  def acceptProposedAction(self) -> None:
    """
    Calls Qt's 'void QQuickDragEvent::acceptProposedAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragevent.html#acceptProposedAction
    """
    #  void QQuickDragEvent::acceptProposedAction()
    self.uglySide.call('ritual_ZN15QQuickDragEvent20acceptProposedActionEv')

  @overload()
  def accept(self) -> None:
    """
    Calls Qt's 'void QQuickDragEvent::accept()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragevent.html#accept
    """
    #  void QQuickDragEvent::accept()
    self.uglySide.call('ritual_ZN15QQuickDragEvent6acceptEv')

  @overload(Qt.DropAction)
  def accept(self, action: Qt.DropAction) -> None:
    """
    Calls Qt's 'void QQuickDragEvent::accept(Qt::DropAction action)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragevent.html#accept

    Parameters
    ----------

    action : Qt.DropAction
      Passed on as its number.
    """
    #  void QQuickDragEvent::accept(Qt::DropAction action)
    self.uglySide.call(
        'ritual_ZN15QQuickDragEvent6acceptEN2Qt10DropActionE', action.value,
    )
