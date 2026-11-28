"""
QQmlMetaTypeData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlmetatypedata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlMetaTypeData to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlPropertyCache

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QMetaType, QTypeRevision
  from . import QQmlType, QQmlTypeModule, QQmlTypePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']
  QMetaType = WAIT['QMetaType']
  QQmlType = WAIT['QQmlType']
  QQmlTypePrivate = WAIT['QQmlTypePrivate']
  QTypeRevision = WAIT['QTypeRevision']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlMetaTypeData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlMetaTypeData: a plain Python object standing in
  front of one C++ QQmlMetaTypeData.

  C++ hands a QQmlMetaTypeData around as a copy, so every C++
  QQmlMetaTypeData behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlMetaTypeData that has a ritual and that Python
  can call so far, 10 names in all: 'registerType', 'findTypeModule',
  'registerModuleTypes', 'propertyCacheForVersion',
  'setPropertyCacheForVersion', 'propertyCache',
  'findPropertyCacheInCompositeTypes', 'recordTypeRegFailure',
  'clearCompositeTypes', 'clearCompositeMetaTypes'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlMetaTypeData::~QQmlMetaTypeData()': the destructor: Python
    removes its C++ QQmlMetaTypeData by it, and has no other use for it.
  - Qt's 'QQmlPropertyCache::ConstPtr
    QQmlMetaTypeData::propertyCacheForPotentialInlineComponentType(QMetaType
    t, const QQmlMetaTypeData::CompositeTypes::const_iterator &iter)': takes
    a type Python has no way to hand over yet.
  - Qt's 'void QQmlMetaTypeData::setTypeRegistrationFailures(QStringList
    *failures)': names 'QStringList', which has no cute class yet.
  - Qt's 'void QQmlMetaTypeData::clearCompositeType(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &cu)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 17 functions Qt declares: 1 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QQmlMetaTypeData is created at the first use, not by
    'QQmlMetaTypeData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlMetaTypeData back gives a copy the ritual made
    for Python, in a new cute QQmlMetaTypeData.
  - Each name of Qt's QQmlMetaTypeData that has no cute function yet,
    'addTypeModule', 'clearCompositeType',
    'propertyCacheForPotentialInlineComponentType',
    'setTypeRegistrationFailures', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QQmlMetaTypeData, each a class in here as
  #  in C++.

  class CompositeMetaTypes(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlMetaTypeData::CompositeMetaTypes: a plain
    Python object standing in front of one C++
    QQmlMetaTypeData::CompositeMetaTypes.

    C++ hands a QQmlMetaTypeData::CompositeMetaTypes around as a copy, so
    every C++ QQmlMetaTypeData::CompositeMetaTypes behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QQmlMetaTypeData::CompositeMetaTypes yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlMetaTypeData::CompositeMetaTypes::~CompositeMetaTypes()': the
      destructor: Python removes its C++ QQmlMetaTypeData::CompositeMetaTypes
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQmlMetaTypeData::CompositeMetaTypes is created at the first
      use, not by 'QQmlMetaTypeData::CompositeMetaTypes(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlMetaTypeData::CompositeMetaTypes back gives a
      copy the ritual made for Python, in a new cute
      QQmlMetaTypeData::CompositeMetaTypes.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlMetaTypeData::CompositeMetaTypes'

    #  Qt's '~QQmlMetaTypeData::CompositeMetaTypes()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QQmlMetaTypeData::CompositeMetaTypes behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN16QQmlMetaTypeData18CompositeMetaTypesD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class Type(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlMetaTypeData::Type: a plain Python object
    standing in front of one C++ QQmlMetaTypeData::Type.

    C++ hands a QQmlMetaTypeData::Type around as a copy, so every C++
    QQmlMetaTypeData::Type behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QQmlMetaTypeData::Type yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlMetaTypeData::Type::~Type()': the destructor: Python removes
      its C++ QQmlMetaTypeData::Type by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQmlMetaTypeData::Type is created at the first use, not by
      'QQmlMetaTypeData::Type(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlMetaTypeData::Type back gives a copy the ritual
      made for Python, in a new cute QQmlMetaTypeData::Type.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlMetaTypeData::Type'

    #  Qt's '~QQmlMetaTypeData::Type()'. Naming it makes this a value class:
    #  Python owns every C++ QQmlMetaTypeData::Type behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QQmlMetaTypeData4TypeD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class VersionedUri(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlMetaTypeData::VersionedUri: a plain Python
    object standing in front of one C++ QQmlMetaTypeData::VersionedUri.

    C++ hands a QQmlMetaTypeData::VersionedUri around as a copy, so every C++
    QQmlMetaTypeData::VersionedUri behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QQmlMetaTypeData::VersionedUri that has a ritual
    and that Python can call so far, 2 names in all: '__eq__', '__lt__'. It
    can be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlMetaTypeData::VersionedUri::VersionedUri(const
      std::unique_ptr<QQmlTypeModule> &module)': takes a type Python has no
      way to hand over yet.
    - Qt's 'QQmlMetaTypeData::VersionedUri::~VersionedUri()': the destructor:
      Python removes its C++ QQmlMetaTypeData::VersionedUri by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQmlMetaTypeData::VersionedUri is created at the first use, not
      by 'QQmlMetaTypeData::VersionedUri(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlMetaTypeData::VersionedUri back gives a copy
      the ritual made for Python, in a new cute
      QQmlMetaTypeData::VersionedUri.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QTypeRevision = WAIT['QTypeRevision']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlMetaTypeData::VersionedUri'

    #  Qt's '~QQmlMetaTypeData::VersionedUri()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlMetaTypeData::VersionedUri behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QQmlMetaTypeData12VersionedUriD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(THIS)
    def __eq__(self, b: QQmlMetaTypeData.VersionedUri) -> bool:
      """
      Calls Qt's 'bool operator==(const VersionedUri &a, const VersionedUri
      &b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlmetatypedata-versioneduri.html#operator==

      Parameters
      ----------

      b : QQmlMetaTypeData.VersionedUri
        Passed on as a value: Qt reads the C++
        QQmlMetaTypeData::VersionedUri, which stays Python's own.
      """
      #  bool operator==(const VersionedUri &a, const VersionedUri &b)
      return Rituals.call(
          'ritual_ZeqRKN16QQmlMetaTypeData12VersionedUriES2_',
          CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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
    def __lt__(self, b: QQmlMetaTypeData.VersionedUri) -> bool:
      """
      Calls Qt's 'bool operator<(const QQmlMetaTypeData::VersionedUri &a,
      const QQmlMetaTypeData::VersionedUri &b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlmetatypedata-versioneduri.html#operator<

      Parameters
      ----------

      b : QQmlMetaTypeData.VersionedUri
        Passed on as a value: Qt reads the C++
        QQmlMetaTypeData::VersionedUri, which stays Python's own.
      """
      #  bool operator<(const QQmlMetaTypeData::VersionedUri &a, const
      #      QQmlMetaTypeData::VersionedUri &b)
      return Rituals.call(
          'ritual_ZltRKN16QQmlMetaTypeData12VersionedUriES2_',
          CuteMixin._valueOf(self), CuteMixin._valueOf(b),
      )

    @overload.fallback
    def __lt__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QQmlMetaTypeData::VersionedUri::VersionedUri()', which is called at
      the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlmetatypedata-versioneduri.html#VersionedUri
      """
      #  QQmlMetaTypeData::VersionedUri::VersionedUri()
      self._noteCreation(QQmlMetaTypeData.VersionedUri, lambda: Rituals.call(
          'ritual_ZN16QQmlMetaTypeData12VersionedUriC1Ev',
      ))

    @overload(str, QTypeRevision)
    def __init__(self, uri: str, version: QTypeRevision) -> None:
      """
      Notes what was given, for Qt's
      'QQmlMetaTypeData::VersionedUri::VersionedUri(const QString &uri,
      QTypeRevision version)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlmetatypedata-versioneduri.html#VersionedUri

      Parameters
      ----------

      uri : str
        Passed on as it is: a QString is made of it for the call.

      version : QTypeRevision
        Passed on as a value: Qt reads the C++ QTypeRevision, which stays
        Python's own.
      """
      #  QQmlMetaTypeData::VersionedUri::VersionedUri(const QString &uri,
      #      QTypeRevision version)
      self._noteCreation(QQmlMetaTypeData.VersionedUri, lambda: Rituals.call(
          'ritual_ZN16QQmlMetaTypeData12VersionedUriC1ERK7QString13QTypeRev'
          'ision',
          uri, self._valueOf(version),
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlMetaTypeData'

  #  Qt's '~QQmlMetaTypeData()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlMetaTypeData behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QQmlMetaTypeDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QTypeRevision)
  def propertyCacheForVersion(
      self,
      index: int,
      version: QTypeRevision,
  ) -> QQmlPropertyCache.ConstPtr:
    """
    Calls Qt's 'QQmlPropertyCache::ConstPtr
    QQmlMetaTypeData::propertyCacheForVersion(int index, QTypeRevision
    version) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatypedata.html#propertyCacheForVersion

    Parameters
    ----------

    index : int
      Passed on as it is.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    Returns
    -------

    QQmlPropertyCache.ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlPropertyCache::ConstPtr
    #      QQmlMetaTypeData::propertyCacheForVersion(int index, QTypeRevision
    #      version) const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlMetaTypeData23propertyCacheForVersionEi13QTypeRevi'
        'sion',
        index, self._valueOf(version),
    )
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

  @overload(QMetaType)
  def findPropertyCacheInCompositeTypes(
      self,
      t: QMetaType,
  ) -> QQmlPropertyCache.ConstPtr:
    """
    Calls Qt's 'QQmlPropertyCache::ConstPtr
    QQmlMetaTypeData::findPropertyCacheInCompositeTypes(QMetaType t) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatypedata.html

    Parameters
    ----------

    t : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    QQmlPropertyCache.ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlPropertyCache::ConstPtr
    #      QQmlMetaTypeData::findPropertyCacheInCompositeTypes(QMetaType t)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlMetaTypeData33findPropertyCacheInCompositeTypesE9Q'
        'MetaType',
        self._valueOf(t),
    )
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QTypeRevision, QQmlPropertyCache.ConstPtr)
  def setPropertyCacheForVersion(
      self,
      index: int,
      version: QTypeRevision,
      cache: QQmlPropertyCache.ConstPtr,
  ) -> None:
    """
    Calls Qt's 'void QQmlMetaTypeData::setPropertyCacheForVersion(int index,
    QTypeRevision version, const QQmlPropertyCache::ConstPtr &cache)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatypedata.html#setPropertyCacheForVersion

    Parameters
    ----------

    index : int
      Passed on as it is.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    cache : QQmlPropertyCache.ConstPtr
      Passed on as a value: Qt reads the C++ QQmlPropertyCache::ConstPtr,
      which stays Python's own.
    """
    #  void QQmlMetaTypeData::setPropertyCacheForVersion(int index,
    #      QTypeRevision version, const QQmlPropertyCache::ConstPtr &cache)
    self.uglySide.call(
        'ritual_ZN16QQmlMetaTypeData26setPropertyCacheForVersionEi13QTypeRe'
        'visionRKN17QQmlPropertyCache8ConstPtrE',
        index, self._valueOf(version), self._valueOf(cache),
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
    Notes what was given, for Qt's 'QQmlMetaTypeData::QQmlMetaTypeData()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatypedata.html#QQmlMetaTypeData
    """
    #  QQmlMetaTypeData::QQmlMetaTypeData()
    self._noteCreation(QQmlMetaTypeData, lambda: Rituals.call(
        'ritual_ZN16QQmlMetaTypeDataC1Ev',
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

  @overload(QQmlTypePrivate)
  @overload(NoneType)
  def registerType(self, priv: Optional[QQmlTypePrivate]) -> None:
    """
    Calls Qt's 'void QQmlMetaTypeData::registerType(QQmlTypePrivate *priv)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatypedata.html#registerType

    Parameters
    ----------

    priv : Optional[QQmlTypePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlMetaTypeData::registerType(QQmlTypePrivate *priv)
    self.uglySide.call(
        'ritual_ZN16QQmlMetaTypeData12registerTypeEP15QQmlTypePrivate',
        self._addressOf(priv),
    )

  @overload(str, QTypeRevision)
  def findTypeModule(
      self,
      module: str,
      version: QTypeRevision,
  ) -> Optional[QQmlTypeModule]:
    """
    Calls Qt's 'QQmlTypeModule *QQmlMetaTypeData::findTypeModule(const
    QString &module, QTypeRevision version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatypedata.html#findTypeModule

    Parameters
    ----------

    module : str
      Passed on as it is: a QString is made of it for the call.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    Returns
    -------

    Optional[QQmlTypeModule]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlTypeModule *QQmlMetaTypeData::findTypeModule(const QString
    #      &module, QTypeRevision version)
    address = self.uglySide.call(
        'ritual_ZN16QQmlMetaTypeData14findTypeModuleERK7QString13QTypeRevis'
        'ion',
        module, self._valueOf(version),
    )
    from . import QQmlTypeModule
    return QQmlTypeModule._cuteAt(address)

  @overload(str)
  def registerModuleTypes(self, uri: str) -> bool:
    """
    Calls Qt's 'bool QQmlMetaTypeData::registerModuleTypes(const QString
    &uri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatypedata.html#registerModuleTypes

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlMetaTypeData::registerModuleTypes(const QString &uri)
    return self.uglySide.call(
        'ritual_ZN16QQmlMetaTypeData19registerModuleTypesERK7QString', uri,
    )

  @overload(QMetaObject, QTypeRevision)
  @overload(NoneType, QTypeRevision)
  def propertyCache(
      self,
      metaObject: Optional[QMetaObject],
      version: QTypeRevision,
  ) -> QQmlPropertyCache.ConstPtr:
    """
    Calls Qt's 'QQmlPropertyCache::ConstPtr
    QQmlMetaTypeData::propertyCache(const QMetaObject *metaObject,
    QTypeRevision version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatypedata.html#propertyCache

    Parameters
    ----------

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    Returns
    -------

    QQmlPropertyCache.ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlPropertyCache::ConstPtr QQmlMetaTypeData::propertyCache(const
    #      QMetaObject *metaObject, QTypeRevision version)
    address = self.uglySide.call(
        'ritual_ZN16QQmlMetaTypeData13propertyCacheEPK11QMetaObject13QTypeR'
        'evision',
        self._addressOf(metaObject, 'QMetaObject'), self._valueOf(version),
    )
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

  @overload(QQmlType, QTypeRevision)
  def propertyCache(
      self,
      type: QQmlType,
      version: QTypeRevision,
  ) -> QQmlPropertyCache.ConstPtr:
    """
    Calls Qt's 'QQmlPropertyCache::ConstPtr
    QQmlMetaTypeData::propertyCache(const QQmlType &type, QTypeRevision
    version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatypedata.html#propertyCache

    Parameters
    ----------

    type : QQmlType
      Passed on as a value: Qt reads the C++ QQmlType, which stays Python's
      own.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    Returns
    -------

    QQmlPropertyCache.ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlPropertyCache::ConstPtr QQmlMetaTypeData::propertyCache(const
    #      QQmlType &type, QTypeRevision version)
    address = self.uglySide.call(
        'ritual_ZN16QQmlMetaTypeData13propertyCacheERK8QQmlType13QTypeRevis'
        'ion',
        self._valueOf(type), self._valueOf(version),
    )
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

  @overload(str)
  def recordTypeRegFailure(self, message: str) -> None:
    """
    Calls Qt's 'void QQmlMetaTypeData::recordTypeRegFailure(const QString
    &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatypedata.html#recordTypeRegFailure

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlMetaTypeData::recordTypeRegFailure(const QString &message)
    self.uglySide.call(
        'ritual_ZN16QQmlMetaTypeData20recordTypeRegFailureERK7QString',
        message,
    )

  def clearCompositeTypes(self) -> None:
    """
    Calls Qt's 'void QQmlMetaTypeData::clearCompositeTypes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatypedata.html#clearCompositeTypes
    """
    #  void QQmlMetaTypeData::clearCompositeTypes()
    self.uglySide.call('ritual_ZN16QQmlMetaTypeData19clearCompositeTypesEv')

  def clearCompositeMetaTypes(self) -> None:
    """
    Calls Qt's 'void QQmlMetaTypeData::clearCompositeMetaTypes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatypedata.html#clearCompositeMetaTypes
    """
    #  void QQmlMetaTypeData::clearCompositeMetaTypes()
    self.uglySide.call(
        'ritual_ZN16QQmlMetaTypeData23clearCompositeMetaTypesEv',
    )

  @staticmethod
  def addTypeModule(*__, **_) -> Never:
    """
    Qt's 'QQmlTypeModule
    *QQmlMetaTypeData::addTypeModule(std::unique_ptr<QQmlTypeModule>
    module)': the compiler refuses its ritual as it would be written here:
    call to deleted constructor of 'std::unique_ptr<QQmlTypeModule>'.
    """
    raise NotImplementedError(
        "'QQmlMetaTypeData.addTypeModule' has no cute function yet. Qt's "
        "'QQmlTypeModule "
        "*QQmlMetaTypeData::addTypeModule(std::unique_ptr<QQmlTypeModule> "
        "module)': the compiler refuses its ritual as it would be written "
        "here: call to deleted constructor of "
        "'std::unique_ptr<QQmlTypeModule>'.")

  @staticmethod
  def clearCompositeType(*__, **_) -> Never:
    """
    Qt's 'void QQmlMetaTypeData::clearCompositeType(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &cu)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlMetaTypeData.clearCompositeType' has no cute function yet. "
        "Qt's 'void QQmlMetaTypeData::clearCompositeType(const "
        "QQmlRefPointer<QV4::CompiledData::CompilationUnit> &cu)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def propertyCacheForPotentialInlineComponentType(*__, **_) -> Never:
    """
    Qt's 'QQmlPropertyCache::ConstPtr
    QQmlMetaTypeData::propertyCacheForPotentialInlineComponentType(QMetaType
    t, const QQmlMetaTypeData::CompositeTypes::const_iterator &iter)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlMetaTypeData.propertyCacheForPotentialInlineComponentType' "
        "has no cute function yet. Qt's 'QQmlPropertyCache::ConstPtr "
        "QQmlMetaTypeData::propertyCacheForPotentialInlineComponentType(QMet"
        "aType t, const QQmlMetaTypeData::CompositeTypes::const_iterator "
        "&iter)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setTypeRegistrationFailures(*__, **_) -> Never:
    """
    Qt's 'void QQmlMetaTypeData::setTypeRegistrationFailures(QStringList
    *failures)': names 'QStringList', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlMetaTypeData.setTypeRegistrationFailures' has no cute "
        "function yet. Qt's 'void "
        "QQmlMetaTypeData::setTypeRegistrationFailures(QStringList "
        "*failures)': names 'QStringList', which has no cute class yet.")
