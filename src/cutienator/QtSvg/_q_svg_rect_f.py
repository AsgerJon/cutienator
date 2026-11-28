"""
QSvgRectF binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvghelper_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgRectF to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QRectF
from . import QtSvg

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QDebug, QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QSvgRectF(QRectF):
  """
  The cute side of Qt's QSvgRectF: a plain Python object standing in front of
  one C++ QSvgRectF.

  It is built on the cute 'QRectF', as Qt's QSvgRectF is built on Qt's
  QRectF, and has everything that class has.

  C++ hands a QSvgRectF around as a copy, so every C++ QSvgRectF behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSvgRectF that has a ritual and that Python can call
  so far, 11 names in all: 'translationRelativeToBoundingBox',
  'resolveRelativeLengths', 'unitX', 'unitY', 'unitW', 'unitH', 'setUnitX',
  'setUnitY', 'setUnitW', 'setUnitH', '__rlshift__'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgRectF::~QSvgRectF()': the destructor: Python removes its C++
    QSvgRectF by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSvgRectF is created at the first use, not by 'QSvgRectF(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSvgRectF back gives a copy the ritual made for
    Python, in a new cute QSvgRectF.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgRectF'

  #  Qt's '~QSvgRectF()'. Naming it makes this a value class: Python owns
  #  every C++ QSvgRectF behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QSvgRectFD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def translationRelativeToBoundingBox(self, boundingBox: QRectF) -> QPointF:
    """
    Calls Qt's 'QPointF QSvgRectF::translationRelativeToBoundingBox(const
    QRectF &boundingBox) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgrectf.html#translationRelativeToBoundingBox

    Parameters
    ----------

    boundingBox : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QSvgRectF::translationRelativeToBoundingBox(const QRectF
    #      &boundingBox) const
    address = self.uglySide.call(
        'ritual_ZNK9QSvgRectF32translationRelativeToBoundingBoxERK6QRectF',
        self._valueOf(boundingBox),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QRectF)
  def resolveRelativeLengths(self, localRect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QSvgRectF::resolveRelativeLengths(const QRectF
    &localRect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgrectf.html#resolveRelativeLengths

    Parameters
    ----------

    localRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSvgRectF::resolveRelativeLengths(const QRectF &localRect)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9QSvgRectF22resolveRelativeLengthsERK6QRectF',
        self._valueOf(localRect),
    )
    return QRectF._cuteOwning(address)

  @overload(QRectF, QtSvg.UnitTypes)
  def resolveRelativeLengths(
      self,
      localRect: QRectF,
      units: QtSvg.UnitTypes,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QSvgRectF::resolveRelativeLengths(const QRectF
    &localRect, QtSvg::UnitTypes units) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgrectf.html#resolveRelativeLengths

    Parameters
    ----------

    localRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    units : QtSvg.UnitTypes
      Passed on as its number.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSvgRectF::resolveRelativeLengths(const QRectF &localRect,
    #      QtSvg::UnitTypes units) const
    address = self.uglySide.call(
        'ritual_ZNK9QSvgRectF22resolveRelativeLengthsERK6QRectFN5QtSvg9Unit'
        'TypesE',
        self._valueOf(localRect), units.value,
    )
    return QRectF._cuteOwning(address)

  def unitX(self) -> QtSvg.UnitTypes:
    """
    Calls Qt's 'QtSvg::UnitTypes QSvgRectF::unitX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrectf.html#unitX

    Returns
    -------

    QtSvg.UnitTypes
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QtSvg.UnitTypes(number)'
      gives.
    """
    #  QtSvg::UnitTypes QSvgRectF::unitX() const
    return QtSvg.UnitTypes(self.uglySide.call(
        'ritual_ZNK9QSvgRectF5unitXEv',
    ))

  def unitY(self) -> QtSvg.UnitTypes:
    """
    Calls Qt's 'QtSvg::UnitTypes QSvgRectF::unitY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrectf.html#unitY

    Returns
    -------

    QtSvg.UnitTypes
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QtSvg.UnitTypes(number)'
      gives.
    """
    #  QtSvg::UnitTypes QSvgRectF::unitY() const
    return QtSvg.UnitTypes(self.uglySide.call(
        'ritual_ZNK9QSvgRectF5unitYEv',
    ))

  def unitW(self) -> QtSvg.UnitTypes:
    """
    Calls Qt's 'QtSvg::UnitTypes QSvgRectF::unitW() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrectf.html#unitW

    Returns
    -------

    QtSvg.UnitTypes
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QtSvg.UnitTypes(number)'
      gives.
    """
    #  QtSvg::UnitTypes QSvgRectF::unitW() const
    return QtSvg.UnitTypes(self.uglySide.call(
        'ritual_ZNK9QSvgRectF5unitWEv',
    ))

  def unitH(self) -> QtSvg.UnitTypes:
    """
    Calls Qt's 'QtSvg::UnitTypes QSvgRectF::unitH() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrectf.html#unitH

    Returns
    -------

    QtSvg.UnitTypes
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QtSvg.UnitTypes(number)'
      gives.
    """
    #  QtSvg::UnitTypes QSvgRectF::unitH() const
    return QtSvg.UnitTypes(self.uglySide.call(
        'ritual_ZNK9QSvgRectF5unitHEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QtSvg.UnitTypes)
  def setUnitX(self, unit: QtSvg.UnitTypes) -> None:
    """
    Calls Qt's 'void QSvgRectF::setUnitX(QtSvg::UnitTypes unit)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrectf.html#setUnitX

    Parameters
    ----------

    unit : QtSvg.UnitTypes
      Passed on as its number.
    """
    #  void QSvgRectF::setUnitX(QtSvg::UnitTypes unit)
    self.uglySide.call(
        'ritual_ZN9QSvgRectF8setUnitXEN5QtSvg9UnitTypesE', unit.value,
    )

  @overload(QtSvg.UnitTypes)
  def setUnitY(self, unit: QtSvg.UnitTypes) -> None:
    """
    Calls Qt's 'void QSvgRectF::setUnitY(QtSvg::UnitTypes unit)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrectf.html#setUnitY

    Parameters
    ----------

    unit : QtSvg.UnitTypes
      Passed on as its number.
    """
    #  void QSvgRectF::setUnitY(QtSvg::UnitTypes unit)
    self.uglySide.call(
        'ritual_ZN9QSvgRectF8setUnitYEN5QtSvg9UnitTypesE', unit.value,
    )

  @overload(QtSvg.UnitTypes)
  def setUnitW(self, unit: QtSvg.UnitTypes) -> None:
    """
    Calls Qt's 'void QSvgRectF::setUnitW(QtSvg::UnitTypes unit)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrectf.html#setUnitW

    Parameters
    ----------

    unit : QtSvg.UnitTypes
      Passed on as its number.
    """
    #  void QSvgRectF::setUnitW(QtSvg::UnitTypes unit)
    self.uglySide.call(
        'ritual_ZN9QSvgRectF8setUnitWEN5QtSvg9UnitTypesE', unit.value,
    )

  @overload(QtSvg.UnitTypes)
  def setUnitH(self, unit: QtSvg.UnitTypes) -> None:
    """
    Calls Qt's 'void QSvgRectF::setUnitH(QtSvg::UnitTypes unit)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrectf.html#setUnitH

    Parameters
    ----------

    unit : QtSvg.UnitTypes
      Passed on as its number.
    """
    #  void QSvgRectF::setUnitH(QtSvg::UnitTypes unit)
    self.uglySide.call(
        'ritual_ZN9QSvgRectF8setUnitHEN5QtSvg9UnitTypesE', unit.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDebug)
  def __rlshift__(self, debug: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug debug, const QSvgRectF &r)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrectf.html#operator<<

    Parameters
    ----------

    debug : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug debug, const QSvgRectF &r)
    address = Rituals.call(
        'ritual_Zls6QDebugRK9QSvgRectF',
        CuteMixin._valueOf(debug), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
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
  @overload(QRectF)
  @overload(QRectF, QtSvg.UnitTypes)
  @overload(QRectF, QtSvg.UnitTypes, QtSvg.UnitTypes)
  @overload(QRectF, QtSvg.UnitTypes, QtSvg.UnitTypes, QtSvg.UnitTypes)
  @overload(
      QRectF, QtSvg.UnitTypes, QtSvg.UnitTypes, QtSvg.UnitTypes,
      QtSvg.UnitTypes,
  )
  def __init__(
      self,
      r: Optional[QRectF] = None,
      unitX: QtSvg.UnitTypes = QtSvg.UnitTypes.userSpaceOnUse,
      unitY: QtSvg.UnitTypes = QtSvg.UnitTypes.userSpaceOnUse,
      unitW: QtSvg.UnitTypes = QtSvg.UnitTypes.userSpaceOnUse,
      unitH: QtSvg.UnitTypes = QtSvg.UnitTypes.userSpaceOnUse,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSvgRectF::QSvgRectF(const QRectF &r,
    QtSvg::UnitTypes unitX, QtSvg::UnitTypes unitY, QtSvg::UnitTypes unitW,
    QtSvg::UnitTypes unitH)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgrectf.html#QSvgRectF

    Parameters
    ----------

    r : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.

    unitX : QtSvg.UnitTypes
      Passed on as its number. May be left out, as in Qt: it is then
      QtSvg.UnitTypes.userSpaceOnUse.

    unitY : QtSvg.UnitTypes
      Passed on as its number. May be left out, as in Qt: it is then
      QtSvg.UnitTypes.userSpaceOnUse.

    unitW : QtSvg.UnitTypes
      Passed on as its number. May be left out, as in Qt: it is then
      QtSvg.UnitTypes.userSpaceOnUse.

    unitH : QtSvg.UnitTypes
      Passed on as its number. May be left out, as in Qt: it is then
      QtSvg.UnitTypes.userSpaceOnUse.
    """
    #  QSvgRectF::QSvgRectF(const QRectF &r, QtSvg::UnitTypes unitX,
    #      QtSvg::UnitTypes unitY, QtSvg::UnitTypes unitW, QtSvg::UnitTypes
    #      unitH)
    if r is None:
      r = QRectF()
    self._noteCreation(QSvgRectF, lambda: Rituals.call(
        'ritual_ZN9QSvgRectFC1ERK6QRectFN5QtSvg9UnitTypesES4_S4_S4_',
        self._valueOf(r), unitX.value, unitY.value, unitW.value, unitH.value,
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
