"""
QCachedPainter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qstyle_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QCachedPainter to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect, QSize
  from ..QtGui import QPainter
  from . import QStyleOption
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']
  QStyleOption = WAIT['QStyleOption']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCachedPainter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCachedPainter: a plain Python object standing in
  front of one C++ QCachedPainter.

  What exists
  -----------

  Every function of Qt's QCachedPainter that has a ritual and that Python can
  call so far, 5 names in all: 'finish', 'needsPainting', 'pixmapRect',
  'painter', 'cleanupPixmapCache'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCachedPainter::~QCachedPainter()': the destructor: Python never
    removes a C++ QCachedPainter.
  - Qt's 'QPainter *QCachedPainter::operator->()': an operator Python has no
    name for.

  What to expect
  --------------

  - The C++ QCachedPainter is created at the first use, not by
    'QCachedPainter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCachedPainter.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def cleanupPixmapCache() -> None:
    """
    Calls Qt's 'void QCachedPainter::cleanupPixmapCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcachedpainter.html#cleanupPixmapCache
    """
    #  void QCachedPainter::cleanupPixmapCache()
    Rituals.call('ritual_ZN14QCachedPainter18cleanupPixmapCacheEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCachedPainter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def needsPainting(self) -> bool:
    """
    Calls Qt's 'bool QCachedPainter::needsPainting() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcachedpainter.html#needsPainting
    """
    #  bool QCachedPainter::needsPainting() const
    return self.uglySide.call('ritual_ZNK14QCachedPainter13needsPaintingEv')

  def pixmapRect(self) -> QRect:
    """
    Calls Qt's 'QRect QCachedPainter::pixmapRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcachedpainter.html#pixmapRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QCachedPainter::pixmapRect() const
    address = self.uglySide.call('ritual_ZNK14QCachedPainter10pixmapRectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

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

  @overload(QPainter, str, QStyleOption)
  @overload(QPainter, str, NoneType)
  @overload(NoneType, str, QStyleOption)
  @overload(NoneType, str, NoneType)
  @overload(QPainter, str, QStyleOption, QSize)
  @overload(QPainter, str, NoneType, QSize)
  @overload(NoneType, str, QStyleOption, QSize)
  @overload(NoneType, str, NoneType, QSize)
  @overload(QPainter, str, QStyleOption, QSize, QRect)
  @overload(QPainter, str, NoneType, QSize, QRect)
  @overload(NoneType, str, QStyleOption, QSize, QRect)
  @overload(NoneType, str, NoneType, QSize, QRect)
  def __init__(
      self,
      painter: Optional[QPainter],
      cachePrefix: str,
      option: Optional[QStyleOption],
      size: Optional[QSize] = None,
      paintRect: Optional[QRect] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QCachedPainter::QCachedPainter(QPainter
    *painter, const QString &cachePrefix, const QStyleOption *option, QSize
    size, QRect paintRect)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcachedpainter.html#QCachedPainter

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    cachePrefix : str
      Passed on as it is: a QString is made of it for the call.

    option : Optional[QStyleOption]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    size : Optional[QSize]
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
      May be left out, as in Qt: a new 'QSize()' is then passed on.

    paintRect : Optional[QRect]
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
      May be left out, as in Qt: a new 'QRect()' is then passed on.
    """
    #  QCachedPainter::QCachedPainter(QPainter *painter, const QString
    #      &cachePrefix, const QStyleOption *option, QSize size, QRect
    #      paintRect)
    if size is None:
      from ..QtCore import QSize
      size = QSize()
    if paintRect is None:
      from ..QtCore import QRect
      paintRect = QRect()
    self._noteCreation(QCachedPainter, lambda: Rituals.call(
        'ritual_ZN14QCachedPainterC1EP8QPainterRK7QStringPK12QStyleOption5Q'
        'Size5QRect',
        self._addressOf(painter), cachePrefix, self._addressOf(option),
        self._valueOf(size), self._valueOf(paintRect),
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

  def finish(self) -> None:
    """
    Calls Qt's 'void QCachedPainter::finish()'.

    Qt's own words: https://doc.qt.io/qt-6/qcachedpainter.html#finish
    """
    #  void QCachedPainter::finish()
    self.uglySide.call('ritual_ZN14QCachedPainter6finishEv')

  def painter(self) -> Optional[QPainter]:
    """
    Calls Qt's 'QPainter *QCachedPainter::painter()'.

    Qt's own words: https://doc.qt.io/qt-6/qcachedpainter.html#painter

    Returns
    -------

    Optional[QPainter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPainter *QCachedPainter::painter()
    address = self.uglySide.call('ritual_ZN14QCachedPainter7painterEv')
    from ..QtGui import QPainter
    return QPainter._cuteAt(address)
