"""
QWebEngineExtensionInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebengineextensioninfo.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QUrl
  from . import QWebEngineExtensionInfoPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWebEngineExtensionInfoPrivate = WAIT['QWebEngineExtensionInfoPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineExtensionInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineExtensionInfo: a plain Python object
  standing in front of one C++ QWebEngineExtensionInfo.

  C++ hands a QWebEngineExtensionInfo around as a copy, so every C++
  QWebEngineExtensionInfo behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QWebEngineExtensionInfo that has a ritual and that
  Python can call so far, 9 names in all: 'name', 'id', 'description',
  'path', 'error', 'actionPopupUrl', 'isEnabled', 'isLoaded', 'isInstalled'.
  It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QWebEngineExtensionInfo::QWebEngineExtensionInfo(QWebEngineExtensionInfo
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QWebEngineExtensionInfo &QWebEngineExtensionInfo::operator=(const
    QWebEngineExtensionInfo &other)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'QWebEngineExtensionInfo::~QWebEngineExtensionInfo()': the
    destructor: Python removes its C++ QWebEngineExtensionInfo by it, and has
    no other use for it.
  - Qt's 'QWebEngineExtensionInfo
    &QWebEngineExtensionInfo::operator=(QWebEngineExtensionInfo &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QWebEngineExtensionInfo::swap(QWebEngineExtensionInfo
    &other)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 20 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QWebEngineExtensionInfo is created at the first use, not by
    'QWebEngineExtensionInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineExtensionInfo back gives a copy the ritual
    made for Python, in a new cute QWebEngineExtensionInfo.
  - Each name of Qt's QWebEngineExtensionInfo that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineExtensionInfo'

  #  Qt's '~QWebEngineExtensionInfo()'. Naming it makes this a value class:
  #  Python owns every C++ QWebEngineExtensionInfo behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QWebEngineExtensionInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QWebEngineExtensionInfo::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineextensioninfo.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineExtensionInfo::name() const
    return self.uglySide.call('ritual_ZNK23QWebEngineExtensionInfo4nameEv')

  def id(self) -> str:
    """
    Calls Qt's 'QString QWebEngineExtensionInfo::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineextensioninfo.html#id

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineExtensionInfo::id() const
    return self.uglySide.call('ritual_ZNK23QWebEngineExtensionInfo2idEv')

  def description(self) -> str:
    """
    Calls Qt's 'QString QWebEngineExtensionInfo::description() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensioninfo.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineExtensionInfo::description() const
    return self.uglySide.call(
        'ritual_ZNK23QWebEngineExtensionInfo11descriptionEv',
    )

  def path(self) -> str:
    """
    Calls Qt's 'QString QWebEngineExtensionInfo::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineextensioninfo.html#path

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineExtensionInfo::path() const
    return self.uglySide.call('ritual_ZNK23QWebEngineExtensionInfo4pathEv')

  def error(self) -> str:
    """
    Calls Qt's 'QString QWebEngineExtensionInfo::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineextensioninfo.html#error

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineExtensionInfo::error() const
    return self.uglySide.call('ritual_ZNK23QWebEngineExtensionInfo5errorEv')

  def actionPopupUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineExtensionInfo::actionPopupUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensioninfo.html#actionPopupUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineExtensionInfo::actionPopupUrl() const
    address = self.uglySide.call(
        'ritual_ZNK23QWebEngineExtensionInfo14actionPopupUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineExtensionInfo::isEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensioninfo.html#isEnabled
    """
    #  bool QWebEngineExtensionInfo::isEnabled() const
    return self.uglySide.call(
        'ritual_ZNK23QWebEngineExtensionInfo9isEnabledEv',
    )

  def isLoaded(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineExtensionInfo::isLoaded() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensioninfo.html#isLoaded
    """
    #  bool QWebEngineExtensionInfo::isLoaded() const
    return self.uglySide.call(
        'ritual_ZNK23QWebEngineExtensionInfo8isLoadedEv',
    )

  def isInstalled(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineExtensionInfo::isInstalled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensioninfo.html#isInstalled
    """
    #  bool QWebEngineExtensionInfo::isInstalled() const
    return self.uglySide.call(
        'ritual_ZNK23QWebEngineExtensionInfo11isInstalledEv',
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
    'QWebEngineExtensionInfo::QWebEngineExtensionInfo()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensioninfo.html
    """
    #  QWebEngineExtensionInfo::QWebEngineExtensionInfo()
    self._noteCreation(QWebEngineExtensionInfo, lambda: Rituals.call(
        'ritual_ZN23QWebEngineExtensionInfoC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QWebEngineExtensionInfo) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineExtensionInfo::QWebEngineExtensionInfo(const
    QWebEngineExtensionInfo &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensioninfo.html

    Parameters
    ----------

    other : QWebEngineExtensionInfo
      Passed on as a value: Qt reads the C++ QWebEngineExtensionInfo, which
      stays Python's own.
    """
    #  QWebEngineExtensionInfo::QWebEngineExtensionInfo(const
    #      QWebEngineExtensionInfo &other)
    self._noteCreation(QWebEngineExtensionInfo, lambda: Rituals.call(
        'ritual_ZN23QWebEngineExtensionInfoC1ERKS_', self._valueOf(other),
    ))

  @overload(QWebEngineExtensionInfoPrivate)
  @overload(NoneType)
  def __init__(self, d: Optional[QWebEngineExtensionInfoPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineExtensionInfo::QWebEngineExtensionInfo(
    QWebEngineExtensionInfoPrivate *d)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensioninfo.html

    Parameters
    ----------

    d : Optional[QWebEngineExtensionInfoPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWebEngineExtensionInfo::QWebEngineExtensionInfo(
    #      QWebEngineExtensionInfoPrivate *d)
    self._noteCreation(QWebEngineExtensionInfo, lambda: Rituals.call(
        'ritual_ZN23QWebEngineExtensionInfoC1EP30QWebEngineExtensionInfoPri'
        'vate',
        self._addressOf(d),
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QWebEngineExtensionInfo::swap(QWebEngineExtensionInfo
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebEngineExtensionInfo.swap' has no cute function yet. Qt's "
        "'void QWebEngineExtensionInfo::swap(QWebEngineExtensionInfo "
        "&other)': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<QWebEngineExtensionInfo>': the list of
#  QWebEngineExtensionInfo, which 'QList[QWebEngineExtensionInfo]' gives. It
#  is made here, so that there is one as soon as there can be a
#  QWebEngineExtensionInfo.
QList.createKind(
    QWebEngineExtensionInfo, 'value',
    make='ritual_list_make_QWebEngineExtensionInfo',
    add='ritual_list_add_QWebEngineExtensionInfo',
    size='ritual_list_size_QWebEngineExtensionInfo',
    at='ritual_list_at_QWebEngineExtensionInfo',
    drop='ritual_list_drop_QWebEngineExtensionInfo',
)
