"""
QXdgDBusImageStruct binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qdbustraytypes_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QXdgDBusImageStruct to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList


class QXdgDBusImageStruct(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXdgDBusImageStruct: a plain Python object standing
  in front of one C++ QXdgDBusImageStruct.

  C++ hands a QXdgDBusImageStruct around as a copy, so every C++
  QXdgDBusImageStruct behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QXdgDBusImageStruct yet. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXdgDBusImageStruct::~QXdgDBusImageStruct()': the destructor:
    Python removes its C++ QXdgDBusImageStruct by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QXdgDBusImageStruct is created at the first use, not by
    'QXdgDBusImageStruct(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QXdgDBusImageStruct back gives a copy the ritual made
    for Python, in a new cute QXdgDBusImageStruct.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXdgDBusImageStruct'

  #  Qt's '~QXdgDBusImageStruct()'. Naming it makes this a value class:
  #  Python owns every C++ QXdgDBusImageStruct behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QXdgDBusImageStructD1Ev'

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QXdgDBusImageStruct::QXdgDBusImageStruct()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxdgdbusimagestruct.html#QXdgDBusImageStruct
    """
    #  QXdgDBusImageStruct::QXdgDBusImageStruct()
    self._noteCreation(QXdgDBusImageStruct, lambda: Rituals.call(
        'ritual_ZN19QXdgDBusImageStructC1Ev',
    ))

  @overload(int, int)
  def __init__(self, w: int, h: int) -> None:
    """
    Notes what was given, for Qt's
    'QXdgDBusImageStruct::QXdgDBusImageStruct(int w, int h)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxdgdbusimagestruct.html#QXdgDBusImageStruct

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  QXdgDBusImageStruct::QXdgDBusImageStruct(int w, int h)
    self._noteCreation(QXdgDBusImageStruct, lambda: Rituals.call(
        'ritual_ZN19QXdgDBusImageStructC1Eii', w, h,
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


#  Qt's 'QList<QXdgDBusImageStruct>': the list of QXdgDBusImageStruct, which
#  'QList[QXdgDBusImageStruct]' gives. It is made here, so that there is one
#  as soon as there can be a QXdgDBusImageStruct. Qt has a name of its own
#  for it.
QXdgDBusImageVector = QList.createKind(
    QXdgDBusImageStruct, 'value',
    name='QXdgDBusImageVector',
    make='ritual_list_make_QXdgDBusImageStruct',
    add='ritual_list_add_QXdgDBusImageStruct',
    size='ritual_list_size_QXdgDBusImageStruct',
    at='ritual_list_at_QXdgDBusImageStruct',
    drop='ritual_list_drop_QXdgDBusImageStruct',
)
