"""
QDBusArgument binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/qdbusargument.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaType, QVariant
  from . import QDBusArgumentPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusArgumentPrivate = WAIT['QDBusArgumentPrivate']
  QMetaType = WAIT['QMetaType']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusArgument(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDBusArgument: a plain Python object standing in
  front of one C++ QDBusArgument.

  C++ hands a QDBusArgument around as a copy, so every C++ QDBusArgument
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDBusArgument that has a ritual and that Python can
  call so far, 13 names in all: 'beginStructure', 'endStructure',
  'beginArray', 'endArray', 'beginMap', 'endMap', 'beginMapEntry',
  'endMapEntry', 'appendVariant', 'currentSignature', 'currentType', 'atEnd',
  'asVariant'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDBusArgument::QDBusArgument(QDBusArgument &&other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QDBusArgument &QDBusArgument::operator=(QDBusArgument &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QDBusArgument &QDBusArgument::operator=(const QDBusArgument
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QDBusArgument::~QDBusArgument()': the destructor: Python removes
    its C++ QDBusArgument by it, and has no other use for it.
  - Qt's 'void QDBusArgument::swap(QDBusArgument &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QDBusArgument &QDBusArgument::operator<<(uchar arg)': gives a type
    Python has no way to take yet.
  - Qt's 'QDBusArgument &QDBusArgument::operator<<(bool arg)': gives a type
    Python has no way to take yet.
  - Qt's 'QDBusArgument &QDBusArgument::operator<<(short arg)': gives a type
    Python has no way to take yet.
  - Qt's 'QDBusArgument &QDBusArgument::operator<<(ushort arg)': gives a type
    Python has no way to take yet.
  - Qt's 'QDBusArgument &QDBusArgument::operator<<(int arg)': gives a type
    Python has no way to take yet.
  - Qt's 'QDBusArgument &QDBusArgument::operator<<(uint arg)': gives a type
    Python has no way to take yet.
  - Qt's 'QDBusArgument &QDBusArgument::operator<<(qlonglong arg)': gives a
    type Python has no way to take yet.
  - Qt's 'QDBusArgument &QDBusArgument::operator<<(qulonglong arg)': gives a
    type Python has no way to take yet.
  - Qt's 'QDBusArgument &QDBusArgument::operator<<(double arg)': gives a type
    Python has no way to take yet.
  - Qt's 'QDBusArgument &QDBusArgument::operator<<(const QString &arg)':
    gives a type Python has no way to take yet.
  - Qt's 'QDBusArgument &QDBusArgument::operator<<(const QDBusVariant &arg)':
    gives a type Python has no way to take yet.
  - Qt's 'QDBusArgument &QDBusArgument::operator<<(const QDBusObjectPath
    &arg)': gives a type Python has no way to take yet.
  - Qt's 'QDBusArgument &QDBusArgument::operator<<(const QDBusSignature
    &arg)': gives a type Python has no way to take yet.
  - Qt's 'QDBusArgument &QDBusArgument::operator<<(const
    QDBusUnixFileDescriptor &arg)': gives a type Python has no way to take
    yet.
  - Qt's 'QDBusArgument &QDBusArgument::operator<<(const QStringList &arg)':
    gives a type Python has no way to take yet.
  - Qt's 'QDBusArgument &QDBusArgument::operator<<(const QByteArray &arg)':
    gives a type Python has no way to take yet.
  - Qt's 'const QDBusArgument &QDBusArgument::operator>>(uchar &arg) const':
    takes a number to change where it is.
  - Qt's 'const QDBusArgument &QDBusArgument::operator>>(bool &arg) const':
    takes a number to change where it is.
  - Qt's 'const QDBusArgument &QDBusArgument::operator>>(short &arg) const':
    takes a number to change where it is.
  - Qt's 'const QDBusArgument &QDBusArgument::operator>>(ushort &arg) const':
    takes a number to change where it is.
  - Qt's 'const QDBusArgument &QDBusArgument::operator>>(int &arg) const':
    takes a number to change where it is.
  - Qt's 'const QDBusArgument &QDBusArgument::operator>>(uint &arg) const':
    takes a number to change where it is.
  - Qt's 'const QDBusArgument &QDBusArgument::operator>>(qlonglong &arg)
    const': takes a number to change where it is.
  - Qt's 'const QDBusArgument &QDBusArgument::operator>>(qulonglong &arg)
    const': takes a number to change where it is.
  - Qt's 'const QDBusArgument &QDBusArgument::operator>>(double &arg) const':
    takes a number to change where it is.
  - Qt's 'const QDBusArgument &QDBusArgument::operator>>(QString &arg)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'const QDBusArgument &QDBusArgument::operator>>(QDBusVariant &arg)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'const QDBusArgument &QDBusArgument::operator>>(QDBusObjectPath
    &arg) const': takes a type Python has no way to hand over yet.
  - Qt's 'const QDBusArgument &QDBusArgument::operator>>(QDBusSignature &arg)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'const QDBusArgument
    &QDBusArgument::operator>>(QDBusUnixFileDescriptor &arg) const': takes a
    type Python has no way to hand over yet.
  - Qt's 'const QDBusArgument &QDBusArgument::operator>>(QStringList &arg)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'const QDBusArgument &QDBusArgument::operator>>(QByteArray &arg)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'void QDBusArgument::beginStructure() const': takes in Python what
    'void QDBusArgument::beginStructure()' takes.
  - Qt's 'void QDBusArgument::endStructure() const': takes in Python what
    'void QDBusArgument::endStructure()' takes.
  - Qt's 'void QDBusArgument::endArray() const': takes in Python what 'void
    QDBusArgument::endArray()' takes.
  - Qt's 'void QDBusArgument::endMap() const': takes in Python what 'void
    QDBusArgument::endMap()' takes.
  - Qt's 'void QDBusArgument::beginMapEntry() const': takes in Python what
    'void QDBusArgument::beginMapEntry()' takes.
  - Qt's 'void QDBusArgument::endMapEntry() const': takes in Python what
    'void QDBusArgument::endMapEntry()' takes.

  What to expect
  --------------

  - The C++ QDBusArgument is created at the first use, not by
    'QDBusArgument(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDBusArgument back gives a copy the ritual made for
    Python, in a new cute QDBusArgument.
  - Each name of Qt's QDBusArgument that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QDBusArgument, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ElementType(CuteNum):
    """
    The enum 'QDBusArgument::ElementType' of Qt, with the 7 names Qt gives in
    it.
    """

    BasicType = Kee[int](0)
    VariantType = Kee[int](1)
    ArrayType = Kee[int](2)
    StructureType = Kee[int](3)
    MapType = Kee[int](4)
    MapEntryType = Kee[int](5)
    UnknownType = Kee[int](-1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusArgument'

  #  Qt's '~QDBusArgument()'. Naming it makes this a value class: Python owns
  #  every C++ QDBusArgument behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QDBusArgumentD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def currentSignature(self) -> str:
    """
    Calls Qt's 'QString QDBusArgument::currentSignature() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusargument.html#currentSignature

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusArgument::currentSignature() const
    return self.uglySide.call(
        'ritual_ZNK13QDBusArgument16currentSignatureEv',
    )

  def currentType(self) -> ElementType:
    """
    Calls Qt's 'ElementType QDBusArgument::currentType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusargument.html#currentType

    Returns
    -------

    ElementType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ElementType(number)'
      gives.
    """
    #  ElementType QDBusArgument::currentType() const
    return QDBusArgument.ElementType(self.uglySide.call(
        'ritual_ZNK13QDBusArgument11currentTypeEv',
    ))

  def atEnd(self) -> bool:
    """
    Calls Qt's 'bool QDBusArgument::atEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusargument.html#atEnd
    """
    #  bool QDBusArgument::atEnd() const
    return self.uglySide.call('ritual_ZNK13QDBusArgument5atEndEv')

  def asVariant(self) -> QVariant:
    """
    Calls Qt's 'QVariant QDBusArgument::asVariant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusargument.html#asVariant

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDBusArgument::asVariant() const
    address = self.uglySide.call('ritual_ZNK13QDBusArgument9asVariantEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

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
    Notes what was given, for Qt's 'QDBusArgument::QDBusArgument()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdbusargument.html#QDBusArgument
    """
    #  QDBusArgument::QDBusArgument()
    self._noteCreation(QDBusArgument, lambda: Rituals.call(
        'ritual_ZN13QDBusArgumentC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QDBusArgument) -> None:
    """
    Notes what was given, for Qt's 'QDBusArgument::QDBusArgument(const
    QDBusArgument &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdbusargument.html#QDBusArgument

    Parameters
    ----------

    other : QDBusArgument
      Passed on as a value: Qt reads the C++ QDBusArgument, which stays
      Python's own.
    """
    #  QDBusArgument::QDBusArgument(const QDBusArgument &other)
    self._noteCreation(QDBusArgument, lambda: Rituals.call(
        'ritual_ZN13QDBusArgumentC1ERKS_', self._valueOf(other),
    ))

  @overload(QDBusArgumentPrivate)
  @overload(NoneType)
  def __init__(self, d: Optional[QDBusArgumentPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QDBusArgument::QDBusArgument(QDBusArgumentPrivate *d)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdbusargument.html#QDBusArgument

    Parameters
    ----------

    d : Optional[QDBusArgumentPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDBusArgument::QDBusArgument(QDBusArgumentPrivate *d)
    self._noteCreation(QDBusArgument, lambda: Rituals.call(
        'ritual_ZN13QDBusArgumentC1EP20QDBusArgumentPrivate',
        self._addressOf(d),
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

  def beginStructure(self) -> None:
    """
    Calls Qt's 'void QDBusArgument::beginStructure()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusargument.html#beginStructure
    """
    #  void QDBusArgument::beginStructure()
    self.uglySide.call('ritual_ZN13QDBusArgument14beginStructureEv')

  def endStructure(self) -> None:
    """
    Calls Qt's 'void QDBusArgument::endStructure()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusargument.html#endStructure
    """
    #  void QDBusArgument::endStructure()
    self.uglySide.call('ritual_ZN13QDBusArgument12endStructureEv')

  @overload(int)
  def beginArray(self, elementMetaTypeId: int) -> None:
    """
    Calls Qt's 'void QDBusArgument::beginArray(int elementMetaTypeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusargument.html#beginArray

    Parameters
    ----------

    elementMetaTypeId : int
      Passed on as it is.
    """
    #  void QDBusArgument::beginArray(int elementMetaTypeId)
    self.uglySide.call(
        'ritual_ZN13QDBusArgument10beginArrayEi', elementMetaTypeId,
    )

  @overload(QMetaType)
  def beginArray(self, elementMetaType: QMetaType) -> None:
    """
    Calls Qt's 'void QDBusArgument::beginArray(QMetaType elementMetaType)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusargument.html#beginArray

    Parameters
    ----------

    elementMetaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  void QDBusArgument::beginArray(QMetaType elementMetaType)
    self.uglySide.call(
        'ritual_ZN13QDBusArgument10beginArrayE9QMetaType',
        self._valueOf(elementMetaType),
    )

  @overload()
  def beginArray(self) -> None:
    """
    Calls Qt's 'void QDBusArgument::beginArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusargument.html#beginArray
    """
    #  void QDBusArgument::beginArray() const
    self.uglySide.call('ritual_ZNK13QDBusArgument10beginArrayEv')

  def endArray(self) -> None:
    """
    Calls Qt's 'void QDBusArgument::endArray()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusargument.html#endArray
    """
    #  void QDBusArgument::endArray()
    self.uglySide.call('ritual_ZN13QDBusArgument8endArrayEv')

  @overload(int, int)
  def beginMap(self, keyMetaTypeId: int, valueMetaTypeId: int) -> None:
    """
    Calls Qt's 'void QDBusArgument::beginMap(int keyMetaTypeId, int
    valueMetaTypeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusargument.html#beginMap

    Parameters
    ----------

    keyMetaTypeId : int
      Passed on as it is.

    valueMetaTypeId : int
      Passed on as it is.
    """
    #  void QDBusArgument::beginMap(int keyMetaTypeId, int valueMetaTypeId)
    self.uglySide.call(
        'ritual_ZN13QDBusArgument8beginMapEii',
        keyMetaTypeId, valueMetaTypeId,
    )

  @overload(QMetaType, QMetaType)
  def beginMap(
      self,
      keyMetaType: QMetaType,
      valueMetaType: QMetaType,
  ) -> None:
    """
    Calls Qt's 'void QDBusArgument::beginMap(QMetaType keyMetaType, QMetaType
    valueMetaType)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusargument.html#beginMap

    Parameters
    ----------

    keyMetaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    valueMetaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  void QDBusArgument::beginMap(QMetaType keyMetaType, QMetaType
    #      valueMetaType)
    self.uglySide.call(
        'ritual_ZN13QDBusArgument8beginMapE9QMetaTypeS0_',
        self._valueOf(keyMetaType), self._valueOf(valueMetaType),
    )

  @overload()
  def beginMap(self) -> None:
    """
    Calls Qt's 'void QDBusArgument::beginMap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusargument.html#beginMap
    """
    #  void QDBusArgument::beginMap() const
    self.uglySide.call('ritual_ZNK13QDBusArgument8beginMapEv')

  def endMap(self) -> None:
    """
    Calls Qt's 'void QDBusArgument::endMap()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusargument.html#endMap
    """
    #  void QDBusArgument::endMap()
    self.uglySide.call('ritual_ZN13QDBusArgument6endMapEv')

  def beginMapEntry(self) -> None:
    """
    Calls Qt's 'void QDBusArgument::beginMapEntry()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusargument.html#beginMapEntry
    """
    #  void QDBusArgument::beginMapEntry()
    self.uglySide.call('ritual_ZN13QDBusArgument13beginMapEntryEv')

  def endMapEntry(self) -> None:
    """
    Calls Qt's 'void QDBusArgument::endMapEntry()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusargument.html#endMapEntry
    """
    #  void QDBusArgument::endMapEntry()
    self.uglySide.call('ritual_ZN13QDBusArgument11endMapEntryEv')

  @overload(QVariant)
  def appendVariant(self, v: QVariant) -> None:
    """
    Calls Qt's 'void QDBusArgument::appendVariant(const QVariant &v)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusargument.html#appendVariant

    Parameters
    ----------

    v : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDBusArgument::appendVariant(const QVariant &v)
    self.uglySide.call(
        'ritual_ZN13QDBusArgument13appendVariantERK8QVariant',
        self._valueOf(v),
    )

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QDBusArgument::swap(QDBusArgument &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDBusArgument.swap' has no cute function yet. Qt's 'void "
        "QDBusArgument::swap(QDBusArgument &other)': takes a type Python "
        "has no way to hand over yet.")
