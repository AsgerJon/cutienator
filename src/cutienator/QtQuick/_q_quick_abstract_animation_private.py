"""
QQuickAbstractAnimationPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickAbstractAnimationPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from ..QtQml import QAnimationJobChangeListener

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QString
  from ..QtQml import QAbstractAnimationJob, QQmlProperty
  from . import QQuickAbstractAnimation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractAnimationJob = WAIT['QAbstractAnimationJob']
  QObject = WAIT['QObject']
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAbstractAnimationPrivate(QObjectPrivate, QAnimationJobChangeListener):
  """
  The cute side of Qt's QQuickAbstractAnimationPrivate: a plain Python object
  standing in front of one C++ QQuickAbstractAnimationPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QQuickAbstractAnimationPrivate is built on Qt's QObjectPrivate, and has
  everything that class has. It is built on the cute
  'QAnimationJobChangeListener' as well, as Qt's
  QQuickAbstractAnimationPrivate is built on Qt's QAnimationJobChangeListener
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAbstractAnimationPrivate that has a ritual and
  that Python can call so far, 5 names in all: 'q_func', 'commence',
  'animationFinished', 'createProperty', 'animationGroupDirty'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickAbstractAnimation
    *QQuickAbstractAnimationPrivate::q_func() const': takes in Python what
    'QQuickAbstractAnimation *QQuickAbstractAnimationPrivate::q_func()'
    takes.

  What to expect
  --------------

  - The C++ QQuickAbstractAnimationPrivate is created at the first use, not
    by 'QQuickAbstractAnimationPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAbstractAnimationPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QObject, str, QObject)
  @overload(QObject, str, NoneType)
  @overload(NoneType, str, QObject)
  @overload(NoneType, str, NoneType)
  @overload(QObject, str, QObject, QString)
  @overload(QObject, str, QObject, NoneType)
  @overload(QObject, str, NoneType, QString)
  @overload(QObject, str, NoneType, NoneType)
  @overload(NoneType, str, QObject, QString)
  @overload(NoneType, str, QObject, NoneType)
  @overload(NoneType, str, NoneType, QString)
  @overload(NoneType, str, NoneType, NoneType)
  def createProperty(
      obj: Optional[QObject],
      str: str,
      infoObj: Optional[QObject],
      errorMessage: Optional[QString] = None,
  ) -> QQmlProperty:
    """
    Calls Qt's 'QQmlProperty
    QQuickAbstractAnimationPrivate::createProperty(QObject *obj, const
    QString &str, QObject *infoObj, QString *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimationprivate.html#createProperty

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    str : str
      Passed on as it is: a QString is made of it for the call.

    infoObj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QQmlProperty
      A new cute QQmlProperty around the copy Qt gave back. Python owns it.
    """
    #  QQmlProperty QQuickAbstractAnimationPrivate::createProperty(QObject
    #      *obj, const QString &str, QObject *infoObj, QString *errorMessage)
    address = Rituals.call(
        'ritual_ZN30QQuickAbstractAnimationPrivate14createPropertyEP7QObjec'
        'tRK7QStringS1_PS2_',
        CuteMixin._addressOf(obj, 'QObject'), str,
        CuteMixin._addressOf(infoObj, 'QObject'),
        CuteMixin._addressOf(errorMessage),
    )
    from ..QtQml import QQmlProperty
    return QQmlProperty._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAbstractAnimationPrivate'

  #  Qt's QQuickAbstractAnimationPrivate is built on more than one class. The
  #  part of a C++ QQuickAbstractAnimationPrivate that belongs to a class
  #  after the first begins somewhere inside the object, and the ritual named
  #  for that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAnimationJobChangeListener':
          'ritual_cast_QQuickAbstractAnimationPrivate_QAnimationJobChangeListener',
  }

  #  A C++ QQuickAbstractAnimationPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAbstractAnimationPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuickAbstractAnimationPrivate::QQuickAbstractAnimationPrivate()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimationprivate.html
    """
    #  QQuickAbstractAnimationPrivate::QQuickAbstractAnimationPrivate()
    self._noteCreation(QQuickAbstractAnimationPrivate, lambda: Rituals.call(
        'ritual_ZN30QQuickAbstractAnimationPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickAbstractAnimation]:
    """
    Calls Qt's 'QQuickAbstractAnimation
    *QQuickAbstractAnimationPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimationprivate.html#q_func

    Returns
    -------

    Optional[QQuickAbstractAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAbstractAnimation *QQuickAbstractAnimationPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN30QQuickAbstractAnimationPrivate6q_funcEv',
    )
    from . import QQuickAbstractAnimation
    return QQuickAbstractAnimation._cuteAt(address)

  def commence(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimationPrivate::commence()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimationprivate.html#commence
    """
    #  void QQuickAbstractAnimationPrivate::commence()
    self.uglySide.call(
        'ritual_ZN30QQuickAbstractAnimationPrivate8commenceEv',
    )

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def animationFinished(self, a0: Optional[QAbstractAnimationJob]) -> None:
    """
    Calls Qt's 'void
    QQuickAbstractAnimationPrivate::animationFinished(QAbstractAnimationJob
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimationprivate.html

    Parameters
    ----------

    a0 : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractAnimationPrivate::animationFinished(
    #      QAbstractAnimationJob *a0)
    ritual = (
        'ritual_ZN30QQuickAbstractAnimationPrivate17animationFinishedEP21QA'
        'bstractAnimationJob')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickAbstractAnimationPrivate17animationFinished'
          'EP21QAbstractAnimationJob')
    self.uglySide.call(ritual, self._addressOf(a0, 'QAbstractAnimationJob'))

  def animationGroupDirty(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractAnimationPrivate::animationGroupDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractanimationprivate.html
    """
    #  void QQuickAbstractAnimationPrivate::animationGroupDirty()
    self.uglySide.call(
        'ritual_ZN30QQuickAbstractAnimationPrivate19animationGroupDirtyEv',
    )
