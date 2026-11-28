"""
QQuickTranslate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktranslate_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTranslate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickTransform

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QMatrix4x4
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTranslate(QQuickTransform):
  """
  The cute side of Qt's QQuickTranslate: a plain Python object standing in
  front of one C++ QQuickTranslate.

  It is built on the cute 'QQuickTransform', as Qt's QQuickTranslate is built
  on Qt's QQuickTransform, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTranslate that has a ritual and that Python
  can call so far, 9 names in all: 'metaObject', 'tr', 'x', 'setX', 'y',
  'setY', 'applyTo', 'xChanged', 'yChanged'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTranslate::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickTranslate::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickTranslatePrivate *QQuickTranslate::d_func()': gives
    'QQuickTranslatePrivate', which has no cute class yet.
  - Qt's 'const QQuickTranslatePrivate *QQuickTranslate::d_func() const':
    gives 'QQuickTranslatePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickTranslate is created at the first use, not by
    'QQuickTranslate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTranslate.
  - Qt tells when it has removed the C++ QQuickTranslate. Every call on the
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
    Calls Qt's 'QString QQuickTranslate::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktranslate.html#tr

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
    #  QString QQuickTranslate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickTranslate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTranslate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTranslate::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktranslate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTranslate::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickTranslate10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def x(self) -> float:
    """
    Calls Qt's 'qreal QQuickTranslate::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktranslate.html#x
    """
    #  qreal QQuickTranslate::x() const
    return self.uglySide.call('ritual_ZNK15QQuickTranslate1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QQuickTranslate::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktranslate.html#y
    """
    #  qreal QQuickTranslate::y() const
    return self.uglySide.call('ritual_ZNK15QQuickTranslate1yEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickTranslate::setX(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktranslate.html#setX

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickTranslate::setX(qreal a0)
    self.uglySide.call('ritual_ZN15QQuickTranslate4setXEd', a0)

  @overload(float)
  def setY(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickTranslate::setY(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktranslate.html#setY

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickTranslate::setY(qreal a0)
    self.uglySide.call('ritual_ZN15QQuickTranslate4setYEd', a0)

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
    Notes what was given, for Qt's 'QQuickTranslate::QQuickTranslate(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktranslate.html#QQuickTranslate

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTranslate::QQuickTranslate(QObject *parent)
    self._noteCreation(QQuickTranslate, lambda: Rituals.call(
        'ritual_ZN15QQuickTranslateC1EP7QObject',
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

  @overload(QMatrix4x4)
  @overload(NoneType)
  def applyTo(self, matrix: Optional[QMatrix4x4]) -> None:
    """
    Calls Qt's 'void QQuickTranslate::applyTo(QMatrix4x4 *matrix) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktranslate.html#applyTo

    Parameters
    ----------

    matrix : Optional[QMatrix4x4]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTranslate::applyTo(QMatrix4x4 *matrix) const
    ritual = 'ritual_ZNK15QQuickTranslate7applyToEP10QMatrix4x4'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickTranslate7applyToEP10QMatrix4x4'
    self.uglySide.call(ritual, self._addressOf(matrix))

  def xChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTranslate::xChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktranslate.html#xChanged
    """
    #  void QQuickTranslate::xChanged()
    self.uglySide.call('ritual_ZN15QQuickTranslate8xChangedEv')

  def yChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTranslate::yChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktranslate.html#yChanged
    """
    #  void QQuickTranslate::yChanged()
    self.uglySide.call('ritual_ZN15QQuickTranslate8yChangedEv')
