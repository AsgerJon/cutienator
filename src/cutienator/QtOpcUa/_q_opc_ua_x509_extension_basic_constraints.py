"""
QOpcUaX509ExtensionBasicConstraints binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuax509extensionbasicconstraints.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..occult import Rituals
from . import QOpcUaX509Extension


class QOpcUaX509ExtensionBasicConstraints(QOpcUaX509Extension):
  """
  The cute side of Qt's QOpcUaX509ExtensionBasicConstraints: a plain Python
  object standing in front of one C++ QOpcUaX509ExtensionBasicConstraints.

  It is built on the cute 'QOpcUaX509Extension', as Qt's
  QOpcUaX509ExtensionBasicConstraints is built on Qt's QOpcUaX509Extension,
  and has everything that class has.

  C++ hands a QOpcUaX509ExtensionBasicConstraints around as a copy, so every
  C++ QOpcUaX509ExtensionBasicConstraints behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaX509ExtensionBasicConstraints that has a
  ritual and that Python can call so far, 5 names in all: '__eq__', 'setCa',
  'ca', 'setPathLength', 'pathLength'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaX509ExtensionBasicConstraints
    &QOpcUaX509ExtensionBasicConstraints::operator=(const
    QOpcUaX509ExtensionBasicConstraints &a0)': assignment: Python binds a
    name and has no operator for it.
  - Qt's 'QOpcUaX509ExtensionBasicConstraints::
    ~QOpcUaX509ExtensionBasicConstraints()': the destructor: Python removes
    its C++ QOpcUaX509ExtensionBasicConstraints by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QOpcUaX509ExtensionBasicConstraints is created at the first use,
    not by 'QOpcUaX509ExtensionBasicConstraints(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaX509ExtensionBasicConstraints back gives a copy
    the ritual made for Python, in a new cute
    QOpcUaX509ExtensionBasicConstraints.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaX509ExtensionBasicConstraints'

  #  Qt's '~QOpcUaX509ExtensionBasicConstraints()'. Naming it makes this a
  #  value class: Python owns every C++ QOpcUaX509ExtensionBasicConstraints
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN35QOpcUaX509ExtensionBasicConstraintsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def ca(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaX509ExtensionBasicConstraints::ca() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extensionbasicconstraints.html#ca
    """
    #  bool QOpcUaX509ExtensionBasicConstraints::ca() const
    return self.uglySide.call(
        'ritual_ZNK35QOpcUaX509ExtensionBasicConstraints2caEv',
    )

  def pathLength(self) -> int:
    """
    Calls Qt's 'int QOpcUaX509ExtensionBasicConstraints::pathLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extensionbasicconstraints.html
    """
    #  int QOpcUaX509ExtensionBasicConstraints::pathLength() const
    return self.uglySide.call(
        'ritual_ZNK35QOpcUaX509ExtensionBasicConstraints10pathLengthEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setCa(self, value: bool) -> None:
    """
    Calls Qt's 'void QOpcUaX509ExtensionBasicConstraints::setCa(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extensionbasicconstraints.html#setCa

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QOpcUaX509ExtensionBasicConstraints::setCa(bool value)
    self.uglySide.call(
        'ritual_ZN35QOpcUaX509ExtensionBasicConstraints5setCaEb', value,
    )

  @overload(int)
  def setPathLength(self, length: int) -> None:
    """
    Calls Qt's 'void QOpcUaX509ExtensionBasicConstraints::setPathLength(int
    length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extensionbasicconstraints.html

    Parameters
    ----------

    length : int
      Passed on as it is.
    """
    #  void QOpcUaX509ExtensionBasicConstraints::setPathLength(int length)
    self.uglySide.call(
        'ritual_ZN35QOpcUaX509ExtensionBasicConstraints13setPathLengthEi',
        length,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaX509ExtensionBasicConstraints) -> bool:
    """
    Calls Qt's 'bool QOpcUaX509ExtensionBasicConstraints::operator==(const
    QOpcUaX509ExtensionBasicConstraints &rhs) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extensionbasicconstraints.html

    Parameters
    ----------

    rhs : QOpcUaX509ExtensionBasicConstraints
      Passed on as a value: Qt reads the C++
      QOpcUaX509ExtensionBasicConstraints, which stays Python's own.
    """
    #  bool QOpcUaX509ExtensionBasicConstraints::operator==(const
    #      QOpcUaX509ExtensionBasicConstraints &rhs) const
    return self.uglySide.call(
        'ritual_ZNK35QOpcUaX509ExtensionBasicConstraintseqERKS_',
        self._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QOpcUaX509ExtensionBasicConstraints::
    QOpcUaX509ExtensionBasicConstraints()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extensionbasicconstraints.html
    """
    #  QOpcUaX509ExtensionBasicConstraints::
    #      QOpcUaX509ExtensionBasicConstraints()
    self._noteCreation(
        QOpcUaX509ExtensionBasicConstraints, lambda: Rituals.call(
            'ritual_ZN35QOpcUaX509ExtensionBasicConstraintsC1Ev',
        ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaX509ExtensionBasicConstraints) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaX509ExtensionBasicConstraints::
    QOpcUaX509ExtensionBasicConstraints(const
    QOpcUaX509ExtensionBasicConstraints &a0)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extensionbasicconstraints.html

    Parameters
    ----------

    a0 : QOpcUaX509ExtensionBasicConstraints
      Passed on as a value: Qt reads the C++
      QOpcUaX509ExtensionBasicConstraints, which stays Python's own.
    """
    #  QOpcUaX509ExtensionBasicConstraints::
    #      QOpcUaX509ExtensionBasicConstraints(const
    #      QOpcUaX509ExtensionBasicConstraints &a0)
    self._noteCreation(
        QOpcUaX509ExtensionBasicConstraints, lambda: Rituals.call(
            'ritual_ZN35QOpcUaX509ExtensionBasicConstraintsC1ERKS_',
            self._valueOf(a0),
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
