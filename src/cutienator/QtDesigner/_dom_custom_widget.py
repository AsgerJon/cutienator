"""
DomCustomWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomCustomWidget to be private: it declares the class in a header
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

  from . import DomHeader, DomPropertySpecifications, DomSize, DomSlots
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomHeader = WAIT['DomHeader']
  DomPropertySpecifications = WAIT['DomPropertySpecifications']
  DomSize = WAIT['DomSize']
  DomSlots = WAIT['DomSlots']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DomCustomWidget(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomCustomWidget: a plain Python object standing in
  front of one C++ DomCustomWidget.

  What exists
  -----------

  Every function of Qt's DomCustomWidget that has a ritual and that Python
  can call so far, 40 names in all: 'elementClass', 'setElementClass',
  'hasElementClass', 'clearElementClass', 'elementExtends',
  'setElementExtends', 'hasElementExtends', 'clearElementExtends',
  'elementHeader', 'takeElementHeader', 'setElementHeader',
  'hasElementHeader', 'clearElementHeader', 'elementSizeHint',
  'takeElementSizeHint', 'setElementSizeHint', 'hasElementSizeHint',
  'clearElementSizeHint', 'elementAddPageMethod', 'setElementAddPageMethod',
  'hasElementAddPageMethod', 'clearElementAddPageMethod', 'elementContainer',
  'setElementContainer', 'hasElementContainer', 'clearElementContainer',
  'elementPixmap', 'setElementPixmap', 'hasElementPixmap',
  'clearElementPixmap', 'elementSlots', 'takeElementSlots',
  'setElementSlots', 'hasElementSlots', 'clearElementSlots',
  'elementPropertyspecifications', 'takeElementPropertyspecifications',
  'setElementPropertyspecifications', 'hasElementPropertyspecifications',
  'clearElementPropertyspecifications'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomCustomWidget::~DomCustomWidget()': the destructor: Python never
    removes a C++ DomCustomWidget.
  - Qt's 'void DomCustomWidget::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomCustomWidget::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 48 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomCustomWidget is created at the first use, not by
    'DomCustomWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomCustomWidget.
  - Each name of Qt's DomCustomWidget that has no cute function yet, 'read',
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
  __qt_class__ = 'DomCustomWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def elementClass(self) -> str:
    """
    Calls Qt's 'QString DomCustomWidget::elementClass() const'.

    Qt's own words: https://doc.qt.io/qt-6/domcustomwidget.html#elementClass

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomCustomWidget::elementClass() const
    return self.uglySide.call('ritual_ZNK15DomCustomWidget12elementClassEv')

  def hasElementClass(self) -> bool:
    """
    Calls Qt's 'bool DomCustomWidget::hasElementClass() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#hasElementClass
    """
    #  bool DomCustomWidget::hasElementClass() const
    return self.uglySide.call(
        'ritual_ZNK15DomCustomWidget15hasElementClassEv',
    )

  def elementExtends(self) -> str:
    """
    Calls Qt's 'QString DomCustomWidget::elementExtends() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#elementExtends

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomCustomWidget::elementExtends() const
    return self.uglySide.call(
        'ritual_ZNK15DomCustomWidget14elementExtendsEv',
    )

  def hasElementExtends(self) -> bool:
    """
    Calls Qt's 'bool DomCustomWidget::hasElementExtends() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#hasElementExtends
    """
    #  bool DomCustomWidget::hasElementExtends() const
    return self.uglySide.call(
        'ritual_ZNK15DomCustomWidget17hasElementExtendsEv',
    )

  def elementHeader(self) -> Optional[DomHeader]:
    """
    Calls Qt's 'DomHeader *DomCustomWidget::elementHeader() const'.

    Qt's own words: https://doc.qt.io/qt-6/domcustomwidget.html#elementHeader

    Returns
    -------

    Optional[DomHeader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomHeader *DomCustomWidget::elementHeader() const
    address = self.uglySide.call(
        'ritual_ZNK15DomCustomWidget13elementHeaderEv',
    )
    from . import DomHeader
    return DomHeader._cuteAt(address)

  def hasElementHeader(self) -> bool:
    """
    Calls Qt's 'bool DomCustomWidget::hasElementHeader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#hasElementHeader
    """
    #  bool DomCustomWidget::hasElementHeader() const
    return self.uglySide.call(
        'ritual_ZNK15DomCustomWidget16hasElementHeaderEv',
    )

  def elementSizeHint(self) -> Optional[DomSize]:
    """
    Calls Qt's 'DomSize *DomCustomWidget::elementSizeHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#elementSizeHint

    Returns
    -------

    Optional[DomSize]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomSize *DomCustomWidget::elementSizeHint() const
    address = self.uglySide.call(
        'ritual_ZNK15DomCustomWidget15elementSizeHintEv',
    )
    from . import DomSize
    return DomSize._cuteAt(address)

  def hasElementSizeHint(self) -> bool:
    """
    Calls Qt's 'bool DomCustomWidget::hasElementSizeHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#hasElementSizeHint
    """
    #  bool DomCustomWidget::hasElementSizeHint() const
    return self.uglySide.call(
        'ritual_ZNK15DomCustomWidget18hasElementSizeHintEv',
    )

  def elementAddPageMethod(self) -> str:
    """
    Calls Qt's 'QString DomCustomWidget::elementAddPageMethod() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#elementAddPageMethod

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomCustomWidget::elementAddPageMethod() const
    return self.uglySide.call(
        'ritual_ZNK15DomCustomWidget20elementAddPageMethodEv',
    )

  def hasElementAddPageMethod(self) -> bool:
    """
    Calls Qt's 'bool DomCustomWidget::hasElementAddPageMethod() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#hasElementAddPageMethod
    """
    #  bool DomCustomWidget::hasElementAddPageMethod() const
    return self.uglySide.call(
        'ritual_ZNK15DomCustomWidget23hasElementAddPageMethodEv',
    )

  def elementContainer(self) -> int:
    """
    Calls Qt's 'int DomCustomWidget::elementContainer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#elementContainer
    """
    #  int DomCustomWidget::elementContainer() const
    return self.uglySide.call(
        'ritual_ZNK15DomCustomWidget16elementContainerEv',
    )

  def hasElementContainer(self) -> bool:
    """
    Calls Qt's 'bool DomCustomWidget::hasElementContainer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#hasElementContainer
    """
    #  bool DomCustomWidget::hasElementContainer() const
    return self.uglySide.call(
        'ritual_ZNK15DomCustomWidget19hasElementContainerEv',
    )

  def elementPixmap(self) -> str:
    """
    Calls Qt's 'QString DomCustomWidget::elementPixmap() const'.

    Qt's own words: https://doc.qt.io/qt-6/domcustomwidget.html#elementPixmap

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomCustomWidget::elementPixmap() const
    return self.uglySide.call('ritual_ZNK15DomCustomWidget13elementPixmapEv')

  def hasElementPixmap(self) -> bool:
    """
    Calls Qt's 'bool DomCustomWidget::hasElementPixmap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#hasElementPixmap
    """
    #  bool DomCustomWidget::hasElementPixmap() const
    return self.uglySide.call(
        'ritual_ZNK15DomCustomWidget16hasElementPixmapEv',
    )

  def elementSlots(self) -> Optional[DomSlots]:
    """
    Calls Qt's 'DomSlots *DomCustomWidget::elementSlots() const'.

    Qt's own words: https://doc.qt.io/qt-6/domcustomwidget.html#elementSlots

    Returns
    -------

    Optional[DomSlots]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomSlots *DomCustomWidget::elementSlots() const
    address = self.uglySide.call(
        'ritual_ZNK15DomCustomWidget12elementSlotsEv',
    )
    from . import DomSlots
    return DomSlots._cuteAt(address)

  def hasElementSlots(self) -> bool:
    """
    Calls Qt's 'bool DomCustomWidget::hasElementSlots() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#hasElementSlots
    """
    #  bool DomCustomWidget::hasElementSlots() const
    return self.uglySide.call(
        'ritual_ZNK15DomCustomWidget15hasElementSlotsEv',
    )

  def elementPropertyspecifications(
      self,
  ) -> Optional[DomPropertySpecifications]:
    """
    Calls Qt's 'DomPropertySpecifications
    *DomCustomWidget::elementPropertyspecifications() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#elementPropertyspecifications

    Returns
    -------

    Optional[DomPropertySpecifications]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomPropertySpecifications
    #      *DomCustomWidget::elementPropertyspecifications() const
    address = self.uglySide.call(
        'ritual_ZNK15DomCustomWidget29elementPropertyspecificationsEv',
    )
    from . import DomPropertySpecifications
    return DomPropertySpecifications._cuteAt(address)

  def hasElementPropertyspecifications(self) -> bool:
    """
    Calls Qt's 'bool DomCustomWidget::hasElementPropertyspecifications()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html
    """
    #  bool DomCustomWidget::hasElementPropertyspecifications() const
    return self.uglySide.call(
        'ritual_ZNK15DomCustomWidget32hasElementPropertyspecificationsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setElementClass(self, a: str) -> None:
    """
    Calls Qt's 'void DomCustomWidget::setElementClass(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#setElementClass

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomCustomWidget::setElementClass(const QString &a)
    self.uglySide.call(
        'ritual_ZN15DomCustomWidget15setElementClassERK7QString', a,
    )

  @overload(str)
  def setElementExtends(self, a: str) -> None:
    """
    Calls Qt's 'void DomCustomWidget::setElementExtends(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#setElementExtends

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomCustomWidget::setElementExtends(const QString &a)
    self.uglySide.call(
        'ritual_ZN15DomCustomWidget17setElementExtendsERK7QString', a,
    )

  @overload(DomHeader)
  @overload(NoneType)
  def setElementHeader(self, a: Optional[DomHeader]) -> None:
    """
    Calls Qt's 'void DomCustomWidget::setElementHeader(DomHeader *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#setElementHeader

    Parameters
    ----------

    a : Optional[DomHeader]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomCustomWidget::setElementHeader(DomHeader *a)
    self.uglySide.call(
        'ritual_ZN15DomCustomWidget16setElementHeaderEP9DomHeader',
        self._addressOf(a),
    )

  @overload(DomSize)
  @overload(NoneType)
  def setElementSizeHint(self, a: Optional[DomSize]) -> None:
    """
    Calls Qt's 'void DomCustomWidget::setElementSizeHint(DomSize *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#setElementSizeHint

    Parameters
    ----------

    a : Optional[DomSize]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomCustomWidget::setElementSizeHint(DomSize *a)
    self.uglySide.call(
        'ritual_ZN15DomCustomWidget18setElementSizeHintEP7DomSize',
        self._addressOf(a),
    )

  @overload(str)
  def setElementAddPageMethod(self, a: str) -> None:
    """
    Calls Qt's 'void DomCustomWidget::setElementAddPageMethod(const QString
    &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#setElementAddPageMethod

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomCustomWidget::setElementAddPageMethod(const QString &a)
    self.uglySide.call(
        'ritual_ZN15DomCustomWidget23setElementAddPageMethodERK7QString', a,
    )

  @overload(int)
  def setElementContainer(self, a: int) -> None:
    """
    Calls Qt's 'void DomCustomWidget::setElementContainer(int a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#setElementContainer

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomCustomWidget::setElementContainer(int a)
    self.uglySide.call(
        'ritual_ZN15DomCustomWidget19setElementContainerEi', a,
    )

  @overload(str)
  def setElementPixmap(self, a: str) -> None:
    """
    Calls Qt's 'void DomCustomWidget::setElementPixmap(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#setElementPixmap

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomCustomWidget::setElementPixmap(const QString &a)
    self.uglySide.call(
        'ritual_ZN15DomCustomWidget16setElementPixmapERK7QString', a,
    )

  @overload(DomSlots)
  @overload(NoneType)
  def setElementSlots(self, a: Optional[DomSlots]) -> None:
    """
    Calls Qt's 'void DomCustomWidget::setElementSlots(DomSlots *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#setElementSlots

    Parameters
    ----------

    a : Optional[DomSlots]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomCustomWidget::setElementSlots(DomSlots *a)
    self.uglySide.call(
        'ritual_ZN15DomCustomWidget15setElementSlotsEP8DomSlots',
        self._addressOf(a),
    )

  @overload(DomPropertySpecifications)
  @overload(NoneType)
  def setElementPropertyspecifications(
      self,
      a: Optional[DomPropertySpecifications],
  ) -> None:
    """
    Calls Qt's 'void DomCustomWidget::setElementPropertyspecifications(
    DomPropertySpecifications *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html

    Parameters
    ----------

    a : Optional[DomPropertySpecifications]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomCustomWidget::setElementPropertyspecifications(
    #      DomPropertySpecifications *a)
    self.uglySide.call(
        'ritual_ZN15DomCustomWidget32setElementPropertyspecificationsEP25Do'
        'mPropertySpecifications',
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
    Notes what was given, for Qt's 'DomCustomWidget::DomCustomWidget()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#DomCustomWidget
    """
    #  DomCustomWidget::DomCustomWidget()
    self._noteCreation(DomCustomWidget, lambda: Rituals.call(
        'ritual_ZN15DomCustomWidgetC1Ev',
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

  def clearElementClass(self) -> None:
    """
    Calls Qt's 'void DomCustomWidget::clearElementClass()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#clearElementClass
    """
    #  void DomCustomWidget::clearElementClass()
    self.uglySide.call('ritual_ZN15DomCustomWidget17clearElementClassEv')

  def clearElementExtends(self) -> None:
    """
    Calls Qt's 'void DomCustomWidget::clearElementExtends()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#clearElementExtends
    """
    #  void DomCustomWidget::clearElementExtends()
    self.uglySide.call('ritual_ZN15DomCustomWidget19clearElementExtendsEv')

  def takeElementHeader(self) -> Optional[DomHeader]:
    """
    Calls Qt's 'DomHeader *DomCustomWidget::takeElementHeader()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#takeElementHeader

    Returns
    -------

    Optional[DomHeader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomHeader *DomCustomWidget::takeElementHeader()
    address = self.uglySide.call(
        'ritual_ZN15DomCustomWidget17takeElementHeaderEv',
    )
    from . import DomHeader
    return DomHeader._cuteAt(address)

  def clearElementHeader(self) -> None:
    """
    Calls Qt's 'void DomCustomWidget::clearElementHeader()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#clearElementHeader
    """
    #  void DomCustomWidget::clearElementHeader()
    self.uglySide.call('ritual_ZN15DomCustomWidget18clearElementHeaderEv')

  def takeElementSizeHint(self) -> Optional[DomSize]:
    """
    Calls Qt's 'DomSize *DomCustomWidget::takeElementSizeHint()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#takeElementSizeHint

    Returns
    -------

    Optional[DomSize]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomSize *DomCustomWidget::takeElementSizeHint()
    address = self.uglySide.call(
        'ritual_ZN15DomCustomWidget19takeElementSizeHintEv',
    )
    from . import DomSize
    return DomSize._cuteAt(address)

  def clearElementSizeHint(self) -> None:
    """
    Calls Qt's 'void DomCustomWidget::clearElementSizeHint()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#clearElementSizeHint
    """
    #  void DomCustomWidget::clearElementSizeHint()
    self.uglySide.call('ritual_ZN15DomCustomWidget20clearElementSizeHintEv')

  def clearElementAddPageMethod(self) -> None:
    """
    Calls Qt's 'void DomCustomWidget::clearElementAddPageMethod()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#clearElementAddPageMethod
    """
    #  void DomCustomWidget::clearElementAddPageMethod()
    self.uglySide.call(
        'ritual_ZN15DomCustomWidget25clearElementAddPageMethodEv',
    )

  def clearElementContainer(self) -> None:
    """
    Calls Qt's 'void DomCustomWidget::clearElementContainer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#clearElementContainer
    """
    #  void DomCustomWidget::clearElementContainer()
    self.uglySide.call('ritual_ZN15DomCustomWidget21clearElementContainerEv')

  def clearElementPixmap(self) -> None:
    """
    Calls Qt's 'void DomCustomWidget::clearElementPixmap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#clearElementPixmap
    """
    #  void DomCustomWidget::clearElementPixmap()
    self.uglySide.call('ritual_ZN15DomCustomWidget18clearElementPixmapEv')

  def takeElementSlots(self) -> Optional[DomSlots]:
    """
    Calls Qt's 'DomSlots *DomCustomWidget::takeElementSlots()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#takeElementSlots

    Returns
    -------

    Optional[DomSlots]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomSlots *DomCustomWidget::takeElementSlots()
    address = self.uglySide.call(
        'ritual_ZN15DomCustomWidget16takeElementSlotsEv',
    )
    from . import DomSlots
    return DomSlots._cuteAt(address)

  def clearElementSlots(self) -> None:
    """
    Calls Qt's 'void DomCustomWidget::clearElementSlots()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html#clearElementSlots
    """
    #  void DomCustomWidget::clearElementSlots()
    self.uglySide.call('ritual_ZN15DomCustomWidget17clearElementSlotsEv')

  def takeElementPropertyspecifications(
      self,
  ) -> Optional[DomPropertySpecifications]:
    """
    Calls Qt's 'DomPropertySpecifications
    *DomCustomWidget::takeElementPropertyspecifications()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html

    Returns
    -------

    Optional[DomPropertySpecifications]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomPropertySpecifications
    #      *DomCustomWidget::takeElementPropertyspecifications()
    address = self.uglySide.call(
        'ritual_ZN15DomCustomWidget33takeElementPropertyspecificationsEv',
    )
    from . import DomPropertySpecifications
    return DomPropertySpecifications._cuteAt(address)

  def clearElementPropertyspecifications(self) -> None:
    """
    Calls Qt's 'void DomCustomWidget::clearElementPropertyspecifications()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidget.html
    """
    #  void DomCustomWidget::clearElementPropertyspecifications()
    self.uglySide.call(
        'ritual_ZN15DomCustomWidget34clearElementPropertyspecificationsEv',
    )

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomCustomWidget::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomCustomWidget.read' has no cute function yet. Qt's 'void "
        "DomCustomWidget::read(QXmlStreamReader &reader)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomCustomWidget::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomCustomWidget.write' has no cute function yet. Qt's 'void "
        "DomCustomWidget::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<DomCustomWidget *>': the list of DomCustomWidget, which
#  'QList[DomCustomWidget]' gives. It is made here, so that there is one as
#  soon as there can be a DomCustomWidget.
QList.createKind(
    DomCustomWidget, 'address',
    make='ritual_list_make_DomCustomWidget_ptr',
    add='ritual_list_add_DomCustomWidget_ptr',
    size='ritual_list_size_DomCustomWidget_ptr',
    at='ritual_list_at_DomCustomWidget_ptr',
    drop='ritual_list_drop_DomCustomWidget_ptr',
)
