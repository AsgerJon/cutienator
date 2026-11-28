"""
QNetworkAccessBackendFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkaccessbackend_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNetworkAccessBackendFactory to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from . import QNetworkAccessManager

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QNetworkAccessBackend, QNetworkRequest
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QNetworkRequest = WAIT['QNetworkRequest']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNetworkAccessBackendFactory(QObject):
  """
  The cute side of Qt's QNetworkAccessBackendFactory: a plain Python object
  standing in front of one C++ QNetworkAccessBackendFactory.

  It is built on the cute 'QObject', as Qt's QNetworkAccessBackendFactory is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkAccessBackendFactory that has a ritual and
  that Python can call so far, 4 names in all: 'metaObject', 'tr',
  'supportedSchemes', 'create'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNetworkAccessBackendFactory::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QNetworkAccessBackendFactory::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QNetworkAccessBackendFactory::~QNetworkAccessBackendFactory()': the
    destructor: Python never removes a C++ QNetworkAccessBackendFactory.

  What has no ritual
  ------------------

  3 of the 10 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QNetworkAccessBackendFactory is created at the first use, not by
    'QNetworkAccessBackendFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkAccessBackendFactory.
  - Qt tells when it has removed the C++ QNetworkAccessBackendFactory. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QNetworkAccessBackendFactory that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString QNetworkAccessBackendFactory::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackendfactory.html#tr

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
    #  QString QNetworkAccessBackendFactory::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QNetworkAccessBackendFactory2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkAccessBackendFactory'

  #  A C++ QNetworkAccessBackendFactory Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNetworkAccessBackendFactory'

  #  The functions Qt calls itself that QNetworkAccessBackendFactory is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'supportedSchemes': (
          'QStringList QNetworkAccessBackendFactory::supportedSchemes() '
          'const',
      ),
  }

  #  The functions Qt calls itself that QNetworkAccessBackendFactory is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'create': (
          ('_ZNK28QNetworkAccessBackendFactory6createEN21QNetworkAccessMana'
           'ger9OperationERK15QNetworkRequest',
           ('address', 'address', 'QtNetwork:QNetworkAccessBackend'),
           (
               ('int', 'enum', 'QtNetwork:QNetworkAccessManager.Operation'),
               ('address', 'value', 'QtNetwork:QNetworkRequest'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QNetworkAccessBackendFactory::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackendfactory.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNetworkAccessBackendFactory::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QNetworkAccessBackendFactory10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def supportedSchemes(self) -> QStringList:
    """
    Calls Qt's 'QStringList QNetworkAccessBackendFactory::supportedSchemes()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackendfactory.html#supportedSchemes

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QNetworkAccessBackendFactory::supportedSchemes() const
    address = self.uglySide.call(
        'ritual_ZNK28QNetworkAccessBackendFactory16supportedSchemesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(QNetworkAccessManager.Operation, QNetworkRequest)
  def create(
      self,
      op: QNetworkAccessManager.Operation,
      request: QNetworkRequest,
  ) -> Optional[QNetworkAccessBackend]:
    """
    Calls Qt's 'QNetworkAccessBackend
    *QNetworkAccessBackendFactory::create(QNetworkAccessManager::Operation
    op, const QNetworkRequest &request) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackendfactory.html#create

    Parameters
    ----------

    op : QNetworkAccessManager.Operation
      Passed on as its number.

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    Returns
    -------

    Optional[QNetworkAccessBackend]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkAccessBackend
    #      *QNetworkAccessBackendFactory::create(QNetworkAccessManager::
    #      Operation op, const QNetworkRequest &request) const
    address = self.uglySide.call(
        'ritual_ZNK28QNetworkAccessBackendFactory6createEN21QNetworkAccessM'
        'anager9OperationERK15QNetworkRequest',
        op.value, self._valueOf(request),
    )
    from . import QNetworkAccessBackend
    return QNetworkAccessBackend._cuteAt(address)

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
    Qt's 'QNetworkAccessBackendFactory::QNetworkAccessBackendFactory()': the
    class is abstract, so C++ cannot make one, and the C++ class of ours does
    not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QNetworkAccessBackendFactory.__init__' has no cute function yet. "
        "Qt's "
        "'QNetworkAccessBackendFactory::QNetworkAccessBackendFactory()': "
        "the class is abstract, so C++ cannot make one, and the C++ class "
        "of ours does not fill in every function it leaves open.")

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
