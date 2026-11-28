"""
QPlaceIdReply binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplaceidreply.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject
from . import QPlaceReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlaceIdReply(QPlaceReply):
  """
  The cute side of Qt's QPlaceIdReply: a plain Python object standing in
  front of one C++ QPlaceIdReply.

  It is built on the cute 'QPlaceReply', as Qt's QPlaceIdReply is built on
  Qt's QPlaceReply, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlaceIdReply that has a ritual and that Python can
  call so far, 6 names in all: 'metaObject', 'tr', 'type', 'operationType',
  'id', 'setId'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlaceIdReply::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QPlaceIdReply::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QPlaceIdReply::~QPlaceIdReply()': the destructor: Python never
    removes a C++ QPlaceIdReply.
  - Qt's 'QPlaceIdReplyPrivate *QPlaceIdReply::d_func()': gives
    'QPlaceIdReplyPrivate', which has no cute class yet.
  - Qt's 'const QPlaceIdReplyPrivate *QPlaceIdReply::d_func() const': gives
    'QPlaceIdReplyPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QPlaceIdReply is created at the first use, not by
    'QPlaceIdReply(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlaceIdReply.
  - Qt tells when it has removed the C++ QPlaceIdReply. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QPlaceIdReply, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class OperationType(CuteNum):
    """
    The enum 'QPlaceIdReply::OperationType' of Qt, with the 4 names Qt gives
    in it.
    """

    SavePlace = Kee[int](0)
    SaveCategory = Kee[int](1)
    RemovePlace = Kee[int](2)
    RemoveCategory = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QPlaceIdReply::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceidreply.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceIdReply::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QPlaceIdReply2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaceIdReply'

  #  A C++ QPlaceIdReply Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlaceIdReply'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPlaceIdReply::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceidreply.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlaceIdReply::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QPlaceIdReply10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> QPlaceReply.Type:
    """
    Calls Qt's 'QPlaceReply::Type QPlaceIdReply::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceidreply.html#type

    Returns
    -------

    QPlaceReply.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QPlaceReply.Type(number)'
      gives.
    """
    #  QPlaceReply::Type QPlaceIdReply::type() const
    ritual = 'ritual_ZNK13QPlaceIdReply4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QPlaceIdReply4typeEv'
    return QPlaceReply.Type(self.uglySide.call(ritual))

  def operationType(self) -> OperationType:
    """
    Calls Qt's 'OperationType QPlaceIdReply::operationType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceidreply.html#operationType

    Returns
    -------

    OperationType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'OperationType(number)'
      gives.
    """
    #  OperationType QPlaceIdReply::operationType() const
    return QPlaceIdReply.OperationType(self.uglySide.call(
        'ritual_ZNK13QPlaceIdReply13operationTypeEv',
    ))

  def id(self) -> str:
    """
    Calls Qt's 'QString QPlaceIdReply::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceidreply.html#id

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceIdReply::id() const
    return self.uglySide.call('ritual_ZNK13QPlaceIdReply2idEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setId(self, identifier: str) -> None:
    """
    Calls Qt's 'void QPlaceIdReply::setId(const QString &identifier)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceidreply.html#setId

    Parameters
    ----------

    identifier : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceIdReply::setId(const QString &identifier)
    self.uglySide.call(
        'ritual_ZN13QPlaceIdReply5setIdERK7QString', identifier,
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

  @overload(OperationType)
  @overload(OperationType, QObject)
  @overload(OperationType, NoneType)
  def __init__(
      self,
      operationType: OperationType,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QPlaceIdReply::QPlaceIdReply(OperationType operationType, QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplaceidreply.html#QPlaceIdReply

    Parameters
    ----------

    operationType : OperationType
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPlaceIdReply::QPlaceIdReply(OperationType operationType, QObject
    #      *parent)
    self._noteCreation(QPlaceIdReply, lambda: Rituals.call(
        'ritual_ZN13QPlaceIdReplyC1ENS_13OperationTypeEP7QObject',
        operationType.value, self._addressOf(parent, 'QObject'),
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
