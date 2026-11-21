"""
QAssociativeIterable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qassociativeiterable.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QAssociativeIterable(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAssociativeIterable: a plain Python object standing
  in front of one C++ QAssociativeIterable.

  C++ hands a QAssociativeIterable around as a copy, so every C++
  QAssociativeIterable behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QAssociativeIterable that has a ritual and that
  Python can call so far, 6 names in all: 'containsKey', 'insertKey',
  'removeKey', 'value', 'setValue', 'canRandomAccessIterate'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAssociativeIterable::~QAssociativeIterable()': the destructor:
    Python removes its C++ QAssociativeIterable by it, and has no other use
    for it.

  What has no ritual
  ------------------

  16 of the 24 functions Qt declares: 13 takes or gives a type that cannot be
  passed yet; 3 a template.

  What to expect
  --------------

  - The C++ QAssociativeIterable is created at the first use, not by
    'QAssociativeIterable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QAssociativeIterable back gives a copy the ritual
    made for Python, in a new cute QAssociativeIterable.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAssociativeIterable'

  #  Qt's '~QAssociativeIterable()'. Naming it makes this a value class:
  #  Python owns every C++ QAssociativeIterable behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QAssociativeIterableD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def value(self, key: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QAssociativeIterable::value(const QVariant &key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qassociativeiterable.html#value

    Parameters
    ----------

    key : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAssociativeIterable::value(const QVariant &key) const
    address = self.uglySide.call(
        'ritual_ZNK20QAssociativeIterable5valueERK8QVariant',
        self._valueOf(key),
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  def canRandomAccessIterate(self) -> bool:
    """
    Calls Qt's 'bool QAssociativeIterable::canRandomAccessIterate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qassociativeiterable.html#canRandomAccessIterate
    """
    #  bool QAssociativeIterable::canRandomAccessIterate() const
    return self.uglySide.call(
        'ritual_ZNK20QAssociativeIterable22canRandomAccessIterateEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant, QVariant)
  def setValue(self, key: QVariant, mapped: QVariant) -> None:
    """
    Calls Qt's 'void QAssociativeIterable::setValue(const QVariant &key,
    const QVariant &mapped)'.

    Qt's own words: https://doc.qt.io/qt-6/qassociativeiterable.html#setValue

    Parameters
    ----------

    key : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    mapped : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAssociativeIterable::setValue(const QVariant &key, const
    #      QVariant &mapped)
    self.uglySide.call(
        'ritual_ZN20QAssociativeIterable8setValueERK8QVariantS2_',
        self._valueOf(key), self._valueOf(mapped),
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
    'QAssociativeIterable::QAssociativeIterable()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qassociativeiterable.html#QAssociativeIterable
    """
    #  QAssociativeIterable::QAssociativeIterable()
    self._noteCreation(QAssociativeIterable, lambda: Rituals.call(
        'ritual_ZN20QAssociativeIterableC1Ev',
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

  @overload(QVariant)
  def containsKey(self, key: QVariant) -> bool:
    """
    Calls Qt's 'bool QAssociativeIterable::containsKey(const QVariant &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qassociativeiterable.html#containsKey

    Parameters
    ----------

    key : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QAssociativeIterable::containsKey(const QVariant &key)
    return self.uglySide.call(
        'ritual_ZN20QAssociativeIterable11containsKeyERK8QVariant',
        self._valueOf(key),
    )

  @overload(QVariant)
  def insertKey(self, key: QVariant) -> None:
    """
    Calls Qt's 'void QAssociativeIterable::insertKey(const QVariant &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qassociativeiterable.html#insertKey

    Parameters
    ----------

    key : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAssociativeIterable::insertKey(const QVariant &key)
    self.uglySide.call(
        'ritual_ZN20QAssociativeIterable9insertKeyERK8QVariant',
        self._valueOf(key),
    )

  @overload(QVariant)
  def removeKey(self, key: QVariant) -> None:
    """
    Calls Qt's 'void QAssociativeIterable::removeKey(const QVariant &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qassociativeiterable.html#removeKey

    Parameters
    ----------

    key : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAssociativeIterable::removeKey(const QVariant &key)
    self.uglySide.call(
        'ritual_ZN20QAssociativeIterable9removeKeyERK8QVariant',
        self._valueOf(key),
    )
