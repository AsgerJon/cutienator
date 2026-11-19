"""
QMetaMethod binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmetaobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ._qt import Qt
from ._q_byte_array import QByteArray
from ._q_byte_array_view import QByteArrayView
from ._q_meta_object import QMetaObject
from ._q_meta_method_access import Access
from ._q_meta_method_attributes import Attributes
from ._q_meta_method_method_type import MethodType

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QMetaMethod(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMetaMethod: a plain Python object standing in front
  of one C++ QMetaMethod.

  C++ hands a QMetaMethod around as a copy, so every C++ QMetaMethod behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMetaMethod that has a ritual and that Python can
  call so far, 18 names in all: 'methodSignature', 'name', 'nameView',
  'typeName', 'returnType', 'parameterCount', 'parameterType',
  'parameterTypeName', 'tag', 'access', 'methodType', 'attributes',
  'methodIndex', 'relativeMethodIndex', 'revision', 'isConst',
  'enclosingMetaObject', 'isValid'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMetaType QMetaMethod::returnMetaType() const': gives 'QMetaType',
    which has no cute class yet.
  - Qt's 'QMetaType QMetaMethod::parameterMetaType(int index) const': gives
    'QMetaType', which has no cute class yet.
  - Qt's 'void QMetaMethod::getParameterTypes(int *types) const': takes a
    number to change where it is.
  - Qt's 'bool QMetaMethod::invoke(QObject *object, Qt::ConnectionType
    connectionType, QGenericReturnArgument returnValue, QGenericArgument
    val0, QGenericArgument val1, QGenericArgument val2, QGenericArgument
    val3, QGenericArgument val4, QGenericArgument val5, QGenericArgument
    val6, QGenericArgument val7, QGenericArgument val8, QGenericArgument
    val9) const': names 'QGenericReturnArgument', which has no cute class
    yet.
  - Qt's 'bool QMetaMethod::invoke(QObject *object, QGenericReturnArgument
    returnValue, QGenericArgument val0, QGenericArgument val1,
    QGenericArgument val2, QGenericArgument val3, QGenericArgument val4,
    QGenericArgument val5, QGenericArgument val6, QGenericArgument val7,
    QGenericArgument val8, QGenericArgument val9) const': names
    'QGenericReturnArgument', which has no cute class yet.
  - Qt's 'bool QMetaMethod::invoke(QObject *object, Qt::ConnectionType
    connectionType, QGenericArgument val0, QGenericArgument val1,
    QGenericArgument val2, QGenericArgument val3, QGenericArgument val4,
    QGenericArgument val5, QGenericArgument val6, QGenericArgument val7,
    QGenericArgument val8, QGenericArgument val9) const': names
    'QGenericArgument', which has no cute class yet.
  - Qt's 'bool QMetaMethod::invoke(QObject *object, QGenericArgument val0,
    QGenericArgument val1, QGenericArgument val2, QGenericArgument val3,
    QGenericArgument val4, QGenericArgument val5, QGenericArgument val6,
    QGenericArgument val7, QGenericArgument val8, QGenericArgument val9)
    const': names 'QGenericArgument', which has no cute class yet.
  - Qt's 'QMetaMethod::~QMetaMethod()': the destructor: Python removes its
    C++ QMetaMethod by it, and has no other use for it.

  What has no ritual
  ------------------

  16 of the 43 functions Qt declares: 7 a template; 5 private; 4 takes or
  gives a type that cannot be passed yet.

  What to expect
  --------------

  - The C++ QMetaMethod is created at the first use, not by
    'QMetaMethod(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMetaMethod back gives a copy the ritual made for
    Python, in a new cute QMetaMethod.
  """

  #  The enums Qt writes inside QMetaMethod, and the names Qt has for the
  #  combinations of its flags enums.
  Access = Access
  Attributes = Attributes
  MethodType = MethodType

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMetaMethod'

  #  Qt's '~QMetaMethod()'. Naming it makes this a value class: Python owns
  #  every C++ QMetaMethod behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QMetaMethodD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def methodSignature(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMetaMethod::methodSignature() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#methodSignature

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMetaMethod::methodSignature() const
    address = self.uglySide.call(
        'ritual_ZNK11QMetaMethod15methodSignatureEv',
    )
    return QByteArray._cuteOwning(address)

  def name(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMetaMethod::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#name

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMetaMethod::name() const
    address = self.uglySide.call('ritual_ZNK11QMetaMethod4nameEv')
    return QByteArray._cuteOwning(address)

  def nameView(self) -> QByteArrayView:
    """
    Calls Qt's 'QByteArrayView QMetaMethod::nameView() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#nameView

    Returns
    -------

    QByteArrayView
      A new cute QByteArrayView around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayView QMetaMethod::nameView() const
    address = self.uglySide.call('ritual_ZNK11QMetaMethod8nameViewEv')
    return QByteArrayView._cuteOwning(address)

  def typeName(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QMetaMethod::typeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#typeName

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QMetaMethod::typeName() const
    chars = self.uglySide.call('ritual_ZNK11QMetaMethod8typeNameEv')
    return None if chars is None else chars.decode()

  def returnType(self) -> int:
    """
    Calls Qt's 'int QMetaMethod::returnType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#returnType
    """
    #  int QMetaMethod::returnType() const
    return self.uglySide.call('ritual_ZNK11QMetaMethod10returnTypeEv')

  def parameterCount(self) -> int:
    """
    Calls Qt's 'int QMetaMethod::parameterCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#parameterCount
    """
    #  int QMetaMethod::parameterCount() const
    return self.uglySide.call('ritual_ZNK11QMetaMethod14parameterCountEv')

  @overload(int)
  def parameterType(self, index: int) -> int:
    """
    Calls Qt's 'int QMetaMethod::parameterType(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#parameterType

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QMetaMethod::parameterType(int index) const
    return self.uglySide.call(
        'ritual_ZNK11QMetaMethod13parameterTypeEi', index,
    )

  @overload(int)
  def parameterTypeName(self, index: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMetaMethod::parameterTypeName(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#parameterTypeName

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMetaMethod::parameterTypeName(int index) const
    address = self.uglySide.call(
        'ritual_ZNK11QMetaMethod17parameterTypeNameEi', index,
    )
    return QByteArray._cuteOwning(address)

  def tag(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QMetaMethod::tag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#tag

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QMetaMethod::tag() const
    chars = self.uglySide.call('ritual_ZNK11QMetaMethod3tagEv')
    return None if chars is None else chars.decode()

  def access(self) -> Access:
    """
    Calls Qt's 'Access QMetaMethod::access() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#access

    Returns
    -------

    Access
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Access(number)' gives.
    """
    #  Access QMetaMethod::access() const
    return Access(self.uglySide.call('ritual_ZNK11QMetaMethod6accessEv'))

  def methodType(self) -> MethodType:
    """
    Calls Qt's 'MethodType QMetaMethod::methodType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#methodType

    Returns
    -------

    MethodType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MethodType(number)'
      gives.
    """
    #  MethodType QMetaMethod::methodType() const
    return MethodType(self.uglySide.call(
        'ritual_ZNK11QMetaMethod10methodTypeEv',
    ))

  def attributes(self) -> int:
    """
    Calls Qt's 'int QMetaMethod::attributes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#attributes
    """
    #  int QMetaMethod::attributes() const
    return self.uglySide.call('ritual_ZNK11QMetaMethod10attributesEv')

  def methodIndex(self) -> int:
    """
    Calls Qt's 'int QMetaMethod::methodIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#methodIndex
    """
    #  int QMetaMethod::methodIndex() const
    return self.uglySide.call('ritual_ZNK11QMetaMethod11methodIndexEv')

  def relativeMethodIndex(self) -> int:
    """
    Calls Qt's 'int QMetaMethod::relativeMethodIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetamethod.html#relativeMethodIndex
    """
    #  int QMetaMethod::relativeMethodIndex() const
    return self.uglySide.call(
        'ritual_ZNK11QMetaMethod19relativeMethodIndexEv',
    )

  def revision(self) -> int:
    """
    Calls Qt's 'int QMetaMethod::revision() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#revision
    """
    #  int QMetaMethod::revision() const
    return self.uglySide.call('ritual_ZNK11QMetaMethod8revisionEv')

  def isConst(self) -> bool:
    """
    Calls Qt's 'bool QMetaMethod::isConst() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#isConst
    """
    #  bool QMetaMethod::isConst() const
    return self.uglySide.call('ritual_ZNK11QMetaMethod7isConstEv')

  def enclosingMetaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMetaMethod::enclosingMetaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetamethod.html#enclosingMetaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMetaMethod::enclosingMetaObject() const
    address = self.uglySide.call(
        'ritual_ZNK11QMetaMethod19enclosingMetaObjectEv',
    )
    return QMetaObject._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QMetaMethod::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#isValid
    """
    #  bool QMetaMethod::isValid() const
    return self.uglySide.call('ritual_ZNK11QMetaMethod7isValidEv')

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QMetaMethod::QMetaMethod()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#QMetaMethod
    """
    #  QMetaMethod::QMetaMethod()
    self._noteCreation(QMetaMethod, lambda: Rituals.call(
        'ritual_ZN11QMetaMethodC1Ev',
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
