"""
QDesignerMetaPropertyInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/abstractintrospection_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDesignerMetaPropertyInterface to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QVariant
  from . import QDesignerMetaEnumInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerMetaPropertyInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerMetaPropertyInterface: a plain Python object
  standing in front of one C++ QDesignerMetaPropertyInterface.

  What exists
  -----------

  Every function of Qt's QDesignerMetaPropertyInterface that has a ritual and
  that Python can call so far, 12 names in all: 'enumerator', 'kind',
  'accessFlags', 'attributes', 'type', 'name', 'typeName', 'userType',
  'hasSetter', 'read', 'reset', 'write'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDesignerMetaPropertyInterface::~QDesignerMetaPropertyInterface()':
    the destructor: Python never removes a C++
    QDesignerMetaPropertyInterface.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QDesignerMetaPropertyInterface is created at the first use, not
    by 'QDesignerMetaPropertyInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerMetaPropertyInterface.
  """

  #  The enums Qt writes inside QDesignerMetaPropertyInterface, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class AccessFlag(CuteFlags):
    """
    The flags enum 'QDesignerMetaPropertyInterface::AccessFlag' of Qt, with
    the 3 names Qt gives in it. Qt names the type of its combinations
    'QDesignerMetaPropertyInterface::AccessFlags'.
    """

    ReadAccess = 0x1
    WriteAccess = 0x2
    ResetAccess = 0x4

  AccessFlags = AccessFlag

  class Attribute(CuteFlags):
    """
    The flags enum 'QDesignerMetaPropertyInterface::Attribute' of Qt, with
    the 4 names Qt gives in it. Qt names the type of its combinations
    'QDesignerMetaPropertyInterface::Attributes'.
    """

    DesignableAttribute = 0x1
    ScriptableAttribute = 0x2
    StoredAttribute = 0x4
    UserAttribute = 0x8

  Attributes = Attribute

  class Kind(CuteNum):
    """
    The enum 'QDesignerMetaPropertyInterface::Kind' of Qt, with the 3 names
    Qt gives in it.
    """

    EnumKind = Kee[int](0)
    FlagKind = Kee[int](1)
    OtherKind = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerMetaPropertyInterface'

  #  A C++ QDesignerMetaPropertyInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerMetaPropertyInterface'

  #  The functions Qt calls itself that QDesignerMetaPropertyInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'enumerator': (
          ('_ZNK30QDesignerMetaPropertyInterface10enumeratorEv',
           ('address', 'address', 'QtDesigner:QDesignerMetaEnumInterface'),
           ()),
      ),
      'kind': (
          ('_ZNK30QDesignerMetaPropertyInterface4kindEv',
           ('int', 'enum', 'QtDesigner:QDesignerMetaPropertyInterface.Kind'),
           ()),
      ),
      'accessFlags': (
          ('_ZNK30QDesignerMetaPropertyInterface11accessFlagsEv',
           ('int', 'flags',
            'QtDesigner:QDesignerMetaPropertyInterface.AccessFlag'),
           ()),
      ),
      'attributes': (
          ('_ZNK30QDesignerMetaPropertyInterface10attributesEv',
           ('int', 'flags',
            'QtDesigner:QDesignerMetaPropertyInterface.Attribute'),
           ()),
      ),
      'type': (
          ('_ZNK30QDesignerMetaPropertyInterface4typeEv',
           ('int', 'number', ''),
           ()),
      ),
      'name': (
          ('_ZNK30QDesignerMetaPropertyInterface4nameEv',
           ('address', 'text', ''),
           ()),
      ),
      'typeName': (
          ('_ZNK30QDesignerMetaPropertyInterface8typeNameEv',
           ('address', 'text', ''),
           ()),
      ),
      'userType': (
          ('_ZNK30QDesignerMetaPropertyInterface8userTypeEv',
           ('int', 'number', ''),
           ()),
      ),
      'hasSetter': (
          ('_ZNK30QDesignerMetaPropertyInterface9hasSetterEv',
           ('bool', 'number', ''),
           ()),
      ),
      'read': (
          ('_ZNK30QDesignerMetaPropertyInterface4readEPK7QObject',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'reset': (
          ('_ZNK30QDesignerMetaPropertyInterface5resetEP7QObject',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'write': (
          ('_ZNK30QDesignerMetaPropertyInterface5writeEP7QObjectRK8QVariant',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def enumerator(self) -> Optional[QDesignerMetaEnumInterface]:
    """
    Calls Qt's 'const QDesignerMetaEnumInterface
    *QDesignerMetaPropertyInterface::enumerator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetapropertyinterface.html#enumerator

    Returns
    -------

    Optional[QDesignerMetaEnumInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QDesignerMetaEnumInterface
    #      *QDesignerMetaPropertyInterface::enumerator() const
    address = self.uglySide.call(
        'ritual_ZNK30QDesignerMetaPropertyInterface10enumeratorEv',
    )
    from . import QDesignerMetaEnumInterface
    return QDesignerMetaEnumInterface._cuteAt(address)

  def kind(self) -> Kind:
    """
    Calls Qt's 'Kind QDesignerMetaPropertyInterface::kind() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetapropertyinterface.html#kind

    Returns
    -------

    Kind
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Kind(number)' gives.
    """
    #  Kind QDesignerMetaPropertyInterface::kind() const
    return QDesignerMetaPropertyInterface.Kind(self.uglySide.call(
        'ritual_ZNK30QDesignerMetaPropertyInterface4kindEv',
    ))

  def accessFlags(self) -> AccessFlags:
    """
    Calls Qt's 'AccessFlags QDesignerMetaPropertyInterface::accessFlags()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetapropertyinterface.html#accessFlags

    Returns
    -------

    AccessFlags
      The value standing for the combination Qt gave back.
    """
    #  AccessFlags QDesignerMetaPropertyInterface::accessFlags() const
    return QDesignerMetaPropertyInterface.AccessFlags(self.uglySide.call(
        'ritual_ZNK30QDesignerMetaPropertyInterface11accessFlagsEv',
    ))

  def attributes(self) -> Attributes:
    """
    Calls Qt's 'Attributes QDesignerMetaPropertyInterface::attributes()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetapropertyinterface.html#attributes

    Returns
    -------

    Attributes
      The value standing for the combination Qt gave back.
    """
    #  Attributes QDesignerMetaPropertyInterface::attributes() const
    return QDesignerMetaPropertyInterface.Attributes(self.uglySide.call(
        'ritual_ZNK30QDesignerMetaPropertyInterface10attributesEv',
    ))

  def type(self) -> int:
    """
    Calls Qt's 'int QDesignerMetaPropertyInterface::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetapropertyinterface.html#type
    """
    #  int QDesignerMetaPropertyInterface::type() const
    return self.uglySide.call(
        'ritual_ZNK30QDesignerMetaPropertyInterface4typeEv',
    )

  def name(self) -> str:
    """
    Calls Qt's 'QString QDesignerMetaPropertyInterface::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetapropertyinterface.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMetaPropertyInterface::name() const
    return self.uglySide.call(
        'ritual_ZNK30QDesignerMetaPropertyInterface4nameEv',
    )

  def typeName(self) -> str:
    """
    Calls Qt's 'QString QDesignerMetaPropertyInterface::typeName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetapropertyinterface.html#typeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMetaPropertyInterface::typeName() const
    return self.uglySide.call(
        'ritual_ZNK30QDesignerMetaPropertyInterface8typeNameEv',
    )

  def userType(self) -> int:
    """
    Calls Qt's 'int QDesignerMetaPropertyInterface::userType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetapropertyinterface.html#userType
    """
    #  int QDesignerMetaPropertyInterface::userType() const
    return self.uglySide.call(
        'ritual_ZNK30QDesignerMetaPropertyInterface8userTypeEv',
    )

  def hasSetter(self) -> bool:
    """
    Calls Qt's 'bool QDesignerMetaPropertyInterface::hasSetter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetapropertyinterface.html#hasSetter
    """
    #  bool QDesignerMetaPropertyInterface::hasSetter() const
    return self.uglySide.call(
        'ritual_ZNK30QDesignerMetaPropertyInterface9hasSetterEv',
    )

  @overload(QObject)
  @overload(NoneType)
  def read(self, object: Optional[QObject]) -> QVariant:
    """
    Calls Qt's 'QVariant QDesignerMetaPropertyInterface::read(const QObject
    *object) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetapropertyinterface.html#read

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDesignerMetaPropertyInterface::read(const QObject *object)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK30QDesignerMetaPropertyInterface4readEPK7QObject',
        self._addressOf(object, 'QObject'),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QObject)
  @overload(NoneType)
  def reset(self, object: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QDesignerMetaPropertyInterface::reset(QObject *object)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetapropertyinterface.html#reset

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerMetaPropertyInterface::reset(QObject *object) const
    return self.uglySide.call(
        'ritual_ZNK30QDesignerMetaPropertyInterface5resetEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(QObject, QVariant)
  @overload(NoneType, QVariant)
  def write(self, object: Optional[QObject], value: QVariant) -> bool:
    """
    Calls Qt's 'bool QDesignerMetaPropertyInterface::write(QObject *object,
    const QVariant &value) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetapropertyinterface.html#write

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QDesignerMetaPropertyInterface::write(QObject *object, const
    #      QVariant &value) const
    return self.uglySide.call(
        'ritual_ZNK30QDesignerMetaPropertyInterface5writeEP7QObjectRK8QVari'
        'ant',
        self._addressOf(object, 'QObject'), self._valueOf(value),
    )

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
    Notes what was given, for Qt's
    'QDesignerMetaPropertyInterface::QDesignerMetaPropertyInterface()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetapropertyinterface.html
    """
    #  QDesignerMetaPropertyInterface::QDesignerMetaPropertyInterface()
    self._noteCreation(QDesignerMetaPropertyInterface, lambda: Rituals.call(
        'ritual_ZN30QDesignerMetaPropertyInterfaceC1Ev',
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
