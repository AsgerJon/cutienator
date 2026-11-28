"""
QMetaPropertyBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qmetaobjectbuilder_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QMetaPropertyBuilder to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QMetaMethodBuilder, QMetaObjectBuilder
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaMethodBuilder = WAIT['QMetaMethodBuilder']
  QMetaObjectBuilder = WAIT['QMetaObjectBuilder']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMetaPropertyBuilder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMetaPropertyBuilder: a plain Python object standing
  in front of one C++ QMetaPropertyBuilder.

  C++ hands a QMetaPropertyBuilder around as a copy, so every C++
  QMetaPropertyBuilder behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMetaPropertyBuilder that has a ritual and that
  Python can call so far, 41 names in all: 'index', 'name', 'type',
  'hasNotifySignal', 'notifySignal', 'setNotifySignal', 'removeNotifySignal',
  'isReadable', 'isWritable', 'isResettable', 'isDesignable', 'isScriptable',
  'isStored', 'isUser', 'hasStdCppSet', 'isEnumOrFlag', 'isConstant',
  'isFinal', 'isVirtual', 'isOverride', 'isAlias', 'isBindable',
  'isRequired', 'setReadable', 'setWritable', 'setResettable',
  'setDesignable', 'setScriptable', 'setStored', 'setUser', 'setStdCppSet',
  'setEnumOrFlag', 'setConstant', 'setFinal', 'setVirtual', 'setOverride',
  'setAlias', 'setBindable', 'setRequired', 'revision', 'setRevision'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMetaPropertyBuilderPrivate *QMetaPropertyBuilder::d_func() const':
    gives 'QMetaPropertyBuilderPrivate', which has no cute class yet.
  - Qt's 'QMetaPropertyBuilder::~QMetaPropertyBuilder()': the destructor:
    Python removes its C++ QMetaPropertyBuilder by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 46 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QMetaPropertyBuilder is created at the first use, not by
    'QMetaPropertyBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMetaPropertyBuilder back gives a copy the ritual
    made for Python, in a new cute QMetaPropertyBuilder.
  - Each name of Qt's QMetaPropertyBuilder that has no cute function yet,
    'd_func', 'isEditable', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMetaPropertyBuilder'

  #  Qt's '~QMetaPropertyBuilder()'. Naming it makes this a value class:
  #  Python owns every C++ QMetaPropertyBuilder behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QMetaPropertyBuilderD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def index(self) -> int:
    """
    Calls Qt's 'int QMetaPropertyBuilder::index() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetapropertybuilder.html#index
    """
    #  int QMetaPropertyBuilder::index() const
    return self.uglySide.call('ritual_ZNK20QMetaPropertyBuilder5indexEv')

  def name(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMetaPropertyBuilder::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetapropertybuilder.html#name

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMetaPropertyBuilder::name() const
    address = self.uglySide.call('ritual_ZNK20QMetaPropertyBuilder4nameEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def type(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMetaPropertyBuilder::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetapropertybuilder.html#type

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMetaPropertyBuilder::type() const
    address = self.uglySide.call('ritual_ZNK20QMetaPropertyBuilder4typeEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def hasNotifySignal(self) -> bool:
    """
    Calls Qt's 'bool QMetaPropertyBuilder::hasNotifySignal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#hasNotifySignal
    """
    #  bool QMetaPropertyBuilder::hasNotifySignal() const
    return self.uglySide.call(
        'ritual_ZNK20QMetaPropertyBuilder15hasNotifySignalEv',
    )

  def notifySignal(self) -> QMetaMethodBuilder:
    """
    Calls Qt's 'QMetaMethodBuilder QMetaPropertyBuilder::notifySignal()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#notifySignal

    Returns
    -------

    QMetaMethodBuilder
      A new cute QMetaMethodBuilder around the copy Qt gave back. Python owns
      it.
    """
    #  QMetaMethodBuilder QMetaPropertyBuilder::notifySignal() const
    address = self.uglySide.call(
        'ritual_ZNK20QMetaPropertyBuilder12notifySignalEv',
    )
    from . import QMetaMethodBuilder
    return QMetaMethodBuilder._cuteOwning(address)

  def isReadable(self) -> bool:
    """
    Calls Qt's 'bool QMetaPropertyBuilder::isReadable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#isReadable
    """
    #  bool QMetaPropertyBuilder::isReadable() const
    return self.uglySide.call(
        'ritual_ZNK20QMetaPropertyBuilder10isReadableEv',
    )

  def isWritable(self) -> bool:
    """
    Calls Qt's 'bool QMetaPropertyBuilder::isWritable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#isWritable
    """
    #  bool QMetaPropertyBuilder::isWritable() const
    return self.uglySide.call(
        'ritual_ZNK20QMetaPropertyBuilder10isWritableEv',
    )

  def isResettable(self) -> bool:
    """
    Calls Qt's 'bool QMetaPropertyBuilder::isResettable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#isResettable
    """
    #  bool QMetaPropertyBuilder::isResettable() const
    return self.uglySide.call(
        'ritual_ZNK20QMetaPropertyBuilder12isResettableEv',
    )

  def isDesignable(self) -> bool:
    """
    Calls Qt's 'bool QMetaPropertyBuilder::isDesignable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#isDesignable
    """
    #  bool QMetaPropertyBuilder::isDesignable() const
    return self.uglySide.call(
        'ritual_ZNK20QMetaPropertyBuilder12isDesignableEv',
    )

  def isScriptable(self) -> bool:
    """
    Calls Qt's 'bool QMetaPropertyBuilder::isScriptable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#isScriptable
    """
    #  bool QMetaPropertyBuilder::isScriptable() const
    return self.uglySide.call(
        'ritual_ZNK20QMetaPropertyBuilder12isScriptableEv',
    )

  def isStored(self) -> bool:
    """
    Calls Qt's 'bool QMetaPropertyBuilder::isStored() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetapropertybuilder.html#isStored
    """
    #  bool QMetaPropertyBuilder::isStored() const
    return self.uglySide.call('ritual_ZNK20QMetaPropertyBuilder8isStoredEv')

  def isUser(self) -> bool:
    """
    Calls Qt's 'bool QMetaPropertyBuilder::isUser() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetapropertybuilder.html#isUser
    """
    #  bool QMetaPropertyBuilder::isUser() const
    return self.uglySide.call('ritual_ZNK20QMetaPropertyBuilder6isUserEv')

  def hasStdCppSet(self) -> bool:
    """
    Calls Qt's 'bool QMetaPropertyBuilder::hasStdCppSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#hasStdCppSet
    """
    #  bool QMetaPropertyBuilder::hasStdCppSet() const
    return self.uglySide.call(
        'ritual_ZNK20QMetaPropertyBuilder12hasStdCppSetEv',
    )

  def isEnumOrFlag(self) -> bool:
    """
    Calls Qt's 'bool QMetaPropertyBuilder::isEnumOrFlag() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#isEnumOrFlag
    """
    #  bool QMetaPropertyBuilder::isEnumOrFlag() const
    return self.uglySide.call(
        'ritual_ZNK20QMetaPropertyBuilder12isEnumOrFlagEv',
    )

  def isConstant(self) -> bool:
    """
    Calls Qt's 'bool QMetaPropertyBuilder::isConstant() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#isConstant
    """
    #  bool QMetaPropertyBuilder::isConstant() const
    return self.uglySide.call(
        'ritual_ZNK20QMetaPropertyBuilder10isConstantEv',
    )

  def isFinal(self) -> bool:
    """
    Calls Qt's 'bool QMetaPropertyBuilder::isFinal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetapropertybuilder.html#isFinal
    """
    #  bool QMetaPropertyBuilder::isFinal() const
    return self.uglySide.call('ritual_ZNK20QMetaPropertyBuilder7isFinalEv')

  def isVirtual(self) -> bool:
    """
    Calls Qt's 'bool QMetaPropertyBuilder::isVirtual() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#isVirtual
    """
    #  bool QMetaPropertyBuilder::isVirtual() const
    return self.uglySide.call('ritual_ZNK20QMetaPropertyBuilder9isVirtualEv')

  def isOverride(self) -> bool:
    """
    Calls Qt's 'bool QMetaPropertyBuilder::isOverride() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#isOverride
    """
    #  bool QMetaPropertyBuilder::isOverride() const
    return self.uglySide.call(
        'ritual_ZNK20QMetaPropertyBuilder10isOverrideEv',
    )

  def isAlias(self) -> bool:
    """
    Calls Qt's 'bool QMetaPropertyBuilder::isAlias() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetapropertybuilder.html#isAlias
    """
    #  bool QMetaPropertyBuilder::isAlias() const
    return self.uglySide.call('ritual_ZNK20QMetaPropertyBuilder7isAliasEv')

  def isBindable(self) -> bool:
    """
    Calls Qt's 'bool QMetaPropertyBuilder::isBindable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#isBindable
    """
    #  bool QMetaPropertyBuilder::isBindable() const
    return self.uglySide.call(
        'ritual_ZNK20QMetaPropertyBuilder10isBindableEv',
    )

  def isRequired(self) -> bool:
    """
    Calls Qt's 'bool QMetaPropertyBuilder::isRequired() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#isRequired
    """
    #  bool QMetaPropertyBuilder::isRequired() const
    return self.uglySide.call(
        'ritual_ZNK20QMetaPropertyBuilder10isRequiredEv',
    )

  def revision(self) -> int:
    """
    Calls Qt's 'int QMetaPropertyBuilder::revision() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetapropertybuilder.html#revision
    """
    #  int QMetaPropertyBuilder::revision() const
    return self.uglySide.call('ritual_ZNK20QMetaPropertyBuilder8revisionEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMetaMethodBuilder)
  def setNotifySignal(self, value: QMetaMethodBuilder) -> None:
    """
    Calls Qt's 'void QMetaPropertyBuilder::setNotifySignal(const
    QMetaMethodBuilder &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#setNotifySignal

    Parameters
    ----------

    value : QMetaMethodBuilder
      Passed on as a value: Qt reads the C++ QMetaMethodBuilder, which stays
      Python's own.
    """
    #  void QMetaPropertyBuilder::setNotifySignal(const QMetaMethodBuilder
    #      &value)
    self.uglySide.call(
        'ritual_ZN20QMetaPropertyBuilder15setNotifySignalERK18QMetaMethodBu'
        'ilder',
        self._valueOf(value),
    )

  @overload(bool)
  def setReadable(self, value: bool) -> None:
    """
    Calls Qt's 'void QMetaPropertyBuilder::setReadable(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#setReadable

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QMetaPropertyBuilder::setReadable(bool value)
    self.uglySide.call(
        'ritual_ZN20QMetaPropertyBuilder11setReadableEb', value,
    )

  @overload(bool)
  def setWritable(self, value: bool) -> None:
    """
    Calls Qt's 'void QMetaPropertyBuilder::setWritable(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#setWritable

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QMetaPropertyBuilder::setWritable(bool value)
    self.uglySide.call(
        'ritual_ZN20QMetaPropertyBuilder11setWritableEb', value,
    )

  @overload(bool)
  def setResettable(self, value: bool) -> None:
    """
    Calls Qt's 'void QMetaPropertyBuilder::setResettable(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#setResettable

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QMetaPropertyBuilder::setResettable(bool value)
    self.uglySide.call(
        'ritual_ZN20QMetaPropertyBuilder13setResettableEb', value,
    )

  @overload(bool)
  def setDesignable(self, value: bool) -> None:
    """
    Calls Qt's 'void QMetaPropertyBuilder::setDesignable(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#setDesignable

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QMetaPropertyBuilder::setDesignable(bool value)
    self.uglySide.call(
        'ritual_ZN20QMetaPropertyBuilder13setDesignableEb', value,
    )

  @overload(bool)
  def setScriptable(self, value: bool) -> None:
    """
    Calls Qt's 'void QMetaPropertyBuilder::setScriptable(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#setScriptable

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QMetaPropertyBuilder::setScriptable(bool value)
    self.uglySide.call(
        'ritual_ZN20QMetaPropertyBuilder13setScriptableEb', value,
    )

  @overload(bool)
  def setStored(self, value: bool) -> None:
    """
    Calls Qt's 'void QMetaPropertyBuilder::setStored(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#setStored

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QMetaPropertyBuilder::setStored(bool value)
    self.uglySide.call('ritual_ZN20QMetaPropertyBuilder9setStoredEb', value)

  @overload(bool)
  def setUser(self, value: bool) -> None:
    """
    Calls Qt's 'void QMetaPropertyBuilder::setUser(bool value)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetapropertybuilder.html#setUser

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QMetaPropertyBuilder::setUser(bool value)
    self.uglySide.call('ritual_ZN20QMetaPropertyBuilder7setUserEb', value)

  @overload(bool)
  def setStdCppSet(self, value: bool) -> None:
    """
    Calls Qt's 'void QMetaPropertyBuilder::setStdCppSet(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#setStdCppSet

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QMetaPropertyBuilder::setStdCppSet(bool value)
    self.uglySide.call(
        'ritual_ZN20QMetaPropertyBuilder12setStdCppSetEb', value,
    )

  @overload(bool)
  def setEnumOrFlag(self, value: bool) -> None:
    """
    Calls Qt's 'void QMetaPropertyBuilder::setEnumOrFlag(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#setEnumOrFlag

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QMetaPropertyBuilder::setEnumOrFlag(bool value)
    self.uglySide.call(
        'ritual_ZN20QMetaPropertyBuilder13setEnumOrFlagEb', value,
    )

  @overload(bool)
  def setConstant(self, value: bool) -> None:
    """
    Calls Qt's 'void QMetaPropertyBuilder::setConstant(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#setConstant

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QMetaPropertyBuilder::setConstant(bool value)
    self.uglySide.call(
        'ritual_ZN20QMetaPropertyBuilder11setConstantEb', value,
    )

  @overload(bool)
  def setFinal(self, value: bool) -> None:
    """
    Calls Qt's 'void QMetaPropertyBuilder::setFinal(bool value)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetapropertybuilder.html#setFinal

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QMetaPropertyBuilder::setFinal(bool value)
    self.uglySide.call('ritual_ZN20QMetaPropertyBuilder8setFinalEb', value)

  @overload(bool)
  def setVirtual(self, value: bool) -> None:
    """
    Calls Qt's 'void QMetaPropertyBuilder::setVirtual(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#setVirtual

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QMetaPropertyBuilder::setVirtual(bool value)
    self.uglySide.call(
        'ritual_ZN20QMetaPropertyBuilder10setVirtualEb', value,
    )

  @overload(bool)
  def setOverride(self, value: bool) -> None:
    """
    Calls Qt's 'void QMetaPropertyBuilder::setOverride(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#setOverride

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QMetaPropertyBuilder::setOverride(bool value)
    self.uglySide.call(
        'ritual_ZN20QMetaPropertyBuilder11setOverrideEb', value,
    )

  @overload(bool)
  def setAlias(self, value: bool) -> None:
    """
    Calls Qt's 'void QMetaPropertyBuilder::setAlias(bool value)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetapropertybuilder.html#setAlias

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QMetaPropertyBuilder::setAlias(bool value)
    self.uglySide.call('ritual_ZN20QMetaPropertyBuilder8setAliasEb', value)

  @overload(bool)
  def setBindable(self, value: bool) -> None:
    """
    Calls Qt's 'void QMetaPropertyBuilder::setBindable(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#setBindable

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QMetaPropertyBuilder::setBindable(bool value)
    self.uglySide.call(
        'ritual_ZN20QMetaPropertyBuilder11setBindableEb', value,
    )

  @overload(bool)
  def setRequired(self, value: bool) -> None:
    """
    Calls Qt's 'void QMetaPropertyBuilder::setRequired(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#setRequired

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QMetaPropertyBuilder::setRequired(bool value)
    self.uglySide.call(
        'ritual_ZN20QMetaPropertyBuilder11setRequiredEb', value,
    )

  @overload(int)
  def setRevision(self, revision: int) -> None:
    """
    Calls Qt's 'void QMetaPropertyBuilder::setRevision(int revision)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#setRevision

    Parameters
    ----------

    revision : int
      Passed on as it is.
    """
    #  void QMetaPropertyBuilder::setRevision(int revision)
    self.uglySide.call(
        'ritual_ZN20QMetaPropertyBuilder11setRevisionEi', revision,
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
    'QMetaPropertyBuilder::QMetaPropertyBuilder()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#QMetaPropertyBuilder
    """
    #  QMetaPropertyBuilder::QMetaPropertyBuilder()
    self._noteCreation(QMetaPropertyBuilder, lambda: Rituals.call(
        'ritual_ZN20QMetaPropertyBuilderC1Ev',
    ))

  @overload(QMetaObjectBuilder, int)
  @overload(NoneType, int)
  def __init__(self, mobj: Optional[QMetaObjectBuilder], index: int) -> None:
    """
    Notes what was given, for Qt's
    'QMetaPropertyBuilder::QMetaPropertyBuilder(const QMetaObjectBuilder
    *mobj, int index)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#QMetaPropertyBuilder

    Parameters
    ----------

    mobj : Optional[QMetaObjectBuilder]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  QMetaPropertyBuilder::QMetaPropertyBuilder(const QMetaObjectBuilder
    #      *mobj, int index)
    self._noteCreation(QMetaPropertyBuilder, lambda: Rituals.call(
        'ritual_ZN20QMetaPropertyBuilderC1EPK18QMetaObjectBuilderi',
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

  def removeNotifySignal(self) -> None:
    """
    Calls Qt's 'void QMetaPropertyBuilder::removeNotifySignal()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetapropertybuilder.html#removeNotifySignal
    """
    #  void QMetaPropertyBuilder::removeNotifySignal()
    self.uglySide.call(
        'ritual_ZN20QMetaPropertyBuilder18removeNotifySignalEv',
    )

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    Qt's 'QMetaPropertyBuilderPrivate *QMetaPropertyBuilder::d_func() const':
    gives 'QMetaPropertyBuilderPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaPropertyBuilder.d_func' has no cute function yet. Qt's "
        "'QMetaPropertyBuilderPrivate *QMetaPropertyBuilder::d_func() "
        "const': gives 'QMetaPropertyBuilderPrivate', which has no cute "
        "class yet.")

  @staticmethod
  def isEditable(*__, **_) -> Never:
    """
    Qt's 'bool QMetaPropertyBuilder::isEditable() const': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QMetaPropertyBuilder.isEditable' has no cute function yet. Qt's "
        "'bool QMetaPropertyBuilder::isEditable() const': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")
