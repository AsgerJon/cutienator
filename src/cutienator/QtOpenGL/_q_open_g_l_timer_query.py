"""
QOpenGLTimerQuery binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopengltimerquery.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLTimerQuery(QObject):
  """
  The cute side of Qt's QOpenGLTimerQuery: a plain Python object standing in
  front of one C++ QOpenGLTimerQuery.

  It is built on the cute 'QObject', as Qt's QOpenGLTimerQuery is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLTimerQuery that has a ritual and that Python
  can call so far, 12 names in all: 'metaObject', 'tr', 'create', 'destroy',
  'isCreated', 'objectId', 'begin', 'end', 'waitForTimestamp',
  'recordTimestamp', 'isResultAvailable', 'waitForResult'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOpenGLTimerQuery::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QOpenGLTimerQuery::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QOpenGLTimerQuery::~QOpenGLTimerQuery()': the destructor: Python
    never removes a C++ QOpenGLTimerQuery.
  - Qt's 'QOpenGLTimerQueryPrivate *QOpenGLTimerQuery::d_func()': gives
    'QOpenGLTimerQueryPrivate', which has no cute class yet.
  - Qt's 'const QOpenGLTimerQueryPrivate *QOpenGLTimerQuery::d_func() const':
    gives 'QOpenGLTimerQueryPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 22 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QOpenGLTimerQuery is created at the first use, not by
    'QOpenGLTimerQuery(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLTimerQuery.
  - Qt tells when it has removed the C++ QOpenGLTimerQuery. Every call on the
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
    Calls Qt's 'QString QOpenGLTimerQuery::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltimerquery.html#tr

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
    #  QString QOpenGLTimerQuery::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QOpenGLTimerQuery2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLTimerQuery'

  #  A C++ QOpenGLTimerQuery Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLTimerQuery'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOpenGLTimerQuery::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltimerquery.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpenGLTimerQuery::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QOpenGLTimerQuery10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isCreated(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLTimerQuery::isCreated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltimerquery.html#isCreated
    """
    #  bool QOpenGLTimerQuery::isCreated() const
    return self.uglySide.call('ritual_ZNK17QOpenGLTimerQuery9isCreatedEv')

  def objectId(self) -> int:
    """
    Calls Qt's 'GLuint QOpenGLTimerQuery::objectId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltimerquery.html#objectId
    """
    #  GLuint QOpenGLTimerQuery::objectId() const
    return self.uglySide.call('ritual_ZNK17QOpenGLTimerQuery8objectIdEv')

  def waitForTimestamp(self) -> int:
    """
    Calls Qt's 'GLuint64 QOpenGLTimerQuery::waitForTimestamp() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltimerquery.html#waitForTimestamp
    """
    #  GLuint64 QOpenGLTimerQuery::waitForTimestamp() const
    return self.uglySide.call(
        'ritual_ZNK17QOpenGLTimerQuery16waitForTimestampEv',
    )

  def isResultAvailable(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLTimerQuery::isResultAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltimerquery.html#isResultAvailable
    """
    #  bool QOpenGLTimerQuery::isResultAvailable() const
    return self.uglySide.call(
        'ritual_ZNK17QOpenGLTimerQuery17isResultAvailableEv',
    )

  def waitForResult(self) -> int:
    """
    Calls Qt's 'GLuint64 QOpenGLTimerQuery::waitForResult() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltimerquery.html#waitForResult
    """
    #  GLuint64 QOpenGLTimerQuery::waitForResult() const
    return self.uglySide.call(
        'ritual_ZNK17QOpenGLTimerQuery13waitForResultEv',
    )

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLTimerQuery::QOpenGLTimerQuery(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltimerquery.html#QOpenGLTimerQuery

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOpenGLTimerQuery::QOpenGLTimerQuery(QObject *parent)
    self._noteCreation(QOpenGLTimerQuery, lambda: Rituals.call(
        'ritual_ZN17QOpenGLTimerQueryC1EP7QObject',
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

  def create(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLTimerQuery::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltimerquery.html#create
    """
    #  bool QOpenGLTimerQuery::create()
    return self.uglySide.call('ritual_ZN17QOpenGLTimerQuery6createEv')

  def destroy(self) -> None:
    """
    Calls Qt's 'void QOpenGLTimerQuery::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltimerquery.html#destroy
    """
    #  void QOpenGLTimerQuery::destroy()
    self.uglySide.call('ritual_ZN17QOpenGLTimerQuery7destroyEv')

  def begin(self) -> None:
    """
    Calls Qt's 'void QOpenGLTimerQuery::begin()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltimerquery.html#begin
    """
    #  void QOpenGLTimerQuery::begin()
    self.uglySide.call('ritual_ZN17QOpenGLTimerQuery5beginEv')

  def end(self) -> None:
    """
    Calls Qt's 'void QOpenGLTimerQuery::end()'.

    Qt's own words: https://doc.qt.io/qt-6/qopengltimerquery.html#end
    """
    #  void QOpenGLTimerQuery::end()
    self.uglySide.call('ritual_ZN17QOpenGLTimerQuery3endEv')

  def recordTimestamp(self) -> None:
    """
    Calls Qt's 'void QOpenGLTimerQuery::recordTimestamp()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltimerquery.html#recordTimestamp
    """
    #  void QOpenGLTimerQuery::recordTimestamp()
    self.uglySide.call('ritual_ZN17QOpenGLTimerQuery15recordTimestampEv')
