"""
QSvgUse binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgUse to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSvgNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgUse(QSvgNode):
  """
  The cute side of Qt's QSvgUse: a plain Python object standing in front of
  one C++ QSvgUse.

  It is built on the cute 'QSvgNode', as Qt's QSvgUse is built on Qt's
  QSvgNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgUse that has a ritual and that Python can call
  so far, 7 names in all: 'type', 'isResolved', 'linkId', 'setLink', 'link',
  'start', 'isRecursing'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgUse::~QSvgUse()': the destructor: Python never removes a C++
    QSvgUse.
  - Qt's 'void QSvgUse::drawCommand(QPainter *p, QSvgExtraStates &states)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgUse::internalBounds(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgUse::decoratedInternalBounds(QPainter *p,
    QSvgExtraStates &states) const': takes a type Python has no way to hand
    over yet.

  What to expect
  --------------

  - The C++ QSvgUse is created at the first use, not by 'QSvgUse(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgUse.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgUse'

  #  A C++ QSvgUse Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgUse'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgNode.Type:
    """
    Calls Qt's 'Type QSvgUse::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvguse.html#type

    Returns
    -------

    QSvgNode.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSvgNode.Type(number)'
      gives.
    """
    #  Type QSvgUse::type() const
    ritual = 'ritual_ZNK7QSvgUse4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QSvgUse4typeEv'
    return QSvgNode.Type(self.uglySide.call(ritual))

  def isResolved(self) -> bool:
    """
    Calls Qt's 'bool QSvgUse::isResolved() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvguse.html#isResolved
    """
    #  bool QSvgUse::isResolved() const
    return self.uglySide.call('ritual_ZNK7QSvgUse10isResolvedEv')

  def linkId(self) -> str:
    """
    Calls Qt's 'const QString &QSvgUse::linkId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvguse.html#linkId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QSvgUse::linkId() const
    return self.uglySide.call('ritual_ZNK7QSvgUse6linkIdEv')

  def link(self) -> Optional[QSvgNode]:
    """
    Calls Qt's 'QSvgNode *QSvgUse::link() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvguse.html#link

    Returns
    -------

    Optional[QSvgNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSvgNode *QSvgUse::link() const
    address = self.uglySide.call('ritual_ZNK7QSvgUse4linkEv')
    return QSvgNode._cuteAt(address)

  def start(self) -> QPointF:
    """
    Calls Qt's 'QPointF QSvgUse::start() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvguse.html#start

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QSvgUse::start() const
    address = self.uglySide.call('ritual_ZNK7QSvgUse5startEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def isRecursing(self) -> bool:
    """
    Calls Qt's 'bool QSvgUse::isRecursing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvguse.html#isRecursing
    """
    #  bool QSvgUse::isRecursing() const
    return self.uglySide.call('ritual_ZNK7QSvgUse11isRecursingEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSvgNode)
  @overload(NoneType)
  def setLink(self, link: Optional[QSvgNode]) -> None:
    """
    Calls Qt's 'void QSvgUse::setLink(QSvgNode *link)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvguse.html#setLink

    Parameters
    ----------

    link : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgUse::setLink(QSvgNode *link)
    self.uglySide.call(
        'ritual_ZN7QSvgUse7setLinkEP8QSvgNode', self._addressOf(link),
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

  @overload(QPointF, QSvgNode, QSvgNode)
  @overload(QPointF, QSvgNode, NoneType)
  @overload(QPointF, NoneType, QSvgNode)
  @overload(QPointF, NoneType, NoneType)
  def __init__(
      self,
      start: QPointF,
      parent: Optional[QSvgNode],
      link: Optional[QSvgNode],
  ) -> None:
    """
    Notes what was given, for Qt's 'QSvgUse::QSvgUse(const QPointF &start,
    QSvgNode *parent, QSvgNode *link)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvguse.html#QSvgUse

    Parameters
    ----------

    start : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    parent : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    link : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSvgUse::QSvgUse(const QPointF &start, QSvgNode *parent, QSvgNode
    #      *link)
    self._noteCreation(QSvgUse, lambda: Rituals.call(
        'ritual_ZN7QSvgUseC1ERK7QPointFP8QSvgNodeS4_',
        self._valueOf(start, 'QPointF'), self._addressOf(parent),
        self._addressOf(link),
    ))

  @overload(QPointF, QSvgNode, str)
  @overload(QPointF, NoneType, str)
  def __init__(
      self,
      start: QPointF,
      parent: Optional[QSvgNode],
      linkId: str,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSvgUse::QSvgUse(const QPointF &start,
    QSvgNode *parent, const QString &linkId)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qsvguse.html#QSvgUse

    Parameters
    ----------

    start : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    parent : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    linkId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QSvgUse::QSvgUse(const QPointF &start, QSvgNode *parent, const QString
    #      &linkId)
    self._noteCreation(QSvgUse, lambda: Rituals.call(
        'ritual_ZN7QSvgUseC1ERK7QPointFP8QSvgNodeRK7QString',
        self._valueOf(start, 'QPointF'), self._addressOf(parent), linkId,
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
