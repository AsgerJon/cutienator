"""
QQmlAbstractBinding binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlabstractbinding_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlAbstractBinding to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlPropertyData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from . import QQmlProperty, QQmlPropertyIndex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlProperty = WAIT['QQmlProperty']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlAbstractBinding(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlAbstractBinding: a plain Python object standing
  in front of one C++ QQmlAbstractBinding.

  What exists
  -----------

  Every function of Qt's QQmlAbstractBinding that has a ritual and that
  Python can call so far, 24 names in all: 'expression', 'kind',
  'targetPropertyIndex', 'targetObject', 'setTarget', 'setEnabled',
  'addToObject', 'removeFromObject', 'printBindingLoopError', 'nextBinding',
  'canUseAccessor', 'setCanUseAccessor', 'isSticky', 'setSticky',
  'setAddedToObject', 'isAddedToObject', 'setNextBinding', 'updatingFlag',
  'setUpdatingFlag', 'enabledFlag', 'setEnabledFlag', 'updateCanUseAccessor',
  'setState', 'hasState'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlAbstractBinding::~QQmlAbstractBinding()': the destructor:
    Python never removes a C++ QQmlAbstractBinding.
  - Qt's 'void QQmlAbstractBinding::getPropertyData(const QQmlPropertyData
    **propertyData, QQmlPropertyData *valueTypeData) const': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QQmlAbstractBinding is created at the first use, not by
    'QQmlAbstractBinding(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlAbstractBinding.
  - Each name of Qt's QQmlAbstractBinding that has no cute function yet,
    'getPropertyData', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QQmlAbstractBinding, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Kind(CuteNum):
    """
    The enum 'QQmlAbstractBinding::Kind' of Qt, with the 3 names Qt gives in
    it.
    """

    ValueTypeProxy = Kee[int](0)
    QmlBinding = Kee[int](1)
    PropertyToPropertyBinding = Kee[int](2)

  class State(CuteNum):
    """
    The enum 'QQmlAbstractBinding::State' of Qt, with the 4 names Qt gives in
    it.
    """

    Disabled = Kee[int](0)
    AddedToObject = Kee[int](1)
    BindingEnabled = Kee[int](2)
    UpdatingBinding = Kee[int](3)

  class TargetTag(CuteFlags):
    """
    The flags enum 'QQmlAbstractBinding::TargetTag' of Qt, with the 3 names
    Qt gives in it. Qt names the type of its combinations
    'QQmlAbstractBinding::TargetTags'.
    """

    NoTargetTag = 0x0
    CanUseAccessor = 0x1
    IsSticky = 0x2

  TargetTags = TargetTag

  #  The classes Qt writes inside QQmlAbstractBinding, each a class in here
  #  as in C++.

  class RefCount(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlAbstractBinding::RefCount: a plain Python
    object standing in front of one C++ QQmlAbstractBinding::RefCount.

    C++ hands a QQmlAbstractBinding::RefCount around as a copy, so every C++
    QQmlAbstractBinding::RefCount behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QQmlAbstractBinding::RefCount that has a ritual
    and that Python can call so far, 2 names in all: 'ref', 'deref'. It can
    be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'int QQmlAbstractBinding::RefCount::operator int() const': an
      operator Python has no name for.
    - Qt's 'QQmlAbstractBinding::RefCount::~RefCount()': the destructor:
      Python removes its C++ QQmlAbstractBinding::RefCount by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQmlAbstractBinding::RefCount is created at the first use, not
      by 'QQmlAbstractBinding::RefCount(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlAbstractBinding::RefCount back gives a copy the
      ritual made for Python, in a new cute QQmlAbstractBinding::RefCount.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlAbstractBinding::RefCount'

    #  Qt's '~QQmlAbstractBinding::RefCount()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlAbstractBinding::RefCount behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN19QQmlAbstractBinding8RefCountD1Ev'

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QQmlAbstractBinding::RefCount::RefCount()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlabstractbinding-refcount.html#RefCount
      """
      #  QQmlAbstractBinding::RefCount::RefCount()
      self._noteCreation(QQmlAbstractBinding.RefCount, lambda: Rituals.call(
          'ritual_ZN19QQmlAbstractBinding8RefCountC1Ev',
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

    def ref(self) -> None:
      """
      Calls Qt's 'void QQmlAbstractBinding::RefCount::ref()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlabstractbinding-refcount.html#ref
      """
      #  void QQmlAbstractBinding::RefCount::ref()
      self.uglySide.call('ritual_ZN19QQmlAbstractBinding8RefCount3refEv')

    def deref(self) -> int:
      """
      Calls Qt's 'int QQmlAbstractBinding::RefCount::deref()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlabstractbinding-refcount.html#deref
      """
      #  int QQmlAbstractBinding::RefCount::deref()
      return self.uglySide.call(
          'ritual_ZN19QQmlAbstractBinding8RefCount5derefEv',
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlAbstractBinding'

  #  A C++ QQmlAbstractBinding Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlAbstractBinding'

  #  The functions Qt calls itself that QQmlAbstractBinding is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'expression': (
          ('_ZNK19QQmlAbstractBinding10expressionEv',
           ('address', 'text', ''),
           ()),
      ),
      'kind': (
          ('_ZNK19QQmlAbstractBinding4kindEv',
           ('int', 'enum', 'QtQml:QQmlAbstractBinding.Kind'),
           ()),
      ),
      'setEnabled': (
          ('_ZN19QQmlAbstractBinding10setEnabledEb6QFlagsIN16QQmlPropertyDa'
           'ta9WriteFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
               ('int', 'flags', 'QtQml:QQmlPropertyData.WriteFlag'),
           )),
      ),
      'printBindingLoopError': (
          ('_ZN19QQmlAbstractBinding21printBindingLoopErrorERK12QQmlPropert'
           'y',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtQml:QQmlProperty'),
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

  def expression(self) -> str:
    """
    Calls Qt's 'QString QQmlAbstractBinding::expression() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractbinding.html#expression

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlAbstractBinding::expression() const
    ritual = 'ritual_ZNK19QQmlAbstractBinding10expressionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQmlAbstractBinding10expressionEv'
    return self._callAs('QQmlAbstractBinding', ritual)

  def kind(self) -> Kind:
    """
    Calls Qt's 'Kind QQmlAbstractBinding::kind() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlabstractbinding.html#kind

    Returns
    -------

    Kind
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Kind(number)' gives.
    """
    #  Kind QQmlAbstractBinding::kind() const
    return QQmlAbstractBinding.Kind(self._callAs(
        'QQmlAbstractBinding', 'ritual_ZNK19QQmlAbstractBinding4kindEv',
    ))

  def targetPropertyIndex(self) -> QQmlPropertyIndex:
    """
    Calls Qt's 'QQmlPropertyIndex QQmlAbstractBinding::targetPropertyIndex()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractbinding.html#targetPropertyIndex

    Returns
    -------

    QQmlPropertyIndex
      A new cute QQmlPropertyIndex around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlPropertyIndex QQmlAbstractBinding::targetPropertyIndex() const
    address = self._callAs(
        'QQmlAbstractBinding',
        'ritual_ZNK19QQmlAbstractBinding19targetPropertyIndexEv',
    )
    from . import QQmlPropertyIndex
    return QQmlPropertyIndex._cuteOwning(address)

  def targetObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlAbstractBinding::targetObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractbinding.html#targetObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlAbstractBinding::targetObject() const
    address = self._callAs(
        'QQmlAbstractBinding',
        'ritual_ZNK19QQmlAbstractBinding12targetObjectEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def nextBinding(self) -> Optional[QQmlAbstractBinding]:
    """
    Calls Qt's 'QQmlAbstractBinding *QQmlAbstractBinding::nextBinding()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractbinding.html#nextBinding

    Returns
    -------

    Optional[QQmlAbstractBinding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlAbstractBinding *QQmlAbstractBinding::nextBinding() const
    address = self._callAs(
        'QQmlAbstractBinding',
        'ritual_ZNK19QQmlAbstractBinding11nextBindingEv',
    )
    return QQmlAbstractBinding._cuteAt(address)

  def canUseAccessor(self) -> bool:
    """
    Calls Qt's 'bool QQmlAbstractBinding::canUseAccessor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractbinding.html#canUseAccessor
    """
    #  bool QQmlAbstractBinding::canUseAccessor() const
    return self._callAs(
        'QQmlAbstractBinding',
        'ritual_ZNK19QQmlAbstractBinding14canUseAccessorEv',
    )

  def isSticky(self) -> bool:
    """
    Calls Qt's 'bool QQmlAbstractBinding::isSticky() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlabstractbinding.html#isSticky
    """
    #  bool QQmlAbstractBinding::isSticky() const
    return self._callAs(
        'QQmlAbstractBinding', 'ritual_ZNK19QQmlAbstractBinding8isStickyEv',
    )

  def isAddedToObject(self) -> bool:
    """
    Calls Qt's 'bool QQmlAbstractBinding::isAddedToObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractbinding.html#isAddedToObject
    """
    #  bool QQmlAbstractBinding::isAddedToObject() const
    return self._callAs(
        'QQmlAbstractBinding',
        'ritual_ZNK19QQmlAbstractBinding15isAddedToObjectEv',
    )

  def updatingFlag(self) -> bool:
    """
    Calls Qt's 'bool QQmlAbstractBinding::updatingFlag() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractbinding.html#updatingFlag
    """
    #  bool QQmlAbstractBinding::updatingFlag() const
    return self._callAs(
        'QQmlAbstractBinding',
        'ritual_ZNK19QQmlAbstractBinding12updatingFlagEv',
    )

  def enabledFlag(self) -> bool:
    """
    Calls Qt's 'bool QQmlAbstractBinding::enabledFlag() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractbinding.html#enabledFlag
    """
    #  bool QQmlAbstractBinding::enabledFlag() const
    return self._callAs(
        'QQmlAbstractBinding',
        'ritual_ZNK19QQmlAbstractBinding11enabledFlagEv',
    )

  @overload(State)
  def hasState(self, state: State) -> bool:
    """
    Calls Qt's 'bool QQmlAbstractBinding::hasState(State state) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlabstractbinding.html#hasState

    Parameters
    ----------

    state : State
      Passed on as its number.
    """
    #  bool QQmlAbstractBinding::hasState(State state) const
    return self._callAs(
        'QQmlAbstractBinding',
        'ritual_ZNK19QQmlAbstractBinding8hasStateENS_5StateE',
        state.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlProperty)
  def setTarget(self, a0: QQmlProperty) -> None:
    """
    Calls Qt's 'void QQmlAbstractBinding::setTarget(const QQmlProperty &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlabstractbinding.html#setTarget

    Parameters
    ----------

    a0 : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.
    """
    #  void QQmlAbstractBinding::setTarget(const QQmlProperty &a0)
    self._callAs(
        'QQmlAbstractBinding',
        'ritual_ZN19QQmlAbstractBinding9setTargetERK12QQmlProperty',
        self._valueOf(a0),
    )

  @overload(QObject, QQmlPropertyData, QQmlPropertyData)
  @overload(QObject, QQmlPropertyData, NoneType)
  @overload(NoneType, QQmlPropertyData, QQmlPropertyData)
  @overload(NoneType, QQmlPropertyData, NoneType)
  def setTarget(
      self,
      a0: Optional[QObject],
      a1: QQmlPropertyData,
      valueType: Optional[QQmlPropertyData],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlAbstractBinding::setTarget(QObject *a0, const
    QQmlPropertyData &a1, const QQmlPropertyData *valueType)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlabstractbinding.html#setTarget

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QQmlPropertyData
      Passed on as a value: Qt reads the C++ QQmlPropertyData, which stays
      Python's own.

    valueType : Optional[QQmlPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlAbstractBinding::setTarget(QObject *a0, const
    #      QQmlPropertyData &a1, const QQmlPropertyData *valueType)
    return self._callAs(
        'QQmlAbstractBinding',
        'ritual_ZN19QQmlAbstractBinding9setTargetEP7QObjectRK16QQmlProperty'
        'DataPS3_',
        self._addressOf(a0, 'QObject'), self._valueOf(a1),
        self._addressOf(valueType),
    )

  @overload(QObject, int, bool, int)
  @overload(NoneType, int, bool, int)
  def setTarget(
      self,
      a0: Optional[QObject],
      coreIndex: int,
      coreIsAlias: bool,
      valueTypeIndex: int,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlAbstractBinding::setTarget(QObject *a0, int
    coreIndex, bool coreIsAlias, int valueTypeIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlabstractbinding.html#setTarget

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    coreIndex : int
      Passed on as it is.

    coreIsAlias : bool
      Passed on as it is.

    valueTypeIndex : int
      Passed on as it is.
    """
    #  bool QQmlAbstractBinding::setTarget(QObject *a0, int coreIndex, bool
    #      coreIsAlias, int valueTypeIndex)
    return self._callAs(
        'QQmlAbstractBinding',
        'ritual_ZN19QQmlAbstractBinding9setTargetEP7QObjectibi',
        self._addressOf(a0, 'QObject'), coreIndex, coreIsAlias,
        valueTypeIndex,
    )

  @overload(bool)
  @overload(bool, QQmlPropertyData.WriteFlags)
  def setEnabled(
      self,
      e: bool,
      f: QQmlPropertyData.WriteFlags = (
          QQmlPropertyData.WriteFlags.DontRemoveBinding),
  ) -> None:
    """
    Calls Qt's 'void QQmlAbstractBinding::setEnabled(bool e,
    QQmlPropertyData::WriteFlags f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractbinding.html#setEnabled

    Parameters
    ----------

    e : bool
      Passed on as it is.

    f : QQmlPropertyData.WriteFlags
      Passed on as its number. May be left out, as in Qt: it is then
      QQmlPropertyData.WriteFlags.DontRemoveBinding.
    """
    #  void QQmlAbstractBinding::setEnabled(bool e,
    #      QQmlPropertyData::WriteFlags f)
    self._callAs(
        'QQmlAbstractBinding',
        'ritual_ZN19QQmlAbstractBinding10setEnabledEb6QFlagsIN16QQmlPropert'
        'yData9WriteFlagEE',
        e, f.value,
    )

  @overload(bool)
  def setCanUseAccessor(self, canUseAccessor: bool) -> None:
    """
    Calls Qt's 'void QQmlAbstractBinding::setCanUseAccessor(bool
    canUseAccessor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractbinding.html#setCanUseAccessor

    Parameters
    ----------

    canUseAccessor : bool
      Passed on as it is.
    """
    #  void QQmlAbstractBinding::setCanUseAccessor(bool canUseAccessor)
    self._callAs(
        'QQmlAbstractBinding',
        'ritual_ZN19QQmlAbstractBinding17setCanUseAccessorEb',
        canUseAccessor,
    )

  @overload(bool)
  def setSticky(self, isSticky: bool) -> None:
    """
    Calls Qt's 'void QQmlAbstractBinding::setSticky(bool isSticky)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlabstractbinding.html#setSticky

    Parameters
    ----------

    isSticky : bool
      Passed on as it is.
    """
    #  void QQmlAbstractBinding::setSticky(bool isSticky)
    self._callAs(
        'QQmlAbstractBinding', 'ritual_ZN19QQmlAbstractBinding9setStickyEb',
        isSticky,
    )

  @overload(bool)
  def setAddedToObject(self, v: bool) -> None:
    """
    Calls Qt's 'void QQmlAbstractBinding::setAddedToObject(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractbinding.html#setAddedToObject

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQmlAbstractBinding::setAddedToObject(bool v)
    self._callAs(
        'QQmlAbstractBinding',
        'ritual_ZN19QQmlAbstractBinding16setAddedToObjectEb',
        v,
    )

  @overload(THIS)
  @overload(NoneType)
  def setNextBinding(self, a0: Optional[QQmlAbstractBinding]) -> None:
    """
    Calls Qt's 'void QQmlAbstractBinding::setNextBinding(QQmlAbstractBinding
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractbinding.html#setNextBinding

    Parameters
    ----------

    a0 : Optional[QQmlAbstractBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlAbstractBinding::setNextBinding(QQmlAbstractBinding *a0)
    self._callAs(
        'QQmlAbstractBinding',
        'ritual_ZN19QQmlAbstractBinding14setNextBindingEPS_',
        self._addressOf(a0, 'QQmlAbstractBinding'),
    )

  @overload(bool)
  def setUpdatingFlag(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQmlAbstractBinding::setUpdatingFlag(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractbinding.html#setUpdatingFlag

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQmlAbstractBinding::setUpdatingFlag(bool a0)
    self._callAs(
        'QQmlAbstractBinding',
        'ritual_ZN19QQmlAbstractBinding15setUpdatingFlagEb',
        a0,
    )

  @overload(bool)
  def setEnabledFlag(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQmlAbstractBinding::setEnabledFlag(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractbinding.html#setEnabledFlag

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQmlAbstractBinding::setEnabledFlag(bool a0)
    self._callAs(
        'QQmlAbstractBinding',
        'ritual_ZN19QQmlAbstractBinding14setEnabledFlagEb',
        a0,
    )

  @overload(State, bool)
  def setState(self, state: State, enabled: bool) -> None:
    """
    Calls Qt's 'void QQmlAbstractBinding::setState(State state, bool
    enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlabstractbinding.html#setState

    Parameters
    ----------

    state : State
      Passed on as its number.

    enabled : bool
      Passed on as it is.
    """
    #  void QQmlAbstractBinding::setState(State state, bool enabled)
    self._callAs(
        'QQmlAbstractBinding',
        'ritual_ZN19QQmlAbstractBinding8setStateENS_5StateEb',
        state.value, enabled,
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
    'QQmlAbstractBinding::QQmlAbstractBinding()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractbinding.html#QQmlAbstractBinding
    """
    #  QQmlAbstractBinding::QQmlAbstractBinding()
    self._noteCreation(QQmlAbstractBinding, lambda: Rituals.call(
        'ritual_ZN19QQmlAbstractBindingC1Ev',
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

  def addToObject(self) -> None:
    """
    Calls Qt's 'void QQmlAbstractBinding::addToObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractbinding.html#addToObject
    """
    #  void QQmlAbstractBinding::addToObject()
    self._callAs(
        'QQmlAbstractBinding',
        'ritual_ZN19QQmlAbstractBinding11addToObjectEv',
    )

  def removeFromObject(self) -> None:
    """
    Calls Qt's 'void QQmlAbstractBinding::removeFromObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractbinding.html#removeFromObject
    """
    #  void QQmlAbstractBinding::removeFromObject()
    self._callAs(
        'QQmlAbstractBinding',
        'ritual_ZN19QQmlAbstractBinding16removeFromObjectEv',
    )

  @overload(QQmlProperty)
  def printBindingLoopError(self, prop: QQmlProperty) -> None:
    """
    Calls Qt's 'void QQmlAbstractBinding::printBindingLoopError(const
    QQmlProperty &prop)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractbinding.html#printBindingLoopError

    Parameters
    ----------

    prop : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.
    """
    #  void QQmlAbstractBinding::printBindingLoopError(const QQmlProperty
    #      &prop)
    ritual = (
        'ritual_ZN19QQmlAbstractBinding21printBindingLoopErrorERK12QQmlProp'
        'erty')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlAbstractBinding21printBindingLoopErrorERK12QQ'
          'mlProperty')
    self._callAs('QQmlAbstractBinding', ritual, self._valueOf(prop))

  def updateCanUseAccessor(self) -> None:
    """
    Calls Qt's 'void QQmlAbstractBinding::updateCanUseAccessor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractbinding.html#updateCanUseAccessor
    """
    #  void QQmlAbstractBinding::updateCanUseAccessor()
    self._callAs(
        'QQmlAbstractBinding',
        'ritual_ZN19QQmlAbstractBinding20updateCanUseAccessorEv',
    )

  @staticmethod
  def getPropertyData(*__, **_) -> Never:
    """
    Qt's 'void QQmlAbstractBinding::getPropertyData(const QQmlPropertyData
    **propertyData, QQmlPropertyData *valueTypeData) const': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlAbstractBinding.getPropertyData' has no cute function yet. "
        "Qt's 'void QQmlAbstractBinding::getPropertyData(const "
        "QQmlPropertyData **propertyData, QQmlPropertyData *valueTypeData) "
        "const': takes a type Python has no way to hand over yet.")
