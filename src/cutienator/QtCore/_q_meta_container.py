"""
QMetaContainer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmetacontainer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtMetaContainerPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMetaContainer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMetaContainer: a plain Python object standing in
  front of one C++ QMetaContainer.

  C++ hands a QMetaContainer around as a copy, so every C++ QMetaContainer
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMetaContainer that has a ritual and that Python can
  call so far, 8 names in all: 'hasInputIterator', 'hasForwardIterator',
  'hasBidirectionalIterator', 'hasRandomAccessIterator', 'hasSize',
  'canClear', 'hasIterator', 'hasConstIterator'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qsizetype QMetaContainer::size(const void *container) const': names
    'void', which has no cute class yet.
  - Qt's 'void QMetaContainer::clear(void *container) const': names 'void',
    which has no cute class yet.
  - Qt's 'void *QMetaContainer::begin(void *container) const': names 'void',
    which has no cute class yet.
  - Qt's 'void *QMetaContainer::end(void *container) const': names 'void',
    which has no cute class yet.
  - Qt's 'void QMetaContainer::destroyIterator(const void *iterator) const':
    names 'void', which has no cute class yet.
  - Qt's 'bool QMetaContainer::compareIterator(const void *i, const void *j)
    const': names 'void', which has no cute class yet.
  - Qt's 'void QMetaContainer::copyIterator(void *target, const void *source)
    const': names 'void', which has no cute class yet.
  - Qt's 'void QMetaContainer::advanceIterator(void *iterator, qsizetype
    step) const': names 'void', which has no cute class yet.
  - Qt's 'qsizetype QMetaContainer::diffIterator(const void *i, const void
    *j) const': names 'void', which has no cute class yet.
  - Qt's 'void *QMetaContainer::constBegin(const void *container) const':
    names 'void', which has no cute class yet.
  - Qt's 'void *QMetaContainer::constEnd(const void *container) const': names
    'void', which has no cute class yet.
  - Qt's 'void QMetaContainer::destroyConstIterator(const void *iterator)
    const': names 'void', which has no cute class yet.
  - Qt's 'bool QMetaContainer::compareConstIterator(const void *i, const void
    *j) const': names 'void', which has no cute class yet.
  - Qt's 'void QMetaContainer::copyConstIterator(void *target, const void
    *source) const': names 'void', which has no cute class yet.
  - Qt's 'void QMetaContainer::advanceConstIterator(void *iterator, qsizetype
    step) const': names 'void', which has no cute class yet.
  - Qt's 'qsizetype QMetaContainer::diffConstIterator(const void *i, const
    void *j) const': names 'void', which has no cute class yet.
  - Qt's 'QMetaContainer::~QMetaContainer()': the destructor: Python removes
    its C++ QMetaContainer by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QMetaContainer is created at the first use, not by
    'QMetaContainer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMetaContainer back gives a copy the ritual made for
    Python, in a new cute QMetaContainer.
  - Each name of Qt's QMetaContainer that has no cute function yet,
    'advanceConstIterator', 'advanceIterator', 'begin', 'clear',
    'compareConstIterator', 'compareIterator', 'constBegin', 'constEnd',
    'copyConstIterator', 'copyIterator', 'destroyConstIterator',
    'destroyIterator', 'diffConstIterator', 'diffIterator', 'end', 'size',
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
  __qt_class__ = 'QMetaContainer'

  #  Qt's '~QMetaContainer()'. Naming it makes this a value class: Python
  #  owns every C++ QMetaContainer behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QMetaContainerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasInputIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaContainer::hasInputIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetacontainer.html#hasInputIterator
    """
    #  bool QMetaContainer::hasInputIterator() const
    return self.uglySide.call(
        'ritual_ZNK14QMetaContainer16hasInputIteratorEv',
    )

  def hasForwardIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaContainer::hasForwardIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetacontainer.html#hasForwardIterator
    """
    #  bool QMetaContainer::hasForwardIterator() const
    return self.uglySide.call(
        'ritual_ZNK14QMetaContainer18hasForwardIteratorEv',
    )

  def hasBidirectionalIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaContainer::hasBidirectionalIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetacontainer.html#hasBidirectionalIterator
    """
    #  bool QMetaContainer::hasBidirectionalIterator() const
    return self.uglySide.call(
        'ritual_ZNK14QMetaContainer24hasBidirectionalIteratorEv',
    )

  def hasRandomAccessIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaContainer::hasRandomAccessIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetacontainer.html#hasRandomAccessIterator
    """
    #  bool QMetaContainer::hasRandomAccessIterator() const
    return self.uglySide.call(
        'ritual_ZNK14QMetaContainer23hasRandomAccessIteratorEv',
    )

  def hasSize(self) -> bool:
    """
    Calls Qt's 'bool QMetaContainer::hasSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetacontainer.html#hasSize
    """
    #  bool QMetaContainer::hasSize() const
    return self.uglySide.call('ritual_ZNK14QMetaContainer7hasSizeEv')

  def canClear(self) -> bool:
    """
    Calls Qt's 'bool QMetaContainer::canClear() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetacontainer.html#canClear
    """
    #  bool QMetaContainer::canClear() const
    return self.uglySide.call('ritual_ZNK14QMetaContainer8canClearEv')

  def hasIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaContainer::hasIterator() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetacontainer.html#hasIterator
    """
    #  bool QMetaContainer::hasIterator() const
    return self.uglySide.call('ritual_ZNK14QMetaContainer11hasIteratorEv')

  def hasConstIterator(self) -> bool:
    """
    Calls Qt's 'bool QMetaContainer::hasConstIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetacontainer.html#hasConstIterator
    """
    #  bool QMetaContainer::hasConstIterator() const
    return self.uglySide.call(
        'ritual_ZNK14QMetaContainer16hasConstIteratorEv',
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
    Notes what was given, for Qt's 'QMetaContainer::QMetaContainer()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmetacontainer.html#QMetaContainer
    """
    #  QMetaContainer::QMetaContainer()
    self._noteCreation(QMetaContainer, lambda: Rituals.call(
        'ritual_ZN14QMetaContainerC1Ev',
    ))

  @overload(WAIT['QtMetaContainerPrivate.QMetaContainerInterface'])
  @overload(NoneType)
  def __init__(
      self,
      d: Optional[QtMetaContainerPrivate.QMetaContainerInterface],
  ) -> None:
    """
    Notes what was given, for Qt's 'QMetaContainer::QMetaContainer(const
    QtMetaContainerPrivate::QMetaContainerInterface *d)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmetacontainer.html#QMetaContainer

    Parameters
    ----------

    d : Optional[QtMetaContainerPrivate.QMetaContainerInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QMetaContainer::QMetaContainer(const
    #      QtMetaContainerPrivate::QMetaContainerInterface *d)
    self._noteCreation(QMetaContainer, lambda: Rituals.call(
        'ritual_ZN14QMetaContainerC1EPKN22QtMetaContainerPrivate23QMetaCont'
        'ainerInterfaceE',
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
  def advanceConstIterator(*__, **_) -> Never:
    """
    Qt's 'void QMetaContainer::advanceConstIterator(void *iterator, qsizetype
    step) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaContainer.advanceConstIterator' has no cute function yet. "
        "Qt's 'void QMetaContainer::advanceConstIterator(void *iterator, "
        "qsizetype step) const': names 'void', which has no cute class yet.")

  @staticmethod
  def advanceIterator(*__, **_) -> Never:
    """
    Qt's 'void QMetaContainer::advanceIterator(void *iterator, qsizetype
    step) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaContainer.advanceIterator' has no cute function yet. Qt's "
        "'void QMetaContainer::advanceIterator(void *iterator, qsizetype "
        "step) const': names 'void', which has no cute class yet.")

  @staticmethod
  def begin(*__, **_) -> Never:
    """
    Qt's 'void *QMetaContainer::begin(void *container) const': names 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaContainer.begin' has no cute function yet. Qt's 'void "
        "*QMetaContainer::begin(void *container) const': names 'void', "
        "which has no cute class yet.")

  @staticmethod
  def clear(*__, **_) -> Never:
    """
    Qt's 'void QMetaContainer::clear(void *container) const': names 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaContainer.clear' has no cute function yet. Qt's 'void "
        "QMetaContainer::clear(void *container) const': names 'void', which "
        "has no cute class yet.")

  @staticmethod
  def compareConstIterator(*__, **_) -> Never:
    """
    Qt's 'bool QMetaContainer::compareConstIterator(const void *i, const void
    *j) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaContainer.compareConstIterator' has no cute function yet. "
        "Qt's 'bool QMetaContainer::compareConstIterator(const void *i, "
        "const void *j) const': names 'void', which has no cute class yet.")

  @staticmethod
  def compareIterator(*__, **_) -> Never:
    """
    Qt's 'bool QMetaContainer::compareIterator(const void *i, const void *j)
    const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaContainer.compareIterator' has no cute function yet. Qt's "
        "'bool QMetaContainer::compareIterator(const void *i, const void "
        "*j) const': names 'void', which has no cute class yet.")

  @staticmethod
  def constBegin(*__, **_) -> Never:
    """
    Qt's 'void *QMetaContainer::constBegin(const void *container) const':
    names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaContainer.constBegin' has no cute function yet. Qt's 'void "
        "*QMetaContainer::constBegin(const void *container) const': names "
        "'void', which has no cute class yet.")

  @staticmethod
  def constEnd(*__, **_) -> Never:
    """
    Qt's 'void *QMetaContainer::constEnd(const void *container) const': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaContainer.constEnd' has no cute function yet. Qt's 'void "
        "*QMetaContainer::constEnd(const void *container) const': names "
        "'void', which has no cute class yet.")

  @staticmethod
  def copyConstIterator(*__, **_) -> Never:
    """
    Qt's 'void QMetaContainer::copyConstIterator(void *target, const void
    *source) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaContainer.copyConstIterator' has no cute function yet. Qt's "
        "'void QMetaContainer::copyConstIterator(void *target, const void "
        "*source) const': names 'void', which has no cute class yet.")

  @staticmethod
  def copyIterator(*__, **_) -> Never:
    """
    Qt's 'void QMetaContainer::copyIterator(void *target, const void *source)
    const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaContainer.copyIterator' has no cute function yet. Qt's 'void "
        "QMetaContainer::copyIterator(void *target, const void *source) "
        "const': names 'void', which has no cute class yet.")

  @staticmethod
  def destroyConstIterator(*__, **_) -> Never:
    """
    Qt's 'void QMetaContainer::destroyConstIterator(const void *iterator)
    const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaContainer.destroyConstIterator' has no cute function yet. "
        "Qt's 'void QMetaContainer::destroyConstIterator(const void "
        "*iterator) const': names 'void', which has no cute class yet.")

  @staticmethod
  def destroyIterator(*__, **_) -> Never:
    """
    Qt's 'void QMetaContainer::destroyIterator(const void *iterator) const':
    names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaContainer.destroyIterator' has no cute function yet. Qt's "
        "'void QMetaContainer::destroyIterator(const void *iterator) "
        "const': names 'void', which has no cute class yet.")

  @staticmethod
  def diffConstIterator(*__, **_) -> Never:
    """
    Qt's 'qsizetype QMetaContainer::diffConstIterator(const void *i, const
    void *j) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaContainer.diffConstIterator' has no cute function yet. Qt's "
        "'qsizetype QMetaContainer::diffConstIterator(const void *i, const "
        "void *j) const': names 'void', which has no cute class yet.")

  @staticmethod
  def diffIterator(*__, **_) -> Never:
    """
    Qt's 'qsizetype QMetaContainer::diffIterator(const void *i, const void
    *j) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaContainer.diffIterator' has no cute function yet. Qt's "
        "'qsizetype QMetaContainer::diffIterator(const void *i, const void "
        "*j) const': names 'void', which has no cute class yet.")

  @staticmethod
  def end(*__, **_) -> Never:
    """
    Qt's 'void *QMetaContainer::end(void *container) const': names 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaContainer.end' has no cute function yet. Qt's 'void "
        "*QMetaContainer::end(void *container) const': names 'void', which "
        "has no cute class yet.")

  @staticmethod
  def size(*__, **_) -> Never:
    """
    Qt's 'qsizetype QMetaContainer::size(const void *container) const': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaContainer.size' has no cute function yet. Qt's 'qsizetype "
        "QMetaContainer::size(const void *container) const': names 'void', "
        "which has no cute class yet.")
