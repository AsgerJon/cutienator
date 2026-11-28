"""
QtGraphicsAnchorLayout::SequentialAnchorData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicsanchorlayout_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QtGraphicsAnchorLayout::SequentialAnchorData to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QtGraphicsAnchorLayout

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class SequentialAnchorData(QtGraphicsAnchorLayout.AnchorData):
  """
  The cute side of Qt's QtGraphicsAnchorLayout::SequentialAnchorData: a plain
  Python object standing in front of one C++
  QtGraphicsAnchorLayout::SequentialAnchorData.

  It is built on the cute 'QtGraphicsAnchorLayout::AnchorData', as Qt's
  QtGraphicsAnchorLayout::SequentialAnchorData is built on Qt's
  QtGraphicsAnchorLayout::AnchorData, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtGraphicsAnchorLayout::SequentialAnchorData that
  has a ritual and that Python can call so far, 1 name in all:
  'updateChildrenSizes'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has no ritual
  ------------------

  2 of the 3 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied; 1 leans on
  'QtGraphicsAnchorLayout.

  What to expect
  --------------

  - The C++ QtGraphicsAnchorLayout::SequentialAnchorData is created at the
    first use, not by 'QtGraphicsAnchorLayout::SequentialAnchorData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtGraphicsAnchorLayout::SequentialAnchorData.
  - Each name of Qt's QtGraphicsAnchorLayout::SequentialAnchorData that has
    no cute function yet, '__init__', 'calculateSizeHints', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtGraphicsAnchorLayout::SequentialAnchorData'

  #  A C++ QtGraphicsAnchorLayout::SequentialAnchorData Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtGraphicsAnchorLayout_SequentialAnchorData'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QtGraphicsAnchorLayout::SequentialAnchorData::SequentialAnchorData(const
    QList<AnchorVertex *> &vertices, const QList<AnchorData *> &edges)':
    leans on 'QtGraphicsAnchorLayout::AnchorData::~AnchorData()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QtGraphicsAnchorLayout.SequentialAnchorData.__init__' has no cute "
        "function yet. Qt's "
        "'QtGraphicsAnchorLayout::SequentialAnchorData::SequentialAnchorData"
        "(const QList<AnchorVertex *> &vertices, const QList<AnchorData *> "
        "&edges)': leans on "
        "'QtGraphicsAnchorLayout::AnchorData::~AnchorData()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  def updateChildrenSizes(self) -> None:
    """
    Calls Qt's 'void
    QtGraphicsAnchorLayout::SequentialAnchorData::updateChildrenSizes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgraphicsanchorlayout-sequentialanchordata.html
    """
    #  void
    #      QtGraphicsAnchorLayout::SequentialAnchorData::updateChildrenSizes(
    #      )
    self.uglySide.call(
        'ritual_ZN22QtGraphicsAnchorLayout20SequentialAnchorData19updateChi'
        'ldrenSizesEv',
    )

  @staticmethod
  def calculateSizeHints(*__, **_) -> Never:
    """
    Qt's 'void
    QtGraphicsAnchorLayout::SequentialAnchorData::calculateSizeHints()':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QtGraphicsAnchorLayout.SequentialAnchorData.calculateSizeHints' "
        "has no cute function yet. Qt's 'void "
        "QtGraphicsAnchorLayout::SequentialAnchorData::calculateSizeHints()'"
        ": cannot be called and cannot be called through the meta-object "
        "and cannot be copied: no header file has its code, Qt's source "
        "does not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")
