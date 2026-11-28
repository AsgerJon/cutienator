"""
QV4::Heap::UrlObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4urlobject_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::Heap::UrlObject to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class UrlObject(QV4.Heap.Object, QV4.Heap.UrlObjectData):
  """
  The cute side of Qt's QV4::Heap::UrlObject: a plain Python object standing
  in front of one C++ QV4::Heap::UrlObject.

  It is built on the cute 'QV4::Heap::Object', as Qt's QV4::Heap::UrlObject
  is built on Qt's QV4::Heap::Object, and has everything that class has. It
  is built on the cute 'QV4::Heap::UrlObjectData' as well, as Qt's
  QV4::Heap::UrlObject is built on Qt's QV4::Heap::UrlObjectData too, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::UrlObject that has a ritual and that
  Python can call so far, 4 names in all: 'markObjects', 'init', 'destroy',
  'url'. None can be made from Python: one comes out of a function of another
  class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QV4::Heap::UrlObject::setUrl(QUrl &&url)': takes a type Python
    has no way to hand over yet.

  What to expect
  --------------

  - The C++ QV4::Heap::UrlObject is created at the first use, not by
    'QV4::Heap::UrlObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::UrlObject.
  - Each name of Qt's QV4::Heap::UrlObject that has no cute function yet,
    'setUrl', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QV4.Heap.Base, WAIT['QV4.MarkStack'])
  @overload(QV4.Heap.Base, NoneType)
  @overload(NoneType, WAIT['QV4.MarkStack'])
  @overload(NoneType, NoneType)
  def markObjects(
      b: Optional[QV4.Heap.Base],
      stack: Optional[QV4.MarkStack],
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::UrlObject::markObjects(Heap::Base *b,
    MarkStack *stack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-urlobject.html#markObjects

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::UrlObject::markObjects(Heap::Base *b, MarkStack
    #      *stack)
    Rituals.call(
        'ritual_ZN3QV44Heap9UrlObject11markObjectsEPNS0_4BaseEPNS_9MarkStac'
        'kE',
        CuteMixin._addressOf(b), CuteMixin._addressOf(stack),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::UrlObject'

  #  Qt's QV4::Heap::UrlObject is built on more than one class. The part of a
  #  C++ QV4::Heap::UrlObject that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QV4::Heap::UrlObjectData':
          'ritual_cast_QV4_Heap_UrlObject_QV4_Heap_UrlObjectData',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QV4::Heap::UrlObject::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-urlobject.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QV4::Heap::UrlObject::url() const
    address = self.uglySide.call('ritual_ZNK3QV44Heap9UrlObject3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

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

  @overload()
  def init(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::UrlObject::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-urlobject.html#init
    """
    #  void QV4::Heap::UrlObject::init()
    self.uglySide.call('ritual_ZN3QV44Heap9UrlObject4initEv')

  @overload(QUrl)
  def init(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QV4::Heap::UrlObject::init(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-urlobject.html#init

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QV4::Heap::UrlObject::init(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN3QV44Heap9UrlObject4initERK4QUrl', self._valueOf(url),
    )

  def destroy(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::UrlObject::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-urlobject.html#destroy
    """
    #  void QV4::Heap::UrlObject::destroy()
    self.uglySide.call('ritual_ZN3QV44Heap9UrlObject7destroyEv')

  @staticmethod
  def setUrl(*__, **_) -> Never:
    """
    Qt's 'void QV4::Heap::UrlObject::setUrl(QUrl &&url)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.Heap.UrlObject.setUrl' has no cute function yet. Qt's 'void "
        "QV4::Heap::UrlObject::setUrl(QUrl &&url)': takes a type Python has "
        "no way to hand over yet.")
