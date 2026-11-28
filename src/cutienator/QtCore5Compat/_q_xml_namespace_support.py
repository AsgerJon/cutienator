"""
QXmlNamespaceSupport binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QXmlNamespaceSupport(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXmlNamespaceSupport: a plain Python object standing
  in front of one C++ QXmlNamespaceSupport.

  What exists
  -----------

  Every function of Qt's QXmlNamespaceSupport that has a ritual and that
  Python can call so far, 7 names in all: 'setPrefix', 'prefix', 'uri',
  'prefixes', 'pushContext', 'popContext', 'reset'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlNamespaceSupport::~QXmlNamespaceSupport()': the destructor:
    Python never removes a C++ QXmlNamespaceSupport.
  - Qt's 'void QXmlNamespaceSupport::splitName(const QString &a0, QString
    &a1, QString &a2) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QXmlNamespaceSupport::processName(const QString &a0, bool a1,
    QString &a2, QString &a3) const': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QXmlNamespaceSupport is created at the first use, not by
    'QXmlNamespaceSupport(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QXmlNamespaceSupport.
  - Each name of Qt's QXmlNamespaceSupport that has no cute function yet,
    'processName', 'splitName', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXmlNamespaceSupport'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def prefix(self, a0: str) -> str:
    """
    Calls Qt's 'QString QXmlNamespaceSupport::prefix(const QString &a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlnamespacesupport.html#prefix

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlNamespaceSupport::prefix(const QString &a0) const
    return self.uglySide.call(
        'ritual_ZNK20QXmlNamespaceSupport6prefixERK7QString', a0,
    )

  @overload(str)
  def uri(self, a0: str) -> str:
    """
    Calls Qt's 'QString QXmlNamespaceSupport::uri(const QString &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlnamespacesupport.html#uri

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlNamespaceSupport::uri(const QString &a0) const
    return self.uglySide.call(
        'ritual_ZNK20QXmlNamespaceSupport3uriERK7QString', a0,
    )

  @overload()
  def prefixes(self) -> QStringList:
    """
    Calls Qt's 'QStringList QXmlNamespaceSupport::prefixes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlnamespacesupport.html#prefixes

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QXmlNamespaceSupport::prefixes() const
    address = self.uglySide.call(
        'ritual_ZNK20QXmlNamespaceSupport8prefixesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def prefixes(self, a0: str) -> QStringList:
    """
    Calls Qt's 'QStringList QXmlNamespaceSupport::prefixes(const QString &a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlnamespacesupport.html#prefixes

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QXmlNamespaceSupport::prefixes(const QString &a0) const
    address = self.uglySide.call(
        'ritual_ZNK20QXmlNamespaceSupport8prefixesERK7QString', a0,
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, str)
  def setPrefix(self, a0: str, a1: str) -> None:
    """
    Calls Qt's 'void QXmlNamespaceSupport::setPrefix(const QString &a0, const
    QString &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlnamespacesupport.html#setPrefix

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlNamespaceSupport::setPrefix(const QString &a0, const QString
    #      &a1)
    self.uglySide.call(
        'ritual_ZN20QXmlNamespaceSupport9setPrefixERK7QStringS2_', a0, a1,
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
    Notes what was given, for Qt's
    'QXmlNamespaceSupport::QXmlNamespaceSupport()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlnamespacesupport.html#QXmlNamespaceSupport
    """
    #  QXmlNamespaceSupport::QXmlNamespaceSupport()
    self._noteCreation(QXmlNamespaceSupport, lambda: Rituals.call(
        'ritual_ZN20QXmlNamespaceSupportC1Ev',
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

  def pushContext(self) -> None:
    """
    Calls Qt's 'void QXmlNamespaceSupport::pushContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlnamespacesupport.html#pushContext
    """
    #  void QXmlNamespaceSupport::pushContext()
    self.uglySide.call('ritual_ZN20QXmlNamespaceSupport11pushContextEv')

  def popContext(self) -> None:
    """
    Calls Qt's 'void QXmlNamespaceSupport::popContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlnamespacesupport.html#popContext
    """
    #  void QXmlNamespaceSupport::popContext()
    self.uglySide.call('ritual_ZN20QXmlNamespaceSupport10popContextEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QXmlNamespaceSupport::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlnamespacesupport.html#reset
    """
    #  void QXmlNamespaceSupport::reset()
    self.uglySide.call('ritual_ZN20QXmlNamespaceSupport5resetEv')

  @staticmethod
  def processName(*__, **_) -> Never:
    """
    Qt's 'void QXmlNamespaceSupport::processName(const QString &a0, bool a1,
    QString &a2, QString &a3) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QXmlNamespaceSupport.processName' has no cute function yet. Qt's "
        "'void QXmlNamespaceSupport::processName(const QString &a0, bool "
        "a1, QString &a2, QString &a3) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def splitName(*__, **_) -> Never:
    """
    Qt's 'void QXmlNamespaceSupport::splitName(const QString &a0, QString
    &a1, QString &a2) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QXmlNamespaceSupport.splitName' has no cute function yet. Qt's "
        "'void QXmlNamespaceSupport::splitName(const QString &a0, QString "
        "&a1, QString &a2) const': takes a type Python has no way to hand "
        "over yet.")
