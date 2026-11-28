"""
QtProtobufPrivate::QProtobufFieldInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtProtobuf/qprotobufpropertyordering.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtProtobufPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QProtobufFieldInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtProtobufPrivate::QProtobufFieldInfo: a plain Python
  object standing in front of one C++ QtProtobufPrivate::QProtobufFieldInfo.

  C++ hands a QtProtobufPrivate::QProtobufFieldInfo around as a copy, so
  every C++ QtProtobufPrivate::QProtobufFieldInfo behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtProtobufPrivate::QProtobufFieldInfo that has a
  ritual and that Python can call so far, 3 names in all: 'fieldNumber',
  'propertyIndex', 'fieldFlags'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QUtf8StringView QtProtobufPrivate::QProtobufFieldInfo::jsonName()
    const': gives a type Python has no way to take yet.
  - Qt's 'QtProtobufPrivate::QProtobufFieldInfo::~QProtobufFieldInfo()': the
    destructor: Python removes its C++ QtProtobufPrivate::QProtobufFieldInfo
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QtProtobufPrivate::QProtobufFieldInfo is created at the first
    use, not by 'QtProtobufPrivate::QProtobufFieldInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtProtobufPrivate::QProtobufFieldInfo back gives a
    copy the ritual made for Python, in a new cute
    QtProtobufPrivate::QProtobufFieldInfo.
  - Each name of Qt's QtProtobufPrivate::QProtobufFieldInfo that has no cute
    function yet, 'jsonName', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtProtobufPrivate::QProtobufFieldInfo'

  #  Qt's '~QtProtobufPrivate::QProtobufFieldInfo()'. Naming it makes this a
  #  value class: Python owns every C++ QtProtobufPrivate::QProtobufFieldInfo
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN17QtProtobufPrivate18QProtobufFieldInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def fieldNumber(self) -> int:
    """
    Calls Qt's 'int QtProtobufPrivate::QProtobufFieldInfo::fieldNumber()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobuffieldinfo.html
    """
    #  int QtProtobufPrivate::QProtobufFieldInfo::fieldNumber() const
    return self.uglySide.call(
        'ritual_ZNK17QtProtobufPrivate18QProtobufFieldInfo11fieldNumberEv',
    )

  def propertyIndex(self) -> int:
    """
    Calls Qt's 'int QtProtobufPrivate::QProtobufFieldInfo::propertyIndex()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobuffieldinfo.html
    """
    #  int QtProtobufPrivate::QProtobufFieldInfo::propertyIndex() const
    return self.uglySide.call(
        'ritual_ZNK17QtProtobufPrivate18QProtobufFieldInfo13propertyIndexEv',
    )

  def fieldFlags(self) -> QtProtobufPrivate.FieldFlags:
    """
    Calls Qt's 'FieldFlags
    QtProtobufPrivate::QProtobufFieldInfo::fieldFlags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobuffieldinfo.html

    Returns
    -------

    QtProtobufPrivate.FieldFlags
      The value standing for the combination Qt gave back.
    """
    #  FieldFlags QtProtobufPrivate::QProtobufFieldInfo::fieldFlags() const
    return QtProtobufPrivate.FieldFlags(self.uglySide.call(
        'ritual_ZNK17QtProtobufPrivate18QProtobufFieldInfo10fieldFlagsEv',
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

  @overload(WAIT['QtProtobufPrivate.QProtobufPropertyOrdering'], int)
  def __init__(
      self,
      ord: QtProtobufPrivate.QProtobufPropertyOrdering,
      ind: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QtProtobufPrivate::QProtobufFieldInfo::QProtobufFieldInfo(
    QProtobufPropertyOrdering ord, int ind)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobuffieldinfo.html

    Parameters
    ----------

    ord : QtProtobufPrivate.QProtobufPropertyOrdering
      Passed on as a value: Qt reads the C++
      QtProtobufPrivate::QProtobufPropertyOrdering, which stays Python's own.

    ind : int
      Passed on as it is.
    """
    #  QtProtobufPrivate::QProtobufFieldInfo::QProtobufFieldInfo(
    #      QProtobufPropertyOrdering ord, int ind)
    self._noteCreation(QProtobufFieldInfo, lambda: Rituals.call(
        'ritual_ZN17QtProtobufPrivate18QProtobufFieldInfoC1ENS_25QProtobufP'
        'ropertyOrderingEi',
        self._valueOf(ord), ind,
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

  @staticmethod
  def jsonName(*__, **_) -> Never:
    """
    Qt's 'QUtf8StringView QtProtobufPrivate::QProtobufFieldInfo::jsonName()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtProtobufPrivate.QProtobufFieldInfo.jsonName' has no cute "
        "function yet. Qt's 'QUtf8StringView "
        "QtProtobufPrivate::QProtobufFieldInfo::jsonName() const': gives a "
        "type Python has no way to take yet.")
