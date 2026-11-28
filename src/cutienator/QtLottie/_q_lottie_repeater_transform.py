"""
QLottieRepeaterTransform binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottierepeatertransform_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QLottieRepeaterTransform to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QLottieBase, QLottieBasicTransform

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QJsonObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLottieRepeaterTransform(QLottieBasicTransform):
  """
  The cute side of Qt's QLottieRepeaterTransform: a plain Python object
  standing in front of one C++ QLottieRepeaterTransform.

  It is built on the cute 'QLottieBasicTransform', as Qt's
  QLottieRepeaterTransform is built on Qt's QLottieBasicTransform, and has
  everything that class has.

  C++ hands a QLottieRepeaterTransform around as a copy, so every C++
  QLottieRepeaterTransform behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieRepeaterTransform that has a ritual and that
  Python can call so far, 7 names in all: 'clone', 'parse',
  'updateProperties', 'startOpacity', 'endOpacity', 'setInstanceCount',
  'opacityAtInstance'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottieRepeaterTransform::render(QLottieRenderer &renderer)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QLottieRepeaterTransform::~QLottieRepeaterTransform()': the
    destructor: Python removes its C++ QLottieRepeaterTransform by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QLottieRepeaterTransform is created at the first use, not by
    'QLottieRepeaterTransform(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieRepeaterTransform back gives a copy the ritual
    made for Python, in a new cute QLottieRepeaterTransform.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieRepeaterTransform'

  #  A C++ QLottieRepeaterTransform Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieRepeaterTransform'

  #  Qt's '~QLottieRepeaterTransform()'. Naming it makes this a value class:
  #  Python owns every C++ QLottieRepeaterTransform behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QLottieRepeaterTransformD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieRepeaterTransform::clone() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottierepeatertransform.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieRepeaterTransform::clone() const
    ritual = 'ritual_ZNK24QLottieRepeaterTransform5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QLottieRepeaterTransform5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  def startOpacity(self) -> float:
    """
    Calls Qt's 'qreal QLottieRepeaterTransform::startOpacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottierepeatertransform.html#startOpacity
    """
    #  qreal QLottieRepeaterTransform::startOpacity() const
    return self.uglySide.call(
        'ritual_ZNK24QLottieRepeaterTransform12startOpacityEv',
    )

  def endOpacity(self) -> float:
    """
    Calls Qt's 'qreal QLottieRepeaterTransform::endOpacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottierepeatertransform.html#endOpacity
    """
    #  qreal QLottieRepeaterTransform::endOpacity() const
    return self.uglySide.call(
        'ritual_ZNK24QLottieRepeaterTransform10endOpacityEv',
    )

  @overload(int)
  def opacityAtInstance(self, instance: int) -> float:
    """
    Calls Qt's 'qreal QLottieRepeaterTransform::opacityAtInstance(int
    instance) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottierepeatertransform.html#opacityAtInstance

    Parameters
    ----------

    instance : int
      Passed on as it is.
    """
    #  qreal QLottieRepeaterTransform::opacityAtInstance(int instance) const
    return self.uglySide.call(
        'ritual_ZNK24QLottieRepeaterTransform17opacityAtInstanceEi',
        instance,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setInstanceCount(self, copies: int) -> None:
    """
    Calls Qt's 'void QLottieRepeaterTransform::setInstanceCount(int copies)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottierepeatertransform.html#setInstanceCount

    Parameters
    ----------

    copies : int
      Passed on as it is.
    """
    #  void QLottieRepeaterTransform::setInstanceCount(int copies)
    self.uglySide.call(
        'ritual_ZN24QLottieRepeaterTransform16setInstanceCountEi', copies,
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

  @overload(THIS)
  def __init__(self, other: QLottieRepeaterTransform) -> None:
    """
    Notes what was given, for Qt's
    'QLottieRepeaterTransform::QLottieRepeaterTransform(const
    QLottieRepeaterTransform &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottierepeatertransform.html

    Parameters
    ----------

    other : QLottieRepeaterTransform
      Passed on as a value: Qt reads the C++ QLottieRepeaterTransform, which
      stays Python's own.
    """
    #  QLottieRepeaterTransform::QLottieRepeaterTransform(const
    #      QLottieRepeaterTransform &other)
    self._noteCreation(QLottieRepeaterTransform, lambda: Rituals.call(
        'ritual_ZN24QLottieRepeaterTransformC1ERKS_', self._valueOf(other),
    ))

  @overload()
  @overload(QLottieBase)
  @overload(NoneType)
  def __init__(self, parent: Optional[QLottieBase] = None) -> None:
    """
    Notes what was given, for Qt's
    'QLottieRepeaterTransform::QLottieRepeaterTransform(QLottieBase
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottierepeatertransform.html

    Parameters
    ----------

    parent : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLottieRepeaterTransform::QLottieRepeaterTransform(QLottieBase
    #      *parent)
    self._noteCreation(QLottieRepeaterTransform, lambda: Rituals.call(
        'ritual_ZN24QLottieRepeaterTransformC1EP11QLottieBase',
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
    Calls Qt's 'int QLottieRepeaterTransform::parse(const QJsonObject
    &definition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottierepeatertransform.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottieRepeaterTransform::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN24QLottieRepeaterTransform5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QLottieRepeaterTransform5parseERK11QJsonObject')
    return self.uglySide.call(ritual, self._valueOf(definition))

  @overload(int)
  def updateProperties(self, frame: int) -> None:
    """
    Calls Qt's 'void QLottieRepeaterTransform::updateProperties(int frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottierepeatertransform.html#updateProperties

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieRepeaterTransform::updateProperties(int frame)
    ritual = 'ritual_ZN24QLottieRepeaterTransform16updatePropertiesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QLottieRepeaterTransform16updatePropertiesEi'
    self.uglySide.call(ritual, frame)
