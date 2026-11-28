"""
QQmlContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qqmlcontext.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl, QVariant
  from . import QJSValue, QQmlContextPrivate, QQmlEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlEngine = WAIT['QQmlEngine']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlContext(QObject):
  """
  The cute side of Qt's QQmlContext: a plain Python object standing in front
  of one C++ QQmlContext.

  It is built on the cute 'QObject', as Qt's QQmlContext is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlContext that has a ritual and that Python can
  call so far, 19 names in all: 'metaObject', 'tr', 'd_func', 'isValid',
  'engine', 'parentContext', 'childContexts', 'contextObject',
  'setContextObject', 'contextProperty', 'setContextProperty',
  'nameForObject', 'objectForName', 'findObjectRecursively',
  'findObjectsRecursively', 'resolvedUrl', 'setBaseUrl', 'baseUrl',
  'importedScript'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlContext::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQmlContext::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QQmlContextPrivate *QQmlContext::d_func() const': takes in
    Python what 'QQmlContextPrivate *QQmlContext::d_func()' takes.
  - Qt's 'QQmlContext::~QQmlContext()': the destructor: Python never removes
    a C++ QQmlContext.
  - Qt's 'void QQmlContext::setContextProperties(const QList<PropertyPair>
    &properties)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlContext::QQmlContext(QQmlContextPrivate &dd, QObject *parent)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 33 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQmlContext is created at the first use, not by
    'QQmlContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlContext.
  - Qt tells when it has removed the C++ QQmlContext. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QQmlContext that has no cute function yet,
    'setContextProperties', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QQmlContext, each a class in here as in
  #  C++.

  class PropertyPair(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlContext::PropertyPair: a plain Python object
    standing in front of one C++ QQmlContext::PropertyPair.

    C++ hands a QQmlContext::PropertyPair around as a copy, so every C++
    QQmlContext::PropertyPair behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQmlContext::PropertyPair yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlContext::PropertyPair::~PropertyPair()': the destructor:
      Python removes its C++ QQmlContext::PropertyPair by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQmlContext::PropertyPair is created at the first use, not by
      'QQmlContext::PropertyPair(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlContext::PropertyPair back gives a copy the
      ritual made for Python, in a new cute QQmlContext::PropertyPair.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlContext::PropertyPair'

    #  Qt's '~QQmlContext::PropertyPair()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlContext::PropertyPair behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QQmlContext12PropertyPairD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Calls Qt's 'QString QQmlContext::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontext.html#tr

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
    #  QString QQmlContext::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QQmlContext2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlContext'

  #  A C++ QQmlContext Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlContext'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlContext::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontext.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlContext::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QQmlContext10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlContext::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontext.html#isValid
    """
    #  bool QQmlContext::isValid() const
    return self.uglySide.call('ritual_ZNK11QQmlContext7isValidEv')

  def engine(self) -> Optional[QQmlEngine]:
    """
    Calls Qt's 'QQmlEngine *QQmlContext::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontext.html#engine

    Returns
    -------

    Optional[QQmlEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlEngine *QQmlContext::engine() const
    address = self.uglySide.call('ritual_ZNK11QQmlContext6engineEv')
    from . import QQmlEngine
    return QQmlEngine._cuteAt(address)

  def parentContext(self) -> Optional[QQmlContext]:
    """
    Calls Qt's 'QQmlContext *QQmlContext::parentContext() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontext.html#parentContext

    Returns
    -------

    Optional[QQmlContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlContext *QQmlContext::parentContext() const
    address = self.uglySide.call('ritual_ZNK11QQmlContext13parentContextEv')
    return QQmlContext._cuteAt(address)

  def childContexts(self) -> QList[QQmlContext]:
    """
    Calls Qt's 'QList<QQmlContext *> QQmlContext::childContexts() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontext.html#childContexts

    Returns
    -------

    QList[QQmlContext]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlContext *> QQmlContext::childContexts() const
    address = self.uglySide.call('ritual_ZNK11QQmlContext13childContextsEv')
    return QList[QQmlContext]._cuteOwning(address)

  def contextObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlContext::contextObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontext.html#contextObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlContext::contextObject() const
    address = self.uglySide.call('ritual_ZNK11QQmlContext13contextObjectEv')
    return QObject._cuteAt(address)

  @overload(str)
  def contextProperty(self, a0: str) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlContext::contextProperty(const QString &a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontext.html#contextProperty

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlContext::contextProperty(const QString &a0) const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlContext15contextPropertyERK7QString', a0,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QObject)
  @overload(NoneType)
  def nameForObject(self, a0: Optional[QObject]) -> str:
    """
    Calls Qt's 'QString QQmlContext::nameForObject(const QObject *a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontext.html#nameForObject

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlContext::nameForObject(const QObject *a0) const
    return self.uglySide.call(
        'ritual_ZNK11QQmlContext13nameForObjectEPK7QObject',
        self._addressOf(a0, 'QObject'),
    )

  @overload(str)
  def objectForName(self, a0: str) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlContext::objectForName(const QString &a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontext.html#objectForName

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlContext::objectForName(const QString &a0) const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlContext13objectForNameERK7QString', a0,
    )
    return QObject._cuteAt(address)

  @overload(str)
  def findObjectRecursively(self, id: str) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlContext::findObjectRecursively(const QString
    &id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontext.html#findObjectRecursively

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlContext::findObjectRecursively(const QString &id) const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlContext21findObjectRecursivelyERK7QString', id,
    )
    return QObject._cuteAt(address)

  @overload(str)
  def findObjectsRecursively(self, id: str) -> QList[QObject]:
    """
    Calls Qt's 'QList<QObject *> QQmlContext::findObjectsRecursively(const
    QString &id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontext.html#findObjectsRecursively

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QList[QObject]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QObject *> QQmlContext::findObjectsRecursively(const QString
    #      &id) const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlContext22findObjectsRecursivelyERK7QString', id,
    )
    return QList[QObject]._cuteOwning(address)

  @overload(QUrl)
  def resolvedUrl(self, a0: QUrl) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlContext::resolvedUrl(const QUrl &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontext.html#resolvedUrl

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlContext::resolvedUrl(const QUrl &a0) const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlContext11resolvedUrlERK4QUrl', self._valueOf(a0),
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def baseUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlContext::baseUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontext.html#baseUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlContext::baseUrl() const
    address = self.uglySide.call('ritual_ZNK11QQmlContext7baseUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(str)
  def importedScript(self, name: str) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQmlContext::importedScript(const QString &name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontext.html#importedScript

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQmlContext::importedScript(const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlContext14importedScriptERK7QString', name,
    )
    from . import QJSValue
    return QJSValue._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setContextObject(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlContext::setContextObject(QObject *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontext.html#setContextObject

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlContext::setContextObject(QObject *a0)
    self.uglySide.call(
        'ritual_ZN11QQmlContext16setContextObjectEP7QObject',
        self._addressOf(a0, 'QObject'),
    )

  @overload(str, QObject)
  @overload(str, NoneType)
  def setContextProperty(self, a0: str, a1: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlContext::setContextProperty(const QString &a0,
    QObject *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontext.html#setContextProperty

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlContext::setContextProperty(const QString &a0, QObject *a1)
    self.uglySide.call(
        'ritual_ZN11QQmlContext18setContextPropertyERK7QStringP7QObject',
        a0, self._addressOf(a1, 'QObject'),
    )

  @overload(str, QVariant)
  def setContextProperty(self, a0: str, a1: QVariant) -> None:
    """
    Calls Qt's 'void QQmlContext::setContextProperty(const QString &a0, const
    QVariant &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontext.html#setContextProperty

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlContext::setContextProperty(const QString &a0, const QVariant
    #      &a1)
    self.uglySide.call(
        'ritual_ZN11QQmlContext18setContextPropertyERK7QStringRK8QVariant',
        a0, self._valueOf(a1),
    )

  @overload(QUrl)
  def setBaseUrl(self, a0: QUrl) -> None:
    """
    Calls Qt's 'void QQmlContext::setBaseUrl(const QUrl &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontext.html#setBaseUrl

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQmlContext::setBaseUrl(const QUrl &a0)
    self.uglySide.call(
        'ritual_ZN11QQmlContext10setBaseUrlERK4QUrl', self._valueOf(a0),
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
  @overload(NoneType)
  @overload(QQmlEngine, QObject)
  @overload(QQmlEngine, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      parent: Optional[QQmlEngine],
      objParent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlContext::QQmlContext(QQmlEngine
    *parent, QObject *objParent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontext.html#QQmlContext

    Parameters
    ----------

    parent : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    objParent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlContext::QQmlContext(QQmlEngine *parent, QObject *objParent)
    self._noteCreation(QQmlContext, lambda: Rituals.call(
        'ritual_ZN11QQmlContextC1EP10QQmlEngineP7QObject',
        self._addressOf(parent), self._addressOf(objParent, 'QObject'),
    ))

  @overload(THIS)
  @overload(THIS, QObject)
  @overload(THIS, NoneType)
  def __init__(
      self,
      parent: Optional[QQmlContext],
      objParent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlContext::QQmlContext(QQmlContext
    *parent, QObject *objParent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontext.html#QQmlContext

    Parameters
    ----------

    parent : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    objParent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlContext::QQmlContext(QQmlContext *parent, QObject *objParent)
    self._noteCreation(QQmlContext, lambda: Rituals.call(
        'ritual_ZN11QQmlContextC1EPS_P7QObject',
        self._addressOf(parent), self._addressOf(objParent, 'QObject'),
    ))

  @overload(QQmlEngine, bool)
  @overload(NoneType, bool)
  def __init__(self, a0: Optional[QQmlEngine], a1: bool) -> None:
    """
    Notes what was given, for Qt's 'QQmlContext::QQmlContext(QQmlEngine *a0,
    bool a1)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontext.html#QQmlContext

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : bool
      Passed on as it is.
    """
    #  QQmlContext::QQmlContext(QQmlEngine *a0, bool a1)
    self._noteCreation(QQmlContext, lambda: Rituals.call(
        'ritual_ZN11QQmlContextC1EP10QQmlEngineb', self._addressOf(a0), a1,
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

  def d_func(self) -> Optional[QQmlContextPrivate]:
    """
    Calls Qt's 'QQmlContextPrivate *QQmlContext::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontext.html#d_func

    Returns
    -------

    Optional[QQmlContextPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlContextPrivate *QQmlContext::d_func()
    address = self.uglySide.call('ritual_ZN11QQmlContext6d_funcEv')
    from . import QQmlContextPrivate
    return QQmlContextPrivate._cuteAt(address)

  @staticmethod
  def setContextProperties(*__, **_) -> Never:
    """
    Qt's 'void QQmlContext::setContextProperties(const QList<PropertyPair>
    &properties)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlContext.setContextProperties' has no cute function yet. Qt's "
        "'void QQmlContext::setContextProperties(const QList<PropertyPair> "
        "&properties)': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<QQmlContext *>': the list of QQmlContext, which
#  'QList[QQmlContext]' gives. It is made here, so that there is one as soon
#  as there can be a QQmlContext.
QList.createKind(
    QQmlContext, 'address',
    make='ritual_list_make_QQmlContext_ptr',
    add='ritual_list_add_QQmlContext_ptr',
    size='ritual_list_size_QQmlContext_ptr',
    at='ritual_list_at_QQmlContext_ptr',
    drop='ritual_list_drop_QQmlContext_ptr',
)
