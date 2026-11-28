"""
QXpmHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qxpmhandler_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QXpmHandler to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QImageIOHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QVariant
  from . import QImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QXpmHandler(QImageIOHandler):
  """
  The cute side of Qt's QXpmHandler: a plain Python object standing in front
  of one C++ QXpmHandler.

  It is built on the cute 'QImageIOHandler', as Qt's QXpmHandler is built on
  Qt's QImageIOHandler, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QXpmHandler that has a ritual and that Python can
  call so far, 6 names in all: 'canRead', 'read', 'write', 'option',
  'setOption', 'supportsOption'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 4 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QXpmHandler is created at the first use, not by
    'QXpmHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QXpmHandler.
  - Each name of Qt's QXpmHandler that has no cute function yet, '__init__',
    'readHeader', 'readImage', holds a function that raises
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
  __qt_class__ = 'QXpmHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def canRead(self) -> bool:
    """
    Calls Qt's 'bool QXpmHandler::canRead() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxpmhandler.html#canRead
    """
    #  bool QXpmHandler::canRead() const
    return self.uglySide.call('ritual_ZNK11QXpmHandler7canReadEv')

  @overload(QImageIOHandler.ImageOption)
  def option(self, option: QImageIOHandler.ImageOption) -> QVariant:
    """
    Calls Qt's 'QVariant QXpmHandler::option(ImageOption option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxpmhandler.html#option

    Parameters
    ----------

    option : QImageIOHandler.ImageOption
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QXpmHandler::option(ImageOption option) const
    address = self.uglySide.call(
        'ritual_ZNK11QXpmHandler6optionEN15QImageIOHandler11ImageOptionE',
        option.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QImageIOHandler.ImageOption)
  def supportsOption(self, option: QImageIOHandler.ImageOption) -> bool:
    """
    Calls Qt's 'bool QXpmHandler::supportsOption(ImageOption option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxpmhandler.html#supportsOption

    Parameters
    ----------

    option : QImageIOHandler.ImageOption
      Passed on as its number.
    """
    #  bool QXpmHandler::supportsOption(ImageOption option) const
    return self.uglySide.call(
        'ritual_ZNK11QXpmHandler14supportsOptionEN15QImageIOHandler11ImageO'
        'ptionE',
        option.value,
    )

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
    Calls Qt's 'void QXpmHandler::setOption(ImageOption option, const
    QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qxpmhandler.html#setOption

    Parameters
    ----------

    option : QImageIOHandler.ImageOption
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QXpmHandler::setOption(ImageOption option, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN11QXpmHandler9setOptionEN15QImageIOHandler11ImageOptionER'
        'K8QVariant',
        option.value, self._valueOf(value),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QXpmHandler::QXpmHandler()': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: expected
    ')'.
    """
    raise NotImplementedError(
        "'QXpmHandler.__init__' has no cute function yet. Qt's "
        "'QXpmHandler::QXpmHandler()': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "expected ')'.")

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
    Calls Qt's 'bool QXpmHandler::read(QImage *image)'.

    Qt's own words: https://doc.qt.io/qt-6/qxpmhandler.html#read

    Parameters
    ----------

    image : Optional[QImage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QXpmHandler::read(QImage *image)
    return self.uglySide.call(
        'ritual_ZN11QXpmHandler4readEP6QImage', self._addressOf(image),
    )

  @overload(QImage)
  def write(self, image: QImage) -> bool:
    """
    Calls Qt's 'bool QXpmHandler::write(const QImage &image)'.

    Qt's own words: https://doc.qt.io/qt-6/qxpmhandler.html#write

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  bool QXpmHandler::write(const QImage &image)
    return self.uglySide.call(
        'ritual_ZN11QXpmHandler5writeERK6QImage', self._valueOf(image),
    )

  @staticmethod
  def readHeader(*__, **_) -> Never:
    """
    Qt's 'bool QXpmHandler::readHeader()': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file:
    expected ')'.
    """
    raise NotImplementedError(
        "'QXpmHandler.readHeader' has no cute function yet. Qt's 'bool "
        "QXpmHandler::readHeader()': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "expected ')'.")

  @staticmethod
  def readImage(*__, **_) -> Never:
    """
    Qt's 'bool QXpmHandler::readImage(QImage *image)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'read_xpm_body'.
    """
    raise NotImplementedError(
        "'QXpmHandler.readImage' has no cute function yet. Qt's 'bool "
        "QXpmHandler::readImage(QImage *image)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'read_xpm_body'.")
