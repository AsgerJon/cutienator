"""
QQuickItemParticleAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickitemparticle_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickItemParticleAttached to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickItemParticle


class QQuickItemParticleAttached(QObject):
  """
  The cute side of Qt's QQuickItemParticleAttached: a plain Python object
  standing in front of one C++ QQuickItemParticleAttached.

  It is built on the cute 'QObject', as Qt's QQuickItemParticleAttached is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickItemParticleAttached that has a ritual and
  that Python can call so far, 4 names in all: 'metaObject', 'particle',
  'detached', 'attached'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickItemParticleAttached::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickItemParticleAttached::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  6 of the 12 functions Qt declares: 4 leans on 'QQuickItemParticleAttached;
  2 not a gap.

  What to expect
  --------------

  - The C++ QQuickItemParticleAttached is created at the first use, not by
    'QQuickItemParticleAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickItemParticleAttached.
  - Qt tells when it has removed the C++ QQuickItemParticleAttached. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickItemParticleAttached that has no cute function
    yet, '__init__', 'attach', 'detach', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickItemParticleAttached'

  #  A C++ QQuickItemParticleAttached Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickItemParticleAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickItemParticleAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemparticleattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickItemParticleAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickItemParticleAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def particle(self) -> Optional[QQuickItemParticle]:
    """
    Calls Qt's 'QQuickItemParticle *QQuickItemParticleAttached::particle()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemparticleattached.html#particle

    Returns
    -------

    Optional[QQuickItemParticle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItemParticle *QQuickItemParticleAttached::particle() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickItemParticleAttached8particleEv',
    )
    from . import QQuickItemParticle
    return QQuickItemParticle._cuteAt(address)

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
    Qt's 'QQuickItemParticleAttached::QQuickItemParticleAttached(QObject
    *parent)': leans on
    'QQuickItemParticleAttached::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickItemParticleAttached.__init__' has no cute function yet. "
        "Qt's "
        "'QQuickItemParticleAttached::QQuickItemParticleAttached(QObject "
        "*parent)': leans on "
        "'QQuickItemParticleAttached::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
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

  def detached(self) -> None:
    """
    Calls Qt's 'void QQuickItemParticleAttached::detached()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemparticleattached.html#detached
    """
    #  void QQuickItemParticleAttached::detached()
    self.uglySide.call('ritual_ZN26QQuickItemParticleAttached8detachedEv')

  def attached(self) -> None:
    """
    Calls Qt's 'void QQuickItemParticleAttached::attached()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemparticleattached.html#attached
    """
    #  void QQuickItemParticleAttached::attached()
    self.uglySide.call('ritual_ZN26QQuickItemParticleAttached8attachedEv')

  @staticmethod
  def attach(*__, **_) -> Never:
    """
    Qt's 'void QQuickItemParticleAttached::attach()': leans on
    'QQuickItemParticleAttached::attached()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickItemParticleAttached.attach' has no cute function yet. Qt's "
        "'void QQuickItemParticleAttached::attach()': leans on "
        "'QQuickItemParticleAttached::attached()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def detach(*__, **_) -> Never:
    """
    Qt's 'void QQuickItemParticleAttached::detach()': leans on
    'QQuickItemParticleAttached::detached()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickItemParticleAttached.detach' has no cute function yet. Qt's "
        "'void QQuickItemParticleAttached::detach()': leans on "
        "'QQuickItemParticleAttached::detached()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
