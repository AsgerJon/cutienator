"""
QPlatformKeyMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformkeymapper.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import Qt, QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QKeyCombination
  from . import QKeyEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QKeyEvent = WAIT['QKeyEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformKeyMapper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformKeyMapper: a plain Python object standing in
  front of one C++ QPlatformKeyMapper.

  C++ hands a QPlatformKeyMapper around as a copy, so every C++
  QPlatformKeyMapper behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlatformKeyMapper that has a ritual and that Python
  can call so far, 2 names in all: 'possibleKeyCombinations',
  'queryKeyboardModifiers'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformKeyMapper::~QPlatformKeyMapper()': the destructor: Python
    removes its C++ QPlatformKeyMapper by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QPlatformKeyMapper is created at the first use, not by
    'QPlatformKeyMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlatformKeyMapper back gives a copy the ritual made
    for Python, in a new cute QPlatformKeyMapper.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformKeyMapper'

  #  A C++ QPlatformKeyMapper Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformKeyMapper'

  #  The functions Qt calls itself that QPlatformKeyMapper is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'possibleKeyCombinations': (
          'QList<QKeyCombination> '
          'QPlatformKeyMapper::possibleKeyCombinations(const QKeyEvent *) '
          'const',
      ),
  }

  #  The functions Qt calls itself that QPlatformKeyMapper is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'queryKeyboardModifiers': (
          ('_ZNK18QPlatformKeyMapper22queryKeyboardModifiersEv',
           ('int', 'flags', 'QtCore:Qt.KeyboardModifier'),
           ()),
      ),
  }

  #  Qt's '~QPlatformKeyMapper()'. Naming it makes this a value class: Python
  #  owns every C++ QPlatformKeyMapper behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QPlatformKeyMapperD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QKeyEvent)
  @overload(NoneType)
  def possibleKeyCombinations(
      self,
      event: Optional[QKeyEvent],
  ) -> QList[QKeyCombination]:
    """
    Calls Qt's 'QList<QKeyCombination>
    QPlatformKeyMapper::possibleKeyCombinations(const QKeyEvent *event)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformkeymapper.html#possibleKeyCombinations

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QKeyCombination]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QKeyCombination>
    #      QPlatformKeyMapper::possibleKeyCombinations(const QKeyEvent
    #      *event) const
    address = self.uglySide.call(
        'ritual_ZNK18QPlatformKeyMapper23possibleKeyCombinationsEPK9QKeyEve'
        'nt',
        self._addressOf(event),
    )
    from ..QtCore import QKeyCombination
    return QList[QKeyCombination]._cuteOwning(address)

  def queryKeyboardModifiers(self) -> Qt.KeyboardModifiers:
    """
    Calls Qt's 'Qt::KeyboardModifiers
    QPlatformKeyMapper::queryKeyboardModifiers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformkeymapper.html#queryKeyboardModifiers

    Returns
    -------

    Qt.KeyboardModifiers
      The value standing for the combination Qt gave back.
    """
    #  Qt::KeyboardModifiers QPlatformKeyMapper::queryKeyboardModifiers()
    #      const
    ritual = 'ritual_ZNK18QPlatformKeyMapper22queryKeyboardModifiersEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QPlatformKeyMapper22queryKeyboardModifiersEv'
    return Qt.KeyboardModifiers(self.uglySide.call(ritual))

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
