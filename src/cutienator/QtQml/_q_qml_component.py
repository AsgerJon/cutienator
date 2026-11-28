"""
QQmlComponent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qqmlcomponent.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap, QObject
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QUrl, QVariant
  from . import QQmlComponentAttached, QQmlComponentPrivate, QQmlContext
  from . import QQmlEngine, QQmlError, QQmlV4Function
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QQmlContext = WAIT['QQmlContext']
  QQmlEngine = WAIT['QQmlEngine']
  QQmlV4Function = WAIT['QQmlV4Function']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlComponent(QObject):
  """
  The cute side of Qt's QQmlComponent: a plain Python object standing in
  front of one C++ QQmlComponent.

  It is built on the cute 'QObject', as Qt's QQmlComponent is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlComponent that has a ritual and that Python can
  call so far, 28 names in all: 'metaObject', 'tr', 'd_func', 'status',
  'isNull', 'isReady', 'isError', 'isLoading', 'isBound', 'errors',
  'errorString', 'progress', 'url', 'create', 'createWithInitialProperties',
  'setInitialProperties', 'beginCreate', 'completeCreate', 'creationContext',
  'engine', 'qmlAttachedProperties', 'loadUrl', 'loadFromModule', 'setData',
  'statusChanged', 'progressChanged', 'createObject', 'incubateObject'. It
  can be made from Python, in 9 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlComponent::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQmlComponent::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QQmlComponentPrivate *QQmlComponent::d_func() const': takes
    in Python what 'QQmlComponentPrivate *QQmlComponent::d_func()' takes.
  - Qt's 'QQmlComponent::~QQmlComponent()': the destructor: Python never
    removes a C++ QQmlComponent.
  - Qt's 'void QQmlComponent::create(QQmlIncubator &a0, QQmlContext *context,
    QQmlContext *forContext)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QQmlComponent::QQmlComponent(QQmlComponentPrivate &dd, QObject
    *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 49 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQmlComponent is created at the first use, not by
    'QQmlComponent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlComponent.
  - Qt tells when it has removed the C++ QQmlComponent. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQmlComponent, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class CompilationMode(CuteNum):
    """
    The enum 'QQmlComponent::CompilationMode' of Qt, with the 2 names Qt
    gives in it.
    """

    PreferSynchronous = Kee[int](0)
    Asynchronous = Kee[int](1)

  class Status(CuteNum):
    """
    The enum 'QQmlComponent::Status' of Qt, with the 4 names Qt gives in it.
    """

    Null = Kee[int](0)
    Ready = Kee[int](1)
    Loading = Kee[int](2)
    Error = Kee[int](3)

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
    Calls Qt's 'QString QQmlComponent::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#tr

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
    #  QString QQmlComponent::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QQmlComponent2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      a0: Optional[QObject],
  ) -> Optional[QQmlComponentAttached]:
    """
    Calls Qt's 'QQmlComponentAttached
    *QQmlComponent::qmlAttachedProperties(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponent.html#qmlAttachedProperties

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlComponentAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponentAttached *QQmlComponent::qmlAttachedProperties(QObject
    #      *a0)
    address = Rituals.call(
        'ritual_ZN13QQmlComponent21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(a0, 'QObject'),
    )
    from . import QQmlComponentAttached
    return QQmlComponentAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlComponent'

  #  A C++ QQmlComponent Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlComponent'

  #  The functions Qt calls itself that QQmlComponent is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'create': (
          ('_ZN13QQmlComponent6createEP11QQmlContext',
           ('address', 'address', 'QtCore:QObject'),
           (
               ('address', 'address', 'QtQml:QQmlContext'),
           )),
      ),
      'beginCreate': (
          ('_ZN13QQmlComponent11beginCreateEP11QQmlContext',
           ('address', 'address', 'QtCore:QObject'),
           (
               ('address', 'address', 'QtQml:QQmlContext'),
           )),
      ),
      'completeCreate': (
          ('_ZN13QQmlComponent14completeCreateEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlComponent::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlComponent::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QQmlComponent10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def status(self) -> Status:
    """
    Calls Qt's 'Status QQmlComponent::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QQmlComponent::status() const
    return QQmlComponent.Status(self.uglySide.call(
        'ritual_ZNK13QQmlComponent6statusEv',
    ))

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QQmlComponent::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#isNull
    """
    #  bool QQmlComponent::isNull() const
    return self.uglySide.call('ritual_ZNK13QQmlComponent6isNullEv')

  def isReady(self) -> bool:
    """
    Calls Qt's 'bool QQmlComponent::isReady() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#isReady
    """
    #  bool QQmlComponent::isReady() const
    return self.uglySide.call('ritual_ZNK13QQmlComponent7isReadyEv')

  def isError(self) -> bool:
    """
    Calls Qt's 'bool QQmlComponent::isError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#isError
    """
    #  bool QQmlComponent::isError() const
    return self.uglySide.call('ritual_ZNK13QQmlComponent7isErrorEv')

  def isLoading(self) -> bool:
    """
    Calls Qt's 'bool QQmlComponent::isLoading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#isLoading
    """
    #  bool QQmlComponent::isLoading() const
    return self.uglySide.call('ritual_ZNK13QQmlComponent9isLoadingEv')

  def isBound(self) -> bool:
    """
    Calls Qt's 'bool QQmlComponent::isBound() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#isBound
    """
    #  bool QQmlComponent::isBound() const
    return self.uglySide.call('ritual_ZNK13QQmlComponent7isBoundEv')

  def errors(self) -> QList[QQmlError]:
    """
    Calls Qt's 'QList<QQmlError> QQmlComponent::errors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#errors

    Returns
    -------

    QList[QQmlError]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlError> QQmlComponent::errors() const
    address = self.uglySide.call('ritual_ZNK13QQmlComponent6errorsEv')
    from . import QQmlError
    return QList[QQmlError]._cuteOwning(address)

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QQmlComponent::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlComponent::errorString() const
    return self.uglySide.call('ritual_ZNK13QQmlComponent11errorStringEv')

  def progress(self) -> float:
    """
    Calls Qt's 'qreal QQmlComponent::progress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#progress
    """
    #  qreal QQmlComponent::progress() const
    return self.uglySide.call('ritual_ZNK13QQmlComponent8progressEv')

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlComponent::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlComponent::url() const
    address = self.uglySide.call('ritual_ZNK13QQmlComponent3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def creationContext(self) -> Optional[QQmlContext]:
    """
    Calls Qt's 'QQmlContext *QQmlComponent::creationContext() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#creationContext

    Returns
    -------

    Optional[QQmlContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlContext *QQmlComponent::creationContext() const
    address = self.uglySide.call(
        'ritual_ZNK13QQmlComponent15creationContextEv',
    )
    from . import QQmlContext
    return QQmlContext._cuteAt(address)

  def engine(self) -> Optional[QQmlEngine]:
    """
    Calls Qt's 'QQmlEngine *QQmlComponent::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#engine

    Returns
    -------

    Optional[QQmlEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlEngine *QQmlComponent::engine() const
    address = self.uglySide.call('ritual_ZNK13QQmlComponent6engineEv')
    from . import QQmlEngine
    return QQmlEngine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject, QMap[str, QVariant])
  @overload(NoneType, QMap[str, QVariant])
  def setInitialProperties(
      self,
      component: Optional[QObject],
      properties: QMap[str, QVariant],
  ) -> None:
    """
    Calls Qt's 'void QQmlComponent::setInitialProperties(QObject *component,
    const QVariantMap &properties)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponent.html#setInitialProperties

    Parameters
    ----------

    component : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    properties : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QQmlComponent::setInitialProperties(QObject *component, const
    #      QVariantMap &properties)
    self.uglySide.call(
        'ritual_ZN13QQmlComponent20setInitialPropertiesEP7QObjectRK4QMapI7Q'
        'String8QVariantE',
        self._addressOf(component, 'QObject'), self._valueOf(properties),
    )

  @overload(QByteArray, QUrl)
  def setData(self, data: QByteArray, baseUrl: QUrl) -> None:
    """
    Calls Qt's 'void QQmlComponent::setData(const QByteArray &data, const
    QUrl &baseUrl)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#setData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    baseUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQmlComponent::setData(const QByteArray &data, const QUrl
    #      &baseUrl)
    self.uglySide.call(
        'ritual_ZN13QQmlComponent7setDataERK10QByteArrayRK4QUrl',
        self._valueOf(data), self._valueOf(baseUrl),
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

  @overload(QQmlEngine)
  @overload(QQmlEngine, QObject)
  @overload(QQmlEngine, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      a0: Optional[QQmlEngine],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlComponent::QQmlComponent(QQmlEngine
    *a0, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#QQmlComponent

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlComponent::QQmlComponent(QQmlEngine *a0, QObject *parent)
    self._noteCreation(QQmlComponent, lambda: Rituals.call(
        'ritual_ZN13QQmlComponentC1EP10QQmlEngineP7QObject',
        self._addressOf(a0), self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QQmlComponent::QQmlComponent(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#QQmlComponent

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlComponent::QQmlComponent(QObject *parent)
    self._noteCreation(QQmlComponent, lambda: Rituals.call(
        'ritual_ZN13QQmlComponentC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QQmlEngine, str)
  @overload(NoneType, str)
  @overload(QQmlEngine, str, QObject)
  @overload(QQmlEngine, str, NoneType)
  @overload(NoneType, str, QObject)
  @overload(NoneType, str, NoneType)
  def __init__(
      self,
      a0: Optional[QQmlEngine],
      fileName: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlComponent::QQmlComponent(QQmlEngine
    *a0, const QString &fileName, QObject *parent)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#QQmlComponent

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlComponent::QQmlComponent(QQmlEngine *a0, const QString &fileName,
    #      QObject *parent)
    self._noteCreation(QQmlComponent, lambda: Rituals.call(
        'ritual_ZN13QQmlComponentC1EP10QQmlEngineRK7QStringP7QObject',
        self._addressOf(a0), fileName, self._addressOf(parent, 'QObject'),
    ))

  @overload(QQmlEngine, str, CompilationMode)
  @overload(NoneType, str, CompilationMode)
  @overload(QQmlEngine, str, CompilationMode, QObject)
  @overload(QQmlEngine, str, CompilationMode, NoneType)
  @overload(NoneType, str, CompilationMode, QObject)
  @overload(NoneType, str, CompilationMode, NoneType)
  def __init__(
      self,
      a0: Optional[QQmlEngine],
      fileName: str,
      mode: CompilationMode,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlComponent::QQmlComponent(QQmlEngine
    *a0, const QString &fileName, CompilationMode mode, QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#QQmlComponent

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    mode : CompilationMode
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlComponent::QQmlComponent(QQmlEngine *a0, const QString &fileName,
    #      CompilationMode mode, QObject *parent)
    self._noteCreation(QQmlComponent, lambda: Rituals.call(
        'ritual_ZN13QQmlComponentC1EP10QQmlEngineRK7QStringNS_15Compilation'
        'ModeEP7QObject',
        self._addressOf(a0), fileName, mode.value, self._addressOf(parent,
        'QObject'),
    ))

  @overload(QQmlEngine, QUrl)
  @overload(NoneType, QUrl)
  @overload(QQmlEngine, QUrl, QObject)
  @overload(QQmlEngine, QUrl, NoneType)
  @overload(NoneType, QUrl, QObject)
  @overload(NoneType, QUrl, NoneType)
  def __init__(
      self,
      a0: Optional[QQmlEngine],
      url: QUrl,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlComponent::QQmlComponent(QQmlEngine
    *a0, const QUrl &url, QObject *parent)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#QQmlComponent

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlComponent::QQmlComponent(QQmlEngine *a0, const QUrl &url, QObject
    #      *parent)
    self._noteCreation(QQmlComponent, lambda: Rituals.call(
        'ritual_ZN13QQmlComponentC1EP10QQmlEngineRK4QUrlP7QObject',
        self._addressOf(a0), self._valueOf(url), self._addressOf(parent,
        'QObject'),
    ))

  @overload(QQmlEngine, QUrl, CompilationMode)
  @overload(NoneType, QUrl, CompilationMode)
  @overload(QQmlEngine, QUrl, CompilationMode, QObject)
  @overload(QQmlEngine, QUrl, CompilationMode, NoneType)
  @overload(NoneType, QUrl, CompilationMode, QObject)
  @overload(NoneType, QUrl, CompilationMode, NoneType)
  def __init__(
      self,
      a0: Optional[QQmlEngine],
      url: QUrl,
      mode: CompilationMode,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlComponent::QQmlComponent(QQmlEngine
    *a0, const QUrl &url, CompilationMode mode, QObject *parent)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#QQmlComponent

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    mode : CompilationMode
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlComponent::QQmlComponent(QQmlEngine *a0, const QUrl &url,
    #      CompilationMode mode, QObject *parent)
    self._noteCreation(QQmlComponent, lambda: Rituals.call(
        'ritual_ZN13QQmlComponentC1EP10QQmlEngineRK4QUrlNS_15CompilationMod'
        'eEP7QObject',
        self._addressOf(a0), self._valueOf(url), mode.value,
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QQmlEngine, str, str)
  @overload(NoneType, str, str)
  @overload(QQmlEngine, str, str, QObject)
  @overload(QQmlEngine, str, str, NoneType)
  @overload(NoneType, str, str, QObject)
  @overload(NoneType, str, str, NoneType)
  def __init__(
      self,
      engine: Optional[QQmlEngine],
      uri: str,
      typeName: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlComponent::QQmlComponent(QQmlEngine
    *engine, QAnyStringView uri, QAnyStringView typeName, QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#QQmlComponent

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    uri : str
      Passed on as it is: a QString is made of it for the call.

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlComponent::QQmlComponent(QQmlEngine *engine, QAnyStringView uri,
    #      QAnyStringView typeName, QObject *parent)
    self._noteCreation(QQmlComponent, lambda: Rituals.call(
        'ritual_ZN13QQmlComponentC1EP10QQmlEngine14QAnyStringViewS2_P7QObje'
        'ct',
        self._addressOf(engine), uri, typeName, self._addressOf(parent,
        'QObject'),
    ))

  @overload(QQmlEngine, str, str, CompilationMode)
  @overload(NoneType, str, str, CompilationMode)
  @overload(QQmlEngine, str, str, CompilationMode, QObject)
  @overload(QQmlEngine, str, str, CompilationMode, NoneType)
  @overload(NoneType, str, str, CompilationMode, QObject)
  @overload(NoneType, str, str, CompilationMode, NoneType)
  def __init__(
      self,
      engine: Optional[QQmlEngine],
      uri: str,
      typeName: str,
      mode: CompilationMode,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlComponent::QQmlComponent(QQmlEngine
    *engine, QAnyStringView uri, QAnyStringView typeName, CompilationMode
    mode, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#QQmlComponent

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    uri : str
      Passed on as it is: a QString is made of it for the call.

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    mode : CompilationMode
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlComponent::QQmlComponent(QQmlEngine *engine, QAnyStringView uri,
    #      QAnyStringView typeName, CompilationMode mode, QObject *parent)
    self._noteCreation(QQmlComponent, lambda: Rituals.call(
        'ritual_ZN13QQmlComponentC1EP10QQmlEngine14QAnyStringViewS2_NS_15Co'
        'mpilationModeEP7QObject',
        self._addressOf(engine), uri, typeName, mode.value,
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QQmlEngine, WAIT['QV4.ExecutableCompilationUnit'], int, QObject)
  @overload(QQmlEngine, WAIT['QV4.ExecutableCompilationUnit'], int, NoneType)
  @overload(QQmlEngine, NoneType, int, QObject)
  @overload(QQmlEngine, NoneType, int, NoneType)
  @overload(NoneType, WAIT['QV4.ExecutableCompilationUnit'], int, QObject)
  @overload(NoneType, WAIT['QV4.ExecutableCompilationUnit'], int, NoneType)
  @overload(NoneType, NoneType, int, QObject)
  @overload(NoneType, NoneType, int, NoneType)
  def __init__(
      self,
      a0: Optional[QQmlEngine],
      compilationUnit: Optional[QV4.ExecutableCompilationUnit],
      a2: int,
      parent: Optional[QObject],
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlComponent::QQmlComponent(QQmlEngine
    *a0, QV4::ExecutableCompilationUnit *compilationUnit, int a2, QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#QQmlComponent

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    compilationUnit : Optional[QV4.ExecutableCompilationUnit]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a2 : int
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlComponent::QQmlComponent(QQmlEngine *a0,
    #      QV4::ExecutableCompilationUnit *compilationUnit, int a2, QObject
    #      *parent)
    self._noteCreation(QQmlComponent, lambda: Rituals.call(
        'ritual_ZN13QQmlComponentC1EP10QQmlEnginePN3QV425ExecutableCompilat'
        'ionUnitEiP7QObject',
        self._addressOf(a0), self._addressOf(compilationUnit), a2,
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

  def d_func(self) -> Optional[QQmlComponentPrivate]:
    """
    Calls Qt's 'QQmlComponentPrivate *QQmlComponent::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#d_func

    Returns
    -------

    Optional[QQmlComponentPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponentPrivate *QQmlComponent::d_func()
    address = self.uglySide.call('ritual_ZN13QQmlComponent6d_funcEv')
    from . import QQmlComponentPrivate
    return QQmlComponentPrivate._cuteAt(address)

  @overload()
  @overload(QQmlContext)
  @overload(NoneType)
  def create(
      self,
      context: Optional[QQmlContext] = None,
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlComponent::create(QQmlContext *context)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#create

    Parameters
    ----------

    context : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlComponent::create(QQmlContext *context)
    ritual = 'ritual_ZN13QQmlComponent6createEP11QQmlContext'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQmlComponent6createEP11QQmlContext'
    address = self.uglySide.call(ritual, self._addressOf(context))
    return QObject._cuteAt(address)

  @overload(QMap[str, QVariant])
  @overload(QMap[str, QVariant], QQmlContext)
  @overload(QMap[str, QVariant], NoneType)
  def createWithInitialProperties(
      self,
      initialProperties: QMap[str, QVariant],
      context: Optional[QQmlContext] = None,
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlComponent::createWithInitialProperties(const
    QVariantMap &initialProperties, QQmlContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponent.html#createWithInitialProperties

    Parameters
    ----------

    initialProperties : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    context : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlComponent::createWithInitialProperties(const QVariantMap
    #      &initialProperties, QQmlContext *context)
    address = self.uglySide.call(
        'ritual_ZN13QQmlComponent27createWithInitialPropertiesERK4QMapI7QSt'
        'ring8QVariantEP11QQmlContext',
        self._valueOf(initialProperties), self._addressOf(context),
    )
    return QObject._cuteAt(address)

  @overload(QQmlContext)
  @overload(NoneType)
  def beginCreate(self, a0: Optional[QQmlContext]) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlComponent::beginCreate(QQmlContext *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#beginCreate

    Parameters
    ----------

    a0 : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlComponent::beginCreate(QQmlContext *a0)
    ritual = 'ritual_ZN13QQmlComponent11beginCreateEP11QQmlContext'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQmlComponent11beginCreateEP11QQmlContext'
    address = self.uglySide.call(ritual, self._addressOf(a0))
    return QObject._cuteAt(address)

  def completeCreate(self) -> None:
    """
    Calls Qt's 'void QQmlComponent::completeCreate()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#completeCreate
    """
    #  void QQmlComponent::completeCreate()
    ritual = 'ritual_ZN13QQmlComponent14completeCreateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQmlComponent14completeCreateEv'
    self.uglySide.call(ritual)

  @overload(QUrl)
  def loadUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QQmlComponent::loadUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#loadUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQmlComponent::loadUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN13QQmlComponent7loadUrlERK4QUrl', self._valueOf(url),
    )

  @overload(QUrl, CompilationMode)
  def loadUrl(self, url: QUrl, mode: CompilationMode) -> None:
    """
    Calls Qt's 'void QQmlComponent::loadUrl(const QUrl &url, CompilationMode
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#loadUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    mode : CompilationMode
      Passed on as its number.
    """
    #  void QQmlComponent::loadUrl(const QUrl &url, CompilationMode mode)
    self.uglySide.call(
        'ritual_ZN13QQmlComponent7loadUrlERK4QUrlNS_15CompilationModeE',
        self._valueOf(url), mode.value,
    )

  @overload(str, str)
  @overload(str, str, CompilationMode)
  def loadFromModule(
      self,
      uri: str,
      typeName: str,
      mode: CompilationMode = CompilationMode.PreferSynchronous,
  ) -> None:
    """
    Calls Qt's 'void QQmlComponent::loadFromModule(QAnyStringView uri,
    QAnyStringView typeName, QQmlComponent::CompilationMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#loadFromModule

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    mode : CompilationMode
      Passed on as its number. May be left out, as in Qt: it is then
      CompilationMode.PreferSynchronous.
    """
    #  void QQmlComponent::loadFromModule(QAnyStringView uri, QAnyStringView
    #      typeName, QQmlComponent::CompilationMode mode)
    self.uglySide.call(
        'ritual_ZN13QQmlComponent14loadFromModuleE14QAnyStringViewS0_NS_15C'
        'ompilationModeE',
        uri, typeName, mode.value,
    )

  @overload(Status)
  def statusChanged(self, a0: Status) -> None:
    """
    Calls Qt's 'void QQmlComponent::statusChanged(QQmlComponent::Status a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#statusChanged

    Parameters
    ----------

    a0 : Status
      Passed on as its number.
    """
    #  void QQmlComponent::statusChanged(QQmlComponent::Status a0)
    self.uglySide.call(
        'ritual_ZN13QQmlComponent13statusChangedENS_6StatusE', a0.value,
    )

  @overload(float)
  def progressChanged(self, a0: float) -> None:
    """
    Calls Qt's 'void QQmlComponent::progressChanged(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#progressChanged

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQmlComponent::progressChanged(qreal a0)
    self.uglySide.call('ritual_ZN13QQmlComponent15progressChangedEd', a0)

  @overload(QQmlV4Function)
  @overload(NoneType)
  def createObject(self, a0: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQmlComponent::createObject(QQmlV4FunctionPtr a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#createObject

    Parameters
    ----------

    a0 : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlComponent::createObject(QQmlV4FunctionPtr a0)
    self.uglySide.call(
        'ritual_ZN13QQmlComponent12createObjectEP14QQmlV4Function',
        self._addressOf(a0),
    )

  @overload(QObject, QMap[str, QVariant])
  @overload(NoneType, QMap[str, QVariant])
  def createObject(
      self,
      parent: Optional[QObject],
      properties: QMap[str, QVariant],
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlComponent::createObject(QObject *parent, const
    QVariantMap &properties)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#createObject

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    properties : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlComponent::createObject(QObject *parent, const
    #      QVariantMap &properties)
    address = self.uglySide.call(
        'ritual_ZN13QQmlComponent12createObjectEP7QObjectRK4QMapI7QString8Q'
        'VariantE',
        self._addressOf(parent, 'QObject'), self._valueOf(properties),
    )
    return QObject._cuteAt(address)

  @overload(QQmlV4Function)
  @overload(NoneType)
  def incubateObject(self, a0: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQmlComponent::incubateObject(QQmlV4FunctionPtr a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponent.html#incubateObject

    Parameters
    ----------

    a0 : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlComponent::incubateObject(QQmlV4FunctionPtr a0)
    self.uglySide.call(
        'ritual_ZN13QQmlComponent14incubateObjectEP14QQmlV4Function',
        self._addressOf(a0),
    )
