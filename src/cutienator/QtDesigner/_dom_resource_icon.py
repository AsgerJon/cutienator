"""
DomResourceIcon binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomResourceIcon to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import DomResourcePixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomResourcePixmap = WAIT['DomResourcePixmap']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DomResourceIcon(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomResourceIcon: a plain Python object standing in
  front of one C++ DomResourceIcon.

  What exists
  -----------

  Every function of Qt's DomResourceIcon that has a ritual and that Python
  can call so far, 50 names in all: 'text', 'setText', 'hasAttributeTheme',
  'attributeTheme', 'setAttributeTheme', 'clearAttributeTheme',
  'hasAttributeResource', 'attributeResource', 'setAttributeResource',
  'clearAttributeResource', 'elementNormalOff', 'takeElementNormalOff',
  'setElementNormalOff', 'hasElementNormalOff', 'clearElementNormalOff',
  'elementNormalOn', 'takeElementNormalOn', 'setElementNormalOn',
  'hasElementNormalOn', 'clearElementNormalOn', 'elementDisabledOff',
  'takeElementDisabledOff', 'setElementDisabledOff', 'hasElementDisabledOff',
  'clearElementDisabledOff', 'elementDisabledOn', 'takeElementDisabledOn',
  'setElementDisabledOn', 'hasElementDisabledOn', 'clearElementDisabledOn',
  'elementActiveOff', 'takeElementActiveOff', 'setElementActiveOff',
  'hasElementActiveOff', 'clearElementActiveOff', 'elementActiveOn',
  'takeElementActiveOn', 'setElementActiveOn', 'hasElementActiveOn',
  'clearElementActiveOn', 'elementSelectedOff', 'takeElementSelectedOff',
  'setElementSelectedOff', 'hasElementSelectedOff',
  'clearElementSelectedOff', 'elementSelectedOn', 'takeElementSelectedOn',
  'setElementSelectedOn', 'hasElementSelectedOn', 'clearElementSelectedOn'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomResourceIcon::~DomResourceIcon()': the destructor: Python never
    removes a C++ DomResourceIcon.
  - Qt's 'void DomResourceIcon::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomResourceIcon::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 58 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomResourceIcon is created at the first use, not by
    'DomResourceIcon(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomResourceIcon.
  - Each name of Qt's DomResourceIcon that has no cute function yet, 'read',
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
  __qt_class__ = 'DomResourceIcon'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def text(self) -> str:
    """
    Calls Qt's 'QString DomResourceIcon::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/domresourceicon.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomResourceIcon::text() const
    return self.uglySide.call('ritual_ZNK15DomResourceIcon4textEv')

  def hasAttributeTheme(self) -> bool:
    """
    Calls Qt's 'bool DomResourceIcon::hasAttributeTheme() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#hasAttributeTheme
    """
    #  bool DomResourceIcon::hasAttributeTheme() const
    return self.uglySide.call(
        'ritual_ZNK15DomResourceIcon17hasAttributeThemeEv',
    )

  def attributeTheme(self) -> str:
    """
    Calls Qt's 'QString DomResourceIcon::attributeTheme() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#attributeTheme

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomResourceIcon::attributeTheme() const
    return self.uglySide.call(
        'ritual_ZNK15DomResourceIcon14attributeThemeEv',
    )

  def hasAttributeResource(self) -> bool:
    """
    Calls Qt's 'bool DomResourceIcon::hasAttributeResource() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#hasAttributeResource
    """
    #  bool DomResourceIcon::hasAttributeResource() const
    return self.uglySide.call(
        'ritual_ZNK15DomResourceIcon20hasAttributeResourceEv',
    )

  def attributeResource(self) -> str:
    """
    Calls Qt's 'QString DomResourceIcon::attributeResource() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#attributeResource

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomResourceIcon::attributeResource() const
    return self.uglySide.call(
        'ritual_ZNK15DomResourceIcon17attributeResourceEv',
    )

  def elementNormalOff(self) -> Optional[DomResourcePixmap]:
    """
    Calls Qt's 'DomResourcePixmap *DomResourceIcon::elementNormalOff()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#elementNormalOff

    Returns
    -------

    Optional[DomResourcePixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResourcePixmap *DomResourceIcon::elementNormalOff() const
    address = self.uglySide.call(
        'ritual_ZNK15DomResourceIcon16elementNormalOffEv',
    )
    from . import DomResourcePixmap
    return DomResourcePixmap._cuteAt(address)

  def hasElementNormalOff(self) -> bool:
    """
    Calls Qt's 'bool DomResourceIcon::hasElementNormalOff() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#hasElementNormalOff
    """
    #  bool DomResourceIcon::hasElementNormalOff() const
    return self.uglySide.call(
        'ritual_ZNK15DomResourceIcon19hasElementNormalOffEv',
    )

  def elementNormalOn(self) -> Optional[DomResourcePixmap]:
    """
    Calls Qt's 'DomResourcePixmap *DomResourceIcon::elementNormalOn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#elementNormalOn

    Returns
    -------

    Optional[DomResourcePixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResourcePixmap *DomResourceIcon::elementNormalOn() const
    address = self.uglySide.call(
        'ritual_ZNK15DomResourceIcon15elementNormalOnEv',
    )
    from . import DomResourcePixmap
    return DomResourcePixmap._cuteAt(address)

  def hasElementNormalOn(self) -> bool:
    """
    Calls Qt's 'bool DomResourceIcon::hasElementNormalOn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#hasElementNormalOn
    """
    #  bool DomResourceIcon::hasElementNormalOn() const
    return self.uglySide.call(
        'ritual_ZNK15DomResourceIcon18hasElementNormalOnEv',
    )

  def elementDisabledOff(self) -> Optional[DomResourcePixmap]:
    """
    Calls Qt's 'DomResourcePixmap *DomResourceIcon::elementDisabledOff()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#elementDisabledOff

    Returns
    -------

    Optional[DomResourcePixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResourcePixmap *DomResourceIcon::elementDisabledOff() const
    address = self.uglySide.call(
        'ritual_ZNK15DomResourceIcon18elementDisabledOffEv',
    )
    from . import DomResourcePixmap
    return DomResourcePixmap._cuteAt(address)

  def hasElementDisabledOff(self) -> bool:
    """
    Calls Qt's 'bool DomResourceIcon::hasElementDisabledOff() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#hasElementDisabledOff
    """
    #  bool DomResourceIcon::hasElementDisabledOff() const
    return self.uglySide.call(
        'ritual_ZNK15DomResourceIcon21hasElementDisabledOffEv',
    )

  def elementDisabledOn(self) -> Optional[DomResourcePixmap]:
    """
    Calls Qt's 'DomResourcePixmap *DomResourceIcon::elementDisabledOn()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#elementDisabledOn

    Returns
    -------

    Optional[DomResourcePixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResourcePixmap *DomResourceIcon::elementDisabledOn() const
    address = self.uglySide.call(
        'ritual_ZNK15DomResourceIcon17elementDisabledOnEv',
    )
    from . import DomResourcePixmap
    return DomResourcePixmap._cuteAt(address)

  def hasElementDisabledOn(self) -> bool:
    """
    Calls Qt's 'bool DomResourceIcon::hasElementDisabledOn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#hasElementDisabledOn
    """
    #  bool DomResourceIcon::hasElementDisabledOn() const
    return self.uglySide.call(
        'ritual_ZNK15DomResourceIcon20hasElementDisabledOnEv',
    )

  def elementActiveOff(self) -> Optional[DomResourcePixmap]:
    """
    Calls Qt's 'DomResourcePixmap *DomResourceIcon::elementActiveOff()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#elementActiveOff

    Returns
    -------

    Optional[DomResourcePixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResourcePixmap *DomResourceIcon::elementActiveOff() const
    address = self.uglySide.call(
        'ritual_ZNK15DomResourceIcon16elementActiveOffEv',
    )
    from . import DomResourcePixmap
    return DomResourcePixmap._cuteAt(address)

  def hasElementActiveOff(self) -> bool:
    """
    Calls Qt's 'bool DomResourceIcon::hasElementActiveOff() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#hasElementActiveOff
    """
    #  bool DomResourceIcon::hasElementActiveOff() const
    return self.uglySide.call(
        'ritual_ZNK15DomResourceIcon19hasElementActiveOffEv',
    )

  def elementActiveOn(self) -> Optional[DomResourcePixmap]:
    """
    Calls Qt's 'DomResourcePixmap *DomResourceIcon::elementActiveOn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#elementActiveOn

    Returns
    -------

    Optional[DomResourcePixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResourcePixmap *DomResourceIcon::elementActiveOn() const
    address = self.uglySide.call(
        'ritual_ZNK15DomResourceIcon15elementActiveOnEv',
    )
    from . import DomResourcePixmap
    return DomResourcePixmap._cuteAt(address)

  def hasElementActiveOn(self) -> bool:
    """
    Calls Qt's 'bool DomResourceIcon::hasElementActiveOn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#hasElementActiveOn
    """
    #  bool DomResourceIcon::hasElementActiveOn() const
    return self.uglySide.call(
        'ritual_ZNK15DomResourceIcon18hasElementActiveOnEv',
    )

  def elementSelectedOff(self) -> Optional[DomResourcePixmap]:
    """
    Calls Qt's 'DomResourcePixmap *DomResourceIcon::elementSelectedOff()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#elementSelectedOff

    Returns
    -------

    Optional[DomResourcePixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResourcePixmap *DomResourceIcon::elementSelectedOff() const
    address = self.uglySide.call(
        'ritual_ZNK15DomResourceIcon18elementSelectedOffEv',
    )
    from . import DomResourcePixmap
    return DomResourcePixmap._cuteAt(address)

  def hasElementSelectedOff(self) -> bool:
    """
    Calls Qt's 'bool DomResourceIcon::hasElementSelectedOff() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#hasElementSelectedOff
    """
    #  bool DomResourceIcon::hasElementSelectedOff() const
    return self.uglySide.call(
        'ritual_ZNK15DomResourceIcon21hasElementSelectedOffEv',
    )

  def elementSelectedOn(self) -> Optional[DomResourcePixmap]:
    """
    Calls Qt's 'DomResourcePixmap *DomResourceIcon::elementSelectedOn()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#elementSelectedOn

    Returns
    -------

    Optional[DomResourcePixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResourcePixmap *DomResourceIcon::elementSelectedOn() const
    address = self.uglySide.call(
        'ritual_ZNK15DomResourceIcon17elementSelectedOnEv',
    )
    from . import DomResourcePixmap
    return DomResourcePixmap._cuteAt(address)

  def hasElementSelectedOn(self) -> bool:
    """
    Calls Qt's 'bool DomResourceIcon::hasElementSelectedOn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#hasElementSelectedOn
    """
    #  bool DomResourceIcon::hasElementSelectedOn() const
    return self.uglySide.call(
        'ritual_ZNK15DomResourceIcon20hasElementSelectedOnEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, s: str) -> None:
    """
    Calls Qt's 'void DomResourceIcon::setText(const QString &s)'.

    Qt's own words: https://doc.qt.io/qt-6/domresourceicon.html#setText

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomResourceIcon::setText(const QString &s)
    self.uglySide.call('ritual_ZN15DomResourceIcon7setTextERK7QString', s)

  @overload(str)
  def setAttributeTheme(self, a: str) -> None:
    """
    Calls Qt's 'void DomResourceIcon::setAttributeTheme(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#setAttributeTheme

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomResourceIcon::setAttributeTheme(const QString &a)
    self.uglySide.call(
        'ritual_ZN15DomResourceIcon17setAttributeThemeERK7QString', a,
    )

  @overload(str)
  def setAttributeResource(self, a: str) -> None:
    """
    Calls Qt's 'void DomResourceIcon::setAttributeResource(const QString
    &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#setAttributeResource

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomResourceIcon::setAttributeResource(const QString &a)
    self.uglySide.call(
        'ritual_ZN15DomResourceIcon20setAttributeResourceERK7QString', a,
    )

  @overload(DomResourcePixmap)
  @overload(NoneType)
  def setElementNormalOff(self, a: Optional[DomResourcePixmap]) -> None:
    """
    Calls Qt's 'void DomResourceIcon::setElementNormalOff(DomResourcePixmap
    *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#setElementNormalOff

    Parameters
    ----------

    a : Optional[DomResourcePixmap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomResourceIcon::setElementNormalOff(DomResourcePixmap *a)
    self.uglySide.call(
        'ritual_ZN15DomResourceIcon19setElementNormalOffEP17DomResourcePixm'
        'ap',
        self._addressOf(a),
    )

  @overload(DomResourcePixmap)
  @overload(NoneType)
  def setElementNormalOn(self, a: Optional[DomResourcePixmap]) -> None:
    """
    Calls Qt's 'void DomResourceIcon::setElementNormalOn(DomResourcePixmap
    *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#setElementNormalOn

    Parameters
    ----------

    a : Optional[DomResourcePixmap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomResourceIcon::setElementNormalOn(DomResourcePixmap *a)
    self.uglySide.call(
        'ritual_ZN15DomResourceIcon18setElementNormalOnEP17DomResourcePixma'
        'p',
        self._addressOf(a),
    )

  @overload(DomResourcePixmap)
  @overload(NoneType)
  def setElementDisabledOff(self, a: Optional[DomResourcePixmap]) -> None:
    """
    Calls Qt's 'void DomResourceIcon::setElementDisabledOff(DomResourcePixmap
    *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#setElementDisabledOff

    Parameters
    ----------

    a : Optional[DomResourcePixmap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomResourceIcon::setElementDisabledOff(DomResourcePixmap *a)
    self.uglySide.call(
        'ritual_ZN15DomResourceIcon21setElementDisabledOffEP17DomResourcePi'
        'xmap',
        self._addressOf(a),
    )

  @overload(DomResourcePixmap)
  @overload(NoneType)
  def setElementDisabledOn(self, a: Optional[DomResourcePixmap]) -> None:
    """
    Calls Qt's 'void DomResourceIcon::setElementDisabledOn(DomResourcePixmap
    *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#setElementDisabledOn

    Parameters
    ----------

    a : Optional[DomResourcePixmap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomResourceIcon::setElementDisabledOn(DomResourcePixmap *a)
    self.uglySide.call(
        'ritual_ZN15DomResourceIcon20setElementDisabledOnEP17DomResourcePix'
        'map',
        self._addressOf(a),
    )

  @overload(DomResourcePixmap)
  @overload(NoneType)
  def setElementActiveOff(self, a: Optional[DomResourcePixmap]) -> None:
    """
    Calls Qt's 'void DomResourceIcon::setElementActiveOff(DomResourcePixmap
    *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#setElementActiveOff

    Parameters
    ----------

    a : Optional[DomResourcePixmap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomResourceIcon::setElementActiveOff(DomResourcePixmap *a)
    self.uglySide.call(
        'ritual_ZN15DomResourceIcon19setElementActiveOffEP17DomResourcePixm'
        'ap',
        self._addressOf(a),
    )

  @overload(DomResourcePixmap)
  @overload(NoneType)
  def setElementActiveOn(self, a: Optional[DomResourcePixmap]) -> None:
    """
    Calls Qt's 'void DomResourceIcon::setElementActiveOn(DomResourcePixmap
    *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#setElementActiveOn

    Parameters
    ----------

    a : Optional[DomResourcePixmap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomResourceIcon::setElementActiveOn(DomResourcePixmap *a)
    self.uglySide.call(
        'ritual_ZN15DomResourceIcon18setElementActiveOnEP17DomResourcePixma'
        'p',
        self._addressOf(a),
    )

  @overload(DomResourcePixmap)
  @overload(NoneType)
  def setElementSelectedOff(self, a: Optional[DomResourcePixmap]) -> None:
    """
    Calls Qt's 'void DomResourceIcon::setElementSelectedOff(DomResourcePixmap
    *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#setElementSelectedOff

    Parameters
    ----------

    a : Optional[DomResourcePixmap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomResourceIcon::setElementSelectedOff(DomResourcePixmap *a)
    self.uglySide.call(
        'ritual_ZN15DomResourceIcon21setElementSelectedOffEP17DomResourcePi'
        'xmap',
        self._addressOf(a),
    )

  @overload(DomResourcePixmap)
  @overload(NoneType)
  def setElementSelectedOn(self, a: Optional[DomResourcePixmap]) -> None:
    """
    Calls Qt's 'void DomResourceIcon::setElementSelectedOn(DomResourcePixmap
    *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#setElementSelectedOn

    Parameters
    ----------

    a : Optional[DomResourcePixmap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomResourceIcon::setElementSelectedOn(DomResourcePixmap *a)
    self.uglySide.call(
        'ritual_ZN15DomResourceIcon20setElementSelectedOnEP17DomResourcePix'
        'map',
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
    Notes what was given, for Qt's 'DomResourceIcon::DomResourceIcon()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#DomResourceIcon
    """
    #  DomResourceIcon::DomResourceIcon()
    self._noteCreation(DomResourceIcon, lambda: Rituals.call(
        'ritual_ZN15DomResourceIconC1Ev',
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

  def clearAttributeTheme(self) -> None:
    """
    Calls Qt's 'void DomResourceIcon::clearAttributeTheme()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#clearAttributeTheme
    """
    #  void DomResourceIcon::clearAttributeTheme()
    self.uglySide.call('ritual_ZN15DomResourceIcon19clearAttributeThemeEv')

  def clearAttributeResource(self) -> None:
    """
    Calls Qt's 'void DomResourceIcon::clearAttributeResource()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#clearAttributeResource
    """
    #  void DomResourceIcon::clearAttributeResource()
    self.uglySide.call(
        'ritual_ZN15DomResourceIcon22clearAttributeResourceEv',
    )

  def takeElementNormalOff(self) -> Optional[DomResourcePixmap]:
    """
    Calls Qt's 'DomResourcePixmap *DomResourceIcon::takeElementNormalOff()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#takeElementNormalOff

    Returns
    -------

    Optional[DomResourcePixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResourcePixmap *DomResourceIcon::takeElementNormalOff()
    address = self.uglySide.call(
        'ritual_ZN15DomResourceIcon20takeElementNormalOffEv',
    )
    from . import DomResourcePixmap
    return DomResourcePixmap._cuteAt(address)

  def clearElementNormalOff(self) -> None:
    """
    Calls Qt's 'void DomResourceIcon::clearElementNormalOff()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#clearElementNormalOff
    """
    #  void DomResourceIcon::clearElementNormalOff()
    self.uglySide.call('ritual_ZN15DomResourceIcon21clearElementNormalOffEv')

  def takeElementNormalOn(self) -> Optional[DomResourcePixmap]:
    """
    Calls Qt's 'DomResourcePixmap *DomResourceIcon::takeElementNormalOn()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#takeElementNormalOn

    Returns
    -------

    Optional[DomResourcePixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResourcePixmap *DomResourceIcon::takeElementNormalOn()
    address = self.uglySide.call(
        'ritual_ZN15DomResourceIcon19takeElementNormalOnEv',
    )
    from . import DomResourcePixmap
    return DomResourcePixmap._cuteAt(address)

  def clearElementNormalOn(self) -> None:
    """
    Calls Qt's 'void DomResourceIcon::clearElementNormalOn()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#clearElementNormalOn
    """
    #  void DomResourceIcon::clearElementNormalOn()
    self.uglySide.call('ritual_ZN15DomResourceIcon20clearElementNormalOnEv')

  def takeElementDisabledOff(self) -> Optional[DomResourcePixmap]:
    """
    Calls Qt's 'DomResourcePixmap
    *DomResourceIcon::takeElementDisabledOff()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#takeElementDisabledOff

    Returns
    -------

    Optional[DomResourcePixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResourcePixmap *DomResourceIcon::takeElementDisabledOff()
    address = self.uglySide.call(
        'ritual_ZN15DomResourceIcon22takeElementDisabledOffEv',
    )
    from . import DomResourcePixmap
    return DomResourcePixmap._cuteAt(address)

  def clearElementDisabledOff(self) -> None:
    """
    Calls Qt's 'void DomResourceIcon::clearElementDisabledOff()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#clearElementDisabledOff
    """
    #  void DomResourceIcon::clearElementDisabledOff()
    self.uglySide.call(
        'ritual_ZN15DomResourceIcon23clearElementDisabledOffEv',
    )

  def takeElementDisabledOn(self) -> Optional[DomResourcePixmap]:
    """
    Calls Qt's 'DomResourcePixmap *DomResourceIcon::takeElementDisabledOn()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#takeElementDisabledOn

    Returns
    -------

    Optional[DomResourcePixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResourcePixmap *DomResourceIcon::takeElementDisabledOn()
    address = self.uglySide.call(
        'ritual_ZN15DomResourceIcon21takeElementDisabledOnEv',
    )
    from . import DomResourcePixmap
    return DomResourcePixmap._cuteAt(address)

  def clearElementDisabledOn(self) -> None:
    """
    Calls Qt's 'void DomResourceIcon::clearElementDisabledOn()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#clearElementDisabledOn
    """
    #  void DomResourceIcon::clearElementDisabledOn()
    self.uglySide.call(
        'ritual_ZN15DomResourceIcon22clearElementDisabledOnEv',
    )

  def takeElementActiveOff(self) -> Optional[DomResourcePixmap]:
    """
    Calls Qt's 'DomResourcePixmap *DomResourceIcon::takeElementActiveOff()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#takeElementActiveOff

    Returns
    -------

    Optional[DomResourcePixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResourcePixmap *DomResourceIcon::takeElementActiveOff()
    address = self.uglySide.call(
        'ritual_ZN15DomResourceIcon20takeElementActiveOffEv',
    )
    from . import DomResourcePixmap
    return DomResourcePixmap._cuteAt(address)

  def clearElementActiveOff(self) -> None:
    """
    Calls Qt's 'void DomResourceIcon::clearElementActiveOff()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#clearElementActiveOff
    """
    #  void DomResourceIcon::clearElementActiveOff()
    self.uglySide.call('ritual_ZN15DomResourceIcon21clearElementActiveOffEv')

  def takeElementActiveOn(self) -> Optional[DomResourcePixmap]:
    """
    Calls Qt's 'DomResourcePixmap *DomResourceIcon::takeElementActiveOn()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#takeElementActiveOn

    Returns
    -------

    Optional[DomResourcePixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResourcePixmap *DomResourceIcon::takeElementActiveOn()
    address = self.uglySide.call(
        'ritual_ZN15DomResourceIcon19takeElementActiveOnEv',
    )
    from . import DomResourcePixmap
    return DomResourcePixmap._cuteAt(address)

  def clearElementActiveOn(self) -> None:
    """
    Calls Qt's 'void DomResourceIcon::clearElementActiveOn()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#clearElementActiveOn
    """
    #  void DomResourceIcon::clearElementActiveOn()
    self.uglySide.call('ritual_ZN15DomResourceIcon20clearElementActiveOnEv')

  def takeElementSelectedOff(self) -> Optional[DomResourcePixmap]:
    """
    Calls Qt's 'DomResourcePixmap
    *DomResourceIcon::takeElementSelectedOff()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#takeElementSelectedOff

    Returns
    -------

    Optional[DomResourcePixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResourcePixmap *DomResourceIcon::takeElementSelectedOff()
    address = self.uglySide.call(
        'ritual_ZN15DomResourceIcon22takeElementSelectedOffEv',
    )
    from . import DomResourcePixmap
    return DomResourcePixmap._cuteAt(address)

  def clearElementSelectedOff(self) -> None:
    """
    Calls Qt's 'void DomResourceIcon::clearElementSelectedOff()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#clearElementSelectedOff
    """
    #  void DomResourceIcon::clearElementSelectedOff()
    self.uglySide.call(
        'ritual_ZN15DomResourceIcon23clearElementSelectedOffEv',
    )

  def takeElementSelectedOn(self) -> Optional[DomResourcePixmap]:
    """
    Calls Qt's 'DomResourcePixmap *DomResourceIcon::takeElementSelectedOn()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#takeElementSelectedOn

    Returns
    -------

    Optional[DomResourcePixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResourcePixmap *DomResourceIcon::takeElementSelectedOn()
    address = self.uglySide.call(
        'ritual_ZN15DomResourceIcon21takeElementSelectedOnEv',
    )
    from . import DomResourcePixmap
    return DomResourcePixmap._cuteAt(address)

  def clearElementSelectedOn(self) -> None:
    """
    Calls Qt's 'void DomResourceIcon::clearElementSelectedOn()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourceicon.html#clearElementSelectedOn
    """
    #  void DomResourceIcon::clearElementSelectedOn()
    self.uglySide.call(
        'ritual_ZN15DomResourceIcon22clearElementSelectedOnEv',
    )

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomResourceIcon::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomResourceIcon.read' has no cute function yet. Qt's 'void "
        "DomResourceIcon::read(QXmlStreamReader &reader)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomResourceIcon::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomResourceIcon.write' has no cute function yet. Qt's 'void "
        "DomResourceIcon::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")
