"""
DomGradientStop binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomGradientStop to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import DomColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomColor = WAIT['DomColor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DomGradientStop(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomGradientStop: a plain Python object standing in
  front of one C++ DomGradientStop.

  What exists
  -----------

  Every function of Qt's DomGradientStop that has a ritual and that Python
  can call so far, 9 names in all: 'hasAttributePosition',
  'attributePosition', 'setAttributePosition', 'clearAttributePosition',
  'elementColor', 'takeElementColor', 'setElementColor', 'hasElementColor',
  'clearElementColor'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomGradientStop::~DomGradientStop()': the destructor: Python never
    removes a C++ DomGradientStop.
  - Qt's 'void DomGradientStop::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomGradientStop::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomGradientStop is created at the first use, not by
    'DomGradientStop(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomGradientStop.
  - Each name of Qt's DomGradientStop that has no cute function yet, 'read',
    'write', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DomGradientStop'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributePosition(self) -> bool:
    """
    Calls Qt's 'bool DomGradientStop::hasAttributePosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradientstop.html#hasAttributePosition
    """
    #  bool DomGradientStop::hasAttributePosition() const
    return self.uglySide.call(
        'ritual_ZNK15DomGradientStop20hasAttributePositionEv',
    )

  def attributePosition(self) -> float:
    """
    Calls Qt's 'double DomGradientStop::attributePosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradientstop.html#attributePosition
    """
    #  double DomGradientStop::attributePosition() const
    return self.uglySide.call(
        'ritual_ZNK15DomGradientStop17attributePositionEv',
    )

  def elementColor(self) -> Optional[DomColor]:
    """
    Calls Qt's 'DomColor *DomGradientStop::elementColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/domgradientstop.html#elementColor

    Returns
    -------

    Optional[DomColor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomColor *DomGradientStop::elementColor() const
    address = self.uglySide.call(
        'ritual_ZNK15DomGradientStop12elementColorEv',
    )
    from . import DomColor
    return DomColor._cuteAt(address)

  def hasElementColor(self) -> bool:
    """
    Calls Qt's 'bool DomGradientStop::hasElementColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradientstop.html#hasElementColor
    """
    #  bool DomGradientStop::hasElementColor() const
    return self.uglySide.call(
        'ritual_ZNK15DomGradientStop15hasElementColorEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setAttributePosition(self, a: float) -> None:
    """
    Calls Qt's 'void DomGradientStop::setAttributePosition(double a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradientstop.html#setAttributePosition

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void DomGradientStop::setAttributePosition(double a)
    self.uglySide.call(
        'ritual_ZN15DomGradientStop20setAttributePositionEd', a,
    )

  @overload(DomColor)
  @overload(NoneType)
  def setElementColor(self, a: Optional[DomColor]) -> None:
    """
    Calls Qt's 'void DomGradientStop::setElementColor(DomColor *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradientstop.html#setElementColor

    Parameters
    ----------

    a : Optional[DomColor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomGradientStop::setElementColor(DomColor *a)
    self.uglySide.call(
        'ritual_ZN15DomGradientStop15setElementColorEP8DomColor',
        self._addressOf(a),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'DomGradientStop::DomGradientStop()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradientstop.html#DomGradientStop
    """
    #  DomGradientStop::DomGradientStop()
    self._noteCreation(DomGradientStop, lambda: Rituals.call(
        'ritual_ZN15DomGradientStopC1Ev',
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

  def clearAttributePosition(self) -> None:
    """
    Calls Qt's 'void DomGradientStop::clearAttributePosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradientstop.html#clearAttributePosition
    """
    #  void DomGradientStop::clearAttributePosition()
    self.uglySide.call(
        'ritual_ZN15DomGradientStop22clearAttributePositionEv',
    )

  def takeElementColor(self) -> Optional[DomColor]:
    """
    Calls Qt's 'DomColor *DomGradientStop::takeElementColor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradientstop.html#takeElementColor

    Returns
    -------

    Optional[DomColor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomColor *DomGradientStop::takeElementColor()
    address = self.uglySide.call(
        'ritual_ZN15DomGradientStop16takeElementColorEv',
    )
    from . import DomColor
    return DomColor._cuteAt(address)

  def clearElementColor(self) -> None:
    """
    Calls Qt's 'void DomGradientStop::clearElementColor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradientstop.html#clearElementColor
    """
    #  void DomGradientStop::clearElementColor()
    self.uglySide.call('ritual_ZN15DomGradientStop17clearElementColorEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomGradientStop::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomGradientStop.read' has no cute function yet. Qt's 'void "
        "DomGradientStop::read(QXmlStreamReader &reader)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomGradientStop::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomGradientStop.write' has no cute function yet. Qt's 'void "
        "DomGradientStop::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<DomGradientStop *>': the list of DomGradientStop, which
#  'QList[DomGradientStop]' gives. It is made here, so that there is one as
#  soon as there can be a DomGradientStop.
QList.createKind(
    DomGradientStop, 'address',
    make='ritual_list_make_DomGradientStop_ptr',
    add='ritual_list_add_DomGradientStop_ptr',
    size='ritual_list_size_DomGradientStop_ptr',
    at='ritual_list_at_DomGradientStop_ptr',
    drop='ritual_list_drop_DomGradientStop_ptr',
)
