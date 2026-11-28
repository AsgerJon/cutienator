"""
QQuickPointHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpointhandler_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickPointHandler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuickSinglePointHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QEventPoint, QPointerEvent, QVector2D
  from . import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEventPoint = WAIT['QEventPoint']
  QPointerEvent = WAIT['QPointerEvent']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPointHandler(QQuickSinglePointHandler):
  """
  The cute side of Qt's QQuickPointHandler: a plain Python object standing in
  front of one C++ QQuickPointHandler.

  It is built on the cute 'QQuickSinglePointHandler', as Qt's
  QQuickPointHandler is built on Qt's QQuickSinglePointHandler, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPointHandler that has a ritual and that Python
  can call so far, 5 names in all: 'metaObject', 'tr', 'translation',
  'translationChanged', 'wantsEventPoint'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPointHandler::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickPointHandler::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickPointHandler::handleEventPoint(QPointerEvent *event,
    QEventPoint &point)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPointHandler is created at the first use, not by
    'QQuickPointHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPointHandler.
  - Qt tells when it has removed the C++ QQuickPointHandler. Every call on
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
    Calls Qt's 'QString QQuickPointHandler::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpointhandler.html#tr

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
    #  QString QQuickPointHandler::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickPointHandler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPointHandler'

  #  A C++ QQuickPointHandler Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPointHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPointHandler::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpointhandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPointHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickPointHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def translation(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D QQuickPointHandler::translation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointhandler.html#translation

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QQuickPointHandler::translation() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickPointHandler11translationEv',
    )
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickPointHandler::QQuickPointHandler(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointhandler.html#QQuickPointHandler

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPointHandler::QQuickPointHandler(QQuickItem *parent)
    self._noteCreation(QQuickPointHandler, lambda: Rituals.call(
        'ritual_ZN18QQuickPointHandlerC1EP10QQuickItem',
        self._addressOf(parent),
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

  def translationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPointHandler::translationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointhandler.html#translationChanged
    """
    #  void QQuickPointHandler::translationChanged()
    self.uglySide.call('ritual_ZN18QQuickPointHandler18translationChangedEv')

  @overload(QPointerEvent, QEventPoint)
  @overload(NoneType, QEventPoint)
  def wantsEventPoint(
      self,
      event: Optional[QPointerEvent],
      point: QEventPoint,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickPointHandler::wantsEventPoint(const QPointerEvent
    *event, const QEventPoint &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpointhandler.html#wantsEventPoint

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  bool QQuickPointHandler::wantsEventPoint(const QPointerEvent *event,
    #      const QEventPoint &point)
    ritual = (
        'ritual_ZN18QQuickPointHandler15wantsEventPointEPK13QPointerEventRK'
        '11QEventPoint')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickPointHandler15wantsEventPointEPK13QPointerE'
          'ventRK11QEventPoint')
    return self.uglySide.call(
        ritual, self._addressOf(event), self._valueOf(point),
    )
