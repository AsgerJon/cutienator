"""
QPlaceMatchReply binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplacematchreply.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QPlaceReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QPlace, QPlaceMatchRequest
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlace = WAIT['QPlace']
  QPlaceMatchRequest = WAIT['QPlaceMatchRequest']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlaceMatchReply(QPlaceReply):
  """
  The cute side of Qt's QPlaceMatchReply: a plain Python object standing in
  front of one C++ QPlaceMatchReply.

  It is built on the cute 'QPlaceReply', as Qt's QPlaceMatchReply is built on
  Qt's QPlaceReply, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlaceMatchReply that has a ritual and that Python
  can call so far, 7 names in all: 'metaObject', 'tr', 'type', 'places',
  'request', 'setPlaces', 'setRequest'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlaceMatchReply::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QPlaceMatchReply::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QPlaceMatchReply::~QPlaceMatchReply()': the destructor: Python
    never removes a C++ QPlaceMatchReply.
  - Qt's 'QPlaceMatchReplyPrivate *QPlaceMatchReply::d_func()': gives
    'QPlaceMatchReplyPrivate', which has no cute class yet.
  - Qt's 'const QPlaceMatchReplyPrivate *QPlaceMatchReply::d_func() const':
    gives 'QPlaceMatchReplyPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QPlaceMatchReply is created at the first use, not by
    'QPlaceMatchReply(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlaceMatchReply.
  - Qt tells when it has removed the C++ QPlaceMatchReply. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QPlaceMatchReply::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacematchreply.html#tr

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
    #  QString QPlaceMatchReply::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QPlaceMatchReply2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaceMatchReply'

  #  A C++ QPlaceMatchReply Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlaceMatchReply'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPlaceMatchReply::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacematchreply.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlaceMatchReply::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QPlaceMatchReply10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> QPlaceReply.Type:
    """
    Calls Qt's 'QPlaceReply::Type QPlaceMatchReply::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacematchreply.html#type

    Returns
    -------

    QPlaceReply.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QPlaceReply.Type(number)'
      gives.
    """
    #  QPlaceReply::Type QPlaceMatchReply::type() const
    ritual = 'ritual_ZNK16QPlaceMatchReply4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QPlaceMatchReply4typeEv'
    return QPlaceReply.Type(self.uglySide.call(ritual))

  def places(self) -> QList[QPlace]:
    """
    Calls Qt's 'QList<QPlace> QPlaceMatchReply::places() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacematchreply.html#places

    Returns
    -------

    QList[QPlace]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPlace> QPlaceMatchReply::places() const
    address = self.uglySide.call('ritual_ZNK16QPlaceMatchReply6placesEv')
    from . import QPlace
    return QList[QPlace]._cuteOwning(address)

  def request(self) -> QPlaceMatchRequest:
    """
    Calls Qt's 'QPlaceMatchRequest QPlaceMatchReply::request() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacematchreply.html#request

    Returns
    -------

    QPlaceMatchRequest
      A new cute QPlaceMatchRequest around the copy Qt gave back. Python owns
      it.
    """
    #  QPlaceMatchRequest QPlaceMatchReply::request() const
    address = self.uglySide.call('ritual_ZNK16QPlaceMatchReply7requestEv')
    from . import QPlaceMatchRequest
    return QPlaceMatchRequest._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QPlace])
  def setPlaces(self, results: QList[QPlace]) -> None:
    """
    Calls Qt's 'void QPlaceMatchReply::setPlaces(const QList<QPlace>
    &results)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacematchreply.html#setPlaces

    Parameters
    ----------

    results : QList[QPlace]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPlaceMatchReply::setPlaces(const QList<QPlace> &results)
    self.uglySide.call(
        'ritual_ZN16QPlaceMatchReply9setPlacesERK5QListI6QPlaceE',
        self._valueOf(results),
    )

  @overload(QPlaceMatchRequest)
  def setRequest(self, request: QPlaceMatchRequest) -> None:
    """
    Calls Qt's 'void QPlaceMatchReply::setRequest(const QPlaceMatchRequest
    &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacematchreply.html#setRequest

    Parameters
    ----------

    request : QPlaceMatchRequest
      Passed on as a value: Qt reads the C++ QPlaceMatchRequest, which stays
      Python's own.
    """
    #  void QPlaceMatchReply::setRequest(const QPlaceMatchRequest &request)
    self.uglySide.call(
        'ritual_ZN16QPlaceMatchReply10setRequestERK18QPlaceMatchRequest',
        self._valueOf(request),
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
    'QPlaceMatchReply::QPlaceMatchReply(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacematchreply.html#QPlaceMatchReply

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPlaceMatchReply::QPlaceMatchReply(QObject *parent)
    self._noteCreation(QPlaceMatchReply, lambda: Rituals.call(
        'ritual_ZN16QPlaceMatchReplyC1EP7QObject',
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
