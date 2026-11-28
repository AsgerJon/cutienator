"""
QQmlApplicationEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qqmlapplicationengine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap, QObject, QStringList
from . import QQmlEngine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QUrl, QVariant
  from . import QQmlApplicationEnginePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlApplicationEngine(QQmlEngine):
  """
  The cute side of Qt's QQmlApplicationEngine: a plain Python object standing
  in front of one C++ QQmlApplicationEngine.

  It is built on the cute 'QQmlEngine', as Qt's QQmlApplicationEngine is
  built on Qt's QQmlEngine, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlApplicationEngine that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'tr', 'rootObjects',
  'load', 'loadFromModule', 'setInitialProperties', 'setExtraFileSelectors',
  'loadData', 'objectCreated', 'objectCreationFailed', 'd_func'. It can be
  made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlApplicationEngine::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlApplicationEngine::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlApplicationEngine::~QQmlApplicationEngine()': the destructor:
    Python never removes a C++ QQmlApplicationEngine.
  - Qt's 'const QQmlApplicationEnginePrivate *QQmlApplicationEngine::d_func()
    const': takes in Python what 'QQmlApplicationEnginePrivate
    *QQmlApplicationEngine::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 24 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQmlApplicationEngine is created at the first use, not by
    'QQmlApplicationEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlApplicationEngine.
  - Qt tells when it has removed the C++ QQmlApplicationEngine. Every call on
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
    Calls Qt's 'QString QQmlApplicationEngine::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlapplicationengine.html#tr

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
    #  QString QQmlApplicationEngine::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQmlApplicationEngine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlApplicationEngine'

  #  A C++ QQmlApplicationEngine Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlApplicationEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlApplicationEngine::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlApplicationEngine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlApplicationEngine10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rootObjects(self) -> QList[QObject]:
    """
    Calls Qt's 'QList<QObject *> QQmlApplicationEngine::rootObjects() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengine.html#rootObjects

    Returns
    -------

    QList[QObject]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QObject *> QQmlApplicationEngine::rootObjects() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlApplicationEngine11rootObjectsEv',
    )
    return QList[QObject]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMap[str, QVariant])
  def setInitialProperties(
      self,
      initialProperties: QMap[str, QVariant],
  ) -> None:
    """
    Calls Qt's 'void QQmlApplicationEngine::setInitialProperties(const
    QVariantMap &initialProperties)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengine.html#setInitialProperties

    Parameters
    ----------

    initialProperties : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QQmlApplicationEngine::setInitialProperties(const QVariantMap
    #      &initialProperties)
    self.uglySide.call(
        'ritual_ZN21QQmlApplicationEngine20setInitialPropertiesERK4QMapI7QS'
        'tring8QVariantE',
        self._valueOf(initialProperties),
    )

  @overload(QStringList)
  def setExtraFileSelectors(self, extraFileSelectors: QStringList) -> None:
    """
    Calls Qt's 'void QQmlApplicationEngine::setExtraFileSelectors(const
    QStringList &extraFileSelectors)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengine.html#setExtraFileSelectors

    Parameters
    ----------

    extraFileSelectors : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlApplicationEngine::setExtraFileSelectors(const QStringList
    #      &extraFileSelectors)
    self.uglySide.call(
        'ritual_ZN21QQmlApplicationEngine21setExtraFileSelectorsERK5QListI7'
        'QStringE',
        self._valueOf(extraFileSelectors),
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
    'QQmlApplicationEngine::QQmlApplicationEngine(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengine.html#QQmlApplicationEngine

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlApplicationEngine::QQmlApplicationEngine(QObject *parent)
    self._noteCreation(QQmlApplicationEngine, lambda: Rituals.call(
        'ritual_ZN21QQmlApplicationEngineC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QUrl)
  @overload(QUrl, QObject)
  @overload(QUrl, NoneType)
  def __init__(self, url: QUrl, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQmlApplicationEngine::QQmlApplicationEngine(const QUrl &url, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengine.html#QQmlApplicationEngine

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlApplicationEngine::QQmlApplicationEngine(const QUrl &url, QObject
    #      *parent)
    self._noteCreation(QQmlApplicationEngine, lambda: Rituals.call(
        'ritual_ZN21QQmlApplicationEngineC1ERK4QUrlP7QObject',
        self._valueOf(url), self._addressOf(parent, 'QObject'),
    ))

  @overload(str, str)
  @overload(str, str, QObject)
  @overload(str, str, NoneType)
  def __init__(
      self,
      uri: str,
      typeName: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlApplicationEngine::QQmlApplicationEngine(QAnyStringView uri,
    QAnyStringView typeName, QObject *parent)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengine.html#QQmlApplicationEngine

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlApplicationEngine::QQmlApplicationEngine(QAnyStringView uri,
    #      QAnyStringView typeName, QObject *parent)
    self._noteCreation(QQmlApplicationEngine, lambda: Rituals.call(
        'ritual_ZN21QQmlApplicationEngineC1E14QAnyStringViewS0_P7QObject',
        uri, typeName, self._addressOf(parent, 'QObject'),
    ))

  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(
      self,
      filePath: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlApplicationEngine::QQmlApplicationEngine(const QString &filePath,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengine.html#QQmlApplicationEngine

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlApplicationEngine::QQmlApplicationEngine(const QString &filePath,
    #      QObject *parent)
    self._noteCreation(QQmlApplicationEngine, lambda: Rituals.call(
        'ritual_ZN21QQmlApplicationEngineC1ERK7QStringP7QObject',
        filePath, self._addressOf(parent, 'QObject'),
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

  @overload(QUrl)
  def load(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QQmlApplicationEngine::load(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlapplicationengine.html#load

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQmlApplicationEngine::load(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN21QQmlApplicationEngine4loadERK4QUrl', self._valueOf(url),
    )

  @overload(str)
  def load(self, filePath: str) -> None:
    """
    Calls Qt's 'void QQmlApplicationEngine::load(const QString &filePath)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlapplicationengine.html#load

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlApplicationEngine::load(const QString &filePath)
    self.uglySide.call(
        'ritual_ZN21QQmlApplicationEngine4loadERK7QString', filePath,
    )

  @overload(str, str)
  def loadFromModule(self, uri: str, typeName: str) -> None:
    """
    Calls Qt's 'void QQmlApplicationEngine::loadFromModule(QAnyStringView
    uri, QAnyStringView typeName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengine.html#loadFromModule

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    typeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlApplicationEngine::loadFromModule(QAnyStringView uri,
    #      QAnyStringView typeName)
    self.uglySide.call(
        'ritual_ZN21QQmlApplicationEngine14loadFromModuleE14QAnyStringViewS'
        '0_',
        uri, typeName,
    )

  @overload(QByteArray)
  @overload(QByteArray, QUrl)
  def loadData(self, data: QByteArray, url: Optional[QUrl] = None) -> None:
    """
    Calls Qt's 'void QQmlApplicationEngine::loadData(const QByteArray &data,
    const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengine.html#loadData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    url : Optional[QUrl]
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
      May be left out, as in Qt: a new 'QUrl()' is then passed on.
    """
    #  void QQmlApplicationEngine::loadData(const QByteArray &data, const
    #      QUrl &url)
    if url is None:
      from ..QtCore import QUrl
      url = QUrl()
    self.uglySide.call(
        'ritual_ZN21QQmlApplicationEngine8loadDataERK10QByteArrayRK4QUrl',
        self._valueOf(data), self._valueOf(url),
    )

  @overload(QObject, QUrl)
  @overload(NoneType, QUrl)
  def objectCreated(self, object: Optional[QObject], url: QUrl) -> None:
    """
    Calls Qt's 'void QQmlApplicationEngine::objectCreated(QObject *object,
    const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengine.html#objectCreated

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQmlApplicationEngine::objectCreated(QObject *object, const QUrl
    #      &url)
    self.uglySide.call(
        'ritual_ZN21QQmlApplicationEngine13objectCreatedEP7QObjectRK4QUrl',
        self._addressOf(object, 'QObject'), self._valueOf(url),
    )

  @overload(QUrl)
  def objectCreationFailed(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QQmlApplicationEngine::objectCreationFailed(const QUrl
    &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengine.html#objectCreationFailed

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQmlApplicationEngine::objectCreationFailed(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN21QQmlApplicationEngine20objectCreationFailedERK4QUrl',
        self._valueOf(url),
    )

  def d_func(self) -> Optional[QQmlApplicationEnginePrivate]:
    """
    Calls Qt's 'QQmlApplicationEnginePrivate
    *QQmlApplicationEngine::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlapplicationengine.html#d_func

    Returns
    -------

    Optional[QQmlApplicationEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlApplicationEnginePrivate *QQmlApplicationEngine::d_func()
    address = self.uglySide.call('ritual_ZN21QQmlApplicationEngine6d_funcEv')
    from . import QQmlApplicationEnginePrivate
    return QQmlApplicationEnginePrivate._cuteAt(address)
