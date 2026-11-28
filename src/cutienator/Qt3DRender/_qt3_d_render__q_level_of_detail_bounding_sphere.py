"""
Qt3DRender::QLevelOfDetailBoundingSphere binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qlevelofdetailboundingsphere.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']


class QLevelOfDetailBoundingSphere(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::QLevelOfDetailBoundingSphere: a plain
  Python object standing in front of one C++
  Qt3DRender::QLevelOfDetailBoundingSphere.

  C++ hands a Qt3DRender::QLevelOfDetailBoundingSphere around as a copy, so
  every C++ Qt3DRender::QLevelOfDetailBoundingSphere behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QLevelOfDetailBoundingSphere that has a
  ritual and that Python can call so far, 5 names in all: 'center', 'radius',
  'isEmpty', '__eq__', '__ne__'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'Qt3DRender::QLevelOfDetailBoundingSphere::~QLevelOfDetailBoundingSphere(
    )': the destructor: Python removes its C++
    Qt3DRender::QLevelOfDetailBoundingSphere by it, and has no other use for
    it.
  - Qt's 'QLevelOfDetailBoundingSphere
    &Qt3DRender::QLevelOfDetailBoundingSphere::operator=(const
    QLevelOfDetailBoundingSphere &other)': assignment: Python binds a name
    and has no operator for it.

  What has no ritual
  ------------------

  3 of the 12 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QLevelOfDetailBoundingSphere is created at the first
    use, not by 'Qt3DRender::QLevelOfDetailBoundingSphere(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::QLevelOfDetailBoundingSphere back gives a
    copy the ritual made for Python, in a new cute
    Qt3DRender::QLevelOfDetailBoundingSphere.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QLevelOfDetailBoundingSphere'

  #  Qt's '~Qt3DRender::QLevelOfDetailBoundingSphere()'. Naming it makes this
  #  a value class: Python owns every C++
  #  Qt3DRender::QLevelOfDetailBoundingSphere behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN10Qt3DRender28QLevelOfDetailBoundingSphereD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def center(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::QLevelOfDetailBoundingSphere::center()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetailboundingsphere.html

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::QLevelOfDetailBoundingSphere::center() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender28QLevelOfDetailBoundingSphere6centerEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def radius(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QLevelOfDetailBoundingSphere::radius()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetailboundingsphere.html
    """
    #  float Qt3DRender::QLevelOfDetailBoundingSphere::radius() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender28QLevelOfDetailBoundingSphere6radiusEv',
    )

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QLevelOfDetailBoundingSphere::isEmpty()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetailboundingsphere.html
    """
    #  bool Qt3DRender::QLevelOfDetailBoundingSphere::isEmpty() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender28QLevelOfDetailBoundingSphere7isEmptyEv',
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

  @overload(THIS)
  def __eq__(self, other: QLevelOfDetailBoundingSphere) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::QLevelOfDetailBoundingSphere::operator==(const
    QLevelOfDetailBoundingSphere &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetailboundingsphere.html

    Parameters
    ----------

    other : QLevelOfDetailBoundingSphere
      Passed on as a value: Qt reads the C++
      Qt3DRender::QLevelOfDetailBoundingSphere, which stays Python's own.
    """
    #  bool Qt3DRender::QLevelOfDetailBoundingSphere::operator==(const
    #      QLevelOfDetailBoundingSphere &other) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender28QLevelOfDetailBoundingSphereeqERKS0_',
        self._valueOf(other),
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
  def __ne__(self, other: QLevelOfDetailBoundingSphere) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::QLevelOfDetailBoundingSphere::operator!=(const
    QLevelOfDetailBoundingSphere &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetailboundingsphere.html

    Parameters
    ----------

    other : QLevelOfDetailBoundingSphere
      Passed on as a value: Qt reads the C++
      Qt3DRender::QLevelOfDetailBoundingSphere, which stays Python's own.
    """
    #  bool Qt3DRender::QLevelOfDetailBoundingSphere::operator!=(const
    #      QLevelOfDetailBoundingSphere &other) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender28QLevelOfDetailBoundingSphereneERKS0_',
        self._valueOf(other),
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
  @overload(QVector3D)
  @overload(QVector3D, float)
  def __init__(
      self,
      center: Optional[QVector3D] = None,
      radius: float = 1.0,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QLevelOfDetailBoundingSphere::QLevelOfDetailBoundingSphere(
    QVector3D center, float radius)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetailboundingsphere.html

    Parameters
    ----------

    center : Optional[QVector3D]
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own. May be left out, as in Qt: a new 'QVector3D()' is then passed on.

    radius : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.
    """
    #  Qt3DRender::QLevelOfDetailBoundingSphere::
    #      QLevelOfDetailBoundingSphere(QVector3D center, float radius)
    if center is None:
      from ..QtGui import QVector3D
      center = QVector3D()
    self._noteCreation(QLevelOfDetailBoundingSphere, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender28QLevelOfDetailBoundingSphereC1E9QVector3Df',
        self._valueOf(center), radius,
    ))

  @overload(THIS)
  def __init__(self, other: QLevelOfDetailBoundingSphere) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QLevelOfDetailBoundingSphere::QLevelOfDetailBoundingSphere(
    const QLevelOfDetailBoundingSphere &other)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qlevelofdetailboundingsphere.html

    Parameters
    ----------

    other : QLevelOfDetailBoundingSphere
      Passed on as a value: Qt reads the C++
      Qt3DRender::QLevelOfDetailBoundingSphere, which stays Python's own.
    """
    #  Qt3DRender::QLevelOfDetailBoundingSphere::
    #      QLevelOfDetailBoundingSphere(const QLevelOfDetailBoundingSphere
    #      &other)
    self._noteCreation(QLevelOfDetailBoundingSphere, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender28QLevelOfDetailBoundingSphereC1ERKS0_',
        self._valueOf(other),
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
