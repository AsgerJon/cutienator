"""
QQuickUniformAnimator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimator_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickUniformAnimator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickAnimator

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickAnimatorJob, QQuickUniformAnimatorPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickUniformAnimator(QQuickAnimator):
  """
  The cute side of Qt's QQuickUniformAnimator: a plain Python object standing
  in front of one C++ QQuickUniformAnimator.

  It is built on the cute 'QQuickAnimator', as Qt's QQuickUniformAnimator is
  built on Qt's QQuickAnimator, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickUniformAnimator that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr', 'd_func',
  'uniform', 'setUniform', 'uniformChanged', 'createJob', 'propertyName'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickUniformAnimator::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickUniformAnimator::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickUniformAnimatorPrivate *QQuickUniformAnimator::d_func()
    const': takes in Python what 'QQuickUniformAnimatorPrivate
    *QQuickUniformAnimator::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickUniformAnimator is created at the first use, not by
    'QQuickUniformAnimator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickUniformAnimator.
  - Qt tells when it has removed the C++ QQuickUniformAnimator. Every call on
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
    Calls Qt's 'QString QQuickUniformAnimator::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickuniformanimator.html#tr

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
    #  QString QQuickUniformAnimator::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickUniformAnimator2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickUniformAnimator'

  #  A C++ QQuickUniformAnimator Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickUniformAnimator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickUniformAnimator::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniformanimator.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickUniformAnimator::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickUniformAnimator10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def uniform(self) -> str:
    """
    Calls Qt's 'QString QQuickUniformAnimator::uniform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickuniformanimator.html#uniform

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickUniformAnimator::uniform() const
    return self.uglySide.call('ritual_ZNK21QQuickUniformAnimator7uniformEv')

  def createJob(self) -> Optional[QQuickAnimatorJob]:
    """
    Calls Qt's 'QQuickAnimatorJob *QQuickUniformAnimator::createJob() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniformanimator.html#createJob

    Returns
    -------

    Optional[QQuickAnimatorJob]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAnimatorJob *QQuickUniformAnimator::createJob() const
    ritual = 'ritual_ZNK21QQuickUniformAnimator9createJobEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QQuickUniformAnimator9createJobEv'
    address = self.uglySide.call(ritual)
    from . import QQuickAnimatorJob
    return QQuickAnimatorJob._cuteAt(address)

  def propertyName(self) -> str:
    """
    Calls Qt's 'QString QQuickUniformAnimator::propertyName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniformanimator.html#propertyName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickUniformAnimator::propertyName() const
    ritual = 'ritual_ZNK21QQuickUniformAnimator12propertyNameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QQuickUniformAnimator12propertyNameEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setUniform(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickUniformAnimator::setUniform(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniformanimator.html#setUniform

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickUniformAnimator::setUniform(const QString &a0)
    self.uglySide.call(
        'ritual_ZN21QQuickUniformAnimator10setUniformERK7QString', a0,
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
    'QQuickUniformAnimator::QQuickUniformAnimator(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniformanimator.html#QQuickUniformAnimator

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickUniformAnimator::QQuickUniformAnimator(QObject *parent)
    self._noteCreation(QQuickUniformAnimator, lambda: Rituals.call(
        'ritual_ZN21QQuickUniformAnimatorC1EP7QObject',
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

  def d_func(self) -> Optional[QQuickUniformAnimatorPrivate]:
    """
    Calls Qt's 'QQuickUniformAnimatorPrivate
    *QQuickUniformAnimator::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickuniformanimator.html#d_func

    Returns
    -------

    Optional[QQuickUniformAnimatorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickUniformAnimatorPrivate *QQuickUniformAnimator::d_func()
    address = self.uglySide.call('ritual_ZN21QQuickUniformAnimator6d_funcEv')
    from . import QQuickUniformAnimatorPrivate
    return QQuickUniformAnimatorPrivate._cuteAt(address)

  @overload(str)
  def uniformChanged(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickUniformAnimator::uniformChanged(const QString
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniformanimator.html#uniformChanged

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickUniformAnimator::uniformChanged(const QString &a0)
    self.uglySide.call(
        'ritual_ZN21QQuickUniformAnimator14uniformChangedERK7QString', a0,
    )
