"""
QIconDirInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qiconloader_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QIconDirInfo to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from ..QtCore import QList


class QIconDirInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QIconDirInfo: a plain Python object standing in front
  of one C++ QIconDirInfo.

  C++ hands a QIconDirInfo around as a copy, so every C++ QIconDirInfo behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QIconDirInfo yet. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QIconDirInfo::~QIconDirInfo()': the destructor: Python removes its
    C++ QIconDirInfo by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QIconDirInfo is created at the first use, not by
    'QIconDirInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QIconDirInfo back gives a copy the ritual made for
    Python, in a new cute QIconDirInfo.
  """

  #  The enums Qt writes inside QIconDirInfo, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Context(CuteNum):
    """
    The enum 'QIconDirInfo::Context' of Qt, with the 3 names Qt gives in it.
    """

    UnknownContext = Kee[int](0)
    Applications = Kee[int](1)
    MimeTypes = Kee[int](2)

  class Type(CuteNum):
    """
    The enum 'QIconDirInfo::Type' of Qt, with the 4 names Qt gives in it.
    """

    Fixed = Kee[int](0)
    Scalable = Kee[int](1)
    Threshold = Kee[int](2)
    Fallback = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QIconDirInfo'

  #  Qt's '~QIconDirInfo()'. Naming it makes this a value class: Python owns
  #  every C++ QIconDirInfo behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QIconDirInfoD1Ev'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(str)
  def __init__(self, _path: str = '') -> None:
    """
    Notes what was given, for Qt's 'QIconDirInfo::QIconDirInfo(const QString
    &_path)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qicondirinfo.html#QIconDirInfo

    Parameters
    ----------

    _path : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QIconDirInfo::QIconDirInfo(const QString &_path)
    self._noteCreation(QIconDirInfo, lambda: Rituals.call(
        'ritual_ZN12QIconDirInfoC1ERK7QString', _path,
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


#  Qt's 'QList<QIconDirInfo>': the list of QIconDirInfo, which
#  'QList[QIconDirInfo]' gives. It is made here, so that there is one as soon
#  as there can be a QIconDirInfo.
QList.createKind(
    QIconDirInfo, 'value',
    make='ritual_list_make_QIconDirInfo',
    add='ritual_list_add_QIconDirInfo',
    size='ritual_list_size_QIconDirInfo',
    at='ritual_list_at_QIconDirInfo',
    drop='ritual_list_drop_QIconDirInfo',
)
