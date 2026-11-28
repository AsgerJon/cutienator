"""
QUntypedPropertyBinding binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qproperty.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QMetaType, QPropertyBindingError


class QUntypedPropertyBinding(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QUntypedPropertyBinding: a plain Python object
  standing in front of one C++ QUntypedPropertyBinding.

  C++ hands a QUntypedPropertyBinding around as a copy, so every C++
  QUntypedPropertyBinding behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QUntypedPropertyBinding that has a ritual and that
  Python can call so far, 3 names in all: 'isNull', 'error', 'valueMetaType'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QUntypedPropertyBinding::QUntypedPropertyBinding(QMetaType
    metaType, const BindingFunctionVTable *vtable, void *function, const
    QPropertyBindingSourceLocation &location)': names
    'QUntypedPropertyBinding::BindingFunctionVTable', which has no cute class
    yet.
  - Qt's
    'QUntypedPropertyBinding::QUntypedPropertyBinding(QUntypedPropertyBinding
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QUntypedPropertyBinding &QUntypedPropertyBinding::operator=(const
    QUntypedPropertyBinding &other)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'QUntypedPropertyBinding
    &QUntypedPropertyBinding::operator=(QUntypedPropertyBinding &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QUntypedPropertyBinding::~QUntypedPropertyBinding()': the
    destructor: Python removes its C++ QUntypedPropertyBinding by it, and has
    no other use for it.
  - Qt's 'QUntypedPropertyBinding::QUntypedPropertyBinding(void *priv)':
    names 'void', which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 12 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QUntypedPropertyBinding is created at the first use, not by
    'QUntypedPropertyBinding(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QUntypedPropertyBinding back gives a copy the ritual
    made for Python, in a new cute QUntypedPropertyBinding.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QUntypedPropertyBinding'

  #  Qt's '~QUntypedPropertyBinding()'. Naming it makes this a value class:
  #  Python owns every C++ QUntypedPropertyBinding behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QUntypedPropertyBindingD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QUntypedPropertyBinding::isNull() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/quntypedpropertybinding.html#isNull
    """
    #  bool QUntypedPropertyBinding::isNull() const
    return self.uglySide.call('ritual_ZNK23QUntypedPropertyBinding6isNullEv')

  def error(self) -> QPropertyBindingError:
    """
    Calls Qt's 'QPropertyBindingError QUntypedPropertyBinding::error()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/quntypedpropertybinding.html#error

    Returns
    -------

    QPropertyBindingError
      A new cute QPropertyBindingError around the copy Qt gave back. Python
      owns it.
    """
    #  QPropertyBindingError QUntypedPropertyBinding::error() const
    address = self.uglySide.call(
        'ritual_ZNK23QUntypedPropertyBinding5errorEv',
    )
    from . import QPropertyBindingError
    return QPropertyBindingError._cuteOwning(address)

  def valueMetaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QUntypedPropertyBinding::valueMetaType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/quntypedpropertybinding.html#valueMetaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QUntypedPropertyBinding::valueMetaType() const
    address = self.uglySide.call(
        'ritual_ZNK23QUntypedPropertyBinding13valueMetaTypeEv',
    )
    from . import QMetaType
    return QMetaType._cuteOwning(address)

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
    'QUntypedPropertyBinding::QUntypedPropertyBinding()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/quntypedpropertybinding.html
    """
    #  QUntypedPropertyBinding::QUntypedPropertyBinding()
    self._noteCreation(QUntypedPropertyBinding, lambda: Rituals.call(
        'ritual_ZN23QUntypedPropertyBindingC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QUntypedPropertyBinding) -> None:
    """
    Notes what was given, for Qt's
    'QUntypedPropertyBinding::QUntypedPropertyBinding(const
    QUntypedPropertyBinding &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/quntypedpropertybinding.html

    Parameters
    ----------

    other : QUntypedPropertyBinding
      Passed on as a value: Qt reads the C++ QUntypedPropertyBinding, which
      stays Python's own.
    """
    #  QUntypedPropertyBinding::QUntypedPropertyBinding(const
    #      QUntypedPropertyBinding &other)
    self._noteCreation(QUntypedPropertyBinding, lambda: Rituals.call(
        'ritual_ZN23QUntypedPropertyBindingC1ERKS_', self._valueOf(other),
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
