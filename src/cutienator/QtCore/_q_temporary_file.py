"""
QTemporaryFile binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qtemporaryfile.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QFile, QIODeviceBase, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QMetaObject, QTemporaryFilePrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTemporaryFile(QFile):
  """
  The cute side of Qt's QTemporaryFile: a plain Python object standing in
  front of one C++ QTemporaryFile.

  It is built on the cute 'QFile', as Qt's QTemporaryFile is built on Qt's
  QFile, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTemporaryFile that has a ritual and that Python can
  call so far, 12 names in all: 'metaObject', 'tr', 'd_func', 'autoRemove',
  'setAutoRemove', 'open', 'fileName', 'fileTemplate', 'setFileTemplate',
  'rename', 'renameOverwrite', 'createNativeFile'. It can be made from
  Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QTemporaryFile::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QTemporaryFile::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QTemporaryFilePrivate *QTemporaryFile::d_func() const': takes
    in Python what 'QTemporaryFilePrivate *QTemporaryFile::d_func()' takes.
  - Qt's 'QTemporaryFile::~QTemporaryFile()': the destructor: Python never
    removes a C++ QTemporaryFile.
  - Qt's 'QTemporaryFile *QTemporaryFile::createNativeFile(QFile &file)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  9 of the 31 functions Qt declares: 5 a template; 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QTemporaryFile is created at the first use, not by
    'QTemporaryFile(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTemporaryFile.
  - Qt tells when it has removed the C++ QTemporaryFile. Every call on the
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
    Calls Qt's 'QString QTemporaryFile::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporaryfile.html#tr

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
    #  QString QTemporaryFile::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QTemporaryFile2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(str)
  def createNativeFile(fileName: str) -> Optional[QTemporaryFile]:
    """
    Calls Qt's 'QTemporaryFile *QTemporaryFile::createNativeFile(const
    QString &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtemporaryfile.html#createNativeFile

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QTemporaryFile]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTemporaryFile *QTemporaryFile::createNativeFile(const QString
    #      &fileName)
    address = Rituals.call(
        'ritual_ZN14QTemporaryFile16createNativeFileERK7QString', fileName,
    )
    return QTemporaryFile._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTemporaryFile'

  #  A C++ QTemporaryFile Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTemporaryFile'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTemporaryFile::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporaryfile.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTemporaryFile::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QTemporaryFile10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def autoRemove(self) -> bool:
    """
    Calls Qt's 'bool QTemporaryFile::autoRemove() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporaryfile.html#autoRemove
    """
    #  bool QTemporaryFile::autoRemove() const
    return self.uglySide.call('ritual_ZNK14QTemporaryFile10autoRemoveEv')

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QTemporaryFile::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporaryfile.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTemporaryFile::fileName() const
    ritual = 'ritual_ZNK14QTemporaryFile8fileNameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QTemporaryFile8fileNameEv'
    return self.uglySide.call(ritual)

  def fileTemplate(self) -> str:
    """
    Calls Qt's 'QString QTemporaryFile::fileTemplate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporaryfile.html#fileTemplate

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTemporaryFile::fileTemplate() const
    return self.uglySide.call('ritual_ZNK14QTemporaryFile12fileTemplateEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAutoRemove(self, b: bool) -> None:
    """
    Calls Qt's 'void QTemporaryFile::setAutoRemove(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporaryfile.html#setAutoRemove

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QTemporaryFile::setAutoRemove(bool b)
    self.uglySide.call('ritual_ZN14QTemporaryFile13setAutoRemoveEb', b)

  @overload(str)
  def setFileTemplate(self, name: str) -> None:
    """
    Calls Qt's 'void QTemporaryFile::setFileTemplate(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtemporaryfile.html#setFileTemplate

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTemporaryFile::setFileTemplate(const QString &name)
    self.uglySide.call(
        'ritual_ZN14QTemporaryFile15setFileTemplateERK7QString', name,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QTemporaryFile::QTemporaryFile()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtemporaryfile.html#QTemporaryFile
    """
    #  QTemporaryFile::QTemporaryFile()
    self._noteCreation(QTemporaryFile, lambda: Rituals.call(
        'ritual_ZN14QTemporaryFileC1Ev',
    ))

  @overload(str)
  def __init__(self, templateName: str) -> None:
    """
    Notes what was given, for Qt's 'QTemporaryFile::QTemporaryFile(const
    QString &templateName)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtemporaryfile.html#QTemporaryFile

    Parameters
    ----------

    templateName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QTemporaryFile::QTemporaryFile(const QString &templateName)
    self._noteCreation(QTemporaryFile, lambda: Rituals.call(
        'ritual_ZN14QTemporaryFileC1ERK7QString', templateName,
    ))

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QTemporaryFile::QTemporaryFile(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtemporaryfile.html#QTemporaryFile

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTemporaryFile::QTemporaryFile(QObject *parent)
    self._noteCreation(QTemporaryFile, lambda: Rituals.call(
        'ritual_ZN14QTemporaryFileC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(self, templateName: str, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QTemporaryFile::QTemporaryFile(const
    QString &templateName, QObject *parent)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qtemporaryfile.html#QTemporaryFile

    Parameters
    ----------

    templateName : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTemporaryFile::QTemporaryFile(const QString &templateName, QObject
    #      *parent)
    self._noteCreation(QTemporaryFile, lambda: Rituals.call(
        'ritual_ZN14QTemporaryFileC1ERK7QStringP7QObject',
        templateName, self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QTemporaryFilePrivate]:
    """
    Calls Qt's 'QTemporaryFilePrivate *QTemporaryFile::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporaryfile.html#d_func

    Returns
    -------

    Optional[QTemporaryFilePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTemporaryFilePrivate *QTemporaryFile::d_func()
    address = self.uglySide.call('ritual_ZN14QTemporaryFile6d_funcEv')
    from . import QTemporaryFilePrivate
    return QTemporaryFilePrivate._cuteAt(address)

  @overload()
  def open(self) -> bool:
    """
    Calls Qt's 'bool QTemporaryFile::open()'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporaryfile.html#open
    """
    #  bool QTemporaryFile::open()
    return self.uglySide.call('ritual_ZN14QTemporaryFile4openEv')

  @overload(QIODeviceBase.OpenMode)
  def open(self, flags: QIODeviceBase.OpenMode) -> bool:
    """
    Calls Qt's 'bool QTemporaryFile::open(OpenMode flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporaryfile.html#open

    Parameters
    ----------

    flags : QIODeviceBase.OpenMode
      Passed on as its number.
    """
    #  bool QTemporaryFile::open(OpenMode flags)
    ritual = (
        'ritual_ZN14QTemporaryFile4openE6QFlagsIN13QIODeviceBase12OpenModeF'
        'lagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QTemporaryFile4openE6QFlagsIN13QIODeviceBase12Ope'
          'nModeFlagEE')
    return self.uglySide.call(ritual, flags.value)

  @overload(str)
  def rename(self, newName: str) -> bool:
    """
    Calls Qt's 'bool QTemporaryFile::rename(const QString &newName)'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporaryfile.html#rename

    Parameters
    ----------

    newName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QTemporaryFile::rename(const QString &newName)
    return self.uglySide.call(
        'ritual_ZN14QTemporaryFile6renameERK7QString', newName,
    )

  @overload(str)
  def renameOverwrite(self, newName: str) -> bool:
    """
    Calls Qt's 'bool QTemporaryFile::renameOverwrite(const QString
    &newName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtemporaryfile.html#renameOverwrite

    Parameters
    ----------

    newName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QTemporaryFile::renameOverwrite(const QString &newName)
    return self.uglySide.call(
        'ritual_ZN14QTemporaryFile15renameOverwriteERK7QString', newName,
    )
