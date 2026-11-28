"""
QNetworkProxyFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qnetworkproxy.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QNetworkProxy, QNetworkProxyQuery
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QNetworkProxyQuery = WAIT['QNetworkProxyQuery']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNetworkProxyFactory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNetworkProxyFactory: a plain Python object standing
  in front of one C++ QNetworkProxyFactory.

  What exists
  -----------

  Every function of Qt's QNetworkProxyFactory that has a ritual and that
  Python can call so far, 6 names in all: 'queryProxy',
  'usesSystemConfiguration', 'setUseSystemConfiguration',
  'setApplicationProxyFactory', 'proxyForQuery', 'systemProxyForQuery'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNetworkProxyFactory::~QNetworkProxyFactory()': the destructor:
    Python never removes a C++ QNetworkProxyFactory.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ QNetworkProxyFactory is created at the first use, not by
    'QNetworkProxyFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkProxyFactory.
  - Each name of Qt's QNetworkProxyFactory that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def usesSystemConfiguration() -> bool:
    """
    Calls Qt's 'bool QNetworkProxyFactory::usesSystemConfiguration()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkproxyfactory.html#usesSystemConfiguration
    """
    #  bool QNetworkProxyFactory::usesSystemConfiguration()
    return Rituals.call(
        'ritual_ZN20QNetworkProxyFactory23usesSystemConfigurationEv',
    )

  @staticmethod
  @overload(bool)
  def setUseSystemConfiguration(enable: bool) -> None:
    """
    Calls Qt's 'void QNetworkProxyFactory::setUseSystemConfiguration(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkproxyfactory.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QNetworkProxyFactory::setUseSystemConfiguration(bool enable)
    Rituals.call(
        'ritual_ZN20QNetworkProxyFactory25setUseSystemConfigurationEb',
        enable,
    )

  @staticmethod
  @overload(THIS)
  @overload(NoneType)
  def setApplicationProxyFactory(
      factory: Optional[QNetworkProxyFactory],
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkProxyFactory::setApplicationProxyFactory(QNetworkProxyFactory
    *factory)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkproxyfactory.html

    Parameters
    ----------

    factory : Optional[QNetworkProxyFactory]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkProxyFactory::setApplicationProxyFactory(
    #      QNetworkProxyFactory *factory)
    Rituals.call(
        'ritual_ZN20QNetworkProxyFactory26setApplicationProxyFactoryEPS_',
        CuteMixin._addressOf(factory),
    )

  @staticmethod
  @overload(QNetworkProxyQuery)
  def proxyForQuery(query: QNetworkProxyQuery) -> QList[QNetworkProxy]:
    """
    Calls Qt's 'QList<QNetworkProxy>
    QNetworkProxyFactory::proxyForQuery(const QNetworkProxyQuery &query)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkproxyfactory.html#proxyForQuery

    Parameters
    ----------

    query : QNetworkProxyQuery
      Passed on as a value: Qt reads the C++ QNetworkProxyQuery, which stays
      Python's own.

    Returns
    -------

    QList[QNetworkProxy]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QNetworkProxy> QNetworkProxyFactory::proxyForQuery(const
    #      QNetworkProxyQuery &query)
    address = Rituals.call(
        'ritual_ZN20QNetworkProxyFactory13proxyForQueryERK18QNetworkProxyQu'
        'ery',
        CuteMixin._valueOf(query),
    )
    from . import QNetworkProxy
    return QList[QNetworkProxy]._cuteOwning(address)

  @staticmethod
  @overload()
  @overload(QNetworkProxyQuery)
  def systemProxyForQuery(
      query: Optional[QNetworkProxyQuery] = None,
  ) -> QList[QNetworkProxy]:
    """
    Calls Qt's 'QList<QNetworkProxy>
    QNetworkProxyFactory::systemProxyForQuery(const QNetworkProxyQuery
    &query)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkproxyfactory.html#systemProxyForQuery

    Parameters
    ----------

    query : Optional[QNetworkProxyQuery]
      Passed on as a value: Qt reads the C++ QNetworkProxyQuery, which stays
      Python's own. May be left out, as in Qt: a new 'QNetworkProxyQuery()'
      is then passed on.

    Returns
    -------

    QList[QNetworkProxy]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QNetworkProxy> QNetworkProxyFactory::systemProxyForQuery(const
    #      QNetworkProxyQuery &query)
    if query is None:
      from . import QNetworkProxyQuery
      query = QNetworkProxyQuery()
    address = Rituals.call(
        'ritual_ZN20QNetworkProxyFactory19systemProxyForQueryERK18QNetworkP'
        'roxyQuery',
        CuteMixin._valueOf(query),
    )
    from . import QNetworkProxy
    return QList[QNetworkProxy]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkProxyFactory'

  #  The functions Qt calls itself that QNetworkProxyFactory is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'queryProxy': (
          'QList<QNetworkProxy> QNetworkProxyFactory::queryProxy(const '
          'QNetworkProxyQuery &)',
      ),
  }

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QNetworkProxyFactory::QNetworkProxyFactory()': the class is
    abstract, so C++ cannot make one, and the C++ class of ours does not fill
    in every function it leaves open.
    """
    raise NotImplementedError(
        "'QNetworkProxyFactory.__init__' has no cute function yet. Qt's "
        "'QNetworkProxyFactory::QNetworkProxyFactory()': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open.")

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

  @overload()
  @overload(QNetworkProxyQuery)
  def queryProxy(
      self,
      query: Optional[QNetworkProxyQuery] = None,
  ) -> QList[QNetworkProxy]:
    """
    Calls Qt's 'QList<QNetworkProxy> QNetworkProxyFactory::queryProxy(const
    QNetworkProxyQuery &query)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkproxyfactory.html#queryProxy

    Parameters
    ----------

    query : Optional[QNetworkProxyQuery]
      Passed on as a value: Qt reads the C++ QNetworkProxyQuery, which stays
      Python's own. May be left out, as in Qt: a new 'QNetworkProxyQuery()'
      is then passed on.

    Returns
    -------

    QList[QNetworkProxy]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QNetworkProxy> QNetworkProxyFactory::queryProxy(const
    #      QNetworkProxyQuery &query)
    if query is None:
      from . import QNetworkProxyQuery
      query = QNetworkProxyQuery()
    address = self.uglySide.call(
        'ritual_ZN20QNetworkProxyFactory10queryProxyERK18QNetworkProxyQuery',
        self._valueOf(query),
    )
    from . import QNetworkProxy
    return QList[QNetworkProxy]._cuteOwning(address)
