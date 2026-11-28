"""
QDomCharacterDataPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtXml/6.12.0/QtXml/private/qdom_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QDomCharacterDataPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QDomNode, QDomNodePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QDomCharacterDataPrivate(QDomNodePrivate):
  """
  The cute side of Qt's QDomCharacterDataPrivate: a plain Python object
  standing in front of one C++ QDomCharacterDataPrivate.

  It is built on the cute 'QDomNodePrivate', as Qt's QDomCharacterDataPrivate
  is built on Qt's QDomNodePrivate, and has everything that class has.

  C++ hands a QDomCharacterDataPrivate around as a copy, so every C++
  QDomCharacterDataPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomCharacterDataPrivate that has a ritual and that
  Python can call so far, 8 names in all: 'dataLength', 'substringData',
  'appendData', 'insertData', 'deleteData', 'replaceData', 'nodeType',
  'cloneNode'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomCharacterDataPrivate::~QDomCharacterDataPrivate()': the
    destructor: Python removes its C++ QDomCharacterDataPrivate by it, and
    has no other use for it.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 leans on 'QDomNodePrivate.

  What to expect
  --------------

  - The C++ QDomCharacterDataPrivate is created at the first use, not by
    'QDomCharacterDataPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomCharacterDataPrivate back gives a copy the ritual
    made for Python, in a new cute QDomCharacterDataPrivate.
  - Each name of Qt's QDomCharacterDataPrivate that has no cute function yet,
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
  __qt_class__ = 'QDomCharacterDataPrivate'

  #  A C++ QDomCharacterDataPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDomCharacterDataPrivate'

  #  Qt's '~QDomCharacterDataPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QDomCharacterDataPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QDomCharacterDataPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def dataLength(self) -> int:
    """
    Calls Qt's 'int QDomCharacterDataPrivate::dataLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomcharacterdataprivate.html#dataLength
    """
    #  int QDomCharacterDataPrivate::dataLength() const
    return self.uglySide.call(
        'ritual_ZNK24QDomCharacterDataPrivate10dataLengthEv',
    )

  @overload(int, int)
  def substringData(self, offset: int, count: int) -> str:
    """
    Calls Qt's 'QString QDomCharacterDataPrivate::substringData(unsigned long
    offset, unsigned long count) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomcharacterdataprivate.html#substringData

    Parameters
    ----------

    offset : int
      Passed on as it is.

    count : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomCharacterDataPrivate::substringData(unsigned long offset,
    #      unsigned long count) const
    return self.uglySide.call(
        'ritual_ZNK24QDomCharacterDataPrivate13substringDataEmm',
        offset, count,
    )

  def nodeType(self) -> QDomNode.NodeType:
    """
    Calls Qt's 'QDomNode::NodeType QDomCharacterDataPrivate::nodeType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomcharacterdataprivate.html#nodeType

    Returns
    -------

    QDomNode.NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDomNode.NodeType(number)' gives.
    """
    #  QDomNode::NodeType QDomCharacterDataPrivate::nodeType() const
    ritual = 'ritual_ZNK24QDomCharacterDataPrivate8nodeTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QDomCharacterDataPrivate8nodeTypeEv'
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
      'QDomCharacterDataPrivate::QDomCharacterDataPrivate(QDomDocumentPrivate
      *a0, QDomNodePrivate *parent, const QString &data)': leans on
      'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*,
      QDomNodePrivate*)', which Qt's source does not mark for use from
      outside Qt and has no code for that could be taken.
    - Qt's 'QDomCharacterDataPrivate::QDomCharacterDataPrivate(
      QDomCharacterDataPrivate *n, bool deep)': leans on
      'QDomNodePrivate::QDomNodePrivate(QDomNodePrivate*, bool)', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    """
    raise NotImplementedError(
        "'QDomCharacterDataPrivate.__init__' has no cute function yet. Qt's "
        "'QDomCharacterDataPrivate::QDomCharacterDataPrivate(QDomDocumentPri"
        "vate *a0, QDomNodePrivate *parent, const QString &data)': leans on "
        "'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*, "
        "QDomNodePrivate*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken. Qt's "
        "'QDomCharacterDataPrivate::QDomCharacterDataPrivate(QDomCharacterDa"
        "taPrivate *n, bool deep)': leans on "
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

  @overload(str)
  def appendData(self, arg: str) -> None:
    """
    Calls Qt's 'void QDomCharacterDataPrivate::appendData(const QString
    &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomcharacterdataprivate.html#appendData

    Parameters
    ----------

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDomCharacterDataPrivate::appendData(const QString &arg)
    self.uglySide.call(
        'ritual_ZN24QDomCharacterDataPrivate10appendDataERK7QString', arg,
    )

  @overload(int, str)
  def insertData(self, offset: int, arg: str) -> None:
    """
    Calls Qt's 'void QDomCharacterDataPrivate::insertData(unsigned long
    offset, const QString &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomcharacterdataprivate.html#insertData

    Parameters
    ----------

    offset : int
      Passed on as it is.

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDomCharacterDataPrivate::insertData(unsigned long offset, const
    #      QString &arg)
    self.uglySide.call(
        'ritual_ZN24QDomCharacterDataPrivate10insertDataEmRK7QString',
        offset, arg,
    )

  @overload(int, int)
  def deleteData(self, offset: int, count: int) -> None:
    """
    Calls Qt's 'void QDomCharacterDataPrivate::deleteData(unsigned long
    offset, unsigned long count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomcharacterdataprivate.html#deleteData

    Parameters
    ----------

    offset : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QDomCharacterDataPrivate::deleteData(unsigned long offset,
    #      unsigned long count)
    self.uglySide.call(
        'ritual_ZN24QDomCharacterDataPrivate10deleteDataEmm', offset, count,
    )

  @overload(int, int, str)
  def replaceData(self, offset: int, count: int, arg: str) -> None:
    """
    Calls Qt's 'void QDomCharacterDataPrivate::replaceData(unsigned long
    offset, unsigned long count, const QString &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomcharacterdataprivate.html#replaceData

    Parameters
    ----------

    offset : int
      Passed on as it is.

    count : int
      Passed on as it is.

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDomCharacterDataPrivate::replaceData(unsigned long offset,
    #      unsigned long count, const QString &arg)
    self.uglySide.call(
        'ritual_ZN24QDomCharacterDataPrivate11replaceDataEmmRK7QString',
        offset, count, arg,
    )

  @overload()
  @overload(bool)
  def cloneNode(self, deep: bool = True) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate *QDomCharacterDataPrivate::cloneNode(bool
    deep)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomcharacterdataprivate.html#cloneNode

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
    #  QDomNodePrivate *QDomCharacterDataPrivate::cloneNode(bool deep)
    address = self.uglySide.call(
        'ritual_ZN24QDomCharacterDataPrivate9cloneNodeEb', deep,
    )
    return QDomNodePrivate._cuteAt(address)
