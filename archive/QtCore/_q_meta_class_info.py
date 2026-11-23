"""
QMetaClassInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmetaobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QMetaObject


class QMetaClassInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMetaClassInfo: a plain Python object standing in
  front of one C++ QMetaClassInfo.

  C++ hands a QMetaClassInfo around as a copy, so every C++ QMetaClassInfo
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMetaClassInfo that has a ritual and that Python can
  call so far, 3 names in all: 'name', 'value', 'enclosingMetaObject'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMetaClassInfo::~QMetaClassInfo()': the destructor: Python removes
    its C++ QMetaClassInfo by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QMetaClassInfo is created at the first use, not by
    'QMetaClassInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMetaClassInfo back gives a copy the ritual made for
    Python, in a new cute QMetaClassInfo.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMetaClassInfo'

  #  Qt's '~QMetaClassInfo()'. Naming it makes this a value class: Python
  #  owns every C++ QMetaClassInfo behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QMetaClassInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QMetaClassInfo::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaclassinfo.html#name

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QMetaClassInfo::name() const
    chars = self.uglySide.call('ritual_ZNK14QMetaClassInfo4nameEv')
    return None if chars is None else chars.decode()

  def value(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QMetaClassInfo::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaclassinfo.html#value

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QMetaClassInfo::value() const
    chars = self.uglySide.call('ritual_ZNK14QMetaClassInfo5valueEv')
    return None if chars is None else chars.decode()

  def enclosingMetaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMetaClassInfo::enclosingMetaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaclassinfo.html#enclosingMetaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMetaClassInfo::enclosingMetaObject() const
    address = self.uglySide.call(
        'ritual_ZNK14QMetaClassInfo19enclosingMetaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Notes what was given, for Qt's 'QMetaClassInfo::QMetaClassInfo()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmetaclassinfo.html#QMetaClassInfo
    """
    #  QMetaClassInfo::QMetaClassInfo()
    self._noteCreation(QMetaClassInfo, lambda: Rituals.call(
        'ritual_ZN14QMetaClassInfoC1Ev',
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
