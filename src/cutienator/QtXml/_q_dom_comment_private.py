"""
QDomCommentPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtXml/6.12.0/QtXml/private/qdom_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QDomCommentPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QDomCharacterDataPrivate, QDomNode, QDomNodePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QDomCommentPrivate(QDomCharacterDataPrivate):
  """
  The cute side of Qt's QDomCommentPrivate: a plain Python object standing in
  front of one C++ QDomCommentPrivate.

  It is built on the cute 'QDomCharacterDataPrivate', as Qt's
  QDomCommentPrivate is built on Qt's QDomCharacterDataPrivate, and has
  everything that class has.

  C++ hands a QDomCommentPrivate around as a copy, so every C++
  QDomCommentPrivate behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomCommentPrivate that has a ritual and that Python
  can call so far, 2 names in all: 'cloneNode', 'nodeType'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QDomCommentPrivate::save(QTextStream &s, int a1, int a2)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QDomCommentPrivate::~QDomCommentPrivate()': the destructor: Python
    removes its C++ QDomCommentPrivate by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 2 leans on 'QDomNodePrivate.

  What to expect
  --------------

  - The C++ QDomCommentPrivate is created at the first use, not by
    'QDomCommentPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomCommentPrivate back gives a copy the ritual made
    for Python, in a new cute QDomCommentPrivate.
  - Each name of Qt's QDomCommentPrivate that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomCommentPrivate'

  #  A C++ QDomCommentPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDomCommentPrivate'

  #  Qt's '~QDomCommentPrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QDomCommentPrivate behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QDomCommentPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def nodeType(self) -> QDomNode.NodeType:
    """
    Calls Qt's 'QDomNode::NodeType QDomCommentPrivate::nodeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomcommentprivate.html#nodeType

    Returns
    -------

    QDomNode.NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDomNode.NodeType(number)' gives.
    """
    #  QDomNode::NodeType QDomCommentPrivate::nodeType() const
    ritual = 'ritual_ZNK18QDomCommentPrivate8nodeTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QDomCommentPrivate8nodeTypeEv'
    return QDomNode.NodeType(self.uglySide.call(ritual))

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
    - Qt's 'QDomCommentPrivate::QDomCommentPrivate(QDomDocumentPrivate *a0,
      QDomNodePrivate *parent, const QString &val)': leans on
      'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*,
      QDomNodePrivate*)', which Qt's source does not mark for use from
      outside Qt and has no code for that could be taken.
    - Qt's 'QDomCommentPrivate::QDomCommentPrivate(QDomCommentPrivate *n,
      bool deep)': leans on
      'QDomNodePrivate::QDomNodePrivate(QDomNodePrivate*, bool)', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    """
    raise NotImplementedError(
        "'QDomCommentPrivate.__init__' has no cute function yet. Qt's "
        "'QDomCommentPrivate::QDomCommentPrivate(QDomDocumentPrivate *a0, "
        "QDomNodePrivate *parent, const QString &val)': leans on "
        "'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*, "
        "QDomNodePrivate*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken. Qt's "
        "'QDomCommentPrivate::QDomCommentPrivate(QDomCommentPrivate *n, "
        "bool deep)': leans on "
        "'QDomNodePrivate::QDomNodePrivate(QDomNodePrivate*, bool)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  @overload()
  @overload(bool)
  def cloneNode(self, deep: bool = True) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate *QDomCommentPrivate::cloneNode(bool deep)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomcommentprivate.html#cloneNode

    Parameters
    ----------

    deep : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate *QDomCommentPrivate::cloneNode(bool deep)
    address = self.uglySide.call(
        'ritual_ZN18QDomCommentPrivate9cloneNodeEb', deep,
    )
    return QDomNodePrivate._cuteAt(address)
