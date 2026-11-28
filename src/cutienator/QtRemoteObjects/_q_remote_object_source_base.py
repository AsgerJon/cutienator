"""
QRemoteObjectSourceBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectsource_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QRemoteObjectSourceBase to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMetaObject, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QVariant
  from . import QRemoteObjectRootSource, QRemoteObjectSourceIo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRemoteObjectSourceBase(QObject):
  """
  The cute side of Qt's QRemoteObjectSourceBase: a plain Python object
  standing in front of one C++ QRemoteObjectSourceBase.

  It is built on the cute 'QObject', as Qt's QRemoteObjectSourceBase is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRemoteObjectSourceBase that has a ritual and that
  Python can call so far, 4 names in all: 'hasAdapter', 'name', 'isRoot',
  'invoke'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRemoteObjectSourceBase::~QRemoteObjectSourceBase()': the
    destructor: Python never removes a C++ QRemoteObjectSourceBase.
  - Qt's 'QVariantList *QRemoteObjectSourceBase::marshalArgs(int index, void
    **a)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 11 functions Qt declares: 2 leans on 'QRemoteObjectPackets; 1 Qt's
  library has no name for it, and its code in Qt's source does not compile
  apart from its file; 1 leans on
  'qRegisterNormalizedMetaType_Qt__Orientation(QByteArray const&)', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken; 1 leans on 'QRemoteObjectSourceIo.

  What to expect
  --------------

  - The C++ QRemoteObjectSourceBase is created at the first use, not by
    'QRemoteObjectSourceBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRemoteObjectSourceBase.
  - Qt tells when it has removed the C++ QRemoteObjectSourceBase. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QRemoteObjectSourceBase that has no cute function yet,
    '__init__', 'handleMetaCall', 'marshalArgs', 'resetObject',
    'setConnections', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The classes Qt writes inside QRemoteObjectSourceBase, each a class in
  #  here as in C++.

  class Private(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRemoteObjectSourceBase::Private: a plain Python
    object standing in front of one C++ QRemoteObjectSourceBase::Private.

    C++ hands a QRemoteObjectSourceBase::Private around as a copy, so every
    C++ QRemoteObjectSourceBase::Private behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QRemoteObjectSourceBase::Private yet. It can be made
    from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRemoteObjectSourceBase::Private::~Private()': the destructor:
      Python removes its C++ QRemoteObjectSourceBase::Private by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QRemoteObjectSourceBase::Private is created at the first use,
      not by 'QRemoteObjectSourceBase::Private(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRemoteObjectSourceBase::Private back gives a copy
      the ritual made for Python, in a new cute
      QRemoteObjectSourceBase::Private.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QRemoteObjectRootSource = WAIT['QRemoteObjectRootSource']
      QRemoteObjectSourceIo = WAIT['QRemoteObjectSourceIo']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRemoteObjectSourceBase::Private'

    #  Qt's '~QRemoteObjectSourceBase::Private()'. Naming it makes this a
    #  value class: Python owns every C++ QRemoteObjectSourceBase::Private
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN23QRemoteObjectSourceBase7PrivateD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QRemoteObjectSourceIo, QRemoteObjectRootSource)
    @overload(QRemoteObjectSourceIo, NoneType)
    @overload(NoneType, QRemoteObjectRootSource)
    @overload(NoneType, NoneType)
    def __init__(
        self,
        io: Optional[QRemoteObjectSourceIo],
        root: Optional[QRemoteObjectRootSource],
    ) -> None:
      """
      Notes what was given, for Qt's
      'QRemoteObjectSourceBase::Private::Private(QRemoteObjectSourceIo *io,
      QRemoteObjectRootSource *root)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qremoteobjectsourcebase-private.html#Private

      Parameters
      ----------

      io : Optional[QRemoteObjectSourceIo]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      root : Optional[QRemoteObjectRootSource]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QRemoteObjectSourceBase::Private::Private(QRemoteObjectSourceIo *io,
      #      QRemoteObjectRootSource *root)
      self._noteCreation(
          QRemoteObjectSourceBase.Private, lambda: Rituals.call(
              'ritual_ZN23QRemoteObjectSourceBase7PrivateC1EP21QRemoteObjec'
              'tSourceIoP23QRemoteObjectRootSource',
              self._addressOf(io), self._addressOf(root),
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRemoteObjectSourceBase'

  #  A C++ QRemoteObjectSourceBase Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRemoteObjectSourceBase'

  #  The functions Qt calls itself that QRemoteObjectSourceBase is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'name': (
          ('_ZNK23QRemoteObjectSourceBase4nameEv',
           ('address', 'text', ''),
           ()),
      ),
      'isRoot': (
          ('_ZNK23QRemoteObjectSourceBase6isRootEv',
           ('bool', 'number', ''),
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

  def hasAdapter(self) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectSourceBase::hasAdapter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectsourcebase.html#hasAdapter
    """
    #  bool QRemoteObjectSourceBase::hasAdapter() const
    return self.uglySide.call(
        'ritual_ZNK23QRemoteObjectSourceBase10hasAdapterEv',
    )

  def name(self) -> str:
    """
    Calls Qt's 'QString QRemoteObjectSourceBase::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjectsourcebase.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QRemoteObjectSourceBase::name() const
    return self.uglySide.call('ritual_ZNK23QRemoteObjectSourceBase4nameEv')

  def isRoot(self) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectSourceBase::isRoot() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectsourcebase.html#isRoot
    """
    #  bool QRemoteObjectSourceBase::isRoot() const
    return self.uglySide.call('ritual_ZNK23QRemoteObjectSourceBase6isRootEv')

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
    Qt's 'QRemoteObjectSourceBase::QRemoteObjectSourceBase(QObject *object,
    Private *d, const SourceApiMap *a2, QObject *adapter)': leans on
    'qRegisterNormalizedMetaType_Qt__Orientation(QByteArray const&)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectSourceBase.__init__' has no cute function yet. Qt's "
        "'QRemoteObjectSourceBase::QRemoteObjectSourceBase(QObject *object, "
        "Private *d, const SourceApiMap *a2, QObject *adapter)': leans on "
        "'qRegisterNormalizedMetaType_Qt__Orientation(QByteArray const&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(QMetaObject.Call, int, QList[QVariant])
  @overload(QMetaObject.Call, int, QList[QVariant], QVariant)
  @overload(QMetaObject.Call, int, QList[QVariant], NoneType)
  def invoke(
      self,
      c: QMetaObject.Call,
      index: int,
      args: QList[QVariant],
      returnValue: Optional[QVariant] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectSourceBase::invoke(QMetaObject::Call c, int
    index, const QVariantList &args, QVariant *returnValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectsourcebase.html#invoke

    Parameters
    ----------

    c : QMetaObject.Call
      Passed on as its number.

    index : int
      Passed on as it is.

    args : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    returnValue : Optional[QVariant]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QRemoteObjectSourceBase::invoke(QMetaObject::Call c, int index,
    #      const QVariantList &args, QVariant *returnValue)
    return self.uglySide.call(
        'ritual_ZN23QRemoteObjectSourceBase6invokeEN11QMetaObject4CallEiRK5'
        'QListI8QVariantEPS3_',
        c.value, index, self._valueOf(args), self._addressOf(returnValue),
    )

  @staticmethod
  def handleMetaCall(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectSourceBase::handleMetaCall(int index,
    QMetaObject::Call call, void **a)': leans on
    'QRemoteObjectPackets::CodecBase::send(QList<QtROIoDeviceBase*> const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectSourceBase.handleMetaCall' has no cute function yet. "
        "Qt's 'void QRemoteObjectSourceBase::handleMetaCall(int index, "
        "QMetaObject::Call call, void **a)': leans on "
        "'QRemoteObjectPackets::CodecBase::send(QList<QtROIoDeviceBase*> "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def marshalArgs(*__, **_) -> Never:
    """
    Qt's 'QVariantList *QRemoteObjectSourceBase::marshalArgs(int index, void
    **a)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectSourceBase.marshalArgs' has no cute function yet. "
        "Qt's 'QVariantList *QRemoteObjectSourceBase::marshalArgs(int "
        "index, void **a)': takes a type Python has no way to hand over yet."
    )

  @staticmethod
  def resetObject(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectSourceBase::resetObject(QObject *newObject)':
    leans on 'QRemoteObjectSourceIo::remoteObjectAdded(std::pair<QString,
    QRemoteObjectSourceLocationInfo> const&)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectSourceBase.resetObject' has no cute function yet. "
        "Qt's 'void QRemoteObjectSourceBase::resetObject(QObject "
        "*newObject)': leans on "
        "'QRemoteObjectSourceIo::remoteObjectAdded(std::pair<QString, "
        "QRemoteObjectSourceLocationInfo> const&)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setConnections(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectSourceBase::setConnections()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'qtro_is_cloned_method'.
    """
    raise NotImplementedError(
        "'QRemoteObjectSourceBase.setConnections' has no cute function yet. "
        "Qt's 'void QRemoteObjectSourceBase::setConnections()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'qtro_is_cloned_method'.")
