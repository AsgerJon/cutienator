"""
RequiredPropertyKey binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlobjectcreator_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means RequiredPropertyKey to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QQmlPropertyData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlPropertyData = WAIT['QQmlPropertyData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class RequiredPropertyKey(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's RequiredPropertyKey: a plain Python object standing
  in front of one C++ RequiredPropertyKey.

  C++ hands a RequiredPropertyKey around as a copy, so every C++
  RequiredPropertyKey behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's RequiredPropertyKey that has a ritual and that
  Python can call so far, 1 name in all: '__eq__'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'RequiredPropertyKey::~RequiredPropertyKey()': the destructor:
    Python removes its C++ RequiredPropertyKey by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ RequiredPropertyKey is created at the first use, not by
    'RequiredPropertyKey(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a RequiredPropertyKey back gives a copy the ritual made
    for Python, in a new cute RequiredPropertyKey.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'RequiredPropertyKey'

  #  Qt's '~RequiredPropertyKey()'. Naming it makes this a value class:
  #  Python owns every C++ RequiredPropertyKey behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19RequiredPropertyKeyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: RequiredPropertyKey) -> bool:
    """
    Calls Qt's 'bool operator==(const RequiredPropertyKey &a, const
    RequiredPropertyKey &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/requiredpropertykey.html#operator==

    Parameters
    ----------

    b : RequiredPropertyKey
      Passed on as a value: Qt reads the C++ RequiredPropertyKey, which stays
      Python's own.
    """
    #  bool operator==(const RequiredPropertyKey &a, const
    #      RequiredPropertyKey &b)
    return Rituals.call(
        'ritual_ZeqRK19RequiredPropertyKeyS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'RequiredPropertyKey::RequiredPropertyKey()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/requiredpropertykey.html#RequiredPropertyKey
    """
    #  RequiredPropertyKey::RequiredPropertyKey()
    self._noteCreation(RequiredPropertyKey, lambda: Rituals.call(
        'ritual_ZN19RequiredPropertyKeyC1Ev',
    ))

  @overload(QObject, QQmlPropertyData)
  @overload(QObject, NoneType)
  @overload(NoneType, QQmlPropertyData)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      object: Optional[QObject],
      data: Optional[QQmlPropertyData],
  ) -> None:
    """
    Notes what was given, for Qt's
    'RequiredPropertyKey::RequiredPropertyKey(const QObject *object, const
    QQmlPropertyData *data)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/requiredpropertykey.html#RequiredPropertyKey

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    data : Optional[QQmlPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  RequiredPropertyKey::RequiredPropertyKey(const QObject *object, const
    #      QQmlPropertyData *data)
    self._noteCreation(RequiredPropertyKey, lambda: Rituals.call(
        'ritual_ZN19RequiredPropertyKeyC1EPK7QObjectPK16QQmlPropertyData',
        self._addressOf(object, 'QObject'), self._addressOf(data),
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
