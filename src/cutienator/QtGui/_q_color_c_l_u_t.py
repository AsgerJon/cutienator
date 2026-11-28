"""
QColorCLUT binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qcolorclut_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QColorCLUT to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QColorVector
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColorVector = WAIT['QColorVector']


class QColorCLUT(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QColorCLUT: a plain Python object standing in front
  of one C++ QColorCLUT.

  C++ hands a QColorCLUT around as a copy, so every C++ QColorCLUT behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QColorCLUT that has a ritual and that Python can
  call so far, 3 names in all: 'interpolate', 'isEmpty', 'apply'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QColorCLUT::interpolateIn(QColorVector &a, const QColorVector
    &b, float t)': takes a type Python has no way to hand over yet.
  - Qt's 'QColorCLUT::~QColorCLUT()': the destructor: Python removes its C++
    QColorCLUT by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QColorCLUT is created at the first use, not by 'QColorCLUT(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QColorCLUT back gives a copy the ritual made for
    Python, in a new cute QColorCLUT.
  - Each name of Qt's QColorCLUT that has no cute function yet,
    'interpolateIn', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QColorVector, QColorVector, float)
  def interpolate(
      a: QColorVector,
      b: QColorVector,
      t: float,
  ) -> QColorVector:
    """
    Calls Qt's 'QColorVector QColorCLUT::interpolate(const QColorVector &a,
    const QColorVector &b, float t)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorclut.html#interpolate

    Parameters
    ----------

    a : QColorVector
      Passed on as a value: Qt reads the C++ QColorVector, which stays
      Python's own.

    b : QColorVector
      Passed on as a value: Qt reads the C++ QColorVector, which stays
      Python's own.

    t : float
      Passed on as it is.

    Returns
    -------

    QColorVector
      A new cute QColorVector around the copy Qt gave back. Python owns it.
    """
    #  QColorVector QColorCLUT::interpolate(const QColorVector &a, const
    #      QColorVector &b, float t)
    address = Rituals.call(
        'ritual_ZN10QColorCLUT11interpolateERK12QColorVectorS2_f',
        CuteMixin._valueOf(a), CuteMixin._valueOf(b), t,
    )
    from . import QColorVector
    return QColorVector._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColorCLUT'

  #  Qt's '~QColorCLUT()'. Naming it makes this a value class: Python owns
  #  every C++ QColorCLUT behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QColorCLUTD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QColorCLUT::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorclut.html#isEmpty
    """
    #  bool QColorCLUT::isEmpty() const
    return self.uglySide.call('ritual_ZNK10QColorCLUT7isEmptyEv')

  @overload(QColorVector)
  def apply(self, v: QColorVector) -> QColorVector:
    """
    Calls Qt's 'QColorVector QColorCLUT::apply(const QColorVector &v) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorclut.html#apply

    Parameters
    ----------

    v : QColorVector
      Passed on as a value: Qt reads the C++ QColorVector, which stays
      Python's own.

    Returns
    -------

    QColorVector
      A new cute QColorVector around the copy Qt gave back. Python owns it.
    """
    #  QColorVector QColorCLUT::apply(const QColorVector &v) const
    address = self.uglySide.call(
        'ritual_ZNK10QColorCLUT5applyERK12QColorVector', self._valueOf(v),
    )
    from . import QColorVector
    return QColorVector._cuteOwning(address)

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

  @staticmethod
  def interpolateIn(*__, **_) -> Never:
    """
    Qt's 'void QColorCLUT::interpolateIn(QColorVector &a, const QColorVector
    &b, float t)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QColorCLUT.interpolateIn' has no cute function yet. Qt's 'void "
        "QColorCLUT::interpolateIn(QColorVector &a, const QColorVector &b, "
        "float t)': takes a type Python has no way to hand over yet.")
