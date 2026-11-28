"""
QQmlGadgetPtrWrapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlGadgetPtrWrapper to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMetaObject, QObject
from . import QQmlPropertyData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaProperty, QMetaType, QVariant
  from . import QQmlEngine, QQmlValueType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaProperty = WAIT['QMetaProperty']
  QMetaType = WAIT['QMetaType']
  QQmlEngine = WAIT['QQmlEngine']
  QQmlValueType = WAIT['QQmlValueType']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlGadgetPtrWrapper(QObject):
  """
  The cute side of Qt's QQmlGadgetPtrWrapper: a plain Python object standing
  in front of one C++ QQmlGadgetPtrWrapper.

  It is built on the cute 'QObject', as Qt's QQmlGadgetPtrWrapper is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlGadgetPtrWrapper that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr', 'instance',
  'read', 'write', 'value', 'setValue', 'metaType', 'property',
  'readOnGadget', 'writeOnGadget', 'valueType'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlGadgetPtrWrapper::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlGadgetPtrWrapper::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlGadgetPtrWrapper::~QQmlGadgetPtrWrapper()': the destructor:
    Python never removes a C++ QQmlGadgetPtrWrapper.
  - Qt's 'int QQmlGadgetPtrWrapper::metaCall(QMetaObject::Call type, int id,
    void **argv)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlGadgetPtrWrapper::writeOnGadget(const QMetaProperty
    &property, QVariant &&value)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlGadgetPtrWrapper is created at the first use, not by
    'QQmlGadgetPtrWrapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlGadgetPtrWrapper.
  - Qt tells when it has removed the C++ QQmlGadgetPtrWrapper. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlGadgetPtrWrapper that has no cute function yet,
    'metaCall', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

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
    Calls Qt's 'QString QQmlGadgetPtrWrapper::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlgadgetptrwrapper.html#tr

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
    #  QString QQmlGadgetPtrWrapper::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQmlGadgetPtrWrapper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QQmlEngine, QMetaType)
  @overload(NoneType, QMetaType)
  def instance(
      engine: Optional[QQmlEngine],
      type: QMetaType,
  ) -> Optional[QQmlGadgetPtrWrapper]:
    """
    Calls Qt's 'QQmlGadgetPtrWrapper
    *QQmlGadgetPtrWrapper::instance(QQmlEngine *engine, QMetaType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlgadgetptrwrapper.html#instance

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    Optional[QQmlGadgetPtrWrapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlGadgetPtrWrapper *QQmlGadgetPtrWrapper::instance(QQmlEngine
    #      *engine, QMetaType type)
    address = Rituals.call(
        'ritual_ZN20QQmlGadgetPtrWrapper8instanceEP10QQmlEngine9QMetaType',
        CuteMixin._addressOf(engine), CuteMixin._valueOf(type),
    )
    return QQmlGadgetPtrWrapper._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlGadgetPtrWrapper'

  #  A C++ QQmlGadgetPtrWrapper Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlGadgetPtrWrapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlGadgetPtrWrapper::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgadgetptrwrapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlGadgetPtrWrapper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlGadgetPtrWrapper10metaObjectEv',
    )
    return QMetaObject._cuteAt(address)

  def value(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlGadgetPtrWrapper::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlgadgetptrwrapper.html#value

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlGadgetPtrWrapper::value() const
    address = self.uglySide.call('ritual_ZNK20QQmlGadgetPtrWrapper5valueEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def metaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QQmlGadgetPtrWrapper::metaType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlgadgetptrwrapper.html#metaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QQmlGadgetPtrWrapper::metaType() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlGadgetPtrWrapper8metaTypeEv',
    )
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  @overload(int)
  def property(self, index: int) -> QMetaProperty:
    """
    Calls Qt's 'QMetaProperty QQmlGadgetPtrWrapper::property(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlgadgetptrwrapper.html#property

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QMetaProperty
      A new cute QMetaProperty around the copy Qt gave back. Python owns it.
    """
    #  QMetaProperty QQmlGadgetPtrWrapper::property(int index) const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlGadgetPtrWrapper8propertyEi', index,
    )
    from ..QtCore import QMetaProperty
    return QMetaProperty._cuteOwning(address)

  @overload(QMetaProperty)
  def readOnGadget(self, property: QMetaProperty) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlGadgetPtrWrapper::readOnGadget(const
    QMetaProperty &property) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgadgetptrwrapper.html#readOnGadget

    Parameters
    ----------

    property : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlGadgetPtrWrapper::readOnGadget(const QMetaProperty
    #      &property) const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlGadgetPtrWrapper12readOnGadgetERK13QMetaProperty',
        self._valueOf(property),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def valueType(self) -> Optional[QQmlValueType]:
    """
    Calls Qt's 'const QQmlValueType *QQmlGadgetPtrWrapper::valueType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgadgetptrwrapper.html#valueType

    Returns
    -------

    Optional[QQmlValueType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QQmlValueType *QQmlGadgetPtrWrapper::valueType() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlGadgetPtrWrapper9valueTypeEv',
    )
    from . import QQmlValueType
    return QQmlValueType._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QQmlGadgetPtrWrapper::setValue(const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlgadgetptrwrapper.html#setValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlGadgetPtrWrapper::setValue(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN20QQmlGadgetPtrWrapper8setValueERK8QVariant',
        self._valueOf(value),
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

  @overload(QQmlValueType)
  @overload(NoneType)
  @overload(QQmlValueType, QObject)
  @overload(QQmlValueType, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      valueType: Optional[QQmlValueType],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlGadgetPtrWrapper::QQmlGadgetPtrWrapper(QQmlValueType *valueType,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgadgetptrwrapper.html#QQmlGadgetPtrWrapper

    Parameters
    ----------

    valueType : Optional[QQmlValueType]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlGadgetPtrWrapper::QQmlGadgetPtrWrapper(QQmlValueType *valueType,
    #      QObject *parent)
    self._noteCreation(QQmlGadgetPtrWrapper, lambda: Rituals.call(
        'ritual_ZN20QQmlGadgetPtrWrapperC1EP13QQmlValueTypeP7QObject',
        self._addressOf(valueType), self._addressOf(parent, 'QObject'),
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

  @overload(QObject, int)
  @overload(NoneType, int)
  def read(self, obj: Optional[QObject], idx: int) -> None:
    """
    Calls Qt's 'void QQmlGadgetPtrWrapper::read(QObject *obj, int idx)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlgadgetptrwrapper.html#read

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    idx : int
      Passed on as it is.
    """
    #  void QQmlGadgetPtrWrapper::read(QObject *obj, int idx)
    self.uglySide.call(
        'ritual_ZN20QQmlGadgetPtrWrapper4readEP7QObjecti',
        self._addressOf(obj, 'QObject'), idx,
    )

  @overload(QObject, int, QQmlPropertyData.WriteFlags, int)
  @overload(NoneType, int, QQmlPropertyData.WriteFlags, int)
  def write(
      self,
      obj: Optional[QObject],
      idx: int,
      flags: QQmlPropertyData.WriteFlags,
      internalIndex: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlGadgetPtrWrapper::write(QObject *obj, int idx,
    QQmlPropertyData::WriteFlags flags, int internalIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlgadgetptrwrapper.html#write

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    idx : int
      Passed on as it is.

    flags : QQmlPropertyData.WriteFlags
      Passed on as its number.

    internalIndex : int
      Passed on as it is.
    """
    #  void QQmlGadgetPtrWrapper::write(QObject *obj, int idx,
    #      QQmlPropertyData::WriteFlags flags, int internalIndex) const
    self.uglySide.call(
        'ritual_ZNK20QQmlGadgetPtrWrapper5writeEP7QObjecti6QFlagsIN16QQmlPr'
        'opertyData9WriteFlagEEi',
        self._addressOf(obj, 'QObject'), idx, flags.value, internalIndex,
    )

  @overload(QMetaProperty, QVariant)
  def writeOnGadget(self, property: QMetaProperty, value: QVariant) -> None:
    """
    Calls Qt's 'void QQmlGadgetPtrWrapper::writeOnGadget(const QMetaProperty
    &property, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgadgetptrwrapper.html#writeOnGadget

    Parameters
    ----------

    property : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlGadgetPtrWrapper::writeOnGadget(const QMetaProperty
    #      &property, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN20QQmlGadgetPtrWrapper13writeOnGadgetERK13QMetaPropertyRK'
        '8QVariant',
        self._valueOf(property), self._valueOf(value),
    )

  @staticmethod
  def metaCall(*__, **_) -> Never:
    """
    Qt's 'int QQmlGadgetPtrWrapper::metaCall(QMetaObject::Call type, int id,
    void **argv)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlGadgetPtrWrapper.metaCall' has no cute function yet. Qt's "
        "'int QQmlGadgetPtrWrapper::metaCall(QMetaObject::Call type, int "
        "id, void **argv)': takes a type Python has no way to hand over yet."
    )
