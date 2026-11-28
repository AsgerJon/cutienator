"""
QCategoryAxisPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qcategoryaxis_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QCategoryAxisPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QValueAxisPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtWidgets import QGraphicsItem
  from . import QCategoryAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCategoryAxis = WAIT['QCategoryAxis']
  QGraphicsItem = WAIT['QGraphicsItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCategoryAxisPrivate(QValueAxisPrivate):
  """
  The cute side of Qt's QCategoryAxisPrivate: a plain Python object standing
  in front of one C++ QCategoryAxisPrivate.

  It is built on the cute 'QValueAxisPrivate', as Qt's QCategoryAxisPrivate
  is built on Qt's QValueAxisPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCategoryAxisPrivate that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'tr',
  'initializeGraphics', 'ticksCount', 'q_func'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCategoryAxisPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QCategoryAxisPrivate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QCategoryAxisPrivate::~QCategoryAxisPrivate()': the destructor:
    Python never removes a C++ QCategoryAxisPrivate.
  - Qt's 'const QCategoryAxis *QCategoryAxisPrivate::q_func() const': takes
    in Python what 'QCategoryAxis *QCategoryAxisPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QCategoryAxisPrivate is created at the first use, not by
    'QCategoryAxisPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCategoryAxisPrivate.
  - Qt tells when it has removed the C++ QCategoryAxisPrivate. Every call on
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
    Calls Qt's 'QString QCategoryAxisPrivate::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcategoryaxisprivate.html#tr

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
    #  QString QCategoryAxisPrivate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QCategoryAxisPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCategoryAxisPrivate'

  #  A C++ QCategoryAxisPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCategoryAxisPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCategoryAxisPrivate::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcategoryaxisprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCategoryAxisPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QCategoryAxisPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def ticksCount(self) -> int:
    """
    Calls Qt's 'int QCategoryAxisPrivate::ticksCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcategoryaxisprivate.html#ticksCount
    """
    #  int QCategoryAxisPrivate::ticksCount() const
    return self.uglySide.call(
        'ritual_ZNK20QCategoryAxisPrivate10ticksCountEv',
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

  @overload(QCategoryAxis)
  @overload(NoneType)
  def __init__(self, q: Optional[QCategoryAxis]) -> None:
    """
    Notes what was given, for Qt's
    'QCategoryAxisPrivate::QCategoryAxisPrivate(QCategoryAxis *q)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcategoryaxisprivate.html#QCategoryAxisPrivate

    Parameters
    ----------

    q : Optional[QCategoryAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QCategoryAxisPrivate::QCategoryAxisPrivate(QCategoryAxis *q)
    self._noteCreation(QCategoryAxisPrivate, lambda: Rituals.call(
        'ritual_ZN20QCategoryAxisPrivateC1EP13QCategoryAxis',
        self._addressOf(q),
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

  @overload(QGraphicsItem)
  @overload(NoneType)
  def initializeGraphics(self, parent: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QCategoryAxisPrivate::initializeGraphics(QGraphicsItem
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcategoryaxisprivate.html#initializeGraphics

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCategoryAxisPrivate::initializeGraphics(QGraphicsItem *parent)
    ritual = (
        'ritual_ZN20QCategoryAxisPrivate18initializeGraphicsEP13QGraphicsIt'
        'em')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QCategoryAxisPrivate18initializeGraphicsEP13QGrap'
          'hicsItem')
    self.uglySide.call(ritual, self._addressOf(parent, 'QGraphicsItem'))

  def q_func(self) -> Optional[QCategoryAxis]:
    """
    Calls Qt's 'QCategoryAxis *QCategoryAxisPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcategoryaxisprivate.html#q_func

    Returns
    -------

    Optional[QCategoryAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCategoryAxis *QCategoryAxisPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QCategoryAxisPrivate6q_funcEv')
    from . import QCategoryAxis
    return QCategoryAxis._cuteAt(address)
