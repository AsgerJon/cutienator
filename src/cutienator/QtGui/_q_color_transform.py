"""
QColorTransform binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qcolortransform.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QColor, QRgba64
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QRgba64 = WAIT['QRgba64']


class QColorTransform(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QColorTransform: a plain Python object standing in
  front of one C++ QColorTransform.

  C++ hands a QColorTransform around as a copy, so every C++ QColorTransform
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QColorTransform that has a ritual and that Python
  can call so far, 5 names in all: 'isIdentity', 'map', '__eq__', '__ne__',
  'compare'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QColorTransform::~QColorTransform()': the destructor: Python
    removes its C++ QColorTransform by it, and has no other use for it.

  What has no ritual
  ------------------

  6 of the 16 functions Qt declares: 6 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QColorTransform is created at the first use, not by
    'QColorTransform(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QColorTransform back gives a copy the ritual made for
    Python, in a new cute QColorTransform.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColorTransform'

  #  Qt's '~QColorTransform()'. Naming it makes this a value class: Python
  #  owns every C++ QColorTransform behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QColorTransformD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isIdentity(self) -> bool:
    """
    Calls Qt's 'bool QColorTransform::isIdentity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortransform.html#isIdentity
    """
    #  bool QColorTransform::isIdentity() const
    return self.uglySide.call('ritual_ZNK15QColorTransform10isIdentityEv')

  @overload(int)
  def map(self, argb: int) -> int:
    """
    Calls Qt's 'QRgb QColorTransform::map(QRgb argb) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortransform.html#map

    Parameters
    ----------

    argb : int
      Passed on as it is.
    """
    #  QRgb QColorTransform::map(QRgb argb) const
    return self.uglySide.call('ritual_ZNK15QColorTransform3mapEj', argb)

  @overload(QRgba64)
  def map(self, rgba64: QRgba64) -> QRgba64:
    """
    Calls Qt's 'QRgba64 QColorTransform::map(QRgba64 rgba64) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortransform.html#map

    Parameters
    ----------

    rgba64 : QRgba64
      Passed on as a value: Qt reads the C++ QRgba64, which stays Python's
      own.

    Returns
    -------

    QRgba64
      A new cute QRgba64 around the copy Qt gave back. Python owns it.
    """
    #  QRgba64 QColorTransform::map(QRgba64 rgba64) const
    address = self.uglySide.call(
        'ritual_ZNK15QColorTransform3mapE7QRgba64', self._valueOf(rgba64),
    )
    from . import QRgba64
    return QRgba64._cuteOwning(address)

  @overload(QColor)
  def map(self, color: QColor) -> QColor:
    """
    Calls Qt's 'QColor QColorTransform::map(const QColor &color) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortransform.html#map

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColorTransform::map(const QColor &color) const
    address = self.uglySide.call(
        'ritual_ZNK15QColorTransform3mapERK6QColor', self._valueOf(color),
    )
    from . import QColor
    return QColor._cuteOwning(address)

  @overload(THIS)
  def compare(self, other: QColorTransform) -> bool:
    """
    Calls Qt's 'bool QColorTransform::compare(const QColorTransform &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortransform.html#compare

    Parameters
    ----------

    other : QColorTransform
      Passed on as a value: Qt reads the C++ QColorTransform, which stays
      Python's own.
    """
    #  bool QColorTransform::compare(const QColorTransform &other) const
    return self.uglySide.call(
        'ritual_ZNK15QColorTransform7compareERKS_', self._valueOf(other),
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
  def __eq__(self, ct2: QColorTransform) -> bool:
    """
    Calls Qt's 'bool operator==(const QColorTransform &ct1, const
    QColorTransform &ct2)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortransform.html#operator==

    Parameters
    ----------

    ct2 : QColorTransform
      Passed on as a value: Qt reads the C++ QColorTransform, which stays
      Python's own.
    """
    #  bool operator==(const QColorTransform &ct1, const QColorTransform
    #      &ct2)
    return Rituals.call(
        'ritual_ZeqRK15QColorTransformS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(ct2),
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
  def __ne__(self, ct2: QColorTransform) -> bool:
    """
    Calls Qt's 'bool operator!=(const QColorTransform &ct1, const
    QColorTransform &ct2)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortransform.html#operator!=

    Parameters
    ----------

    ct2 : QColorTransform
      Passed on as a value: Qt reads the C++ QColorTransform, which stays
      Python's own.
    """
    #  bool operator!=(const QColorTransform &ct1, const QColorTransform
    #      &ct2)
    return Rituals.call(
        'ritual_ZneRK15QColorTransformS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(ct2),
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
    Notes what was given, for Qt's 'QColorTransform::QColorTransform()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransform.html#QColorTransform
    """
    #  QColorTransform::QColorTransform()
    self._noteCreation(QColorTransform, lambda: Rituals.call(
        'ritual_ZN15QColorTransformC1Ev',
    ))

  @overload(THIS)
  def __init__(self, colorTransform: QColorTransform) -> None:
    """
    Notes what was given, for Qt's 'QColorTransform::QColorTransform(const
    QColorTransform &colorTransform)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransform.html#QColorTransform

    Parameters
    ----------

    colorTransform : QColorTransform
      Passed on as a value: Qt reads the C++ QColorTransform, which stays
      Python's own.
    """
    #  QColorTransform::QColorTransform(const QColorTransform
    #      &colorTransform)
    self._noteCreation(QColorTransform, lambda: Rituals.call(
        'ritual_ZN15QColorTransformC1ERKS_', self._valueOf(colorTransform),
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
