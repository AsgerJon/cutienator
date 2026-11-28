"""
QQuickFlexboxLayoutAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquickflexboxlayout_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickFlexboxLayoutAttached to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickFlexboxLayout

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFlexboxLayoutAttached(QObject):
  """
  The cute side of Qt's QQuickFlexboxLayoutAttached: a plain Python object
  standing in front of one C++ QQuickFlexboxLayoutAttached.

  It is built on the cute 'QObject', as Qt's QQuickFlexboxLayoutAttached is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickFlexboxLayoutAttached that has a ritual and
  that Python can call so far, 4 names in all: 'metaObject', 'tr',
  'alignSelf', 'alignSelfChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFlexboxLayoutAttached::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickFlexboxLayoutAttached::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickFlexboxLayoutAttached::setAlignSelf(const
    QQuickFlexboxLayout::FlexboxAlignment a0)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickFlexboxLayoutAttached is created at the first use, not by
    'QQuickFlexboxLayoutAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFlexboxLayoutAttached.
  - Qt tells when it has removed the C++ QQuickFlexboxLayoutAttached. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickFlexboxLayoutAttached that has no cute function
    yet, 'setAlignSelf', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QQuickFlexboxLayoutAttached::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayoutattached.html#tr

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
    #  QString QQuickFlexboxLayoutAttached::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QQuickFlexboxLayoutAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFlexboxLayoutAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFlexboxLayoutAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayoutattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFlexboxLayoutAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickFlexboxLayoutAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def alignSelf(self) -> QQuickFlexboxLayout.FlexboxAlignment:
    """
    Calls Qt's 'QQuickFlexboxLayout::FlexboxAlignment
    QQuickFlexboxLayoutAttached::alignSelf() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayoutattached.html#alignSelf

    Returns
    -------

    QQuickFlexboxLayout.FlexboxAlignment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickFlexboxLayout.FlexboxAlignment(number)' gives.
    """
    #  QQuickFlexboxLayout::FlexboxAlignment
    #      QQuickFlexboxLayoutAttached::alignSelf() const
    return QQuickFlexboxLayout.FlexboxAlignment(self.uglySide.call(
        'ritual_ZNK27QQuickFlexboxLayoutAttached9alignSelfEv',
    ))

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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, object: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickFlexboxLayoutAttached::QQuickFlexboxLayoutAttached(QObject
    *object)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayoutattached.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickFlexboxLayoutAttached::QQuickFlexboxLayoutAttached(QObject
    #      *object)
    self._noteCreation(QQuickFlexboxLayoutAttached, lambda: Rituals.call(
        'ritual_ZN27QQuickFlexboxLayoutAttachedC1EP7QObject',
        self._addressOf(object, 'QObject'),
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

  def alignSelfChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlexboxLayoutAttached::alignSelfChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflexboxlayoutattached.html#alignSelfChanged
    """
    #  void QQuickFlexboxLayoutAttached::alignSelfChanged()
    self.uglySide.call(
        'ritual_ZN27QQuickFlexboxLayoutAttached16alignSelfChangedEv',
    )

  @staticmethod
  def setAlignSelf(*__, **_) -> Never:
    """
    Qt's 'void QQuickFlexboxLayoutAttached::setAlignSelf(const
    QQuickFlexboxLayout::FlexboxAlignment a0)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickFlexboxLayoutAttached.setAlignSelf' has no cute function "
        "yet. Qt's 'void QQuickFlexboxLayoutAttached::setAlignSelf(const "
        "QQuickFlexboxLayout::FlexboxAlignment a0)': takes a type Python "
        "has no way to hand over yet.")
