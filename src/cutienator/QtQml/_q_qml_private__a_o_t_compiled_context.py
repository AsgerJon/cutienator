"""
QQmlPrivate::AOTCompiledContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qqmlprivate.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlPrivate, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDateTime, QMetaObject, QMetaType, QObject, QVariant
  from . import QJSPrimitiveValue, QJSValue, QQmlEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSPrimitiveValue = WAIT['QJSPrimitiveValue']
  QMetaObject = WAIT['QMetaObject']
  QMetaType = WAIT['QMetaType']
  QObject = WAIT['QObject']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AOTCompiledContext(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlPrivate::AOTCompiledContext: a plain Python
  object standing in front of one C++ QQmlPrivate::AOTCompiledContext.

  C++ hands a QQmlPrivate::AOTCompiledContext around as a copy, so every C++
  QQmlPrivate::AOTCompiledContext behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQmlPrivate::AOTCompiledContext that has a ritual
  and that Python can call so far, 34 names in all: 'thisObject',
  'qmlEngine', 'jsMetaType', 'setInstructionPointer', 'setLocals',
  'setReturnValueUndefined', 'mark', 'captureLookup',
  'captureQmlContextPropertyLookup', 'captureTranslation',
  'translationContext', 'lookupResultMetaType', 'javaScriptGlobalProperty',
  'constructDateTime', 'initCallQmlContextPropertyLookup',
  'initLoadContextIdLookup', 'initCallObjectPropertyLookup',
  'initCallObjectPropertyLookupAsVariant', 'initLoadGlobalLookup',
  'initLoadScopeObjectPropertyLookup', 'initLoadSingletonLookup',
  'initLoadAttachedLookup', 'initLoadTypeLookup', 'initGetObjectLookup',
  'initGetObjectLookupAsVariant', 'initGetValueLookup', 'initGetEnumLookup',
  'initSetObjectLookup', 'initSetObjectLookupAsVariant',
  'initSetValueLookup', 'initSetValueLookupAsVariant', 'initCallValueLookup',
  'setObjectImplicitDestructible', 'setImplicitDestructible'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlPrivate::AOTCompiledContext::storeNameSloppy(uint
    nameIndex, void *value, QMetaType type) const': names 'void', which has
    no cute class yet.
  - Qt's 'const QLoggingCategory
    *QQmlPrivate::AOTCompiledContext::resolveLoggingCategory(QObject
    *wrapper, bool *ok) const': takes a number to change where it is.
  - Qt's 'void QQmlPrivate::AOTCompiledContext::writeToConsole(QtMsgType
    type, const QString &message, const QLoggingCategory *loggingCategory)
    const': names the enum 'QtMsgType', whose class cannot be named here.
  - Qt's 'QVariant
    QQmlPrivate::AOTCompiledContext::constructValueType(QMetaType
    resultMetaType, const QMetaObject *resultMetaObject, int ctorIndex, void
    **args) const': takes a type Python has no way to hand over yet.
  - Qt's 'bool
    QQmlPrivate::AOTCompiledContext::callQmlContextPropertyLookup(uint index,
    void **args, int argc) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'bool QQmlPrivate::AOTCompiledContext::loadContextIdLookup(uint
    index, void *target) const': names 'void', which has no cute class yet.
  - Qt's 'bool QQmlPrivate::AOTCompiledContext::callObjectPropertyLookup(uint
    index, QObject *object, void **args, int argc) const': takes a type
    Python has no way to hand over yet.
  - Qt's 'bool QQmlPrivate::AOTCompiledContext::loadGlobalLookup(uint index,
    void *target) const': names 'void', which has no cute class yet.
  - Qt's 'bool
    QQmlPrivate::AOTCompiledContext::loadScopeObjectPropertyLookup(uint
    index, void *target) const': names 'void', which has no cute class yet.
  - Qt's 'bool
    QQmlPrivate::AOTCompiledContext::writeBackScopeObjectPropertyLookup(uint
    index, void *source) const': names 'void', which has no cute class yet.
  - Qt's 'bool QQmlPrivate::AOTCompiledContext::loadSingletonLookup(uint
    index, void *target) const': names 'void', which has no cute class yet.
  - Qt's 'bool QQmlPrivate::AOTCompiledContext::loadAttachedLookup(uint
    index, QObject *object, void *target) const': names 'void', which has no
    cute class yet.
  - Qt's 'bool QQmlPrivate::AOTCompiledContext::loadTypeLookup(uint index,
    void *target) const': names 'void', which has no cute class yet.
  - Qt's 'bool QQmlPrivate::AOTCompiledContext::getObjectLookup(uint index,
    QObject *object, void *target) const': names 'void', which has no cute
    class yet.
  - Qt's 'bool QQmlPrivate::AOTCompiledContext::writeBackObjectLookup(uint
    index, QObject *object, void *source) const': names 'void', which has no
    cute class yet.
  - Qt's 'bool QQmlPrivate::AOTCompiledContext::getValueLookup(uint index,
    void *value, void *target) const': names 'void', which has no cute class
    yet.
  - Qt's 'bool QQmlPrivate::AOTCompiledContext::writeBackValueLookup(uint
    index, void *value, void *source) const': names 'void', which has no cute
    class yet.
  - Qt's 'bool QQmlPrivate::AOTCompiledContext::getEnumLookup(uint index,
    void *target) const': names 'void', which has no cute class yet.
  - Qt's 'bool QQmlPrivate::AOTCompiledContext::setObjectLookup(uint index,
    QObject *object, void *value) const': names 'void', which has no cute
    class yet.
  - Qt's 'bool QQmlPrivate::AOTCompiledContext::setValueLookup(uint index,
    void *target, void *value) const': names 'void', which has no cute class
    yet.
  - Qt's 'bool QQmlPrivate::AOTCompiledContext::callValueLookup(uint index,
    void *target, void **args, int argc) const': names 'void', which has no
    cute class yet.
  - Qt's 'QQmlPrivate::AOTCompiledContext::~AOTCompiledContext()': the
    destructor: Python removes its C++ QQmlPrivate::AOTCompiledContext by it,
    and has no other use for it.

  What has no ritual
  ------------------

  2 of the 63 functions Qt declares: 2 a template.

  What to expect
  --------------

  - The C++ QQmlPrivate::AOTCompiledContext is created at the first use, not
    by 'QQmlPrivate::AOTCompiledContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlPrivate::AOTCompiledContext back gives a copy the
    ritual made for Python, in a new cute QQmlPrivate::AOTCompiledContext.
  - Each name of Qt's QQmlPrivate::AOTCompiledContext that has no cute
    function yet, 'callObjectPropertyLookup', 'callQmlContextPropertyLookup',
    'callValueLookup', 'constructValueType', 'getEnumLookup',
    'getObjectLookup', 'getValueLookup', 'loadAttachedLookup',
    'loadContextIdLookup', 'loadGlobalLookup',
    'loadScopeObjectPropertyLookup', 'loadSingletonLookup', 'loadTypeLookup',
    'resolveLoggingCategory', 'setObjectLookup', 'setValueLookup',
    'storeNameSloppy', 'writeBackObjectLookup',
    'writeBackScopeObjectPropertyLookup', 'writeBackValueLookup',
    'writeToConsole', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QObject, WAIT['QV4.MarkStack'])
  @overload(QObject, NoneType)
  @overload(NoneType, WAIT['QV4.MarkStack'])
  @overload(NoneType, NoneType)
  def mark(
      object: Optional[QObject],
      markStack: Optional[QV4.MarkStack],
  ) -> None:
    """
    Calls Qt's 'void QQmlPrivate::AOTCompiledContext::mark(QObject *object,
    QV4::MarkStack *markStack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html#mark

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    markStack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPrivate::AOTCompiledContext::mark(QObject *object,
    #      QV4::MarkStack *markStack)
    Rituals.call(
        'ritual_ZN11QQmlPrivate18AOTCompiledContext4markEP7QObjectPN3QV49Ma'
        'rkStackE',
        CuteMixin._addressOf(object, 'QObject'),
        CuteMixin._addressOf(markStack),
    )

  @staticmethod
  @overload(QVariant, WAIT['QV4.MarkStack'])
  @overload(QVariant, NoneType)
  def mark(variant: QVariant, markStack: Optional[QV4.MarkStack]) -> None:
    """
    Calls Qt's 'void QQmlPrivate::AOTCompiledContext::mark(const QVariant
    &variant, QV4::MarkStack *markStack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html#mark

    Parameters
    ----------

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    markStack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPrivate::AOTCompiledContext::mark(const QVariant &variant,
    #      QV4::MarkStack *markStack)
    Rituals.call(
        'ritual_ZN11QQmlPrivate18AOTCompiledContext4markERK8QVariantPN3QV49'
        'MarkStackE',
        CuteMixin._valueOf(variant), CuteMixin._addressOf(markStack),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlPrivate::AOTCompiledContext'

  #  Qt's '~QQmlPrivate::AOTCompiledContext()'. Naming it makes this a value
  #  class: Python owns every C++ QQmlPrivate::AOTCompiledContext behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QQmlPrivate18AOTCompiledContextD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def thisObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlPrivate::AOTCompiledContext::thisObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html#thisObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlPrivate::AOTCompiledContext::thisObject() const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext10thisObjectEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def qmlEngine(self) -> Optional[QQmlEngine]:
    """
    Calls Qt's 'QQmlEngine *QQmlPrivate::AOTCompiledContext::qmlEngine()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html#qmlEngine

    Returns
    -------

    Optional[QQmlEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlEngine *QQmlPrivate::AOTCompiledContext::qmlEngine() const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext9qmlEngineEv',
    )
    from . import QQmlEngine
    return QQmlEngine._cuteAt(address)

  @overload(int)
  def jsMetaType(self, index: int) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQmlPrivate::AOTCompiledContext::jsMetaType(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html#jsMetaType

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQmlPrivate::AOTCompiledContext::jsMetaType(int index) const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext10jsMetaTypeEi', index,
    )
    from . import QJSValue
    return QJSValue._cuteOwning(address)

  @overload(int, QObject)
  @overload(int, NoneType)
  def captureLookup(self, index: int, object: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QQmlPrivate::AOTCompiledContext::captureLookup(uint
    index, QObject *object) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html#captureLookup

    Parameters
    ----------

    index : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlPrivate::AOTCompiledContext::captureLookup(uint index,
    #      QObject *object) const
    return self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext13captureLookupEjP7QObj'
        'ect',
        index, self._addressOf(object, 'QObject'),
    )

  @overload(int)
  def captureQmlContextPropertyLookup(self, index: int) -> bool:
    """
    Calls Qt's 'bool
    QQmlPrivate::AOTCompiledContext::captureQmlContextPropertyLookup(uint
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QQmlPrivate::AOTCompiledContext::captureQmlContextPropertyLookup(
    #      uint index) const
    return self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext31captureQmlContextProp'
        'ertyLookupEj',
        index,
    )

  def translationContext(self) -> str:
    """
    Calls Qt's 'QString QQmlPrivate::AOTCompiledContext::translationContext()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlPrivate::AOTCompiledContext::translationContext() const
    return self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext18translationContextEv',
    )

  @overload(int)
  def lookupResultMetaType(self, index: int) -> QMetaType:
    """
    Calls Qt's 'QMetaType
    QQmlPrivate::AOTCompiledContext::lookupResultMetaType(uint index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QQmlPrivate::AOTCompiledContext::lookupResultMetaType(uint
    #      index) const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext20lookupResultMetaTypeE'
        'j',
        index,
    )
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  @overload(int)
  def javaScriptGlobalProperty(self, nameIndex: int) -> QJSValue:
    """
    Calls Qt's 'QJSValue
    QQmlPrivate::AOTCompiledContext::javaScriptGlobalProperty(uint nameIndex)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    nameIndex : int
      Passed on as it is.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue
    #      QQmlPrivate::AOTCompiledContext::javaScriptGlobalProperty(uint
    #      nameIndex) const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext24javaScriptGlobalPrope'
        'rtyEj',
        nameIndex,
    )
    from . import QJSValue
    return QJSValue._cuteOwning(address)

  @overload(float)
  def constructDateTime(self, timestamp: float) -> QDateTime:
    """
    Calls Qt's 'QDateTime
    QQmlPrivate::AOTCompiledContext::constructDateTime(double timestamp)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    timestamp : float
      Passed on as it is.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QQmlPrivate::AOTCompiledContext::constructDateTime(double
    #      timestamp) const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext17constructDateTimeEd',
        timestamp,
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(str)
  def constructDateTime(self, string: str) -> QDateTime:
    """
    Calls Qt's 'QDateTime
    QQmlPrivate::AOTCompiledContext::constructDateTime(const QString &string)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QQmlPrivate::AOTCompiledContext::constructDateTime(const
    #      QString &string) const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext17constructDateTimeERK7'
        'QString',
        string,
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(QJSPrimitiveValue)
  def constructDateTime(self, arg: QJSPrimitiveValue) -> QDateTime:
    """
    Calls Qt's 'QDateTime
    QQmlPrivate::AOTCompiledContext::constructDateTime(const
    QJSPrimitiveValue &arg) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    arg : QJSPrimitiveValue
      Passed on as a value: Qt reads the C++ QJSPrimitiveValue, which stays
      Python's own.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QQmlPrivate::AOTCompiledContext::constructDateTime(const
    #      QJSPrimitiveValue &arg) const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext17constructDateTimeERK1'
        '7QJSPrimitiveValue',
        self._valueOf(arg),
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(float, float)
  @overload(float, float, float)
  @overload(float, float, float, float)
  @overload(float, float, float, float, float)
  @overload(float, float, float, float, float, float)
  @overload(float, float, float, float, float, float, float)
  def constructDateTime(
      self,
      year: float,
      month: float,
      day: float = 1.0,
      hours: float = 0.0,
      minutes: float = 0.0,
      seconds: float = 0.0,
      msecs: float = 0.0,
  ) -> QDateTime:
    """
    Calls Qt's 'QDateTime
    QQmlPrivate::AOTCompiledContext::constructDateTime(double year, double
    month, double day, double hours, double minutes, double seconds, double
    msecs) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    year : float
      Passed on as it is.

    month : float
      Passed on as it is.

    day : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.

    hours : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    minutes : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    seconds : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    msecs : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QQmlPrivate::AOTCompiledContext::constructDateTime(double
    #      year, double month, double day, double hours, double minutes,
    #      double seconds, double msecs) const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext17constructDateTimeEddd'
        'dddd',
        year, month, day, hours, minutes, seconds, msecs,
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setInstructionPointer(self, offset: int) -> None:
    """
    Calls Qt's 'void
    QQmlPrivate::AOTCompiledContext::setInstructionPointer(int offset)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QQmlPrivate::AOTCompiledContext::setInstructionPointer(int
    #      offset) const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext21setInstructionPointer'
        'Ei',
        offset,
    )

  @overload(WAIT['QQmlPrivate.AOTTrackedLocalsStorage'])
  @overload(NoneType)
  def setLocals(
      self,
      locals: Optional[QQmlPrivate.AOTTrackedLocalsStorage],
  ) -> None:
    """
    Calls Qt's 'void QQmlPrivate::AOTCompiledContext::setLocals(const
    AOTTrackedLocalsStorage *locals) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html#setLocals

    Parameters
    ----------

    locals : Optional[QQmlPrivate.AOTTrackedLocalsStorage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPrivate::AOTCompiledContext::setLocals(const
    #      AOTTrackedLocalsStorage *locals) const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext9setLocalsEPKNS_23AOTTr'
        'ackedLocalsStorageE',
        self._addressOf(locals),
    )

  def setReturnValueUndefined(self) -> None:
    """
    Calls Qt's 'void
    QQmlPrivate::AOTCompiledContext::setReturnValueUndefined() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html
    """
    #  void QQmlPrivate::AOTCompiledContext::setReturnValueUndefined() const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext23setReturnValueUndefin'
        'edEv',
    )

  @overload(QObject)
  @overload(NoneType)
  def setObjectImplicitDestructible(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    QQmlPrivate::AOTCompiledContext::setObjectImplicitDestructible(QObject
    *object) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPrivate::AOTCompiledContext::setObjectImplicitDestructible(
    #      QObject *object) const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext29setObjectImplicitDest'
        'ructibleEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(QObject)
  @overload(NoneType)
  def setImplicitDestructible(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    QQmlPrivate::AOTCompiledContext::setImplicitDestructible(QObject *object)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPrivate::AOTCompiledContext::setImplicitDestructible(QObject
    #      *object) const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext23setImplicitDestructib'
        'leEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(QVariant)
  def setImplicitDestructible(self, variant: QVariant) -> None:
    """
    Calls Qt's 'void
    QQmlPrivate::AOTCompiledContext::setImplicitDestructible(const QVariant
    &variant) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlPrivate::AOTCompiledContext::setImplicitDestructible(const
    #      QVariant &variant) const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext23setImplicitDestructib'
        'leERK8QVariant',
        self._valueOf(variant),
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

  def captureTranslation(self) -> None:
    """
    Calls Qt's 'void QQmlPrivate::AOTCompiledContext::captureTranslation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html
    """
    #  void QQmlPrivate::AOTCompiledContext::captureTranslation() const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext18captureTranslationEv',
    )

  @overload(int, int)
  def initCallQmlContextPropertyLookup(
      self,
      index: int,
      relativeMethodIndex: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlPrivate::AOTCompiledContext::initCallQmlContextPropertyLookup(uint
    index, int relativeMethodIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    relativeMethodIndex : int
      Passed on as it is.
    """
    #  void
    #      QQmlPrivate::AOTCompiledContext::initCallQmlContextPropertyLookup(
    #      uint index, int relativeMethodIndex) const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext32initCallQmlContextPro'
        'pertyLookupEji',
        index, relativeMethodIndex,
    )

  @overload(int)
  def initLoadContextIdLookup(self, index: int) -> None:
    """
    Calls Qt's 'void
    QQmlPrivate::AOTCompiledContext::initLoadContextIdLookup(uint index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlPrivate::AOTCompiledContext::initLoadContextIdLookup(uint
    #      index) const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext23initLoadContextIdLook'
        'upEj',
        index,
    )

  @overload(int, QObject, int)
  @overload(int, NoneType, int)
  def initCallObjectPropertyLookup(
      self,
      index: int,
      object: Optional[QObject],
      relativeMethodIndex: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlPrivate::AOTCompiledContext::initCallObjectPropertyLookup(uint index,
    QObject *object, int relativeMethodIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    relativeMethodIndex : int
      Passed on as it is.
    """
    #  void
    #      QQmlPrivate::AOTCompiledContext::initCallObjectPropertyLookup(uint
    #      index, QObject *object, int relativeMethodIndex) const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext28initCallObjectPropert'
        'yLookupEjP7QObjecti',
        index, self._addressOf(object, 'QObject'), relativeMethodIndex,
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def initCallObjectPropertyLookupAsVariant(
      self,
      index: int,
      object: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlPrivate::AOTCompiledContext::initCallObjectPropertyLookupAsVariant(
    uint index, QObject *object) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPrivate::AOTCompiledContext::
    #      initCallObjectPropertyLookupAsVariant(uint index, QObject *object)
    #      const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext37initCallObjectPropert'
        'yLookupAsVariantEjP7QObject',
        index, self._addressOf(object, 'QObject'),
    )

  @overload(int, QMetaType)
  def initLoadGlobalLookup(self, index: int, type: QMetaType) -> None:
    """
    Calls Qt's 'void
    QQmlPrivate::AOTCompiledContext::initLoadGlobalLookup(uint index,
    QMetaType type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    type : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  void QQmlPrivate::AOTCompiledContext::initLoadGlobalLookup(uint index,
    #      QMetaType type) const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext20initLoadGlobalLookupE'
        'j9QMetaType',
        index, self._valueOf(type),
    )

  @overload(int)
  def initLoadScopeObjectPropertyLookup(self, index: int) -> None:
    """
    Calls Qt's 'void
    QQmlPrivate::AOTCompiledContext::initLoadScopeObjectPropertyLookup(uint
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlPrivate::AOTCompiledContext::
    #      initLoadScopeObjectPropertyLookup(uint index) const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext33initLoadScopeObjectPr'
        'opertyLookupEj',
        index,
    )

  @overload(int, int)
  def initLoadSingletonLookup(
      self,
      index: int,
      importNamespace: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlPrivate::AOTCompiledContext::initLoadSingletonLookup(uint index, uint
    importNamespace) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    importNamespace : int
      Passed on as it is.
    """
    #  void QQmlPrivate::AOTCompiledContext::initLoadSingletonLookup(uint
    #      index, uint importNamespace) const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext23initLoadSingletonLook'
        'upEjj',
        index, importNamespace,
    )

  @overload(int, int, QObject)
  @overload(int, int, NoneType)
  def initLoadAttachedLookup(
      self,
      index: int,
      importNamespace: int,
      object: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlPrivate::AOTCompiledContext::initLoadAttachedLookup(uint index, uint
    importNamespace, QObject *object) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    importNamespace : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPrivate::AOTCompiledContext::initLoadAttachedLookup(uint
    #      index, uint importNamespace, QObject *object) const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext22initLoadAttachedLooku'
        'pEjjP7QObject',
        index, importNamespace, self._addressOf(object, 'QObject'),
    )

  @overload(int, int)
  def initLoadTypeLookup(self, index: int, importNamespace: int) -> None:
    """
    Calls Qt's 'void QQmlPrivate::AOTCompiledContext::initLoadTypeLookup(uint
    index, uint importNamespace) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    importNamespace : int
      Passed on as it is.
    """
    #  void QQmlPrivate::AOTCompiledContext::initLoadTypeLookup(uint index,
    #      uint importNamespace) const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext18initLoadTypeLookupEjj',
        index, importNamespace,
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def initGetObjectLookup(
      self,
      index: int,
      object: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlPrivate::AOTCompiledContext::initGetObjectLookup(uint index, QObject
    *object) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPrivate::AOTCompiledContext::initGetObjectLookup(uint index,
    #      QObject *object) const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext19initGetObjectLookupEj'
        'P7QObject',
        index, self._addressOf(object, 'QObject'),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def initGetObjectLookupAsVariant(
      self,
      index: int,
      object: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlPrivate::AOTCompiledContext::initGetObjectLookupAsVariant(uint index,
    QObject *object) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QQmlPrivate::AOTCompiledContext::initGetObjectLookupAsVariant(uint
    #      index, QObject *object) const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext28initGetObjectLookupAs'
        'VariantEjP7QObject',
        index, self._addressOf(object, 'QObject'),
    )

  @overload(int, QMetaObject)
  @overload(int, NoneType)
  def initGetValueLookup(
      self,
      index: int,
      metaObject: Optional[QMetaObject],
  ) -> None:
    """
    Calls Qt's 'void QQmlPrivate::AOTCompiledContext::initGetValueLookup(uint
    index, const QMetaObject *metaObject) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPrivate::AOTCompiledContext::initGetValueLookup(uint index,
    #      const QMetaObject *metaObject) const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext18initGetValueLookupEjP'
        'K11QMetaObject',
        index, self._addressOf(metaObject, 'QMetaObject'),
    )

  @overload(int, QMetaObject, str, str)
  @overload(int, QMetaObject, str, NoneType)
  @overload(int, QMetaObject, NoneType, str)
  @overload(int, QMetaObject, NoneType, NoneType)
  @overload(int, NoneType, str, str)
  @overload(int, NoneType, str, NoneType)
  @overload(int, NoneType, NoneType, str)
  @overload(int, NoneType, NoneType, NoneType)
  def initGetEnumLookup(
      self,
      index: int,
      metaObject: Optional[QMetaObject],
      enumerator: Optional[str],
      enumValue: Optional[str],
  ) -> None:
    """
    Calls Qt's 'void QQmlPrivate::AOTCompiledContext::initGetEnumLookup(uint
    index, const QMetaObject *metaObject, const char *enumerator, const char
    *enumValue) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    enumerator : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    enumValue : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QQmlPrivate::AOTCompiledContext::initGetEnumLookup(uint index,
    #      const QMetaObject *metaObject, const char *enumerator, const char
    #      *enumValue) const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext17initGetEnumLookupEjPK'
        '11QMetaObjectPKcS5_',
        index, self._addressOf(metaObject, 'QMetaObject'),
        self._bytesOf(enumerator), self._bytesOf(enumValue),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def initSetObjectLookup(
      self,
      index: int,
      object: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlPrivate::AOTCompiledContext::initSetObjectLookup(uint index, QObject
    *object) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPrivate::AOTCompiledContext::initSetObjectLookup(uint index,
    #      QObject *object) const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext19initSetObjectLookupEj'
        'P7QObject',
        index, self._addressOf(object, 'QObject'),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def initSetObjectLookupAsVariant(
      self,
      index: int,
      object: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlPrivate::AOTCompiledContext::initSetObjectLookupAsVariant(uint index,
    QObject *object) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QQmlPrivate::AOTCompiledContext::initSetObjectLookupAsVariant(uint
    #      index, QObject *object) const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext28initSetObjectLookupAs'
        'VariantEjP7QObject',
        index, self._addressOf(object, 'QObject'),
    )

  @overload(int, QMetaObject)
  @overload(int, NoneType)
  def initSetValueLookup(
      self,
      index: int,
      metaObject: Optional[QMetaObject],
  ) -> None:
    """
    Calls Qt's 'void QQmlPrivate::AOTCompiledContext::initSetValueLookup(uint
    index, const QMetaObject *metaObject) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPrivate::AOTCompiledContext::initSetValueLookup(uint index,
    #      const QMetaObject *metaObject) const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext18initSetValueLookupEjP'
        'K11QMetaObject',
        index, self._addressOf(metaObject, 'QMetaObject'),
    )

  @overload(int, QMetaObject)
  @overload(int, NoneType)
  def initSetValueLookupAsVariant(
      self,
      index: int,
      metaObject: Optional[QMetaObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlPrivate::AOTCompiledContext::initSetValueLookupAsVariant(uint index,
    const QMetaObject *metaObject) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPrivate::AOTCompiledContext::initSetValueLookupAsVariant(uint
    #      index, const QMetaObject *metaObject) const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext27initSetValueLookupAsV'
        'ariantEjPK11QMetaObject',
        index, self._addressOf(metaObject, 'QMetaObject'),
    )

  @overload(int, QMetaObject, int)
  @overload(int, NoneType, int)
  def initCallValueLookup(
      self,
      index: int,
      metaObject: Optional[QMetaObject],
      relativeMethodIndex: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlPrivate::AOTCompiledContext::initCallValueLookup(uint index, const
    QMetaObject *metaObject, int relativeMethodIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprivate-aotcompiledcontext.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    relativeMethodIndex : int
      Passed on as it is.
    """
    #  void QQmlPrivate::AOTCompiledContext::initCallValueLookup(uint index,
    #      const QMetaObject *metaObject, int relativeMethodIndex) const
    self.uglySide.call(
        'ritual_ZNK11QQmlPrivate18AOTCompiledContext19initCallValueLookupEj'
        'PK11QMetaObjecti',
        index, self._addressOf(metaObject, 'QMetaObject'),
        relativeMethodIndex,
    )

  @staticmethod
  def callObjectPropertyLookup(*__, **_) -> Never:
    """
    Qt's 'bool QQmlPrivate::AOTCompiledContext::callObjectPropertyLookup(uint
    index, QObject *object, void **args, int argc) const': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlPrivate.AOTCompiledContext.callObjectPropertyLookup' has no "
        "cute function yet. Qt's 'bool "
        "QQmlPrivate::AOTCompiledContext::callObjectPropertyLookup(uint "
        "index, QObject *object, void **args, int argc) const': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def callQmlContextPropertyLookup(*__, **_) -> Never:
    """
    Qt's 'bool
    QQmlPrivate::AOTCompiledContext::callQmlContextPropertyLookup(uint index,
    void **args, int argc) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQmlPrivate.AOTCompiledContext.callQmlContextPropertyLookup' has "
        "no cute function yet. Qt's 'bool "
        "QQmlPrivate::AOTCompiledContext::callQmlContextPropertyLookup(uint "
        "index, void **args, int argc) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def callValueLookup(*__, **_) -> Never:
    """
    Qt's 'bool QQmlPrivate::AOTCompiledContext::callValueLookup(uint index,
    void *target, void **args, int argc) const': names 'void', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQmlPrivate.AOTCompiledContext.callValueLookup' has no cute "
        "function yet. Qt's 'bool "
        "QQmlPrivate::AOTCompiledContext::callValueLookup(uint index, void "
        "*target, void **args, int argc) const': names 'void', which has no "
        "cute class yet.")

  @staticmethod
  def constructValueType(*__, **_) -> Never:
    """
    Qt's 'QVariant
    QQmlPrivate::AOTCompiledContext::constructValueType(QMetaType
    resultMetaType, const QMetaObject *resultMetaObject, int ctorIndex, void
    **args) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlPrivate.AOTCompiledContext.constructValueType' has no cute "
        "function yet. Qt's 'QVariant "
        "QQmlPrivate::AOTCompiledContext::constructValueType(QMetaType "
        "resultMetaType, const QMetaObject *resultMetaObject, int "
        "ctorIndex, void **args) const': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def getEnumLookup(*__, **_) -> Never:
    """
    Qt's 'bool QQmlPrivate::AOTCompiledContext::getEnumLookup(uint index,
    void *target) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlPrivate.AOTCompiledContext.getEnumLookup' has no cute "
        "function yet. Qt's 'bool "
        "QQmlPrivate::AOTCompiledContext::getEnumLookup(uint index, void "
        "*target) const': names 'void', which has no cute class yet.")

  @staticmethod
  def getObjectLookup(*__, **_) -> Never:
    """
    Qt's 'bool QQmlPrivate::AOTCompiledContext::getObjectLookup(uint index,
    QObject *object, void *target) const': names 'void', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQmlPrivate.AOTCompiledContext.getObjectLookup' has no cute "
        "function yet. Qt's 'bool "
        "QQmlPrivate::AOTCompiledContext::getObjectLookup(uint index, "
        "QObject *object, void *target) const': names 'void', which has no "
        "cute class yet.")

  @staticmethod
  def getValueLookup(*__, **_) -> Never:
    """
    Qt's 'bool QQmlPrivate::AOTCompiledContext::getValueLookup(uint index,
    void *value, void *target) const': names 'void', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQmlPrivate.AOTCompiledContext.getValueLookup' has no cute "
        "function yet. Qt's 'bool "
        "QQmlPrivate::AOTCompiledContext::getValueLookup(uint index, void "
        "*value, void *target) const': names 'void', which has no cute "
        "class yet.")

  @staticmethod
  def loadAttachedLookup(*__, **_) -> Never:
    """
    Qt's 'bool QQmlPrivate::AOTCompiledContext::loadAttachedLookup(uint
    index, QObject *object, void *target) const': names 'void', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQmlPrivate.AOTCompiledContext.loadAttachedLookup' has no cute "
        "function yet. Qt's 'bool "
        "QQmlPrivate::AOTCompiledContext::loadAttachedLookup(uint index, "
        "QObject *object, void *target) const': names 'void', which has no "
        "cute class yet.")

  @staticmethod
  def loadContextIdLookup(*__, **_) -> Never:
    """
    Qt's 'bool QQmlPrivate::AOTCompiledContext::loadContextIdLookup(uint
    index, void *target) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlPrivate.AOTCompiledContext.loadContextIdLookup' has no cute "
        "function yet. Qt's 'bool "
        "QQmlPrivate::AOTCompiledContext::loadContextIdLookup(uint index, "
        "void *target) const': names 'void', which has no cute class yet.")

  @staticmethod
  def loadGlobalLookup(*__, **_) -> Never:
    """
    Qt's 'bool QQmlPrivate::AOTCompiledContext::loadGlobalLookup(uint index,
    void *target) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlPrivate.AOTCompiledContext.loadGlobalLookup' has no cute "
        "function yet. Qt's 'bool "
        "QQmlPrivate::AOTCompiledContext::loadGlobalLookup(uint index, void "
        "*target) const': names 'void', which has no cute class yet.")

  @staticmethod
  def loadScopeObjectPropertyLookup(*__, **_) -> Never:
    """
    Qt's 'bool
    QQmlPrivate::AOTCompiledContext::loadScopeObjectPropertyLookup(uint
    index, void *target) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlPrivate.AOTCompiledContext.loadScopeObjectPropertyLookup' has "
        "no cute function yet. Qt's 'bool "
        "QQmlPrivate::AOTCompiledContext::loadScopeObjectPropertyLookup(uint"
        " index, void *target) const': names 'void', which has no cute "
        "class yet.")

  @staticmethod
  def loadSingletonLookup(*__, **_) -> Never:
    """
    Qt's 'bool QQmlPrivate::AOTCompiledContext::loadSingletonLookup(uint
    index, void *target) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlPrivate.AOTCompiledContext.loadSingletonLookup' has no cute "
        "function yet. Qt's 'bool "
        "QQmlPrivate::AOTCompiledContext::loadSingletonLookup(uint index, "
        "void *target) const': names 'void', which has no cute class yet.")

  @staticmethod
  def loadTypeLookup(*__, **_) -> Never:
    """
    Qt's 'bool QQmlPrivate::AOTCompiledContext::loadTypeLookup(uint index,
    void *target) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlPrivate.AOTCompiledContext.loadTypeLookup' has no cute "
        "function yet. Qt's 'bool "
        "QQmlPrivate::AOTCompiledContext::loadTypeLookup(uint index, void "
        "*target) const': names 'void', which has no cute class yet.")

  @staticmethod
  def resolveLoggingCategory(*__, **_) -> Never:
    """
    Qt's 'const QLoggingCategory
    *QQmlPrivate::AOTCompiledContext::resolveLoggingCategory(QObject
    *wrapper, bool *ok) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQmlPrivate.AOTCompiledContext.resolveLoggingCategory' has no "
        "cute function yet. Qt's 'const QLoggingCategory "
        "*QQmlPrivate::AOTCompiledContext::resolveLoggingCategory(QObject "
        "*wrapper, bool *ok) const': takes a number to change where it is.")

  @staticmethod
  def setObjectLookup(*__, **_) -> Never:
    """
    Qt's 'bool QQmlPrivate::AOTCompiledContext::setObjectLookup(uint index,
    QObject *object, void *value) const': names 'void', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQmlPrivate.AOTCompiledContext.setObjectLookup' has no cute "
        "function yet. Qt's 'bool "
        "QQmlPrivate::AOTCompiledContext::setObjectLookup(uint index, "
        "QObject *object, void *value) const': names 'void', which has no "
        "cute class yet.")

  @staticmethod
  def setValueLookup(*__, **_) -> Never:
    """
    Qt's 'bool QQmlPrivate::AOTCompiledContext::setValueLookup(uint index,
    void *target, void *value) const': names 'void', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQmlPrivate.AOTCompiledContext.setValueLookup' has no cute "
        "function yet. Qt's 'bool "
        "QQmlPrivate::AOTCompiledContext::setValueLookup(uint index, void "
        "*target, void *value) const': names 'void', which has no cute "
        "class yet.")

  @staticmethod
  def storeNameSloppy(*__, **_) -> Never:
    """
    Qt's 'void QQmlPrivate::AOTCompiledContext::storeNameSloppy(uint
    nameIndex, void *value, QMetaType type) const': names 'void', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlPrivate.AOTCompiledContext.storeNameSloppy' has no cute "
        "function yet. Qt's 'void "
        "QQmlPrivate::AOTCompiledContext::storeNameSloppy(uint nameIndex, "
        "void *value, QMetaType type) const': names 'void', which has no "
        "cute class yet.")

  @staticmethod
  def writeBackObjectLookup(*__, **_) -> Never:
    """
    Qt's 'bool QQmlPrivate::AOTCompiledContext::writeBackObjectLookup(uint
    index, QObject *object, void *source) const': names 'void', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQmlPrivate.AOTCompiledContext.writeBackObjectLookup' has no cute "
        "function yet. Qt's 'bool "
        "QQmlPrivate::AOTCompiledContext::writeBackObjectLookup(uint index, "
        "QObject *object, void *source) const': names 'void', which has no "
        "cute class yet.")

  @staticmethod
  def writeBackScopeObjectPropertyLookup(*__, **_) -> Never:
    """
    Qt's 'bool
    QQmlPrivate::AOTCompiledContext::writeBackScopeObjectPropertyLookup(uint
    index, void *source) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlPrivate.AOTCompiledContext.writeBackScopeObjectPropertyLookup'"
        " has no cute function yet. Qt's 'bool "
        "QQmlPrivate::AOTCompiledContext::writeBackScopeObjectPropertyLookup"
        "(uint index, void *source) const': names 'void', which has no cute "
        "class yet.")

  @staticmethod
  def writeBackValueLookup(*__, **_) -> Never:
    """
    Qt's 'bool QQmlPrivate::AOTCompiledContext::writeBackValueLookup(uint
    index, void *value, void *source) const': names 'void', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQmlPrivate.AOTCompiledContext.writeBackValueLookup' has no cute "
        "function yet. Qt's 'bool "
        "QQmlPrivate::AOTCompiledContext::writeBackValueLookup(uint index, "
        "void *value, void *source) const': names 'void', which has no cute "
        "class yet.")

  @staticmethod
  def writeToConsole(*__, **_) -> Never:
    """
    Qt's 'void QQmlPrivate::AOTCompiledContext::writeToConsole(QtMsgType
    type, const QString &message, const QLoggingCategory *loggingCategory)
    const': names the enum 'QtMsgType', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QQmlPrivate.AOTCompiledContext.writeToConsole' has no cute "
        "function yet. Qt's 'void "
        "QQmlPrivate::AOTCompiledContext::writeToConsole(QtMsgType type, "
        "const QString &message, const QLoggingCategory *loggingCategory) "
        "const': names the enum 'QtMsgType', whose class cannot be named "
        "here.")
