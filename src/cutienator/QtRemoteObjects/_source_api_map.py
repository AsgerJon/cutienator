"""
SourceApiMap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/qremoteobjectsource.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..QtCore import QList, QMetaMethod

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray


class SourceApiMap(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's SourceApiMap: a plain Python object standing in front
  of one C++ SourceApiMap.

  What exists
  -----------

  Every function of Qt's SourceApiMap that has a ritual and that Python can
  call so far, 27 names in all: 'name', 'typeName', 'className', 'enumCount',
  'propertyCount', 'signalCount', 'methodCount', 'sourceEnumIndex',
  'sourcePropertyIndex', 'sourceSignalIndex', 'sourceMethodIndex',
  'signalParameterCount', 'signalParameterType', 'signalSignature',
  'signalParameterNames', 'methodParameterCount', 'methodParameterType',
  'methodSignature', 'methodType', 'methodParameterNames',
  'propertyIndexFromSignal', 'propertyRawIndexFromSignal', 'objectSignature',
  'isDynamic', 'isAdapterSignal', 'isAdapterMethod', 'isAdapterProperty'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'SourceApiMap::~SourceApiMap()': the destructor: Python never
    removes a C++ SourceApiMap.

  What has no ritual
  ------------------

  1 of the 30 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ SourceApiMap is created at the first use, not by
    'SourceApiMap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ SourceApiMap.
  - Each name of Qt's SourceApiMap that has no cute function yet, '__init__',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'SourceApiMap'

  #  A C++ SourceApiMap Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_SourceApiMap'

  #  The functions Qt calls itself that SourceApiMap is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'signalParameterNames': (
          'QByteArrayList SourceApiMap::signalParameterNames(int) const',
      ),
      'methodParameterNames': (
          'QByteArrayList SourceApiMap::methodParameterNames(int) const',
      ),
  }

  #  The functions Qt calls itself that SourceApiMap is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'name': (
          ('_ZNK12SourceApiMap4nameEv',
           ('address', 'text', ''),
           ()),
      ),
      'typeName': (
          ('_ZNK12SourceApiMap8typeNameEv',
           ('address', 'text', ''),
           ()),
          ('_ZNK12SourceApiMap8typeNameEi',
           ('address', 'value', 'QtCore:QByteArray'),
           (
               ('int', 'number', ''),
           )),
      ),
      'className': (
          ('_ZNK12SourceApiMap9classNameEv',
           ('address', 'value', 'QtCore:QByteArray'),
           ()),
      ),
      'enumCount': (
          ('_ZNK12SourceApiMap9enumCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'propertyCount': (
          ('_ZNK12SourceApiMap13propertyCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'signalCount': (
          ('_ZNK12SourceApiMap11signalCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'methodCount': (
          ('_ZNK12SourceApiMap11methodCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'sourceEnumIndex': (
          ('_ZNK12SourceApiMap15sourceEnumIndexEi',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'sourcePropertyIndex': (
          ('_ZNK12SourceApiMap19sourcePropertyIndexEi',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'sourceSignalIndex': (
          ('_ZNK12SourceApiMap17sourceSignalIndexEi',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'sourceMethodIndex': (
          ('_ZNK12SourceApiMap17sourceMethodIndexEi',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'signalParameterCount': (
          ('_ZNK12SourceApiMap20signalParameterCountEi',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'signalParameterType': (
          ('_ZNK12SourceApiMap19signalParameterTypeEii',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'signalSignature': (
          ('_ZNK12SourceApiMap15signalSignatureEi',
           ('address', 'value', 'QtCore:QByteArray'),
           (
               ('int', 'number', ''),
           )),
      ),
      'methodParameterCount': (
          ('_ZNK12SourceApiMap20methodParameterCountEi',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'methodParameterType': (
          ('_ZNK12SourceApiMap19methodParameterTypeEii',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'methodSignature': (
          ('_ZNK12SourceApiMap15methodSignatureEi',
           ('address', 'value', 'QtCore:QByteArray'),
           (
               ('int', 'number', ''),
           )),
      ),
      'methodType': (
          ('_ZNK12SourceApiMap10methodTypeEi',
           ('int', 'enum', 'QtCore:QMetaMethod.MethodType'),
           (
               ('int', 'number', ''),
           )),
      ),
      'propertyIndexFromSignal': (
          ('_ZNK12SourceApiMap23propertyIndexFromSignalEi',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'propertyRawIndexFromSignal': (
          ('_ZNK12SourceApiMap26propertyRawIndexFromSignalEi',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'objectSignature': (
          ('_ZNK12SourceApiMap15objectSignatureEv',
           ('address', 'value', 'QtCore:QByteArray'),
           ()),
      ),
      'isDynamic': (
          ('_ZNK12SourceApiMap9isDynamicEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isAdapterSignal': (
          ('_ZNK12SourceApiMap15isAdapterSignalEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'isAdapterMethod': (
          ('_ZNK12SourceApiMap15isAdapterMethodEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'isAdapterProperty': (
          ('_ZNK12SourceApiMap17isAdapterPropertyEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
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

  def name(self) -> str:
    """
    Calls Qt's 'QString SourceApiMap::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/sourceapimap.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString SourceApiMap::name() const
    return self.uglySide.call('ritual_ZNK12SourceApiMap4nameEv')

  @overload()
  def typeName(self) -> str:
    """
    Calls Qt's 'QString SourceApiMap::typeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/sourceapimap.html#typeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString SourceApiMap::typeName() const
    return self.uglySide.call('ritual_ZNK12SourceApiMap8typeNameEv')

  @overload(int)
  def typeName(self, index: int) -> QByteArray:
    """
    Calls Qt's 'const QByteArray SourceApiMap::typeName(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/sourceapimap.html#typeName

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray SourceApiMap::typeName(int index) const
    address = self.uglySide.call(
        'ritual_ZNK12SourceApiMap8typeNameEi', index,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def className(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray SourceApiMap::className() const'.

    Qt's own words: https://doc.qt.io/qt-6/sourceapimap.html#className

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray SourceApiMap::className() const
    ritual = 'ritual_ZNK12SourceApiMap9classNameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12SourceApiMap9classNameEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def enumCount(self) -> int:
    """
    Calls Qt's 'int SourceApiMap::enumCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/sourceapimap.html#enumCount
    """
    #  int SourceApiMap::enumCount() const
    return self.uglySide.call('ritual_ZNK12SourceApiMap9enumCountEv')

  def propertyCount(self) -> int:
    """
    Calls Qt's 'int SourceApiMap::propertyCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/sourceapimap.html#propertyCount
    """
    #  int SourceApiMap::propertyCount() const
    return self.uglySide.call('ritual_ZNK12SourceApiMap13propertyCountEv')

  def signalCount(self) -> int:
    """
    Calls Qt's 'int SourceApiMap::signalCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/sourceapimap.html#signalCount
    """
    #  int SourceApiMap::signalCount() const
    return self.uglySide.call('ritual_ZNK12SourceApiMap11signalCountEv')

  def methodCount(self) -> int:
    """
    Calls Qt's 'int SourceApiMap::methodCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/sourceapimap.html#methodCount
    """
    #  int SourceApiMap::methodCount() const
    return self.uglySide.call('ritual_ZNK12SourceApiMap11methodCountEv')

  @overload(int)
  def sourceEnumIndex(self, index: int) -> int:
    """
    Calls Qt's 'int SourceApiMap::sourceEnumIndex(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/sourceapimap.html#sourceEnumIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int SourceApiMap::sourceEnumIndex(int index) const
    return self.uglySide.call(
        'ritual_ZNK12SourceApiMap15sourceEnumIndexEi', index,
    )

  @overload(int)
  def sourcePropertyIndex(self, index: int) -> int:
    """
    Calls Qt's 'int SourceApiMap::sourcePropertyIndex(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/sourceapimap.html#sourcePropertyIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int SourceApiMap::sourcePropertyIndex(int index) const
    return self.uglySide.call(
        'ritual_ZNK12SourceApiMap19sourcePropertyIndexEi', index,
    )

  @overload(int)
  def sourceSignalIndex(self, index: int) -> int:
    """
    Calls Qt's 'int SourceApiMap::sourceSignalIndex(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/sourceapimap.html#sourceSignalIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int SourceApiMap::sourceSignalIndex(int index) const
    return self.uglySide.call(
        'ritual_ZNK12SourceApiMap17sourceSignalIndexEi', index,
    )

  @overload(int)
  def sourceMethodIndex(self, index: int) -> int:
    """
    Calls Qt's 'int SourceApiMap::sourceMethodIndex(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/sourceapimap.html#sourceMethodIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int SourceApiMap::sourceMethodIndex(int index) const
    return self.uglySide.call(
        'ritual_ZNK12SourceApiMap17sourceMethodIndexEi', index,
    )

  @overload(int)
  def signalParameterCount(self, index: int) -> int:
    """
    Calls Qt's 'int SourceApiMap::signalParameterCount(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/sourceapimap.html#signalParameterCount

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int SourceApiMap::signalParameterCount(int index) const
    return self.uglySide.call(
        'ritual_ZNK12SourceApiMap20signalParameterCountEi', index,
    )

  @overload(int, int)
  def signalParameterType(self, sigIndex: int, paramIndex: int) -> int:
    """
    Calls Qt's 'int SourceApiMap::signalParameterType(int sigIndex, int
    paramIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/sourceapimap.html#signalParameterType

    Parameters
    ----------

    sigIndex : int
      Passed on as it is.

    paramIndex : int
      Passed on as it is.
    """
    #  int SourceApiMap::signalParameterType(int sigIndex, int paramIndex)
    #      const
    return self.uglySide.call(
        'ritual_ZNK12SourceApiMap19signalParameterTypeEii',
        sigIndex, paramIndex,
    )

  @overload(int)
  def signalSignature(self, index: int) -> QByteArray:
    """
    Calls Qt's 'const QByteArray SourceApiMap::signalSignature(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/sourceapimap.html#signalSignature

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray SourceApiMap::signalSignature(int index) const
    address = self.uglySide.call(
        'ritual_ZNK12SourceApiMap15signalSignatureEi', index,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(int)
  def signalParameterNames(self, index: int) -> QList[QByteArray]:
    """
    Calls Qt's 'QByteArrayList SourceApiMap::signalParameterNames(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/sourceapimap.html#signalParameterNames

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayList SourceApiMap::signalParameterNames(int index) const
    address = self.uglySide.call(
        'ritual_ZNK12SourceApiMap20signalParameterNamesEi', index,
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @overload(int)
  def methodParameterCount(self, index: int) -> int:
    """
    Calls Qt's 'int SourceApiMap::methodParameterCount(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/sourceapimap.html#methodParameterCount

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int SourceApiMap::methodParameterCount(int index) const
    return self.uglySide.call(
        'ritual_ZNK12SourceApiMap20methodParameterCountEi', index,
    )

  @overload(int, int)
  def methodParameterType(self, methodIndex: int, paramIndex: int) -> int:
    """
    Calls Qt's 'int SourceApiMap::methodParameterType(int methodIndex, int
    paramIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/sourceapimap.html#methodParameterType

    Parameters
    ----------

    methodIndex : int
      Passed on as it is.

    paramIndex : int
      Passed on as it is.
    """
    #  int SourceApiMap::methodParameterType(int methodIndex, int paramIndex)
    #      const
    return self.uglySide.call(
        'ritual_ZNK12SourceApiMap19methodParameterTypeEii',
        methodIndex, paramIndex,
    )

  @overload(int)
  def methodSignature(self, index: int) -> QByteArray:
    """
    Calls Qt's 'const QByteArray SourceApiMap::methodSignature(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/sourceapimap.html#methodSignature

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray SourceApiMap::methodSignature(int index) const
    address = self.uglySide.call(
        'ritual_ZNK12SourceApiMap15methodSignatureEi', index,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(int)
  def methodType(self, index: int) -> QMetaMethod.MethodType:
    """
    Calls Qt's 'QMetaMethod::MethodType SourceApiMap::methodType(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/sourceapimap.html#methodType

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QMetaMethod.MethodType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QMetaMethod.MethodType(number)' gives.
    """
    #  QMetaMethod::MethodType SourceApiMap::methodType(int index) const
    return QMetaMethod.MethodType(self.uglySide.call(
        'ritual_ZNK12SourceApiMap10methodTypeEi', index,
    ))

  @overload(int)
  def methodParameterNames(self, index: int) -> QList[QByteArray]:
    """
    Calls Qt's 'QByteArrayList SourceApiMap::methodParameterNames(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/sourceapimap.html#methodParameterNames

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayList SourceApiMap::methodParameterNames(int index) const
    address = self.uglySide.call(
        'ritual_ZNK12SourceApiMap20methodParameterNamesEi', index,
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @overload(int)
  def propertyIndexFromSignal(self, index: int) -> int:
    """
    Calls Qt's 'int SourceApiMap::propertyIndexFromSignal(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/sourceapimap.html#propertyIndexFromSignal

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int SourceApiMap::propertyIndexFromSignal(int index) const
    return self.uglySide.call(
        'ritual_ZNK12SourceApiMap23propertyIndexFromSignalEi', index,
    )

  @overload(int)
  def propertyRawIndexFromSignal(self, index: int) -> int:
    """
    Calls Qt's 'int SourceApiMap::propertyRawIndexFromSignal(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/sourceapimap.html#propertyRawIndexFromSignal

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int SourceApiMap::propertyRawIndexFromSignal(int index) const
    return self.uglySide.call(
        'ritual_ZNK12SourceApiMap26propertyRawIndexFromSignalEi', index,
    )

  def objectSignature(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray SourceApiMap::objectSignature() const'.

    Qt's own words: https://doc.qt.io/qt-6/sourceapimap.html#objectSignature

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray SourceApiMap::objectSignature() const
    address = self.uglySide.call(
        'ritual_ZNK12SourceApiMap15objectSignatureEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def isDynamic(self) -> bool:
    """
    Calls Qt's 'bool SourceApiMap::isDynamic() const'.

    Qt's own words: https://doc.qt.io/qt-6/sourceapimap.html#isDynamic
    """
    #  bool SourceApiMap::isDynamic() const
    ritual = 'ritual_ZNK12SourceApiMap9isDynamicEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12SourceApiMap9isDynamicEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def isAdapterSignal(self, a0: int) -> bool:
    """
    Calls Qt's 'bool SourceApiMap::isAdapterSignal(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/sourceapimap.html#isAdapterSignal

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  bool SourceApiMap::isAdapterSignal(int a0) const
    ritual = 'ritual_ZNK12SourceApiMap15isAdapterSignalEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12SourceApiMap15isAdapterSignalEi'
    return self.uglySide.call(ritual, a0)

  @overload(int)
  def isAdapterMethod(self, a0: int) -> bool:
    """
    Calls Qt's 'bool SourceApiMap::isAdapterMethod(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/sourceapimap.html#isAdapterMethod

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  bool SourceApiMap::isAdapterMethod(int a0) const
    ritual = 'ritual_ZNK12SourceApiMap15isAdapterMethodEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12SourceApiMap15isAdapterMethodEi'
    return self.uglySide.call(ritual, a0)

  @overload(int)
  def isAdapterProperty(self, a0: int) -> bool:
    """
    Calls Qt's 'bool SourceApiMap::isAdapterProperty(int a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/sourceapimap.html#isAdapterProperty

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  bool SourceApiMap::isAdapterProperty(int a0) const
    ritual = 'ritual_ZNK12SourceApiMap17isAdapterPropertyEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12SourceApiMap17isAdapterPropertyEi'
    return self.uglySide.call(ritual, a0)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'SourceApiMap::SourceApiMap()': the class is abstract, so C++ cannot
    make one, and the C++ class of ours does not fill in every function it
    leaves open.
    """
    raise NotImplementedError(
        "'SourceApiMap.__init__' has no cute function yet. Qt's "
        "'SourceApiMap::SourceApiMap()': the class is abstract, so C++ "
        "cannot make one, and the C++ class of ours does not fill in every "
        "function it leaves open.")

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
