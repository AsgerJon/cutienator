"""
QRestAccessManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qrestaccessmanager.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QIODevice, QJsonDocument, QMetaObject
  from ..QtCore import QVariant
  from . import QHttpMultiPart, QNetworkAccessManager, QNetworkReply
  from . import QNetworkRequest, QRestAccessManagerPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QHttpMultiPart = WAIT['QHttpMultiPart']
  QIODevice = WAIT['QIODevice']
  QJsonDocument = WAIT['QJsonDocument']
  QNetworkAccessManager = WAIT['QNetworkAccessManager']
  QNetworkRequest = WAIT['QNetworkRequest']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRestAccessManager(QObject):
  """
  The cute side of Qt's QRestAccessManager: a plain Python object standing in
  front of one C++ QRestAccessManager.

  It is built on the cute 'QObject', as Qt's QRestAccessManager is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRestAccessManager that has a ritual and that Python
  can call so far, 11 names in all: 'metaObject', 'tr',
  'networkAccessManager', 'deleteResource', 'head', 'get', 'post', 'put',
  'patch', 'sendCustomRequest', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QRestAccessManager::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QRestAccessManager::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QRestAccessManager::~QRestAccessManager()': the destructor: Python
    never removes a C++ QRestAccessManager.
  - Qt's 'QNetworkReply *QRestAccessManager::deleteResourceNoDataImpl(const
    QNetworkRequest &request, const QObject *context,
    QtPrivate::QSlotObjectBase *slot)': names 'QtPrivate::QSlotObjectBase',
    which has no cute class yet.
  - Qt's 'QNetworkReply *QRestAccessManager::headNoDataImpl(const
    QNetworkRequest &request, const QObject *context,
    QtPrivate::QSlotObjectBase *slot)': names 'QtPrivate::QSlotObjectBase',
    which has no cute class yet.
  - Qt's 'QNetworkReply *QRestAccessManager::getNoDataImpl(const
    QNetworkRequest &request, const QObject *context,
    QtPrivate::QSlotObjectBase *slot)': names 'QtPrivate::QSlotObjectBase',
    which has no cute class yet.
  - Qt's 'QNetworkReply *QRestAccessManager::getWithDataImpl(const
    QNetworkRequest &request, const QByteArray &data, const QObject *context,
    QtPrivate::QSlotObjectBase *slot)': names 'QtPrivate::QSlotObjectBase',
    which has no cute class yet.
  - Qt's 'QNetworkReply *QRestAccessManager::getWithDataImpl(const
    QNetworkRequest &request, const QJsonDocument &data, const QObject
    *context, QtPrivate::QSlotObjectBase *slot)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.
  - Qt's 'QNetworkReply *QRestAccessManager::getWithDataImpl(const
    QNetworkRequest &request, QIODevice *data, const QObject *context,
    QtPrivate::QSlotObjectBase *slot)': names 'QtPrivate::QSlotObjectBase',
    which has no cute class yet.
  - Qt's 'QNetworkReply *QRestAccessManager::postWithDataImpl(const
    QNetworkRequest &request, const QJsonDocument &data, const QObject
    *context, QtPrivate::QSlotObjectBase *slot)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.
  - Qt's 'QNetworkReply *QRestAccessManager::postWithDataImpl(const
    QNetworkRequest &request, const QVariantMap &data, const QObject
    *context, QtPrivate::QSlotObjectBase *slot)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.
  - Qt's 'QNetworkReply *QRestAccessManager::postWithDataImpl(const
    QNetworkRequest &request, const QByteArray &data, const QObject *context,
    QtPrivate::QSlotObjectBase *slot)': names 'QtPrivate::QSlotObjectBase',
    which has no cute class yet.
  - Qt's 'QNetworkReply *QRestAccessManager::postWithDataImpl(const
    QNetworkRequest &request, QHttpMultiPart *data, const QObject *context,
    QtPrivate::QSlotObjectBase *slot)': names 'QtPrivate::QSlotObjectBase',
    which has no cute class yet.
  - Qt's 'QNetworkReply *QRestAccessManager::postWithDataImpl(const
    QNetworkRequest &request, QIODevice *data, const QObject *context,
    QtPrivate::QSlotObjectBase *slot)': names 'QtPrivate::QSlotObjectBase',
    which has no cute class yet.
  - Qt's 'QNetworkReply *QRestAccessManager::putWithDataImpl(const
    QNetworkRequest &request, const QJsonDocument &data, const QObject
    *context, QtPrivate::QSlotObjectBase *slot)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.
  - Qt's 'QNetworkReply *QRestAccessManager::putWithDataImpl(const
    QNetworkRequest &request, const QVariantMap &data, const QObject
    *context, QtPrivate::QSlotObjectBase *slot)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.
  - Qt's 'QNetworkReply *QRestAccessManager::putWithDataImpl(const
    QNetworkRequest &request, const QByteArray &data, const QObject *context,
    QtPrivate::QSlotObjectBase *slot)': names 'QtPrivate::QSlotObjectBase',
    which has no cute class yet.
  - Qt's 'QNetworkReply *QRestAccessManager::putWithDataImpl(const
    QNetworkRequest &request, QHttpMultiPart *data, const QObject *context,
    QtPrivate::QSlotObjectBase *slot)': names 'QtPrivate::QSlotObjectBase',
    which has no cute class yet.
  - Qt's 'QNetworkReply *QRestAccessManager::putWithDataImpl(const
    QNetworkRequest &request, QIODevice *data, const QObject *context,
    QtPrivate::QSlotObjectBase *slot)': names 'QtPrivate::QSlotObjectBase',
    which has no cute class yet.
  - Qt's 'QNetworkReply *QRestAccessManager::patchWithDataImpl(const
    QNetworkRequest &request, const QJsonDocument &data, const QObject
    *context, QtPrivate::QSlotObjectBase *slot)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.
  - Qt's 'QNetworkReply *QRestAccessManager::patchWithDataImpl(const
    QNetworkRequest &request, const QVariantMap &data, const QObject
    *context, QtPrivate::QSlotObjectBase *slot)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.
  - Qt's 'QNetworkReply *QRestAccessManager::patchWithDataImpl(const
    QNetworkRequest &request, const QByteArray &data, const QObject *context,
    QtPrivate::QSlotObjectBase *slot)': names 'QtPrivate::QSlotObjectBase',
    which has no cute class yet.
  - Qt's 'QNetworkReply *QRestAccessManager::patchWithDataImpl(const
    QNetworkRequest &request, QIODevice *data, const QObject *context,
    QtPrivate::QSlotObjectBase *slot)': names 'QtPrivate::QSlotObjectBase',
    which has no cute class yet.
  - Qt's 'QNetworkReply *QRestAccessManager::customWithDataImpl(const
    QNetworkRequest &request, const QByteArray &method, const QByteArray
    &data, const QObject *context, QtPrivate::QSlotObjectBase *slot)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.
  - Qt's 'QNetworkReply *QRestAccessManager::customWithDataImpl(const
    QNetworkRequest &request, const QByteArray &method, QIODevice *data,
    const QObject *context, QtPrivate::QSlotObjectBase *slot)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.
  - Qt's 'QNetworkReply *QRestAccessManager::customWithDataImpl(const
    QNetworkRequest &request, const QByteArray &method, QHttpMultiPart *data,
    const QObject *context, QtPrivate::QSlotObjectBase *slot)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.
  - Qt's 'const QRestAccessManagerPrivate *QRestAccessManager::d_func()
    const': takes in Python what 'QRestAccessManagerPrivate
    *QRestAccessManager::d_func()' takes.

  What has no ritual
  ------------------

  27 of the 82 functions Qt declares: 23 a template; 2 not a gap; 2
  forbidden.

  What to expect
  --------------

  - The C++ QRestAccessManager is created at the first use, not by
    'QRestAccessManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRestAccessManager.
  - Qt tells when it has removed the C++ QRestAccessManager. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QRestAccessManager that has no cute function yet,
    'customWithDataImpl', 'deleteResourceNoDataImpl', 'getNoDataImpl',
    'getWithDataImpl', 'headNoDataImpl', 'patchWithDataImpl',
    'postWithDataImpl', 'putWithDataImpl', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QRestAccessManager::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qrestaccessmanager.html#tr

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
    #  QString QRestAccessManager::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QRestAccessManager2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRestAccessManager'

  #  A C++ QRestAccessManager Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRestAccessManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QRestAccessManager::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrestaccessmanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QRestAccessManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QRestAccessManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def networkAccessManager(self) -> Optional[QNetworkAccessManager]:
    """
    Calls Qt's 'QNetworkAccessManager
    *QRestAccessManager::networkAccessManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrestaccessmanager.html#networkAccessManager

    Returns
    -------

    Optional[QNetworkAccessManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkAccessManager *QRestAccessManager::networkAccessManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QRestAccessManager20networkAccessManagerEv',
    )
    from . import QNetworkAccessManager
    return QNetworkAccessManager._cuteAt(address)

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

  @overload(QNetworkAccessManager)
  @overload(NoneType)
  @overload(QNetworkAccessManager, QObject)
  @overload(QNetworkAccessManager, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      manager: Optional[QNetworkAccessManager],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QRestAccessManager::QRestAccessManager(QNetworkAccessManager *manager,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrestaccessmanager.html#QRestAccessManager

    Parameters
    ----------

    manager : Optional[QNetworkAccessManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QRestAccessManager::QRestAccessManager(QNetworkAccessManager *manager,
    #      QObject *parent)
    self._noteCreation(QRestAccessManager, lambda: Rituals.call(
        'ritual_ZN18QRestAccessManagerC1EP21QNetworkAccessManagerP7QObject',
        self._addressOf(manager), self._addressOf(parent, 'QObject'),
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

  @overload(QNetworkRequest)
  def deleteResource(
      self,
      request: QNetworkRequest,
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::deleteResource(const
    QNetworkRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrestaccessmanager.html#deleteResource

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::deleteResource(const
    #      QNetworkRequest &request)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager14deleteResourceERK15QNetworkRequest',
        self._valueOf(request),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest)
  def head(self, request: QNetworkRequest) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::head(const QNetworkRequest
    &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qrestaccessmanager.html#head

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::head(const QNetworkRequest
    #      &request)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager4headERK15QNetworkRequest',
        self._valueOf(request),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest)
  def get(self, request: QNetworkRequest) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::get(const QNetworkRequest
    &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qrestaccessmanager.html#get

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::get(const QNetworkRequest &request)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager3getERK15QNetworkRequest',
        self._valueOf(request),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QByteArray)
  def get(
      self,
      request: QNetworkRequest,
      data: QByteArray,
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::get(const QNetworkRequest
    &request, const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qrestaccessmanager.html#get

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::get(const QNetworkRequest &request,
    #      const QByteArray &data)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager3getERK15QNetworkRequestRK10QByteArra'
        'y',
        self._valueOf(request), self._valueOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QJsonDocument)
  def get(
      self,
      request: QNetworkRequest,
      data: QJsonDocument,
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::get(const QNetworkRequest
    &request, const QJsonDocument &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qrestaccessmanager.html#get

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : QJsonDocument
      Passed on as a value: Qt reads the C++ QJsonDocument, which stays
      Python's own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::get(const QNetworkRequest &request,
    #      const QJsonDocument &data)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager3getERK15QNetworkRequestRK13QJsonDocu'
        'ment',
        self._valueOf(request), self._valueOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QIODevice)
  @overload(QNetworkRequest, NoneType)
  def get(
      self,
      request: QNetworkRequest,
      data: Optional[QIODevice],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::get(const QNetworkRequest
    &request, QIODevice *data)'.

    Qt's own words: https://doc.qt.io/qt-6/qrestaccessmanager.html#get

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::get(const QNetworkRequest &request,
    #      QIODevice *data)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager3getERK15QNetworkRequestP9QIODevice',
        self._valueOf(request), self._addressOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QJsonDocument)
  def post(
      self,
      request: QNetworkRequest,
      data: QJsonDocument,
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::post(const QNetworkRequest
    &request, const QJsonDocument &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qrestaccessmanager.html#post

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : QJsonDocument
      Passed on as a value: Qt reads the C++ QJsonDocument, which stays
      Python's own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::post(const QNetworkRequest
    #      &request, const QJsonDocument &data)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager4postERK15QNetworkRequestRK13QJsonDoc'
        'ument',
        self._valueOf(request), self._valueOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QMap[str, QVariant])
  def post(
      self,
      request: QNetworkRequest,
      data: QMap[str, QVariant],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::post(const QNetworkRequest
    &request, const QVariantMap &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qrestaccessmanager.html#post

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::post(const QNetworkRequest
    #      &request, const QVariantMap &data)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager4postERK15QNetworkRequestRK4QMapI7QSt'
        'ring8QVariantE',
        self._valueOf(request), self._valueOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QByteArray)
  def post(
      self,
      request: QNetworkRequest,
      data: QByteArray,
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::post(const QNetworkRequest
    &request, const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qrestaccessmanager.html#post

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::post(const QNetworkRequest
    #      &request, const QByteArray &data)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager4postERK15QNetworkRequestRK10QByteArr'
        'ay',
        self._valueOf(request), self._valueOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QHttpMultiPart)
  @overload(QNetworkRequest, NoneType)
  def post(
      self,
      request: QNetworkRequest,
      data: Optional[QHttpMultiPart],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::post(const QNetworkRequest
    &request, QHttpMultiPart *data)'.

    Qt's own words: https://doc.qt.io/qt-6/qrestaccessmanager.html#post

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : Optional[QHttpMultiPart]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::post(const QNetworkRequest
    #      &request, QHttpMultiPart *data)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager4postERK15QNetworkRequestP14QHttpMult'
        'iPart',
        self._valueOf(request), self._addressOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QIODevice)
  def post(
      self,
      request: QNetworkRequest,
      data: Optional[QIODevice],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::post(const QNetworkRequest
    &request, QIODevice *data)'.

    Qt's own words: https://doc.qt.io/qt-6/qrestaccessmanager.html#post

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::post(const QNetworkRequest
    #      &request, QIODevice *data)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager4postERK15QNetworkRequestP9QIODevice',
        self._valueOf(request), self._addressOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QJsonDocument)
  def put(
      self,
      request: QNetworkRequest,
      data: QJsonDocument,
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::put(const QNetworkRequest
    &request, const QJsonDocument &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qrestaccessmanager.html#put

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : QJsonDocument
      Passed on as a value: Qt reads the C++ QJsonDocument, which stays
      Python's own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::put(const QNetworkRequest &request,
    #      const QJsonDocument &data)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager3putERK15QNetworkRequestRK13QJsonDocu'
        'ment',
        self._valueOf(request), self._valueOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QMap[str, QVariant])
  def put(
      self,
      request: QNetworkRequest,
      data: QMap[str, QVariant],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::put(const QNetworkRequest
    &request, const QVariantMap &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qrestaccessmanager.html#put

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::put(const QNetworkRequest &request,
    #      const QVariantMap &data)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager3putERK15QNetworkRequestRK4QMapI7QStr'
        'ing8QVariantE',
        self._valueOf(request), self._valueOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QByteArray)
  def put(
      self,
      request: QNetworkRequest,
      data: QByteArray,
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::put(const QNetworkRequest
    &request, const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qrestaccessmanager.html#put

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::put(const QNetworkRequest &request,
    #      const QByteArray &data)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager3putERK15QNetworkRequestRK10QByteArra'
        'y',
        self._valueOf(request), self._valueOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QHttpMultiPart)
  @overload(QNetworkRequest, NoneType)
  def put(
      self,
      request: QNetworkRequest,
      data: Optional[QHttpMultiPart],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::put(const QNetworkRequest
    &request, QHttpMultiPart *data)'.

    Qt's own words: https://doc.qt.io/qt-6/qrestaccessmanager.html#put

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : Optional[QHttpMultiPart]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::put(const QNetworkRequest &request,
    #      QHttpMultiPart *data)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager3putERK15QNetworkRequestP14QHttpMulti'
        'Part',
        self._valueOf(request), self._addressOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QIODevice)
  def put(
      self,
      request: QNetworkRequest,
      data: Optional[QIODevice],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::put(const QNetworkRequest
    &request, QIODevice *data)'.

    Qt's own words: https://doc.qt.io/qt-6/qrestaccessmanager.html#put

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::put(const QNetworkRequest &request,
    #      QIODevice *data)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager3putERK15QNetworkRequestP9QIODevice',
        self._valueOf(request), self._addressOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QJsonDocument)
  def patch(
      self,
      request: QNetworkRequest,
      data: QJsonDocument,
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::patch(const
    QNetworkRequest &request, const QJsonDocument &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qrestaccessmanager.html#patch

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : QJsonDocument
      Passed on as a value: Qt reads the C++ QJsonDocument, which stays
      Python's own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::patch(const QNetworkRequest
    #      &request, const QJsonDocument &data)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager5patchERK15QNetworkRequestRK13QJsonDo'
        'cument',
        self._valueOf(request), self._valueOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QMap[str, QVariant])
  def patch(
      self,
      request: QNetworkRequest,
      data: QMap[str, QVariant],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::patch(const
    QNetworkRequest &request, const QVariantMap &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qrestaccessmanager.html#patch

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::patch(const QNetworkRequest
    #      &request, const QVariantMap &data)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager5patchERK15QNetworkRequestRK4QMapI7QS'
        'tring8QVariantE',
        self._valueOf(request), self._valueOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QByteArray)
  def patch(
      self,
      request: QNetworkRequest,
      data: QByteArray,
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::patch(const
    QNetworkRequest &request, const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qrestaccessmanager.html#patch

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::patch(const QNetworkRequest
    #      &request, const QByteArray &data)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager5patchERK15QNetworkRequestRK10QByteAr'
        'ray',
        self._valueOf(request), self._valueOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QIODevice)
  @overload(QNetworkRequest, NoneType)
  def patch(
      self,
      request: QNetworkRequest,
      data: Optional[QIODevice],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::patch(const
    QNetworkRequest &request, QIODevice *data)'.

    Qt's own words: https://doc.qt.io/qt-6/qrestaccessmanager.html#patch

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::patch(const QNetworkRequest
    #      &request, QIODevice *data)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager5patchERK15QNetworkRequestP9QIODevice',
        self._valueOf(request), self._addressOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QByteArray, QByteArray)
  def sendCustomRequest(
      self,
      request: QNetworkRequest,
      method: QByteArray,
      data: QByteArray,
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::sendCustomRequest(const
    QNetworkRequest &request, const QByteArray &method, const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrestaccessmanager.html#sendCustomRequest

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    method : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::sendCustomRequest(const
    #      QNetworkRequest &request, const QByteArray &method, const
    #      QByteArray &data)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager17sendCustomRequestERK15QNetworkReque'
        'stRK10QByteArrayS5_',
        self._valueOf(request), self._valueOf(method), self._valueOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QByteArray, QIODevice)
  @overload(QNetworkRequest, QByteArray, NoneType)
  def sendCustomRequest(
      self,
      request: QNetworkRequest,
      method: QByteArray,
      data: Optional[QIODevice],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::sendCustomRequest(const
    QNetworkRequest &request, const QByteArray &method, QIODevice *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrestaccessmanager.html#sendCustomRequest

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    method : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    data : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::sendCustomRequest(const
    #      QNetworkRequest &request, const QByteArray &method, QIODevice
    #      *data)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager17sendCustomRequestERK15QNetworkReque'
        'stRK10QByteArrayP9QIODevice',
        self._valueOf(request), self._valueOf(method), self._addressOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QByteArray, QHttpMultiPart)
  def sendCustomRequest(
      self,
      request: QNetworkRequest,
      method: QByteArray,
      data: Optional[QHttpMultiPart],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QRestAccessManager::sendCustomRequest(const
    QNetworkRequest &request, const QByteArray &method, QHttpMultiPart
    *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrestaccessmanager.html#sendCustomRequest

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    method : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    data : Optional[QHttpMultiPart]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QRestAccessManager::sendCustomRequest(const
    #      QNetworkRequest &request, const QByteArray &method, QHttpMultiPart
    #      *data)
    address = self.uglySide.call(
        'ritual_ZN18QRestAccessManager17sendCustomRequestERK15QNetworkReque'
        'stRK10QByteArrayP14QHttpMultiPart',
        self._valueOf(request), self._valueOf(method), self._addressOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  def d_func(self) -> Optional[QRestAccessManagerPrivate]:
    """
    Calls Qt's 'QRestAccessManagerPrivate *QRestAccessManager::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qrestaccessmanager.html#d_func

    Returns
    -------

    Optional[QRestAccessManagerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRestAccessManagerPrivate *QRestAccessManager::d_func()
    address = self.uglySide.call('ritual_ZN18QRestAccessManager6d_funcEv')
    from . import QRestAccessManagerPrivate
    return QRestAccessManagerPrivate._cuteAt(address)

  @staticmethod
  def customWithDataImpl(*__, **_) -> Never:
    """
    - Qt's 'QNetworkReply *QRestAccessManager::customWithDataImpl(const
      QNetworkRequest &request, const QByteArray &method, const QByteArray
      &data, const QObject *context, QtPrivate::QSlotObjectBase *slot)':
      names 'QtPrivate::QSlotObjectBase', which has no cute class yet.
    - Qt's 'QNetworkReply *QRestAccessManager::customWithDataImpl(const
      QNetworkRequest &request, const QByteArray &method, QIODevice *data,
      const QObject *context, QtPrivate::QSlotObjectBase *slot)': names
      'QtPrivate::QSlotObjectBase', which has no cute class yet.
    - Qt's 'QNetworkReply *QRestAccessManager::customWithDataImpl(const
      QNetworkRequest &request, const QByteArray &method, QHttpMultiPart
      *data, const QObject *context, QtPrivate::QSlotObjectBase *slot)':
      names 'QtPrivate::QSlotObjectBase', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRestAccessManager.customWithDataImpl' has no cute function yet. "
        "Qt's 'QNetworkReply *QRestAccessManager::customWithDataImpl(const "
        "QNetworkRequest &request, const QByteArray &method, const "
        "QByteArray &data, const QObject *context, "
        "QtPrivate::QSlotObjectBase *slot)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet. Qt's "
        "'QNetworkReply *QRestAccessManager::customWithDataImpl(const "
        "QNetworkRequest &request, const QByteArray &method, QIODevice "
        "*data, const QObject *context, QtPrivate::QSlotObjectBase *slot)': "
        "names 'QtPrivate::QSlotObjectBase', which has no cute class yet. "
        "Qt's 'QNetworkReply *QRestAccessManager::customWithDataImpl(const "
        "QNetworkRequest &request, const QByteArray &method, QHttpMultiPart "
        "*data, const QObject *context, QtPrivate::QSlotObjectBase *slot)': "
        "names 'QtPrivate::QSlotObjectBase', which has no cute class yet.")

  @staticmethod
  def deleteResourceNoDataImpl(*__, **_) -> Never:
    """
    Qt's 'QNetworkReply *QRestAccessManager::deleteResourceNoDataImpl(const
    QNetworkRequest &request, const QObject *context,
    QtPrivate::QSlotObjectBase *slot)': names 'QtPrivate::QSlotObjectBase',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRestAccessManager.deleteResourceNoDataImpl' has no cute function "
        "yet. Qt's 'QNetworkReply "
        "*QRestAccessManager::deleteResourceNoDataImpl(const "
        "QNetworkRequest &request, const QObject *context, "
        "QtPrivate::QSlotObjectBase *slot)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet.")

  @staticmethod
  def getNoDataImpl(*__, **_) -> Never:
    """
    Qt's 'QNetworkReply *QRestAccessManager::getNoDataImpl(const
    QNetworkRequest &request, const QObject *context,
    QtPrivate::QSlotObjectBase *slot)': names 'QtPrivate::QSlotObjectBase',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRestAccessManager.getNoDataImpl' has no cute function yet. Qt's "
        "'QNetworkReply *QRestAccessManager::getNoDataImpl(const "
        "QNetworkRequest &request, const QObject *context, "
        "QtPrivate::QSlotObjectBase *slot)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet.")

  @staticmethod
  def getWithDataImpl(*__, **_) -> Never:
    """
    - Qt's 'QNetworkReply *QRestAccessManager::getWithDataImpl(const
      QNetworkRequest &request, const QByteArray &data, const QObject
      *context, QtPrivate::QSlotObjectBase *slot)': names
      'QtPrivate::QSlotObjectBase', which has no cute class yet.
    - Qt's 'QNetworkReply *QRestAccessManager::getWithDataImpl(const
      QNetworkRequest &request, const QJsonDocument &data, const QObject
      *context, QtPrivate::QSlotObjectBase *slot)': names
      'QtPrivate::QSlotObjectBase', which has no cute class yet.
    - Qt's 'QNetworkReply *QRestAccessManager::getWithDataImpl(const
      QNetworkRequest &request, QIODevice *data, const QObject *context,
      QtPrivate::QSlotObjectBase *slot)': names 'QtPrivate::QSlotObjectBase',
      which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRestAccessManager.getWithDataImpl' has no cute function yet. "
        "Qt's 'QNetworkReply *QRestAccessManager::getWithDataImpl(const "
        "QNetworkRequest &request, const QByteArray &data, const QObject "
        "*context, QtPrivate::QSlotObjectBase *slot)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet. Qt's "
        "'QNetworkReply *QRestAccessManager::getWithDataImpl(const "
        "QNetworkRequest &request, const QJsonDocument &data, const QObject "
        "*context, QtPrivate::QSlotObjectBase *slot)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet. Qt's "
        "'QNetworkReply *QRestAccessManager::getWithDataImpl(const "
        "QNetworkRequest &request, QIODevice *data, const QObject *context, "
        "QtPrivate::QSlotObjectBase *slot)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet.")

  @staticmethod
  def headNoDataImpl(*__, **_) -> Never:
    """
    Qt's 'QNetworkReply *QRestAccessManager::headNoDataImpl(const
    QNetworkRequest &request, const QObject *context,
    QtPrivate::QSlotObjectBase *slot)': names 'QtPrivate::QSlotObjectBase',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRestAccessManager.headNoDataImpl' has no cute function yet. Qt's "
        "'QNetworkReply *QRestAccessManager::headNoDataImpl(const "
        "QNetworkRequest &request, const QObject *context, "
        "QtPrivate::QSlotObjectBase *slot)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet.")

  @staticmethod
  def patchWithDataImpl(*__, **_) -> Never:
    """
    - Qt's 'QNetworkReply *QRestAccessManager::patchWithDataImpl(const
      QNetworkRequest &request, const QJsonDocument &data, const QObject
      *context, QtPrivate::QSlotObjectBase *slot)': names
      'QtPrivate::QSlotObjectBase', which has no cute class yet.
    - Qt's 'QNetworkReply *QRestAccessManager::patchWithDataImpl(const
      QNetworkRequest &request, const QVariantMap &data, const QObject
      *context, QtPrivate::QSlotObjectBase *slot)': names
      'QtPrivate::QSlotObjectBase', which has no cute class yet.
    - Qt's 'QNetworkReply *QRestAccessManager::patchWithDataImpl(const
      QNetworkRequest &request, const QByteArray &data, const QObject
      *context, QtPrivate::QSlotObjectBase *slot)': names
      'QtPrivate::QSlotObjectBase', which has no cute class yet.
    - Qt's 'QNetworkReply *QRestAccessManager::patchWithDataImpl(const
      QNetworkRequest &request, QIODevice *data, const QObject *context,
      QtPrivate::QSlotObjectBase *slot)': names 'QtPrivate::QSlotObjectBase',
      which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRestAccessManager.patchWithDataImpl' has no cute function yet. "
        "Qt's 'QNetworkReply *QRestAccessManager::patchWithDataImpl(const "
        "QNetworkRequest &request, const QJsonDocument &data, const QObject "
        "*context, QtPrivate::QSlotObjectBase *slot)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet. Qt's "
        "'QNetworkReply *QRestAccessManager::patchWithDataImpl(const "
        "QNetworkRequest &request, const QVariantMap &data, const QObject "
        "*context, QtPrivate::QSlotObjectBase *slot)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet. Qt's "
        "'QNetworkReply *QRestAccessManager::patchWithDataImpl(const "
        "QNetworkRequest &request, const QByteArray &data, const QObject "
        "*context, QtPrivate::QSlotObjectBase *slot)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet. Qt's "
        "'QNetworkReply *QRestAccessManager::patchWithDataImpl(const "
        "QNetworkRequest &request, QIODevice *data, const QObject *context, "
        "QtPrivate::QSlotObjectBase *slot)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet.")

  @staticmethod
  def postWithDataImpl(*__, **_) -> Never:
    """
    - Qt's 'QNetworkReply *QRestAccessManager::postWithDataImpl(const
      QNetworkRequest &request, const QJsonDocument &data, const QObject
      *context, QtPrivate::QSlotObjectBase *slot)': names
      'QtPrivate::QSlotObjectBase', which has no cute class yet.
    - Qt's 'QNetworkReply *QRestAccessManager::postWithDataImpl(const
      QNetworkRequest &request, const QVariantMap &data, const QObject
      *context, QtPrivate::QSlotObjectBase *slot)': names
      'QtPrivate::QSlotObjectBase', which has no cute class yet.
    - Qt's 'QNetworkReply *QRestAccessManager::postWithDataImpl(const
      QNetworkRequest &request, const QByteArray &data, const QObject
      *context, QtPrivate::QSlotObjectBase *slot)': names
      'QtPrivate::QSlotObjectBase', which has no cute class yet.
    - Qt's 'QNetworkReply *QRestAccessManager::postWithDataImpl(const
      QNetworkRequest &request, QHttpMultiPart *data, const QObject *context,
      QtPrivate::QSlotObjectBase *slot)': names 'QtPrivate::QSlotObjectBase',
      which has no cute class yet.
    - Qt's 'QNetworkReply *QRestAccessManager::postWithDataImpl(const
      QNetworkRequest &request, QIODevice *data, const QObject *context,
      QtPrivate::QSlotObjectBase *slot)': names 'QtPrivate::QSlotObjectBase',
      which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRestAccessManager.postWithDataImpl' has no cute function yet. "
        "Qt's 'QNetworkReply *QRestAccessManager::postWithDataImpl(const "
        "QNetworkRequest &request, const QJsonDocument &data, const QObject "
        "*context, QtPrivate::QSlotObjectBase *slot)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet. Qt's "
        "'QNetworkReply *QRestAccessManager::postWithDataImpl(const "
        "QNetworkRequest &request, const QVariantMap &data, const QObject "
        "*context, QtPrivate::QSlotObjectBase *slot)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet. Qt's "
        "'QNetworkReply *QRestAccessManager::postWithDataImpl(const "
        "QNetworkRequest &request, const QByteArray &data, const QObject "
        "*context, QtPrivate::QSlotObjectBase *slot)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet. Qt's "
        "'QNetworkReply *QRestAccessManager::postWithDataImpl(const "
        "QNetworkRequest &request, QHttpMultiPart *data, const QObject "
        "*context, QtPrivate::QSlotObjectBase *slot)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet. Qt's "
        "'QNetworkReply *QRestAccessManager::postWithDataImpl(const "
        "QNetworkRequest &request, QIODevice *data, const QObject *context, "
        "QtPrivate::QSlotObjectBase *slot)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet.")

  @staticmethod
  def putWithDataImpl(*__, **_) -> Never:
    """
    - Qt's 'QNetworkReply *QRestAccessManager::putWithDataImpl(const
      QNetworkRequest &request, const QJsonDocument &data, const QObject
      *context, QtPrivate::QSlotObjectBase *slot)': names
      'QtPrivate::QSlotObjectBase', which has no cute class yet.
    - Qt's 'QNetworkReply *QRestAccessManager::putWithDataImpl(const
      QNetworkRequest &request, const QVariantMap &data, const QObject
      *context, QtPrivate::QSlotObjectBase *slot)': names
      'QtPrivate::QSlotObjectBase', which has no cute class yet.
    - Qt's 'QNetworkReply *QRestAccessManager::putWithDataImpl(const
      QNetworkRequest &request, const QByteArray &data, const QObject
      *context, QtPrivate::QSlotObjectBase *slot)': names
      'QtPrivate::QSlotObjectBase', which has no cute class yet.
    - Qt's 'QNetworkReply *QRestAccessManager::putWithDataImpl(const
      QNetworkRequest &request, QHttpMultiPart *data, const QObject *context,
      QtPrivate::QSlotObjectBase *slot)': names 'QtPrivate::QSlotObjectBase',
      which has no cute class yet.
    - Qt's 'QNetworkReply *QRestAccessManager::putWithDataImpl(const
      QNetworkRequest &request, QIODevice *data, const QObject *context,
      QtPrivate::QSlotObjectBase *slot)': names 'QtPrivate::QSlotObjectBase',
      which has no cute class yet.
    """
    raise NotImplementedError(
        "'QRestAccessManager.putWithDataImpl' has no cute function yet. "
        "Qt's 'QNetworkReply *QRestAccessManager::putWithDataImpl(const "
        "QNetworkRequest &request, const QJsonDocument &data, const QObject "
        "*context, QtPrivate::QSlotObjectBase *slot)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet. Qt's "
        "'QNetworkReply *QRestAccessManager::putWithDataImpl(const "
        "QNetworkRequest &request, const QVariantMap &data, const QObject "
        "*context, QtPrivate::QSlotObjectBase *slot)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet. Qt's "
        "'QNetworkReply *QRestAccessManager::putWithDataImpl(const "
        "QNetworkRequest &request, const QByteArray &data, const QObject "
        "*context, QtPrivate::QSlotObjectBase *slot)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet. Qt's "
        "'QNetworkReply *QRestAccessManager::putWithDataImpl(const "
        "QNetworkRequest &request, QHttpMultiPart *data, const QObject "
        "*context, QtPrivate::QSlotObjectBase *slot)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet. Qt's "
        "'QNetworkReply *QRestAccessManager::putWithDataImpl(const "
        "QNetworkRequest &request, QIODevice *data, const QObject *context, "
        "QtPrivate::QSlotObjectBase *slot)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet.")
