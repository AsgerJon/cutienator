"""
QQmlPropertyBindingBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpropertybindingbase_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlPropertyBindingBase to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QPropertyBindingPrivate, QtPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaType, QObject
  from . import QQmlPropertyIndex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']
  QObject = WAIT['QObject']
  QQmlPropertyIndex = WAIT['QQmlPropertyIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlPropertyBindingBase(QPropertyBindingPrivate):
  """
  The cute side of Qt's QQmlPropertyBindingBase: a plain Python object
  standing in front of one C++ QQmlPropertyBindingBase.

  It is built on the cute 'QPropertyBindingPrivate', as Qt's
  QQmlPropertyBindingBase is built on Qt's QPropertyBindingPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlPropertyBindingBase that has a ritual and that
  Python can call so far, 7 names in all: 'bindingKind', 'isUndefined',
  'target', 'targetIndex', 'hasBoundFunction', 'setIsUndefined',
  'kindOffset'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'TargetData *QQmlPropertyBindingBase::targetData()': gives
    'QQmlPropertyBindingBase::TargetData', which has no cute class yet.
  - Qt's 'const TargetData *QQmlPropertyBindingBase::targetData() const':
    gives 'QQmlPropertyBindingBase::TargetData', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQmlPropertyBindingBase is created at the first use, not by
    'QQmlPropertyBindingBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlPropertyBindingBase.
  - Each name of Qt's QQmlPropertyBindingBase that has no cute function yet,
    'targetData', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQmlPropertyBindingBase, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class BindingKind(CuteNum, scoped=True):
    """
    The enum 'QQmlPropertyBindingBase::BindingKind' of Qt, with the 2 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    JavaScript = Kee[int](0)
    PropertyToProperty = Kee[int](1)

  class HasBoundFunction(CuteNum, scoped=True):
    """
    The enum 'QQmlPropertyBindingBase::HasBoundFunction' of Qt, with the 2
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    No = Kee[int](0)
    Yes = Kee[int](1)

  class IsUndefined(CuteNum, scoped=True):
    """
    The enum 'QQmlPropertyBindingBase::IsUndefined' of Qt, with the 2 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    No = Kee[int](0)
    Yes = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def kindOffset() -> int:
    """
    Calls Qt's 'size_t QQmlPropertyBindingBase::kindOffset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertybindingbase.html#kindOffset
    """
    #  size_t QQmlPropertyBindingBase::kindOffset()
    return Rituals.call('ritual_ZN23QQmlPropertyBindingBase10kindOffsetEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlPropertyBindingBase'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def bindingKind(self) -> BindingKind:
    """
    Calls Qt's 'BindingKind QQmlPropertyBindingBase::bindingKind() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertybindingbase.html#bindingKind

    Returns
    -------

    BindingKind
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'BindingKind(number)'
      gives.
    """
    #  BindingKind QQmlPropertyBindingBase::bindingKind() const
    return QQmlPropertyBindingBase.BindingKind(self.uglySide.call(
        'ritual_ZNK23QQmlPropertyBindingBase11bindingKindEv',
    ))

  def isUndefined(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyBindingBase::isUndefined() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertybindingbase.html#isUndefined
    """
    #  bool QQmlPropertyBindingBase::isUndefined() const
    return self.uglySide.call(
        'ritual_ZNK23QQmlPropertyBindingBase11isUndefinedEv',
    )

  def target(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlPropertyBindingBase::target() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertybindingbase.html#target

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlPropertyBindingBase::target() const
    address = self.uglySide.call(
        'ritual_ZNK23QQmlPropertyBindingBase6targetEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def targetIndex(self) -> QQmlPropertyIndex:
    """
    Calls Qt's 'QQmlPropertyIndex QQmlPropertyBindingBase::targetIndex()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertybindingbase.html#targetIndex

    Returns
    -------

    QQmlPropertyIndex
      A new cute QQmlPropertyIndex around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlPropertyIndex QQmlPropertyBindingBase::targetIndex() const
    address = self.uglySide.call(
        'ritual_ZNK23QQmlPropertyBindingBase11targetIndexEv',
    )
    from . import QQmlPropertyIndex
    return QQmlPropertyIndex._cuteOwning(address)

  def hasBoundFunction(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyBindingBase::hasBoundFunction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertybindingbase.html#hasBoundFunction
    """
    #  bool QQmlPropertyBindingBase::hasBoundFunction() const
    return self.uglySide.call(
        'ritual_ZNK23QQmlPropertyBindingBase16hasBoundFunctionEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setIsUndefined(self, isUndefined: bool) -> None:
    """
    Calls Qt's 'void QQmlPropertyBindingBase::setIsUndefined(bool
    isUndefined)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertybindingbase.html#setIsUndefined

    Parameters
    ----------

    isUndefined : bool
      Passed on as it is.
    """
    #  void QQmlPropertyBindingBase::setIsUndefined(bool isUndefined)
    self.uglySide.call(
        'ritual_ZN23QQmlPropertyBindingBase14setIsUndefinedEb', isUndefined,
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

  @overload(
      QObject, QQmlPropertyIndex, QMetaType,
      WAIT['QtPrivate.BindingFunctionVTable'], BindingKind,
  )
  @overload(QObject, QQmlPropertyIndex, QMetaType, NoneType, BindingKind)
  @overload(
      NoneType, QQmlPropertyIndex, QMetaType,
      WAIT['QtPrivate.BindingFunctionVTable'], BindingKind,
  )
  @overload(NoneType, QQmlPropertyIndex, QMetaType, NoneType, BindingKind)
  @overload(
      QObject, QQmlPropertyIndex, QMetaType,
      WAIT['QtPrivate.BindingFunctionVTable'], BindingKind, HasBoundFunction,
  )
  @overload(
      QObject, QQmlPropertyIndex, QMetaType, NoneType, BindingKind,
      HasBoundFunction,
  )
  @overload(
      NoneType, QQmlPropertyIndex, QMetaType,
      WAIT['QtPrivate.BindingFunctionVTable'], BindingKind, HasBoundFunction,
  )
  @overload(
      NoneType, QQmlPropertyIndex, QMetaType, NoneType, BindingKind,
      HasBoundFunction,
  )
  def __init__(
      self,
      target: Optional[QObject],
      targetIndex: QQmlPropertyIndex,
      targetMetaType: QMetaType,
      vtable: Optional[QtPrivate.BindingFunctionVTable],
      bindingKind: BindingKind,
      hasBoundFunction: HasBoundFunction = HasBoundFunction.No,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlPropertyBindingBase::QQmlPropertyBindingBase(QObject *target,
    QQmlPropertyIndex targetIndex, QMetaType targetMetaType, const
    QtPrivate::BindingFunctionVTable *vtable, BindingKind bindingKind,
    HasBoundFunction hasBoundFunction)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertybindingbase.html

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    targetIndex : QQmlPropertyIndex
      Passed on as a value: Qt reads the C++ QQmlPropertyIndex, which stays
      Python's own.

    targetMetaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    vtable : Optional[QtPrivate.BindingFunctionVTable]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    bindingKind : BindingKind
      Passed on as its number.

    hasBoundFunction : HasBoundFunction
      Passed on as its number. May be left out, as in Qt: it is then
      HasBoundFunction.No.
    """
    #  QQmlPropertyBindingBase::QQmlPropertyBindingBase(QObject *target,
    #      QQmlPropertyIndex targetIndex, QMetaType targetMetaType, const
    #      QtPrivate::BindingFunctionVTable *vtable, BindingKind bindingKind,
    #      HasBoundFunction hasBoundFunction)
    self._noteCreation(QQmlPropertyBindingBase, lambda: Rituals.call(
        'ritual_ZN23QQmlPropertyBindingBaseC1EP7QObject17QQmlPropertyIndex9'
        'QMetaTypePKN9QtPrivate21BindingFunctionVTableENS_11BindingKindENS_'
        '16HasBoundFunctionE',
        self._addressOf(target, 'QObject'), self._valueOf(targetIndex),
        self._valueOf(targetMetaType), self._addressOf(vtable),
        bindingKind.value, hasBoundFunction.value,
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
  def targetData(*__, **_) -> Never:
    """
    - Qt's 'TargetData *QQmlPropertyBindingBase::targetData()': gives
      'QQmlPropertyBindingBase::TargetData', which has no cute class yet.
    - Qt's 'const TargetData *QQmlPropertyBindingBase::targetData() const':
      gives 'QQmlPropertyBindingBase::TargetData', which has no cute class
      yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyBindingBase.targetData' has no cute function yet. "
        "Qt's 'TargetData *QQmlPropertyBindingBase::targetData()': gives "
        "'QQmlPropertyBindingBase::TargetData', which has no cute class "
        "yet. Qt's 'const TargetData *QQmlPropertyBindingBase::targetData() "
        "const': gives 'QQmlPropertyBindingBase::TargetData', which has no "
        "cute class yet.")
