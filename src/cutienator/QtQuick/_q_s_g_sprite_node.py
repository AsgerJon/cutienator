"""
QSGSpriteNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGSpriteNode to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSGTexture, QSGVisitableNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint, QSize, QSizeF
  from . import QSGNodeVisitorEx
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QSGNodeVisitorEx = WAIT['QSGNodeVisitorEx']
  QSize = WAIT['QSize']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGSpriteNode(QSGVisitableNode):
  """
  The cute side of Qt's QSGSpriteNode: a plain Python object standing in
  front of one C++ QSGSpriteNode.

  It is built on the cute 'QSGVisitableNode', as Qt's QSGSpriteNode is built
  on Qt's QSGVisitableNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGSpriteNode that has a ritual and that Python can
  call so far, 10 names in all: 'setTexture', 'setTime', 'setSourceA',
  'setSourceB', 'setSpriteSize', 'setSheetSize', 'setSize', 'setFiltering',
  'update', 'accept'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGSpriteNode::~QSGSpriteNode()': the destructor: Python never
    removes a C++ QSGSpriteNode.

  What to expect
  --------------

  - The C++ QSGSpriteNode is created at the first use, not by
    'QSGSpriteNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGSpriteNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGSpriteNode'

  #  A C++ QSGSpriteNode Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGSpriteNode'

  #  The functions Qt calls itself that QSGSpriteNode is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setTexture': (
          ('_ZN13QSGSpriteNode10setTextureEP10QSGTexture',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGTexture'),
           )),
      ),
      'setTime': (
          ('_ZN13QSGSpriteNode7setTimeEf',
           ('nothing', 'nothing', ''),
           (
               ('float', 'number', ''),
           )),
      ),
      'setSourceA': (
          ('_ZN13QSGSpriteNode10setSourceAERK6QPoint',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'setSourceB': (
          ('_ZN13QSGSpriteNode10setSourceBERK6QPoint',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'setSpriteSize': (
          ('_ZN13QSGSpriteNode13setSpriteSizeERK5QSize',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'setSheetSize': (
          ('_ZN13QSGSpriteNode12setSheetSizeERK5QSize',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'setSize': (
          ('_ZN13QSGSpriteNode7setSizeERK6QSizeF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QSizeF'),
           )),
      ),
      'setFiltering': (
          ('_ZN13QSGSpriteNode12setFilteringEN10QSGTexture9FilteringE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQuick:QSGTexture.Filtering'),
           )),
      ),
      'update': (
          ('_ZN13QSGSpriteNode6updateEv',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGTexture)
  @overload(NoneType)
  def setTexture(self, texture: Optional[QSGTexture]) -> None:
    """
    Calls Qt's 'void QSGSpriteNode::setTexture(QSGTexture *texture)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgspritenode.html#setTexture

    Parameters
    ----------

    texture : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSpriteNode::setTexture(QSGTexture *texture)
    self.uglySide.call(
        'ritual_ZN13QSGSpriteNode10setTextureEP10QSGTexture',
        self._addressOf(texture),
    )

  @overload(float)
  def setTime(self, time: float) -> None:
    """
    Calls Qt's 'void QSGSpriteNode::setTime(float time)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgspritenode.html#setTime

    Parameters
    ----------

    time : float
      Passed on as it is.
    """
    #  void QSGSpriteNode::setTime(float time)
    self.uglySide.call('ritual_ZN13QSGSpriteNode7setTimeEf', time)

  @overload(QPoint)
  def setSourceA(self, source: QPoint) -> None:
    """
    Calls Qt's 'void QSGSpriteNode::setSourceA(const QPoint &source)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgspritenode.html#setSourceA

    Parameters
    ----------

    source : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QSGSpriteNode::setSourceA(const QPoint &source)
    self.uglySide.call(
        'ritual_ZN13QSGSpriteNode10setSourceAERK6QPoint',
        self._valueOf(source),
    )

  @overload(QPoint)
  def setSourceB(self, source: QPoint) -> None:
    """
    Calls Qt's 'void QSGSpriteNode::setSourceB(const QPoint &source)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgspritenode.html#setSourceB

    Parameters
    ----------

    source : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QSGSpriteNode::setSourceB(const QPoint &source)
    self.uglySide.call(
        'ritual_ZN13QSGSpriteNode10setSourceBERK6QPoint',
        self._valueOf(source),
    )

  @overload(QSize)
  def setSpriteSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QSGSpriteNode::setSpriteSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgspritenode.html#setSpriteSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QSGSpriteNode::setSpriteSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN13QSGSpriteNode13setSpriteSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(QSize)
  def setSheetSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QSGSpriteNode::setSheetSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgspritenode.html#setSheetSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QSGSpriteNode::setSheetSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN13QSGSpriteNode12setSheetSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(QSizeF)
  def setSize(self, size: QSizeF) -> None:
    """
    Calls Qt's 'void QSGSpriteNode::setSize(const QSizeF &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgspritenode.html#setSize

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QSGSpriteNode::setSize(const QSizeF &size)
    self.uglySide.call(
        'ritual_ZN13QSGSpriteNode7setSizeERK6QSizeF', self._valueOf(size),
    )

  @overload(QSGTexture.Filtering)
  def setFiltering(self, filtering: QSGTexture.Filtering) -> None:
    """
    Calls Qt's 'void QSGSpriteNode::setFiltering(QSGTexture::Filtering
    filtering)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgspritenode.html#setFiltering

    Parameters
    ----------

    filtering : QSGTexture.Filtering
      Passed on as its number.
    """
    #  void QSGSpriteNode::setFiltering(QSGTexture::Filtering filtering)
    self.uglySide.call(
        'ritual_ZN13QSGSpriteNode12setFilteringEN10QSGTexture9FilteringE',
        filtering.value,
    )

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

  def update(self) -> None:
    """
    Calls Qt's 'void QSGSpriteNode::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgspritenode.html#update
    """
    #  void QSGSpriteNode::update()
    self.uglySide.call('ritual_ZN13QSGSpriteNode6updateEv')

  @overload(QSGNodeVisitorEx)
  @overload(NoneType)
  def accept(self, visitor: Optional[QSGNodeVisitorEx]) -> None:
    """
    Calls Qt's 'void QSGSpriteNode::accept(QSGNodeVisitorEx *visitor)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgspritenode.html#accept

    Parameters
    ----------

    visitor : Optional[QSGNodeVisitorEx]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSpriteNode::accept(QSGNodeVisitorEx *visitor)
    ritual = 'ritual_ZN13QSGSpriteNode6acceptEP16QSGNodeVisitorEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QSGSpriteNode6acceptEP16QSGNodeVisitorEx'
    self.uglySide.call(ritual, self._addressOf(visitor))
