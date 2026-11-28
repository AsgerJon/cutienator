"""
QPlaceSearchReplyUnsupported binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/unsupportedreplies_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QPlaceSearchReplyUnsupported to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QPlaceReply, QPlaceSearchReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QPlaceManagerEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlaceManagerEngine = WAIT['QPlaceManagerEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlaceSearchReplyUnsupported(QPlaceSearchReply):
  """
  The cute side of Qt's QPlaceSearchReplyUnsupported: a plain Python object
  standing in front of one C++ QPlaceSearchReplyUnsupported.

  It is built on the cute 'QPlaceSearchReply', as Qt's
  QPlaceSearchReplyUnsupported is built on Qt's QPlaceSearchReply, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QPlaceSearchReplyUnsupported that has a ritual and
  that Python can call so far, 2 names in all: 'metaObject', 'tr'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlaceSearchReplyUnsupported::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QPlaceSearchReplyUnsupported::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPlaceSearchReplyUnsupported is created at the first use, not by
    'QPlaceSearchReplyUnsupported(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlaceSearchReplyUnsupported.
  - Qt tells when it has removed the C++ QPlaceSearchReplyUnsupported. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QPlaceSearchReplyUnsupported::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchreplyunsupported.html#tr

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
    #  QString QPlaceSearchReplyUnsupported::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QPlaceSearchReplyUnsupported2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaceSearchReplyUnsupported'

  #  A C++ QPlaceSearchReplyUnsupported Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlaceSearchReplyUnsupported'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPlaceSearchReplyUnsupported::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchreplyunsupported.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlaceSearchReplyUnsupported::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QPlaceSearchReplyUnsupported10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(QPlaceReply.Error, str, QPlaceManagerEngine)
  @overload(QPlaceReply.Error, str, NoneType)
  def __init__(
      self,
      errorCode: QPlaceReply.Error,
      message: str,
      parent: Optional[QPlaceManagerEngine],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QPlaceSearchReplyUnsupported::QPlaceSearchReplyUnsupported(
    QPlaceReply::Error errorCode, const QString &message, QPlaceManagerEngine
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchreplyunsupported.html

    Parameters
    ----------

    errorCode : QPlaceReply.Error
      Passed on as its number.

    message : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QPlaceManagerEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPlaceSearchReplyUnsupported::QPlaceSearchReplyUnsupported(
    #      QPlaceReply::Error errorCode, const QString &message,
    #      QPlaceManagerEngine *parent)
    self._noteCreation(QPlaceSearchReplyUnsupported, lambda: Rituals.call(
        'ritual_ZN28QPlaceSearchReplyUnsupportedC1EN11QPlaceReply5ErrorERK7'
        'QStringP19QPlaceManagerEngine',
        errorCode.value, message, self._addressOf(parent),
    ))

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
