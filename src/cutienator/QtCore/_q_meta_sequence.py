"""
QMetaSequence binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmetacontainer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QMetaContainer, QtMetaContainerPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QMetaType

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMetaSequence(QMetaContainer):
  """
  The cute side of Qt's QMetaSequence: a plain Python object standing in
  front of one C++ QMetaSequence.

  It is built on the cute 'QMetaContainer', as Qt's QMetaSequence is built on
  Qt's QMetaContainer, and has everything that class has.

  C++ hands a QMetaSequence around as a copy, so every C++ QMetaSequence
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMetaSequence that has a ritual and that Python can
  call so far, 20 names in all: 'valueMetaType', 'isSortable',
  'canAddValueAtBegin', 'canAddValueAtEnd', 'canRemoveValueAtBegin',
  'canRemoveValueAtEnd', 'canGetValueAtIndex', 'canSetValueAtIndex',
  'canAddValue', 'canRemoveValue', 'canGetValueAtIterator',
  'canSetValueAtIterator', 'canInsertValueAtIterator',
  'canEraseValueAtIterator', 'canEraseRangeAtIterator',
  'canGetValueAtConstIterator', 'iface', '__eq__', '__ne__', 'd'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QMetaSequence::addValueAtBegin(void *container, const void
    *value) const': names 'void', which has no cute class yet.
  - Qt's 'void QMetaSequence::addValueAtEnd(void *container, const void
    *value) const': names 'void', which has no cute class yet.
  - Qt's 'void QMetaSequence::removeValueAtBegin(void *container) const':
    names 'void', which has no cute class yet.
  - Qt's 'void QMetaSequence::removeValueAtEnd(void *container) const': names
    'void', which has no cute class yet.
  - Qt's 'void QMetaSequence::valueAtIndex(const void *container, qsizetype
    index, void *result) const': names 'void', which has no cute class yet.
  - Qt's 'void QMetaSequence::setValueAtIndex(void *container, qsizetype
    index, const void *value) const': names 'void', which has no cute class
    yet.
  - Qt's 'void QMetaSequence::addValue(void *container, const void *value)
    const': names 'void', which has no cute class yet.
  - Qt's 'void QMetaSequence::removeValue(void *container) const': names
    'void', which has no cute class yet.
  - Qt's 'void QMetaSequence::valueAtIterator(const void *iterator, void
    *result) const': names 'void', which has no cute class yet.
  - Qt's 'void QMetaSequence::setValueAtIterator(const void *iterator, const
    void *value) const': names 'void', which has no cute class yet.
  - Qt's 'void QMetaSequence::insertValueAtIterator(void *container, const
    void *iterator, const void *value) const': names 'void', which has no
    cute class yet.
  - Qt's 'void QMetaSequence::eraseValueAtIterator(void *container, const
    void *iterator) const': names 'void', which has no cute class yet.
  - Qt's 'void QMetaSequence::eraseRangeAtIterator(void *container, const
    void *iterator1, const void *iterator2) const': names 'void', which has
    no cute class yet.
  - Qt's 'void QMetaSequence::valueAtConstIterator(const void *iterator, void
    *result) const': names 'void', which has no cute class yet.
  - Qt's 'QMetaSequence::~QMetaSequence()': the destructor: Python removes
    its C++ QMetaSequence by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 38 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QMetaSequence is created at the first use, not by
    'QMetaSequence(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMetaSequence back gives a copy the ritual made for
    Python, in a new cute QMetaSequence.
  - Each name of Qt's QMetaSequence that has no cute function yet,
    'addValue', 'addValueAtBegin', 'addValueAtEnd', 'eraseRangeAtIterator',
    'eraseValueAtIterator', 'fromContainer', 'insertValueAtIterator',
    'removeValue', 'removeValueAtBegin', 'removeValueAtEnd',
    'setValueAtIndex', 'setValueAtIterator', 'valueAtConstIterator',
    'valueAtIndex', 'valueAtIterator', holds a function that raises
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
  __qt_class__ = 'QMetaSequence'

  #  Qt's '~QMetaSequence()'. Naming it makes this a value class: Python owns
  #  every C++ QMetaSequence behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QMetaSequenceD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def valueMetaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QMetaSequence::valueMetaType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetasequence.html#valueMetaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QMetaSequence::valueMetaType() const
    address = self.uglySide.call(
        'ritual_ZNK13QMetaSequence13valueMetaTypeEv',
    )
    from . import QMetaType
    return QMetaType._cuteOwning(address)

  def isSortable(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::isSortable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetasequence.html#isSortable
    """
    #  bool QMetaSequence::isSortable() const
    return self.uglySide.call('ritual_ZNK13QMetaSequence10isSortableEv')

  def canAddValueAtBegin(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canAddValueAtBegin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canAddValueAtBegin
    """
    #  bool QMetaSequence::canAddValueAtBegin() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence18canAddValueAtBeginEv',
    )

  def canAddValueAtEnd(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canAddValueAtEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canAddValueAtEnd
    """
    #  bool QMetaSequence::canAddValueAtEnd() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence16canAddValueAtEndEv',
    )

  def canRemoveValueAtBegin(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canRemoveValueAtBegin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canRemoveValueAtBegin
    """
    #  bool QMetaSequence::canRemoveValueAtBegin() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence21canRemoveValueAtBeginEv',
    )

  def canRemoveValueAtEnd(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canRemoveValueAtEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canRemoveValueAtEnd
    """
    #  bool QMetaSequence::canRemoveValueAtEnd() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence19canRemoveValueAtEndEv',
    )

  def canGetValueAtIndex(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canGetValueAtIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canGetValueAtIndex
    """
    #  bool QMetaSequence::canGetValueAtIndex() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence18canGetValueAtIndexEv',
    )

  def canSetValueAtIndex(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canSetValueAtIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canSetValueAtIndex
    """
    #  bool QMetaSequence::canSetValueAtIndex() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence18canSetValueAtIndexEv',
    )

  def canAddValue(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canAddValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetasequence.html#canAddValue
    """
    #  bool QMetaSequence::canAddValue() const
    return self.uglySide.call('ritual_ZNK13QMetaSequence11canAddValueEv')

  def canRemoveValue(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canRemoveValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetasequence.html#canRemoveValue
    """
    #  bool QMetaSequence::canRemoveValue() const
    return self.uglySide.call('ritual_ZNK13QMetaSequence14canRemoveValueEv')

  def canGetValueAtIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canGetValueAtIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canGetValueAtIterator
    """
    #  bool QMetaSequence::canGetValueAtIterator() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence21canGetValueAtIteratorEv',
    )

  def canSetValueAtIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canSetValueAtIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canSetValueAtIterator
    """
    #  bool QMetaSequence::canSetValueAtIterator() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence21canSetValueAtIteratorEv',
    )

  def canInsertValueAtIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canInsertValueAtIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canInsertValueAtIterator
    """
    #  bool QMetaSequence::canInsertValueAtIterator() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence24canInsertValueAtIteratorEv',
    )

  def canEraseValueAtIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canEraseValueAtIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canEraseValueAtIterator
    """
    #  bool QMetaSequence::canEraseValueAtIterator() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence23canEraseValueAtIteratorEv',
    )

  def canEraseRangeAtIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canEraseRangeAtIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canEraseRangeAtIterator
    """
    #  bool QMetaSequence::canEraseRangeAtIterator() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence23canEraseRangeAtIteratorEv',
    )

  def canGetValueAtConstIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaSequence::canGetValueAtConstIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetasequence.html#canGetValueAtConstIterator
    """
    #  bool QMetaSequence::canGetValueAtConstIterator() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaSequence26canGetValueAtConstIteratorEv',
    )

  def iface(self) -> Optional[QtMetaContainerPrivate.QMetaSequenceInterface]:
    """
    Calls Qt's 'const QtMetaContainerPrivate::QMetaSequenceInterface
    *QMetaSequence::iface() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetasequence.html#iface

    Returns
    -------

    Optional[QtMetaContainerPrivate.QMetaSequenceInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QtMetaContainerPrivate::QMetaSequenceInterface
    #      *QMetaSequence::iface() const
    address = self.uglySide.call('ritual_ZNK13QMetaSequence5ifaceEv')
    return QtMetaContainerPrivate.QMetaSequenceInterface._cuteAt(address)

  def d(self) -> Optional[QtMetaContainerPrivate.QMetaSequenceInterface]:
    """
    Calls Qt's 'const QtMetaContainerPrivate::QMetaSequenceInterface
    *QMetaSequence::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetasequence.html#d

    Returns
    -------

    Optional[QtMetaContainerPrivate.QMetaSequenceInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QtMetaContainerPrivate::QMetaSequenceInterface
    #      *QMetaSequence::d() const
    address = self.uglySide.call('ritual_ZNK13QMetaSequence1dEv')
    return QtMetaContainerPrivate.QMetaSequenceInterface._cuteAt(address)

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
  def __eq__(self, rhs: QMetaSequence) -> bool:
    """
    Calls Qt's 'bool operator==(const QMetaSequence &lhs, const QMetaSequence
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetasequence.html#operator==

    Parameters
    ----------

    rhs : QMetaSequence
      Passed on as a value: Qt reads the C++ QMetaSequence, which stays
      Python's own.
    """
    #  bool operator==(const QMetaSequence &lhs, const QMetaSequence &rhs)
    return Rituals.call(
        'ritual_ZeqRK13QMetaSequenceS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
  def __ne__(self, rhs: QMetaSequence) -> bool:
    """
    Calls Qt's 'bool operator!=(const QMetaSequence &lhs, const QMetaSequence
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetasequence.html#operator!=

    Parameters
    ----------

    rhs : QMetaSequence
      Passed on as a value: Qt reads the C++ QMetaSequence, which stays
      Python's own.
    """
    #  bool operator!=(const QMetaSequence &lhs, const QMetaSequence &rhs)
    return Rituals.call(
        'ritual_ZneRK13QMetaSequenceS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QMetaSequence::QMetaSequence()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmetasequence.html#QMetaSequence
    """
    #  QMetaSequence::QMetaSequence()
    self._noteCreation(QMetaSequence, lambda: Rituals.call(
        'ritual_ZN13QMetaSequenceC1Ev',
    ))

  @overload(WAIT['QtMetaContainerPrivate.QMetaSequenceInterface'])
  @overload(NoneType)
  def __init__(
      self,
      d: Optional[QtMetaContainerPrivate.QMetaSequenceInterface],
  ) -> None:
    """
    Notes what was given, for Qt's 'QMetaSequence::QMetaSequence(const
    QtMetaContainerPrivate::QMetaSequenceInterface *d)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmetasequence.html#QMetaSequence

    Parameters
    ----------

    d : Optional[QtMetaContainerPrivate.QMetaSequenceInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QMetaSequence::QMetaSequence(const
    #      QtMetaContainerPrivate::QMetaSequenceInterface *d)
    self._noteCreation(QMetaSequence, lambda: Rituals.call(
        'ritual_ZN13QMetaSequenceC1EPKN22QtMetaContainerPrivate22QMetaSeque'
        'nceInterfaceE',
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

  @staticmethod
  def addValue(*__, **_) -> Never:
    """
    Qt's 'void QMetaSequence::addValue(void *container, const void *value)
    const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaSequence.addValue' has no cute function yet. Qt's 'void "
        "QMetaSequence::addValue(void *container, const void *value) "
        "const': names 'void', which has no cute class yet.")

  @staticmethod
  def addValueAtBegin(*__, **_) -> Never:
    """
    Qt's 'void QMetaSequence::addValueAtBegin(void *container, const void
    *value) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaSequence.addValueAtBegin' has no cute function yet. Qt's "
        "'void QMetaSequence::addValueAtBegin(void *container, const void "
        "*value) const': names 'void', which has no cute class yet.")

  @staticmethod
  def addValueAtEnd(*__, **_) -> Never:
    """
    Qt's 'void QMetaSequence::addValueAtEnd(void *container, const void
    *value) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaSequence.addValueAtEnd' has no cute function yet. Qt's 'void "
        "QMetaSequence::addValueAtEnd(void *container, const void *value) "
        "const': names 'void', which has no cute class yet.")

  @staticmethod
  def eraseRangeAtIterator(*__, **_) -> Never:
    """
    Qt's 'void QMetaSequence::eraseRangeAtIterator(void *container, const
    void *iterator1, const void *iterator2) const': names 'void', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaSequence.eraseRangeAtIterator' has no cute function yet. "
        "Qt's 'void QMetaSequence::eraseRangeAtIterator(void *container, "
        "const void *iterator1, const void *iterator2) const': names "
        "'void', which has no cute class yet.")

  @staticmethod
  def eraseValueAtIterator(*__, **_) -> Never:
    """
    Qt's 'void QMetaSequence::eraseValueAtIterator(void *container, const
    void *iterator) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaSequence.eraseValueAtIterator' has no cute function yet. "
        "Qt's 'void QMetaSequence::eraseValueAtIterator(void *container, "
        "const void *iterator) const': names 'void', which has no cute "
        "class yet.")

  @staticmethod
  def fromContainer(*__, **_) -> Never:
    """
    Qt's 'QMetaSequence::fromContainer': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QMetaSequence.fromContainer' has no cute function yet. Qt's "
        "'QMetaSequence::fromContainer': a template: a pattern and no "
        "single function.")

  @staticmethod
  def insertValueAtIterator(*__, **_) -> Never:
    """
    Qt's 'void QMetaSequence::insertValueAtIterator(void *container, const
    void *iterator, const void *value) const': names 'void', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QMetaSequence.insertValueAtIterator' has no cute function yet. "
        "Qt's 'void QMetaSequence::insertValueAtIterator(void *container, "
        "const void *iterator, const void *value) const': names 'void', "
        "which has no cute class yet.")

  @staticmethod
  def removeValue(*__, **_) -> Never:
    """
    Qt's 'void QMetaSequence::removeValue(void *container) const': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaSequence.removeValue' has no cute function yet. Qt's 'void "
        "QMetaSequence::removeValue(void *container) const': names 'void', "
        "which has no cute class yet.")

  @staticmethod
  def removeValueAtBegin(*__, **_) -> Never:
    """
    Qt's 'void QMetaSequence::removeValueAtBegin(void *container) const':
    names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaSequence.removeValueAtBegin' has no cute function yet. Qt's "
        "'void QMetaSequence::removeValueAtBegin(void *container) const': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def removeValueAtEnd(*__, **_) -> Never:
    """
    Qt's 'void QMetaSequence::removeValueAtEnd(void *container) const': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaSequence.removeValueAtEnd' has no cute function yet. Qt's "
        "'void QMetaSequence::removeValueAtEnd(void *container) const': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def setValueAtIndex(*__, **_) -> Never:
    """
    Qt's 'void QMetaSequence::setValueAtIndex(void *container, qsizetype
    index, const void *value) const': names 'void', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QMetaSequence.setValueAtIndex' has no cute function yet. Qt's "
        "'void QMetaSequence::setValueAtIndex(void *container, qsizetype "
        "index, const void *value) const': names 'void', which has no cute "
        "class yet.")

  @staticmethod
  def setValueAtIterator(*__, **_) -> Never:
    """
    Qt's 'void QMetaSequence::setValueAtIterator(const void *iterator, const
    void *value) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaSequence.setValueAtIterator' has no cute function yet. Qt's "
        "'void QMetaSequence::setValueAtIterator(const void *iterator, "
        "const void *value) const': names 'void', which has no cute class "
        "yet.")

  @staticmethod
  def valueAtConstIterator(*__, **_) -> Never:
    """
    Qt's 'void QMetaSequence::valueAtConstIterator(const void *iterator, void
    *result) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaSequence.valueAtConstIterator' has no cute function yet. "
        "Qt's 'void QMetaSequence::valueAtConstIterator(const void "
        "*iterator, void *result) const': names 'void', which has no cute "
        "class yet.")

  @staticmethod
  def valueAtIndex(*__, **_) -> Never:
    """
    Qt's 'void QMetaSequence::valueAtIndex(const void *container, qsizetype
    index, void *result) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaSequence.valueAtIndex' has no cute function yet. Qt's 'void "
        "QMetaSequence::valueAtIndex(const void *container, qsizetype "
        "index, void *result) const': names 'void', which has no cute class "
        "yet.")

  @staticmethod
  def valueAtIterator(*__, **_) -> Never:
    """
    Qt's 'void QMetaSequence::valueAtIterator(const void *iterator, void
    *result) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaSequence.valueAtIterator' has no cute function yet. Qt's "
        "'void QMetaSequence::valueAtIterator(const void *iterator, void "
        "*result) const': names 'void', which has no cute class yet.")
