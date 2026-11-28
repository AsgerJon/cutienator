"""
QDomDocumentTypePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtXml/6.12.0/QtXml/private/qdom_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QDomDocumentTypePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QDomNode, QDomNodePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomDocumentTypePrivate(QDomNodePrivate):
  """
  The cute side of Qt's QDomDocumentTypePrivate: a plain Python object
  standing in front of one C++ QDomDocumentTypePrivate.

  It is built on the cute 'QDomNodePrivate', as Qt's QDomDocumentTypePrivate
  is built on Qt's QDomNodePrivate, and has everything that class has.

  C++ hands a QDomDocumentTypePrivate around as a copy, so every C++
  QDomDocumentTypePrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomDocumentTypePrivate that has a ritual and that
  Python can call so far, 8 names in all: 'init', 'cloneNode',
  'insertBefore', 'insertAfter', 'replaceChild', 'removeChild',
  'appendChild', 'nodeType'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomDocumentTypePrivate::~QDomDocumentTypePrivate()': the
    destructor: Python removes its C++ QDomDocumentTypePrivate by it, and has
    no other use for it.
  - Qt's 'void QDomDocumentTypePrivate::save(QTextStream &s, int a1, int a2)
    const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 leans on 'QDomNodePrivate.

  What to expect
  --------------

  - The C++ QDomDocumentTypePrivate is created at the first use, not by
    'QDomDocumentTypePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomDocumentTypePrivate back gives a copy the ritual
    made for Python, in a new cute QDomDocumentTypePrivate.
  - Each name of Qt's QDomDocumentTypePrivate that has no cute function yet,
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
  __qt_class__ = 'QDomDocumentTypePrivate'

  #  A C++ QDomDocumentTypePrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDomDocumentTypePrivate'

  #  Qt's '~QDomDocumentTypePrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QDomDocumentTypePrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QDomDocumentTypePrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def nodeType(self) -> QDomNode.NodeType:
    """
    Calls Qt's 'QDomNode::NodeType QDomDocumentTypePrivate::nodeType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocumenttypeprivate.html#nodeType

    Returns
    -------

    QDomNode.NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDomNode.NodeType(number)' gives.
    """
    #  QDomNode::NodeType QDomDocumentTypePrivate::nodeType() const
    ritual = 'ritual_ZNK23QDomDocumentTypePrivate8nodeTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QDomDocumentTypePrivate8nodeTypeEv'
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
    - Qt's
      'QDomDocumentTypePrivate::QDomDocumentTypePrivate(QDomDocumentPrivate
      *a0, QDomNodePrivate *parent)': leans on
      'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*,
      QDomNodePrivate*)', which Qt's source does not mark for use from
      outside Qt and has no code for that could be taken.
    - Qt's 'QDomDocumentTypePrivate::QDomDocumentTypePrivate(
      QDomDocumentTypePrivate *n, bool deep)': leans on
      'QDomNodePrivate::QDomNodePrivate(QDomNodePrivate*, bool)', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    """
    raise NotImplementedError(
        "'QDomDocumentTypePrivate.__init__' has no cute function yet. Qt's "
        "'QDomDocumentTypePrivate::QDomDocumentTypePrivate(QDomDocumentPriva"
        "te *a0, QDomNodePrivate *parent)': leans on "
        "'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*, "
        "QDomNodePrivate*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken. Qt's "
        "'QDomDocumentTypePrivate::QDomDocumentTypePrivate(QDomDocumentTypeP"
        "rivate *n, bool deep)': leans on "
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

  def init(self) -> None:
    """
    Calls Qt's 'void QDomDocumentTypePrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocumenttypeprivate.html#init
    """
    #  void QDomDocumentTypePrivate::init()
    self.uglySide.call('ritual_ZN23QDomDocumentTypePrivate4initEv')

  @overload()
  @overload(bool)
  def cloneNode(self, deep: bool = True) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate *QDomDocumentTypePrivate::cloneNode(bool
    deep)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocumenttypeprivate.html#cloneNode

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
    #  QDomNodePrivate *QDomDocumentTypePrivate::cloneNode(bool deep)
    address = self.uglySide.call(
        'ritual_ZN23QDomDocumentTypePrivate9cloneNodeEb', deep,
    )
    return QDomNodePrivate._cuteAt(address)

  @overload(QDomNodePrivate, QDomNodePrivate)
  @overload(QDomNodePrivate, NoneType)
  @overload(NoneType, QDomNodePrivate)
  @overload(NoneType, NoneType)
  def insertBefore(
      self,
      newChild: Optional[QDomNodePrivate],
      refChild: Optional[QDomNodePrivate],
  ) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate
    *QDomDocumentTypePrivate::insertBefore(QDomNodePrivate *newChild,
    QDomNodePrivate *refChild)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocumenttypeprivate.html#insertBefore

    Parameters
    ----------

    newChild : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    refChild : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate *QDomDocumentTypePrivate::insertBefore(QDomNodePrivate
    #      *newChild, QDomNodePrivate *refChild)
    ritual = (
        'ritual_ZN23QDomDocumentTypePrivate12insertBeforeEP15QDomNodePrivat'
        'eS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QDomDocumentTypePrivate12insertBeforeEP15QDomNode'
          'PrivateS1_')
    address = self.uglySide.call(
        ritual, self._addressOf(newChild), self._addressOf(refChild),
    )
    return QDomNodePrivate._cuteAt(address)

  @overload(QDomNodePrivate, QDomNodePrivate)
  @overload(QDomNodePrivate, NoneType)
  @overload(NoneType, QDomNodePrivate)
  @overload(NoneType, NoneType)
  def insertAfter(
      self,
      newChild: Optional[QDomNodePrivate],
      refChild: Optional[QDomNodePrivate],
  ) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate
    *QDomDocumentTypePrivate::insertAfter(QDomNodePrivate *newChild,
    QDomNodePrivate *refChild)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocumenttypeprivate.html#insertAfter

    Parameters
    ----------

    newChild : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    refChild : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate *QDomDocumentTypePrivate::insertAfter(QDomNodePrivate
    #      *newChild, QDomNodePrivate *refChild)
    ritual = (
        'ritual_ZN23QDomDocumentTypePrivate11insertAfterEP15QDomNodePrivate'
        'S1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QDomDocumentTypePrivate11insertAfterEP15QDomNodeP'
          'rivateS1_')
    address = self.uglySide.call(
        ritual, self._addressOf(newChild), self._addressOf(refChild),
    )
    return QDomNodePrivate._cuteAt(address)

  @overload(QDomNodePrivate, QDomNodePrivate)
  @overload(QDomNodePrivate, NoneType)
  @overload(NoneType, QDomNodePrivate)
  @overload(NoneType, NoneType)
  def replaceChild(
      self,
      newChild: Optional[QDomNodePrivate],
      oldChild: Optional[QDomNodePrivate],
  ) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate
    *QDomDocumentTypePrivate::replaceChild(QDomNodePrivate *newChild,
    QDomNodePrivate *oldChild)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocumenttypeprivate.html#replaceChild

    Parameters
    ----------

    newChild : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldChild : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate *QDomDocumentTypePrivate::replaceChild(QDomNodePrivate
    #      *newChild, QDomNodePrivate *oldChild)
    ritual = (
        'ritual_ZN23QDomDocumentTypePrivate12replaceChildEP15QDomNodePrivat'
        'eS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QDomDocumentTypePrivate12replaceChildEP15QDomNode'
          'PrivateS1_')
    address = self.uglySide.call(
        ritual, self._addressOf(newChild), self._addressOf(oldChild),
    )
    return QDomNodePrivate._cuteAt(address)

  @overload(QDomNodePrivate)
  @overload(NoneType)
  def removeChild(
      self,
      oldChild: Optional[QDomNodePrivate],
  ) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate
    *QDomDocumentTypePrivate::removeChild(QDomNodePrivate *oldChild)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocumenttypeprivate.html#removeChild

    Parameters
    ----------

    oldChild : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate *QDomDocumentTypePrivate::removeChild(QDomNodePrivate
    #      *oldChild)
    ritual = (
        'ritual_ZN23QDomDocumentTypePrivate11removeChildEP15QDomNodePrivate')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QDomDocumentTypePrivate11removeChildEP15QDomNodeP'
          'rivate')
    address = self.uglySide.call(ritual, self._addressOf(oldChild))
    return QDomNodePrivate._cuteAt(address)

  @overload(QDomNodePrivate)
  @overload(NoneType)
  def appendChild(
      self,
      newChild: Optional[QDomNodePrivate],
  ) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate
    *QDomDocumentTypePrivate::appendChild(QDomNodePrivate *newChild)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocumenttypeprivate.html#appendChild

    Parameters
    ----------

    newChild : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate *QDomDocumentTypePrivate::appendChild(QDomNodePrivate
    #      *newChild)
    ritual = (
        'ritual_ZN23QDomDocumentTypePrivate11appendChildEP15QDomNodePrivate')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QDomDocumentTypePrivate11appendChildEP15QDomNodeP'
          'rivate')
    address = self.uglySide.call(ritual, self._addressOf(newChild))
    return QDomNodePrivate._cuteAt(address)
