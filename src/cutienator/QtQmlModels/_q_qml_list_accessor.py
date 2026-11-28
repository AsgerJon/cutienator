"""
QQmlListAccessor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistaccessor_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlListAccessor to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QQmlListAccessor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlListAccessor: a plain Python object standing in
  front of one C++ QQmlListAccessor.

  C++ hands a QQmlListAccessor around as a copy, so every C++
  QQmlListAccessor behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlListAccessor that has a ritual and that Python
  can call so far, 7 names in all: 'list', 'setList', 'isValid', 'count',
  'at', 'set', 'type'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlListAccessor::~QQmlListAccessor()': the destructor: Python
    removes its C++ QQmlListAccessor by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlListAccessor is created at the first use, not by
    'QQmlListAccessor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlListAccessor back gives a copy the ritual made
    for Python, in a new cute QQmlListAccessor.
  """

  #  The enums Qt writes inside QQmlListAccessor, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QQmlListAccessor::Type' of Qt, with the 10 names Qt gives in
    it.
    """

    Invalid = Kee[int](0)
    StringList = Kee[int](1)
    UrlList = Kee[int](2)
    VariantList = Kee[int](3)
    ObjectList = Kee[int](4)
    ListProperty = Kee[int](5)
    Instance = Kee[int](6)
    Integer = Kee[int](7)
    ObjectSequence = Kee[int](8)
    ValueSequence = Kee[int](9)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlListAccessor'

  #  Qt's '~QQmlListAccessor()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlListAccessor behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QQmlListAccessorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def list(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlListAccessor::list() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistaccessor.html#list

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlListAccessor::list() const
    address = self.uglySide.call('ritual_ZNK16QQmlListAccessor4listEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlListAccessor::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistaccessor.html#isValid
    """
    #  bool QQmlListAccessor::isValid() const
    return self.uglySide.call('ritual_ZNK16QQmlListAccessor7isValidEv')

  def count(self) -> int:
    """
    Calls Qt's 'qsizetype QQmlListAccessor::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistaccessor.html#count
    """
    #  qsizetype QQmlListAccessor::count() const
    return self.uglySide.call('ritual_ZNK16QQmlListAccessor5countEv')

  @overload(int)
  def at(self, a0: int) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlListAccessor::at(qsizetype a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistaccessor.html#at

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlListAccessor::at(qsizetype a0) const
    address = self.uglySide.call('ritual_ZNK16QQmlListAccessor2atEx', a0)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def type(self) -> Type:
    """
    Calls Qt's 'Type QQmlListAccessor::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistaccessor.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QQmlListAccessor::type() const
    return QQmlListAccessor.Type(self.uglySide.call(
        'ritual_ZNK16QQmlListAccessor4typeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setList(self, a0: QVariant) -> None:
    """
    Calls Qt's 'void QQmlListAccessor::setList(const QVariant &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistaccessor.html#setList

    Parameters
    ----------

    a0 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlListAccessor::setList(const QVariant &a0)
    self.uglySide.call(
        'ritual_ZN16QQmlListAccessor7setListERK8QVariant', self._valueOf(a0),
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
    Notes what was given, for Qt's 'QQmlListAccessor::QQmlListAccessor()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistaccessor.html#QQmlListAccessor
    """
    #  QQmlListAccessor::QQmlListAccessor()
    self._noteCreation(QQmlListAccessor, lambda: Rituals.call(
        'ritual_ZN16QQmlListAccessorC1Ev',
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

  @overload(int, QVariant)
  def set(self, a0: int, a1: QVariant) -> None:
    """
    Calls Qt's 'void QQmlListAccessor::set(qsizetype a0, const QVariant
    &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistaccessor.html#set

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlListAccessor::set(qsizetype a0, const QVariant &a1)
    self.uglySide.call(
        'ritual_ZN16QQmlListAccessor3setExRK8QVariant',
        a0, self._valueOf(a1),
    )
