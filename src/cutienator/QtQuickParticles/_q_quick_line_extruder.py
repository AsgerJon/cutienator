"""
QQuickLineExtruder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquicklineextruder_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickLineExtruder to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickParticleExtruder

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickLineExtruder(QQuickParticleExtruder):
  """
  The cute side of Qt's QQuickLineExtruder: a plain Python object standing in
  front of one C++ QQuickLineExtruder.

  It is built on the cute 'QQuickParticleExtruder', as Qt's
  QQuickLineExtruder is built on Qt's QQuickParticleExtruder, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickLineExtruder that has a ritual and that Python
  can call so far, 6 names in all: 'metaObject', 'tr', 'extrude', 'mirrored',
  'mirroredChanged', 'setMirrored'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickLineExtruder::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickLineExtruder::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickLineExtruder is created at the first use, not by
    'QQuickLineExtruder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLineExtruder.
  - Qt tells when it has removed the C++ QQuickLineExtruder. Every call on
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
    Calls Qt's 'QString QQuickLineExtruder::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklineextruder.html#tr

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
    #  QString QQuickLineExtruder::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickLineExtruder2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLineExtruder'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickLineExtruder::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklineextruder.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLineExtruder::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickLineExtruder10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def mirrored(self) -> bool:
    """
    Calls Qt's 'bool QQuickLineExtruder::mirrored() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklineextruder.html#mirrored
    """
    #  bool QQuickLineExtruder::mirrored() const
    return self.uglySide.call('ritual_ZNK18QQuickLineExtruder8mirroredEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setMirrored(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickLineExtruder::setMirrored(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklineextruder.html#setMirrored

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickLineExtruder::setMirrored(bool arg)
    self.uglySide.call('ritual_ZN18QQuickLineExtruder11setMirroredEb', arg)

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
    'QQuickLineExtruder::QQuickLineExtruder(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklineextruder.html#QQuickLineExtruder

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickLineExtruder::QQuickLineExtruder(QObject *parent)
    self._noteCreation(QQuickLineExtruder, lambda: Rituals.call(
        'ritual_ZN18QQuickLineExtruderC1EP7QObject',
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

  @overload(QRectF)
  def extrude(self, a0: QRectF) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickLineExtruder::extrude(const QRectF &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklineextruder.html#extrude

    Parameters
    ----------

    a0 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickLineExtruder::extrude(const QRectF &a0)
    ritual = 'ritual_ZN18QQuickLineExtruder7extrudeERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickLineExtruder7extrudeERK6QRectF'
    address = self.uglySide.call(ritual, self._valueOf(a0))
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(bool)
  def mirroredChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickLineExtruder::mirroredChanged(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklineextruder.html#mirroredChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickLineExtruder::mirroredChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN18QQuickLineExtruder15mirroredChangedEb', arg,
    )
