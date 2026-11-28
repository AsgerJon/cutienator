"""
DomPalette binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomPalette to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import DomColorGroup
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomColorGroup = WAIT['DomColorGroup']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DomPalette(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomPalette: a plain Python object standing in front
  of one C++ DomPalette.

  What exists
  -----------

  Every function of Qt's DomPalette that has a ritual and that Python can
  call so far, 15 names in all: 'elementActive', 'takeElementActive',
  'setElementActive', 'hasElementActive', 'clearElementActive',
  'elementInactive', 'takeElementInactive', 'setElementInactive',
  'hasElementInactive', 'clearElementInactive', 'elementDisabled',
  'takeElementDisabled', 'setElementDisabled', 'hasElementDisabled',
  'clearElementDisabled'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomPalette::~DomPalette()': the destructor: Python never removes a
    C++ DomPalette.
  - Qt's 'void DomPalette::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomPalette::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 23 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomPalette is created at the first use, not by 'DomPalette(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomPalette.
  - Each name of Qt's DomPalette that has no cute function yet, 'read',
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
  __qt_class__ = 'DomPalette'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def elementActive(self) -> Optional[DomColorGroup]:
    """
    Calls Qt's 'DomColorGroup *DomPalette::elementActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/dompalette.html#elementActive

    Returns
    -------

    Optional[DomColorGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomColorGroup *DomPalette::elementActive() const
    address = self.uglySide.call('ritual_ZNK10DomPalette13elementActiveEv')
    from . import DomColorGroup
    return DomColorGroup._cuteAt(address)

  def hasElementActive(self) -> bool:
    """
    Calls Qt's 'bool DomPalette::hasElementActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/dompalette.html#hasElementActive
    """
    #  bool DomPalette::hasElementActive() const
    return self.uglySide.call('ritual_ZNK10DomPalette16hasElementActiveEv')

  def elementInactive(self) -> Optional[DomColorGroup]:
    """
    Calls Qt's 'DomColorGroup *DomPalette::elementInactive() const'.

    Qt's own words: https://doc.qt.io/qt-6/dompalette.html#elementInactive

    Returns
    -------

    Optional[DomColorGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomColorGroup *DomPalette::elementInactive() const
    address = self.uglySide.call('ritual_ZNK10DomPalette15elementInactiveEv')
    from . import DomColorGroup
    return DomColorGroup._cuteAt(address)

  def hasElementInactive(self) -> bool:
    """
    Calls Qt's 'bool DomPalette::hasElementInactive() const'.

    Qt's own words: https://doc.qt.io/qt-6/dompalette.html#hasElementInactive
    """
    #  bool DomPalette::hasElementInactive() const
    return self.uglySide.call('ritual_ZNK10DomPalette18hasElementInactiveEv')

  def elementDisabled(self) -> Optional[DomColorGroup]:
    """
    Calls Qt's 'DomColorGroup *DomPalette::elementDisabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/dompalette.html#elementDisabled

    Returns
    -------

    Optional[DomColorGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomColorGroup *DomPalette::elementDisabled() const
    address = self.uglySide.call('ritual_ZNK10DomPalette15elementDisabledEv')
    from . import DomColorGroup
    return DomColorGroup._cuteAt(address)

  def hasElementDisabled(self) -> bool:
    """
    Calls Qt's 'bool DomPalette::hasElementDisabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/dompalette.html#hasElementDisabled
    """
    #  bool DomPalette::hasElementDisabled() const
    return self.uglySide.call('ritual_ZNK10DomPalette18hasElementDisabledEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(DomColorGroup)
  @overload(NoneType)
  def setElementActive(self, a: Optional[DomColorGroup]) -> None:
    """
    Calls Qt's 'void DomPalette::setElementActive(DomColorGroup *a)'.

    Qt's own words: https://doc.qt.io/qt-6/dompalette.html#setElementActive

    Parameters
    ----------

    a : Optional[DomColorGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomPalette::setElementActive(DomColorGroup *a)
    self.uglySide.call(
        'ritual_ZN10DomPalette16setElementActiveEP13DomColorGroup',
        self._addressOf(a),
    )

  @overload(DomColorGroup)
  @overload(NoneType)
  def setElementInactive(self, a: Optional[DomColorGroup]) -> None:
    """
    Calls Qt's 'void DomPalette::setElementInactive(DomColorGroup *a)'.

    Qt's own words: https://doc.qt.io/qt-6/dompalette.html#setElementInactive

    Parameters
    ----------

    a : Optional[DomColorGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomPalette::setElementInactive(DomColorGroup *a)
    self.uglySide.call(
        'ritual_ZN10DomPalette18setElementInactiveEP13DomColorGroup',
        self._addressOf(a),
    )

  @overload(DomColorGroup)
  @overload(NoneType)
  def setElementDisabled(self, a: Optional[DomColorGroup]) -> None:
    """
    Calls Qt's 'void DomPalette::setElementDisabled(DomColorGroup *a)'.

    Qt's own words: https://doc.qt.io/qt-6/dompalette.html#setElementDisabled

    Parameters
    ----------

    a : Optional[DomColorGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomPalette::setElementDisabled(DomColorGroup *a)
    self.uglySide.call(
        'ritual_ZN10DomPalette18setElementDisabledEP13DomColorGroup',
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
    Notes what was given, for Qt's 'DomPalette::DomPalette()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/dompalette.html#DomPalette
    """
    #  DomPalette::DomPalette()
    self._noteCreation(DomPalette, lambda: Rituals.call(
        'ritual_ZN10DomPaletteC1Ev',
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

  def takeElementActive(self) -> Optional[DomColorGroup]:
    """
    Calls Qt's 'DomColorGroup *DomPalette::takeElementActive()'.

    Qt's own words: https://doc.qt.io/qt-6/dompalette.html#takeElementActive

    Returns
    -------

    Optional[DomColorGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomColorGroup *DomPalette::takeElementActive()
    address = self.uglySide.call(
        'ritual_ZN10DomPalette17takeElementActiveEv',
    )
    from . import DomColorGroup
    return DomColorGroup._cuteAt(address)

  def clearElementActive(self) -> None:
    """
    Calls Qt's 'void DomPalette::clearElementActive()'.

    Qt's own words: https://doc.qt.io/qt-6/dompalette.html#clearElementActive
    """
    #  void DomPalette::clearElementActive()
    self.uglySide.call('ritual_ZN10DomPalette18clearElementActiveEv')

  def takeElementInactive(self) -> Optional[DomColorGroup]:
    """
    Calls Qt's 'DomColorGroup *DomPalette::takeElementInactive()'.

    Qt's own words:
    https://doc.qt.io/qt-6/dompalette.html#takeElementInactive

    Returns
    -------

    Optional[DomColorGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomColorGroup *DomPalette::takeElementInactive()
    address = self.uglySide.call(
        'ritual_ZN10DomPalette19takeElementInactiveEv',
    )
    from . import DomColorGroup
    return DomColorGroup._cuteAt(address)

  def clearElementInactive(self) -> None:
    """
    Calls Qt's 'void DomPalette::clearElementInactive()'.

    Qt's own words:
    https://doc.qt.io/qt-6/dompalette.html#clearElementInactive
    """
    #  void DomPalette::clearElementInactive()
    self.uglySide.call('ritual_ZN10DomPalette20clearElementInactiveEv')

  def takeElementDisabled(self) -> Optional[DomColorGroup]:
    """
    Calls Qt's 'DomColorGroup *DomPalette::takeElementDisabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/dompalette.html#takeElementDisabled

    Returns
    -------

    Optional[DomColorGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomColorGroup *DomPalette::takeElementDisabled()
    address = self.uglySide.call(
        'ritual_ZN10DomPalette19takeElementDisabledEv',
    )
    from . import DomColorGroup
    return DomColorGroup._cuteAt(address)

  def clearElementDisabled(self) -> None:
    """
    Calls Qt's 'void DomPalette::clearElementDisabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/dompalette.html#clearElementDisabled
    """
    #  void DomPalette::clearElementDisabled()
    self.uglySide.call('ritual_ZN10DomPalette20clearElementDisabledEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomPalette::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomPalette.read' has no cute function yet. Qt's 'void "
        "DomPalette::read(QXmlStreamReader &reader)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomPalette::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomPalette.write' has no cute function yet. Qt's 'void "
        "DomPalette::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")
