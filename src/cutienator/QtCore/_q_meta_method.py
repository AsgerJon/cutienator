"""
QMetaMethod binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmetaobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QByteArrayView, QGenericArgument
  from . import QGenericReturnArgument, QMetaObject, QMetaType, QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGenericArgument = WAIT['QGenericArgument']
  QGenericReturnArgument = WAIT['QGenericReturnArgument']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


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
  call so far, 23 names in all: 'methodSignature', 'name', 'nameView',
  'typeName', 'returnType', 'returnMetaType', 'parameterCount',
  'parameterType', 'parameterMetaType', 'parameterTypeName', 'tag', 'access',
  'methodType', 'attributes', 'methodIndex', 'relativeMethodIndex',
  'revision', 'isConst', 'enclosingMetaObject', 'invoke', 'isValid',
  '__eq__', '__ne__'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QMetaMethod::getParameterTypes(int *types) const': takes a
    number to change where it is.
  - Qt's 'QMetaMethod::~QMetaMethod()': the destructor: Python removes its
    C++ QMetaMethod by it, and has no other use for it.

  What has no ritual
  ------------------

  16 of the 45 functions Qt declares: 7 a template; 5 private; 4 takes or
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

  #  The enums Qt writes inside QMetaMethod, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Access(CuteNum):
    """
    The enum 'QMetaMethod::Access' of Qt, with the 3 names Qt gives in it.
    """

    Private = Kee[int](0)
    Protected = Kee[int](1)
    Public = Kee[int](2)

  class Attributes(CuteNum):
    """
    The enum 'QMetaMethod::Attributes' of Qt, with the 3 names Qt gives in
    it.
    """

    Compatibility = Kee[int](1)
    Cloned = Kee[int](2)
    Scriptable = Kee[int](4)

  class MethodType(CuteNum):
    """
    The enum 'QMetaMethod::MethodType' of Qt, with the 4 names Qt gives in
    it.
    """

    Method = Kee[int](0)
    Signal = Kee[int](1)
    Slot = Kee[int](2)
    Constructor = Kee[int](3)

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
    from . import QByteArray
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
    from . import QByteArray
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
    from . import QByteArrayView
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

  def returnMetaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QMetaMethod::returnMetaType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#returnMetaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QMetaMethod::returnMetaType() const
    address = self.uglySide.call('ritual_ZNK11QMetaMethod14returnMetaTypeEv')
    from . import QMetaType
    return QMetaType._cuteOwning(address)

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
  def parameterMetaType(self, index: int) -> QMetaType:
    """
    Calls Qt's 'QMetaType QMetaMethod::parameterMetaType(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#parameterMetaType

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QMetaMethod::parameterMetaType(int index) const
    address = self.uglySide.call(
        'ritual_ZNK11QMetaMethod17parameterMetaTypeEi', index,
    )
    from . import QMetaType
    return QMetaType._cuteOwning(address)

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
    from . import QByteArray
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
    return QMetaMethod.Access(self.uglySide.call(
        'ritual_ZNK11QMetaMethod6accessEv',
    ))

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
    return QMetaMethod.MethodType(self.uglySide.call(
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
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(
      QObject, Qt.ConnectionType, QGenericReturnArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument,
  )
  @overload(
      NoneType, Qt.ConnectionType, QGenericReturnArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument,
  )
  def invoke(
      self,
      object: Optional[QObject],
      connectionType: Qt.ConnectionType,
      returnValue: QGenericReturnArgument,
      val0: QGenericArgument,
      val1: QGenericArgument,
      val2: QGenericArgument,
      val3: QGenericArgument,
      val4: QGenericArgument,
      val5: QGenericArgument,
      val6: QGenericArgument,
      val7: QGenericArgument,
      val8: QGenericArgument,
      val9: QGenericArgument,
  ) -> bool:
    """
    Calls Qt's 'bool QMetaMethod::invoke(QObject *object, Qt::ConnectionType
    connectionType, QGenericReturnArgument returnValue, QGenericArgument
    val0, QGenericArgument val1, QGenericArgument val2, QGenericArgument
    val3, QGenericArgument val4, QGenericArgument val5, QGenericArgument
    val6, QGenericArgument val7, QGenericArgument val8, QGenericArgument
    val9) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#invoke

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    connectionType : Qt.ConnectionType
      Passed on as its number.

    returnValue : QGenericReturnArgument
      Passed on as a value: Qt reads the C++ QGenericReturnArgument, which
      stays Python's own.

    val0 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val1 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val2 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val3 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val4 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val5 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val6 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val7 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val8 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val9 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.
    """
    #  bool QMetaMethod::invoke(QObject *object, Qt::ConnectionType
    #      connectionType, QGenericReturnArgument returnValue,
    #      QGenericArgument val0, QGenericArgument val1, QGenericArgument
    #      val2, QGenericArgument val3, QGenericArgument val4,
    #      QGenericArgument val5, QGenericArgument val6, QGenericArgument
    #      val7, QGenericArgument val8, QGenericArgument val9) const
    return self.uglySide.call(
        'ritual_ZNK11QMetaMethod6invokeEP7QObjectN2Qt14ConnectionTypeE22QGe'
        'nericReturnArgument16QGenericArgumentS5_S5_S5_S5_S5_S5_S5_S5_S5_',
        self._addressOf(object), connectionType.value,
        self._valueOf(returnValue), self._valueOf(val0), self._valueOf(val1),
        self._valueOf(val2), self._valueOf(val3), self._valueOf(val4),
        self._valueOf(val5), self._valueOf(val6), self._valueOf(val7),
        self._valueOf(val8), self._valueOf(val9),
    )

  @overload(
      QObject, QGenericReturnArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
  )
  @overload(
      NoneType, QGenericReturnArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
  )
  def invoke(
      self,
      object: Optional[QObject],
      returnValue: QGenericReturnArgument,
      val0: QGenericArgument,
      val1: QGenericArgument,
      val2: QGenericArgument,
      val3: QGenericArgument,
      val4: QGenericArgument,
      val5: QGenericArgument,
      val6: QGenericArgument,
      val7: QGenericArgument,
      val8: QGenericArgument,
      val9: QGenericArgument,
  ) -> bool:
    """
    Calls Qt's 'bool QMetaMethod::invoke(QObject *object,
    QGenericReturnArgument returnValue, QGenericArgument val0,
    QGenericArgument val1, QGenericArgument val2, QGenericArgument val3,
    QGenericArgument val4, QGenericArgument val5, QGenericArgument val6,
    QGenericArgument val7, QGenericArgument val8, QGenericArgument val9)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#invoke

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    returnValue : QGenericReturnArgument
      Passed on as a value: Qt reads the C++ QGenericReturnArgument, which
      stays Python's own.

    val0 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val1 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val2 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val3 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val4 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val5 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val6 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val7 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val8 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val9 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.
    """
    #  bool QMetaMethod::invoke(QObject *object, QGenericReturnArgument
    #      returnValue, QGenericArgument val0, QGenericArgument val1,
    #      QGenericArgument val2, QGenericArgument val3, QGenericArgument
    #      val4, QGenericArgument val5, QGenericArgument val6,
    #      QGenericArgument val7, QGenericArgument val8, QGenericArgument
    #      val9) const
    return self.uglySide.call(
        'ritual_ZNK11QMetaMethod6invokeEP7QObject22QGenericReturnArgument16'
        'QGenericArgumentS3_S3_S3_S3_S3_S3_S3_S3_S3_',
        self._addressOf(object), self._valueOf(returnValue),
        self._valueOf(val0), self._valueOf(val1), self._valueOf(val2),
        self._valueOf(val3), self._valueOf(val4), self._valueOf(val5),
        self._valueOf(val6), self._valueOf(val7), self._valueOf(val8),
        self._valueOf(val9),
    )

  @overload(
      QObject, Qt.ConnectionType, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
  )
  @overload(
      NoneType, Qt.ConnectionType, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
  )
  def invoke(
      self,
      object: Optional[QObject],
      connectionType: Qt.ConnectionType,
      val0: QGenericArgument,
      val1: QGenericArgument,
      val2: QGenericArgument,
      val3: QGenericArgument,
      val4: QGenericArgument,
      val5: QGenericArgument,
      val6: QGenericArgument,
      val7: QGenericArgument,
      val8: QGenericArgument,
      val9: QGenericArgument,
  ) -> bool:
    """
    Calls Qt's 'bool QMetaMethod::invoke(QObject *object, Qt::ConnectionType
    connectionType, QGenericArgument val0, QGenericArgument val1,
    QGenericArgument val2, QGenericArgument val3, QGenericArgument val4,
    QGenericArgument val5, QGenericArgument val6, QGenericArgument val7,
    QGenericArgument val8, QGenericArgument val9) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#invoke

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    connectionType : Qt.ConnectionType
      Passed on as its number.

    val0 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val1 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val2 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val3 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val4 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val5 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val6 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val7 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val8 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val9 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.
    """
    #  bool QMetaMethod::invoke(QObject *object, Qt::ConnectionType
    #      connectionType, QGenericArgument val0, QGenericArgument val1,
    #      QGenericArgument val2, QGenericArgument val3, QGenericArgument
    #      val4, QGenericArgument val5, QGenericArgument val6,
    #      QGenericArgument val7, QGenericArgument val8, QGenericArgument
    #      val9) const
    return self.uglySide.call(
        'ritual_ZNK11QMetaMethod6invokeEP7QObjectN2Qt14ConnectionTypeE16QGe'
        'nericArgumentS4_S4_S4_S4_S4_S4_S4_S4_S4_',
        self._addressOf(object), connectionType.value, self._valueOf(val0),
        self._valueOf(val1), self._valueOf(val2), self._valueOf(val3),
        self._valueOf(val4), self._valueOf(val5), self._valueOf(val6),
        self._valueOf(val7), self._valueOf(val8), self._valueOf(val9),
    )

  @overload(
      QObject, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument,
  )
  @overload(
      NoneType, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument, QGenericArgument,
      QGenericArgument, QGenericArgument, QGenericArgument,
  )
  def invoke(
      self,
      object: Optional[QObject],
      val0: QGenericArgument,
      val1: QGenericArgument,
      val2: QGenericArgument,
      val3: QGenericArgument,
      val4: QGenericArgument,
      val5: QGenericArgument,
      val6: QGenericArgument,
      val7: QGenericArgument,
      val8: QGenericArgument,
      val9: QGenericArgument,
  ) -> bool:
    """
    Calls Qt's 'bool QMetaMethod::invoke(QObject *object, QGenericArgument
    val0, QGenericArgument val1, QGenericArgument val2, QGenericArgument
    val3, QGenericArgument val4, QGenericArgument val5, QGenericArgument
    val6, QGenericArgument val7, QGenericArgument val8, QGenericArgument
    val9) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#invoke

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    val0 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val1 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val2 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val3 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val4 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val5 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val6 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val7 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val8 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.

    val9 : QGenericArgument
      Passed on as a value: Qt reads the C++ QGenericArgument, which stays
      Python's own.
    """
    #  bool QMetaMethod::invoke(QObject *object, QGenericArgument val0,
    #      QGenericArgument val1, QGenericArgument val2, QGenericArgument
    #      val3, QGenericArgument val4, QGenericArgument val5,
    #      QGenericArgument val6, QGenericArgument val7, QGenericArgument
    #      val8, QGenericArgument val9) const
    return self.uglySide.call(
        'ritual_ZNK11QMetaMethod6invokeEP7QObject16QGenericArgumentS2_S2_S2'
        '_S2_S2_S2_S2_S2_S2_',
        self._addressOf(object), self._valueOf(val0), self._valueOf(val1),
        self._valueOf(val2), self._valueOf(val3), self._valueOf(val4),
        self._valueOf(val5), self._valueOf(val6), self._valueOf(val7),
        self._valueOf(val8), self._valueOf(val9),
    )

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

  @overload(THIS)
  def __eq__(self, rhs: QMetaMethod) -> bool:
    """
    Calls Qt's 'bool operator==(const QMetaMethod &lhs, const QMetaMethod
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#operator==

    Parameters
    ----------

    rhs : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  bool operator==(const QMetaMethod &lhs, const QMetaMethod &rhs)
    return Rituals.call(
        'ritual_ZeqRK11QMetaMethodS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QMetaMethod) -> bool:
    """
    Calls Qt's 'bool operator!=(const QMetaMethod &lhs, const QMetaMethod
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethod.html#operator!=

    Parameters
    ----------

    rhs : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  bool operator!=(const QMetaMethod &lhs, const QMetaMethod &rhs)
    return Rituals.call(
        'ritual_ZneRK11QMetaMethodS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

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
