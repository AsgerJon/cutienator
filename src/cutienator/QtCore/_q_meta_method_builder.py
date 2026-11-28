"""
QMetaMethodBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qmetaobjectbuilder_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QMetaMethodBuilder to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QList, QMetaMethod

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QByteArrayView, QMetaObjectBuilder
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QMetaObjectBuilder = WAIT['QMetaObjectBuilder']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMetaMethodBuilder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMetaMethodBuilder: a plain Python object standing in
  front of one C++ QMetaMethodBuilder.

  C++ hands a QMetaMethodBuilder around as a copy, so every C++
  QMetaMethodBuilder behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMetaMethodBuilder that has a ritual and that Python
  can call so far, 18 names in all: 'index', 'methodType', 'signature',
  'returnType', 'setReturnType', 'parameterTypes', 'parameterNames',
  'setParameterNames', 'tag', 'setTag', 'access', 'setAccess', 'attributes',
  'setAttributes', 'isConst', 'setConst', 'revision', 'setRevision'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMetaMethodBuilderPrivate *QMetaMethodBuilder::d_func() const':
    gives 'QMetaMethodBuilderPrivate', which has no cute class yet.
  - Qt's 'QMetaMethodBuilder::~QMetaMethodBuilder()': the destructor: Python
    removes its C++ QMetaMethodBuilder by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QMetaMethodBuilder is created at the first use, not by
    'QMetaMethodBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMetaMethodBuilder back gives a copy the ritual made
    for Python, in a new cute QMetaMethodBuilder.
  - Each name of Qt's QMetaMethodBuilder that has no cute function yet,
    'd_func', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMetaMethodBuilder'

  #  Qt's '~QMetaMethodBuilder()'. Naming it makes this a value class: Python
  #  owns every C++ QMetaMethodBuilder behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QMetaMethodBuilderD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def index(self) -> int:
    """
    Calls Qt's 'int QMetaMethodBuilder::index() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethodbuilder.html#index
    """
    #  int QMetaMethodBuilder::index() const
    return self.uglySide.call('ritual_ZNK18QMetaMethodBuilder5indexEv')

  def methodType(self) -> QMetaMethod.MethodType:
    """
    Calls Qt's 'QMetaMethod::MethodType QMetaMethodBuilder::methodType()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethodbuilder.html#methodType

    Returns
    -------

    QMetaMethod.MethodType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QMetaMethod.MethodType(number)' gives.
    """
    #  QMetaMethod::MethodType QMetaMethodBuilder::methodType() const
    return QMetaMethod.MethodType(self.uglySide.call(
        'ritual_ZNK18QMetaMethodBuilder10methodTypeEv',
    ))

  def signature(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMetaMethodBuilder::signature() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethodbuilder.html#signature

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMetaMethodBuilder::signature() const
    address = self.uglySide.call(
        'ritual_ZNK18QMetaMethodBuilder9signatureEv',
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def returnType(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMetaMethodBuilder::returnType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethodbuilder.html#returnType

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMetaMethodBuilder::returnType() const
    address = self.uglySide.call(
        'ritual_ZNK18QMetaMethodBuilder10returnTypeEv',
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def parameterTypes(self) -> QList[QByteArrayView]:
    """
    Calls Qt's 'QList<QByteArrayView> QMetaMethodBuilder::parameterTypes()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetamethodbuilder.html#parameterTypes

    Returns
    -------

    QList[QByteArrayView]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArrayView> QMetaMethodBuilder::parameterTypes() const
    address = self.uglySide.call(
        'ritual_ZNK18QMetaMethodBuilder14parameterTypesEv',
    )
    from . import QByteArrayView
    return QList[QByteArrayView]._cuteOwning(address)

  def parameterNames(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QMetaMethodBuilder::parameterNames()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetamethodbuilder.html#parameterNames

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QMetaMethodBuilder::parameterNames() const
    address = self.uglySide.call(
        'ritual_ZNK18QMetaMethodBuilder14parameterNamesEv',
    )
    from . import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  def tag(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMetaMethodBuilder::tag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethodbuilder.html#tag

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMetaMethodBuilder::tag() const
    address = self.uglySide.call('ritual_ZNK18QMetaMethodBuilder3tagEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def access(self) -> QMetaMethod.Access:
    """
    Calls Qt's 'QMetaMethod::Access QMetaMethodBuilder::access() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethodbuilder.html#access

    Returns
    -------

    QMetaMethod.Access
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QMetaMethod.Access(number)' gives.
    """
    #  QMetaMethod::Access QMetaMethodBuilder::access() const
    return QMetaMethod.Access(self.uglySide.call(
        'ritual_ZNK18QMetaMethodBuilder6accessEv',
    ))

  def attributes(self) -> int:
    """
    Calls Qt's 'int QMetaMethodBuilder::attributes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethodbuilder.html#attributes
    """
    #  int QMetaMethodBuilder::attributes() const
    return self.uglySide.call('ritual_ZNK18QMetaMethodBuilder10attributesEv')

  def isConst(self) -> bool:
    """
    Calls Qt's 'bool QMetaMethodBuilder::isConst() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethodbuilder.html#isConst
    """
    #  bool QMetaMethodBuilder::isConst() const
    return self.uglySide.call('ritual_ZNK18QMetaMethodBuilder7isConstEv')

  def revision(self) -> int:
    """
    Calls Qt's 'int QMetaMethodBuilder::revision() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethodbuilder.html#revision
    """
    #  int QMetaMethodBuilder::revision() const
    return self.uglySide.call('ritual_ZNK18QMetaMethodBuilder8revisionEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setReturnType(self, value: QByteArray) -> None:
    """
    Calls Qt's 'void QMetaMethodBuilder::setReturnType(const QByteArray
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetamethodbuilder.html#setReturnType

    Parameters
    ----------

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QMetaMethodBuilder::setReturnType(const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN18QMetaMethodBuilder13setReturnTypeERK10QByteArray',
        self._valueOf(value),
    )

  @overload(QList[QByteArray])
  def setParameterNames(self, value: QList[QByteArray]) -> None:
    """
    Calls Qt's 'void QMetaMethodBuilder::setParameterNames(const
    QList<QByteArray> &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetamethodbuilder.html#setParameterNames

    Parameters
    ----------

    value : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QMetaMethodBuilder::setParameterNames(const QList<QByteArray>
    #      &value)
    self.uglySide.call(
        'ritual_ZN18QMetaMethodBuilder17setParameterNamesERK5QListI10QByteA'
        'rrayE',
        self._valueOf(value),
    )

  @overload(QByteArray)
  def setTag(self, value: QByteArray) -> None:
    """
    Calls Qt's 'void QMetaMethodBuilder::setTag(const QByteArray &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethodbuilder.html#setTag

    Parameters
    ----------

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QMetaMethodBuilder::setTag(const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN18QMetaMethodBuilder6setTagERK10QByteArray',
        self._valueOf(value),
    )

  @overload(QMetaMethod.Access)
  def setAccess(self, value: QMetaMethod.Access) -> None:
    """
    Calls Qt's 'void QMetaMethodBuilder::setAccess(QMetaMethod::Access
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethodbuilder.html#setAccess

    Parameters
    ----------

    value : QMetaMethod.Access
      Passed on as its number.
    """
    #  void QMetaMethodBuilder::setAccess(QMetaMethod::Access value)
    self.uglySide.call(
        'ritual_ZN18QMetaMethodBuilder9setAccessEN11QMetaMethod6AccessE',
        value.value,
    )

  @overload(int)
  def setAttributes(self, value: int) -> None:
    """
    Calls Qt's 'void QMetaMethodBuilder::setAttributes(int value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetamethodbuilder.html#setAttributes

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QMetaMethodBuilder::setAttributes(int value)
    self.uglySide.call(
        'ritual_ZN18QMetaMethodBuilder13setAttributesEi', value,
    )

  @overload()
  @overload(bool)
  def setConst(self, methodIsConst: bool = True) -> None:
    """
    Calls Qt's 'void QMetaMethodBuilder::setConst(bool methodIsConst)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetamethodbuilder.html#setConst

    Parameters
    ----------

    methodIsConst : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QMetaMethodBuilder::setConst(bool methodIsConst)
    self.uglySide.call(
        'ritual_ZN18QMetaMethodBuilder8setConstEb', methodIsConst,
    )

  @overload(int)
  def setRevision(self, revision: int) -> None:
    """
    Calls Qt's 'void QMetaMethodBuilder::setRevision(int revision)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetamethodbuilder.html#setRevision

    Parameters
    ----------

    revision : int
      Passed on as it is.
    """
    #  void QMetaMethodBuilder::setRevision(int revision)
    self.uglySide.call(
        'ritual_ZN18QMetaMethodBuilder11setRevisionEi', revision,
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
    Notes what was given, for Qt's
    'QMetaMethodBuilder::QMetaMethodBuilder()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetamethodbuilder.html#QMetaMethodBuilder
    """
    #  QMetaMethodBuilder::QMetaMethodBuilder()
    self._noteCreation(QMetaMethodBuilder, lambda: Rituals.call(
        'ritual_ZN18QMetaMethodBuilderC1Ev',
    ))

  @overload(QMetaObjectBuilder, int, QMetaMethod.MethodType)
  @overload(NoneType, int, QMetaMethod.MethodType)
  def __init__(
      self,
      mobj: Optional[QMetaObjectBuilder],
      index: int,
      type: QMetaMethod.MethodType,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QMetaMethodBuilder::QMetaMethodBuilder(const QMetaObjectBuilder *mobj,
    int index, QMetaMethod::MethodType type)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetamethodbuilder.html#QMetaMethodBuilder

    Parameters
    ----------

    mobj : Optional[QMetaObjectBuilder]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    type : QMetaMethod.MethodType
      Passed on as its number.
    """
    #  QMetaMethodBuilder::QMetaMethodBuilder(const QMetaObjectBuilder *mobj,
    #      int index, QMetaMethod::MethodType type)
    self._noteCreation(QMetaMethodBuilder, lambda: Rituals.call(
        'ritual_ZN18QMetaMethodBuilderC1EPK18QMetaObjectBuilderiN11QMetaMet'
        'hod10MethodTypeE',
        self._addressOf(mobj), index, type.value,
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

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    Qt's 'QMetaMethodBuilderPrivate *QMetaMethodBuilder::d_func() const':
    gives 'QMetaMethodBuilderPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaMethodBuilder.d_func' has no cute function yet. Qt's "
        "'QMetaMethodBuilderPrivate *QMetaMethodBuilder::d_func() const': "
        "gives 'QMetaMethodBuilderPrivate', which has no cute class yet.")
