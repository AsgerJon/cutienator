"""
QDomAttrPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtXml/6.12.0/QtXml/private/qdom_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QDomAttrPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QDomNode, QDomNodePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QDomAttrPrivate(QDomNodePrivate):
  """
  The cute side of Qt's QDomAttrPrivate: a plain Python object standing in
  front of one C++ QDomAttrPrivate.

  It is built on the cute 'QDomNodePrivate', as Qt's QDomAttrPrivate is built
  on Qt's QDomNodePrivate, and has everything that class has.

  C++ hands a QDomAttrPrivate around as a copy, so every C++ QDomAttrPrivate
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomAttrPrivate that has a ritual and that Python
  can call so far, 4 names in all: 'specified', 'setNodeValue', 'cloneNode',
  'nodeType'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QDomAttrPrivate::save(QTextStream &s, int a1, int a2) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QDomAttrPrivate::~QDomAttrPrivate()': the destructor: Python
    removes its C++ QDomAttrPrivate by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 9 functions Qt declares: 3 leans on 'QDomNodePrivate.

  What to expect
  --------------

  - The C++ QDomAttrPrivate is created at the first use, not by
    'QDomAttrPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomAttrPrivate back gives a copy the ritual made for
    Python, in a new cute QDomAttrPrivate.
  - Each name of Qt's QDomAttrPrivate that has no cute function yet,
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
  __qt_class__ = 'QDomAttrPrivate'

  #  A C++ QDomAttrPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDomAttrPrivate'

  #  Qt's '~QDomAttrPrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QDomAttrPrivate behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QDomAttrPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def specified(self) -> bool:
    """
    Calls Qt's 'bool QDomAttrPrivate::specified() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomattrprivate.html#specified
    """
    #  bool QDomAttrPrivate::specified() const
    return self.uglySide.call('ritual_ZNK15QDomAttrPrivate9specifiedEv')

  def nodeType(self) -> QDomNode.NodeType:
    """
    Calls Qt's 'QDomNode::NodeType QDomAttrPrivate::nodeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomattrprivate.html#nodeType

    Returns
    -------

    QDomNode.NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDomNode.NodeType(number)' gives.
    """
    #  QDomNode::NodeType QDomAttrPrivate::nodeType() const
    ritual = 'ritual_ZNK15QDomAttrPrivate8nodeTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QDomAttrPrivate8nodeTypeEv'
    return QDomNode.NodeType(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setNodeValue(self, v: str) -> None:
    """
    Calls Qt's 'void QDomAttrPrivate::setNodeValue(const QString &v)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomattrprivate.html#setNodeValue

    Parameters
    ----------

    v : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDomAttrPrivate::setNodeValue(const QString &v)
    self.uglySide.call(
        'ritual_ZN15QDomAttrPrivate12setNodeValueERK7QString', v,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QDomAttrPrivate::QDomAttrPrivate(QDomDocumentPrivate *a0,
      QDomNodePrivate *a1, const QString &name)': leans on
      'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*,
      QDomNodePrivate*)', which Qt's source does not mark for use from
      outside Qt and has no code for that could be taken.
    - Qt's 'QDomAttrPrivate::QDomAttrPrivate(QDomDocumentPrivate *a0,
      QDomNodePrivate *a1, const QString &nsURI, const QString &qName)':
      leans on 'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*,
      QDomNodePrivate*)', which Qt's source does not mark for use from
      outside Qt and has no code for that could be taken.
    - Qt's 'QDomAttrPrivate::QDomAttrPrivate(QDomAttrPrivate *n, bool deep)':
      leans on 'QDomNodePrivate::QDomNodePrivate(QDomNodePrivate*, bool)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    """
    raise NotImplementedError(
        "'QDomAttrPrivate.__init__' has no cute function yet. Qt's "
        "'QDomAttrPrivate::QDomAttrPrivate(QDomDocumentPrivate *a0, "
        "QDomNodePrivate *a1, const QString &name)': leans on "
        "'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*, "
        "QDomNodePrivate*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken. Qt's "
        "'QDomAttrPrivate::QDomAttrPrivate(QDomDocumentPrivate *a0, "
        "QDomNodePrivate *a1, const QString &nsURI, const QString &qName)': "
        "leans on 'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*, "
        "QDomNodePrivate*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken. Qt's "
        "'QDomAttrPrivate::QDomAttrPrivate(QDomAttrPrivate *n, bool deep)': "
        "leans on 'QDomNodePrivate::QDomNodePrivate(QDomNodePrivate*, "
        "bool)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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
    Calls Qt's 'QDomNodePrivate *QDomAttrPrivate::cloneNode(bool deep)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomattrprivate.html#cloneNode

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
    #  QDomNodePrivate *QDomAttrPrivate::cloneNode(bool deep)
    address = self.uglySide.call(
        'ritual_ZN15QDomAttrPrivate9cloneNodeEb', deep,
    )
    return QDomNodePrivate._cuteAt(address)
