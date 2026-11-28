"""
QQuickScrollIndicatorAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickscrollindicator_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickScrollIndicatorAttached to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickScrollIndicator
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickScrollIndicator = WAIT['QQuickScrollIndicator']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickScrollIndicatorAttached(QObject):
  """
  The cute side of Qt's QQuickScrollIndicatorAttached: a plain Python object
  standing in front of one C++ QQuickScrollIndicatorAttached.

  It is built on the cute 'QObject', as Qt's QQuickScrollIndicatorAttached is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickScrollIndicatorAttached that has a ritual and
  that Python can call so far, 8 names in all: 'metaObject', 'tr',
  'horizontal', 'setHorizontal', 'vertical', 'setVertical',
  'horizontalChanged', 'verticalChanged'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickScrollIndicatorAttached::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickScrollIndicatorAttached::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickScrollIndicatorAttached::~QQuickScrollIndicatorAttached()':
    the destructor: Python never removes a C++ QQuickScrollIndicatorAttached.
  - Qt's 'QQuickScrollIndicatorAttachedPrivate
    *QQuickScrollIndicatorAttached::d_func()': gives
    'QQuickScrollIndicatorAttachedPrivate', which has no cute class yet.
  - Qt's 'const QQuickScrollIndicatorAttachedPrivate
    *QQuickScrollIndicatorAttached::d_func() const': gives
    'QQuickScrollIndicatorAttachedPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickScrollIndicatorAttached is created at the first use, not by
    'QQuickScrollIndicatorAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickScrollIndicatorAttached.
  - Qt tells when it has removed the C++ QQuickScrollIndicatorAttached. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickScrollIndicatorAttached::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicatorattached.html#tr

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
    #  QString QQuickScrollIndicatorAttached::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN29QQuickScrollIndicatorAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickScrollIndicatorAttached'

  #  A C++ QQuickScrollIndicatorAttached Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickScrollIndicatorAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickScrollIndicatorAttached::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicatorattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickScrollIndicatorAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickScrollIndicatorAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def horizontal(self) -> Optional[QQuickScrollIndicator]:
    """
    Calls Qt's 'QQuickScrollIndicator
    *QQuickScrollIndicatorAttached::horizontal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicatorattached.html#horizontal

    Returns
    -------

    Optional[QQuickScrollIndicator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickScrollIndicator *QQuickScrollIndicatorAttached::horizontal()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickScrollIndicatorAttached10horizontalEv',
    )
    from . import QQuickScrollIndicator
    return QQuickScrollIndicator._cuteAt(address)

  def vertical(self) -> Optional[QQuickScrollIndicator]:
    """
    Calls Qt's 'QQuickScrollIndicator
    *QQuickScrollIndicatorAttached::vertical() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicatorattached.html#vertical

    Returns
    -------

    Optional[QQuickScrollIndicator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickScrollIndicator *QQuickScrollIndicatorAttached::vertical() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickScrollIndicatorAttached8verticalEv',
    )
    from . import QQuickScrollIndicator
    return QQuickScrollIndicator._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickScrollIndicator)
  @overload(NoneType)
  def setHorizontal(
      self,
      horizontal: Optional[QQuickScrollIndicator],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickScrollIndicatorAttached::setHorizontal(QQuickScrollIndicator
    *horizontal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicatorattached.html#setHorizontal

    Parameters
    ----------

    horizontal : Optional[QQuickScrollIndicator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QQuickScrollIndicatorAttached::setHorizontal(QQuickScrollIndicator
    #      *horizontal)
    self.uglySide.call(
        'ritual_ZN29QQuickScrollIndicatorAttached13setHorizontalEP21QQuickS'
        'crollIndicator',
        self._addressOf(horizontal),
    )

  @overload(QQuickScrollIndicator)
  @overload(NoneType)
  def setVertical(self, vertical: Optional[QQuickScrollIndicator]) -> None:
    """
    Calls Qt's 'void
    QQuickScrollIndicatorAttached::setVertical(QQuickScrollIndicator
    *vertical)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicatorattached.html#setVertical

    Parameters
    ----------

    vertical : Optional[QQuickScrollIndicator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickScrollIndicatorAttached::setVertical(QQuickScrollIndicator
    #      *vertical)
    self.uglySide.call(
        'ritual_ZN29QQuickScrollIndicatorAttached11setVerticalEP21QQuickScr'
        'ollIndicator',
        self._addressOf(vertical),
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
    'QQuickScrollIndicatorAttached::QQuickScrollIndicatorAttached(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicatorattached.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickScrollIndicatorAttached::QQuickScrollIndicatorAttached(QObject
    #      *parent)
    self._noteCreation(QQuickScrollIndicatorAttached, lambda: Rituals.call(
        'ritual_ZN29QQuickScrollIndicatorAttachedC1EP7QObject',
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

  def horizontalChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollIndicatorAttached::horizontalChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicatorattached.html
    """
    #  void QQuickScrollIndicatorAttached::horizontalChanged()
    self.uglySide.call(
        'ritual_ZN29QQuickScrollIndicatorAttached17horizontalChangedEv',
    )

  def verticalChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollIndicatorAttached::verticalChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicatorattached.html#verticalChanged
    """
    #  void QQuickScrollIndicatorAttached::verticalChanged()
    self.uglySide.call(
        'ritual_ZN29QQuickScrollIndicatorAttached15verticalChangedEv',
    )
