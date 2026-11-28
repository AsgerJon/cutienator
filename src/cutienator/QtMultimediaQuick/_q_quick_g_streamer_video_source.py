"""
QQuickGStreamerVideoSource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qquickgstreamervideosource_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickGStreamerVideoSource to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from ..QtMultimedia import QGStreamerVideoSource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGStreamerVideoSource(QGStreamerVideoSource):
  """
  The cute side of Qt's QQuickGStreamerVideoSource: a plain Python object
  standing in front of one C++ QQuickGStreamerVideoSource.

  It is built on the cute 'QGStreamerVideoSource', as Qt's
  QQuickGStreamerVideoSource is built on Qt's QGStreamerVideoSource, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickGStreamerVideoSource that has a ritual and
  that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'qmlIsActive', 'qmlSetActive', 'setQmlGstBinDescription'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGStreamerVideoSource::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickGStreamerVideoSource::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickGStreamerVideoSource is created at the first use, not by
    'QQuickGStreamerVideoSource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGStreamerVideoSource.
  - Qt tells when it has removed the C++ QQuickGStreamerVideoSource. Every
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
    Calls Qt's 'QString QQuickGStreamerVideoSource::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgstreamervideosource.html#tr

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
    #  QString QQuickGStreamerVideoSource::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QQuickGStreamerVideoSource2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGStreamerVideoSource'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGStreamerVideoSource::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgstreamervideosource.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGStreamerVideoSource::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickGStreamerVideoSource10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def qmlIsActive(self) -> bool:
    """
    Calls Qt's 'bool QQuickGStreamerVideoSource::qmlIsActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgstreamervideosource.html#qmlIsActive
    """
    #  bool QQuickGStreamerVideoSource::qmlIsActive() const
    return self.uglySide.call(
        'ritual_ZNK26QQuickGStreamerVideoSource11qmlIsActiveEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setQmlGstBinDescription(self, gstBinDescription: str) -> None:
    """
    Calls Qt's 'void
    QQuickGStreamerVideoSource::setQmlGstBinDescription(QString
    gstBinDescription)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgstreamervideosource.html

    Parameters
    ----------

    gstBinDescription : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickGStreamerVideoSource::setQmlGstBinDescription(QString
    #      gstBinDescription)
    self.uglySide.call(
        'ritual_ZN26QQuickGStreamerVideoSource23setQmlGstBinDescriptionE7QS'
        'tring',
        gstBinDescription,
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
    'QQuickGStreamerVideoSource::QQuickGStreamerVideoSource(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgstreamervideosource.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickGStreamerVideoSource::QQuickGStreamerVideoSource(QObject
    #      *parent)
    self._noteCreation(QQuickGStreamerVideoSource, lambda: Rituals.call(
        'ritual_ZN26QQuickGStreamerVideoSourceC1EP7QObject',
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

  @overload(bool)
  def qmlSetActive(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickGStreamerVideoSource::qmlSetActive(bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgstreamervideosource.html#qmlSetActive

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickGStreamerVideoSource::qmlSetActive(bool active)
    self.uglySide.call(
        'ritual_ZN26QQuickGStreamerVideoSource12qmlSetActiveEb', active,
    )
