"""
QPngHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpnghandler_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QPngHandler to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QImageIOHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QIODevice, QVariant
  from . import QImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIODevice = WAIT['QIODevice']
  QImage = WAIT['QImage']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPngHandler(QImageIOHandler):
  """
  The cute side of Qt's QPngHandler: a plain Python object standing in front
  of one C++ QPngHandler.

  It is built on the cute 'QImageIOHandler', as Qt's QPngHandler is built on
  Qt's QImageIOHandler, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPngHandler that has a ritual and that Python can
  call so far, 6 names in all: 'canRead', 'read', 'write', 'option',
  'setOption', 'supportsOption'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QPngHandler.

  What to expect
  --------------

  - The C++ QPngHandler is created at the first use, not by
    'QPngHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPngHandler.
  - Each name of Qt's QPngHandler that has no cute function yet, '__init__',
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
  __qt_class__ = 'QPngHandler'

  #  A C++ QPngHandler Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPngHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def canRead(self) -> bool:
    """
    Calls Qt's 'bool QPngHandler::canRead() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpnghandler.html#canRead
    """
    #  bool QPngHandler::canRead() const
    ritual = 'ritual_ZNK11QPngHandler7canReadEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QPngHandler7canReadEv'
    return self.uglySide.call(ritual)

  @staticmethod
  @overload(QIODevice)
  @overload(NoneType)
  def canRead(device: Optional[QIODevice]) -> bool:
    """
    Calls Qt's 'bool QPngHandler::canRead(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qpnghandler.html#canRead

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPngHandler::canRead(QIODevice *device)
    return Rituals.call(
        'ritual_ZN11QPngHandler7canReadEP9QIODevice',
        CuteMixin._addressOf(device),
    )

  @overload(QImageIOHandler.ImageOption)
  def option(self, option: QImageIOHandler.ImageOption) -> QVariant:
    """
    Calls Qt's 'QVariant QPngHandler::option(ImageOption option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpnghandler.html#option

    Parameters
    ----------

    option : QImageIOHandler.ImageOption
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QPngHandler::option(ImageOption option) const
    address = self.uglySide.call(
        'ritual_ZNK11QPngHandler6optionEN15QImageIOHandler11ImageOptionE',
        option.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QImageIOHandler.ImageOption)
  def supportsOption(self, option: QImageIOHandler.ImageOption) -> bool:
    """
    Calls Qt's 'bool QPngHandler::supportsOption(ImageOption option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpnghandler.html#supportsOption

    Parameters
    ----------

    option : QImageIOHandler.ImageOption
      Passed on as its number.
    """
    #  bool QPngHandler::supportsOption(ImageOption option) const
    ritual = (
        'ritual_ZNK11QPngHandler14supportsOptionEN15QImageIOHandler11ImageO'
        'ptionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QPngHandler14supportsOptionEN15QImageIOHandler11'
          'ImageOptionE')
    return self.uglySide.call(ritual, option.value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QImageIOHandler.ImageOption, QVariant)
  def setOption(
      self,
      option: QImageIOHandler.ImageOption,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void QPngHandler::setOption(ImageOption option, const
    QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qpnghandler.html#setOption

    Parameters
    ----------

    option : QImageIOHandler.ImageOption
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QPngHandler::setOption(ImageOption option, const QVariant &value)
    ritual = (
        'ritual_ZN11QPngHandler9setOptionEN15QImageIOHandler11ImageOptionER'
        'K8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QPngHandler9setOptionEN15QImageIOHandler11ImageOp'
          'tionERK8QVariant')
    self.uglySide.call(ritual, option.value, self._valueOf(value))

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
    Qt's 'QPngHandler::QPngHandler()': leans on 'QPngHandler::write(QImage
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QPngHandler.__init__' has no cute function yet. Qt's "
        "'QPngHandler::QPngHandler()': leans on 'QPngHandler::write(QImage "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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
  @overload(NoneType)
  def read(self, image: Optional[QImage]) -> bool:
    """
    Calls Qt's 'bool QPngHandler::read(QImage *image)'.

    Qt's own words: https://doc.qt.io/qt-6/qpnghandler.html#read

    Parameters
    ----------

    image : Optional[QImage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPngHandler::read(QImage *image)
    return self.uglySide.call(
        'ritual_ZN11QPngHandler4readEP6QImage', self._addressOf(image),
    )

  @overload(QImage)
  def write(self, image: QImage) -> bool:
    """
    Calls Qt's 'bool QPngHandler::write(const QImage &image)'.

    Qt's own words: https://doc.qt.io/qt-6/qpnghandler.html#write

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  bool QPngHandler::write(const QImage &image)
    return self.uglySide.call(
        'ritual_ZN11QPngHandler5writeERK6QImage', self._valueOf(image),
    )
