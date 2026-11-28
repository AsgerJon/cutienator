"""
QPlaceDetailsReply binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplacedetailsreply.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QPlaceReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QPlace
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlace = WAIT['QPlace']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlaceDetailsReply(QPlaceReply):
  """
  The cute side of Qt's QPlaceDetailsReply: a plain Python object standing in
  front of one C++ QPlaceDetailsReply.

  It is built on the cute 'QPlaceReply', as Qt's QPlaceDetailsReply is built
  on Qt's QPlaceReply, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlaceDetailsReply that has a ritual and that Python
  can call so far, 5 names in all: 'metaObject', 'tr', 'type', 'place',
  'setPlace'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlaceDetailsReply::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QPlaceDetailsReply::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QPlaceDetailsReply::~QPlaceDetailsReply()': the destructor: Python
    never removes a C++ QPlaceDetailsReply.
  - Qt's 'QPlaceDetailsReplyPrivate *QPlaceDetailsReply::d_func()': gives
    'QPlaceDetailsReplyPrivate', which has no cute class yet.
  - Qt's 'const QPlaceDetailsReplyPrivate *QPlaceDetailsReply::d_func()
    const': gives 'QPlaceDetailsReplyPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QPlaceDetailsReply is created at the first use, not by
    'QPlaceDetailsReply(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlaceDetailsReply.
  - Qt tells when it has removed the C++ QPlaceDetailsReply. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

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
    Calls Qt's 'QString QPlaceDetailsReply::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacedetailsreply.html#tr

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
    #  QString QPlaceDetailsReply::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QPlaceDetailsReply2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaceDetailsReply'

  #  A C++ QPlaceDetailsReply Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlaceDetailsReply'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPlaceDetailsReply::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacedetailsreply.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlaceDetailsReply::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QPlaceDetailsReply10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> QPlaceReply.Type:
    """
    Calls Qt's 'QPlaceReply::Type QPlaceDetailsReply::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacedetailsreply.html#type

    Returns
    -------

    QPlaceReply.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QPlaceReply.Type(number)'
      gives.
    """
    #  QPlaceReply::Type QPlaceDetailsReply::type() const
    ritual = 'ritual_ZNK18QPlaceDetailsReply4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QPlaceDetailsReply4typeEv'
    return QPlaceReply.Type(self.uglySide.call(ritual))

  def place(self) -> QPlace:
    """
    Calls Qt's 'QPlace QPlaceDetailsReply::place() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacedetailsreply.html#place

    Returns
    -------

    QPlace
      A new cute QPlace around the copy Qt gave back. Python owns it.
    """
    #  QPlace QPlaceDetailsReply::place() const
    address = self.uglySide.call('ritual_ZNK18QPlaceDetailsReply5placeEv')
    from . import QPlace
    return QPlace._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPlace)
  def setPlace(self, place: QPlace) -> None:
    """
    Calls Qt's 'void QPlaceDetailsReply::setPlace(const QPlace &place)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacedetailsreply.html#setPlace

    Parameters
    ----------

    place : QPlace
      Passed on as a value: Qt reads the C++ QPlace, which stays Python's
      own.
    """
    #  void QPlaceDetailsReply::setPlace(const QPlace &place)
    self.uglySide.call(
        'ritual_ZN18QPlaceDetailsReply8setPlaceERK6QPlace',
        self._valueOf(place),
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QPlaceDetailsReply::QPlaceDetailsReply(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacedetailsreply.html#QPlaceDetailsReply

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPlaceDetailsReply::QPlaceDetailsReply(QObject *parent)
    self._noteCreation(QPlaceDetailsReply, lambda: Rituals.call(
        'ritual_ZN18QPlaceDetailsReplyC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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
