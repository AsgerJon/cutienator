"""
QQmlTypePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltype_p_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlTypePrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlPropertyCache, QQmlType, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from . import QQmlTypeLoader
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']
  QQmlTypeLoader = WAIT['QQmlTypeLoader']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlTypePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlTypePrivate: a plain Python object standing in
  front of one C++ QQmlTypePrivate.

  What exists
  -----------

  Every function of Qt's QQmlTypePrivate that has a ritual and that Python
  can call so far, 15 names in all: 'init', 'sourceUrl',
  'attachedPropertiesBase', 'isComposite', 'isValueType',
  'resolveCompositeBaseType', 'compositePropertyCache', 'setName',
  'metaObject', 'metaObjectForValueType', 'visibleQmlTypeByName',
  'initEnums', 'insertEnums', 'insertEnumsFromPropertyCache',
  'createEnumConflictReport'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlType QQmlTypePrivate::visibleQmlTypeByName(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &unit, const QString
    &elementName, QQmlTypeLoader *typeLoader)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QQmlTypePrivate::~QQmlTypePrivate()': the destructor: Python never
    removes a C++ QQmlTypePrivate.
  - Qt's 'void QQmlTypePrivate::createListOfPossibleConflictingItems(const
    QMetaObject *metaObject, QList<EnumInfo> &enumInfoList, QStringList path)
    const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  11 of the 30 functions Qt declares: 7 a template; 4 forbidden.

  What to expect
  --------------

  - The C++ QQmlTypePrivate is created at the first use, not by
    'QQmlTypePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlTypePrivate.
  - Each name of Qt's QQmlTypePrivate that has no cute function yet,
    'createListOfPossibleConflictingItems', 'doGetEnumOp', 'enumIndex',
    'enumKey', 'enumKeys', 'enumValue', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QQmlTypePrivate, each a class in here as in
  #  C++.

  class Enums(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlTypePrivate::Enums: a plain Python object
    standing in front of one C++ QQmlTypePrivate::Enums.

    C++ hands a QQmlTypePrivate::Enums around as a copy, so every C++
    QQmlTypePrivate::Enums behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QQmlTypePrivate::Enums yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlTypePrivate::Enums::~Enums()': the destructor: Python removes
      its C++ QQmlTypePrivate::Enums by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQmlTypePrivate::Enums is created at the first use, not by
      'QQmlTypePrivate::Enums(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlTypePrivate::Enums back gives a copy the ritual
      made for Python, in a new cute QQmlTypePrivate::Enums.
    """

    #  The enums Qt writes inside QQmlTypePrivate::Enums, each a class in
    #  here as in C++, and the names Qt has for the combinations of its flags
    #  enums.

    class Scoping(CuteNum):
      """
      The enum 'QQmlTypePrivate::Enums::Scoping' of Qt, with the 2 names Qt
      gives in it.
      """

      Scoped = Kee[int](0)
      Unscoped = Kee[int](1)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlTypePrivate::Enums'

    #  Qt's '~QQmlTypePrivate::Enums()'. Naming it makes this a value class:
    #  Python owns every C++ QQmlTypePrivate::Enums behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN15QQmlTypePrivate5EnumsD1Ev'

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

  class ProxyMetaObjects(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlTypePrivate::ProxyMetaObjects: a plain Python
    object standing in front of one C++ QQmlTypePrivate::ProxyMetaObjects.

    C++ hands a QQmlTypePrivate::ProxyMetaObjects around as a copy, so every
    C++ QQmlTypePrivate::ProxyMetaObjects behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQmlTypePrivate::ProxyMetaObjects yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlTypePrivate::ProxyMetaObjects::~ProxyMetaObjects()': the
      destructor: Python removes its C++ QQmlTypePrivate::ProxyMetaObjects by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQmlTypePrivate::ProxyMetaObjects is created at the first use,
      not by 'QQmlTypePrivate::ProxyMetaObjects(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlTypePrivate::ProxyMetaObjects back gives a copy
      the ritual made for Python, in a new cute
      QQmlTypePrivate::ProxyMetaObjects.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlTypePrivate::ProxyMetaObjects'

    #  Qt's '~QQmlTypePrivate::ProxyMetaObjects()'. Naming it makes this a
    #  value class: Python owns every C++ QQmlTypePrivate::ProxyMetaObjects
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN15QQmlTypePrivate16ProxyMetaObjectsD1Ev'

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

  class QQmlCppTypeData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlTypePrivate::QQmlCppTypeData: a plain Python
    object standing in front of one C++ QQmlTypePrivate::QQmlCppTypeData.

    C++ hands a QQmlTypePrivate::QQmlCppTypeData around as a copy, so every
    C++ QQmlTypePrivate::QQmlCppTypeData behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQmlTypePrivate::QQmlCppTypeData yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlTypePrivate::QQmlCppTypeData::~QQmlCppTypeData()': the
      destructor: Python removes its C++ QQmlTypePrivate::QQmlCppTypeData by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQmlTypePrivate::QQmlCppTypeData is created at the first use,
      not by 'QQmlTypePrivate::QQmlCppTypeData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlTypePrivate::QQmlCppTypeData back gives a copy
      the ritual made for Python, in a new cute
      QQmlTypePrivate::QQmlCppTypeData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlTypePrivate::QQmlCppTypeData'

    #  Qt's '~QQmlTypePrivate::QQmlCppTypeData()'. Naming it makes this a
    #  value class: Python owns every C++ QQmlTypePrivate::QQmlCppTypeData
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN15QQmlTypePrivate15QQmlCppTypeDataD1Ev'

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

  class QQmlSingletonTypeData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlTypePrivate::QQmlSingletonTypeData: a plain
    Python object standing in front of one C++
    QQmlTypePrivate::QQmlSingletonTypeData.

    C++ hands a QQmlTypePrivate::QQmlSingletonTypeData around as a copy, so
    every C++ QQmlTypePrivate::QQmlSingletonTypeData behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QQmlTypePrivate::QQmlSingletonTypeData yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QQmlTypePrivate::QQmlSingletonTypeData::~QQmlSingletonTypeData()': the
      destructor: Python removes its C++
      QQmlTypePrivate::QQmlSingletonTypeData by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QQmlTypePrivate::QQmlSingletonTypeData is created at the first
      use, not by 'QQmlTypePrivate::QQmlSingletonTypeData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlTypePrivate::QQmlSingletonTypeData back gives a
      copy the ritual made for Python, in a new cute
      QQmlTypePrivate::QQmlSingletonTypeData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlTypePrivate::QQmlSingletonTypeData'

    #  Qt's '~QQmlTypePrivate::QQmlSingletonTypeData()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QQmlTypePrivate::QQmlSingletonTypeData behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN15QQmlTypePrivate21QQmlSingletonTypeDataD1Ev')

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

  class extraData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlTypePrivate::extraData: a plain Python object
    standing in front of one C++ QQmlTypePrivate::extraData.

    What exists
    -----------

    No function of Qt's QQmlTypePrivate::extraData yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has no ritual
    ------------------

    2 of the 2 functions Qt declares: 2 the compiler refuses its ritual as it
    would be written here.

    What to expect
    --------------

    - The C++ QQmlTypePrivate::extraData is created at the first use, not by
      'QQmlTypePrivate::extraData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QQmlTypePrivate::extraData.
    - Each name of Qt's QQmlTypePrivate::extraData that has no cute function
      yet, '__init__', holds a function that raises 'NotImplementedError',
      and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlTypePrivate::extraData'

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

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      Qt's 'QQmlTypePrivate::extraData::extraData()': the compiler refuses
      its ritual as it would be written here: no type named 'extraData' in
      'QQmlTypePrivate'; did you mean 'QV4::GCStateMachine::ExtraData'?.
      """
      raise NotImplementedError(
          "'QQmlTypePrivate.extraData.__init__' has no cute function yet. "
          "Qt's 'QQmlTypePrivate::extraData::extraData()': the compiler "
          "refuses its ritual as it would be written here: no type named "
          "'extraData' in 'QQmlTypePrivate'; did you mean "
          "'QV4::GCStateMachine::ExtraData'?.")

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

  @staticmethod
  @overload(WAIT['QV4.ExecutableCompilationUnit'], int)
  @overload(NoneType, int)
  @overload(WAIT['QV4.ExecutableCompilationUnit'], int, QQmlTypeLoader)
  @overload(WAIT['QV4.ExecutableCompilationUnit'], int, NoneType)
  @overload(NoneType, int, QQmlTypeLoader)
  @overload(NoneType, int, NoneType)
  def visibleQmlTypeByName(
      unit: Optional[QV4.ExecutableCompilationUnit],
      elementNameId: int,
      typeLoader: Optional[QQmlTypeLoader] = None,
  ) -> QQmlType:
    """
    Calls Qt's 'QQmlType QQmlTypePrivate::visibleQmlTypeByName(const
    QV4::ExecutableCompilationUnit *unit, int elementNameId, QQmlTypeLoader
    *typeLoader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeprivate.html#visibleQmlTypeByName

    Parameters
    ----------

    unit : Optional[QV4.ExecutableCompilationUnit]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    elementNameId : int
      Passed on as it is.

    typeLoader : Optional[QQmlTypeLoader]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QQmlTypePrivate::visibleQmlTypeByName(const
    #      QV4::ExecutableCompilationUnit *unit, int elementNameId,
    #      QQmlTypeLoader *typeLoader)
    address = Rituals.call(
        'ritual_ZN15QQmlTypePrivate20visibleQmlTypeByNameEPKN3QV425Executab'
        'leCompilationUnitEiP14QQmlTypeLoader',
        CuteMixin._addressOf(unit), elementNameId,
        CuteMixin._addressOf(typeLoader),
    )
    return QQmlType._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlTypePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def init(self) -> Optional[ProxyMetaObjects]:
    """
    Calls Qt's 'const ProxyMetaObjects *QQmlTypePrivate::init() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeprivate.html#init

    Returns
    -------

    Optional[ProxyMetaObjects]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const ProxyMetaObjects *QQmlTypePrivate::init() const
    address = self.uglySide.call('ritual_ZNK15QQmlTypePrivate4initEv')
    return QQmlTypePrivate.ProxyMetaObjects._cuteAt(address)

  def sourceUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlTypePrivate::sourceUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeprivate.html#sourceUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlTypePrivate::sourceUrl() const
    address = self.uglySide.call('ritual_ZNK15QQmlTypePrivate9sourceUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(QQmlTypeLoader)
  @overload(NoneType)
  def attachedPropertiesBase(
      self,
      typeLoader: Optional[QQmlTypeLoader],
  ) -> Optional[QQmlTypePrivate]:
    """
    Calls Qt's 'const QQmlTypePrivate
    *QQmlTypePrivate::attachedPropertiesBase(QQmlTypeLoader *typeLoader)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeprivate.html#attachedPropertiesBase

    Parameters
    ----------

    typeLoader : Optional[QQmlTypeLoader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlTypePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QQmlTypePrivate
    #      *QQmlTypePrivate::attachedPropertiesBase(QQmlTypeLoader
    #      *typeLoader) const
    address = self.uglySide.call(
        'ritual_ZNK15QQmlTypePrivate22attachedPropertiesBaseEP14QQmlTypeLoa'
        'der',
        self._addressOf(typeLoader),
    )
    return QQmlTypePrivate._cuteAt(address)

  def isComposite(self) -> bool:
    """
    Calls Qt's 'bool QQmlTypePrivate::isComposite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeprivate.html#isComposite
    """
    #  bool QQmlTypePrivate::isComposite() const
    return self.uglySide.call('ritual_ZNK15QQmlTypePrivate11isCompositeEv')

  def isValueType(self) -> bool:
    """
    Calls Qt's 'bool QQmlTypePrivate::isValueType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeprivate.html#isValueType
    """
    #  bool QQmlTypePrivate::isValueType() const
    return self.uglySide.call('ritual_ZNK15QQmlTypePrivate11isValueTypeEv')

  @overload(QQmlTypeLoader)
  @overload(NoneType)
  def resolveCompositeBaseType(
      self,
      typeLoader: Optional[QQmlTypeLoader],
  ) -> QQmlType:
    """
    Calls Qt's 'QQmlType
    QQmlTypePrivate::resolveCompositeBaseType(QQmlTypeLoader *typeLoader)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeprivate.html#resolveCompositeBaseType

    Parameters
    ----------

    typeLoader : Optional[QQmlTypeLoader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QQmlTypePrivate::resolveCompositeBaseType(QQmlTypeLoader
    #      *typeLoader) const
    address = self.uglySide.call(
        'ritual_ZNK15QQmlTypePrivate24resolveCompositeBaseTypeEP14QQmlTypeL'
        'oader',
        self._addressOf(typeLoader),
    )
    return QQmlType._cuteOwning(address)

  @overload(QQmlTypeLoader)
  @overload(NoneType)
  def compositePropertyCache(
      self,
      typeLoader: Optional[QQmlTypeLoader],
  ) -> QQmlPropertyCache.ConstPtr:
    """
    Calls Qt's 'QQmlPropertyCache::ConstPtr
    QQmlTypePrivate::compositePropertyCache(QQmlTypeLoader *typeLoader)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeprivate.html#compositePropertyCache

    Parameters
    ----------

    typeLoader : Optional[QQmlTypeLoader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQmlPropertyCache.ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlPropertyCache::ConstPtr
    #      QQmlTypePrivate::compositePropertyCache(QQmlTypeLoader
    #      *typeLoader) const
    address = self.uglySide.call(
        'ritual_ZNK15QQmlTypePrivate22compositePropertyCacheEP14QQmlTypeLoa'
        'der',
        self._addressOf(typeLoader),
    )
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlTypePrivate::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlTypePrivate::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQmlTypePrivate10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def metaObjectForValueType(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlTypePrivate::metaObjectForValueType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeprivate.html#metaObjectForValueType

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlTypePrivate::metaObjectForValueType() const
    address = self.uglySide.call(
        'ritual_ZNK15QQmlTypePrivate22metaObjectForValueTypeEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QQmlTypeLoader)
  @overload(NoneType)
  def initEnums(
      self,
      typeLoader: Optional[QQmlTypeLoader],
  ) -> Optional[Enums]:
    """
    Calls Qt's 'const Enums *QQmlTypePrivate::initEnums(QQmlTypeLoader
    *typeLoader) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeprivate.html#initEnums

    Parameters
    ----------

    typeLoader : Optional[QQmlTypeLoader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[Enums]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Enums *QQmlTypePrivate::initEnums(QQmlTypeLoader *typeLoader)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK15QQmlTypePrivate9initEnumsEP14QQmlTypeLoader',
        self._addressOf(typeLoader),
    )
    return QQmlTypePrivate.Enums._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, str)
  def setName(self, uri: str, element: str) -> None:
    """
    Calls Qt's 'void QQmlTypePrivate::setName(const QString &uri, const
    QString &element)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeprivate.html#setName

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    element : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlTypePrivate::setName(const QString &uri, const QString
    #      &element)
    self.uglySide.call(
        'ritual_ZN15QQmlTypePrivate7setNameERK7QStringS2_', uri, element,
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

  @overload(QQmlType.RegistrationType)
  def __init__(self, type: QQmlType.RegistrationType) -> None:
    """
    Notes what was given, for Qt's
    'QQmlTypePrivate::QQmlTypePrivate(QQmlType::RegistrationType type)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeprivate.html#QQmlTypePrivate

    Parameters
    ----------

    type : QQmlType.RegistrationType
      Passed on as its number.
    """
    #  QQmlTypePrivate::QQmlTypePrivate(QQmlType::RegistrationType type)
    self._noteCreation(QQmlTypePrivate, lambda: Rituals.call(
        'ritual_ZN15QQmlTypePrivateC1EN8QQmlType16RegistrationTypeE',
        type.value,
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

  @overload(Enums, QMetaObject)
  @overload(Enums, NoneType)
  @overload(NoneType, QMetaObject)
  @overload(NoneType, NoneType)
  def insertEnums(
      self,
      enums: Optional[Enums],
      metaObject: Optional[QMetaObject],
  ) -> None:
    """
    Calls Qt's 'void QQmlTypePrivate::insertEnums(Enums *enums, const
    QMetaObject *metaObject) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypeprivate.html#insertEnums

    Parameters
    ----------

    enums : Optional[Enums]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlTypePrivate::insertEnums(Enums *enums, const QMetaObject
    #      *metaObject) const
    self.uglySide.call(
        'ritual_ZNK15QQmlTypePrivate11insertEnumsEPNS_5EnumsEPK11QMetaObjec'
        't',
        self._addressOf(enums), self._addressOf(metaObject, 'QMetaObject'),
    )

  @overload(Enums, QQmlPropertyCache.ConstPtr)
  @overload(NoneType, QQmlPropertyCache.ConstPtr)
  def insertEnumsFromPropertyCache(
      self,
      enums: Optional[Enums],
      cache: QQmlPropertyCache.ConstPtr,
  ) -> None:
    """
    Calls Qt's 'void QQmlTypePrivate::insertEnumsFromPropertyCache(Enums
    *enums, const QQmlPropertyCache::ConstPtr &cache) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeprivate.html#insertEnumsFromPropertyCache

    Parameters
    ----------

    enums : Optional[Enums]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    cache : QQmlPropertyCache.ConstPtr
      Passed on as a value: Qt reads the C++ QQmlPropertyCache::ConstPtr,
      which stays Python's own.
    """
    #  void QQmlTypePrivate::insertEnumsFromPropertyCache(Enums *enums, const
    #      QQmlPropertyCache::ConstPtr &cache) const
    self.uglySide.call(
        'ritual_ZNK15QQmlTypePrivate28insertEnumsFromPropertyCacheEPNS_5Enu'
        'msERKN17QQmlPropertyCache8ConstPtrE',
        self._addressOf(enums), self._valueOf(cache),
    )

  @overload(QMetaObject, str)
  @overload(NoneType, str)
  def createEnumConflictReport(
      self,
      metaObject: Optional[QMetaObject],
      conflictingKey: str,
  ) -> None:
    """
    Calls Qt's 'void QQmlTypePrivate::createEnumConflictReport(const
    QMetaObject *metaObject, const QString &conflictingKey) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeprivate.html#createEnumConflictReport

    Parameters
    ----------

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    conflictingKey : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlTypePrivate::createEnumConflictReport(const QMetaObject
    #      *metaObject, const QString &conflictingKey) const
    self.uglySide.call(
        'ritual_ZNK15QQmlTypePrivate24createEnumConflictReportEPK11QMetaObj'
        'ectRK7QString',
        self._addressOf(metaObject, 'QMetaObject'), conflictingKey,
    )

  @staticmethod
  def createListOfPossibleConflictingItems(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypePrivate::createListOfPossibleConflictingItems(const
    QMetaObject *metaObject, QList<EnumInfo> &enumInfoList, QStringList path)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTypePrivate.createListOfPossibleConflictingItems' has no cute "
        "function yet. Qt's 'void "
        "QQmlTypePrivate::createListOfPossibleConflictingItems(const "
        "QMetaObject *metaObject, QList<EnumInfo> &enumInfoList, "
        "QStringList path) const': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def doGetEnumOp(*__, **_) -> Never:
    """
    Qt's 'QQmlTypePrivate::doGetEnumOp': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlTypePrivate.doGetEnumOp' has no cute function yet. Qt's "
        "'QQmlTypePrivate::doGetEnumOp': a template: a pattern and no "
        "single function.")

  @staticmethod
  def enumIndex(*__, **_) -> Never:
    """
    Qt's 'QQmlTypePrivate::enumIndex': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlTypePrivate.enumIndex' has no cute function yet. Qt's "
        "'QQmlTypePrivate::enumIndex': a template: a pattern and no single "
        "function.")

  @staticmethod
  def enumKey(*__, **_) -> Never:
    """
    Qt's 'QQmlTypePrivate::enumKey': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlTypePrivate.enumKey' has no cute function yet. Qt's "
        "'QQmlTypePrivate::enumKey': a template: a pattern and no single "
        "function.")

  @staticmethod
  def enumKeys(*__, **_) -> Never:
    """
    Qt's 'QQmlTypePrivate::enumKeys': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlTypePrivate.enumKeys' has no cute function yet. Qt's "
        "'QQmlTypePrivate::enumKeys': a template: a pattern and no single "
        "function.")

  @staticmethod
  def enumValue(*__, **_) -> Never:
    """
    Qt's 'QQmlTypePrivate::enumValue': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlTypePrivate.enumValue' has no cute function yet. Qt's "
        "'QQmlTypePrivate::enumValue': a template: a pattern and no single "
        "function.")
