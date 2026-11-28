"""
QPlatformVideoDevices binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qplatformvideodevices_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QPlatformVideoDevices to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QCameraDevice

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformVideoDevices(QObject):
  """
  The cute side of Qt's QPlatformVideoDevices: a plain Python object standing
  in front of one C++ QPlatformVideoDevices.

  It is built on the cute 'QObject', as Qt's QPlatformVideoDevices is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformVideoDevices that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr', 'videoInputs',
  'findVideoInputs', 'onVideoInputsChanged', 'updateVideoInputsCache'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformVideoDevices::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QPlatformVideoDevices::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QPlatformVideoDevices::~QPlatformVideoDevices()': the destructor:
    Python never removes a C++ QPlatformVideoDevices.
  - Qt's 'void QPlatformVideoDevices::videoInputsChanged(PrivateTag a0)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 13 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QPlatformVideoDevices is created at the first use, not by
    'QPlatformVideoDevices(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformVideoDevices.
  - Qt tells when it has removed the C++ QPlatformVideoDevices. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlatformVideoDevices that has no cute function yet,
    '__init__', 'videoInputsChanged', holds a function that raises
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
    Calls Qt's 'QString QPlatformVideoDevices::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformvideodevices.html#tr

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
    #  QString QPlatformVideoDevices::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QPlatformVideoDevices2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformVideoDevices'

  #  A C++ QPlatformVideoDevices Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformVideoDevices'

  #  The functions Qt calls itself that QPlatformVideoDevices is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'findVideoInputs': (
          'QList<QCameraDevice> QPlatformVideoDevices::findVideoInputs() '
          'const',
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
    Calls Qt's 'const QMetaObject *QPlatformVideoDevices::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideodevices.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformVideoDevices::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QPlatformVideoDevices10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def videoInputs(self) -> QList[QCameraDevice]:
    """
    Calls Qt's 'QList<QCameraDevice> QPlatformVideoDevices::videoInputs()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideodevices.html#videoInputs

    Returns
    -------

    QList[QCameraDevice]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCameraDevice> QPlatformVideoDevices::videoInputs() const
    address = self.uglySide.call(
        'ritual_ZNK21QPlatformVideoDevices11videoInputsEv',
    )
    from . import QCameraDevice
    return QList[QCameraDevice]._cuteOwning(address)

  def findVideoInputs(self) -> QList[QCameraDevice]:
    """
    Calls Qt's 'QList<QCameraDevice> QPlatformVideoDevices::findVideoInputs()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideodevices.html#findVideoInputs

    Returns
    -------

    QList[QCameraDevice]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCameraDevice> QPlatformVideoDevices::findVideoInputs() const
    address = self.uglySide.call(
        'ritual_ZNK21QPlatformVideoDevices15findVideoInputsEv',
    )
    from . import QCameraDevice
    return QList[QCameraDevice]._cuteOwning(address)

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
    'QPlatformVideoDevices::QPlatformVideoDevices(QPlatformMediaIntegration
    *integration)': the class is abstract, so C++ cannot make one, and the
    C++ class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QPlatformVideoDevices.__init__' has no cute function yet. Qt's "
        "'QPlatformVideoDevices::QPlatformVideoDevices(QPlatformMediaIntegra"
        "tion *integration)': the class is abstract, so C++ cannot make "
        "one, and the C++ class of ours does not fill in every function it "
        "leaves open.")

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

  def onVideoInputsChanged(self) -> None:
    """
    Calls Qt's 'void QPlatformVideoDevices::onVideoInputsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideodevices.html#onVideoInputsChanged
    """
    #  void QPlatformVideoDevices::onVideoInputsChanged()
    self.uglySide.call(
        'ritual_ZN21QPlatformVideoDevices20onVideoInputsChangedEv',
    )

  def updateVideoInputsCache(self) -> None:
    """
    Calls Qt's 'void QPlatformVideoDevices::updateVideoInputsCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideodevices.html#updateVideoInputsCache
    """
    #  void QPlatformVideoDevices::updateVideoInputsCache()
    self.uglySide.call(
        'ritual_ZN21QPlatformVideoDevices22updateVideoInputsCacheEv',
    )

  @staticmethod
  def videoInputsChanged(*__, **_) -> Never:
    """
    Qt's 'void QPlatformVideoDevices::videoInputsChanged(PrivateTag a0)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformVideoDevices.videoInputsChanged' has no cute function "
        "yet. Qt's 'void "
        "QPlatformVideoDevices::videoInputsChanged(PrivateTag a0)': takes a "
        "type Python has no way to hand over yet.")
