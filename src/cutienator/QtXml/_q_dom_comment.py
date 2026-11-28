"""
QDomComment binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtXml/qdom.h, Qt
#  6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QDomCharacterData, QDomNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDomCommentPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDomCommentPrivate = WAIT['QDomCommentPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomComment(QDomCharacterData):
  """
  The cute side of Qt's QDomComment: a plain Python object standing in front
  of one C++ QDomComment.

  It is built on the cute 'QDomCharacterData', as Qt's QDomComment is built
  on Qt's QDomCharacterData, and has everything that class has.

  C++ hands a QDomComment around as a copy, so every C++ QDomComment behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomComment that has a ritual and that Python can
  call so far, 1 name in all: 'nodeType'. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomComment &QDomComment::operator=(const QDomComment &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QDomComment::~QDomComment()': the destructor: Python removes its
    C++ QDomComment by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QDomComment is created at the first use, not by
    'QDomComment(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomComment back gives a copy the ritual made for
    Python, in a new cute QDomComment.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomComment'

  #  Qt's '~QDomComment()'. Naming it makes this a value class: Python owns
  #  every C++ QDomComment behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QDomCommentD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def nodeType(self) -> QDomNode.NodeType:
    """
    Calls Qt's 'QDomNode::NodeType QDomComment::nodeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomcomment.html#nodeType

    Returns
    -------

    QDomNode.NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDomNode.NodeType(number)' gives.
    """
    #  QDomNode::NodeType QDomComment::nodeType() const
    return QDomNode.NodeType(self.uglySide.call(
        'ritual_ZNK11QDomComment8nodeTypeEv',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QDomComment::QDomComment()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomcomment.html#QDomComment
    """
    #  QDomComment::QDomComment()
    self._noteCreation(QDomComment, lambda: Rituals.call(
        'ritual_ZN11QDomCommentC1Ev',
    ))

  @overload(THIS)
  def __init__(self, comment: QDomComment) -> None:
    """
    Notes what was given, for Qt's 'QDomComment::QDomComment(const
    QDomComment &comment)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomcomment.html#QDomComment

    Parameters
    ----------

    comment : QDomComment
      Passed on as a value: Qt reads the C++ QDomComment, which stays
      Python's own.
    """
    #  QDomComment::QDomComment(const QDomComment &comment)
    self._noteCreation(QDomComment, lambda: Rituals.call(
        'ritual_ZN11QDomCommentC1ERKS_', self._valueOf(comment),
    ))

  @overload(QDomCommentPrivate)
  @overload(NoneType)
  def __init__(self, a0: Optional[QDomCommentPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QDomComment::QDomComment(QDomCommentPrivate *a0)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomcomment.html#QDomComment

    Parameters
    ----------

    a0 : Optional[QDomCommentPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDomComment::QDomComment(QDomCommentPrivate *a0)
    self._noteCreation(QDomComment, lambda: Rituals.call(
        'ritual_ZN11QDomCommentC1EP18QDomCommentPrivate',
        self._addressOf(a0),
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
