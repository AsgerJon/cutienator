"""
QCanUniqueIdDescriptionPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/6.12.0/QtSerialBus/private/qcanuniqueiddescription_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QCanUniqueIdDescriptionPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QCanUniqueIdDescription
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanUniqueIdDescription = WAIT['QCanUniqueIdDescription']


class QCanUniqueIdDescriptionPrivate(QSharedData):
  """
  The cute side of Qt's QCanUniqueIdDescriptionPrivate: a plain Python object
  standing in front of one C++ QCanUniqueIdDescriptionPrivate.

  It is built on the cute 'QSharedData', as Qt's
  QCanUniqueIdDescriptionPrivate is built on Qt's QSharedData, and has
  everything that class has.

  C++ hands a QCanUniqueIdDescriptionPrivate around as a copy, so every C++
  QCanUniqueIdDescriptionPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QCanUniqueIdDescriptionPrivate that has a ritual and
  that Python can call so far, 2 names in all: 'isShared', 'get'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanUniqueIdDescriptionPrivate::~QCanUniqueIdDescriptionPrivate()':
    the destructor: Python removes its C++ QCanUniqueIdDescriptionPrivate by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QCanUniqueIdDescriptionPrivate is created at the first use, not
    by 'QCanUniqueIdDescriptionPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanUniqueIdDescriptionPrivate back gives a copy the
    ritual made for Python, in a new cute QCanUniqueIdDescriptionPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QCanUniqueIdDescription)
  def get(
      desc: QCanUniqueIdDescription,
  ) -> Optional[QCanUniqueIdDescriptionPrivate]:
    """
    Calls Qt's 'QCanUniqueIdDescriptionPrivate
    *QCanUniqueIdDescriptionPrivate::get(const QCanUniqueIdDescription
    &desc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanuniqueiddescriptionprivate.html#get

    Parameters
    ----------

    desc : QCanUniqueIdDescription
      Passed on as a value: Qt reads the C++ QCanUniqueIdDescription, which
      stays Python's own.

    Returns
    -------

    Optional[QCanUniqueIdDescriptionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanUniqueIdDescriptionPrivate
    #      *QCanUniqueIdDescriptionPrivate::get(const QCanUniqueIdDescription
    #      &desc)
    address = Rituals.call(
        'ritual_ZN30QCanUniqueIdDescriptionPrivate3getERK23QCanUniqueIdDesc'
        'ription',
        CuteMixin._valueOf(desc),
    )
    return QCanUniqueIdDescriptionPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanUniqueIdDescriptionPrivate'

  #  Qt's '~QCanUniqueIdDescriptionPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QCanUniqueIdDescriptionPrivate behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN30QCanUniqueIdDescriptionPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isShared(self) -> bool:
    """
    Calls Qt's 'bool QCanUniqueIdDescriptionPrivate::isShared() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanuniqueiddescriptionprivate.html#isShared
    """
    #  bool QCanUniqueIdDescriptionPrivate::isShared() const
    return self.uglySide.call(
        'ritual_ZNK30QCanUniqueIdDescriptionPrivate8isSharedEv',
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
