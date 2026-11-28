"""
QQuickRoundButton binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickroundbutton_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickRoundButton to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem
from . import QQuickButton

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickRoundButton(QQuickButton):
  """
  The cute side of Qt's QQuickRoundButton: a plain Python object standing in
  front of one C++ QQuickRoundButton.

  It is built on the cute 'QQuickButton', as Qt's QQuickRoundButton is built
  on Qt's QQuickButton, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickRoundButton that has a ritual and that Python
  can call so far, 7 names in all: 'metaObject', 'tr', 'radius', 'setRadius',
  'resetRadius', 'radiusChanged', 'geometryChange'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickRoundButton::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickRoundButton::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickRoundButtonPrivate *QQuickRoundButton::d_func()': gives
    'QQuickRoundButtonPrivate', which has no cute class yet.
  - Qt's 'const QQuickRoundButtonPrivate *QQuickRoundButton::d_func() const':
    gives 'QQuickRoundButtonPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickRoundButton is created at the first use, not by
    'QQuickRoundButton(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRoundButton.
  - Qt tells when it has removed the C++ QQuickRoundButton. Every call on the
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
    Calls Qt's 'QString QQuickRoundButton::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickroundbutton.html#tr

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
    #  QString QQuickRoundButton::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickRoundButton2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRoundButton'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickRoundButton::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickroundbutton.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickRoundButton::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickRoundButton10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def radius(self) -> float:
    """
    Calls Qt's 'qreal QQuickRoundButton::radius() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickroundbutton.html#radius
    """
    #  qreal QQuickRoundButton::radius() const
    return self.uglySide.call('ritual_ZNK17QQuickRoundButton6radiusEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQuickRoundButton::setRadius(qreal radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickroundbutton.html#setRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQuickRoundButton::setRadius(qreal radius)
    self.uglySide.call('ritual_ZN17QQuickRoundButton9setRadiusEd', radius)

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
    'QQuickRoundButton::QQuickRoundButton(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickroundbutton.html#QQuickRoundButton

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickRoundButton::QQuickRoundButton(QQuickItem *parent)
    self._noteCreation(QQuickRoundButton, lambda: Rituals.call(
        'ritual_ZN17QQuickRoundButtonC1EP10QQuickItem',
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

  def resetRadius(self) -> None:
    """
    Calls Qt's 'void QQuickRoundButton::resetRadius()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickroundbutton.html#resetRadius
    """
    #  void QQuickRoundButton::resetRadius()
    self.uglySide.call('ritual_ZN17QQuickRoundButton11resetRadiusEv')

  def radiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRoundButton::radiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickroundbutton.html#radiusChanged
    """
    #  void QQuickRoundButton::radiusChanged()
    self.uglySide.call('ritual_ZN17QQuickRoundButton13radiusChangedEv')

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickRoundButton::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickroundbutton.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickRoundButton::geometryChange(const QRectF &newGeometry,
    #      const QRectF &oldGeometry)
    ritual = 'ritual_ZN17QQuickRoundButton14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickRoundButton14geometryChangeERK6QRectFS2_')
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )
