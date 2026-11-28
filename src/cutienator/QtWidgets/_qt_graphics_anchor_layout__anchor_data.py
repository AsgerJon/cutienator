"""
QtGraphicsAnchorLayout::AnchorData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicsanchorlayout_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QtGraphicsAnchorLayout::AnchorData to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteNum
from . import QSimplexVariable

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class AnchorData(QSimplexVariable):
  """
  The cute side of Qt's QtGraphicsAnchorLayout::AnchorData: a plain Python
  object standing in front of one C++ QtGraphicsAnchorLayout::AnchorData.

  It is built on the cute 'QSimplexVariable', as Qt's
  QtGraphicsAnchorLayout::AnchorData is built on Qt's QSimplexVariable, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QtGraphicsAnchorLayout::AnchorData that has a ritual
  and that Python can call so far, 2 names in all: 'updateChildrenSizes',
  'toString'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtGraphicsAnchorLayout::AnchorData::~AnchorData()': the destructor:
    Python never removes a C++ QtGraphicsAnchorLayout::AnchorData.

  What has no ritual
  ------------------

  7 of the 10 functions Qt declares: 4 forbidden; 2 cannot be called and
  cannot be called through the meta-object and cannot be copied; 1 leans on
  'QtGraphicsAnchorLayout.

  What to expect
  --------------

  - The C++ QtGraphicsAnchorLayout::AnchorData is created at the first use,
    not by 'QtGraphicsAnchorLayout::AnchorData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtGraphicsAnchorLayout::AnchorData.
  - Each name of Qt's QtGraphicsAnchorLayout::AnchorData that has no cute
    function yet, '__init__', 'dump', 'refreshSizeHints', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QtGraphicsAnchorLayout::AnchorData, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Dependency(CuteNum):
    """
    The enum 'QtGraphicsAnchorLayout::AnchorData::Dependency' of Qt, with the
    3 names Qt gives in it.
    """

    Independent = Kee[int](0)
    Master = Kee[int](1)
    Slave = Kee[int](2)

  class Type(CuteNum):
    """
    The enum 'QtGraphicsAnchorLayout::AnchorData::Type' of Qt, with the 3
    names Qt gives in it.
    """

    Normal = Kee[int](0)
    Sequential = Kee[int](1)
    Parallel = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtGraphicsAnchorLayout::AnchorData'

  #  A C++ QtGraphicsAnchorLayout::AnchorData Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtGraphicsAnchorLayout_AnchorData'

  #  The functions Qt calls itself that QtGraphicsAnchorLayout::AnchorData is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'updateChildrenSizes': (
          ('_ZN22QtGraphicsAnchorLayout10AnchorData19updateChildrenSizesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QtGraphicsAnchorLayout::AnchorData::toString()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgraphicsanchorlayout-anchordata.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtGraphicsAnchorLayout::AnchorData::toString() const
    return self.uglySide.call(
        'ritual_ZNK22QtGraphicsAnchorLayout10AnchorData8toStringEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QtGraphicsAnchorLayout::AnchorData::AnchorData()': leans on
    'QtGraphicsAnchorLayout::AnchorData::~AnchorData()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QtGraphicsAnchorLayout.AnchorData.__init__' has no cute function "
        "yet. Qt's 'QtGraphicsAnchorLayout::AnchorData::AnchorData()': "
        "leans on 'QtGraphicsAnchorLayout::AnchorData::~AnchorData()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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
    QtGraphicsAnchorLayout::AnchorData::updateChildrenSizes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgraphicsanchorlayout-anchordata.html
    """
    #  void QtGraphicsAnchorLayout::AnchorData::updateChildrenSizes()
    ritual = (
        'ritual_ZN22QtGraphicsAnchorLayout10AnchorData19updateChildrenSizes'
        'Ev')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QtGraphicsAnchorLayout10AnchorData19updateChildre'
          'nSizesEv')
    self.uglySide.call(ritual)

  @staticmethod
  def dump(*__, **_) -> Never:
    """
    Qt's 'void QtGraphicsAnchorLayout::AnchorData::dump(int indent)': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QtGraphicsAnchorLayout.AnchorData.dump' has no cute function yet. "
        "Qt's 'void QtGraphicsAnchorLayout::AnchorData::dump(int indent)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def refreshSizeHints(*__, **_) -> Never:
    """
    Qt's 'void QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(const
    QLayoutStyleInfo *styleInfo)': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QtGraphicsAnchorLayout.AnchorData.refreshSizeHints' has no cute "
        "function yet. Qt's 'void "
        "QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(const "
        "QLayoutStyleInfo *styleInfo)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")
