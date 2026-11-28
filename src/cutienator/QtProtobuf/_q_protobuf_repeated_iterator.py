"""
QProtobufRepeatedIterator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtProtobuf/qprotobufrepeatediterator.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QProtobufMessage


class QProtobufRepeatedIterator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QProtobufRepeatedIterator: a plain Python object
  standing in front of one C++ QProtobufRepeatedIterator.

  What exists
  -----------

  Every function of Qt's QProtobufRepeatedIterator that has a ritual and that
  Python can call so far, 5 names in all: 'isValid', 'hasNext', 'next',
  'addNext', 'push'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QProtobufRepeatedIterator::~QProtobufRepeatedIterator()': the
    destructor: Python never removes a C++ QProtobufRepeatedIterator.
  - Qt's 'QProtobufRepeatedIterator::QProtobufRepeatedIterator(
    QProtobufRepeatedIterator &&other)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QProtobufRepeatedIterator
    &QProtobufRepeatedIterator::operator=(QProtobufRepeatedIterator
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QProtobufRepeatedIterator::swap(QProtobufRepeatedIterator
    &other)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  7 of the 17 functions Qt declares: 5 a template; 2 forbidden.

  What to expect
  --------------

  - The C++ QProtobufRepeatedIterator is created at the first use, not by
    'QProtobufRepeatedIterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QProtobufRepeatedIterator.
  - Each name of Qt's QProtobufRepeatedIterator that has no cute function
    yet, 'MakeImpl', 'fromHash', 'fromList', 'swap', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QProtobufRepeatedIterator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QProtobufRepeatedIterator::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufrepeatediterator.html#isValid
    """
    #  bool QProtobufRepeatedIterator::isValid() const
    return self.uglySide.call(
        'ritual_ZNK25QProtobufRepeatedIterator7isValidEv',
    )

  def hasNext(self) -> bool:
    """
    Calls Qt's 'bool QProtobufRepeatedIterator::hasNext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufrepeatediterator.html#hasNext
    """
    #  bool QProtobufRepeatedIterator::hasNext() const
    return self.uglySide.call(
        'ritual_ZNK25QProtobufRepeatedIterator7hasNextEv',
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
    'QProtobufRepeatedIterator::QProtobufRepeatedIterator()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufrepeatediterator.html
    """
    #  QProtobufRepeatedIterator::QProtobufRepeatedIterator()
    self._noteCreation(QProtobufRepeatedIterator, lambda: Rituals.call(
        'ritual_ZN25QProtobufRepeatedIteratorC1Ev',
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

  def next(self) -> Optional[QProtobufMessage]:
    """
    Calls Qt's 'QProtobufMessage *QProtobufRepeatedIterator::next()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufrepeatediterator.html#next

    Returns
    -------

    Optional[QProtobufMessage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QProtobufMessage *QProtobufRepeatedIterator::next()
    address = self.uglySide.call(
        'ritual_ZN25QProtobufRepeatedIterator4nextEv',
    )
    from . import QProtobufMessage
    return QProtobufMessage._cuteAt(address)

  def addNext(self) -> Optional[QProtobufMessage]:
    """
    Calls Qt's 'QProtobufMessage *QProtobufRepeatedIterator::addNext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufrepeatediterator.html#addNext

    Returns
    -------

    Optional[QProtobufMessage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QProtobufMessage *QProtobufRepeatedIterator::addNext()
    address = self.uglySide.call(
        'ritual_ZN25QProtobufRepeatedIterator7addNextEv',
    )
    from . import QProtobufMessage
    return QProtobufMessage._cuteAt(address)

  def push(self) -> None:
    """
    Calls Qt's 'void QProtobufRepeatedIterator::push()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufrepeatediterator.html#push
    """
    #  void QProtobufRepeatedIterator::push()
    self.uglySide.call('ritual_ZN25QProtobufRepeatedIterator4pushEv')

  @staticmethod
  def MakeImpl(*__, **_) -> Never:
    """
    Qt's 'QProtobufRepeatedIterator::MakeImpl': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QProtobufRepeatedIterator.MakeImpl' has no cute function yet. "
        "Qt's 'QProtobufRepeatedIterator::MakeImpl': a template: a pattern "
        "and no single function.")

  @staticmethod
  def fromHash(*__, **_) -> Never:
    """
    Qt's 'QProtobufRepeatedIterator::fromHash': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QProtobufRepeatedIterator.fromHash' has no cute function yet. "
        "Qt's 'QProtobufRepeatedIterator::fromHash': a template: a pattern "
        "and no single function.")

  @staticmethod
  def fromList(*__, **_) -> Never:
    """
    Qt's 'QProtobufRepeatedIterator::fromList': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QProtobufRepeatedIterator.fromList' has no cute function yet. "
        "Qt's 'QProtobufRepeatedIterator::fromList': a template: a pattern "
        "and no single function.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QProtobufRepeatedIterator::swap(QProtobufRepeatedIterator
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QProtobufRepeatedIterator.swap' has no cute function yet. Qt's "
        "'void QProtobufRepeatedIterator::swap(QProtobufRepeatedIterator "
        "&other)': takes a type Python has no way to hand over yet.")
