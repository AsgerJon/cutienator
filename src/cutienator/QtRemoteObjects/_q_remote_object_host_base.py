"""
QRemoteObjectHostBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/qremoteobjectnode.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QRemoteObjectNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QIODevice, QMetaObject, QUrl
  from . import QRemoteObjectHostBasePrivate, SourceApiMap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIODevice = WAIT['QIODevice']
  QUrl = WAIT['QUrl']
  SourceApiMap = WAIT['SourceApiMap']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRemoteObjectHostBase(QRemoteObjectNode):
  """
  The cute side of Qt's QRemoteObjectHostBase: a plain Python object standing
  in front of one C++ QRemoteObjectHostBase.

  It is built on the cute 'QRemoteObjectNode', as Qt's QRemoteObjectHostBase
  is built on Qt's QRemoteObjectNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRemoteObjectHostBase that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'setName',
  'enableRemoting', 'disableRemoting', 'addHostSideConnection', 'hostUrl',
  'setHostUrl', 'd_func'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QRemoteObjectHostBase::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QRemoteObjectHostBase::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QRemoteObjectHostBase::~QRemoteObjectHostBase()': the destructor:
    Python never removes a C++ QRemoteObjectHostBase.
  - Qt's 'bool QRemoteObjectHostBase::enableRemoting(QAbstractItemModel
    *model, const QString &name, const QList<int> roles, QItemSelectionModel
    *selectionModel)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QRemoteObjectHostBase::proxy(const QUrl &registryUrl, const
    QUrl &hostUrl, RemoteObjectNameFilter filter)': takes a type Python has
    no way to hand over yet.
  - Qt's 'bool QRemoteObjectHostBase::reverseProxy(RemoteObjectNameFilter
    filter)': takes a type Python has no way to hand over yet.
  - Qt's 'QRemoteObjectHostBase::QRemoteObjectHostBase(
    QRemoteObjectHostBasePrivate &a0, QObject *a1)': takes a type Python has
    no way to hand over yet.
  - Qt's 'const QRemoteObjectHostBasePrivate *QRemoteObjectHostBase::d_func()
    const': takes in Python what 'QRemoteObjectHostBasePrivate
    *QRemoteObjectHostBase::d_func()' takes.

  What has no ritual
  ------------------

  3 of the 21 functions Qt declares: 2 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ QRemoteObjectHostBase is created at the first use, not by
    'QRemoteObjectHostBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRemoteObjectHostBase.
  - Qt tells when it has removed the C++ QRemoteObjectHostBase. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QRemoteObjectHostBase that has no cute function yet,
    '__init__', 'proxy', 'reverseProxy', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QRemoteObjectHostBase, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class AllowedSchemas(CuteNum):
    """
    The enum 'QRemoteObjectHostBase::AllowedSchemas' of Qt, with the 2 names
    Qt gives in it.
    """

    BuiltInSchemasOnly = Kee[int](0)
    AllowExternalRegistration = Kee[int](1)

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
    Calls Qt's 'QString QRemoteObjectHostBase::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjecthostbase.html#tr

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
    #  QString QRemoteObjectHostBase::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QRemoteObjectHostBase2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRemoteObjectHostBase'

  #  A C++ QRemoteObjectHostBase Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRemoteObjectHostBase'

  #  The functions Qt calls itself that QRemoteObjectHostBase is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'hostUrl': (
          ('_ZNK21QRemoteObjectHostBase7hostUrlEv',
           ('address', 'value', 'QtCore:QUrl'),
           ()),
      ),
      'setHostUrl': (
          ('_ZN21QRemoteObjectHostBase10setHostUrlERK4QUrlNS_14AllowedSchem'
           'asE',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
               ('int', 'enum',
                'QtRemoteObjects:QRemoteObjectHostBase.AllowedSchemas'),
           )),
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
    Calls Qt's 'const QMetaObject *QRemoteObjectHostBase::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjecthostbase.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QRemoteObjectHostBase::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QRemoteObjectHostBase10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def hostUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QRemoteObjectHostBase::hostUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjecthostbase.html#hostUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QRemoteObjectHostBase::hostUrl() const
    ritual = 'ritual_ZNK21QRemoteObjectHostBase7hostUrlEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QRemoteObjectHostBase7hostUrlEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QRemoteObjectHostBase::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjecthostbase.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QRemoteObjectHostBase::setName(const QString &name)
    ritual = 'ritual_ZN21QRemoteObjectHostBase7setNameERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QRemoteObjectHostBase7setNameERK7QString'
    self.uglySide.call(ritual, name)

  @overload(QUrl)
  @overload(QUrl, AllowedSchemas)
  def setHostUrl(
      self,
      hostAddress: QUrl,
      allowedSchemas: AllowedSchemas = AllowedSchemas.BuiltInSchemasOnly,
  ) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectHostBase::setHostUrl(const QUrl
    &hostAddress, AllowedSchemas allowedSchemas)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjecthostbase.html#setHostUrl

    Parameters
    ----------

    hostAddress : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    allowedSchemas : AllowedSchemas
      Passed on as its number. May be left out, as in Qt: it is then
      AllowedSchemas.BuiltInSchemasOnly.
    """
    #  bool QRemoteObjectHostBase::setHostUrl(const QUrl &hostAddress,
    #      AllowedSchemas allowedSchemas)
    ritual = (
        'ritual_ZN21QRemoteObjectHostBase10setHostUrlERK4QUrlNS_14AllowedSc'
        'hemasE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QRemoteObjectHostBase10setHostUrlERK4QUrlNS_14All'
          'owedSchemasE')
    return self.uglySide.call(
        ritual, self._valueOf(hostAddress), allowedSchemas.value,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QRemoteObjectHostBase::QRemoteObjectHostBase(
    QRemoteObjectHostBasePrivate &a0, QObject *a1)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectHostBase.__init__' has no cute function yet. Qt's "
        "'QRemoteObjectHostBase::QRemoteObjectHostBase(QRemoteObjectHostBase"
        "Private &a0, QObject *a1)': takes a type Python has no way to hand "
        "over yet.")

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

  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, str)
  @overload(NoneType, str)
  def enableRemoting(
      self,
      object: Optional[QObject],
      name: str = '',
  ) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectHostBase::enableRemoting(QObject *object,
    const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjecthostbase.html#enableRemoting

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  bool QRemoteObjectHostBase::enableRemoting(QObject *object, const
    #      QString &name)
    return self.uglySide.call(
        'ritual_ZN21QRemoteObjectHostBase14enableRemotingEP7QObjectRK7QStri'
        'ng',
        self._addressOf(object, 'QObject'), name,
    )

  @overload(QObject, SourceApiMap)
  @overload(QObject, NoneType)
  @overload(NoneType, SourceApiMap)
  @overload(NoneType, NoneType)
  @overload(QObject, SourceApiMap, QObject)
  @overload(QObject, SourceApiMap, NoneType)
  @overload(QObject, NoneType, QObject)
  @overload(QObject, NoneType, NoneType)
  @overload(NoneType, SourceApiMap, QObject)
  @overload(NoneType, SourceApiMap, NoneType)
  @overload(NoneType, NoneType, QObject)
  @overload(NoneType, NoneType, NoneType)
  def enableRemoting(
      self,
      object: Optional[QObject],
      a1: Optional[SourceApiMap],
      adapter: Optional[QObject] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectHostBase::enableRemoting(QObject *object,
    const SourceApiMap *a1, QObject *adapter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjecthostbase.html#enableRemoting

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[SourceApiMap]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    adapter : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QRemoteObjectHostBase::enableRemoting(QObject *object, const
    #      SourceApiMap *a1, QObject *adapter)
    return self.uglySide.call(
        'ritual_ZN21QRemoteObjectHostBase14enableRemotingEP7QObjectPK12Sour'
        'ceApiMapS1_',
        self._addressOf(object, 'QObject'), self._addressOf(a1),
        self._addressOf(adapter, 'QObject'),
    )

  @overload(QObject)
  @overload(NoneType)
  def disableRemoting(self, remoteObject: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectHostBase::disableRemoting(QObject
    *remoteObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjecthostbase.html#disableRemoting

    Parameters
    ----------

    remoteObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QRemoteObjectHostBase::disableRemoting(QObject *remoteObject)
    return self.uglySide.call(
        'ritual_ZN21QRemoteObjectHostBase15disableRemotingEP7QObject',
        self._addressOf(remoteObject, 'QObject'),
    )

  @overload(QIODevice)
  @overload(NoneType)
  def addHostSideConnection(self, ioDevice: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QRemoteObjectHostBase::addHostSideConnection(QIODevice
    *ioDevice)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjecthostbase.html#addHostSideConnection

    Parameters
    ----------

    ioDevice : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRemoteObjectHostBase::addHostSideConnection(QIODevice *ioDevice)
    self.uglySide.call(
        'ritual_ZN21QRemoteObjectHostBase21addHostSideConnectionEP9QIODevic'
        'e',
        self._addressOf(ioDevice),
    )

  def d_func(self) -> Optional[QRemoteObjectHostBasePrivate]:
    """
    Calls Qt's 'QRemoteObjectHostBasePrivate
    *QRemoteObjectHostBase::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjecthostbase.html#d_func

    Returns
    -------

    Optional[QRemoteObjectHostBasePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRemoteObjectHostBasePrivate *QRemoteObjectHostBase::d_func()
    address = self.uglySide.call('ritual_ZN21QRemoteObjectHostBase6d_funcEv')
    from . import QRemoteObjectHostBasePrivate
    return QRemoteObjectHostBasePrivate._cuteAt(address)

  @staticmethod
  def proxy(*__, **_) -> Never:
    """
    Qt's 'bool QRemoteObjectHostBase::proxy(const QUrl &registryUrl, const
    QUrl &hostUrl, RemoteObjectNameFilter filter)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectHostBase.proxy' has no cute function yet. Qt's 'bool "
        "QRemoteObjectHostBase::proxy(const QUrl &registryUrl, const QUrl "
        "&hostUrl, RemoteObjectNameFilter filter)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def reverseProxy(*__, **_) -> Never:
    """
    Qt's 'bool QRemoteObjectHostBase::reverseProxy(RemoteObjectNameFilter
    filter)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectHostBase.reverseProxy' has no cute function yet. "
        "Qt's 'bool "
        "QRemoteObjectHostBase::reverseProxy(RemoteObjectNameFilter "
        "filter)': takes a type Python has no way to hand over yet.")
