"""
qdesigner_internal::QDesignerDnDItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_dnditem_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::QDesignerDnDItem to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QDesignerDnDItemInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint
  from ..QtWidgets import QWidget
  from . import DomUI
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomUI = WAIT['DomUI']
  QPoint = WAIT['QPoint']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerDnDItem(QDesignerDnDItemInterface):
  """
  The cute side of Qt's qdesigner_internal::QDesignerDnDItem: a plain Python
  object standing in front of one C++ qdesigner_internal::QDesignerDnDItem.

  It is built on the cute 'QDesignerDnDItemInterface', as Qt's
  qdesigner_internal::QDesignerDnDItem is built on Qt's
  QDesignerDnDItemInterface, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::QDesignerDnDItem that has a
  ritual and that Python can call so far, 8 names in all: 'domUi',
  'decoration', 'widget', 'hotSpot', 'source', 'type', 'setDomUi', 'init'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::QDesignerDnDItem::~QDesignerDnDItem()': the
    destructor: Python never removes a C++
    qdesigner_internal::QDesignerDnDItem.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ qdesigner_internal::QDesignerDnDItem is created at the first use,
    not by 'qdesigner_internal::QDesignerDnDItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::QDesignerDnDItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::QDesignerDnDItem'

  #  A C++ qdesigner_internal::QDesignerDnDItem Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_QDesignerDnDItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def domUi(self) -> Optional[DomUI]:
    """
    Calls Qt's 'DomUI *qdesigner_internal::QDesignerDnDItem::domUi() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerdnditem.html#domUi

    Returns
    -------

    Optional[DomUI]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomUI *qdesigner_internal::QDesignerDnDItem::domUi() const
    ritual = 'ritual_ZNK18qdesigner_internal16QDesignerDnDItem5domUiEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18qdesigner_internal16QDesignerDnDItem5domUiEv'
    address = self.uglySide.call(ritual)
    from . import DomUI
    return DomUI._cuteAt(address)

  def decoration(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *qdesigner_internal::QDesignerDnDItem::decoration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerdnditem.html

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::QDesignerDnDItem::decoration() const
    ritual = 'ritual_ZNK18qdesigner_internal16QDesignerDnDItem10decorationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal16QDesignerDnDItem10decoration'
          'Ev')
    address = self.uglySide.call(ritual)
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  def widget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *qdesigner_internal::QDesignerDnDItem::widget()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerdnditem.html#widget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::QDesignerDnDItem::widget() const
    ritual = 'ritual_ZNK18qdesigner_internal16QDesignerDnDItem6widgetEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal16QDesignerDnDItem6widgetEv')
    address = self.uglySide.call(ritual)
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  def hotSpot(self) -> QPoint:
    """
    Calls Qt's 'QPoint qdesigner_internal::QDesignerDnDItem::hotSpot()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerdnditem.html#hotSpot

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint qdesigner_internal::QDesignerDnDItem::hotSpot() const
    ritual = 'ritual_ZNK18qdesigner_internal16QDesignerDnDItem7hotSpotEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal16QDesignerDnDItem7hotSpotEv')
    address = self.uglySide.call(ritual)
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def source(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *qdesigner_internal::QDesignerDnDItem::source()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerdnditem.html#source

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::QDesignerDnDItem::source() const
    ritual = 'ritual_ZNK18qdesigner_internal16QDesignerDnDItem6sourceEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal16QDesignerDnDItem6sourceEv')
    address = self.uglySide.call(ritual)
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  def type(self) -> QDesignerDnDItemInterface.DropType:
    """
    Calls Qt's 'DropType qdesigner_internal::QDesignerDnDItem::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerdnditem.html#type

    Returns
    -------

    QDesignerDnDItemInterface.DropType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDesignerDnDItemInterface.DropType(number)' gives.
    """
    #  DropType qdesigner_internal::QDesignerDnDItem::type() const
    ritual = 'ritual_ZNK18qdesigner_internal16QDesignerDnDItem4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18qdesigner_internal16QDesignerDnDItem4typeEv'
    return QDesignerDnDItemInterface.DropType(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(DomUI)
  @overload(NoneType)
  def setDomUi(self, dom_ui: Optional[DomUI]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::QDesignerDnDItem::setDomUi(DomUI
    *dom_ui)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerdnditem.html#setDomUi

    Parameters
    ----------

    dom_ui : Optional[DomUI]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::QDesignerDnDItem::setDomUi(DomUI *dom_ui)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal16QDesignerDnDItem8setDomUiEP5DomUI',
        self._addressOf(dom_ui),
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

  @overload(QDesignerDnDItemInterface.DropType)
  @overload(QDesignerDnDItemInterface.DropType, QWidget)
  @overload(QDesignerDnDItemInterface.DropType, NoneType)
  def __init__(
      self,
      type: QDesignerDnDItemInterface.DropType,
      source: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::QDesignerDnDItem::QDesignerDnDItem(DropType type,
    QWidget *source)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerdnditem.html

    Parameters
    ----------

    type : QDesignerDnDItemInterface.DropType
      Passed on as its number.

    source : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qdesigner_internal::QDesignerDnDItem::QDesignerDnDItem(DropType type,
    #      QWidget *source)
    self._noteCreation(QDesignerDnDItem, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal16QDesignerDnDItemC1EN25QDesignerDnDI'
        'temInterface8DropTypeEP7QWidget',
        type.value, self._addressOf(source),
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

  @overload(DomUI, QWidget, QWidget, QPoint)
  @overload(DomUI, QWidget, NoneType, QPoint)
  @overload(DomUI, NoneType, QWidget, QPoint)
  @overload(DomUI, NoneType, NoneType, QPoint)
  @overload(NoneType, QWidget, QWidget, QPoint)
  @overload(NoneType, QWidget, NoneType, QPoint)
  @overload(NoneType, NoneType, QWidget, QPoint)
  @overload(NoneType, NoneType, NoneType, QPoint)
  def init(
      self,
      ui: Optional[DomUI],
      widget: Optional[QWidget],
      decoration: Optional[QWidget],
      global_mouse_pos: QPoint,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::QDesignerDnDItem::init(DomUI *ui,
    QWidget *widget, QWidget *decoration, const QPoint &global_mouse_pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerdnditem.html#init

    Parameters
    ----------

    ui : Optional[DomUI]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    decoration : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    global_mouse_pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void qdesigner_internal::QDesignerDnDItem::init(DomUI *ui, QWidget
    #      *widget, QWidget *decoration, const QPoint &global_mouse_pos)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal16QDesignerDnDItem4initEP5DomUIP7QWid'
        'getS4_RK6QPoint',
        self._addressOf(ui), self._addressOf(widget),
        self._addressOf(decoration), self._valueOf(global_mouse_pos),
    )
