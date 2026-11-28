"""
QQuickTextUtil binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktextutil_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickTextUtil to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQuickTextUtil(QObject):
  """
  The cute side of Qt's QQuickTextUtil: a plain Python object standing in
  front of one C++ QQuickTextUtil.

  It is built on the cute 'QObject', as Qt's QQuickTextUtil is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTextUtil that has a ritual and that Python can
  call so far, 3 names in all: 'metaObject', 'alignedX', 'alignedY'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTextUtil::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickTextUtil::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  7 of the 12 functions Qt declares: 3 a template; 2 not a gap; 2 leans on
  'QQuickTextUtil.

  What to expect
  --------------

  - The C++ QQuickTextUtil is created at the first use, not by
    'QQuickTextUtil(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTextUtil.
  - Qt tells when it has removed the C++ QQuickTextUtil. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickTextUtil that has no cute function yet,
    'createCursor', 'setCursorDelegate', 'textRenderType', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(float, float, int)
  def alignedX(textWidth: float, itemWidth: float, alignment: int) -> float:
    """
    Calls Qt's 'qreal QQuickTextUtil::alignedX(qreal textWidth, qreal
    itemWidth, int alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextutil.html#alignedX

    Parameters
    ----------

    textWidth : float
      Passed on as it is.

    itemWidth : float
      Passed on as it is.

    alignment : int
      Passed on as it is.
    """
    #  qreal QQuickTextUtil::alignedX(qreal textWidth, qreal itemWidth, int
    #      alignment)
    return Rituals.call(
        'ritual_ZN14QQuickTextUtil8alignedXEddi',
        textWidth, itemWidth, alignment,
    )

  @staticmethod
  @overload(float, float, int)
  def alignedY(
      textHeight: float,
      itemHeight: float,
      alignment: int,
  ) -> float:
    """
    Calls Qt's 'qreal QQuickTextUtil::alignedY(qreal textHeight, qreal
    itemHeight, int alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextutil.html#alignedY

    Parameters
    ----------

    textHeight : float
      Passed on as it is.

    itemHeight : float
      Passed on as it is.

    alignment : int
      Passed on as it is.
    """
    #  qreal QQuickTextUtil::alignedY(qreal textHeight, qreal itemHeight, int
    #      alignment)
    return Rituals.call(
        'ritual_ZN14QQuickTextUtil8alignedYEddi',
        textHeight, itemHeight, alignment,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTextUtil'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTextUtil::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextutil.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTextUtil::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickTextUtil10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def createCursor(*__, **_) -> Never:
    """
    - Qt's 'QQuickTextUtil::createCursor': a template: a pattern and no
      single function.
    - Qt's 'QQuickItem *QQuickTextUtil::createCursor(QQmlComponent
      *component, QQuickItem *parent, const QRectF &cursorRectangle, const
      char *className)': leans on 'QQuickTextUtil::staticMetaObject', which
      Qt's source does not mark for use from outside Qt and has no code for
      that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextUtil.createCursor' has no cute function yet. Qt's "
        "'QQuickTextUtil::createCursor': a template: a pattern and no "
        "single function. Qt's 'QQuickItem "
        "*QQuickTextUtil::createCursor(QQmlComponent *component, QQuickItem "
        "*parent, const QRectF &cursorRectangle, const char *className)': "
        "leans on 'QQuickTextUtil::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setCursorDelegate(*__, **_) -> Never:
    """
    Qt's 'QQuickTextUtil::setCursorDelegate': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQuickTextUtil.setCursorDelegate' has no cute function yet. Qt's "
        "'QQuickTextUtil::setCursorDelegate': a template: a pattern and no "
        "single function.")

  @staticmethod
  def textRenderType(*__, **_) -> Never:
    """
    Qt's 'QQuickTextUtil::textRenderType': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQuickTextUtil.textRenderType' has no cute function yet. Qt's "
        "'QQuickTextUtil::textRenderType': a template: a pattern and no "
        "single function.")
