"""
QColorTransformPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qcolortransform_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QColorTransformPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QColorTransform, QColorVector
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColorTransform = WAIT['QColorTransform']
  QColorVector = WAIT['QColorVector']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QColorTransformPrivate(QSharedData):
  """
  The cute side of Qt's QColorTransformPrivate: a plain Python object
  standing in front of one C++ QColorTransformPrivate.

  It is built on the cute 'QSharedData', as Qt's QColorTransformPrivate is
  built on Qt's QSharedData, and has everything that class has.

  C++ hands a QColorTransformPrivate around as a copy, so every C++
  QColorTransformPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QColorTransformPrivate that has a ritual and that
  Python can call so far, 3 names in all: 'get', 'prepare', 'pcsAdapt'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QColorTransformPrivate::~QColorTransformPrivate()': the destructor:
    Python removes its C++ QColorTransformPrivate by it, and has no other use
    for it.

  What has no ritual
  ------------------

  8 of the 12 functions Qt declares: 3 a template; 3 leans on
  'QColorSpacePrivate; 2 Qt's library has no name for it, and its code in
  Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QColorTransformPrivate is created at the first use, not by
    'QColorTransformPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QColorTransformPrivate back gives a copy the ritual
    made for Python, in a new cute QColorTransformPrivate.
  - Each name of Qt's QColorTransformPrivate that has no cute function yet,
    'apply', 'applyConvertIn', 'applyConvertOut', 'isIdentity', 'map',
    'mapExtended', 'updateLutsIn', 'updateLutsOut', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QColorTransformPrivate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class TransformFlag(CuteFlags):
    """
    The flags enum 'QColorTransformPrivate::TransformFlag' of Qt, with the 5
    names Qt gives in it. Qt names the type of its combinations
    'QColorTransformPrivate::TransformFlags'.
    """

    Unpremultiplied = 0x0
    InputOpaque = 0x1
    InputPremultiplied = 0x2
    OutputPremultiplied = 0x4
    Premultiplied = 0x6

  TransformFlags = TransformFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QColorTransform)
  def get(q: QColorTransform) -> Optional[QColorTransformPrivate]:
    """
    Calls Qt's 'QColorTransformPrivate *QColorTransformPrivate::get(const
    QColorTransform &q)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortransformprivate.html#get

    Parameters
    ----------

    q : QColorTransform
      Passed on as a value: Qt reads the C++ QColorTransform, which stays
      Python's own.

    Returns
    -------

    Optional[QColorTransformPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QColorTransformPrivate *QColorTransformPrivate::get(const
    #      QColorTransform &q)
    address = Rituals.call(
        'ritual_ZN22QColorTransformPrivate3getERK15QColorTransform',
        CuteMixin._valueOf(q),
    )
    return QColorTransformPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColorTransformPrivate'

  #  Qt's '~QColorTransformPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QColorTransformPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QColorTransformPrivateD1Ev'

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

  def prepare(self) -> None:
    """
    Calls Qt's 'void QColorTransformPrivate::prepare()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransformprivate.html#prepare
    """
    #  void QColorTransformPrivate::prepare()
    self.uglySide.call('ritual_ZN22QColorTransformPrivate7prepareEv')

  @overload(QColorVector, int)
  @overload(NoneType, int)
  def pcsAdapt(self, buffer: Optional[QColorVector], len: int) -> None:
    """
    Calls Qt's 'void QColorTransformPrivate::pcsAdapt(QColorVector *buffer,
    qsizetype len) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransformprivate.html#pcsAdapt

    Parameters
    ----------

    buffer : Optional[QColorVector]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    len : int
      Passed on as it is.
    """
    #  void QColorTransformPrivate::pcsAdapt(QColorVector *buffer, qsizetype
    #      len) const
    self.uglySide.call(
        'ritual_ZNK22QColorTransformPrivate8pcsAdaptEP12QColorVectorx',
        self._addressOf(buffer), len,
    )

  @staticmethod
  def apply(*__, **_) -> Never:
    """
    Qt's 'QColorTransformPrivate::apply': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QColorTransformPrivate.apply' has no cute function yet. Qt's "
        "'QColorTransformPrivate::apply': a template: a pattern and no "
        "single function.")

  @staticmethod
  def applyConvertIn(*__, **_) -> Never:
    """
    Qt's 'QColorTransformPrivate::applyConvertIn': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QColorTransformPrivate.applyConvertIn' has no cute function yet. "
        "Qt's 'QColorTransformPrivate::applyConvertIn': a template: a "
        "pattern and no single function.")

  @staticmethod
  def applyConvertOut(*__, **_) -> Never:
    """
    Qt's 'QColorTransformPrivate::applyConvertOut': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QColorTransformPrivate.applyConvertOut' has no cute function yet. "
        "Qt's 'QColorTransformPrivate::applyConvertOut': a template: a "
        "pattern and no single function.")

  @staticmethod
  def isIdentity(*__, **_) -> Never:
    """
    Qt's 'bool QColorTransformPrivate::isIdentity() const': leans on
    'QColorSpacePrivate::equals(QColorSpacePrivate const*) const', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QColorTransformPrivate.isIdentity' has no cute function yet. Qt's "
        "'bool QColorTransformPrivate::isIdentity() const': leans on "
        "'QColorSpacePrivate::equals(QColorSpacePrivate const*) const', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def map(*__, **_) -> Never:
    """
    Qt's 'QColorVector QColorTransformPrivate::map(QColorVector color)
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'visitElement'.
    """
    raise NotImplementedError(
        "'QColorTransformPrivate.map' has no cute function yet. Qt's "
        "'QColorVector QColorTransformPrivate::map(QColorVector color) "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'visitElement'.")

  @staticmethod
  def mapExtended(*__, **_) -> Never:
    """
    Qt's 'QColorVector QColorTransformPrivate::mapExtended(QColorVector
    color) const': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'visitElement'.
    """
    raise NotImplementedError(
        "'QColorTransformPrivate.mapExtended' has no cute function yet. "
        "Qt's 'QColorVector "
        "QColorTransformPrivate::mapExtended(QColorVector color) const': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'visitElement'.")

  @staticmethod
  def updateLutsIn(*__, **_) -> Never:
    """
    Qt's 'void QColorTransformPrivate::updateLutsIn() const': leans on
    'QColorSpacePrivate::s_lutWriteLock', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QColorTransformPrivate.updateLutsIn' has no cute function yet. "
        "Qt's 'void QColorTransformPrivate::updateLutsIn() const': leans on "
        "'QColorSpacePrivate::s_lutWriteLock', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def updateLutsOut(*__, **_) -> Never:
    """
    Qt's 'void QColorTransformPrivate::updateLutsOut() const': leans on
    'QColorSpacePrivate::s_lutWriteLock', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QColorTransformPrivate.updateLutsOut' has no cute function yet. "
        "Qt's 'void QColorTransformPrivate::updateLutsOut() const': leans "
        "on 'QColorSpacePrivate::s_lutWriteLock', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
