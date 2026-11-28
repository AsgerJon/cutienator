"""
QNetworkInformationBackendFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkinformation_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNetworkInformationBackendFactory to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QNetworkInformation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QNetworkInformationBackend

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNetworkInformationBackendFactory(QObject):
  """
  The cute side of Qt's QNetworkInformationBackendFactory: a plain Python
  object standing in front of one C++ QNetworkInformationBackendFactory.

  It is built on the cute 'QObject', as Qt's
  QNetworkInformationBackendFactory is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkInformationBackendFactory that has a ritual
  and that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'name', 'create', 'featuresSupported'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNetworkInformationBackendFactory::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QNetworkInformationBackendFactory::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QNetworkInformationBackendFactory::~QNetworkInformationBackendFactory(
    )': the destructor: Python never removes a C++
    QNetworkInformationBackendFactory.

  What has no ritual
  ------------------

  7 of the 15 functions Qt declares: 4 forbidden; 2 not a gap; 1 the class is
  abstract, so C++ cannot make one, and the C++ class of ours does not fill
  in every function it leaves open.

  What to expect
  --------------

  - The C++ QNetworkInformationBackendFactory is created at the first use,
    not by 'QNetworkInformationBackendFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkInformationBackendFactory.
  - Qt tells when it has removed the C++ QNetworkInformationBackendFactory.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QNetworkInformationBackendFactory that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QNetworkInformationBackendFactory::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformationbackendfactory.html#tr

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
    #  QString QNetworkInformationBackendFactory::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN33QNetworkInformationBackendFactory2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkInformationBackendFactory'

  #  A C++ QNetworkInformationBackendFactory Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNetworkInformationBackendFactory'

  #  The functions Qt calls itself that QNetworkInformationBackendFactory is
  #  the first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'create': (
          'QNetworkInformationBackend '
          '*QNetworkInformationBackendFactory::create(Features) const',
      ),
      'featuresSupported': (
          'Features QNetworkInformationBackendFactory::featuresSupported() '
          'const',
      ),
  }

  #  The functions Qt calls itself that QNetworkInformationBackendFactory is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'name': (
          ('_ZNK33QNetworkInformationBackendFactory4nameEv',
           ('address', 'text', ''),
           ()),
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
    Calls Qt's 'const QMetaObject
    *QNetworkInformationBackendFactory::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformationbackendfactory.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNetworkInformationBackendFactory::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK33QNetworkInformationBackendFactory10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QNetworkInformationBackendFactory::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformationbackendfactory.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNetworkInformationBackendFactory::name() const
    return self.uglySide.call(
        'ritual_ZNK33QNetworkInformationBackendFactory4nameEv',
    )

  @overload(QNetworkInformation.Features)
  def create(
      self,
      requiredFeatures: QNetworkInformation.Features,
  ) -> Optional[QNetworkInformationBackend]:
    """
    Calls Qt's 'QNetworkInformationBackend
    *QNetworkInformationBackendFactory::create(Features requiredFeatures)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformationbackendfactory.html#create

    Parameters
    ----------

    requiredFeatures : QNetworkInformation.Features
      Passed on as its number.

    Returns
    -------

    Optional[QNetworkInformationBackend]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkInformationBackend
    #      *QNetworkInformationBackendFactory::create(Features
    #      requiredFeatures) const
    address = self.uglySide.call(
        'ritual_ZNK33QNetworkInformationBackendFactory6createE6QFlagsIN19QN'
        'etworkInformation7FeatureEE',
        requiredFeatures.value,
    )
    from . import QNetworkInformationBackend
    return QNetworkInformationBackend._cuteAt(address)

  def featuresSupported(self) -> QNetworkInformation.Features:
    """
    Calls Qt's 'Features
    QNetworkInformationBackendFactory::featuresSupported() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinformationbackendfactory.html

    Returns
    -------

    QNetworkInformation.Features
      The value standing for the combination Qt gave back.
    """
    #  Features QNetworkInformationBackendFactory::featuresSupported() const
    return QNetworkInformation.Features(self.uglySide.call(
        'ritual_ZNK33QNetworkInformationBackendFactory17featuresSupportedEv',
    ))

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
    Qt's
    'QNetworkInformationBackendFactory::QNetworkInformationBackendFactory()':
    the class is abstract, so C++ cannot make one, and the C++ class of ours
    does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QNetworkInformationBackendFactory.__init__' has no cute function "
        "yet. Qt's "
        "'QNetworkInformationBackendFactory::QNetworkInformationBackendFacto"
        "ry()': the class is abstract, so C++ cannot make one, and the C++ "
        "class of ours does not fill in every function it leaves open.")

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
