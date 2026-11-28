"""
QCoapResourceDiscoveryReply binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/qcoapresourcediscoveryreply.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QCoapReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QCoapRequest, QCoapResource
  from . import QCoapResourceDiscoveryReplyPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCoapRequest = WAIT['QCoapRequest']
  QCoapResource = WAIT['QCoapResource']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCoapResourceDiscoveryReply(QCoapReply):
  """
  The cute side of Qt's QCoapResourceDiscoveryReply: a plain Python object
  standing in front of one C++ QCoapResourceDiscoveryReply.

  It is built on the cute 'QCoapReply', as Qt's QCoapResourceDiscoveryReply
  is built on Qt's QCoapReply, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCoapResourceDiscoveryReply that has a ritual and
  that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'resources', 'discovered', 'd_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCoapResourceDiscoveryReply::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QCoapResourceDiscoveryReply::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QCoapResourceDiscoveryReplyPrivate
    *QCoapResourceDiscoveryReply::d_func() const': takes in Python what
    'QCoapResourceDiscoveryReplyPrivate
    *QCoapResourceDiscoveryReply::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QCoapResourceDiscoveryReply is created at the first use, not by
    'QCoapResourceDiscoveryReply(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCoapResourceDiscoveryReply.
  - Qt tells when it has removed the C++ QCoapResourceDiscoveryReply. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QCoapResourceDiscoveryReply::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapresourcediscoveryreply.html#tr

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
    #  QString QCoapResourceDiscoveryReply::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QCoapResourceDiscoveryReply2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoapResourceDiscoveryReply'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCoapResourceDiscoveryReply::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapresourcediscoveryreply.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCoapResourceDiscoveryReply::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QCoapResourceDiscoveryReply10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def resources(self) -> QList[QCoapResource]:
    """
    Calls Qt's 'QList<QCoapResource> QCoapResourceDiscoveryReply::resources()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapresourcediscoveryreply.html#resources

    Returns
    -------

    QList[QCoapResource]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCoapResource> QCoapResourceDiscoveryReply::resources() const
    address = self.uglySide.call(
        'ritual_ZNK27QCoapResourceDiscoveryReply9resourcesEv',
    )
    from . import QCoapResource
    return QList[QCoapResource]._cuteOwning(address)

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

  @overload(QCoapRequest)
  @overload(QCoapRequest, QObject)
  @overload(QCoapRequest, NoneType)
  def __init__(
      self,
      request: QCoapRequest,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCoapResourceDiscoveryReply::QCoapResourceDiscoveryReply(const
    QCoapRequest &request, QObject *parent)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapresourcediscoveryreply.html

    Parameters
    ----------

    request : QCoapRequest
      Passed on as a value: Qt reads the C++ QCoapRequest, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCoapResourceDiscoveryReply::QCoapResourceDiscoveryReply(const
    #      QCoapRequest &request, QObject *parent)
    self._noteCreation(QCoapResourceDiscoveryReply, lambda: Rituals.call(
        'ritual_ZN27QCoapResourceDiscoveryReplyC1ERK12QCoapRequestP7QObject',
        self._valueOf(request), self._addressOf(parent, 'QObject'),
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

  @overload(THIS, QList[QCoapResource])
  @overload(NoneType, QList[QCoapResource])
  def discovered(
      self,
      reply: Optional[QCoapResourceDiscoveryReply],
      resources: QList[QCoapResource],
  ) -> None:
    """
    Calls Qt's 'void
    QCoapResourceDiscoveryReply::discovered(QCoapResourceDiscoveryReply
    *reply, QList<QCoapResource> resources)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapresourcediscoveryreply.html#discovered

    Parameters
    ----------

    reply : Optional[QCoapResourceDiscoveryReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resources : QList[QCoapResource]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QCoapResourceDiscoveryReply::discovered(
    #      QCoapResourceDiscoveryReply *reply, QList<QCoapResource>
    #      resources)
    self.uglySide.call(
        'ritual_ZN27QCoapResourceDiscoveryReply10discoveredEPS_5QListI13QCo'
        'apResourceE',
        self._addressOf(reply), self._valueOf(resources),
    )

  def d_func(self) -> Optional[QCoapResourceDiscoveryReplyPrivate]:
    """
    Calls Qt's 'QCoapResourceDiscoveryReplyPrivate
    *QCoapResourceDiscoveryReply::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapresourcediscoveryreply.html#d_func

    Returns
    -------

    Optional[QCoapResourceDiscoveryReplyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapResourceDiscoveryReplyPrivate
    #      *QCoapResourceDiscoveryReply::d_func()
    address = self.uglySide.call(
        'ritual_ZN27QCoapResourceDiscoveryReply6d_funcEv',
    )
    from . import QCoapResourceDiscoveryReplyPrivate
    return QCoapResourceDiscoveryReplyPrivate._cuteAt(address)
