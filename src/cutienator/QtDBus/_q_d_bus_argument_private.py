"""
QDBusArgumentPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/6.12.0/QtDBus/private/qdbusargument_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDBusArgumentPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QDBusArgument, QDBusDemarshaller, QDBusMarshaller

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusArgumentPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDBusArgumentPrivate: a plain Python object standing
  in front of one C++ QDBusArgumentPrivate.

  What exists
  -----------

  Every function of Qt's QDBusArgumentPrivate that has a ritual and that
  Python can call so far, 4 names in all: 'checkRead', 'marshaller',
  'demarshaller', 'create'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDBusArgumentPrivate::~QDBusArgumentPrivate()': the destructor:
    Python never removes a C++ QDBusArgumentPrivate.
  - Qt's 'QDBusArgumentPrivate *QDBusArgumentPrivate::d(QDBusArgument &q)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  8 of the 14 functions Qt declares: 4 forbidden; 2 takes or gives a type
  that cannot be passed yet; 1 leans on 'qdbus_loadLibDBus()', which Qt's
  source does not mark for use from outside Qt and has no code for that could
  be taken; 1 leans on 'qdbus_resolve_me(char const*)', which Qt's source
  does not mark for use from outside Qt and has no code for that could be
  taken.

  What to expect
  --------------

  - The C++ QDBusArgumentPrivate is created at the first use, not by
    'QDBusArgumentPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusArgumentPrivate.
  - Each name of Qt's QDBusArgumentPrivate that has no cute function yet,
    '__init__', 'checkReadAndDetach', 'checkWrite', 'createSignature', 'd',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QDBusArgumentPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Direction(CuteNum, scoped=True):
    """
    The enum 'QDBusArgumentPrivate::Direction' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Marshalling = Kee[int](0)
    Demarshalling = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS)
  @overload(NoneType)
  def checkRead(d: Optional[QDBusArgumentPrivate]) -> bool:
    """
    Calls Qt's 'bool QDBusArgumentPrivate::checkRead(QDBusArgumentPrivate
    *d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusargumentprivate.html#checkRead

    Parameters
    ----------

    d : Optional[QDBusArgumentPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDBusArgumentPrivate::checkRead(QDBusArgumentPrivate *d)
    return Rituals.call(
        'ritual_ZN20QDBusArgumentPrivate9checkReadEPS_',
        CuteMixin._addressOf(d),
    )

  @staticmethod
  @overload(THIS)
  @overload(NoneType)
  def create(d: Optional[QDBusArgumentPrivate]) -> QDBusArgument:
    """
    Calls Qt's 'QDBusArgument
    QDBusArgumentPrivate::create(QDBusArgumentPrivate *d)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusargumentprivate.html#create

    Parameters
    ----------

    d : Optional[QDBusArgumentPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QDBusArgument
      A new cute QDBusArgument around the copy Qt gave back. Python owns it.
    """
    #  QDBusArgument QDBusArgumentPrivate::create(QDBusArgumentPrivate *d)
    address = Rituals.call(
        'ritual_ZN20QDBusArgumentPrivate6createEPS_',
        CuteMixin._addressOf(d),
    )
    from . import QDBusArgument
    return QDBusArgument._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusArgumentPrivate'

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
    Qt's 'QDBusArgumentPrivate::QDBusArgumentPrivate(Direction direction,
    QDBusConnection::ConnectionCapabilities flags)': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusArgumentPrivate.__init__' has no cute function yet. Qt's "
        "'QDBusArgumentPrivate::QDBusArgumentPrivate(Direction direction, "
        "QDBusConnection::ConnectionCapabilities flags)': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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

  def marshaller(self) -> Optional[QDBusMarshaller]:
    """
    Calls Qt's 'QDBusMarshaller *QDBusArgumentPrivate::marshaller()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusargumentprivate.html#marshaller

    Returns
    -------

    Optional[QDBusMarshaller]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDBusMarshaller *QDBusArgumentPrivate::marshaller()
    address = self.uglySide.call(
        'ritual_ZN20QDBusArgumentPrivate10marshallerEv',
    )
    from . import QDBusMarshaller
    return QDBusMarshaller._cuteAt(address)

  def demarshaller(self) -> Optional[QDBusDemarshaller]:
    """
    Calls Qt's 'QDBusDemarshaller *QDBusArgumentPrivate::demarshaller()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusargumentprivate.html#demarshaller

    Returns
    -------

    Optional[QDBusDemarshaller]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDBusDemarshaller *QDBusArgumentPrivate::demarshaller()
    address = self.uglySide.call(
        'ritual_ZN20QDBusArgumentPrivate12demarshallerEv',
    )
    from . import QDBusDemarshaller
    return QDBusDemarshaller._cuteAt(address)

  @staticmethod
  def checkReadAndDetach(*__, **_) -> Never:
    """
    Qt's 'bool QDBusArgumentPrivate::checkReadAndDetach(QDBusArgumentPrivate
    *&d)': takes or gives a type that cannot be passed yet:
    QDBusArgumentPrivate *&.
    """
    raise NotImplementedError(
        "'QDBusArgumentPrivate.checkReadAndDetach' has no cute function "
        "yet. Qt's 'bool "
        "QDBusArgumentPrivate::checkReadAndDetach(QDBusArgumentPrivate "
        "*&d)': takes or gives a type that cannot be passed yet: "
        "QDBusArgumentPrivate *&.")

  @staticmethod
  def checkWrite(*__, **_) -> Never:
    """
    Qt's 'bool QDBusArgumentPrivate::checkWrite(QDBusArgumentPrivate *&d)':
    takes or gives a type that cannot be passed yet: QDBusArgumentPrivate *&.
    """
    raise NotImplementedError(
        "'QDBusArgumentPrivate.checkWrite' has no cute function yet. Qt's "
        "'bool QDBusArgumentPrivate::checkWrite(QDBusArgumentPrivate *&d)': "
        "takes or gives a type that cannot be passed yet: "
        "QDBusArgumentPrivate *&.")

  @staticmethod
  def createSignature(*__, **_) -> Never:
    """
    Qt's 'QByteArray QDBusArgumentPrivate::createSignature(QMetaType type)':
    leans on 'qdbus_loadLibDBus()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusArgumentPrivate.createSignature' has no cute function yet. "
        "Qt's 'QByteArray QDBusArgumentPrivate::createSignature(QMetaType "
        "type)': leans on 'qdbus_loadLibDBus()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def d(*__, **_) -> Never:
    """
    Qt's 'QDBusArgumentPrivate *QDBusArgumentPrivate::d(QDBusArgument &q)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDBusArgumentPrivate.d' has no cute function yet. Qt's "
        "'QDBusArgumentPrivate *QDBusArgumentPrivate::d(QDBusArgument &q)': "
        "takes a type Python has no way to hand over yet.")
