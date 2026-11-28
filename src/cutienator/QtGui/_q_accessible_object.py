"""
QAccessibleObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qaccessibleobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAccessible, QAccessibleInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QRect
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleObject(QAccessibleInterface):
  """
  The cute side of Qt's QAccessibleObject: a plain Python object standing in
  front of one C++ QAccessibleObject.

  It is built on the cute 'QAccessibleInterface', as Qt's QAccessibleObject
  is built on Qt's QAccessibleInterface, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleObject that has a ritual and that Python
  can call so far, 5 names in all: 'isValid', 'object', 'rect', 'setText',
  'childAt'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleObject::~QAccessibleObject()': the destructor: Python
    never removes a C++ QAccessibleObject.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QAccessibleObject is created at the first use, not by
    'QAccessibleObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleObject.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleObject'

  #  A C++ QAccessibleObject Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleObject::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleobject.html#isValid
    """
    #  bool QAccessibleObject::isValid() const
    ritual = 'ritual_ZNK17QAccessibleObject7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QAccessibleObject7isValidEv'
    return self._callAs('QAccessibleObject', ritual)

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QAccessibleObject::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleobject.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QAccessibleObject::object() const
    ritual = 'ritual_ZNK17QAccessibleObject6objectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QAccessibleObject6objectEv'
    address = self._callAs('QAccessibleObject', ritual)
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def rect(self) -> QRect:
    """
    Calls Qt's 'QRect QAccessibleObject::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleobject.html#rect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QAccessibleObject::rect() const
    ritual = 'ritual_ZNK17QAccessibleObject4rectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QAccessibleObject4rectEv'
    address = self._callAs('QAccessibleObject', ritual)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(int, int)
  def childAt(self, x: int, y: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleObject::childAt(int x, int
    y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleobject.html#childAt

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
    ritual = 'ritual_ZNK17QAccessibleObject7childAtEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QAccessibleObject7childAtEii'
    address = self._callAs('QAccessibleObject', ritual, x, y)
    return QAccessibleInterface._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAccessible.Text, str)
  def setText(self, t: QAccessible.Text, text: str) -> None:
    """
    Calls Qt's 'void QAccessibleObject::setText(QAccessible::Text t, const
    QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibleobject.html#setText

    Parameters
    ----------

    t : QAccessible.Text
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAccessibleObject::setText(QAccessible::Text t, const QString
    #      &text)
    ritual = (
        'ritual_ZN17QAccessibleObject7setTextEN11QAccessible4TextERK7QStrin'
        'g')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAccessibleObject7setTextEN11QAccessible4TextERK7'
          'QString')
    self._callAs('QAccessibleObject', ritual, t.value, text)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, object: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleObject::QAccessibleObject(QObject *object)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibleobject.html#QAccessibleObject

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessibleObject::QAccessibleObject(QObject *object)
    self._noteCreation(QAccessibleObject, lambda: Rituals.call(
        'ritual_ZN17QAccessibleObjectC1EP7QObject',
        self._addressOf(object, 'QObject'),
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
