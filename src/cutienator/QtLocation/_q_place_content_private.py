"""
QPlaceContentPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qplacecontent_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QPlaceContentPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QSharedData
from . import QPlaceContent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlaceContentPrivate(QSharedData):
  """
  The cute side of Qt's QPlaceContentPrivate: a plain Python object standing
  in front of one C++ QPlaceContentPrivate.

  It is built on the cute 'QSharedData', as Qt's QPlaceContentPrivate is
  built on Qt's QSharedData, and has everything that class has.

  C++ hands a QPlaceContentPrivate around as a copy, so every C++
  QPlaceContentPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlaceContentPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'compare', 'type'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlaceContentPrivate::~QPlaceContentPrivate()': the destructor:
    Python removes its C++ QPlaceContentPrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QPlaceContentPrivate is created at the first use, not by
    'QPlaceContentPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlaceContentPrivate back gives a copy the ritual
    made for Python, in a new cute QPlaceContentPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaceContentPrivate'

  #  Qt's '~QPlaceContentPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QPlaceContentPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QPlaceContentPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  @overload(NoneType)
  def compare(self, other: Optional[QPlaceContentPrivate]) -> bool:
    """
    Calls Qt's 'bool QPlaceContentPrivate::compare(const QPlaceContentPrivate
    *other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontentprivate.html#compare

    Parameters
    ----------

    other : Optional[QPlaceContentPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPlaceContentPrivate::compare(const QPlaceContentPrivate *other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QPlaceContentPrivate7compareEPKS_',
        self._addressOf(other),
    )

  def type(self) -> QPlaceContent.Type:
    """
    Calls Qt's 'QPlaceContent::Type QPlaceContentPrivate::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontentprivate.html#type

    Returns
    -------

    QPlaceContent.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPlaceContent.Type(number)' gives.
    """
    #  QPlaceContent::Type QPlaceContentPrivate::type() const
    return QPlaceContent.Type(self.uglySide.call(
        'ritual_ZNK20QPlaceContentPrivate4typeEv',
    ))

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

  @overload(QPlaceContent.Type)
  def __init__(self, type: QPlaceContent.Type) -> None:
    """
    Notes what was given, for Qt's
    'QPlaceContentPrivate::QPlaceContentPrivate(QPlaceContent::Type type)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacecontentprivate.html#QPlaceContentPrivate

    Parameters
    ----------

    type : QPlaceContent.Type
      Passed on as its number.
    """
    #  QPlaceContentPrivate::QPlaceContentPrivate(QPlaceContent::Type type)
    self._noteCreation(QPlaceContentPrivate, lambda: Rituals.call(
        'ritual_ZN20QPlaceContentPrivateC1EN13QPlaceContent4TypeE',
        type.value,
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
