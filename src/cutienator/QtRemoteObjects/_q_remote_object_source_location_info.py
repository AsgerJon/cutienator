"""
QRemoteObjectSourceLocationInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/qtremoteobjectglobal.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QHash

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']


class QRemoteObjectSourceLocationInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRemoteObjectSourceLocationInfo: a plain Python
  object standing in front of one C++ QRemoteObjectSourceLocationInfo.

  C++ hands a QRemoteObjectSourceLocationInfo around as a copy, so every C++
  QRemoteObjectSourceLocationInfo behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QRemoteObjectSourceLocationInfo that has a ritual
  and that Python can call so far, 2 names in all: '__eq__', '__ne__'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QRemoteObjectSourceLocationInfo::~QRemoteObjectSourceLocationInfo()':
    the destructor: Python removes its C++ QRemoteObjectSourceLocationInfo by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QRemoteObjectSourceLocationInfo is created at the first use, not
    by 'QRemoteObjectSourceLocationInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRemoteObjectSourceLocationInfo back gives a copy the
    ritual made for Python, in a new cute QRemoteObjectSourceLocationInfo.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRemoteObjectSourceLocationInfo'

  #  Qt's '~QRemoteObjectSourceLocationInfo()'. Naming it makes this a value
  #  class: Python owns every C++ QRemoteObjectSourceLocationInfo behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN31QRemoteObjectSourceLocationInfoD1Ev'

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

  @overload(THIS)
  def __eq__(self, other: QRemoteObjectSourceLocationInfo) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectSourceLocationInfo::operator==(const
    QRemoteObjectSourceLocationInfo &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectsourcelocationinfo.html#operator==

    Parameters
    ----------

    other : QRemoteObjectSourceLocationInfo
      Passed on as a value: Qt reads the C++ QRemoteObjectSourceLocationInfo,
      which stays Python's own.
    """
    #  bool QRemoteObjectSourceLocationInfo::operator==(const
    #      QRemoteObjectSourceLocationInfo &other) const
    return self.uglySide.call(
        'ritual_ZNK31QRemoteObjectSourceLocationInfoeqERKS_',
        self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: QRemoteObjectSourceLocationInfo) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectSourceLocationInfo::operator!=(const
    QRemoteObjectSourceLocationInfo &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectsourcelocationinfo.html#operator!=

    Parameters
    ----------

    other : QRemoteObjectSourceLocationInfo
      Passed on as a value: Qt reads the C++ QRemoteObjectSourceLocationInfo,
      which stays Python's own.
    """
    #  bool QRemoteObjectSourceLocationInfo::operator!=(const
    #      QRemoteObjectSourceLocationInfo &other) const
    return self.uglySide.call(
        'ritual_ZNK31QRemoteObjectSourceLocationInfoneERKS_',
        self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
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
    'QRemoteObjectSourceLocationInfo::QRemoteObjectSourceLocationInfo()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectsourcelocationinfo.html
    """
    #  QRemoteObjectSourceLocationInfo::QRemoteObjectSourceLocationInfo()
    self._noteCreation(QRemoteObjectSourceLocationInfo, lambda: Rituals.call(
        'ritual_ZN31QRemoteObjectSourceLocationInfoC1Ev',
    ))

  @overload(str, QUrl)
  def __init__(self, typeName_: str, hostUrl_: QUrl) -> None:
    """
    Notes what was given, for Qt's
    'QRemoteObjectSourceLocationInfo::QRemoteObjectSourceLocationInfo(const
    QString &typeName_, const QUrl &hostUrl_)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectsourcelocationinfo.html

    Parameters
    ----------

    typeName_ : str
      Passed on as it is: a QString is made of it for the call.

    hostUrl_ : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  QRemoteObjectSourceLocationInfo::QRemoteObjectSourceLocationInfo(const
    #      QString &typeName_, const QUrl &hostUrl_)
    self._noteCreation(QRemoteObjectSourceLocationInfo, lambda: Rituals.call(
        'ritual_ZN31QRemoteObjectSourceLocationInfoC1ERK7QStringRK4QUrl',
        typeName_, self._valueOf(hostUrl_),
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


#  Qt's 'QHash<QString, QRemoteObjectSourceLocationInfo>': the QHash from
#  text to QRemoteObjectSourceLocationInfo, which 'QHash[str,
#  QRemoteObjectSourceLocationInfo]' gives. It is completed here, in the file
#  of the class of its values. Qt has a name of its own for it.
QRemoteObjectSourceLocations = QHash.createKind(
    str, QRemoteObjectSourceLocationInfo, 'value',
    name='QRemoteObjectSourceLocations',
    make='ritual_map_make_QHash_QString_QRemoteObjectSourceLocationInfo',
    put='ritual_map_put_QHash_QString_QRemoteObjectSourceLocationInfo',
    size='ritual_map_size_QHash_QString_QRemoteObjectSourceLocationInfo',
    key='ritual_map_key_QHash_QString_QRemoteObjectSourceLocationInfo',
    value='ritual_map_value_QHash_QString_QRemoteObjectSourceLocationInfo',
    has='ritual_map_has_QHash_QString_QRemoteObjectSourceLocationInfo',
    get='ritual_map_get_QHash_QString_QRemoteObjectSourceLocationInfo',
    drop='ritual_map_drop_QHash_QString_QRemoteObjectSourceLocationInfo',
)
