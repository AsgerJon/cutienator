"""
FileProperty binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsFolderListModel/6.12.0/QtLabsFolderListModel/private/fileproperty_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means FileProperty to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QDateTime, QFileInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFileInfo = WAIT['QFileInfo']


class FileProperty(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's FileProperty: a plain Python object standing in front
  of one C++ FileProperty.

  C++ hands a FileProperty around as a copy, so every C++ FileProperty behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's FileProperty that has a ritual and that Python can
  call so far, 11 names in all: 'fileName', 'filePath', 'baseName', 'size',
  'suffix', 'isDir', 'isFile', 'lastModified', 'lastRead', '__ne__',
  '__eq__'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void FileProperty::qt_qmlMarker_anonymous()': one of Qt's own inner
    workings.
  - Qt's 'FileProperty::~FileProperty()': the destructor: Python removes its
    C++ FileProperty by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 17 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ FileProperty is created at the first use, not by
    'FileProperty(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a FileProperty back gives a copy the ritual made for
    Python, in a new cute FileProperty.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'FileProperty'

  #  Qt's '~FileProperty()'. Naming it makes this a value class: Python owns
  #  every C++ FileProperty behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12FilePropertyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def fileName(self) -> str:
    """
    Calls Qt's 'QString FileProperty::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/fileproperty.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString FileProperty::fileName() const
    return self.uglySide.call('ritual_ZNK12FileProperty8fileNameEv')

  def filePath(self) -> str:
    """
    Calls Qt's 'QString FileProperty::filePath() const'.

    Qt's own words: https://doc.qt.io/qt-6/fileproperty.html#filePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString FileProperty::filePath() const
    return self.uglySide.call('ritual_ZNK12FileProperty8filePathEv')

  def baseName(self) -> str:
    """
    Calls Qt's 'QString FileProperty::baseName() const'.

    Qt's own words: https://doc.qt.io/qt-6/fileproperty.html#baseName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString FileProperty::baseName() const
    return self.uglySide.call('ritual_ZNK12FileProperty8baseNameEv')

  def size(self) -> int:
    """
    Calls Qt's 'qint64 FileProperty::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/fileproperty.html#size
    """
    #  qint64 FileProperty::size() const
    return self.uglySide.call('ritual_ZNK12FileProperty4sizeEv')

  def suffix(self) -> str:
    """
    Calls Qt's 'QString FileProperty::suffix() const'.

    Qt's own words: https://doc.qt.io/qt-6/fileproperty.html#suffix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString FileProperty::suffix() const
    return self.uglySide.call('ritual_ZNK12FileProperty6suffixEv')

  def isDir(self) -> bool:
    """
    Calls Qt's 'bool FileProperty::isDir() const'.

    Qt's own words: https://doc.qt.io/qt-6/fileproperty.html#isDir
    """
    #  bool FileProperty::isDir() const
    return self.uglySide.call('ritual_ZNK12FileProperty5isDirEv')

  def isFile(self) -> bool:
    """
    Calls Qt's 'bool FileProperty::isFile() const'.

    Qt's own words: https://doc.qt.io/qt-6/fileproperty.html#isFile
    """
    #  bool FileProperty::isFile() const
    return self.uglySide.call('ritual_ZNK12FileProperty6isFileEv')

  def lastModified(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime FileProperty::lastModified() const'.

    Qt's own words: https://doc.qt.io/qt-6/fileproperty.html#lastModified

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime FileProperty::lastModified() const
    address = self.uglySide.call('ritual_ZNK12FileProperty12lastModifiedEv')
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def lastRead(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime FileProperty::lastRead() const'.

    Qt's own words: https://doc.qt.io/qt-6/fileproperty.html#lastRead

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime FileProperty::lastRead() const
    address = self.uglySide.call('ritual_ZNK12FileProperty8lastReadEv')
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __ne__(self, fileInfo: FileProperty) -> bool:
    """
    Calls Qt's 'bool FileProperty::operator!=(const FileProperty &fileInfo)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/fileproperty.html#operator!=

    Parameters
    ----------

    fileInfo : FileProperty
      Passed on as a value: Qt reads the C++ FileProperty, which stays
      Python's own.
    """
    #  bool FileProperty::operator!=(const FileProperty &fileInfo) const
    return self.uglySide.call(
        'ritual_ZNK12FilePropertyneERKS_', self._valueOf(fileInfo),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __eq__(self, property: FileProperty) -> bool:
    """
    Calls Qt's 'bool FileProperty::operator==(const FileProperty &property)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/fileproperty.html#operator==

    Parameters
    ----------

    property : FileProperty
      Passed on as a value: Qt reads the C++ FileProperty, which stays
      Python's own.
    """
    #  bool FileProperty::operator==(const FileProperty &property) const
    return self.uglySide.call(
        'ritual_ZNK12FilePropertyeqERKS_', self._valueOf(property),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(QFileInfo)
  def __init__(self, info: Optional[QFileInfo] = None) -> None:
    """
    Notes what was given, for Qt's 'FileProperty::FileProperty(const
    QFileInfo &info)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/fileproperty.html#FileProperty

    Parameters
    ----------

    info : Optional[QFileInfo]
      Passed on as a value: Qt reads the C++ QFileInfo, which stays Python's
      own. May be left out, as in Qt: a new 'QFileInfo()' is then passed on.
    """
    #  FileProperty::FileProperty(const QFileInfo &info)
    if info is None:
      from ..QtCore import QFileInfo
      info = QFileInfo()
    self._noteCreation(FileProperty, lambda: Rituals.call(
        'ritual_ZN12FilePropertyC1ERK9QFileInfo', self._valueOf(info),
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


#  Qt's 'QList<FileProperty>': the list of FileProperty, which
#  'QList[FileProperty]' gives. It is made here, so that there is one as soon
#  as there can be a FileProperty.
QList.createKind(
    FileProperty, 'value',
    make='ritual_list_make_FileProperty',
    add='ritual_list_add_FileProperty',
    size='ritual_list_size_FileProperty',
    at='ritual_list_at_FileProperty',
    drop='ritual_list_drop_FileProperty',
)
