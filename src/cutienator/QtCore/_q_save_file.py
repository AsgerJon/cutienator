"""
QSaveFile binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qsavefile.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QFileDevice, QIODeviceBase, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSaveFile(QFileDevice):
  """
  The cute side of Qt's QSaveFile: a plain Python object standing in front of
  one C++ QSaveFile.

  It is built on the cute 'QFileDevice', as Qt's QSaveFile is built on Qt's
  QFileDevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSaveFile that has a ritual and that Python can call
  so far, 9 names in all: 'metaObject', 'tr', 'fileName', 'setFileName',
  'open', 'commit', 'cancelWriting', 'setDirectWriteFallback',
  'directWriteFallback'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSaveFile::~QSaveFile()': the destructor: Python never removes a
    C++ QSaveFile.

  What has no ritual
  ------------------

  13 of the 25 functions Qt declares: 4 private; 3 takes or gives a type that
  cannot be passed yet; 3 a template; 2 forbidden; 1 protected.

  What to expect
  --------------

  - The C++ QSaveFile is created at the first use, not by 'QSaveFile(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSaveFile.
  - Qt tells when it has removed the C++ QSaveFile. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QSaveFile::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsavefile.html#tr

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
    #  QString QSaveFile::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QSaveFile2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSaveFile'

  #  A C++ QSaveFile Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSaveFile'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSaveFile::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsavefile.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSaveFile::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QSaveFile10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QSaveFile::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsavefile.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSaveFile::fileName() const
    ritual = 'ritual_ZNK9QSaveFile8fileNameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QSaveFile8fileNameEv'
    return self.uglySide.call(ritual)

  def directWriteFallback(self) -> bool:
    """
    Calls Qt's 'bool QSaveFile::directWriteFallback() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsavefile.html#directWriteFallback
    """
    #  bool QSaveFile::directWriteFallback() const
    return self.uglySide.call('ritual_ZNK9QSaveFile19directWriteFallbackEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setFileName(self, name: str) -> None:
    """
    Calls Qt's 'void QSaveFile::setFileName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qsavefile.html#setFileName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSaveFile::setFileName(const QString &name)
    self.uglySide.call('ritual_ZN9QSaveFile11setFileNameERK7QString', name)

  @overload(bool)
  def setDirectWriteFallback(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QSaveFile::setDirectWriteFallback(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsavefile.html#setDirectWriteFallback

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QSaveFile::setDirectWriteFallback(bool enabled)
    self.uglySide.call(
        'ritual_ZN9QSaveFile22setDirectWriteFallbackEb', enabled,
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
    Notes what was given, for Qt's 'QSaveFile::QSaveFile(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsavefile.html#QSaveFile

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSaveFile::QSaveFile(QObject *parent)
    self._noteCreation(QSaveFile, lambda: Rituals.call(
        'ritual_ZN9QSaveFileC1EP7QObject', self._addressOf(parent),
    ))

  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(self, name: str, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QSaveFile::QSaveFile(const QString &name,
    QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsavefile.html#QSaveFile

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSaveFile::QSaveFile(const QString &name, QObject *parent)
    self._noteCreation(QSaveFile, lambda: Rituals.call(
        'ritual_ZN9QSaveFileC1ERK7QStringP7QObject',
        name, self._addressOf(parent),
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

  @overload(QIODeviceBase.OpenMode)
  def open(self, flags: QIODeviceBase.OpenMode) -> bool:
    """
    Calls Qt's 'bool QSaveFile::open(OpenMode flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qsavefile.html#open

    Parameters
    ----------

    flags : QIODeviceBase.OpenMode
      Passed on as its number.
    """
    #  bool QSaveFile::open(OpenMode flags)
    ritual = (
        'ritual_ZN9QSaveFile4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QSaveFile4openE6QFlagsIN13QIODeviceBase12OpenModeF'
          'lagEE')
    return self.uglySide.call(ritual, flags.value)

  def commit(self) -> bool:
    """
    Calls Qt's 'bool QSaveFile::commit()'.

    Qt's own words: https://doc.qt.io/qt-6/qsavefile.html#commit
    """
    #  bool QSaveFile::commit()
    return self.uglySide.call('ritual_ZN9QSaveFile6commitEv')

  def cancelWriting(self) -> None:
    """
    Calls Qt's 'void QSaveFile::cancelWriting()'.

    Qt's own words: https://doc.qt.io/qt-6/qsavefile.html#cancelWriting
    """
    #  void QSaveFile::cancelWriting()
    self.uglySide.call('ritual_ZN9QSaveFile13cancelWritingEv')
