"""
QProtobufSelfcheckIterator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtProtobuf/6.12.0/QtProtobuf/private/qprotobufselfcheckiterator_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QProtobufSelfcheckIterator to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArrayView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArrayView = WAIT['QByteArrayView']


class QProtobufSelfcheckIterator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QProtobufSelfcheckIterator: a plain Python object
  standing in front of one C++ QProtobufSelfcheckIterator.

  C++ hands a QProtobufSelfcheckIterator around as a copy, so every C++
  QProtobufSelfcheckIterator behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QProtobufSelfcheckIterator that has a ritual and
  that Python can call so far, 9 names in all: 'fromView', 'isValid',
  '__iadd__', '__isub__', 'data', 'bytesLeft', '__eq__', '__ne__', '__sub__'.
  It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QProtobufSelfcheckIterator
    &QProtobufSelfcheckIterator::operator=(const QProtobufSelfcheckIterator
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QByteArray::const_iterator &QProtobufSelfcheckIterator::operator
    const char *&()': an operator Python has no name for.
  - Qt's 'QByteArray::const_iterator QProtobufSelfcheckIterator::operator
    const char *() const': an operator Python has no name for.
  - Qt's 'char QProtobufSelfcheckIterator::operator*()': an operator Python
    has no name for.
  - Qt's 'QProtobufSelfcheckIterator
    &QProtobufSelfcheckIterator::operator++()': an operator Python has no
    name for.
  - Qt's 'QProtobufSelfcheckIterator
    QProtobufSelfcheckIterator::operator++(int a0)': an operator Python has
    no name for.
  - Qt's 'QProtobufSelfcheckIterator
    &QProtobufSelfcheckIterator::operator--()': an operator Python has no
    name for.
  - Qt's 'QProtobufSelfcheckIterator
    QProtobufSelfcheckIterator::operator--(int a0)': an operator Python has
    no name for.
  - Qt's 'bool operator==(const QProtobufSelfcheckIterator &lhs, const
    QByteArray::const_iterator &other)': takes a type Python has no way to
    hand over yet.
  - Qt's 'bool operator!=(const QProtobufSelfcheckIterator &lhs, const
    QByteArray::const_iterator &other)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QProtobufSelfcheckIterator::~QProtobufSelfcheckIterator()': the
    destructor: Python removes its C++ QProtobufSelfcheckIterator by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QProtobufSelfcheckIterator is created at the first use, not by
    'QProtobufSelfcheckIterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QProtobufSelfcheckIterator back gives a copy the
    ritual made for Python, in a new cute QProtobufSelfcheckIterator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QByteArrayView)
  def fromView(container: QByteArrayView) -> QProtobufSelfcheckIterator:
    """
    Calls Qt's 'QProtobufSelfcheckIterator
    QProtobufSelfcheckIterator::fromView(QByteArrayView container)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufselfcheckiterator.html#fromView

    Parameters
    ----------

    container : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    Returns
    -------

    QProtobufSelfcheckIterator
      A new cute QProtobufSelfcheckIterator around the copy Qt gave back.
      Python owns it.
    """
    #  QProtobufSelfcheckIterator
    #      QProtobufSelfcheckIterator::fromView(QByteArrayView container)
    address = Rituals.call(
        'ritual_ZN26QProtobufSelfcheckIterator8fromViewE14QByteArrayView',
        CuteMixin._valueOf(container),
    )
    return QProtobufSelfcheckIterator._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QProtobufSelfcheckIterator'

  #  Qt's '~QProtobufSelfcheckIterator()'. Naming it makes this a value
  #  class: Python owns every C++ QProtobufSelfcheckIterator behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QProtobufSelfcheckIteratorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QProtobufSelfcheckIterator::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufselfcheckiterator.html#isValid
    """
    #  bool QProtobufSelfcheckIterator::isValid() const
    return self.uglySide.call(
        'ritual_ZNK26QProtobufSelfcheckIterator7isValidEv',
    )

  def data(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QProtobufSelfcheckIterator::data() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufselfcheckiterator.html#data

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QProtobufSelfcheckIterator::data() const
    chars = self.uglySide.call(
        'ritual_ZNK26QProtobufSelfcheckIterator4dataEv',
    )
    return None if chars is None else chars.decode()

  def bytesLeft(self) -> int:
    """
    Calls Qt's 'qsizetype QProtobufSelfcheckIterator::bytesLeft() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufselfcheckiterator.html#bytesLeft
    """
    #  qsizetype QProtobufSelfcheckIterator::bytesLeft() const
    return self.uglySide.call(
        'ritual_ZNK26QProtobufSelfcheckIterator9bytesLeftEv',
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

  @overload(int)
  def __iadd__(self, count: int) -> QProtobufSelfcheckIterator:
    """
    Calls Qt's 'QProtobufSelfcheckIterator
    &QProtobufSelfcheckIterator::operator+=(qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufselfcheckiterator.html#operator+=

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  QProtobufSelfcheckIterator
    #      &QProtobufSelfcheckIterator::operator+=(qsizetype count)
    self.uglySide.call('ritual_ZN26QProtobufSelfcheckIteratorpLEx', count)
    return self

  @overload.fallback
  def __iadd__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(int)
  def __isub__(self, count: int) -> QProtobufSelfcheckIterator:
    """
    Calls Qt's 'QProtobufSelfcheckIterator
    &QProtobufSelfcheckIterator::operator-=(qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufselfcheckiterator.html#operator-=

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  QProtobufSelfcheckIterator
    #      &QProtobufSelfcheckIterator::operator-=(qsizetype count)
    self.uglySide.call('ritual_ZN26QProtobufSelfcheckIteratormIEx', count)
    return self

  @overload.fallback
  def __isub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __eq__(self, rhs: QProtobufSelfcheckIterator) -> bool:
    """
    Calls Qt's 'bool operator==(const QProtobufSelfcheckIterator &lhs, const
    QProtobufSelfcheckIterator &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufselfcheckiterator.html#operator==

    Parameters
    ----------

    rhs : QProtobufSelfcheckIterator
      Passed on as a value: Qt reads the C++ QProtobufSelfcheckIterator,
      which stays Python's own.
    """
    #  bool operator==(const QProtobufSelfcheckIterator &lhs, const
    #      QProtobufSelfcheckIterator &rhs)
    return Rituals.call(
        'ritual_ZeqRK26QProtobufSelfcheckIteratorS1_',
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
  def __ne__(self, rhs: QProtobufSelfcheckIterator) -> bool:
    """
    Calls Qt's 'bool operator!=(const QProtobufSelfcheckIterator &lhs, const
    QProtobufSelfcheckIterator &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufselfcheckiterator.html#operator!=

    Parameters
    ----------

    rhs : QProtobufSelfcheckIterator
      Passed on as a value: Qt reads the C++ QProtobufSelfcheckIterator,
      which stays Python's own.
    """
    #  bool operator!=(const QProtobufSelfcheckIterator &lhs, const
    #      QProtobufSelfcheckIterator &rhs)
    return Rituals.call(
        'ritual_ZneRK26QProtobufSelfcheckIteratorS1_',
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

  @overload(THIS)
  def __sub__(self, rhs: QProtobufSelfcheckIterator) -> int:
    """
    Calls Qt's 'qint64 operator-(const QProtobufSelfcheckIterator &lhs, const
    QProtobufSelfcheckIterator &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufselfcheckiterator.html#operator-

    Parameters
    ----------

    rhs : QProtobufSelfcheckIterator
      Passed on as a value: Qt reads the C++ QProtobufSelfcheckIterator,
      which stays Python's own.
    """
    #  qint64 operator-(const QProtobufSelfcheckIterator &lhs, const
    #      QProtobufSelfcheckIterator &rhs)
    return Rituals.call(
        'ritual_ZmiRK26QProtobufSelfcheckIteratorS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __sub__(self, *args: object) -> object:
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
    Notes what was given, for Qt's
    'QProtobufSelfcheckIterator::QProtobufSelfcheckIterator()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufselfcheckiterator.html
    """
    #  QProtobufSelfcheckIterator::QProtobufSelfcheckIterator()
    self._noteCreation(QProtobufSelfcheckIterator, lambda: Rituals.call(
        'ritual_ZN26QProtobufSelfcheckIteratorC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QProtobufSelfcheckIterator) -> None:
    """
    Notes what was given, for Qt's
    'QProtobufSelfcheckIterator::QProtobufSelfcheckIterator(const
    QProtobufSelfcheckIterator &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufselfcheckiterator.html

    Parameters
    ----------

    other : QProtobufSelfcheckIterator
      Passed on as a value: Qt reads the C++ QProtobufSelfcheckIterator,
      which stays Python's own.
    """
    #  QProtobufSelfcheckIterator::QProtobufSelfcheckIterator(const
    #      QProtobufSelfcheckIterator &other)
    self._noteCreation(QProtobufSelfcheckIterator, lambda: Rituals.call(
        'ritual_ZN26QProtobufSelfcheckIteratorC1ERKS_', self._valueOf(other),
    ))

  @overload(QByteArrayView)
  def __init__(self, container: QByteArrayView) -> None:
    """
    Notes what was given, for Qt's
    'QProtobufSelfcheckIterator::QProtobufSelfcheckIterator(QByteArrayView
    container)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufselfcheckiterator.html

    Parameters
    ----------

    container : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  QProtobufSelfcheckIterator::QProtobufSelfcheckIterator(QByteArrayView
    #      container)
    self._noteCreation(QProtobufSelfcheckIterator, lambda: Rituals.call(
        'ritual_ZN26QProtobufSelfcheckIteratorC1E14QByteArrayView',
        self._valueOf(container),
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
