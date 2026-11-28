"""
QQuickColorSpaceValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickvaluetypes_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickColorSpaceValueType to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtGui import QColorSpace
from . import QQuickColorSpaceEnums

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QVariant
  from ..QtQml import QJSValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSValue = WAIT['QJSValue']


class QQuickColorSpaceValueType(QColorSpace):
  """
  The cute side of Qt's QQuickColorSpaceValueType: a plain Python object
  standing in front of one C++ QQuickColorSpaceValueType.

  It is built on the cute 'QColorSpace', as Qt's QQuickColorSpaceValueType is
  built on Qt's QColorSpace, and has everything that class has.

  C++ hands a QQuickColorSpaceValueType around as a copy, so every C++
  QQuickColorSpaceValueType behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickColorSpaceValueType that has a ritual and that
  Python can call so far, 9 names in all: 'create', 'namedColorSpace',
  'setNamedColorSpace', 'primaries', 'setPrimaries', 'transferFunction',
  'setTransferFunction', 'gamma', 'setGamma'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQuickColorSpaceValueType::qt_qmlMarker_anonymous()': one of
    Qt's own inner workings.
  - Qt's 'void QQuickColorSpaceValueType::qt_qmlMarker_foreign()': one of
    Qt's own inner workings.
  - Qt's 'void QQuickColorSpaceValueType::qt_qmlMarker_extended()': one of
    Qt's own inner workings.
  - Qt's 'QQuickColorSpaceValueType::~QQuickColorSpaceValueType()': the
    destructor: Python removes its C++ QQuickColorSpaceValueType by it, and
    has no other use for it.

  What has no ritual
  ------------------

  3 of the 16 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQuickColorSpaceValueType is created at the first use, not by
    'QQuickColorSpaceValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickColorSpaceValueType back gives a copy the
    ritual made for Python, in a new cute QQuickColorSpaceValueType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QJSValue)
  def create(params: QJSValue) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickColorSpaceValueType::create(const QJSValue
    &params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorspacevaluetype.html#create

    Parameters
    ----------

    params : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickColorSpaceValueType::create(const QJSValue &params)
    address = Rituals.call(
        'ritual_ZN25QQuickColorSpaceValueType6createERK8QJSValue',
        CuteMixin._valueOf(params),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickColorSpaceValueType'

  #  Qt's '~QQuickColorSpaceValueType()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickColorSpaceValueType behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QQuickColorSpaceValueTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def namedColorSpace(self) -> QQuickColorSpaceEnums.NamedColorSpace:
    """
    Calls Qt's 'QQuickColorSpaceEnums::NamedColorSpace
    QQuickColorSpaceValueType::namedColorSpace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorspacevaluetype.html#namedColorSpace

    Returns
    -------

    QQuickColorSpaceEnums.NamedColorSpace
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickColorSpaceEnums.NamedColorSpace(number)' gives.
    """
    #  QQuickColorSpaceEnums::NamedColorSpace
    #      QQuickColorSpaceValueType::namedColorSpace() const
    return QQuickColorSpaceEnums.NamedColorSpace(self.uglySide.call(
        'ritual_ZNK25QQuickColorSpaceValueType15namedColorSpaceEv',
    ))

  def primaries(self) -> QQuickColorSpaceEnums.Primaries:
    """
    Calls Qt's 'QQuickColorSpaceEnums::Primaries
    QQuickColorSpaceValueType::primaries() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorspacevaluetype.html#primaries

    Returns
    -------

    QQuickColorSpaceEnums.Primaries
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickColorSpaceEnums.Primaries(number)' gives.
    """
    #  QQuickColorSpaceEnums::Primaries
    #      QQuickColorSpaceValueType::primaries() const
    return QQuickColorSpaceEnums.Primaries(self.uglySide.call(
        'ritual_ZNK25QQuickColorSpaceValueType9primariesEv',
    ))

  def transferFunction(self) -> QQuickColorSpaceEnums.TransferFunction:
    """
    Calls Qt's 'QQuickColorSpaceEnums::TransferFunction
    QQuickColorSpaceValueType::transferFunction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorspacevaluetype.html#transferFunction

    Returns
    -------

    QQuickColorSpaceEnums.TransferFunction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickColorSpaceEnums.TransferFunction(number)' gives.
    """
    #  QQuickColorSpaceEnums::TransferFunction
    #      QQuickColorSpaceValueType::transferFunction() const
    return QQuickColorSpaceEnums.TransferFunction(self.uglySide.call(
        'ritual_ZNK25QQuickColorSpaceValueType16transferFunctionEv',
    ))

  def gamma(self) -> float:
    """
    Calls Qt's 'float QQuickColorSpaceValueType::gamma() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorspacevaluetype.html#gamma
    """
    #  float QQuickColorSpaceValueType::gamma() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickColorSpaceValueType5gammaEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickColorSpaceEnums.NamedColorSpace)
  def setNamedColorSpace(
      self,
      namedColorSpace: QQuickColorSpaceEnums.NamedColorSpace,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickColorSpaceValueType::setNamedColorSpace(QQuickColorSpaceEnums::
    NamedColorSpace namedColorSpace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorspacevaluetype.html#setNamedColorSpace

    Parameters
    ----------

    namedColorSpace : QQuickColorSpaceEnums.NamedColorSpace
      Passed on as its number.
    """
    #  void QQuickColorSpaceValueType::setNamedColorSpace(
    #      QQuickColorSpaceEnums::NamedColorSpace namedColorSpace)
    self.uglySide.call(
        'ritual_ZN25QQuickColorSpaceValueType18setNamedColorSpaceEN21QQuick'
        'ColorSpaceEnums15NamedColorSpaceE',
        namedColorSpace.value,
    )

  @overload(QQuickColorSpaceEnums.Primaries)
  def setPrimaries(
      self,
      primariesId: QQuickColorSpaceEnums.Primaries,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickColorSpaceValueType::setPrimaries(QQuickColorSpaceEnums::Primaries
    primariesId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorspacevaluetype.html#setPrimaries

    Parameters
    ----------

    primariesId : QQuickColorSpaceEnums.Primaries
      Passed on as its number.
    """
    #  void QQuickColorSpaceValueType::setPrimaries(QQuickColorSpaceEnums::
    #      Primaries primariesId)
    self.uglySide.call(
        'ritual_ZN25QQuickColorSpaceValueType12setPrimariesEN21QQuickColorS'
        'paceEnums9PrimariesE',
        primariesId.value,
    )

  @overload(QQuickColorSpaceEnums.TransferFunction)
  def setTransferFunction(
      self,
      transferFunction: QQuickColorSpaceEnums.TransferFunction,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickColorSpaceValueType::setTransferFunction(QQuickColorSpaceEnums::
    TransferFunction transferFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorspacevaluetype.html#setTransferFunction

    Parameters
    ----------

    transferFunction : QQuickColorSpaceEnums.TransferFunction
      Passed on as its number.
    """
    #  void QQuickColorSpaceValueType::setTransferFunction(
    #      QQuickColorSpaceEnums::TransferFunction transferFunction)
    self.uglySide.call(
        'ritual_ZN25QQuickColorSpaceValueType19setTransferFunctionEN21QQuic'
        'kColorSpaceEnums16TransferFunctionE',
        transferFunction.value,
    )

  @overload(float)
  def setGamma(self, gamma: float) -> None:
    """
    Calls Qt's 'void QQuickColorSpaceValueType::setGamma(float gamma)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolorspacevaluetype.html#setGamma

    Parameters
    ----------

    gamma : float
      Passed on as it is.
    """
    #  void QQuickColorSpaceValueType::setGamma(float gamma)
    self.uglySide.call(
        'ritual_ZN25QQuickColorSpaceValueType8setGammaEf', gamma,
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
