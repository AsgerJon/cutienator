"""
QQmlProperty binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qqmlproperty.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaMethod, QMetaProperty, QMetaType, QObject
  from ..QtCore import QVariant
  from . import QQmlContext, QQmlEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlContext = WAIT['QQmlContext']
  QQmlEngine = WAIT['QQmlEngine']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlProperty(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlProperty: a plain Python object standing in front
  of one C++ QQmlProperty.

  C++ hands a QQmlProperty around as a copy, so every C++ QQmlProperty behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlProperty that has a ritual and that Python can
  call so far, 24 names in all: '__eq__', 'type', 'isValid', 'isProperty',
  'isSignalProperty', 'propertyType', 'propertyMetaType',
  'propertyTypeCategory', 'propertyTypeName', 'name', 'read', 'write',
  'reset', 'hasNotifySignal', 'needsNotifySignal', 'connectNotifySignal',
  'isWritable', 'isBindable', 'isDesignable', 'isResettable', 'object',
  'index', 'property', 'method'. It can be made from Python, in 8 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlProperty::~QQmlProperty()': the destructor: Python removes its
    C++ QQmlProperty by it, and has no other use for it.
  - Qt's 'QQmlProperty &QQmlProperty::operator=(const QQmlProperty &a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QQmlProperty::QQmlProperty(QQmlProperty &&other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QQmlProperty &QQmlProperty::operator=(QQmlProperty &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QQmlProperty::swap(QQmlProperty &other)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 47 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQmlProperty is created at the first use, not by
    'QQmlProperty(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlProperty back gives a copy the ritual made for
    Python, in a new cute QQmlProperty.
  - Each name of Qt's QQmlProperty that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QQmlProperty, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class PropertyTypeCategory(CuteNum):
    """
    The enum 'QQmlProperty::PropertyTypeCategory' of Qt, with the 4 names Qt
    gives in it.
    """

    InvalidCategory = Kee[int](0)
    List = Kee[int](1)
    Object = Kee[int](2)
    Normal = Kee[int](3)

  class Type(CuteNum):
    """
    The enum 'QQmlProperty::Type' of Qt, with the 3 names Qt gives in it.
    """

    Invalid = Kee[int](0)
    Property = Kee[int](1)
    SignalProperty = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlProperty'

  #  Qt's '~QQmlProperty()'. Naming it makes this a value class: Python owns
  #  every C++ QQmlProperty behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QQmlPropertyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Type:
    """
    Calls Qt's 'Type QQmlProperty::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QQmlProperty::type() const
    return QQmlProperty.Type(self.uglySide.call(
        'ritual_ZNK12QQmlProperty4typeEv',
    ))

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlProperty::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#isValid
    """
    #  bool QQmlProperty::isValid() const
    return self.uglySide.call('ritual_ZNK12QQmlProperty7isValidEv')

  def isProperty(self) -> bool:
    """
    Calls Qt's 'bool QQmlProperty::isProperty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#isProperty
    """
    #  bool QQmlProperty::isProperty() const
    return self.uglySide.call('ritual_ZNK12QQmlProperty10isPropertyEv')

  def isSignalProperty(self) -> bool:
    """
    Calls Qt's 'bool QQmlProperty::isSignalProperty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#isSignalProperty
    """
    #  bool QQmlProperty::isSignalProperty() const
    return self.uglySide.call('ritual_ZNK12QQmlProperty16isSignalPropertyEv')

  def propertyType(self) -> int:
    """
    Calls Qt's 'int QQmlProperty::propertyType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#propertyType
    """
    #  int QQmlProperty::propertyType() const
    return self.uglySide.call('ritual_ZNK12QQmlProperty12propertyTypeEv')

  def propertyMetaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QQmlProperty::propertyMetaType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#propertyMetaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QQmlProperty::propertyMetaType() const
    address = self.uglySide.call(
        'ritual_ZNK12QQmlProperty16propertyMetaTypeEv',
    )
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  def propertyTypeCategory(self) -> PropertyTypeCategory:
    """
    Calls Qt's 'PropertyTypeCategory QQmlProperty::propertyTypeCategory()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlproperty.html#propertyTypeCategory

    Returns
    -------

    PropertyTypeCategory
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'PropertyTypeCategory(number)' gives.
    """
    #  PropertyTypeCategory QQmlProperty::propertyTypeCategory() const
    return QQmlProperty.PropertyTypeCategory(self.uglySide.call(
        'ritual_ZNK12QQmlProperty20propertyTypeCategoryEv',
    ))

  def propertyTypeName(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QQmlProperty::propertyTypeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#propertyTypeName

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QQmlProperty::propertyTypeName() const
    chars = self.uglySide.call(
        'ritual_ZNK12QQmlProperty16propertyTypeNameEv',
    )
    return None if chars is None else chars.decode()

  def name(self) -> str:
    """
    Calls Qt's 'QString QQmlProperty::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlProperty::name() const
    return self.uglySide.call('ritual_ZNK12QQmlProperty4nameEv')

  @overload()
  def read(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlProperty::read() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#read

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlProperty::read() const
    address = self.uglySide.call('ritual_ZNK12QQmlProperty4readEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @staticmethod
  @overload(QObject, str)
  @overload(NoneType, str)
  def read(a0: Optional[QObject], a1: str) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlProperty::read(const QObject *a0, const QString
    &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#read

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlProperty::read(const QObject *a0, const QString &a1)
    address = Rituals.call(
        'ritual_ZN12QQmlProperty4readEPK7QObjectRK7QString',
        CuteMixin._addressOf(a0, 'QObject'), a1,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @staticmethod
  @overload(QObject, str, QQmlContext)
  @overload(QObject, str, NoneType)
  @overload(NoneType, str, QQmlContext)
  @overload(NoneType, str, NoneType)
  def read(
      a0: Optional[QObject],
      a1: str,
      a2: Optional[QQmlContext],
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlProperty::read(const QObject *a0, const QString
    &a1, QQmlContext *a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#read

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : str
      Passed on as it is: a QString is made of it for the call.

    a2 : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlProperty::read(const QObject *a0, const QString &a1,
    #      QQmlContext *a2)
    address = Rituals.call(
        'ritual_ZN12QQmlProperty4readEPK7QObjectRK7QStringP11QQmlContext',
        CuteMixin._addressOf(a0, 'QObject'), a1, CuteMixin._addressOf(a2),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @staticmethod
  @overload(QObject, str, QQmlEngine)
  @overload(NoneType, str, QQmlEngine)
  def read(
      a0: Optional[QObject],
      a1: str,
      a2: Optional[QQmlEngine],
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlProperty::read(const QObject *a0, const QString
    &a1, QQmlEngine *a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#read

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : str
      Passed on as it is: a QString is made of it for the call.

    a2 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlProperty::read(const QObject *a0, const QString &a1,
    #      QQmlEngine *a2)
    address = Rituals.call(
        'ritual_ZN12QQmlProperty4readEPK7QObjectRK7QStringP10QQmlEngine',
        CuteMixin._addressOf(a0, 'QObject'), a1, CuteMixin._addressOf(a2),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QVariant)
  def write(self, a0: QVariant) -> bool:
    """
    Calls Qt's 'bool QQmlProperty::write(const QVariant &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#write

    Parameters
    ----------

    a0 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QQmlProperty::write(const QVariant &a0) const
    return self.uglySide.call(
        'ritual_ZNK12QQmlProperty5writeERK8QVariant', self._valueOf(a0),
    )

  @staticmethod
  @overload(QObject, str, QVariant)
  @overload(NoneType, str, QVariant)
  def write(a0: Optional[QObject], a1: str, a2: QVariant) -> bool:
    """
    Calls Qt's 'bool QQmlProperty::write(QObject *a0, const QString &a1,
    const QVariant &a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#write

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : str
      Passed on as it is: a QString is made of it for the call.

    a2 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QQmlProperty::write(QObject *a0, const QString &a1, const
    #      QVariant &a2)
    return Rituals.call(
        'ritual_ZN12QQmlProperty5writeEP7QObjectRK7QStringRK8QVariant',
        CuteMixin._addressOf(a0, 'QObject'), a1, CuteMixin._valueOf(a2),
    )

  @staticmethod
  @overload(QObject, str, QVariant, QQmlContext)
  @overload(QObject, str, QVariant, NoneType)
  @overload(NoneType, str, QVariant, QQmlContext)
  @overload(NoneType, str, QVariant, NoneType)
  def write(
      a0: Optional[QObject],
      a1: str,
      a2: QVariant,
      a3: Optional[QQmlContext],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlProperty::write(QObject *a0, const QString &a1,
    const QVariant &a2, QQmlContext *a3)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#write

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : str
      Passed on as it is: a QString is made of it for the call.

    a2 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    a3 : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlProperty::write(QObject *a0, const QString &a1, const
    #      QVariant &a2, QQmlContext *a3)
    return Rituals.call(
        'ritual_ZN12QQmlProperty5writeEP7QObjectRK7QStringRK8QVariantP11QQm'
        'lContext',
        CuteMixin._addressOf(a0, 'QObject'), a1, CuteMixin._valueOf(a2),
        CuteMixin._addressOf(a3),
    )

  @staticmethod
  @overload(QObject, str, QVariant, QQmlEngine)
  @overload(NoneType, str, QVariant, QQmlEngine)
  def write(
      a0: Optional[QObject],
      a1: str,
      a2: QVariant,
      a3: Optional[QQmlEngine],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlProperty::write(QObject *a0, const QString &a1,
    const QVariant &a2, QQmlEngine *a3)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#write

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : str
      Passed on as it is: a QString is made of it for the call.

    a2 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    a3 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlProperty::write(QObject *a0, const QString &a1, const
    #      QVariant &a2, QQmlEngine *a3)
    return Rituals.call(
        'ritual_ZN12QQmlProperty5writeEP7QObjectRK7QStringRK8QVariantP10QQm'
        'lEngine',
        CuteMixin._addressOf(a0, 'QObject'), a1, CuteMixin._valueOf(a2),
        CuteMixin._addressOf(a3),
    )

  def reset(self) -> bool:
    """
    Calls Qt's 'bool QQmlProperty::reset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#reset
    """
    #  bool QQmlProperty::reset() const
    return self.uglySide.call('ritual_ZNK12QQmlProperty5resetEv')

  def hasNotifySignal(self) -> bool:
    """
    Calls Qt's 'bool QQmlProperty::hasNotifySignal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#hasNotifySignal
    """
    #  bool QQmlProperty::hasNotifySignal() const
    return self.uglySide.call('ritual_ZNK12QQmlProperty15hasNotifySignalEv')

  def needsNotifySignal(self) -> bool:
    """
    Calls Qt's 'bool QQmlProperty::needsNotifySignal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlproperty.html#needsNotifySignal
    """
    #  bool QQmlProperty::needsNotifySignal() const
    return self.uglySide.call(
        'ritual_ZNK12QQmlProperty17needsNotifySignalEv',
    )

  @overload(QObject, str)
  @overload(QObject, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def connectNotifySignal(
      self,
      dest: Optional[QObject],
      slot: Optional[str],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlProperty::connectNotifySignal(QObject *dest, const
    char *slot) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlproperty.html#connectNotifySignal

    Parameters
    ----------

    dest : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    slot : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QQmlProperty::connectNotifySignal(QObject *dest, const char
    #      *slot) const
    return self.uglySide.call(
        'ritual_ZNK12QQmlProperty19connectNotifySignalEP7QObjectPKc',
        self._addressOf(dest, 'QObject'), self._bytesOf(slot),
    )

  @overload(QObject, int)
  @overload(NoneType, int)
  def connectNotifySignal(
      self,
      dest: Optional[QObject],
      method: int,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlProperty::connectNotifySignal(QObject *dest, int
    method) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlproperty.html#connectNotifySignal

    Parameters
    ----------

    dest : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    method : int
      Passed on as it is.
    """
    #  bool QQmlProperty::connectNotifySignal(QObject *dest, int method)
    #      const
    return self.uglySide.call(
        'ritual_ZNK12QQmlProperty19connectNotifySignalEP7QObjecti',
        self._addressOf(dest, 'QObject'), method,
    )

  def isWritable(self) -> bool:
    """
    Calls Qt's 'bool QQmlProperty::isWritable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#isWritable
    """
    #  bool QQmlProperty::isWritable() const
    return self.uglySide.call('ritual_ZNK12QQmlProperty10isWritableEv')

  def isBindable(self) -> bool:
    """
    Calls Qt's 'bool QQmlProperty::isBindable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#isBindable
    """
    #  bool QQmlProperty::isBindable() const
    return self.uglySide.call('ritual_ZNK12QQmlProperty10isBindableEv')

  def isDesignable(self) -> bool:
    """
    Calls Qt's 'bool QQmlProperty::isDesignable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#isDesignable
    """
    #  bool QQmlProperty::isDesignable() const
    return self.uglySide.call('ritual_ZNK12QQmlProperty12isDesignableEv')

  def isResettable(self) -> bool:
    """
    Calls Qt's 'bool QQmlProperty::isResettable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#isResettable
    """
    #  bool QQmlProperty::isResettable() const
    return self.uglySide.call('ritual_ZNK12QQmlProperty12isResettableEv')

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlProperty::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlProperty::object() const
    address = self.uglySide.call('ritual_ZNK12QQmlProperty6objectEv')
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def index(self) -> int:
    """
    Calls Qt's 'int QQmlProperty::index() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#index
    """
    #  int QQmlProperty::index() const
    return self.uglySide.call('ritual_ZNK12QQmlProperty5indexEv')

  def property(self) -> QMetaProperty:
    """
    Calls Qt's 'QMetaProperty QQmlProperty::property() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#property

    Returns
    -------

    QMetaProperty
      A new cute QMetaProperty around the copy Qt gave back. Python owns it.
    """
    #  QMetaProperty QQmlProperty::property() const
    address = self.uglySide.call('ritual_ZNK12QQmlProperty8propertyEv')
    from ..QtCore import QMetaProperty
    return QMetaProperty._cuteOwning(address)

  def method(self) -> QMetaMethod:
    """
    Calls Qt's 'QMetaMethod QQmlProperty::method() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#method

    Returns
    -------

    QMetaMethod
      A new cute QMetaMethod around the copy Qt gave back. Python owns it.
    """
    #  QMetaMethod QQmlProperty::method() const
    address = self.uglySide.call('ritual_ZNK12QQmlProperty6methodEv')
    from ..QtCore import QMetaMethod
    return QMetaMethod._cuteOwning(address)

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
  def __eq__(self, a0: QQmlProperty) -> bool:
    """
    Calls Qt's 'bool QQmlProperty::operator==(const QQmlProperty &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#operator==

    Parameters
    ----------

    a0 : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.
    """
    #  bool QQmlProperty::operator==(const QQmlProperty &a0) const
    return self.uglySide.call(
        'ritual_ZNK12QQmlPropertyeqERKS_', self._valueOf(a0),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QQmlProperty::QQmlProperty()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#QQmlProperty
    """
    #  QQmlProperty::QQmlProperty()
    self._noteCreation(QQmlProperty, lambda: Rituals.call(
        'ritual_ZN12QQmlPropertyC1Ev',
    ))

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, a0: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QQmlProperty::QQmlProperty(QObject *a0)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#QQmlProperty

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlProperty::QQmlProperty(QObject *a0)
    self._noteCreation(QQmlProperty, lambda: Rituals.call(
        'ritual_ZN12QQmlPropertyC1EP7QObject',
        self._addressOf(a0, 'QObject'),
    ))

  @overload(QObject, QQmlContext)
  @overload(QObject, NoneType)
  @overload(NoneType, QQmlContext)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      a0: Optional[QObject],
      a1: Optional[QQmlContext],
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlProperty::QQmlProperty(QObject *a0,
    QQmlContext *a1)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#QQmlProperty

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlProperty::QQmlProperty(QObject *a0, QQmlContext *a1)
    self._noteCreation(QQmlProperty, lambda: Rituals.call(
        'ritual_ZN12QQmlPropertyC1EP7QObjectP11QQmlContext',
        self._addressOf(a0, 'QObject'), self._addressOf(a1),
    ))

  @overload(QObject, QQmlEngine)
  @overload(NoneType, QQmlEngine)
  def __init__(
      self,
      a0: Optional[QObject],
      a1: Optional[QQmlEngine],
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlProperty::QQmlProperty(QObject *a0,
    QQmlEngine *a1)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#QQmlProperty

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlProperty::QQmlProperty(QObject *a0, QQmlEngine *a1)
    self._noteCreation(QQmlProperty, lambda: Rituals.call(
        'ritual_ZN12QQmlPropertyC1EP7QObjectP10QQmlEngine',
        self._addressOf(a0, 'QObject'), self._addressOf(a1),
    ))

  @overload(QObject, str)
  @overload(NoneType, str)
  def __init__(self, a0: Optional[QObject], a1: str) -> None:
    """
    Notes what was given, for Qt's 'QQmlProperty::QQmlProperty(QObject *a0,
    const QString &a1)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#QQmlProperty

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QQmlProperty::QQmlProperty(QObject *a0, const QString &a1)
    self._noteCreation(QQmlProperty, lambda: Rituals.call(
        'ritual_ZN12QQmlPropertyC1EP7QObjectRK7QString',
        self._addressOf(a0, 'QObject'), a1,
    ))

  @overload(QObject, str, QQmlContext)
  @overload(QObject, str, NoneType)
  @overload(NoneType, str, QQmlContext)
  @overload(NoneType, str, NoneType)
  def __init__(
      self,
      a0: Optional[QObject],
      a1: str,
      a2: Optional[QQmlContext],
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlProperty::QQmlProperty(QObject *a0,
    const QString &a1, QQmlContext *a2)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#QQmlProperty

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : str
      Passed on as it is: a QString is made of it for the call.

    a2 : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlProperty::QQmlProperty(QObject *a0, const QString &a1, QQmlContext
    #      *a2)
    self._noteCreation(QQmlProperty, lambda: Rituals.call(
        'ritual_ZN12QQmlPropertyC1EP7QObjectRK7QStringP11QQmlContext',
        self._addressOf(a0, 'QObject'), a1, self._addressOf(a2),
    ))

  @overload(QObject, str, QQmlEngine)
  @overload(NoneType, str, QQmlEngine)
  def __init__(
      self,
      a0: Optional[QObject],
      a1: str,
      a2: Optional[QQmlEngine],
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlProperty::QQmlProperty(QObject *a0,
    const QString &a1, QQmlEngine *a2)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#QQmlProperty

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : str
      Passed on as it is: a QString is made of it for the call.

    a2 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlProperty::QQmlProperty(QObject *a0, const QString &a1, QQmlEngine
    #      *a2)
    self._noteCreation(QQmlProperty, lambda: Rituals.call(
        'ritual_ZN12QQmlPropertyC1EP7QObjectRK7QStringP10QQmlEngine',
        self._addressOf(a0, 'QObject'), a1, self._addressOf(a2),
    ))

  @overload(THIS)
  def __init__(self, a0: QQmlProperty) -> None:
    """
    Notes what was given, for Qt's 'QQmlProperty::QQmlProperty(const
    QQmlProperty &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproperty.html#QQmlProperty

    Parameters
    ----------

    a0 : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.
    """
    #  QQmlProperty::QQmlProperty(const QQmlProperty &a0)
    self._noteCreation(QQmlProperty, lambda: Rituals.call(
        'ritual_ZN12QQmlPropertyC1ERKS_', self._valueOf(a0),
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QQmlProperty::swap(QQmlProperty &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlProperty.swap' has no cute function yet. Qt's 'void "
        "QQmlProperty::swap(QQmlProperty &other)': takes a type Python has "
        "no way to hand over yet.")


#  Qt's 'QList<QQmlProperty>': the list of QQmlProperty, which
#  'QList[QQmlProperty]' gives. It is made here, so that there is one as soon
#  as there can be a QQmlProperty. Qt has a name of its own for it.
QQmlProperties = QList.createKind(
    QQmlProperty, 'value',
    name='QQmlProperties',
    make='ritual_list_make_QQmlProperty',
    add='ritual_list_add_QQmlProperty',
    size='ritual_list_size_QQmlProperty',
    at='ritual_list_at_QQmlProperty',
    drop='ritual_list_drop_QQmlProperty',
)
