"""
QIconPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qicon_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QIconPrivate to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QSize
  from . import QIcon, QIconEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIcon = WAIT['QIcon']
  QIconEngine = WAIT['QIconEngine']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QIconPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QIconPrivate: a plain Python object standing in front
  of one C++ QIconPrivate.

  C++ hands a QIconPrivate around as a copy, so every C++ QIconPrivate behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QIconPrivate that has a ritual and that Python can
  call so far, 2 names in all: 'get', 'pixmapDevicePixelRatio'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QIconPrivate::~QIconPrivate()': the destructor: Python removes its
    C++ QIconPrivate by it, and has no other use for it.
  - Qt's 'const QIconPrivate *QIconPrivate::get(const QIcon *icon)': takes in
    Python what 'QIconPrivate *QIconPrivate::get(QIcon *icon)' takes.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QIconPrivate is created at the first use, not by
    'QIconPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QIconPrivate back gives a copy the ritual made for
    Python, in a new cute QIconPrivate.
  - Each name of Qt's QIconPrivate that has no cute function yet,
    'clearIconCache', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QIconPrivate, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class IconEngineHook(CuteNum):
    """
    The enum 'QIconPrivate::IconEngineHook' of Qt, with the 1 names Qt gives
    in it.
    """

    PlatformIconHook = Kee[int](1000)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QIcon)
  @overload(NoneType)
  def get(icon: Optional[QIcon]) -> Optional[QIconPrivate]:
    """
    Calls Qt's 'QIconPrivate *QIconPrivate::get(QIcon *icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qiconprivate.html#get

    Parameters
    ----------

    icon : Optional[QIcon]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QIconPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIconPrivate *QIconPrivate::get(QIcon *icon)
    address = Rituals.call(
        'ritual_ZN12QIconPrivate3getEP5QIcon', CuteMixin._addressOf(icon),
    )
    return QIconPrivate._cuteAt(address)

  @staticmethod
  @overload(float, QSize, QSize)
  def pixmapDevicePixelRatio(
      displayDevicePixelRatio: float,
      requestedSize: QSize,
      actualSize: QSize,
  ) -> float:
    """
    Calls Qt's 'qreal QIconPrivate::pixmapDevicePixelRatio(qreal
    displayDevicePixelRatio, const QSize &requestedSize, const QSize
    &actualSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiconprivate.html#pixmapDevicePixelRatio

    Parameters
    ----------

    displayDevicePixelRatio : float
      Passed on as it is.

    requestedSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    actualSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  qreal QIconPrivate::pixmapDevicePixelRatio(qreal
    #      displayDevicePixelRatio, const QSize &requestedSize, const QSize
    #      &actualSize)
    return Rituals.call(
        'ritual_ZN12QIconPrivate22pixmapDevicePixelRatioEdRK5QSizeS2_',
        displayDevicePixelRatio, CuteMixin._valueOf(requestedSize),
        CuteMixin._valueOf(actualSize),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QIconPrivate'

  #  Qt's '~QIconPrivate()'. Naming it makes this a value class: Python owns
  #  every C++ QIconPrivate behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QIconPrivateD1Ev'

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

  @overload(QIconEngine)
  @overload(NoneType)
  def __init__(self, e: Optional[QIconEngine]) -> None:
    """
    Notes what was given, for Qt's 'QIconPrivate::QIconPrivate(QIconEngine
    *e)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qiconprivate.html#QIconPrivate

    Parameters
    ----------

    e : Optional[QIconEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QIconPrivate::QIconPrivate(QIconEngine *e)
    self._noteCreation(QIconPrivate, lambda: Rituals.call(
        'ritual_ZN12QIconPrivateC1EP11QIconEngine', self._addressOf(e),
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

  @staticmethod
  def clearIconCache(*__, **_) -> Never:
    """
    Qt's 'void QIconPrivate::clearIconCache()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'qt_cleanup_icon_cache'.
    """
    raise NotImplementedError(
        "'QIconPrivate.clearIconCache' has no cute function yet. Qt's 'void "
        "QIconPrivate::clearIconCache()': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'qt_cleanup_icon_cache'.")
