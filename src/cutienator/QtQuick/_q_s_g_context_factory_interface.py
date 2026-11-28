"""
QSGContextFactoryInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgcontextplugin_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGContextFactoryInterface to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteFlags, WAIT
from ..QtCore import QFactoryInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QImage
  from . import QQuickTextureFactory, QSGContext, QSGRenderLoop
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']


class QSGContextFactoryInterface(QFactoryInterface):
  """
  The cute side of Qt's QSGContextFactoryInterface: a plain Python object
  standing in front of one C++ QSGContextFactoryInterface.

  It is built on the cute 'QFactoryInterface', as Qt's
  QSGContextFactoryInterface is built on Qt's QFactoryInterface, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSGContextFactoryInterface that has a ritual and
  that Python can call so far, 4 names in all: 'create', 'flags',
  'createTextureFactoryFromImage', 'createWindowManager'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What to expect
  --------------

  - The C++ QSGContextFactoryInterface is created at the first use, not by
    'QSGContextFactoryInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGContextFactoryInterface.
  """

  #  The enums Qt writes inside QSGContextFactoryInterface, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QSGContextFactoryInterface::Flag' of Qt, with the 1 names
    Qt gives in it. Qt names the type of its combinations
    'QSGContextFactoryInterface::Flags'.
    """

    SupportsShaderEffectNode = 0x1

  Flags = Flag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGContextFactoryInterface'

  #  A C++ QSGContextFactoryInterface Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGContextFactoryInterface'

  #  The functions Qt calls itself that QSGContextFactoryInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'create': (
          ('_ZNK26QSGContextFactoryInterface6createERK7QString',
           ('address', 'address', 'QtQuick:QSGContext'),
           (
               ('address', 'text', ''),
           )),
      ),
      'flags': (
          ('_ZNK26QSGContextFactoryInterface5flagsERK7QString',
           ('int', 'flags', 'QtQuick:QSGContextFactoryInterface.Flag'),
           (
               ('address', 'text', ''),
           )),
      ),
      'createTextureFactoryFromImage': (
          ('_ZN26QSGContextFactoryInterface29createTextureFactoryFromImageE'
           'RK6QImage',
           ('address', 'address', 'QtQuick:QQuickTextureFactory'),
           (
               ('address', 'value', 'QtGui:QImage'),
           )),
      ),
      'createWindowManager': (
          ('_ZN26QSGContextFactoryInterface19createWindowManagerEv',
           ('address', 'address', 'QtQuick:QSGRenderLoop'),
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

  @overload(str)
  def create(self, key: str) -> Optional[QSGContext]:
    """
    Calls Qt's 'QSGContext *QSGContextFactoryInterface::create(const QString
    &key) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontextfactoryinterface.html#create

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QSGContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGContext *QSGContextFactoryInterface::create(const QString &key)
    #      const
    address = self._callAs(
        'QSGContextFactoryInterface',
        'ritual_ZNK26QSGContextFactoryInterface6createERK7QString',
        key,
    )
    from . import QSGContext
    return QSGContext._cuteAt(address)

  @overload(str)
  def flags(self, key: str) -> Flags:
    """
    Calls Qt's 'Flags QSGContextFactoryInterface::flags(const QString &key)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontextfactoryinterface.html#flags

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QSGContextFactoryInterface::flags(const QString &key) const
    return QSGContextFactoryInterface.Flags(self._callAs(
        'QSGContextFactoryInterface',
        'ritual_ZNK26QSGContextFactoryInterface5flagsERK7QString',
        key,
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

  @overload(QImage)
  def createTextureFactoryFromImage(
      self,
      image: QImage,
  ) -> Optional[QQuickTextureFactory]:
    """
    Calls Qt's 'QQuickTextureFactory
    *QSGContextFactoryInterface::createTextureFactoryFromImage(const QImage
    &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontextfactoryinterface.html

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    Returns
    -------

    Optional[QQuickTextureFactory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextureFactory
    #      *QSGContextFactoryInterface::createTextureFactoryFromImage(const
    #      QImage &image)
    address = self._callAs(
        'QSGContextFactoryInterface',
        'ritual_ZN26QSGContextFactoryInterface29createTextureFactoryFromIma'
        'geERK6QImage',
        self._valueOf(image),
    )
    from . import QQuickTextureFactory
    return QQuickTextureFactory._cuteAt(address)

  def createWindowManager(self) -> Optional[QSGRenderLoop]:
    """
    Calls Qt's 'QSGRenderLoop
    *QSGContextFactoryInterface::createWindowManager()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcontextfactoryinterface.html

    Returns
    -------

    Optional[QSGRenderLoop]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRenderLoop *QSGContextFactoryInterface::createWindowManager()
    address = self._callAs(
        'QSGContextFactoryInterface',
        'ritual_ZN26QSGContextFactoryInterface19createWindowManagerEv',
    )
    from . import QSGRenderLoop
    return QSGRenderLoop._cuteAt(address)
