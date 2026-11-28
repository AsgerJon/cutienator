"""
QFusionStylePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qfusionstyle_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QFusionStylePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QCommonStylePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QColor, QPalette
  from . import QFusionStyle
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPalette = WAIT['QPalette']


class QFusionStylePrivate(QCommonStylePrivate):
  """
  The cute side of Qt's QFusionStylePrivate: a plain Python object standing
  in front of one C++ QFusionStylePrivate.

  It is built on the cute 'QCommonStylePrivate', as Qt's QFusionStylePrivate
  is built on Qt's QCommonStylePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFusionStylePrivate that has a ritual and that
  Python can call so far, 10 names in all: 'q_func', 'isMacSystemPalette',
  'highlight', 'highlightedText', 'outline', 'highlightedOutline',
  'tabFrameColor', 'buttonColor', 'colorScheme', 'isHighContrast'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QFusionStyle *QFusionStylePrivate::q_func() const': takes in
    Python what 'QFusionStyle *QFusionStylePrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QFusionStylePrivate is created at the first use, not by
    'QFusionStylePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFusionStylePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFusionStylePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPalette)
  def isMacSystemPalette(self, pal: QPalette) -> bool:
    """
    Calls Qt's 'bool QFusionStylePrivate::isMacSystemPalette(const QPalette
    &pal) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfusionstyleprivate.html#isMacSystemPalette

    Parameters
    ----------

    pal : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  bool QFusionStylePrivate::isMacSystemPalette(const QPalette &pal)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QFusionStylePrivate18isMacSystemPaletteERK8QPalette',
        self._valueOf(pal),
    )

  @overload(QPalette)
  def highlight(self, pal: QPalette) -> QColor:
    """
    Calls Qt's 'QColor QFusionStylePrivate::highlight(const QPalette &pal)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyleprivate.html#highlight

    Parameters
    ----------

    pal : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QFusionStylePrivate::highlight(const QPalette &pal) const
    address = self.uglySide.call(
        'ritual_ZNK19QFusionStylePrivate9highlightERK8QPalette',
        self._valueOf(pal),
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(QPalette)
  def highlightedText(self, pal: QPalette) -> QColor:
    """
    Calls Qt's 'QColor QFusionStylePrivate::highlightedText(const QPalette
    &pal) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfusionstyleprivate.html#highlightedText

    Parameters
    ----------

    pal : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QFusionStylePrivate::highlightedText(const QPalette &pal) const
    address = self.uglySide.call(
        'ritual_ZNK19QFusionStylePrivate15highlightedTextERK8QPalette',
        self._valueOf(pal),
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(QPalette)
  def outline(self, pal: QPalette) -> QColor:
    """
    Calls Qt's 'QColor QFusionStylePrivate::outline(const QPalette &pal)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyleprivate.html#outline

    Parameters
    ----------

    pal : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QFusionStylePrivate::outline(const QPalette &pal) const
    address = self.uglySide.call(
        'ritual_ZNK19QFusionStylePrivate7outlineERK8QPalette',
        self._valueOf(pal),
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(QPalette)
  def highlightedOutline(self, pal: QPalette) -> QColor:
    """
    Calls Qt's 'QColor QFusionStylePrivate::highlightedOutline(const QPalette
    &pal) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfusionstyleprivate.html#highlightedOutline

    Parameters
    ----------

    pal : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QFusionStylePrivate::highlightedOutline(const QPalette &pal)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QFusionStylePrivate18highlightedOutlineERK8QPalette',
        self._valueOf(pal),
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(QPalette)
  def tabFrameColor(self, pal: QPalette) -> QColor:
    """
    Calls Qt's 'QColor QFusionStylePrivate::tabFrameColor(const QPalette
    &pal) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfusionstyleprivate.html#tabFrameColor

    Parameters
    ----------

    pal : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QFusionStylePrivate::tabFrameColor(const QPalette &pal) const
    address = self.uglySide.call(
        'ritual_ZNK19QFusionStylePrivate13tabFrameColorERK8QPalette',
        self._valueOf(pal),
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(QPalette)
  def buttonColor(self, pal: QPalette) -> QColor:
    """
    Calls Qt's 'QColor QFusionStylePrivate::buttonColor(const QPalette &pal)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfusionstyleprivate.html#buttonColor

    Parameters
    ----------

    pal : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QFusionStylePrivate::buttonColor(const QPalette &pal) const
    address = self.uglySide.call(
        'ritual_ZNK19QFusionStylePrivate11buttonColorERK8QPalette',
        self._valueOf(pal),
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def colorScheme(self) -> Qt.ColorScheme:
    """
    Calls Qt's 'Qt::ColorScheme QFusionStylePrivate::colorScheme() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfusionstyleprivate.html#colorScheme

    Returns
    -------

    Qt.ColorScheme
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.ColorScheme(number)'
      gives.
    """
    #  Qt::ColorScheme QFusionStylePrivate::colorScheme() const
    return Qt.ColorScheme(self.uglySide.call(
        'ritual_ZNK19QFusionStylePrivate11colorSchemeEv',
    ))

  def isHighContrast(self) -> bool:
    """
    Calls Qt's 'bool QFusionStylePrivate::isHighContrast() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfusionstyleprivate.html#isHighContrast
    """
    #  bool QFusionStylePrivate::isHighContrast() const
    return self.uglySide.call(
        'ritual_ZNK19QFusionStylePrivate14isHighContrastEv',
    )

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
    'QFusionStylePrivate::QFusionStylePrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfusionstyleprivate.html#QFusionStylePrivate
    """
    #  QFusionStylePrivate::QFusionStylePrivate()
    self._noteCreation(QFusionStylePrivate, lambda: Rituals.call(
        'ritual_ZN19QFusionStylePrivateC1Ev',
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

  def q_func(self) -> Optional[QFusionStyle]:
    """
    Calls Qt's 'QFusionStyle *QFusionStylePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qfusionstyleprivate.html#q_func

    Returns
    -------

    Optional[QFusionStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFusionStyle *QFusionStylePrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QFusionStylePrivate6q_funcEv')
    from . import QFusionStyle
    return QFusionStyle._cuteAt(address)
