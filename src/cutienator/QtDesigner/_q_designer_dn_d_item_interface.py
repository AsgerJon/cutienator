"""
QDesignerDnDItemInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractdnditem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint
  from ..QtWidgets import QWidget
  from . import DomUI


class QDesignerDnDItemInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerDnDItemInterface: a plain Python object
  standing in front of one C++ QDesignerDnDItemInterface.

  What exists
  -----------

  Every function of Qt's QDesignerDnDItemInterface that has a ritual and that
  Python can call so far, 6 names in all: 'domUi', 'widget', 'decoration',
  'hotSpot', 'type', 'source'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDesignerDnDItemInterface::~QDesignerDnDItemInterface()': the
    destructor: Python never removes a C++ QDesignerDnDItemInterface.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QDesignerDnDItemInterface is created at the first use, not by
    'QDesignerDnDItemInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerDnDItemInterface.
  """

  #  The enums Qt writes inside QDesignerDnDItemInterface, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class DropType(CuteNum):
    """
    The enum 'QDesignerDnDItemInterface::DropType' of Qt, with the 2 names Qt
    gives in it.
    """

    MoveDrop = Kee[int](0)
    CopyDrop = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerDnDItemInterface'

  #  A C++ QDesignerDnDItemInterface Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerDnDItemInterface'

  #  The functions Qt calls itself that QDesignerDnDItemInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'domUi': (
          ('_ZNK25QDesignerDnDItemInterface5domUiEv',
           ('address', 'address', 'QtDesigner:DomUI'),
           ()),
      ),
      'widget': (
          ('_ZNK25QDesignerDnDItemInterface6widgetEv',
           ('address', 'address', 'QtWidgets:QWidget'),
           ()),
      ),
      'decoration': (
          ('_ZNK25QDesignerDnDItemInterface10decorationEv',
           ('address', 'address', 'QtWidgets:QWidget'),
           ()),
      ),
      'hotSpot': (
          ('_ZNK25QDesignerDnDItemInterface7hotSpotEv',
           ('address', 'value', 'QtCore:QPoint'),
           ()),
      ),
      'type': (
          ('_ZNK25QDesignerDnDItemInterface4typeEv',
           ('int', 'enum', 'QtDesigner:QDesignerDnDItemInterface.DropType'),
           ()),
      ),
      'source': (
          ('_ZNK25QDesignerDnDItemInterface6sourceEv',
           ('address', 'address', 'QtWidgets:QWidget'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def domUi(self) -> Optional[DomUI]:
    """
    Calls Qt's 'DomUI *QDesignerDnDItemInterface::domUi() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdnditeminterface.html#domUi

    Returns
    -------

    Optional[DomUI]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomUI *QDesignerDnDItemInterface::domUi() const
    address = self.uglySide.call(
        'ritual_ZNK25QDesignerDnDItemInterface5domUiEv',
    )
    from . import DomUI
    return DomUI._cuteAt(address)

  def widget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QDesignerDnDItemInterface::widget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdnditeminterface.html#widget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QDesignerDnDItemInterface::widget() const
    address = self.uglySide.call(
        'ritual_ZNK25QDesignerDnDItemInterface6widgetEv',
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  def decoration(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QDesignerDnDItemInterface::decoration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdnditeminterface.html#decoration

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QDesignerDnDItemInterface::decoration() const
    address = self.uglySide.call(
        'ritual_ZNK25QDesignerDnDItemInterface10decorationEv',
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  def hotSpot(self) -> QPoint:
    """
    Calls Qt's 'QPoint QDesignerDnDItemInterface::hotSpot() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdnditeminterface.html#hotSpot

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QDesignerDnDItemInterface::hotSpot() const
    address = self.uglySide.call(
        'ritual_ZNK25QDesignerDnDItemInterface7hotSpotEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def type(self) -> DropType:
    """
    Calls Qt's 'DropType QDesignerDnDItemInterface::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdnditeminterface.html#type

    Returns
    -------

    DropType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DropType(number)' gives.
    """
    #  DropType QDesignerDnDItemInterface::type() const
    return QDesignerDnDItemInterface.DropType(self.uglySide.call(
        'ritual_ZNK25QDesignerDnDItemInterface4typeEv',
    ))

  def source(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QDesignerDnDItemInterface::source() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdnditeminterface.html#source

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QDesignerDnDItemInterface::source() const
    address = self.uglySide.call(
        'ritual_ZNK25QDesignerDnDItemInterface6sourceEv',
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

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
    'QDesignerDnDItemInterface::QDesignerDnDItemInterface()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdnditeminterface.html
    """
    #  QDesignerDnDItemInterface::QDesignerDnDItemInterface()
    self._noteCreation(QDesignerDnDItemInterface, lambda: Rituals.call(
        'ritual_ZN25QDesignerDnDItemInterfaceC1Ev',
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


#  Qt's 'QList<QDesignerDnDItemInterface *>': the list of
#  QDesignerDnDItemInterface, which 'QList[QDesignerDnDItemInterface]' gives.
#  It is made here, so that there is one as soon as there can be a
#  QDesignerDnDItemInterface.
QList.createKind(
    QDesignerDnDItemInterface, 'address',
    make='ritual_list_make_QDesignerDnDItemInterface_ptr',
    add='ritual_list_add_QDesignerDnDItemInterface_ptr',
    size='ritual_list_size_QDesignerDnDItemInterface_ptr',
    at='ritual_list_at_QDesignerDnDItemInterface_ptr',
    drop='ritual_list_drop_QDesignerDnDItemInterface_ptr',
)
