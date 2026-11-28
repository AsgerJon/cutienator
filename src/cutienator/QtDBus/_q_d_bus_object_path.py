"""
QDBusObjectPath binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/qdbusextratypes.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDebug, QLatin1String
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']
  QLatin1String = WAIT['QLatin1String']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusObjectPath(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDBusObjectPath: a plain Python object standing in
  front of one C++ QDBusObjectPath.

  C++ hands a QDBusObjectPath around as a copy, so every C++ QDBusObjectPath
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDBusObjectPath that has a ritual and that Python
  can call so far, 4 names in all: 'setPath', 'path', '__rlshift__',
  'doCheck'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDBusObjectPath::QDBusObjectPath(const QString &path)': takes in
    Python what 'QDBusObjectPath::QDBusObjectPath(const char *path)' takes.
  - Qt's 'QDBusObjectPath::QDBusObjectPath(QString &&p)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void QDBusObjectPath::swap(QDBusObjectPath &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QVariant QDBusObjectPath::operator QVariant() const': an operator
    Python has no name for.
  - Qt's 'QDBusObjectPath::~QDBusObjectPath()': the destructor: Python
    removes its C++ QDBusObjectPath by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QDBusObjectPath is created at the first use, not by
    'QDBusObjectPath(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDBusObjectPath back gives a copy the ritual made for
    Python, in a new cute QDBusObjectPath.
  - Each name of Qt's QDBusObjectPath that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusObjectPath'

  #  Qt's '~QDBusObjectPath()'. Naming it makes this a value class: Python
  #  owns every C++ QDBusObjectPath behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QDBusObjectPathD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def path(self) -> str:
    """
    Calls Qt's 'QString QDBusObjectPath::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusobjectpath.html#path

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusObjectPath::path() const
    return self.uglySide.call('ritual_ZNK15QDBusObjectPath4pathEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setPath(self, path: str) -> None:
    """
    Calls Qt's 'void QDBusObjectPath::setPath(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusobjectpath.html#setPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusObjectPath::setPath(const QString &path)
    self.uglySide.call('ritual_ZN15QDBusObjectPath7setPathERK7QString', path)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDebug)
  def __rlshift__(self, a0: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug a0, const QDBusObjectPath &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusobjectpath.html#operator<<

    Parameters
    ----------

    a0 : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug a0, const QDBusObjectPath &a1)
    address = Rituals.call(
        'ritual_Zls6QDebugRK15QDBusObjectPath',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QDBusObjectPath::QDBusObjectPath()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusobjectpath.html#QDBusObjectPath
    """
    #  QDBusObjectPath::QDBusObjectPath()
    self._noteCreation(QDBusObjectPath, lambda: Rituals.call(
        'ritual_ZN15QDBusObjectPathC1Ev',
    ))

  @overload(str)
  @overload(NoneType)
  def __init__(self, path: Optional[str]) -> None:
    """
    Notes what was given, for Qt's 'QDBusObjectPath::QDBusObjectPath(const
    char *path)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusobjectpath.html#QDBusObjectPath

    Parameters
    ----------

    path : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QDBusObjectPath::QDBusObjectPath(const char *path)
    self._noteCreation(QDBusObjectPath, lambda: Rituals.call(
        'ritual_ZN15QDBusObjectPathC1EPKc', self._bytesOf(path),
    ))

  @overload(QLatin1String)
  def __init__(self, path: QLatin1String) -> None:
    """
    Notes what was given, for Qt's
    'QDBusObjectPath::QDBusObjectPath(QLatin1StringView path)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusobjectpath.html#QDBusObjectPath

    Parameters
    ----------

    path : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  QDBusObjectPath::QDBusObjectPath(QLatin1StringView path)
    self._noteCreation(QDBusObjectPath, lambda: Rituals.call(
        'ritual_ZN15QDBusObjectPathC1E13QLatin1String', self._valueOf(path),
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

  def doCheck(self) -> None:
    """
    Calls Qt's 'void QDBusObjectPath::doCheck()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusobjectpath.html#doCheck
    """
    #  void QDBusObjectPath::doCheck()
    self.uglySide.call('ritual_ZN15QDBusObjectPath7doCheckEv')

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QDBusObjectPath::swap(QDBusObjectPath &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDBusObjectPath.swap' has no cute function yet. Qt's 'void "
        "QDBusObjectPath::swap(QDBusObjectPath &other)': takes a type "
        "Python has no way to hand over yet.")


#  Qt's 'QList<QDBusObjectPath>': the list of QDBusObjectPath, which
#  'QList[QDBusObjectPath]' gives. It is made here, so that there is one as
#  soon as there can be a QDBusObjectPath.
QList.createKind(
    QDBusObjectPath, 'value',
    make='ritual_list_make_QDBusObjectPath',
    add='ritual_list_add_QDBusObjectPath',
    size='ritual_list_size_QDBusObjectPath',
    at='ritual_list_at_QDBusObjectPath',
    drop='ritual_list_drop_QDBusObjectPath',
)
