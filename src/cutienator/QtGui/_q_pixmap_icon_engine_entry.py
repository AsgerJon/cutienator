"""
QPixmapIconEngineEntry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qicon_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QPixmapIconEngineEntry to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QIcon

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QSize
  from . import QImage, QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QPixmap = WAIT['QPixmap']
  QSize = WAIT['QSize']


class QPixmapIconEngineEntry(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPixmapIconEngineEntry: a plain Python object
  standing in front of one C++ QPixmapIconEngineEntry.

  C++ hands a QPixmapIconEngineEntry around as a copy, so every C++
  QPixmapIconEngineEntry behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QPixmapIconEngineEntry yet. It can be made from Python,
  in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPixmapIconEngineEntry::~QPixmapIconEngineEntry()': the destructor:
    Python removes its C++ QPixmapIconEngineEntry by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QPixmapIconEngineEntry is created at the first use, not by
    'QPixmapIconEngineEntry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPixmapIconEngineEntry back gives a copy the ritual
    made for Python, in a new cute QPixmapIconEngineEntry.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPixmapIconEngineEntry'

  #  Qt's '~QPixmapIconEngineEntry()'. Naming it makes this a value class:
  #  Python owns every C++ QPixmapIconEngineEntry behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QPixmapIconEngineEntryD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QPixmapIconEngineEntry::QPixmapIconEngineEntry()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapiconengineentry.html#QPixmapIconEngineEntry
    """
    #  QPixmapIconEngineEntry::QPixmapIconEngineEntry()
    self._noteCreation(QPixmapIconEngineEntry, lambda: Rituals.call(
        'ritual_ZN22QPixmapIconEngineEntryC1Ev',
    ))

  @overload(QPixmap, QIcon.Mode, QIcon.State)
  def __init__(self, pm: QPixmap, m: QIcon.Mode, s: QIcon.State) -> None:
    """
    Notes what was given, for Qt's
    'QPixmapIconEngineEntry::QPixmapIconEngineEntry(const QPixmap &pm,
    QIcon::Mode m, QIcon::State s)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapiconengineentry.html#QPixmapIconEngineEntry

    Parameters
    ----------

    pm : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    m : QIcon.Mode
      Passed on as its number.

    s : QIcon.State
      Passed on as its number.
    """
    #  QPixmapIconEngineEntry::QPixmapIconEngineEntry(const QPixmap &pm,
    #      QIcon::Mode m, QIcon::State s)
    self._noteCreation(QPixmapIconEngineEntry, lambda: Rituals.call(
        'ritual_ZN22QPixmapIconEngineEntryC1ERK7QPixmapN5QIcon4ModeENS3_5St'
        'ateE',
        self._valueOf(pm), m.value, s.value,
    ))

  @overload(str, QSize, QIcon.Mode, QIcon.State)
  def __init__(
      self,
      file: str,
      sz: QSize,
      m: QIcon.Mode,
      s: QIcon.State,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QPixmapIconEngineEntry::QPixmapIconEngineEntry(const QString &file,
    const QSize &sz, QIcon::Mode m, QIcon::State s)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapiconengineentry.html#QPixmapIconEngineEntry

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.

    sz : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    m : QIcon.Mode
      Passed on as its number.

    s : QIcon.State
      Passed on as its number.
    """
    #  QPixmapIconEngineEntry::QPixmapIconEngineEntry(const QString &file,
    #      const QSize &sz, QIcon::Mode m, QIcon::State s)
    self._noteCreation(QPixmapIconEngineEntry, lambda: Rituals.call(
        'ritual_ZN22QPixmapIconEngineEntryC1ERK7QStringRK5QSizeN5QIcon4Mode'
        'ENS6_5StateE',
        file, self._valueOf(sz), m.value, s.value,
    ))

  @overload(str, QImage, QIcon.Mode, QIcon.State)
  def __init__(
      self,
      file: str,
      image: QImage,
      m: QIcon.Mode,
      s: QIcon.State,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QPixmapIconEngineEntry::QPixmapIconEngineEntry(const QString &file,
    const QImage &image, QIcon::Mode m, QIcon::State s)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpixmapiconengineentry.html#QPixmapIconEngineEntry

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    m : QIcon.Mode
      Passed on as its number.

    s : QIcon.State
      Passed on as its number.
    """
    #  QPixmapIconEngineEntry::QPixmapIconEngineEntry(const QString &file,
    #      const QImage &image, QIcon::Mode m, QIcon::State s)
    self._noteCreation(QPixmapIconEngineEntry, lambda: Rituals.call(
        'ritual_ZN22QPixmapIconEngineEntryC1ERK7QStringRK6QImageN5QIcon4Mod'
        'eENS6_5StateE',
        file, self._valueOf(image), m.value, s.value,
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
