"""
QImageIOPlugin binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qimageiohandler.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QIODevice, QMetaObject
  from . import QImageIOHandler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QImageIOPlugin(QObject):
  """
  The cute side of Qt's QImageIOPlugin: a plain Python object standing in
  front of one C++ QImageIOPlugin.

  It is built on the cute 'QObject', as Qt's QImageIOPlugin is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QImageIOPlugin that has a ritual and that Python can
  call so far, 4 names in all: 'metaObject', 'tr', 'capabilities', 'create'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QImageIOPlugin::~QImageIOPlugin()': the destructor: Python never
    removes a C++ QImageIOPlugin.

  What has no ritual
  ------------------

  5 of the 10 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 1 a template; 1 private; 1 the class is abstract, so C++ cannot
  make one.

  What to expect
  --------------

  - The C++ QImageIOPlugin is created at the first use, not by
    'QImageIOPlugin(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QImageIOPlugin.
  - Qt tells when it has removed the C++ QImageIOPlugin. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QImageIOPlugin, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Capability(CuteFlags):
    """
    The flags enum 'QImageIOPlugin::Capability' of Qt, with the 3 names Qt
    gives in it. Qt names the type of its combinations
    'QImageIOPlugin::Capabilities'.
    """

    CanRead = 0x1
    CanWrite = 0x2
    CanReadIncremental = 0x4

  Capabilities = Capability

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
    Calls Qt's 'QString QImageIOPlugin::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qimageioplugin.html#tr

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
    #  QString QImageIOPlugin::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QImageIOPlugin2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QImageIOPlugin'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QImageIOPlugin::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qimageioplugin.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QImageIOPlugin::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QImageIOPlugin10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QIODevice, QByteArray)
  @overload(NoneType, QByteArray)
  def capabilities(
      self,
      device: Optional[QIODevice],
      format: QByteArray,
  ) -> Capabilities:
    """
    Calls Qt's 'Capabilities QImageIOPlugin::capabilities(QIODevice *device,
    const QByteArray &format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimageioplugin.html#capabilities

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    format : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    Capabilities
      The value standing for the combination Qt gave back.
    """
    #  Capabilities QImageIOPlugin::capabilities(QIODevice *device, const
    #      QByteArray &format) const
    return QImageIOPlugin.Capabilities(self.uglySide.call(
        'ritual_ZNK14QImageIOPlugin12capabilitiesEP9QIODeviceRK10QByteArray',
        self._addressOf(device), self._valueOf(format),
    ))

  @overload(QIODevice)
  @overload(NoneType)
  @overload(QIODevice, QByteArray)
  @overload(NoneType, QByteArray)
  def create(
      self,
      device: Optional[QIODevice],
      format: Optional[QByteArray] = None,
  ) -> Optional[QImageIOHandler]:
    """
    Calls Qt's 'QImageIOHandler *QImageIOPlugin::create(QIODevice *device,
    const QByteArray &format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qimageioplugin.html#create

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    format : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    Returns
    -------

    Optional[QImageIOHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QImageIOHandler *QImageIOPlugin::create(QIODevice *device, const
    #      QByteArray &format) const
    if format is None:
      from ..QtCore import QByteArray
      format = QByteArray()
    address = self.uglySide.call(
        'ritual_ZNK14QImageIOPlugin6createEP9QIODeviceRK10QByteArray',
        self._addressOf(device), self._valueOf(format),
    )
    from . import QImageIOHandler
    return QImageIOHandler._cuteAt(address)

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
