"""
QAccessibleViewportInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPointF, QSizeF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']


class QAccessibleViewportInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAccessibleViewportInterface: a plain Python object
  standing in front of one C++ QAccessibleViewportInterface.

  What exists
  -----------

  Every function of Qt's QAccessibleViewportInterface that has a ritual and
  that Python can call so far, 5 names in all: 'contentSize', 'position',
  'viewportSize', 'isIndexed', 'setPosition'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleViewportInterface::~QAccessibleViewportInterface()': the
    destructor: Python never removes a C++ QAccessibleViewportInterface.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QAccessibleViewportInterface is created at the first use, not by
    'QAccessibleViewportInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleViewportInterface.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleViewportInterface'

  #  A C++ QAccessibleViewportInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleViewportInterface'

  #  The functions Qt calls itself that QAccessibleViewportInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'contentSize': (
          ('_ZNK28QAccessibleViewportInterface11contentSizeEv',
           ('address', 'value', 'QtCore:QSizeF'),
           ()),
      ),
      'position': (
          ('_ZNK28QAccessibleViewportInterface8positionEv',
           ('address', 'value', 'QtCore:QPointF'),
           ()),
      ),
      'viewportSize': (
          ('_ZNK28QAccessibleViewportInterface12viewportSizeEv',
           ('address', 'value', 'QtCore:QSizeF'),
           ()),
      ),
      'isIndexed': (
          ('_ZNK28QAccessibleViewportInterface9isIndexedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setPosition': (
          ('_ZN28QAccessibleViewportInterface11setPositionE7QPointF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def contentSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QAccessibleViewportInterface::contentSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleviewportinterface.html#contentSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QAccessibleViewportInterface::contentSize() const
    address = self._callAs(
        'QAccessibleViewportInterface',
        'ritual_ZNK28QAccessibleViewportInterface11contentSizeEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def position(self) -> QPointF:
    """
    Calls Qt's 'QPointF QAccessibleViewportInterface::position() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleviewportinterface.html#position

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QAccessibleViewportInterface::position() const
    address = self._callAs(
        'QAccessibleViewportInterface',
        'ritual_ZNK28QAccessibleViewportInterface8positionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def viewportSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QAccessibleViewportInterface::viewportSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleviewportinterface.html#viewportSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QAccessibleViewportInterface::viewportSize() const
    address = self._callAs(
        'QAccessibleViewportInterface',
        'ritual_ZNK28QAccessibleViewportInterface12viewportSizeEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def isIndexed(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleViewportInterface::isIndexed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleviewportinterface.html#isIndexed
    """
    #  bool QAccessibleViewportInterface::isIndexed() const
    return self._callAs(
        'QAccessibleViewportInterface',
        'ritual_ZNK28QAccessibleViewportInterface9isIndexedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setPosition(self, position: QPointF) -> None:
    """
    Calls Qt's 'void QAccessibleViewportInterface::setPosition(QPointF
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleviewportinterface.html#setPosition

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QAccessibleViewportInterface::setPosition(QPointF position)
    self._callAs(
        'QAccessibleViewportInterface',
        'ritual_ZN28QAccessibleViewportInterface11setPositionE7QPointF',
        self._valueOf(position, 'QPointF'),
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
    Notes what was given, for Qt's
    'QAccessibleViewportInterface::QAccessibleViewportInterface()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleviewportinterface.html
    """
    #  QAccessibleViewportInterface::QAccessibleViewportInterface()
    self._noteCreation(QAccessibleViewportInterface, lambda: Rituals.call(
        'ritual_ZN28QAccessibleViewportInterfaceC1Ev',
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
