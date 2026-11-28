"""
QRhiDepthStencilClearValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QRhiDepthStencilClearValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhiDepthStencilClearValue: a plain Python object
  standing in front of one C++ QRhiDepthStencilClearValue.

  C++ hands a QRhiDepthStencilClearValue around as a copy, so every C++
  QRhiDepthStencilClearValue behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QRhiDepthStencilClearValue that has a ritual and
  that Python can call so far, 6 names in all: 'depthClearValue',
  'setDepthClearValue', 'stencilClearValue', 'setStencilClearValue',
  '__eq__', '__ne__'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhiDepthStencilClearValue::~QRhiDepthStencilClearValue()': the
    destructor: Python removes its C++ QRhiDepthStencilClearValue by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QRhiDepthStencilClearValue is created at the first use, not by
    'QRhiDepthStencilClearValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiDepthStencilClearValue back gives a copy the
    ritual made for Python, in a new cute QRhiDepthStencilClearValue.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiDepthStencilClearValue'

  #  Qt's '~QRhiDepthStencilClearValue()'. Naming it makes this a value
  #  class: Python owns every C++ QRhiDepthStencilClearValue behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QRhiDepthStencilClearValueD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def depthClearValue(self) -> float:
    """
    Calls Qt's 'float QRhiDepthStencilClearValue::depthClearValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhidepthstencilclearvalue.html#depthClearValue
    """
    #  float QRhiDepthStencilClearValue::depthClearValue() const
    return self.uglySide.call(
        'ritual_ZNK26QRhiDepthStencilClearValue15depthClearValueEv',
    )

  def stencilClearValue(self) -> int:
    """
    Calls Qt's 'quint32 QRhiDepthStencilClearValue::stencilClearValue()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhidepthstencilclearvalue.html#stencilClearValue
    """
    #  quint32 QRhiDepthStencilClearValue::stencilClearValue() const
    return self.uglySide.call(
        'ritual_ZNK26QRhiDepthStencilClearValue17stencilClearValueEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setDepthClearValue(self, d: float) -> None:
    """
    Calls Qt's 'void QRhiDepthStencilClearValue::setDepthClearValue(float
    d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhidepthstencilclearvalue.html#setDepthClearValue

    Parameters
    ----------

    d : float
      Passed on as it is.
    """
    #  void QRhiDepthStencilClearValue::setDepthClearValue(float d)
    self.uglySide.call(
        'ritual_ZN26QRhiDepthStencilClearValue18setDepthClearValueEf', d,
    )

  @overload(int)
  def setStencilClearValue(self, s: int) -> None:
    """
    Calls Qt's 'void QRhiDepthStencilClearValue::setStencilClearValue(quint32
    s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhidepthstencilclearvalue.html

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  void QRhiDepthStencilClearValue::setStencilClearValue(quint32 s)
    self.uglySide.call(
        'ritual_ZN26QRhiDepthStencilClearValue20setStencilClearValueEj', s,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QRhiDepthStencilClearValue) -> bool:
    """
    Calls Qt's 'bool operator==(const QRhiDepthStencilClearValue &a, const
    QRhiDepthStencilClearValue &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhidepthstencilclearvalue.html#operator==

    Parameters
    ----------

    b : QRhiDepthStencilClearValue
      Passed on as a value: Qt reads the C++ QRhiDepthStencilClearValue,
      which stays Python's own.
    """
    #  bool operator==(const QRhiDepthStencilClearValue &a, const
    #      QRhiDepthStencilClearValue &b)
    return Rituals.call(
        'ritual_ZeqRK26QRhiDepthStencilClearValueS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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
  def __ne__(self, b: QRhiDepthStencilClearValue) -> bool:
    """
    Calls Qt's 'bool operator!=(const QRhiDepthStencilClearValue &a, const
    QRhiDepthStencilClearValue &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhidepthstencilclearvalue.html#operator!=

    Parameters
    ----------

    b : QRhiDepthStencilClearValue
      Passed on as a value: Qt reads the C++ QRhiDepthStencilClearValue,
      which stays Python's own.
    """
    #  bool operator!=(const QRhiDepthStencilClearValue &a, const
    #      QRhiDepthStencilClearValue &b)
    return Rituals.call(
        'ritual_ZneRK26QRhiDepthStencilClearValueS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
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
    'QRhiDepthStencilClearValue::QRhiDepthStencilClearValue()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhidepthstencilclearvalue.html
    """
    #  QRhiDepthStencilClearValue::QRhiDepthStencilClearValue()
    self._noteCreation(QRhiDepthStencilClearValue, lambda: Rituals.call(
        'ritual_ZN26QRhiDepthStencilClearValueC1Ev',
    ))

  @overload(float, int)
  def __init__(self, d: float, s: int) -> None:
    """
    Notes what was given, for Qt's
    'QRhiDepthStencilClearValue::QRhiDepthStencilClearValue(float d, quint32
    s)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhidepthstencilclearvalue.html

    Parameters
    ----------

    d : float
      Passed on as it is.

    s : int
      Passed on as it is.
    """
    #  QRhiDepthStencilClearValue::QRhiDepthStencilClearValue(float d,
    #      quint32 s)
    self._noteCreation(QRhiDepthStencilClearValue, lambda: Rituals.call(
        'ritual_ZN26QRhiDepthStencilClearValueC1Efj', d, s,
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
