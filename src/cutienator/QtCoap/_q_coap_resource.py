"""
QCoapResource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/qcoapresource.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtNetwork import QHostAddress
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHostAddress = WAIT['QHostAddress']


class QCoapResource(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCoapResource: a plain Python object standing in
  front of one C++ QCoapResource.

  C++ hands a QCoapResource around as a copy, so every C++ QCoapResource
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCoapResource that has a ritual and that Python can
  call so far, 16 names in all: 'host', 'path', 'title', 'observable',
  'resourceType', 'interface', 'maximumSize', 'contentFormat', 'setHost',
  'setPath', 'setTitle', 'setObservable', 'setResourceType', 'setInterface',
  'setMaximumSize', 'setContentFormat'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCoapResource::~QCoapResource()': the destructor: Python removes
    its C++ QCoapResource by it, and has no other use for it.
  - Qt's 'QCoapResource &QCoapResource::operator=(const QCoapResource
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QCoapResource::swap(QCoapResource &other)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QCoapResource is created at the first use, not by
    'QCoapResource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCoapResource back gives a copy the ritual made for
    Python, in a new cute QCoapResource.
  - Each name of Qt's QCoapResource that has no cute function yet, 'swap',
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
  __qt_class__ = 'QCoapResource'

  #  Qt's '~QCoapResource()'. Naming it makes this a value class: Python owns
  #  every C++ QCoapResource behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QCoapResourceD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def host(self) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress QCoapResource::host() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapresource.html#host

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QCoapResource::host() const
    address = self.uglySide.call('ritual_ZNK13QCoapResource4hostEv')
    from ..QtNetwork import QHostAddress
    return QHostAddress._cuteOwning(address)

  def path(self) -> str:
    """
    Calls Qt's 'QString QCoapResource::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapresource.html#path

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCoapResource::path() const
    return self.uglySide.call('ritual_ZNK13QCoapResource4pathEv')

  def title(self) -> str:
    """
    Calls Qt's 'QString QCoapResource::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapresource.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCoapResource::title() const
    return self.uglySide.call('ritual_ZNK13QCoapResource5titleEv')

  def observable(self) -> bool:
    """
    Calls Qt's 'bool QCoapResource::observable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapresource.html#observable
    """
    #  bool QCoapResource::observable() const
    return self.uglySide.call('ritual_ZNK13QCoapResource10observableEv')

  def resourceType(self) -> str:
    """
    Calls Qt's 'QString QCoapResource::resourceType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapresource.html#resourceType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCoapResource::resourceType() const
    return self.uglySide.call('ritual_ZNK13QCoapResource12resourceTypeEv')

  def interface(self) -> str:
    """
    Calls Qt's 'QString QCoapResource::interface() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapresource.html#interface

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCoapResource::interface() const
    return self.uglySide.call('ritual_ZNK13QCoapResource9interfaceEv')

  def maximumSize(self) -> int:
    """
    Calls Qt's 'int QCoapResource::maximumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapresource.html#maximumSize
    """
    #  int QCoapResource::maximumSize() const
    return self.uglySide.call('ritual_ZNK13QCoapResource11maximumSizeEv')

  def contentFormat(self) -> int:
    """
    Calls Qt's 'uint QCoapResource::contentFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapresource.html#contentFormat
    """
    #  uint QCoapResource::contentFormat() const
    return self.uglySide.call('ritual_ZNK13QCoapResource13contentFormatEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QHostAddress)
  def setHost(self, host: QHostAddress) -> None:
    """
    Calls Qt's 'void QCoapResource::setHost(const QHostAddress &host)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapresource.html#setHost

    Parameters
    ----------

    host : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  void QCoapResource::setHost(const QHostAddress &host)
    self.uglySide.call(
        'ritual_ZN13QCoapResource7setHostERK12QHostAddress',
        self._valueOf(host),
    )

  @overload(str)
  def setPath(self, path: str) -> None:
    """
    Calls Qt's 'void QCoapResource::setPath(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapresource.html#setPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCoapResource::setPath(const QString &path)
    self.uglySide.call('ritual_ZN13QCoapResource7setPathERK7QString', path)

  @overload(str)
  def setTitle(self, title: str) -> None:
    """
    Calls Qt's 'void QCoapResource::setTitle(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapresource.html#setTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCoapResource::setTitle(const QString &title)
    self.uglySide.call('ritual_ZN13QCoapResource8setTitleERK7QString', title)

  @overload(bool)
  def setObservable(self, observable: bool) -> None:
    """
    Calls Qt's 'void QCoapResource::setObservable(bool observable)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapresource.html#setObservable

    Parameters
    ----------

    observable : bool
      Passed on as it is.
    """
    #  void QCoapResource::setObservable(bool observable)
    self.uglySide.call(
        'ritual_ZN13QCoapResource13setObservableEb', observable,
    )

  @overload(str)
  def setResourceType(self, resourceType: str) -> None:
    """
    Calls Qt's 'void QCoapResource::setResourceType(const QString
    &resourceType)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapresource.html#setResourceType

    Parameters
    ----------

    resourceType : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCoapResource::setResourceType(const QString &resourceType)
    self.uglySide.call(
        'ritual_ZN13QCoapResource15setResourceTypeERK7QString', resourceType,
    )

  @overload(str)
  def setInterface(self, interface: str) -> None:
    """
    Calls Qt's 'void QCoapResource::setInterface(const QString &interface)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapresource.html#setInterface

    Parameters
    ----------

    interface : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCoapResource::setInterface(const QString &interface)
    self.uglySide.call(
        'ritual_ZN13QCoapResource12setInterfaceERK7QString', interface,
    )

  @overload(int)
  def setMaximumSize(self, maximumSize: int) -> None:
    """
    Calls Qt's 'void QCoapResource::setMaximumSize(int maximumSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapresource.html#setMaximumSize

    Parameters
    ----------

    maximumSize : int
      Passed on as it is.
    """
    #  void QCoapResource::setMaximumSize(int maximumSize)
    self.uglySide.call(
        'ritual_ZN13QCoapResource14setMaximumSizeEi', maximumSize,
    )

  @overload(int)
  def setContentFormat(self, contentFormat: int) -> None:
    """
    Calls Qt's 'void QCoapResource::setContentFormat(uint contentFormat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapresource.html#setContentFormat

    Parameters
    ----------

    contentFormat : int
      Passed on as it is.
    """
    #  void QCoapResource::setContentFormat(uint contentFormat)
    self.uglySide.call(
        'ritual_ZN13QCoapResource16setContentFormatEj', contentFormat,
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
    Notes what was given, for Qt's 'QCoapResource::QCoapResource()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcoapresource.html#QCoapResource
    """
    #  QCoapResource::QCoapResource()
    self._noteCreation(QCoapResource, lambda: Rituals.call(
        'ritual_ZN13QCoapResourceC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QCoapResource) -> None:
    """
    Notes what was given, for Qt's 'QCoapResource::QCoapResource(const
    QCoapResource &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcoapresource.html#QCoapResource

    Parameters
    ----------

    other : QCoapResource
      Passed on as a value: Qt reads the C++ QCoapResource, which stays
      Python's own.
    """
    #  QCoapResource::QCoapResource(const QCoapResource &other)
    self._noteCreation(QCoapResource, lambda: Rituals.call(
        'ritual_ZN13QCoapResourceC1ERKS_', self._valueOf(other),
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
    Qt's 'void QCoapResource::swap(QCoapResource &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCoapResource.swap' has no cute function yet. Qt's 'void "
        "QCoapResource::swap(QCoapResource &other)': takes a type Python "
        "has no way to hand over yet.")


#  Qt's 'QList<QCoapResource>': the list of QCoapResource, which
#  'QList[QCoapResource]' gives. It is made here, so that there is one as
#  soon as there can be a QCoapResource.
QList.createKind(
    QCoapResource, 'value',
    make='ritual_list_make_QCoapResource',
    add='ritual_list_add_QCoapResource',
    size='ritual_list_size_QCoapResource',
    at='ritual_list_at_QCoapResource',
    drop='ritual_list_drop_QCoapResource',
)
