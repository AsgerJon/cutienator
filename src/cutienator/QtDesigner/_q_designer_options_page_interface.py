"""
QDesignerOptionsPageInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractoptionspage.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtWidgets import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerOptionsPageInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerOptionsPageInterface: a plain Python object
  standing in front of one C++ QDesignerOptionsPageInterface.

  What exists
  -----------

  Every function of Qt's QDesignerOptionsPageInterface that has a ritual and
  that Python can call so far, 4 names in all: 'name', 'createPage', 'apply',
  'finish'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDesignerOptionsPageInterface::~QDesignerOptionsPageInterface()':
    the destructor: Python never removes a C++ QDesignerOptionsPageInterface.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QDesignerOptionsPageInterface is created at the first use, not by
    'QDesignerOptionsPageInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerOptionsPageInterface.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerOptionsPageInterface'

  #  A C++ QDesignerOptionsPageInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerOptionsPageInterface'

  #  The functions Qt calls itself that QDesignerOptionsPageInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'name': (
          ('_ZNK29QDesignerOptionsPageInterface4nameEv',
           ('address', 'text', ''),
           ()),
      ),
      'createPage': (
          ('_ZN29QDesignerOptionsPageInterface10createPageEP7QWidget',
           ('address', 'address', 'QtWidgets:QWidget'),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'apply': (
          ('_ZN29QDesignerOptionsPageInterface5applyEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'finish': (
          ('_ZN29QDesignerOptionsPageInterface6finishEv',
           ('nothing', 'nothing', ''),
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

  def name(self) -> str:
    """
    Calls Qt's 'QString QDesignerOptionsPageInterface::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigneroptionspageinterface.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerOptionsPageInterface::name() const
    return self.uglySide.call(
        'ritual_ZNK29QDesignerOptionsPageInterface4nameEv',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QDesignerOptionsPageInterface::QDesignerOptionsPageInterface()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigneroptionspageinterface.html
    """
    #  QDesignerOptionsPageInterface::QDesignerOptionsPageInterface()
    self._noteCreation(QDesignerOptionsPageInterface, lambda: Rituals.call(
        'ritual_ZN29QDesignerOptionsPageInterfaceC1Ev',
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

  @overload(QWidget)
  @overload(NoneType)
  def createPage(self, parent: Optional[QWidget]) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QDesignerOptionsPageInterface::createPage(QWidget
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigneroptionspageinterface.html#createPage

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QDesignerOptionsPageInterface::createPage(QWidget *parent)
    address = self.uglySide.call(
        'ritual_ZN29QDesignerOptionsPageInterface10createPageEP7QWidget',
        self._addressOf(parent),
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  def apply(self) -> None:
    """
    Calls Qt's 'void QDesignerOptionsPageInterface::apply()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigneroptionspageinterface.html#apply
    """
    #  void QDesignerOptionsPageInterface::apply()
    self.uglySide.call('ritual_ZN29QDesignerOptionsPageInterface5applyEv')

  def finish(self) -> None:
    """
    Calls Qt's 'void QDesignerOptionsPageInterface::finish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigneroptionspageinterface.html#finish
    """
    #  void QDesignerOptionsPageInterface::finish()
    self.uglySide.call('ritual_ZN29QDesignerOptionsPageInterface6finishEv')


#  Qt's 'QList<QDesignerOptionsPageInterface *>': the list of
#  QDesignerOptionsPageInterface, which
#  'QList[QDesignerOptionsPageInterface]' gives. It is made here, so that
#  there is one as soon as there can be a QDesignerOptionsPageInterface.
QList.createKind(
    QDesignerOptionsPageInterface, 'address',
    make='ritual_list_make_QDesignerOptionsPageInterface_ptr',
    add='ritual_list_add_QDesignerOptionsPageInterface_ptr',
    size='ritual_list_size_QDesignerOptionsPageInterface_ptr',
    at='ritual_list_at_QDesignerOptionsPageInterface_ptr',
    drop='ritual_list_drop_QDesignerOptionsPageInterface_ptr',
)
