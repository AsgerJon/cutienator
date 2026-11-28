"""
Qt3DRender::QAxisAlignedBoundingBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qaxisalignedboundingbox_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::QAxisAlignedBoundingBox to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtGui import QMatrix4x4, QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QVector3D = WAIT['QVector3D']


class QAxisAlignedBoundingBox(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::QAxisAlignedBoundingBox: a plain Python
  object standing in front of one C++ Qt3DRender::QAxisAlignedBoundingBox.

  C++ hands a Qt3DRender::QAxisAlignedBoundingBox around as a copy, so every
  C++ Qt3DRender::QAxisAlignedBoundingBox behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QAxisAlignedBoundingBox that has a
  ritual and that Python can call so far, 14 names in all: 'clear', 'isNull',
  'center', 'radii', 'minPoint', 'maxPoint', 'xExtent', 'yExtent', 'zExtent',
  'maxExtent', 'minExtent', 'contains', 'expandToContain', 'transformBy'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::QAxisAlignedBoundingBox::QAxisAlignedBoundingBox(const
    std::vector<QVector3D> &points)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void Qt3DRender::QAxisAlignedBoundingBox::update(const
    std::vector<QVector3D> &points)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QAxisAlignedBoundingBox
    &Qt3DRender::QAxisAlignedBoundingBox::transform(const QMatrix4x4 &mat)':
    gives a type Python has no way to take yet.
  - Qt's 'Qt3DRender::QAxisAlignedBoundingBox::~QAxisAlignedBoundingBox()':
    the destructor: Python removes its C++
    Qt3DRender::QAxisAlignedBoundingBox by it, and has no other use for it.

  What to expect
  --------------

  - The C++ Qt3DRender::QAxisAlignedBoundingBox is created at the first use,
    not by 'Qt3DRender::QAxisAlignedBoundingBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::QAxisAlignedBoundingBox back gives a copy
    the ritual made for Python, in a new cute
    Qt3DRender::QAxisAlignedBoundingBox.
  - Each name of Qt's Qt3DRender::QAxisAlignedBoundingBox that has no cute
    function yet, 'transform', 'update', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QAxisAlignedBoundingBox'

  #  Qt's '~Qt3DRender::QAxisAlignedBoundingBox()'. Naming it makes this a
  #  value class: Python owns every C++ Qt3DRender::QAxisAlignedBoundingBox
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender23QAxisAlignedBoundingBoxD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QAxisAlignedBoundingBox::isNull() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qaxisalignedboundingbox.html#isNull
    """
    #  bool Qt3DRender::QAxisAlignedBoundingBox::isNull() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox6isNullEv',
    )

  def center(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::QAxisAlignedBoundingBox::center()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qaxisalignedboundingbox.html#center

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::QAxisAlignedBoundingBox::center() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox6centerEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def radii(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::QAxisAlignedBoundingBox::radii()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qaxisalignedboundingbox.html#radii

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::QAxisAlignedBoundingBox::radii() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox5radiiEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def minPoint(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::QAxisAlignedBoundingBox::minPoint()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qaxisalignedboundingbox.html#minPoint

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::QAxisAlignedBoundingBox::minPoint() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox8minPointEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def maxPoint(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::QAxisAlignedBoundingBox::maxPoint()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qaxisalignedboundingbox.html#maxPoint

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::QAxisAlignedBoundingBox::maxPoint() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox8maxPointEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def xExtent(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QAxisAlignedBoundingBox::xExtent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qaxisalignedboundingbox.html#xExtent
    """
    #  float Qt3DRender::QAxisAlignedBoundingBox::xExtent() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox7xExtentEv',
    )

  def yExtent(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QAxisAlignedBoundingBox::yExtent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qaxisalignedboundingbox.html#yExtent
    """
    #  float Qt3DRender::QAxisAlignedBoundingBox::yExtent() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox7yExtentEv',
    )

  def zExtent(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QAxisAlignedBoundingBox::zExtent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qaxisalignedboundingbox.html#zExtent
    """
    #  float Qt3DRender::QAxisAlignedBoundingBox::zExtent() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox7zExtentEv',
    )

  def maxExtent(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QAxisAlignedBoundingBox::maxExtent()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qaxisalignedboundingbox.html#maxExtent
    """
    #  float Qt3DRender::QAxisAlignedBoundingBox::maxExtent() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox9maxExtentEv',
    )

  def minExtent(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QAxisAlignedBoundingBox::minExtent()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qaxisalignedboundingbox.html#minExtent
    """
    #  float Qt3DRender::QAxisAlignedBoundingBox::minExtent() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox9minExtentEv',
    )

  @overload(QVector3D)
  def contains(self, pt: QVector3D) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QAxisAlignedBoundingBox::contains(const
    QVector3D &pt) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qaxisalignedboundingbox.html#contains

    Parameters
    ----------

    pt : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  bool Qt3DRender::QAxisAlignedBoundingBox::contains(const QVector3D
    #      &pt) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox8containsERK9QVecto'
        'r3D',
        self._valueOf(pt),
    )

  @overload(QMatrix4x4)
  def transformBy(self, mat: QMatrix4x4) -> QAxisAlignedBoundingBox:
    """
    Calls Qt's 'QAxisAlignedBoundingBox
    Qt3DRender::QAxisAlignedBoundingBox::transformBy(const QMatrix4x4 &mat)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qaxisalignedboundingbox.html

    Parameters
    ----------

    mat : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    Returns
    -------

    QAxisAlignedBoundingBox
      A new cute Qt3DRender::QAxisAlignedBoundingBox around the copy Qt gave
      back. Python owns it.
    """
    #  QAxisAlignedBoundingBox
    #      Qt3DRender::QAxisAlignedBoundingBox::transformBy(const QMatrix4x4
    #      &mat) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender23QAxisAlignedBoundingBox11transformByERK10Q'
        'Matrix4x4',
        self._valueOf(mat),
    )
    return QAxisAlignedBoundingBox._cuteOwning(address)

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
    'Qt3DRender::QAxisAlignedBoundingBox::QAxisAlignedBoundingBox()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qaxisalignedboundingbox.html
    """
    #  Qt3DRender::QAxisAlignedBoundingBox::QAxisAlignedBoundingBox()
    self._noteCreation(QAxisAlignedBoundingBox, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender23QAxisAlignedBoundingBoxC1Ev',
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

  def clear(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAxisAlignedBoundingBox::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qaxisalignedboundingbox.html#clear
    """
    #  void Qt3DRender::QAxisAlignedBoundingBox::clear()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender23QAxisAlignedBoundingBox5clearEv',
    )

  @overload(QVector3D)
  def expandToContain(self, pt: QVector3D) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QAxisAlignedBoundingBox::expandToContain(const QVector3D
    &pt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qaxisalignedboundingbox.html

    Parameters
    ----------

    pt : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::QAxisAlignedBoundingBox::expandToContain(const
    #      QVector3D &pt)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender23QAxisAlignedBoundingBox15expandToContainERK'
        '9QVector3D',
        self._valueOf(pt),
    )

  @overload(THIS)
  def expandToContain(self, other: QAxisAlignedBoundingBox) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QAxisAlignedBoundingBox::expandToContain(const
    QAxisAlignedBoundingBox &other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qaxisalignedboundingbox.html

    Parameters
    ----------

    other : QAxisAlignedBoundingBox
      Passed on as a value: Qt reads the C++
      Qt3DRender::QAxisAlignedBoundingBox, which stays Python's own.
    """
    #  void Qt3DRender::QAxisAlignedBoundingBox::expandToContain(const
    #      QAxisAlignedBoundingBox &other)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender23QAxisAlignedBoundingBox15expandToContainERK'
        'S0_',
        self._valueOf(other),
    )

  @staticmethod
  def transform(*__, **_) -> Never:
    """
    Qt's 'QAxisAlignedBoundingBox
    &Qt3DRender::QAxisAlignedBoundingBox::transform(const QMatrix4x4 &mat)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QAxisAlignedBoundingBox.transform' has no cute "
        "function yet. Qt's 'QAxisAlignedBoundingBox "
        "&Qt3DRender::QAxisAlignedBoundingBox::transform(const QMatrix4x4 "
        "&mat)': gives a type Python has no way to take yet.")

  @staticmethod
  def update(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::QAxisAlignedBoundingBox::update(const
    std::vector<QVector3D> &points)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QAxisAlignedBoundingBox.update' has no cute function "
        "yet. Qt's 'void Qt3DRender::QAxisAlignedBoundingBox::update(const "
        "std::vector<QVector3D> &points)': takes a type Python has no way "
        "to hand over yet.")
