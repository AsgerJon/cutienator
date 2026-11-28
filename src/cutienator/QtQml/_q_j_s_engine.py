"""
QJSEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qjsengine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QJSValue, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDate, QDateTime, QMetaObject
  from . import QJSEnginePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']
  QMetaObject = WAIT['QMetaObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QJSEngine(QObject):
  """
  The cute side of Qt's QJSEngine: a plain Python object standing in front of
  one C++ QJSEngine.

  It is built on the cute 'QObject', as Qt's QJSEngine is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QJSEngine that has a ritual and that Python can call
  so far, 29 names in all: 'metaObject', 'tr', 'globalObject',
  'importModule', 'registerModule', 'newObject', 'newSymbol', 'newArray',
  'newQObject', 'newQMetaObject', 'newErrorObject', 'collectGarbage',
  'setObjectOwnership', 'objectOwnership', 'installExtensions',
  'setInterrupted', 'isInterrupted', 'handle', 'throwError', 'hasError',
  'catchError', 'uiLanguage', 'setUiLanguage', 'uiLanguageChanged',
  'convertQObjectToString', 'convertDateTimeToString',
  'convertDateTimeToNumber', 'convertDateTimeToDate', 'd_func'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QJSEngine::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QJSEngine::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QJSEngine::~QJSEngine()': the destructor: Python never removes a
    C++ QJSEngine.
  - Qt's 'QJSValue QJSEngine::evaluate(const QString &program, const QString
    &fileName, int lineNumber, QStringList *exceptionStackTrace)': names
    'QStringList', which has no cute class yet.
  - Qt's 'QJSPrimitiveValue QJSEngine::createPrimitive(QMetaType type, const
    void *ptr)': names 'void', which has no cute class yet.
  - Qt's 'QJSManagedValue QJSEngine::createManaged(QMetaType type, const void
    *ptr)': names 'void', which has no cute class yet.
  - Qt's 'QJSValue QJSEngine::create(QMetaType type, const void *ptr)': names
    'void', which has no cute class yet.
  - Qt's 'bool QJSEngine::convertPrimitive(const QJSPrimitiveValue &value,
    QMetaType type, void *ptr)': names 'void', which has no cute class yet.
  - Qt's 'bool QJSEngine::convertManaged(const QJSManagedValue &value, int
    type, void *ptr)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QJSEngine::convertManaged(const QJSManagedValue &value,
    QMetaType type, void *ptr)': takes a type Python has no way to hand over
    yet.
  - Qt's 'bool QJSEngine::convertV2(const QJSValue &value, QMetaType
    metaType, void *ptr)': names 'void', which has no cute class yet.
  - Qt's 'bool QJSEngine::convertString(const QString &string, QMetaType
    metaType, void *ptr)': names 'void', which has no cute class yet.
  - Qt's 'bool QJSEngine::convertVariant(const QVariant &value, QMetaType
    metaType, void *ptr)': names 'void', which has no cute class yet.
  - Qt's 'bool QJSEngine::convertMetaType(QMetaType fromType, const void
    *from, QMetaType toType, void *to)': names 'void', which has no cute
    class yet.
  - Qt's 'QJSEngine::QJSEngine(QJSEnginePrivate &dd, QObject *parent)': takes
    a type Python has no way to hand over yet.
  - Qt's 'const QJSEnginePrivate *QJSEngine::d_func() const': takes in Python
    what 'QJSEnginePrivate *QJSEngine::d_func()' takes.

  What has no ritual
  ------------------

  13 of the 62 functions Qt declares: 9 a template; 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QJSEngine is created at the first use, not by 'QJSEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QJSEngine.
  - Qt tells when it has removed the C++ QJSEngine. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QJSEngine that has no cute function yet, 'coerceValue',
    'convertManaged', 'convertMetaType', 'convertPrimitive', 'convertString',
    'convertV2', 'convertVariant', 'create', 'createManaged',
    'createPrimitive', 'evaluate', 'fromManagedValue', 'fromPrimitiveValue',
    'fromScriptValue', 'fromVariant', 'toManagedValue', 'toPrimitiveValue',
    'toScriptValue', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QJSEngine, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Extension(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QJSEngine::Extension' of Qt, with the 4 names Qt gives in
    it. Qt names the type of its combinations 'QJSEngine::Extensions'.
    """

    TranslationExtension = 0x1
    ConsoleExtension = 0x2
    GarbageCollectionExtension = 0x4
    AllExtensions = 0xffffffff

  Extensions = Extension

  class ObjectOwnership(CuteNum):
    """
    The enum 'QJSEngine::ObjectOwnership' of Qt, with the 2 names Qt gives in
    it.
    """

    CppOwnership = Kee[int](0)
    JavaScriptOwnership = Kee[int](1)

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
    Calls Qt's 'QString QJSEngine::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#tr

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
    #  QString QJSEngine::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QJSEngine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject, ObjectOwnership)
  @overload(NoneType, ObjectOwnership)
  def setObjectOwnership(a0: Optional[QObject], a1: ObjectOwnership) -> None:
    """
    Calls Qt's 'void QJSEngine::setObjectOwnership(QObject *a0,
    ObjectOwnership a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#setObjectOwnership

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : ObjectOwnership
      Passed on as its number.
    """
    #  void QJSEngine::setObjectOwnership(QObject *a0, ObjectOwnership a1)
    Rituals.call(
        'ritual_ZN9QJSEngine18setObjectOwnershipEP7QObjectNS_15ObjectOwners'
        'hipE',
        CuteMixin._addressOf(a0, 'QObject'), a1.value,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def objectOwnership(a0: Optional[QObject]) -> ObjectOwnership:
    """
    Calls Qt's 'ObjectOwnership QJSEngine::objectOwnership(QObject *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#objectOwnership

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    ObjectOwnership
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ObjectOwnership(number)'
      gives.
    """
    #  ObjectOwnership QJSEngine::objectOwnership(QObject *a0)
    return QJSEngine.ObjectOwnership(Rituals.call(
        'ritual_ZN9QJSEngine15objectOwnershipEP7QObject',
        CuteMixin._addressOf(a0, 'QObject'),
    ))

  @staticmethod
  @overload(QDateTime)
  def convertDateTimeToDate(dateTime: QDateTime) -> QDate:
    """
    Calls Qt's 'QDate QJSEngine::convertDateTimeToDate(const QDateTime
    &dateTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsengine.html#convertDateTimeToDate

    Parameters
    ----------

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QJSEngine::convertDateTimeToDate(const QDateTime &dateTime)
    address = Rituals.call(
        'ritual_ZN9QJSEngine21convertDateTimeToDateERK9QDateTime',
        CuteMixin._valueOf(dateTime),
    )
    from ..QtCore import QDate
    return QDate._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QJSEngine'

  #  A C++ QJSEngine Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QJSEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QJSEngine::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QJSEngine::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QJSEngine10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def globalObject(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QJSEngine::globalObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#globalObject

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSEngine::globalObject() const
    address = self.uglySide.call('ritual_ZNK9QJSEngine12globalObjectEv')
    return QJSValue._cuteOwning(address)

  def isInterrupted(self) -> bool:
    """
    Calls Qt's 'bool QJSEngine::isInterrupted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#isInterrupted
    """
    #  bool QJSEngine::isInterrupted() const
    return self.uglySide.call('ritual_ZNK9QJSEngine13isInterruptedEv')

  def handle(self) -> Optional[QV4.ExecutionEngine]:
    """
    Calls Qt's 'QV4::ExecutionEngine *QJSEngine::handle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#handle

    Returns
    -------

    Optional[QV4.ExecutionEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::ExecutionEngine *QJSEngine::handle() const
    address = self.uglySide.call('ritual_ZNK9QJSEngine6handleEv')
    return QV4.ExecutionEngine._cuteAt(address)

  def hasError(self) -> bool:
    """
    Calls Qt's 'bool QJSEngine::hasError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#hasError
    """
    #  bool QJSEngine::hasError() const
    return self.uglySide.call('ritual_ZNK9QJSEngine8hasErrorEv')

  def uiLanguage(self) -> str:
    """
    Calls Qt's 'QString QJSEngine::uiLanguage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#uiLanguage

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QJSEngine::uiLanguage() const
    return self.uglySide.call('ritual_ZNK9QJSEngine10uiLanguageEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setInterrupted(self, interrupted: bool) -> None:
    """
    Calls Qt's 'void QJSEngine::setInterrupted(bool interrupted)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#setInterrupted

    Parameters
    ----------

    interrupted : bool
      Passed on as it is.
    """
    #  void QJSEngine::setInterrupted(bool interrupted)
    self.uglySide.call('ritual_ZN9QJSEngine14setInterruptedEb', interrupted)

  @overload(str)
  def setUiLanguage(self, language: str) -> None:
    """
    Calls Qt's 'void QJSEngine::setUiLanguage(const QString &language)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#setUiLanguage

    Parameters
    ----------

    language : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QJSEngine::setUiLanguage(const QString &language)
    self.uglySide.call(
        'ritual_ZN9QJSEngine13setUiLanguageERK7QString', language,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QJSEngine::QJSEngine()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#QJSEngine
    """
    #  QJSEngine::QJSEngine()
    self._noteCreation(QJSEngine, lambda: Rituals.call(
        'ritual_ZN9QJSEngineC1Ev',
    ))

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QJSEngine::QJSEngine(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#QJSEngine

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QJSEngine::QJSEngine(QObject *parent)
    self._noteCreation(QJSEngine, lambda: Rituals.call(
        'ritual_ZN9QJSEngineC1EP7QObject',
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

  @overload(str)
  def importModule(self, fileName: str) -> QJSValue:
    """
    Calls Qt's 'QJSValue QJSEngine::importModule(const QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#importModule

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSEngine::importModule(const QString &fileName)
    address = self.uglySide.call(
        'ritual_ZN9QJSEngine12importModuleERK7QString', fileName,
    )
    return QJSValue._cuteOwning(address)

  @overload(str, QJSValue)
  def registerModule(self, moduleName: str, value: QJSValue) -> bool:
    """
    Calls Qt's 'bool QJSEngine::registerModule(const QString &moduleName,
    const QJSValue &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#registerModule

    Parameters
    ----------

    moduleName : str
      Passed on as it is: a QString is made of it for the call.

    value : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  bool QJSEngine::registerModule(const QString &moduleName, const
    #      QJSValue &value)
    return self.uglySide.call(
        'ritual_ZN9QJSEngine14registerModuleERK7QStringRK8QJSValue',
        moduleName, self._valueOf(value),
    )

  def newObject(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QJSEngine::newObject()'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#newObject

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSEngine::newObject()
    address = self.uglySide.call('ritual_ZN9QJSEngine9newObjectEv')
    return QJSValue._cuteOwning(address)

  @overload(str)
  def newSymbol(self, name: str) -> QJSValue:
    """
    Calls Qt's 'QJSValue QJSEngine::newSymbol(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#newSymbol

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSEngine::newSymbol(const QString &name)
    address = self.uglySide.call(
        'ritual_ZN9QJSEngine9newSymbolERK7QString', name,
    )
    return QJSValue._cuteOwning(address)

  @overload()
  @overload(int)
  def newArray(self, length: int = 0) -> QJSValue:
    """
    Calls Qt's 'QJSValue QJSEngine::newArray(uint length)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#newArray

    Parameters
    ----------

    length : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSEngine::newArray(uint length)
    address = self.uglySide.call('ritual_ZN9QJSEngine8newArrayEj', length)
    return QJSValue._cuteOwning(address)

  @overload(QObject)
  @overload(NoneType)
  def newQObject(self, object: Optional[QObject]) -> QJSValue:
    """
    Calls Qt's 'QJSValue QJSEngine::newQObject(QObject *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#newQObject

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSEngine::newQObject(QObject *object)
    address = self.uglySide.call(
        'ritual_ZN9QJSEngine10newQObjectEP7QObject',
        self._addressOf(object, 'QObject'),
    )
    return QJSValue._cuteOwning(address)

  @overload(QMetaObject)
  @overload(NoneType)
  def newQMetaObject(self, metaObject: Optional[QMetaObject]) -> QJSValue:
    """
    Calls Qt's 'QJSValue QJSEngine::newQMetaObject(const QMetaObject
    *metaObject)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#newQMetaObject

    Parameters
    ----------

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSEngine::newQMetaObject(const QMetaObject *metaObject)
    address = self.uglySide.call(
        'ritual_ZN9QJSEngine14newQMetaObjectEPK11QMetaObject',
        self._addressOf(metaObject, 'QMetaObject'),
    )
    return QJSValue._cuteOwning(address)

  @overload(QJSValue.ErrorType)
  @overload(QJSValue.ErrorType, str)
  def newErrorObject(
      self,
      errorType: QJSValue.ErrorType,
      message: str = '',
  ) -> QJSValue:
    """
    Calls Qt's 'QJSValue QJSEngine::newErrorObject(QJSValue::ErrorType
    errorType, const QString &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#newErrorObject

    Parameters
    ----------

    errorType : QJSValue.ErrorType
      Passed on as its number.

    message : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSEngine::newErrorObject(QJSValue::ErrorType errorType,
    #      const QString &message)
    address = self.uglySide.call(
        'ritual_ZN9QJSEngine14newErrorObjectEN8QJSValue9ErrorTypeERK7QStrin'
        'g',
        errorType.value, message,
    )
    return QJSValue._cuteOwning(address)

  def collectGarbage(self) -> None:
    """
    Calls Qt's 'void QJSEngine::collectGarbage()'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#collectGarbage
    """
    #  void QJSEngine::collectGarbage()
    self.uglySide.call('ritual_ZN9QJSEngine14collectGarbageEv')

  @overload(Extensions, QJSValue)
  def installExtensions(
      self,
      extensions: Extensions,
      object: QJSValue,
  ) -> None:
    """
    Calls Qt's 'void QJSEngine::installExtensions(Extensions extensions,
    const QJSValue &object)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#installExtensions

    Parameters
    ----------

    extensions : Extensions
      Passed on as its number.

    object : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QJSEngine::installExtensions(Extensions extensions, const
    #      QJSValue &object)
    self.uglySide.call(
        'ritual_ZN9QJSEngine17installExtensionsE6QFlagsINS_9ExtensionEERK8Q'
        'JSValue',
        extensions.value, self._valueOf(object),
    )

  @overload(str)
  def throwError(self, message: str) -> None:
    """
    Calls Qt's 'void QJSEngine::throwError(const QString &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#throwError

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QJSEngine::throwError(const QString &message)
    self.uglySide.call('ritual_ZN9QJSEngine10throwErrorERK7QString', message)

  @overload(QJSValue.ErrorType)
  @overload(QJSValue.ErrorType, str)
  def throwError(
      self,
      errorType: QJSValue.ErrorType,
      message: str = '',
  ) -> None:
    """
    Calls Qt's 'void QJSEngine::throwError(QJSValue::ErrorType errorType,
    const QString &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#throwError

    Parameters
    ----------

    errorType : QJSValue.ErrorType
      Passed on as its number.

    message : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QJSEngine::throwError(QJSValue::ErrorType errorType, const
    #      QString &message)
    self.uglySide.call(
        'ritual_ZN9QJSEngine10throwErrorEN8QJSValue9ErrorTypeERK7QString',
        errorType.value, message,
    )

  @overload(QJSValue)
  def throwError(self, error: QJSValue) -> None:
    """
    Calls Qt's 'void QJSEngine::throwError(const QJSValue &error)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#throwError

    Parameters
    ----------

    error : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QJSEngine::throwError(const QJSValue &error)
    self.uglySide.call(
        'ritual_ZN9QJSEngine10throwErrorERK8QJSValue', self._valueOf(error),
    )

  def catchError(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QJSEngine::catchError()'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#catchError

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QJSEngine::catchError()
    address = self.uglySide.call('ritual_ZN9QJSEngine10catchErrorEv')
    return QJSValue._cuteOwning(address)

  def uiLanguageChanged(self) -> None:
    """
    Calls Qt's 'void QJSEngine::uiLanguageChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#uiLanguageChanged
    """
    #  void QJSEngine::uiLanguageChanged()
    self.uglySide.call('ritual_ZN9QJSEngine17uiLanguageChangedEv')

  @overload(QObject)
  @overload(NoneType)
  def convertQObjectToString(self, object: Optional[QObject]) -> str:
    """
    Calls Qt's 'QString QJSEngine::convertQObjectToString(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsengine.html#convertQObjectToString

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QJSEngine::convertQObjectToString(QObject *object)
    return self.uglySide.call(
        'ritual_ZN9QJSEngine22convertQObjectToStringEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(QDateTime)
  def convertDateTimeToString(self, dateTime: QDateTime) -> str:
    """
    Calls Qt's 'QString QJSEngine::convertDateTimeToString(const QDateTime
    &dateTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsengine.html#convertDateTimeToString

    Parameters
    ----------

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QJSEngine::convertDateTimeToString(const QDateTime &dateTime)
    return self.uglySide.call(
        'ritual_ZN9QJSEngine23convertDateTimeToStringERK9QDateTime',
        self._valueOf(dateTime),
    )

  @overload(QDateTime)
  def convertDateTimeToNumber(self, dateTime: QDateTime) -> float:
    """
    Calls Qt's 'double QJSEngine::convertDateTimeToNumber(const QDateTime
    &dateTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsengine.html#convertDateTimeToNumber

    Parameters
    ----------

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  double QJSEngine::convertDateTimeToNumber(const QDateTime &dateTime)
    return self.uglySide.call(
        'ritual_ZN9QJSEngine23convertDateTimeToNumberERK9QDateTime',
        self._valueOf(dateTime),
    )

  def d_func(self) -> Optional[QJSEnginePrivate]:
    """
    Calls Qt's 'QJSEnginePrivate *QJSEngine::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qjsengine.html#d_func

    Returns
    -------

    Optional[QJSEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QJSEnginePrivate *QJSEngine::d_func()
    address = self.uglySide.call('ritual_ZN9QJSEngine6d_funcEv')
    from . import QJSEnginePrivate
    return QJSEnginePrivate._cuteAt(address)

  @staticmethod
  def coerceValue(*__, **_) -> Never:
    """
    Qt's 'QJSEngine::coerceValue': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QJSEngine.coerceValue' has no cute function yet. Qt's "
        "'QJSEngine::coerceValue': a template: a pattern and no single "
        "function.")

  @staticmethod
  def convertManaged(*__, **_) -> Never:
    """
    - Qt's 'bool QJSEngine::convertManaged(const QJSManagedValue &value, int
      type, void *ptr)': takes a type Python has no way to hand over yet.
    - Qt's 'bool QJSEngine::convertManaged(const QJSManagedValue &value,
      QMetaType type, void *ptr)': takes a type Python has no way to hand
      over yet.
    """
    raise NotImplementedError(
        "'QJSEngine.convertManaged' has no cute function yet. Qt's 'bool "
        "QJSEngine::convertManaged(const QJSManagedValue &value, int type, "
        "void *ptr)': takes a type Python has no way to hand over yet. Qt's "
        "'bool QJSEngine::convertManaged(const QJSManagedValue &value, "
        "QMetaType type, void *ptr)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def convertMetaType(*__, **_) -> Never:
    """
    Qt's 'bool QJSEngine::convertMetaType(QMetaType fromType, const void
    *from, QMetaType toType, void *to)': names 'void', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QJSEngine.convertMetaType' has no cute function yet. Qt's 'bool "
        "QJSEngine::convertMetaType(QMetaType fromType, const void *from, "
        "QMetaType toType, void *to)': names 'void', which has no cute "
        "class yet.")

  @staticmethod
  def convertPrimitive(*__, **_) -> Never:
    """
    Qt's 'bool QJSEngine::convertPrimitive(const QJSPrimitiveValue &value,
    QMetaType type, void *ptr)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QJSEngine.convertPrimitive' has no cute function yet. Qt's 'bool "
        "QJSEngine::convertPrimitive(const QJSPrimitiveValue &value, "
        "QMetaType type, void *ptr)': names 'void', which has no cute class "
        "yet.")

  @staticmethod
  def convertString(*__, **_) -> Never:
    """
    Qt's 'bool QJSEngine::convertString(const QString &string, QMetaType
    metaType, void *ptr)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QJSEngine.convertString' has no cute function yet. Qt's 'bool "
        "QJSEngine::convertString(const QString &string, QMetaType "
        "metaType, void *ptr)': names 'void', which has no cute class yet.")

  @staticmethod
  def convertV2(*__, **_) -> Never:
    """
    Qt's 'bool QJSEngine::convertV2(const QJSValue &value, QMetaType
    metaType, void *ptr)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QJSEngine.convertV2' has no cute function yet. Qt's 'bool "
        "QJSEngine::convertV2(const QJSValue &value, QMetaType metaType, "
        "void *ptr)': names 'void', which has no cute class yet.")

  @staticmethod
  def convertVariant(*__, **_) -> Never:
    """
    Qt's 'bool QJSEngine::convertVariant(const QVariant &value, QMetaType
    metaType, void *ptr)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QJSEngine.convertVariant' has no cute function yet. Qt's 'bool "
        "QJSEngine::convertVariant(const QVariant &value, QMetaType "
        "metaType, void *ptr)': names 'void', which has no cute class yet.")

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'QJSValue QJSEngine::create(QMetaType type, const void *ptr)': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QJSEngine.create' has no cute function yet. Qt's 'QJSValue "
        "QJSEngine::create(QMetaType type, const void *ptr)': names 'void', "
        "which has no cute class yet.")

  @staticmethod
  def createManaged(*__, **_) -> Never:
    """
    Qt's 'QJSManagedValue QJSEngine::createManaged(QMetaType type, const void
    *ptr)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QJSEngine.createManaged' has no cute function yet. Qt's "
        "'QJSManagedValue QJSEngine::createManaged(QMetaType type, const "
        "void *ptr)': names 'void', which has no cute class yet.")

  @staticmethod
  def createPrimitive(*__, **_) -> Never:
    """
    Qt's 'QJSPrimitiveValue QJSEngine::createPrimitive(QMetaType type, const
    void *ptr)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QJSEngine.createPrimitive' has no cute function yet. Qt's "
        "'QJSPrimitiveValue QJSEngine::createPrimitive(QMetaType type, "
        "const void *ptr)': names 'void', which has no cute class yet.")

  @staticmethod
  def evaluate(*__, **_) -> Never:
    """
    Qt's 'QJSValue QJSEngine::evaluate(const QString &program, const QString
    &fileName, int lineNumber, QStringList *exceptionStackTrace)': names
    'QStringList', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QJSEngine.evaluate' has no cute function yet. Qt's 'QJSValue "
        "QJSEngine::evaluate(const QString &program, const QString "
        "&fileName, int lineNumber, QStringList *exceptionStackTrace)': "
        "names 'QStringList', which has no cute class yet.")

  @staticmethod
  def fromManagedValue(*__, **_) -> Never:
    """
    Qt's 'QJSEngine::fromManagedValue': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QJSEngine.fromManagedValue' has no cute function yet. Qt's "
        "'QJSEngine::fromManagedValue': a template: a pattern and no single "
        "function.")

  @staticmethod
  def fromPrimitiveValue(*__, **_) -> Never:
    """
    Qt's 'QJSEngine::fromPrimitiveValue': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QJSEngine.fromPrimitiveValue' has no cute function yet. Qt's "
        "'QJSEngine::fromPrimitiveValue': a template: a pattern and no "
        "single function.")

  @staticmethod
  def fromScriptValue(*__, **_) -> Never:
    """
    Qt's 'QJSEngine::fromScriptValue': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QJSEngine.fromScriptValue' has no cute function yet. Qt's "
        "'QJSEngine::fromScriptValue': a template: a pattern and no single "
        "function.")

  @staticmethod
  def fromVariant(*__, **_) -> Never:
    """
    Qt's 'QJSEngine::fromVariant': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QJSEngine.fromVariant' has no cute function yet. Qt's "
        "'QJSEngine::fromVariant': a template: a pattern and no single "
        "function.")

  @staticmethod
  def toManagedValue(*__, **_) -> Never:
    """
    Qt's 'QJSEngine::toManagedValue': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QJSEngine.toManagedValue' has no cute function yet. Qt's "
        "'QJSEngine::toManagedValue': a template: a pattern and no single "
        "function.")

  @staticmethod
  def toPrimitiveValue(*__, **_) -> Never:
    """
    Qt's 'QJSEngine::toPrimitiveValue': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QJSEngine.toPrimitiveValue' has no cute function yet. Qt's "
        "'QJSEngine::toPrimitiveValue': a template: a pattern and no single "
        "function.")

  @staticmethod
  def toScriptValue(*__, **_) -> Never:
    """
    Qt's 'QJSEngine::toScriptValue': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QJSEngine.toScriptValue' has no cute function yet. Qt's "
        "'QJSEngine::toScriptValue': a template: a pattern and no single "
        "function.")
