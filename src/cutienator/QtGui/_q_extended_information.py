"""
QExtendedInformation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qfileinfogatherer_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QExtendedInformation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDateTime, QFileInfo, QTimeZone
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFileInfo = WAIT['QFileInfo']
  QTimeZone = WAIT['QTimeZone']


class QExtendedInformation(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QExtendedInformation: a plain Python object standing
  in front of one C++ QExtendedInformation.

  C++ hands a QExtendedInformation around as a copy, so every C++
  QExtendedInformation behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QExtendedInformation that has a ritual and that
  Python can call so far, 11 names in all: 'isDir', 'isFile', 'isSystem',
  '__eq__', 'isCaseSensitive', 'type', 'isSymLink', 'isHidden', 'fileInfo',
  'lastModified', 'size'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFile::Permissions QExtendedInformation::permissions() const':
    gives a type Python has no way to take yet.
  - Qt's 'QExtendedInformation::~QExtendedInformation()': the destructor:
    Python removes its C++ QExtendedInformation by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QExtendedInformation is created at the first use, not by
    'QExtendedInformation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QExtendedInformation back gives a copy the ritual
    made for Python, in a new cute QExtendedInformation.
  - Each name of Qt's QExtendedInformation that has no cute function yet,
    'permissions', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QExtendedInformation, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QExtendedInformation::Type' of Qt, with the 3 names Qt gives in
    it.
    """

    Dir = Kee[int](0)
    File = Kee[int](1)
    System = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QExtendedInformation'

  #  Qt's '~QExtendedInformation()'. Naming it makes this a value class:
  #  Python owns every C++ QExtendedInformation behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QExtendedInformationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isCaseSensitive(self) -> bool:
    """
    Calls Qt's 'bool QExtendedInformation::isCaseSensitive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qextendedinformation.html#isCaseSensitive
    """
    #  bool QExtendedInformation::isCaseSensitive() const
    return self.uglySide.call(
        'ritual_ZNK20QExtendedInformation15isCaseSensitiveEv',
    )

  def type(self) -> Type:
    """
    Calls Qt's 'Type QExtendedInformation::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qextendedinformation.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QExtendedInformation::type() const
    return QExtendedInformation.Type(self.uglySide.call(
        'ritual_ZNK20QExtendedInformation4typeEv',
    ))

  @overload()
  @overload(bool)
  def isSymLink(self, ignoreNtfsSymLinks: bool = False) -> bool:
    """
    Calls Qt's 'bool QExtendedInformation::isSymLink(bool ignoreNtfsSymLinks)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qextendedinformation.html#isSymLink

    Parameters
    ----------

    ignoreNtfsSymLinks : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QExtendedInformation::isSymLink(bool ignoreNtfsSymLinks) const
    return self.uglySide.call(
        'ritual_ZNK20QExtendedInformation9isSymLinkEb', ignoreNtfsSymLinks,
    )

  def isHidden(self) -> bool:
    """
    Calls Qt's 'bool QExtendedInformation::isHidden() const'.

    Qt's own words: https://doc.qt.io/qt-6/qextendedinformation.html#isHidden
    """
    #  bool QExtendedInformation::isHidden() const
    return self.uglySide.call('ritual_ZNK20QExtendedInformation8isHiddenEv')

  def fileInfo(self) -> QFileInfo:
    """
    Calls Qt's 'QFileInfo QExtendedInformation::fileInfo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qextendedinformation.html#fileInfo

    Returns
    -------

    QFileInfo
      A new cute QFileInfo around the copy Qt gave back. Python owns it.
    """
    #  QFileInfo QExtendedInformation::fileInfo() const
    address = self.uglySide.call(
        'ritual_ZNK20QExtendedInformation8fileInfoEv',
    )
    from ..QtCore import QFileInfo
    return QFileInfo._cuteOwning(address)

  @overload(QTimeZone)
  def lastModified(self, tz: QTimeZone) -> QDateTime:
    """
    Calls Qt's 'QDateTime QExtendedInformation::lastModified(const QTimeZone
    &tz) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qextendedinformation.html#lastModified

    Parameters
    ----------

    tz : QTimeZone
      Passed on as a value: Qt reads the C++ QTimeZone, which stays Python's
      own.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QExtendedInformation::lastModified(const QTimeZone &tz)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QExtendedInformation12lastModifiedERK9QTimeZone',
        self._valueOf(tz),
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QExtendedInformation::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qextendedinformation.html#size
    """
    #  qint64 QExtendedInformation::size() const
    return self.uglySide.call('ritual_ZNK20QExtendedInformation4sizeEv')

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
  def __eq__(self, fileInfo: QExtendedInformation) -> bool:
    """
    Calls Qt's 'bool QExtendedInformation::operator==(const
    QExtendedInformation &fileInfo) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qextendedinformation.html#operator==

    Parameters
    ----------

    fileInfo : QExtendedInformation
      Passed on as a value: Qt reads the C++ QExtendedInformation, which
      stays Python's own.
    """
    #  bool QExtendedInformation::operator==(const QExtendedInformation
    #      &fileInfo) const
    return self.uglySide.call(
        'ritual_ZNK20QExtendedInformationeqERKS_', self._valueOf(fileInfo),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QExtendedInformation::QExtendedInformation()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qextendedinformation.html#QExtendedInformation
    """
    #  QExtendedInformation::QExtendedInformation()
    self._noteCreation(QExtendedInformation, lambda: Rituals.call(
        'ritual_ZN20QExtendedInformationC1Ev',
    ))

  @overload(QFileInfo)
  def __init__(self, info: QFileInfo) -> None:
    """
    Notes what was given, for Qt's
    'QExtendedInformation::QExtendedInformation(const QFileInfo &info)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qextendedinformation.html#QExtendedInformation

    Parameters
    ----------

    info : QFileInfo
      Passed on as a value: Qt reads the C++ QFileInfo, which stays Python's
      own.
    """
    #  QExtendedInformation::QExtendedInformation(const QFileInfo &info)
    self._noteCreation(QExtendedInformation, lambda: Rituals.call(
        'ritual_ZN20QExtendedInformationC1ERK9QFileInfo',
        self._valueOf(info),
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

  def isDir(self) -> bool:
    """
    Calls Qt's 'bool QExtendedInformation::isDir()'.

    Qt's own words: https://doc.qt.io/qt-6/qextendedinformation.html#isDir
    """
    #  bool QExtendedInformation::isDir()
    return self.uglySide.call('ritual_ZN20QExtendedInformation5isDirEv')

  def isFile(self) -> bool:
    """
    Calls Qt's 'bool QExtendedInformation::isFile()'.

    Qt's own words: https://doc.qt.io/qt-6/qextendedinformation.html#isFile
    """
    #  bool QExtendedInformation::isFile()
    return self.uglySide.call('ritual_ZN20QExtendedInformation6isFileEv')

  def isSystem(self) -> bool:
    """
    Calls Qt's 'bool QExtendedInformation::isSystem()'.

    Qt's own words: https://doc.qt.io/qt-6/qextendedinformation.html#isSystem
    """
    #  bool QExtendedInformation::isSystem()
    return self.uglySide.call('ritual_ZN20QExtendedInformation8isSystemEv')

  @staticmethod
  def permissions(*__, **_) -> Never:
    """
    Qt's 'QFile::Permissions QExtendedInformation::permissions() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QExtendedInformation.permissions' has no cute function yet. Qt's "
        "'QFile::Permissions QExtendedInformation::permissions() const': "
        "gives a type Python has no way to take yet.")
