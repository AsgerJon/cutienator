"""
QMetaEnumBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qmetaobjectbuilder_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QMetaEnumBuilder to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QMetaObjectBuilder, QMetaType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QMetaObjectBuilder = WAIT['QMetaObjectBuilder']
  QMetaType = WAIT['QMetaType']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMetaEnumBuilder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMetaEnumBuilder: a plain Python object standing in
  front of one C++ QMetaEnumBuilder.

  C++ hands a QMetaEnumBuilder around as a copy, so every C++
  QMetaEnumBuilder behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMetaEnumBuilder that has a ritual and that Python
  can call so far, 17 names in all: 'index', 'name', 'enumName',
  'setEnumName', 'metaType', 'setMetaType', 'isFlag', 'setIsFlag',
  'isScoped', 'setIsScoped', 'is64Bit', 'setIs64Bit', 'keyCount', 'key',
  'value', 'addKey', 'removeKey'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'std::optional<quint64> QMetaEnumBuilder::value64(int index) const':
    gives a type Python has no way to take yet.
  - Qt's 'int QMetaEnumBuilder::addKey(const QByteArray &name, quint64
    value)': takes in Python what 'int QMetaEnumBuilder::addKey(const
    QByteArray &name, int value)' takes.
  - Qt's 'QMetaEnumBuilderPrivate *QMetaEnumBuilder::d_func() const': gives
    'QMetaEnumBuilderPrivate', which has no cute class yet.
  - Qt's 'QMetaEnumBuilder::~QMetaEnumBuilder()': the destructor: Python
    removes its C++ QMetaEnumBuilder by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QMetaEnumBuilder is created at the first use, not by
    'QMetaEnumBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMetaEnumBuilder back gives a copy the ritual made
    for Python, in a new cute QMetaEnumBuilder.
  - Each name of Qt's QMetaEnumBuilder that has no cute function yet,
    'd_func', 'value64', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMetaEnumBuilder'

  #  Qt's '~QMetaEnumBuilder()'. Naming it makes this a value class: Python
  #  owns every C++ QMetaEnumBuilder behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QMetaEnumBuilderD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def index(self) -> int:
    """
    Calls Qt's 'int QMetaEnumBuilder::index() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenumbuilder.html#index
    """
    #  int QMetaEnumBuilder::index() const
    return self.uglySide.call('ritual_ZNK16QMetaEnumBuilder5indexEv')

  def name(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMetaEnumBuilder::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenumbuilder.html#name

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMetaEnumBuilder::name() const
    address = self.uglySide.call('ritual_ZNK16QMetaEnumBuilder4nameEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def enumName(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMetaEnumBuilder::enumName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenumbuilder.html#enumName

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMetaEnumBuilder::enumName() const
    address = self.uglySide.call('ritual_ZNK16QMetaEnumBuilder8enumNameEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def metaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QMetaEnumBuilder::metaType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenumbuilder.html#metaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QMetaEnumBuilder::metaType() const
    address = self.uglySide.call('ritual_ZNK16QMetaEnumBuilder8metaTypeEv')
    from . import QMetaType
    return QMetaType._cuteOwning(address)

  def isFlag(self) -> bool:
    """
    Calls Qt's 'bool QMetaEnumBuilder::isFlag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenumbuilder.html#isFlag
    """
    #  bool QMetaEnumBuilder::isFlag() const
    return self.uglySide.call('ritual_ZNK16QMetaEnumBuilder6isFlagEv')

  def isScoped(self) -> bool:
    """
    Calls Qt's 'bool QMetaEnumBuilder::isScoped() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenumbuilder.html#isScoped
    """
    #  bool QMetaEnumBuilder::isScoped() const
    return self.uglySide.call('ritual_ZNK16QMetaEnumBuilder8isScopedEv')

  def is64Bit(self) -> bool:
    """
    Calls Qt's 'bool QMetaEnumBuilder::is64Bit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenumbuilder.html#is64Bit
    """
    #  bool QMetaEnumBuilder::is64Bit() const
    return self.uglySide.call('ritual_ZNK16QMetaEnumBuilder7is64BitEv')

  def keyCount(self) -> int:
    """
    Calls Qt's 'int QMetaEnumBuilder::keyCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenumbuilder.html#keyCount
    """
    #  int QMetaEnumBuilder::keyCount() const
    return self.uglySide.call('ritual_ZNK16QMetaEnumBuilder8keyCountEv')

  @overload(int)
  def key(self, index: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMetaEnumBuilder::key(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenumbuilder.html#key

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMetaEnumBuilder::key(int index) const
    address = self.uglySide.call('ritual_ZNK16QMetaEnumBuilder3keyEi', index)
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(int)
  def value(self, index: int) -> int:
    """
    Calls Qt's 'int QMetaEnumBuilder::value(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenumbuilder.html#value

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QMetaEnumBuilder::value(int index) const
    return self.uglySide.call('ritual_ZNK16QMetaEnumBuilder5valueEi', index)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setEnumName(self, alias: QByteArray) -> None:
    """
    Calls Qt's 'void QMetaEnumBuilder::setEnumName(const QByteArray &alias)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenumbuilder.html#setEnumName

    Parameters
    ----------

    alias : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QMetaEnumBuilder::setEnumName(const QByteArray &alias)
    self.uglySide.call(
        'ritual_ZN16QMetaEnumBuilder11setEnumNameERK10QByteArray',
        self._valueOf(alias),
    )

  @overload(QMetaType)
  def setMetaType(self, metaType: QMetaType) -> None:
    """
    Calls Qt's 'void QMetaEnumBuilder::setMetaType(QMetaType metaType)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenumbuilder.html#setMetaType

    Parameters
    ----------

    metaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  void QMetaEnumBuilder::setMetaType(QMetaType metaType)
    self.uglySide.call(
        'ritual_ZN16QMetaEnumBuilder11setMetaTypeE9QMetaType',
        self._valueOf(metaType),
    )

  @overload(bool)
  def setIsFlag(self, value: bool) -> None:
    """
    Calls Qt's 'void QMetaEnumBuilder::setIsFlag(bool value)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenumbuilder.html#setIsFlag

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QMetaEnumBuilder::setIsFlag(bool value)
    self.uglySide.call('ritual_ZN16QMetaEnumBuilder9setIsFlagEb', value)

  @overload(bool)
  def setIsScoped(self, value: bool) -> None:
    """
    Calls Qt's 'void QMetaEnumBuilder::setIsScoped(bool value)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenumbuilder.html#setIsScoped

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QMetaEnumBuilder::setIsScoped(bool value)
    self.uglySide.call('ritual_ZN16QMetaEnumBuilder11setIsScopedEb', value)

  @overload(bool)
  def setIs64Bit(self, value: bool) -> None:
    """
    Calls Qt's 'void QMetaEnumBuilder::setIs64Bit(bool value)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenumbuilder.html#setIs64Bit

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QMetaEnumBuilder::setIs64Bit(bool value)
    self.uglySide.call('ritual_ZN16QMetaEnumBuilder10setIs64BitEb', value)

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
    Notes what was given, for Qt's 'QMetaEnumBuilder::QMetaEnumBuilder()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaenumbuilder.html#QMetaEnumBuilder
    """
    #  QMetaEnumBuilder::QMetaEnumBuilder()
    self._noteCreation(QMetaEnumBuilder, lambda: Rituals.call(
        'ritual_ZN16QMetaEnumBuilderC1Ev',
    ))

  @overload(QMetaObjectBuilder, int)
  @overload(NoneType, int)
  def __init__(self, mobj: Optional[QMetaObjectBuilder], index: int) -> None:
    """
    Notes what was given, for Qt's 'QMetaEnumBuilder::QMetaEnumBuilder(const
    QMetaObjectBuilder *mobj, int index)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaenumbuilder.html#QMetaEnumBuilder

    Parameters
    ----------

    mobj : Optional[QMetaObjectBuilder]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  QMetaEnumBuilder::QMetaEnumBuilder(const QMetaObjectBuilder *mobj, int
    #      index)
    self._noteCreation(QMetaEnumBuilder, lambda: Rituals.call(
        'ritual_ZN16QMetaEnumBuilderC1EPK18QMetaObjectBuilderi',
        self._addressOf(mobj), index,
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

  @overload(QByteArray, int)
  def addKey(self, name: QByteArray, value: int) -> int:
    """
    Calls Qt's 'int QMetaEnumBuilder::addKey(const QByteArray &name, int
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenumbuilder.html#addKey

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    value : int
      Passed on as it is.
    """
    #  int QMetaEnumBuilder::addKey(const QByteArray &name, int value)
    return self.uglySide.call(
        'ritual_ZN16QMetaEnumBuilder6addKeyERK10QByteArrayi',
        self._valueOf(name), value,
    )

  @overload(int)
  def removeKey(self, index: int) -> None:
    """
    Calls Qt's 'void QMetaEnumBuilder::removeKey(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaenumbuilder.html#removeKey

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QMetaEnumBuilder::removeKey(int index)
    self.uglySide.call('ritual_ZN16QMetaEnumBuilder9removeKeyEi', index)

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    Qt's 'QMetaEnumBuilderPrivate *QMetaEnumBuilder::d_func() const': gives
    'QMetaEnumBuilderPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaEnumBuilder.d_func' has no cute function yet. Qt's "
        "'QMetaEnumBuilderPrivate *QMetaEnumBuilder::d_func() const': gives "
        "'QMetaEnumBuilderPrivate', which has no cute class yet.")

  @staticmethod
  def value64(*__, **_) -> Never:
    """
    Qt's 'std::optional<quint64> QMetaEnumBuilder::value64(int index) const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QMetaEnumBuilder.value64' has no cute function yet. Qt's "
        "'std::optional<quint64> QMetaEnumBuilder::value64(int index) "
        "const': gives a type Python has no way to take yet.")
