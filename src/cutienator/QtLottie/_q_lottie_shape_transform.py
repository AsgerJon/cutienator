"""
QLottieShapeTransform binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottieshapetransform_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QLottieShapeTransform to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QLottieBase, QLottieBasicTransform

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QJsonObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLottieShapeTransform(QLottieBasicTransform):
  """
  The cute side of Qt's QLottieShapeTransform: a plain Python object standing
  in front of one C++ QLottieShapeTransform.

  It is built on the cute 'QLottieBasicTransform', as Qt's
  QLottieShapeTransform is built on Qt's QLottieBasicTransform, and has
  everything that class has.

  C++ hands a QLottieShapeTransform around as a copy, so every C++
  QLottieShapeTransform behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieShapeTransform that has a ritual and that
  Python can call so far, 8 names in all: 'clone', 'parse',
  'updateProperties', 'skew', 'skewAxis', 'shearX', 'shearY', 'shearAngle'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottieShapeTransform::render(QLottieRenderer &renderer)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QLottieProperty<qreal> QLottieShapeTransform::skewProperty()
    const': gives a type Python has no way to take yet.
  - Qt's 'QLottieProperty<qreal> QLottieShapeTransform::skewAxisProperty()
    const': gives a type Python has no way to take yet.
  - Qt's 'QLottieShapeTransform::~QLottieShapeTransform()': the destructor:
    Python removes its C++ QLottieShapeTransform by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QLottieShapeTransform is created at the first use, not by
    'QLottieShapeTransform(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieShapeTransform back gives a copy the ritual
    made for Python, in a new cute QLottieShapeTransform.
  - Each name of Qt's QLottieShapeTransform that has no cute function yet,
    'skewAxisProperty', 'skewProperty', holds a function that raises
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
  __qt_class__ = 'QLottieShapeTransform'

  #  A C++ QLottieShapeTransform Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieShapeTransform'

  #  Qt's '~QLottieShapeTransform()'. Naming it makes this a value class:
  #  Python owns every C++ QLottieShapeTransform behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QLottieShapeTransformD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieShapeTransform::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieshapetransform.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieShapeTransform::clone() const
    ritual = 'ritual_ZNK21QLottieShapeTransform5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QLottieShapeTransform5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  def skew(self) -> float:
    """
    Calls Qt's 'qreal QLottieShapeTransform::skew() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieshapetransform.html#skew
    """
    #  qreal QLottieShapeTransform::skew() const
    return self.uglySide.call('ritual_ZNK21QLottieShapeTransform4skewEv')

  def skewAxis(self) -> float:
    """
    Calls Qt's 'qreal QLottieShapeTransform::skewAxis() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieshapetransform.html#skewAxis
    """
    #  qreal QLottieShapeTransform::skewAxis() const
    return self.uglySide.call('ritual_ZNK21QLottieShapeTransform8skewAxisEv')

  def shearX(self) -> float:
    """
    Calls Qt's 'qreal QLottieShapeTransform::shearX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieshapetransform.html#shearX
    """
    #  qreal QLottieShapeTransform::shearX() const
    return self.uglySide.call('ritual_ZNK21QLottieShapeTransform6shearXEv')

  def shearY(self) -> float:
    """
    Calls Qt's 'qreal QLottieShapeTransform::shearY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieshapetransform.html#shearY
    """
    #  qreal QLottieShapeTransform::shearY() const
    return self.uglySide.call('ritual_ZNK21QLottieShapeTransform6shearYEv')

  def shearAngle(self) -> float:
    """
    Calls Qt's 'qreal QLottieShapeTransform::shearAngle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieshapetransform.html#shearAngle
    """
    #  qreal QLottieShapeTransform::shearAngle() const
    return self.uglySide.call(
        'ritual_ZNK21QLottieShapeTransform10shearAngleEv',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __init__(self, other: QLottieShapeTransform) -> None:
    """
    Notes what was given, for Qt's
    'QLottieShapeTransform::QLottieShapeTransform(const QLottieShapeTransform
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieshapetransform.html#QLottieShapeTransform

    Parameters
    ----------

    other : QLottieShapeTransform
      Passed on as a value: Qt reads the C++ QLottieShapeTransform, which
      stays Python's own.
    """
    #  QLottieShapeTransform::QLottieShapeTransform(const
    #      QLottieShapeTransform &other)
    self._noteCreation(QLottieShapeTransform, lambda: Rituals.call(
        'ritual_ZN21QLottieShapeTransformC1ERKS_', self._valueOf(other),
    ))

  @overload()
  @overload(QLottieBase)
  @overload(NoneType)
  def __init__(self, parent: Optional[QLottieBase] = None) -> None:
    """
    Notes what was given, for Qt's
    'QLottieShapeTransform::QLottieShapeTransform(QLottieBase *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieshapetransform.html#QLottieShapeTransform

    Parameters
    ----------

    parent : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLottieShapeTransform::QLottieShapeTransform(QLottieBase *parent)
    self._noteCreation(QLottieShapeTransform, lambda: Rituals.call(
        'ritual_ZN21QLottieShapeTransformC1EP11QLottieBase',
        self._addressOf(parent),
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

  @overload(QJsonObject)
  def parse(self, definition: QJsonObject) -> int:
    """
    Calls Qt's 'int QLottieShapeTransform::parse(const QJsonObject
    &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieshapetransform.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottieShapeTransform::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN21QLottieShapeTransform5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QLottieShapeTransform5parseERK11QJsonObject'
    return self.uglySide.call(ritual, self._valueOf(definition))

  @overload(int)
  def updateProperties(self, frame: int) -> None:
    """
    Calls Qt's 'void QLottieShapeTransform::updateProperties(int frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieshapetransform.html#updateProperties

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieShapeTransform::updateProperties(int frame)
    ritual = 'ritual_ZN21QLottieShapeTransform16updatePropertiesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QLottieShapeTransform16updatePropertiesEi'
    self.uglySide.call(ritual, frame)

  @staticmethod
  def skewAxisProperty(*__, **_) -> Never:
    """
    Qt's 'QLottieProperty<qreal> QLottieShapeTransform::skewAxisProperty()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLottieShapeTransform.skewAxisProperty' has no cute function yet. "
        "Qt's 'QLottieProperty<qreal> "
        "QLottieShapeTransform::skewAxisProperty() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def skewProperty(*__, **_) -> Never:
    """
    Qt's 'QLottieProperty<qreal> QLottieShapeTransform::skewProperty()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLottieShapeTransform.skewProperty' has no cute function yet. "
        "Qt's 'QLottieProperty<qreal> QLottieShapeTransform::skewProperty() "
        "const': gives a type Python has no way to take yet.")
