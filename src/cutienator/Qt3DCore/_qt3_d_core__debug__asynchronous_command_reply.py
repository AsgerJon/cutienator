"""
Qt3DCore::Debug::AsynchronousCommandReply binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qabstractaspect_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DCore::Debug::AsynchronousCommandReply to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AsynchronousCommandReply(QObject):
  """
  The cute side of Qt's Qt3DCore::Debug::AsynchronousCommandReply: a plain
  Python object standing in front of one C++
  Qt3DCore::Debug::AsynchronousCommandReply.

  It is built on the cute 'QObject', as Qt's
  Qt3DCore::Debug::AsynchronousCommandReply is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::Debug::AsynchronousCommandReply that has a
  ritual and that Python can call so far, 8 names in all: 'metaObject', 'tr',
  'data', 'commandName', 'isFinished', 'setFinished', 'setData', 'finished'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::Debug::AsynchronousCommandReply::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DCore::Debug::AsynchronousCommandReply::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::Debug::AsynchronousCommandReply is created at the first
    use, not by 'Qt3DCore::Debug::AsynchronousCommandReply(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::Debug::AsynchronousCommandReply.
  - Qt tells when it has removed the C++
    Qt3DCore::Debug::AsynchronousCommandReply. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
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
    Calls Qt's 'QString Qt3DCore::Debug::AsynchronousCommandReply::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-debug-asynchronouscommandreply.html#tr

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
    #  QString Qt3DCore::Debug::AsynchronousCommandReply::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore5Debug24AsynchronousCommandReply2trEPKcS3_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::Debug::AsynchronousCommandReply'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DCore::Debug::AsynchronousCommandReply::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-debug-asynchronouscommandreply.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *Qt3DCore::Debug::AsynchronousCommandReply::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Debug24AsynchronousCommandReply10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def data(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray Qt3DCore::Debug::AsynchronousCommandReply::data()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-debug-asynchronouscommandreply.html#data

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DCore::Debug::AsynchronousCommandReply::data() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Debug24AsynchronousCommandReply4dataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def commandName(self) -> str:
    """
    Calls Qt's 'QString
    Qt3DCore::Debug::AsynchronousCommandReply::commandName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-debug-asynchronouscommandreply.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::Debug::AsynchronousCommandReply::commandName() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Debug24AsynchronousCommandReply11commandNameEv',
    )

  def isFinished(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::Debug::AsynchronousCommandReply::isFinished()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-debug-asynchronouscommandreply.html
    """
    #  bool Qt3DCore::Debug::AsynchronousCommandReply::isFinished() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Debug24AsynchronousCommandReply10isFinishedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setFinished(self, finished: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Debug::AsynchronousCommandReply::setFinished(bool finished)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-debug-asynchronouscommandreply.html

    Parameters
    ----------

    finished : bool
      Passed on as it is.
    """
    #  void Qt3DCore::Debug::AsynchronousCommandReply::setFinished(bool
    #      finished)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Debug24AsynchronousCommandReply11setFinishedEb',
        finished,
    )

  @overload(QByteArray)
  def setData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void Qt3DCore::Debug::AsynchronousCommandReply::setData(const
    QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-debug-asynchronouscommandreply.html

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DCore::Debug::AsynchronousCommandReply::setData(const
    #      QByteArray &data)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Debug24AsynchronousCommandReply7setDataERK10QBy'
        'teArray',
        self._valueOf(data),
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

  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(
      self,
      commandName: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::Debug::AsynchronousCommandReply::AsynchronousCommandReply(
    const QString &commandName, QObject *parent)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-debug-asynchronouscommandreply.html

    Parameters
    ----------

    commandName : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::Debug::AsynchronousCommandReply::
    #      AsynchronousCommandReply(const QString &commandName, QObject
    #      *parent)
    self._noteCreation(AsynchronousCommandReply, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore5Debug24AsynchronousCommandReplyC1ERK7QStringP7Q'
        'Object',
        commandName, self._addressOf(parent, 'QObject'),
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

  @overload(THIS)
  @overload(NoneType)
  def finished(self, reply: Optional[AsynchronousCommandReply]) -> None:
    """
    Calls Qt's 'void Qt3DCore::Debug::AsynchronousCommandReply::finished(
    AsynchronousCommandReply *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-debug-asynchronouscommandreply.html

    Parameters
    ----------

    reply : Optional[AsynchronousCommandReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::Debug::AsynchronousCommandReply::finished(
    #      AsynchronousCommandReply *reply)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Debug24AsynchronousCommandReply8finishedEPS1_',
        self._addressOf(reply),
    )
