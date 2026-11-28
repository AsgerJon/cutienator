"""
QQmlWebChannel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebChannelQuick/qqmlwebchannel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlWebChannelAttached
  from ..QtCore import QMetaObject, QObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlWebChannel(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlWebChannel: a plain Python object standing in
  front of one C++ QQmlWebChannel.

  What exists
  -----------

  Every function of Qt's QQmlWebChannel that has a ritual and that Python can
  call so far, 6 names in all: 'metaObject', 'tr', 'registerObjects',
  'qmlAttachedProperties', 'connectTo', 'disconnectFrom'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlWebChannel::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQmlWebChannel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQmlWebChannel::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'QQmlWebChannel::~QQmlWebChannel()': the destructor: Python never
    removes a C++ QQmlWebChannel.
  - Qt's 'QQmlListProperty<QObject> QQmlWebChannel::registeredObjects()':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlListProperty<QObject> QQmlWebChannel::transports()': gives a
    type Python has no way to take yet.
  - Qt's 'QQmlWebChannelPrivate *QQmlWebChannel::d_func()': gives
    'QQmlWebChannelPrivate', which has no cute class yet.
  - Qt's 'const QQmlWebChannelPrivate *QQmlWebChannel::d_func() const': gives
    'QQmlWebChannelPrivate', which has no cute class yet.
  - Qt's 'void
    QQmlWebChannel::registeredObjects_append(QQmlListProperty<QObject> *prop,
    QObject *item)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'qsizetype
    QQmlWebChannel::registeredObjects_count(QQmlListProperty<QObject>
    *prop)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QObject
    *QQmlWebChannel::registeredObjects_at(QQmlListProperty<QObject> *prop,
    qsizetype index)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'void
    QQmlWebChannel::registeredObjects_clear(QQmlListProperty<QObject>
    *prop)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'void QQmlWebChannel::transports_append(QQmlListProperty<QObject>
    *prop, QObject *item)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
  - Qt's 'qsizetype
    QQmlWebChannel::transports_count(QQmlListProperty<QObject> *prop)': names
    'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QObject *QQmlWebChannel::transports_at(QQmlListProperty<QObject>
    *prop, qsizetype index)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
  - Qt's 'void QQmlWebChannel::transports_clear(QQmlListProperty<QObject>
    *prop)': names 'QQmlListProperty<QObject>', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 27 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQmlWebChannel is created at the first use, not by
    'QQmlWebChannel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlWebChannel.
  - Qt tells when it has removed the C++ QQmlWebChannel. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlWebChannel that has no cute function yet,
    'registeredObjects_append', 'registeredObjects_at',
    'registeredObjects_clear', 'registeredObjects_count', 'transports',
    'transports_append', 'transports_at', 'transports_clear',
    'transports_count', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QQmlWebChannel::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlwebchannel.html#tr

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
    #  QString QQmlWebChannel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQmlWebChannel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      obj: Optional[QObject],
  ) -> Optional[QQmlWebChannelAttached]:
    """
    Calls Qt's 'QQmlWebChannelAttached
    *QQmlWebChannel::qmlAttachedProperties(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlwebchannel.html#qmlAttachedProperties

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlWebChannelAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlWebChannelAttached *QQmlWebChannel::qmlAttachedProperties(QObject
    #      *obj)
    address = Rituals.call(
        'ritual_ZN14QQmlWebChannel21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(obj, 'QObject'),
    )
    from . import QQmlWebChannelAttached
    return QQmlWebChannelAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlWebChannel'

  #  A C++ QQmlWebChannel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlWebChannel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlWebChannel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlwebchannel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlWebChannel::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQmlWebChannel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QQmlWebChannel::QQmlWebChannel(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlwebchannel.html#QQmlWebChannel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlWebChannel::QQmlWebChannel(QObject *parent)
    self._noteCreation(QQmlWebChannel, lambda: Rituals.call(
        'ritual_ZN14QQmlWebChannelC1EP7QObject',
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

  @overload(QMap[str, QVariant])
  def registerObjects(self, objects: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QQmlWebChannel::registerObjects(const QVariantMap
    &objects)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlwebchannel.html#registerObjects

    Parameters
    ----------

    objects : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QQmlWebChannel::registerObjects(const QVariantMap &objects)
    self.uglySide.call(
        'ritual_ZN14QQmlWebChannel15registerObjectsERK4QMapI7QString8QVaria'
        'ntE',
        self._valueOf(objects),
    )

  @overload(QObject)
  @overload(NoneType)
  def connectTo(self, transport: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlWebChannel::connectTo(QObject *transport)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlwebchannel.html#connectTo

    Parameters
    ----------

    transport : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlWebChannel::connectTo(QObject *transport)
    self.uglySide.call(
        'ritual_ZN14QQmlWebChannel9connectToEP7QObject',
        self._addressOf(transport, 'QObject'),
    )

  @overload(QObject)
  @overload(NoneType)
  def disconnectFrom(self, transport: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlWebChannel::disconnectFrom(QObject *transport)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlwebchannel.html#disconnectFrom

    Parameters
    ----------

    transport : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlWebChannel::disconnectFrom(QObject *transport)
    self.uglySide.call(
        'ritual_ZN14QQmlWebChannel14disconnectFromEP7QObject',
        self._addressOf(transport, 'QObject'),
    )

  @staticmethod
  def registeredObjects_append(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlWebChannel::registeredObjects_append(QQmlListProperty<QObject> *prop,
    QObject *item)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQmlWebChannel.registeredObjects_append' has no cute function "
        "yet. Qt's 'void "
        "QQmlWebChannel::registeredObjects_append(QQmlListProperty<QObject> "
        "*prop, QObject *item)': names 'QQmlListProperty<QObject>', which "
        "has no cute class yet.")

  @staticmethod
  def registeredObjects_at(*__, **_) -> Never:
    """
    Qt's 'QObject
    *QQmlWebChannel::registeredObjects_at(QQmlListProperty<QObject> *prop,
    qsizetype index)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQmlWebChannel.registeredObjects_at' has no cute function yet. "
        "Qt's 'QObject "
        "*QQmlWebChannel::registeredObjects_at(QQmlListProperty<QObject> "
        "*prop, qsizetype index)': names 'QQmlListProperty<QObject>', which "
        "has no cute class yet.")

  @staticmethod
  def registeredObjects_clear(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlWebChannel::registeredObjects_clear(QQmlListProperty<QObject>
    *prop)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlWebChannel.registeredObjects_clear' has no cute function yet. "
        "Qt's 'void "
        "QQmlWebChannel::registeredObjects_clear(QQmlListProperty<QObject> "
        "*prop)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def registeredObjects_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQmlWebChannel::registeredObjects_count(QQmlListProperty<QObject>
    *prop)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlWebChannel.registeredObjects_count' has no cute function yet. "
        "Qt's 'qsizetype "
        "QQmlWebChannel::registeredObjects_count(QQmlListProperty<QObject> "
        "*prop)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def transports(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQmlWebChannel::transports()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlWebChannel.transports' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQmlWebChannel::transports()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def transports_append(*__, **_) -> Never:
    """
    Qt's 'void QQmlWebChannel::transports_append(QQmlListProperty<QObject>
    *prop, QObject *item)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQmlWebChannel.transports_append' has no cute function yet. Qt's "
        "'void QQmlWebChannel::transports_append(QQmlListProperty<QObject> "
        "*prop, QObject *item)': names 'QQmlListProperty<QObject>', which "
        "has no cute class yet.")

  @staticmethod
  def transports_at(*__, **_) -> Never:
    """
    Qt's 'QObject *QQmlWebChannel::transports_at(QQmlListProperty<QObject>
    *prop, qsizetype index)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQmlWebChannel.transports_at' has no cute function yet. Qt's "
        "'QObject *QQmlWebChannel::transports_at(QQmlListProperty<QObject> "
        "*prop, qsizetype index)': names 'QQmlListProperty<QObject>', which "
        "has no cute class yet.")

  @staticmethod
  def transports_clear(*__, **_) -> Never:
    """
    Qt's 'void QQmlWebChannel::transports_clear(QQmlListProperty<QObject>
    *prop)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlWebChannel.transports_clear' has no cute function yet. Qt's "
        "'void QQmlWebChannel::transports_clear(QQmlListProperty<QObject> "
        "*prop)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def transports_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQmlWebChannel::transports_count(QQmlListProperty<QObject> *prop)': names
    'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlWebChannel.transports_count' has no cute function yet. Qt's "
        "'qsizetype "
        "QQmlWebChannel::transports_count(QQmlListProperty<QObject> "
        "*prop)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")
