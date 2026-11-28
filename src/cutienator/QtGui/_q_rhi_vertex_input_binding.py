"""
QRhiVertexInputBinding binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class QRhiVertexInputBinding(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhiVertexInputBinding: a plain Python object
  standing in front of one C++ QRhiVertexInputBinding.

  C++ hands a QRhiVertexInputBinding around as a copy, so every C++
  QRhiVertexInputBinding behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRhiVertexInputBinding that has a ritual and that
  Python can call so far, 8 names in all: 'stride', 'setStride',
  'classification', 'setClassification', 'instanceStepRate',
  'setInstanceStepRate', '__eq__', '__ne__'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhiVertexInputBinding::~QRhiVertexInputBinding()': the destructor:
    Python removes its C++ QRhiVertexInputBinding by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QRhiVertexInputBinding is created at the first use, not by
    'QRhiVertexInputBinding(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiVertexInputBinding back gives a copy the ritual
    made for Python, in a new cute QRhiVertexInputBinding.
  """

  #  The enums Qt writes inside QRhiVertexInputBinding, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Classification(CuteNum):
    """
    The enum 'QRhiVertexInputBinding::Classification' of Qt, with the 2 names
    Qt gives in it.
    """

    PerVertex = Kee[int](0)
    PerInstance = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiVertexInputBinding'

  #  Qt's '~QRhiVertexInputBinding()'. Naming it makes this a value class:
  #  Python owns every C++ QRhiVertexInputBinding behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QRhiVertexInputBindingD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def stride(self) -> int:
    """
    Calls Qt's 'quint32 QRhiVertexInputBinding::stride() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhivertexinputbinding.html#stride
    """
    #  quint32 QRhiVertexInputBinding::stride() const
    return self.uglySide.call('ritual_ZNK22QRhiVertexInputBinding6strideEv')

  def classification(self) -> Classification:
    """
    Calls Qt's 'Classification QRhiVertexInputBinding::classification()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputbinding.html#classification

    Returns
    -------

    Classification
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Classification(number)'
      gives.
    """
    #  Classification QRhiVertexInputBinding::classification() const
    return QRhiVertexInputBinding.Classification(self.uglySide.call(
        'ritual_ZNK22QRhiVertexInputBinding14classificationEv',
    ))

  def instanceStepRate(self) -> int:
    """
    Calls Qt's 'quint32 QRhiVertexInputBinding::instanceStepRate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputbinding.html#instanceStepRate
    """
    #  quint32 QRhiVertexInputBinding::instanceStepRate() const
    return self.uglySide.call(
        'ritual_ZNK22QRhiVertexInputBinding16instanceStepRateEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setStride(self, s: int) -> None:
    """
    Calls Qt's 'void QRhiVertexInputBinding::setStride(quint32 s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputbinding.html#setStride

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  void QRhiVertexInputBinding::setStride(quint32 s)
    self.uglySide.call('ritual_ZN22QRhiVertexInputBinding9setStrideEj', s)

  @overload(Classification)
  def setClassification(self, c: Classification) -> None:
    """
    Calls Qt's 'void QRhiVertexInputBinding::setClassification(Classification
    c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputbinding.html#setClassification

    Parameters
    ----------

    c : Classification
      Passed on as its number.
    """
    #  void QRhiVertexInputBinding::setClassification(Classification c)
    self.uglySide.call(
        'ritual_ZN22QRhiVertexInputBinding17setClassificationENS_14Classifi'
        'cationE',
        c.value,
    )

  @overload(int)
  def setInstanceStepRate(self, rate: int) -> None:
    """
    Calls Qt's 'void QRhiVertexInputBinding::setInstanceStepRate(quint32
    rate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputbinding.html#setInstanceStepRate

    Parameters
    ----------

    rate : int
      Passed on as it is.
    """
    #  void QRhiVertexInputBinding::setInstanceStepRate(quint32 rate)
    self.uglySide.call(
        'ritual_ZN22QRhiVertexInputBinding19setInstanceStepRateEj', rate,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QRhiVertexInputBinding) -> bool:
    """
    Calls Qt's 'bool operator==(const QRhiVertexInputBinding &a, const
    QRhiVertexInputBinding &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputbinding.html#operator==

    Parameters
    ----------

    b : QRhiVertexInputBinding
      Passed on as a value: Qt reads the C++ QRhiVertexInputBinding, which
      stays Python's own.
    """
    #  bool operator==(const QRhiVertexInputBinding &a, const
    #      QRhiVertexInputBinding &b)
    return Rituals.call(
        'ritual_ZeqRK22QRhiVertexInputBindingS1_',
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
  def __ne__(self, b: QRhiVertexInputBinding) -> bool:
    """
    Calls Qt's 'bool operator!=(const QRhiVertexInputBinding &a, const
    QRhiVertexInputBinding &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputbinding.html#operator!=

    Parameters
    ----------

    b : QRhiVertexInputBinding
      Passed on as a value: Qt reads the C++ QRhiVertexInputBinding, which
      stays Python's own.
    """
    #  bool operator!=(const QRhiVertexInputBinding &a, const
    #      QRhiVertexInputBinding &b)
    return Rituals.call(
        'ritual_ZneRK22QRhiVertexInputBindingS1_',
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
    'QRhiVertexInputBinding::QRhiVertexInputBinding()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputbinding.html#QRhiVertexInputBinding
    """
    #  QRhiVertexInputBinding::QRhiVertexInputBinding()
    self._noteCreation(QRhiVertexInputBinding, lambda: Rituals.call(
        'ritual_ZN22QRhiVertexInputBindingC1Ev',
    ))

  @overload(int)
  @overload(int, Classification)
  @overload(int, Classification, int)
  def __init__(
      self,
      stride: int,
      cls: Classification = Classification.PerVertex,
      stepRate: int = 1,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QRhiVertexInputBinding::QRhiVertexInputBinding(quint32 stride,
    Classification cls, quint32 stepRate)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputbinding.html#QRhiVertexInputBinding

    Parameters
    ----------

    stride : int
      Passed on as it is.

    cls : Classification
      Passed on as its number. May be left out, as in Qt: it is then
      Classification.PerVertex.

    stepRate : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  QRhiVertexInputBinding::QRhiVertexInputBinding(quint32 stride,
    #      Classification cls, quint32 stepRate)
    self._noteCreation(QRhiVertexInputBinding, lambda: Rituals.call(
        'ritual_ZN22QRhiVertexInputBindingC1EjNS_14ClassificationEj',
        stride, cls.value, stepRate,
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
