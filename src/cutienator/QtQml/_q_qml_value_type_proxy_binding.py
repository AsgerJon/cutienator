"""
QQmlValueTypeProxyBinding binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlvaluetypeproxybinding_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlValueTypeProxyBinding to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQmlAbstractBinding, QQmlPropertyData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QQmlPropertyIndex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlPropertyIndex = WAIT['QQmlPropertyIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlValueTypeProxyBinding(QQmlAbstractBinding):
  """
  The cute side of Qt's QQmlValueTypeProxyBinding: a plain Python object
  standing in front of one C++ QQmlValueTypeProxyBinding.

  It is built on the cute 'QQmlAbstractBinding', as Qt's
  QQmlValueTypeProxyBinding is built on Qt's QQmlAbstractBinding, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlValueTypeProxyBinding that has a ritual and that
  Python can call so far, 5 names in all: 'subBindings', 'binding',
  'removeBindings', 'setEnabled', 'kind'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlValueTypeProxyBinding::~QQmlValueTypeProxyBinding()': the
    destructor: Python never removes a C++ QQmlValueTypeProxyBinding.

  What to expect
  --------------

  - The C++ QQmlValueTypeProxyBinding is created at the first use, not by
    'QQmlValueTypeProxyBinding(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlValueTypeProxyBinding.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlValueTypeProxyBinding'

  #  A C++ QQmlValueTypeProxyBinding Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlValueTypeProxyBinding'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def subBindings(self) -> Optional[QQmlAbstractBinding]:
    """
    Calls Qt's 'QQmlAbstractBinding *QQmlValueTypeProxyBinding::subBindings()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvaluetypeproxybinding.html#subBindings

    Returns
    -------

    Optional[QQmlAbstractBinding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlAbstractBinding *QQmlValueTypeProxyBinding::subBindings() const
    address = self.uglySide.call(
        'ritual_ZNK25QQmlValueTypeProxyBinding11subBindingsEv',
    )
    return QQmlAbstractBinding._cuteAt(address)

  @overload(QQmlPropertyIndex)
  def binding(
      self,
      targetPropertyIndex: QQmlPropertyIndex,
  ) -> Optional[QQmlAbstractBinding]:
    """
    Calls Qt's 'QQmlAbstractBinding
    *QQmlValueTypeProxyBinding::binding(QQmlPropertyIndex
    targetPropertyIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvaluetypeproxybinding.html#binding

    Parameters
    ----------

    targetPropertyIndex : QQmlPropertyIndex
      Passed on as a value: Qt reads the C++ QQmlPropertyIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QQmlAbstractBinding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlAbstractBinding
    #      *QQmlValueTypeProxyBinding::binding(QQmlPropertyIndex
    #      targetPropertyIndex) const
    address = self.uglySide.call(
        'ritual_ZNK25QQmlValueTypeProxyBinding7bindingE17QQmlPropertyIndex',
        self._valueOf(targetPropertyIndex),
    )
    return QQmlAbstractBinding._cuteAt(address)

  def kind(self) -> QQmlAbstractBinding.Kind:
    """
    Calls Qt's 'Kind QQmlValueTypeProxyBinding::kind() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvaluetypeproxybinding.html#kind

    Returns
    -------

    QQmlAbstractBinding.Kind
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlAbstractBinding.Kind(number)' gives.
    """
    #  Kind QQmlValueTypeProxyBinding::kind() const
    return QQmlAbstractBinding.Kind(self.uglySide.call(
        'ritual_ZNK25QQmlValueTypeProxyBinding4kindEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool, QQmlPropertyData.WriteFlags)
  def setEnabled(self, a0: bool, a1: QQmlPropertyData.WriteFlags) -> None:
    """
    Calls Qt's 'void QQmlValueTypeProxyBinding::setEnabled(bool a0,
    QQmlPropertyData::WriteFlags a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvaluetypeproxybinding.html#setEnabled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.

    a1 : QQmlPropertyData.WriteFlags
      Passed on as its number.
    """
    #  void QQmlValueTypeProxyBinding::setEnabled(bool a0,
    #      QQmlPropertyData::WriteFlags a1)
    ritual = (
        'ritual_ZN25QQmlValueTypeProxyBinding10setEnabledEb6QFlagsIN16QQmlP'
        'ropertyData9WriteFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQmlValueTypeProxyBinding10setEnabledEb6QFlagsIN1'
          '6QQmlPropertyData9WriteFlagEE')
    self.uglySide.call(ritual, a0, a1.value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject, QQmlPropertyIndex)
  @overload(NoneType, QQmlPropertyIndex)
  def __init__(
      self,
      o: Optional[QObject],
      coreIndex: QQmlPropertyIndex,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlValueTypeProxyBinding::QQmlValueTypeProxyBinding(QObject *o,
    QQmlPropertyIndex coreIndex)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvaluetypeproxybinding.html

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    coreIndex : QQmlPropertyIndex
      Passed on as a value: Qt reads the C++ QQmlPropertyIndex, which stays
      Python's own.
    """
    #  QQmlValueTypeProxyBinding::QQmlValueTypeProxyBinding(QObject *o,
    #      QQmlPropertyIndex coreIndex)
    self._noteCreation(QQmlValueTypeProxyBinding, lambda: Rituals.call(
        'ritual_ZN25QQmlValueTypeProxyBindingC1EP7QObject17QQmlPropertyInde'
        'x',
        self._addressOf(o, 'QObject'), self._valueOf(coreIndex),
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

  @overload(int)
  def removeBindings(self, mask: int) -> None:
    """
    Calls Qt's 'void QQmlValueTypeProxyBinding::removeBindings(quint32
    mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvaluetypeproxybinding.html#removeBindings

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QQmlValueTypeProxyBinding::removeBindings(quint32 mask)
    self.uglySide.call(
        'ritual_ZN25QQmlValueTypeProxyBinding14removeBindingsEj', mask,
    )
