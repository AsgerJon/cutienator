"""
LabelItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/labelitem_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means LabelItem to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSize = WAIT['QSize']


class LabelItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's LabelItem: a plain Python object standing in front of
  one C++ LabelItem.

  What exists
  -----------

  Every function of Qt's LabelItem that has a ritual and that Python can call
  so far, 5 names in all: 'setSize', 'size', 'setTextureId', 'textureId',
  'clear'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'LabelItem::~LabelItem()': the destructor: Python never removes a
    C++ LabelItem.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ LabelItem is created at the first use, not by 'LabelItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ LabelItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'LabelItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize LabelItem::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/labelitem.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize LabelItem::size() const
    address = self.uglySide.call('ritual_ZNK9LabelItem4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def textureId(self) -> int:
    """
    Calls Qt's 'GLuint LabelItem::textureId() const'.

    Qt's own words: https://doc.qt.io/qt-6/labelitem.html#textureId
    """
    #  GLuint LabelItem::textureId() const
    return self.uglySide.call('ritual_ZNK9LabelItem9textureIdEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSize)
  def setSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void LabelItem::setSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/labelitem.html#setSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void LabelItem::setSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN9LabelItem7setSizeERK5QSize', self._valueOf(size),
    )

  @overload(int)
  def setTextureId(self, textureId: int) -> None:
    """
    Calls Qt's 'void LabelItem::setTextureId(GLuint textureId)'.

    Qt's own words: https://doc.qt.io/qt-6/labelitem.html#setTextureId

    Parameters
    ----------

    textureId : int
      Passed on as it is.
    """
    #  void LabelItem::setTextureId(GLuint textureId)
    self.uglySide.call('ritual_ZN9LabelItem12setTextureIdEj', textureId)

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
    Notes what was given, for Qt's 'LabelItem::LabelItem()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/labelitem.html#LabelItem
    """
    #  LabelItem::LabelItem()
    self._noteCreation(LabelItem, lambda: Rituals.call(
        'ritual_ZN9LabelItemC1Ev',
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

  def clear(self) -> None:
    """
    Calls Qt's 'void LabelItem::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/labelitem.html#clear
    """
    #  void LabelItem::clear()
    self.uglySide.call('ritual_ZN9LabelItem5clearEv')
