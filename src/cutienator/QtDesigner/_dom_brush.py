"""
DomBrush binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomBrush to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import DomColor, DomGradient, DomProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomColor = WAIT['DomColor']
  DomGradient = WAIT['DomGradient']
  DomProperty = WAIT['DomProperty']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DomBrush(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomBrush: a plain Python object standing in front of
  one C++ DomBrush.

  What exists
  -----------

  Every function of Qt's DomBrush that has a ritual and that Python can call
  so far, 15 names in all: 'hasAttributeBrushStyle', 'attributeBrushStyle',
  'setAttributeBrushStyle', 'clearAttributeBrushStyle', 'kind',
  'elementColor', 'takeElementColor', 'setElementColor', 'elementTexture',
  'takeElementTexture', 'setElementTexture', 'elementGradient',
  'takeElementGradient', 'setElementGradient', 'clear'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomBrush::~DomBrush()': the destructor: Python never removes a C++
    DomBrush.
  - Qt's 'void DomBrush::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void DomBrush::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 23 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomBrush is created at the first use, not by 'DomBrush(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomBrush.
  - Each name of Qt's DomBrush that has no cute function yet, 'read',
    'write', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside DomBrush, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class Kind(CuteNum):
    """The enum 'DomBrush::Kind' of Qt, with the 4 names Qt gives in it."""

    Unknown = Kee[int](0)
    Color = Kee[int](1)
    Texture = Kee[int](2)
    Gradient = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DomBrush'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeBrushStyle(self) -> bool:
    """
    Calls Qt's 'bool DomBrush::hasAttributeBrushStyle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/dombrush.html#hasAttributeBrushStyle
    """
    #  bool DomBrush::hasAttributeBrushStyle() const
    return self.uglySide.call(
        'ritual_ZNK8DomBrush22hasAttributeBrushStyleEv',
    )

  def attributeBrushStyle(self) -> str:
    """
    Calls Qt's 'QString DomBrush::attributeBrushStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/dombrush.html#attributeBrushStyle

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomBrush::attributeBrushStyle() const
    return self.uglySide.call('ritual_ZNK8DomBrush19attributeBrushStyleEv')

  def kind(self) -> Kind:
    """
    Calls Qt's 'Kind DomBrush::kind() const'.

    Qt's own words: https://doc.qt.io/qt-6/dombrush.html#kind

    Returns
    -------

    Kind
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Kind(number)' gives.
    """
    #  Kind DomBrush::kind() const
    return DomBrush.Kind(self.uglySide.call('ritual_ZNK8DomBrush4kindEv'))

  def elementColor(self) -> Optional[DomColor]:
    """
    Calls Qt's 'DomColor *DomBrush::elementColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/dombrush.html#elementColor

    Returns
    -------

    Optional[DomColor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomColor *DomBrush::elementColor() const
    address = self.uglySide.call('ritual_ZNK8DomBrush12elementColorEv')
    from . import DomColor
    return DomColor._cuteAt(address)

  def elementTexture(self) -> Optional[DomProperty]:
    """
    Calls Qt's 'DomProperty *DomBrush::elementTexture() const'.

    Qt's own words: https://doc.qt.io/qt-6/dombrush.html#elementTexture

    Returns
    -------

    Optional[DomProperty]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomProperty *DomBrush::elementTexture() const
    address = self.uglySide.call('ritual_ZNK8DomBrush14elementTextureEv')
    from . import DomProperty
    return DomProperty._cuteAt(address)

  def elementGradient(self) -> Optional[DomGradient]:
    """
    Calls Qt's 'DomGradient *DomBrush::elementGradient() const'.

    Qt's own words: https://doc.qt.io/qt-6/dombrush.html#elementGradient

    Returns
    -------

    Optional[DomGradient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomGradient *DomBrush::elementGradient() const
    address = self.uglySide.call('ritual_ZNK8DomBrush15elementGradientEv')
    from . import DomGradient
    return DomGradient._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAttributeBrushStyle(self, a: str) -> None:
    """
    Calls Qt's 'void DomBrush::setAttributeBrushStyle(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/dombrush.html#setAttributeBrushStyle

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomBrush::setAttributeBrushStyle(const QString &a)
    self.uglySide.call(
        'ritual_ZN8DomBrush22setAttributeBrushStyleERK7QString', a,
    )

  @overload(DomColor)
  @overload(NoneType)
  def setElementColor(self, a: Optional[DomColor]) -> None:
    """
    Calls Qt's 'void DomBrush::setElementColor(DomColor *a)'.

    Qt's own words: https://doc.qt.io/qt-6/dombrush.html#setElementColor

    Parameters
    ----------

    a : Optional[DomColor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomBrush::setElementColor(DomColor *a)
    self.uglySide.call(
        'ritual_ZN8DomBrush15setElementColorEP8DomColor', self._addressOf(a),
    )

  @overload(DomProperty)
  @overload(NoneType)
  def setElementTexture(self, a: Optional[DomProperty]) -> None:
    """
    Calls Qt's 'void DomBrush::setElementTexture(DomProperty *a)'.

    Qt's own words: https://doc.qt.io/qt-6/dombrush.html#setElementTexture

    Parameters
    ----------

    a : Optional[DomProperty]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomBrush::setElementTexture(DomProperty *a)
    self.uglySide.call(
        'ritual_ZN8DomBrush17setElementTextureEP11DomProperty',
        self._addressOf(a),
    )

  @overload(DomGradient)
  @overload(NoneType)
  def setElementGradient(self, a: Optional[DomGradient]) -> None:
    """
    Calls Qt's 'void DomBrush::setElementGradient(DomGradient *a)'.

    Qt's own words: https://doc.qt.io/qt-6/dombrush.html#setElementGradient

    Parameters
    ----------

    a : Optional[DomGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomBrush::setElementGradient(DomGradient *a)
    self.uglySide.call(
        'ritual_ZN8DomBrush18setElementGradientEP11DomGradient',
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
    Notes what was given, for Qt's 'DomBrush::DomBrush()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/dombrush.html#DomBrush
    """
    #  DomBrush::DomBrush()
    self._noteCreation(DomBrush, lambda: Rituals.call(
        'ritual_ZN8DomBrushC1Ev',
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

  def clearAttributeBrushStyle(self) -> None:
    """
    Calls Qt's 'void DomBrush::clearAttributeBrushStyle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/dombrush.html#clearAttributeBrushStyle
    """
    #  void DomBrush::clearAttributeBrushStyle()
    self.uglySide.call('ritual_ZN8DomBrush24clearAttributeBrushStyleEv')

  def takeElementColor(self) -> Optional[DomColor]:
    """
    Calls Qt's 'DomColor *DomBrush::takeElementColor()'.

    Qt's own words: https://doc.qt.io/qt-6/dombrush.html#takeElementColor

    Returns
    -------

    Optional[DomColor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomColor *DomBrush::takeElementColor()
    address = self.uglySide.call('ritual_ZN8DomBrush16takeElementColorEv')
    from . import DomColor
    return DomColor._cuteAt(address)

  def takeElementTexture(self) -> Optional[DomProperty]:
    """
    Calls Qt's 'DomProperty *DomBrush::takeElementTexture()'.

    Qt's own words: https://doc.qt.io/qt-6/dombrush.html#takeElementTexture

    Returns
    -------

    Optional[DomProperty]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomProperty *DomBrush::takeElementTexture()
    address = self.uglySide.call('ritual_ZN8DomBrush18takeElementTextureEv')
    from . import DomProperty
    return DomProperty._cuteAt(address)

  def takeElementGradient(self) -> Optional[DomGradient]:
    """
    Calls Qt's 'DomGradient *DomBrush::takeElementGradient()'.

    Qt's own words: https://doc.qt.io/qt-6/dombrush.html#takeElementGradient

    Returns
    -------

    Optional[DomGradient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomGradient *DomBrush::takeElementGradient()
    address = self.uglySide.call('ritual_ZN8DomBrush19takeElementGradientEv')
    from . import DomGradient
    return DomGradient._cuteAt(address)

  def clear(self) -> None:
    """
    Calls Qt's 'void DomBrush::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/dombrush.html#clear
    """
    #  void DomBrush::clear()
    self.uglySide.call('ritual_ZN8DomBrush5clearEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomBrush::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomBrush.read' has no cute function yet. Qt's 'void "
        "DomBrush::read(QXmlStreamReader &reader)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomBrush::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomBrush.write' has no cute function yet. Qt's 'void "
        "DomBrush::write(QXmlStreamWriter &writer, const QString &tagName) "
        "const': takes a type Python has no way to hand over yet.")
