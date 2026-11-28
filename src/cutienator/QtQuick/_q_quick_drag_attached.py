"""
QQuickDragAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickdrag_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickDragAttached to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QMap, QObject, QStringList
from . import QQuickDrag

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QPointF, QSize, QUrl, QVariant
  from ..QtQml import QQmlV4Function
  from . import QQuickDragAttachedPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QPointF = WAIT['QPointF']
  QQmlV4Function = WAIT['QQmlV4Function']
  QSize = WAIT['QSize']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDragAttached(QObject):
  """
  The cute side of Qt's QQuickDragAttached: a plain Python object standing in
  front of one C++ QQuickDragAttached.

  It is built on the cute 'QObject', as Qt's QQuickDragAttached is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDragAttached that has a ritual and that Python
  can call so far, 43 names in all: 'metaObject', 'tr', 'd_func', 'isActive',
  'setActive', 'source', 'setSource', 'resetSource', 'target', 'hotSpot',
  'setHotSpot', 'imageSource', 'setImageSource', 'imageSourceSize',
  'setImageSourceSize', 'keys', 'setKeys', 'mimeData', 'setMimeData',
  'supportedActions', 'setSupportedActions', 'proposedAction',
  'setProposedAction', 'dragType', 'setDragType', 'drop', 'event', 'start',
  'startDrag', 'cancel', 'dragStarted', 'dragFinished', 'activeChanged',
  'sourceChanged', 'targetChanged', 'hotSpotChanged', 'imageSourceChanged',
  'imageSourceSizeChanged', 'keysChanged', 'mimeDataChanged',
  'supportedActionsChanged', 'proposedActionChanged', 'dragTypeChanged'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickDragAttached::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickDragAttached::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickDragAttachedPrivate *QQuickDragAttached::d_func()
    const': takes in Python what 'QQuickDragAttachedPrivate
    *QQuickDragAttached::d_func()' takes.
  - Qt's 'void QQuickDragAttached::qt_qmlMarker_anonymous()': one of Qt's own
    inner workings.
  - Qt's 'QQuickDragAttached::~QQuickDragAttached()': the destructor: Python
    never removes a C++ QQuickDragAttached.

  What has no ritual
  ------------------

  2 of the 51 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickDragAttached is created at the first use, not by
    'QQuickDragAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDragAttached.
  - Qt tells when it has removed the C++ QQuickDragAttached. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickDragAttached::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragattached.html#tr

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
    #  QString QQuickDragAttached::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickDragAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDragAttached'

  #  A C++ QQuickDragAttached Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickDragAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickDragAttached::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickDragAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickDragAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QQuickDragAttached::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragattached.html#isActive
    """
    #  bool QQuickDragAttached::isActive() const
    return self.uglySide.call('ritual_ZNK18QQuickDragAttached8isActiveEv')

  def source(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQuickDragAttached::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragattached.html#source

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickDragAttached::source() const
    address = self.uglySide.call('ritual_ZNK18QQuickDragAttached6sourceEv')
    return QObject._cuteAt(address)

  def target(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQuickDragAttached::target() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragattached.html#target

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickDragAttached::target() const
    address = self.uglySide.call('ritual_ZNK18QQuickDragAttached6targetEv')
    return QObject._cuteAt(address)

  def hotSpot(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickDragAttached::hotSpot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragattached.html#hotSpot

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickDragAttached::hotSpot() const
    address = self.uglySide.call('ritual_ZNK18QQuickDragAttached7hotSpotEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def imageSource(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickDragAttached::imageSource() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#imageSource

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickDragAttached::imageSource() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickDragAttached11imageSourceEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def imageSourceSize(self) -> QSize:
    """
    Calls Qt's 'QSize QQuickDragAttached::imageSourceSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#imageSourceSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuickDragAttached::imageSourceSize() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickDragAttached15imageSourceSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def keys(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuickDragAttached::keys() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragattached.html#keys

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickDragAttached::keys() const
    address = self.uglySide.call('ritual_ZNK18QQuickDragAttached4keysEv')
    return QStringList._cuteOwning(address)

  def mimeData(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QQuickDragAttached::mimeData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragattached.html#mimeData

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QQuickDragAttached::mimeData() const
    address = self.uglySide.call('ritual_ZNK18QQuickDragAttached8mimeDataEv')
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  def supportedActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QQuickDragAttached::supportedActions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#supportedActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QQuickDragAttached::supportedActions() const
    return Qt.DropActions(self.uglySide.call(
        'ritual_ZNK18QQuickDragAttached16supportedActionsEv',
    ))

  def proposedAction(self) -> Qt.DropAction:
    """
    Calls Qt's 'Qt::DropAction QQuickDragAttached::proposedAction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#proposedAction

    Returns
    -------

    Qt.DropAction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.DropAction(number)'
      gives.
    """
    #  Qt::DropAction QQuickDragAttached::proposedAction() const
    return Qt.DropAction(self.uglySide.call(
        'ritual_ZNK18QQuickDragAttached14proposedActionEv',
    ))

  def dragType(self) -> QQuickDrag.DragType:
    """
    Calls Qt's 'QQuickDrag::DragType QQuickDragAttached::dragType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragattached.html#dragType

    Returns
    -------

    QQuickDrag.DragType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickDrag.DragType(number)' gives.
    """
    #  QQuickDrag::DragType QQuickDragAttached::dragType() const
    return QQuickDrag.DragType(self.uglySide.call(
        'ritual_ZNK18QQuickDragAttached8dragTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setActive(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::setActive(bool active)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragattached.html#setActive

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickDragAttached::setActive(bool active)
    self.uglySide.call('ritual_ZN18QQuickDragAttached9setActiveEb', active)

  @overload(QObject)
  @overload(NoneType)
  def setSource(self, item: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::setSource(QObject *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragattached.html#setSource

    Parameters
    ----------

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDragAttached::setSource(QObject *item)
    self.uglySide.call(
        'ritual_ZN18QQuickDragAttached9setSourceEP7QObject',
        self._addressOf(item, 'QObject'),
    )

  @overload(QPointF)
  def setHotSpot(self, hotSpot: QPointF) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::setHotSpot(const QPointF &hotSpot)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragattached.html#setHotSpot

    Parameters
    ----------

    hotSpot : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickDragAttached::setHotSpot(const QPointF &hotSpot)
    self.uglySide.call(
        'ritual_ZN18QQuickDragAttached10setHotSpotERK7QPointF',
        self._valueOf(hotSpot, 'QPointF'),
    )

  @overload(QUrl)
  def setImageSource(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::setImageSource(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#setImageSource

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickDragAttached::setImageSource(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN18QQuickDragAttached14setImageSourceERK4QUrl',
        self._valueOf(url),
    )

  @overload(QSize)
  def setImageSourceSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::setImageSourceSize(const QSize
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#setImageSourceSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QQuickDragAttached::setImageSourceSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN18QQuickDragAttached18setImageSourceSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(QStringList)
  def setKeys(self, keys: QStringList) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::setKeys(const QStringList &keys)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragattached.html#setKeys

    Parameters
    ----------

    keys : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickDragAttached::setKeys(const QStringList &keys)
    self.uglySide.call(
        'ritual_ZN18QQuickDragAttached7setKeysERK5QListI7QStringE',
        self._valueOf(keys),
    )

  @overload(QMap[str, QVariant])
  def setMimeData(self, mimeData: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::setMimeData(const QVariantMap
    &mimeData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#setMimeData

    Parameters
    ----------

    mimeData : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QQuickDragAttached::setMimeData(const QVariantMap &mimeData)
    self.uglySide.call(
        'ritual_ZN18QQuickDragAttached11setMimeDataERK4QMapI7QString8QVaria'
        'ntE',
        self._valueOf(mimeData),
    )

  @overload(Qt.DropActions)
  def setSupportedActions(self, actions: Qt.DropActions) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::setSupportedActions(Qt::DropActions
    actions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#setSupportedActions

    Parameters
    ----------

    actions : Qt.DropActions
      Passed on as its number.
    """
    #  void QQuickDragAttached::setSupportedActions(Qt::DropActions actions)
    self.uglySide.call(
        'ritual_ZN18QQuickDragAttached19setSupportedActionsE6QFlagsIN2Qt10D'
        'ropActionEE',
        actions.value,
    )

  @overload(Qt.DropAction)
  def setProposedAction(self, action: Qt.DropAction) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::setProposedAction(Qt::DropAction
    action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#setProposedAction

    Parameters
    ----------

    action : Qt.DropAction
      Passed on as its number.
    """
    #  void QQuickDragAttached::setProposedAction(Qt::DropAction action)
    self.uglySide.call(
        'ritual_ZN18QQuickDragAttached17setProposedActionEN2Qt10DropActionE',
        action.value,
    )

  @overload(QQuickDrag.DragType)
  def setDragType(self, dragType: QQuickDrag.DragType) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::setDragType(QQuickDrag::DragType
    dragType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#setDragType

    Parameters
    ----------

    dragType : QQuickDrag.DragType
      Passed on as its number.
    """
    #  void QQuickDragAttached::setDragType(QQuickDrag::DragType dragType)
    self.uglySide.call(
        'ritual_ZN18QQuickDragAttached11setDragTypeEN10QQuickDrag8DragTypeE',
        dragType.value,
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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickDragAttached::QQuickDragAttached(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#QQuickDragAttached

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickDragAttached::QQuickDragAttached(QObject *parent)
    self._noteCreation(QQuickDragAttached, lambda: Rituals.call(
        'ritual_ZN18QQuickDragAttachedC1EP7QObject',
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

  def d_func(self) -> Optional[QQuickDragAttachedPrivate]:
    """
    Calls Qt's 'QQuickDragAttachedPrivate *QQuickDragAttached::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragattached.html#d_func

    Returns
    -------

    Optional[QQuickDragAttachedPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDragAttachedPrivate *QQuickDragAttached::d_func()
    address = self.uglySide.call('ritual_ZN18QQuickDragAttached6d_funcEv')
    from . import QQuickDragAttachedPrivate
    return QQuickDragAttachedPrivate._cuteAt(address)

  def resetSource(self) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::resetSource()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#resetSource
    """
    #  void QQuickDragAttached::resetSource()
    self.uglySide.call('ritual_ZN18QQuickDragAttached11resetSourceEv')

  def drop(self) -> int:
    """
    Calls Qt's 'int QQuickDragAttached::drop()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragattached.html#drop
    """
    #  int QQuickDragAttached::drop()
    return self.uglySide.call('ritual_ZN18QQuickDragAttached4dropEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickDragAttached::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragattached.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDragAttached::event(QEvent *event)
    ritual = 'ritual_ZN18QQuickDragAttached5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickDragAttached5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QQmlV4Function)
  @overload(NoneType)
  def start(self, a0: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::start(QQmlV4FunctionPtr a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragattached.html#start

    Parameters
    ----------

    a0 : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDragAttached::start(QQmlV4FunctionPtr a0)
    self.uglySide.call(
        'ritual_ZN18QQuickDragAttached5startEP14QQmlV4Function',
        self._addressOf(a0),
    )

  @overload(QQmlV4Function)
  @overload(NoneType)
  def startDrag(self, a0: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::startDrag(QQmlV4FunctionPtr a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragattached.html#startDrag

    Parameters
    ----------

    a0 : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDragAttached::startDrag(QQmlV4FunctionPtr a0)
    self.uglySide.call(
        'ritual_ZN18QQuickDragAttached9startDragEP14QQmlV4Function',
        self._addressOf(a0),
    )

  def cancel(self) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::cancel()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragattached.html#cancel
    """
    #  void QQuickDragAttached::cancel()
    self.uglySide.call('ritual_ZN18QQuickDragAttached6cancelEv')

  def dragStarted(self) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::dragStarted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#dragStarted
    """
    #  void QQuickDragAttached::dragStarted()
    self.uglySide.call('ritual_ZN18QQuickDragAttached11dragStartedEv')

  @overload(Qt.DropAction)
  def dragFinished(self, dropAction: Qt.DropAction) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::dragFinished(Qt::DropAction
    dropAction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#dragFinished

    Parameters
    ----------

    dropAction : Qt.DropAction
      Passed on as its number.
    """
    #  void QQuickDragAttached::dragFinished(Qt::DropAction dropAction)
    self.uglySide.call(
        'ritual_ZN18QQuickDragAttached12dragFinishedEN2Qt10DropActionE',
        dropAction.value,
    )

  def activeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::activeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#activeChanged
    """
    #  void QQuickDragAttached::activeChanged()
    self.uglySide.call('ritual_ZN18QQuickDragAttached13activeChangedEv')

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#sourceChanged
    """
    #  void QQuickDragAttached::sourceChanged()
    self.uglySide.call('ritual_ZN18QQuickDragAttached13sourceChangedEv')

  def targetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::targetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#targetChanged
    """
    #  void QQuickDragAttached::targetChanged()
    self.uglySide.call('ritual_ZN18QQuickDragAttached13targetChangedEv')

  def hotSpotChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::hotSpotChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#hotSpotChanged
    """
    #  void QQuickDragAttached::hotSpotChanged()
    self.uglySide.call('ritual_ZN18QQuickDragAttached14hotSpotChangedEv')

  def imageSourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::imageSourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#imageSourceChanged
    """
    #  void QQuickDragAttached::imageSourceChanged()
    self.uglySide.call('ritual_ZN18QQuickDragAttached18imageSourceChangedEv')

  def imageSourceSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::imageSourceSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#imageSourceSizeChanged
    """
    #  void QQuickDragAttached::imageSourceSizeChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickDragAttached22imageSourceSizeChangedEv',
    )

  def keysChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::keysChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#keysChanged
    """
    #  void QQuickDragAttached::keysChanged()
    self.uglySide.call('ritual_ZN18QQuickDragAttached11keysChangedEv')

  def mimeDataChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::mimeDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#mimeDataChanged
    """
    #  void QQuickDragAttached::mimeDataChanged()
    self.uglySide.call('ritual_ZN18QQuickDragAttached15mimeDataChangedEv')

  def supportedActionsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::supportedActionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#supportedActionsChanged
    """
    #  void QQuickDragAttached::supportedActionsChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickDragAttached23supportedActionsChangedEv',
    )

  def proposedActionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::proposedActionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#proposedActionChanged
    """
    #  void QQuickDragAttached::proposedActionChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickDragAttached21proposedActionChangedEv',
    )

  def dragTypeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDragAttached::dragTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattached.html#dragTypeChanged
    """
    #  void QQuickDragAttached::dragTypeChanged()
    self.uglySide.call('ritual_ZN18QQuickDragAttached15dragTypeChangedEv')
