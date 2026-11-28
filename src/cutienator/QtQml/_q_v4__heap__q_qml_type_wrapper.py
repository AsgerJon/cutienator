"""
QV4::Heap::QQmlTypeWrapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltypewrapper_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Heap::QQmlTypeWrapper to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from . import QQmlTypeNameCache, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QMetaType, QObject
  from . import QQmlImportRef, QQmlType, QQmlTypePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlImportRef = WAIT['QQmlImportRef']
  QQmlTypePrivate = WAIT['QQmlTypePrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlTypeWrapper(QV4.Heap.FunctionObject):
  """
  The cute side of Qt's QV4::Heap::QQmlTypeWrapper: a plain Python object
  standing in front of one C++ QV4::Heap::QQmlTypeWrapper.

  It is built on the cute 'QV4::Heap::FunctionObject', as Qt's
  QV4::Heap::QQmlTypeWrapper is built on Qt's QV4::Heap::FunctionObject, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::QQmlTypeWrapper that has a ritual and
  that Python can call so far, 8 names in all: 'init', 'destroy',
  'metaObject', 'metaType', 'type', 'typeNameMode', 'kind', 'queryNamespace'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QQmlPropertyData.

  What to expect
  --------------

  - The C++ QV4::Heap::QQmlTypeWrapper is created at the first use, not by
    'QV4::Heap::QQmlTypeWrapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::QQmlTypeWrapper.
  - Each name of Qt's QV4::Heap::QQmlTypeWrapper that has no cute function
    yet, 'ensureConstructorsCache', 'warnIfUncreatable', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QV4::Heap::QQmlTypeWrapper, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Kind(CuteNum):
    """
    The enum 'QV4::Heap::QQmlTypeWrapper::Kind' of Qt, with the 3 names Qt
    gives in it.
    """

    Type = Kee[int](0)
    Namespace = Kee[int](2)
    KindMask = Kee[int](2)

  class TypeNameMode(CuteNum):
    """
    The enum 'QV4::Heap::QQmlTypeWrapper::TypeNameMode' of Qt, with the 3
    names Qt gives in it.
    """

    ExcludeEnums = Kee[int](0)
    IncludeEnums = Kee[int](1)
    TypeNameModeMask = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::QQmlTypeWrapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QV4::Heap::QQmlTypeWrapper::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qqmltypewrapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QV4::Heap::QQmlTypeWrapper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap15QQmlTypeWrapper10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def metaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QV4::Heap::QQmlTypeWrapper::metaType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qqmltypewrapper.html#metaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QV4::Heap::QQmlTypeWrapper::metaType() const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap15QQmlTypeWrapper8metaTypeEv',
    )
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  def type(self) -> QQmlType:
    """
    Calls Qt's 'QQmlType QV4::Heap::QQmlTypeWrapper::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-qqmltypewrapper.html#type

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QV4::Heap::QQmlTypeWrapper::type() const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap15QQmlTypeWrapper4typeEv',
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  def typeNameMode(self) -> TypeNameMode:
    """
    Calls Qt's 'TypeNameMode QV4::Heap::QQmlTypeWrapper::typeNameMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qqmltypewrapper.html#typeNameMode

    Returns
    -------

    TypeNameMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TypeNameMode(number)'
      gives.
    """
    #  TypeNameMode QV4::Heap::QQmlTypeWrapper::typeNameMode() const
    return QQmlTypeWrapper.TypeNameMode(self.uglySide.call(
        'ritual_ZNK3QV44Heap15QQmlTypeWrapper12typeNameModeEv',
    ))

  def kind(self) -> Kind:
    """
    Calls Qt's 'Kind QV4::Heap::QQmlTypeWrapper::kind() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-qqmltypewrapper.html#kind

    Returns
    -------

    Kind
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Kind(number)' gives.
    """
    #  Kind QV4::Heap::QQmlTypeWrapper::kind() const
    return QQmlTypeWrapper.Kind(self.uglySide.call(
        'ritual_ZNK3QV44Heap15QQmlTypeWrapper4kindEv',
    ))

  @overload(WAIT['QV4.String'], WAIT['QV4.ExecutionEngine'])
  @overload(WAIT['QV4.String'], NoneType)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'])
  @overload(NoneType, NoneType)
  def queryNamespace(
      self,
      name: Optional[QV4.String],
      engine: Optional[QV4.ExecutionEngine],
  ) -> QQmlTypeNameCache.Result:
    """
    Calls Qt's 'QQmlTypeNameCache::Result
    QV4::Heap::QQmlTypeWrapper::queryNamespace(const QV4::String *name,
    QV4::ExecutionEngine *engine) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qqmltypewrapper.html#queryNamespace

    Parameters
    ----------

    name : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQmlTypeNameCache.Result
      A new cute QQmlTypeNameCache::Result around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlTypeNameCache::Result
    #      QV4::Heap::QQmlTypeWrapper::queryNamespace(const QV4::String
    #      *name, QV4::ExecutionEngine *engine) const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap15QQmlTypeWrapper14queryNamespaceEPKNS_6StringE'
        'PNS_15ExecutionEngineE',
        self._addressOf(name), self._addressOf(engine),
    )
    return QQmlTypeNameCache.Result._cuteOwning(address)

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

  @overload(TypeNameMode, QObject, QQmlTypePrivate)
  @overload(TypeNameMode, QObject, NoneType)
  @overload(TypeNameMode, NoneType, QQmlTypePrivate)
  @overload(TypeNameMode, NoneType, NoneType)
  def init(
      self,
      m: TypeNameMode,
      o: Optional[QObject],
      type: Optional[QQmlTypePrivate],
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::QQmlTypeWrapper::init(TypeNameMode m, QObject
    *o, const QQmlTypePrivate *type)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-qqmltypewrapper.html#init

    Parameters
    ----------

    m : TypeNameMode
      Passed on as its number.

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : Optional[QQmlTypePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::QQmlTypeWrapper::init(TypeNameMode m, QObject *o,
    #      const QQmlTypePrivate *type)
    self.uglySide.call(
        'ritual_ZN3QV44Heap15QQmlTypeWrapper4initENS1_12TypeNameModeEP7QObj'
        'ectPK15QQmlTypePrivate',
        m.value, self._addressOf(o, 'QObject'), self._addressOf(type),
    )

  @overload(TypeNameMode, QObject, QQmlTypeNameCache, QQmlImportRef)
  @overload(TypeNameMode, QObject, QQmlTypeNameCache, NoneType)
  @overload(TypeNameMode, QObject, NoneType, QQmlImportRef)
  @overload(TypeNameMode, QObject, NoneType, NoneType)
  @overload(TypeNameMode, NoneType, QQmlTypeNameCache, QQmlImportRef)
  @overload(TypeNameMode, NoneType, QQmlTypeNameCache, NoneType)
  @overload(TypeNameMode, NoneType, NoneType, QQmlImportRef)
  @overload(TypeNameMode, NoneType, NoneType, NoneType)
  def init(
      self,
      m: TypeNameMode,
      o: Optional[QObject],
      type: Optional[QQmlTypeNameCache],
      import_: Optional[QQmlImportRef],
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::QQmlTypeWrapper::init(TypeNameMode m, QObject
    *o, QQmlTypeNameCache *type, const QQmlImportRef *import)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-qqmltypewrapper.html#init

    Parameters
    ----------

    m : TypeNameMode
      Passed on as its number.

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : Optional[QQmlTypeNameCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    import_ : Optional[QQmlImportRef]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::QQmlTypeWrapper::init(TypeNameMode m, QObject *o,
    #      QQmlTypeNameCache *type, const QQmlImportRef *import)
    self.uglySide.call(
        'ritual_ZN3QV44Heap15QQmlTypeWrapper4initENS1_12TypeNameModeEP7QObj'
        'ectP17QQmlTypeNameCachePK13QQmlImportRef',
        m.value, self._addressOf(o, 'QObject'), self._addressOf(type),
        self._addressOf(import_),
    )

  def destroy(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::QQmlTypeWrapper::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qqmltypewrapper.html#destroy
    """
    #  void QV4::Heap::QQmlTypeWrapper::destroy()
    self.uglySide.call('ritual_ZN3QV44Heap15QQmlTypeWrapper7destroyEv')

  @staticmethod
  def ensureConstructorsCache(*__, **_) -> Never:
    """
    Qt's 'const QQmlPropertyData
    *QV4::Heap::QQmlTypeWrapper::ensureConstructorsCache(const QMetaObject
    *metaObject, QMetaType metaType)': leans on
    'QQmlPropertyData::load(QMetaMethod const&)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Heap.QQmlTypeWrapper.ensureConstructorsCache' has no cute "
        "function yet. Qt's 'const QQmlPropertyData "
        "*QV4::Heap::QQmlTypeWrapper::ensureConstructorsCache(const "
        "QMetaObject *metaObject, QMetaType metaType)': leans on "
        "'QQmlPropertyData::load(QMetaMethod const&)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def warnIfUncreatable(*__, **_) -> Never:
    """
    Qt's 'void QV4::Heap::QQmlTypeWrapper::warnIfUncreatable() const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'warnWithLocation'.
    """
    raise NotImplementedError(
        "'QV4.Heap.QQmlTypeWrapper.warnIfUncreatable' has no cute function "
        "yet. Qt's 'void QV4::Heap::QQmlTypeWrapper::warnIfUncreatable() "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'warnWithLocation'.")
