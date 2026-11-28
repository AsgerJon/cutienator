"""
QOpcUaX509Extension binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuax509extension.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QOpcUaX509Extension(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaX509Extension: a plain Python object standing
  in front of one C++ QOpcUaX509Extension.

  C++ hands a QOpcUaX509Extension around as a copy, so every C++
  QOpcUaX509Extension behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaX509Extension that has a ritual and that
  Python can call so far, 3 names in all: '__eq__', 'setCritical',
  'critical'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaX509Extension &QOpcUaX509Extension::operator=(const
    QOpcUaX509Extension &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QOpcUaX509Extension::~QOpcUaX509Extension()': the destructor:
    Python removes its C++ QOpcUaX509Extension by it, and has no other use
    for it.
  - Qt's 'QOpcUaX509Extension::QOpcUaX509Extension(QOpcUaX509ExtensionData
    *a0)': names 'QOpcUaX509ExtensionData', which has no cute class yet.
  - Qt's 'QOpcUaX509Extension::QOpcUaX509Extension(
    QSharedDataPointer<QOpcUaX509ExtensionData> a0)': takes a type Python has
    no way to hand over yet.

  What to expect
  --------------

  - The C++ QOpcUaX509Extension is created at the first use, not by
    'QOpcUaX509Extension(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaX509Extension back gives a copy the ritual made
    for Python, in a new cute QOpcUaX509Extension.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaX509Extension'

  #  Qt's '~QOpcUaX509Extension()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaX509Extension behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QOpcUaX509ExtensionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def critical(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaX509Extension::critical() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuax509extension.html#critical
    """
    #  bool QOpcUaX509Extension::critical() const
    return self.uglySide.call('ritual_ZNK19QOpcUaX509Extension8criticalEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setCritical(self, critical: bool) -> None:
    """
    Calls Qt's 'void QOpcUaX509Extension::setCritical(bool critical)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extension.html#setCritical

    Parameters
    ----------

    critical : bool
      Passed on as it is.
    """
    #  void QOpcUaX509Extension::setCritical(bool critical)
    self.uglySide.call(
        'ritual_ZN19QOpcUaX509Extension11setCriticalEb', critical,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaX509Extension) -> bool:
    """
    Calls Qt's 'bool QOpcUaX509Extension::operator==(const
    QOpcUaX509Extension &rhs) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extension.html#operator==

    Parameters
    ----------

    rhs : QOpcUaX509Extension
      Passed on as a value: Qt reads the C++ QOpcUaX509Extension, which stays
      Python's own.
    """
    #  bool QOpcUaX509Extension::operator==(const QOpcUaX509Extension &rhs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QOpcUaX509ExtensioneqERKS_', self._valueOf(rhs),
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
    Notes what was given, for Qt's
    'QOpcUaX509Extension::QOpcUaX509Extension()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extension.html#QOpcUaX509Extension
    """
    #  QOpcUaX509Extension::QOpcUaX509Extension()
    self._noteCreation(QOpcUaX509Extension, lambda: Rituals.call(
        'ritual_ZN19QOpcUaX509ExtensionC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaX509Extension) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaX509Extension::QOpcUaX509Extension(const QOpcUaX509Extension
    &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extension.html#QOpcUaX509Extension

    Parameters
    ----------

    a0 : QOpcUaX509Extension
      Passed on as a value: Qt reads the C++ QOpcUaX509Extension, which stays
      Python's own.
    """
    #  QOpcUaX509Extension::QOpcUaX509Extension(const QOpcUaX509Extension
    #      &a0)
    self._noteCreation(QOpcUaX509Extension, lambda: Rituals.call(
        'ritual_ZN19QOpcUaX509ExtensionC1ERKS_', self._valueOf(a0),
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
