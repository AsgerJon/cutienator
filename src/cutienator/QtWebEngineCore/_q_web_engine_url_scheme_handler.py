"""
QWebEngineUrlSchemeHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebengineurlschemehandler.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QWebEngineUrlRequestJob
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWebEngineUrlRequestJob = WAIT['QWebEngineUrlRequestJob']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineUrlSchemeHandler(QObject):
  """
  The cute side of Qt's QWebEngineUrlSchemeHandler: a plain Python object
  standing in front of one C++ QWebEngineUrlSchemeHandler.

  It is built on the cute 'QObject', as Qt's QWebEngineUrlSchemeHandler is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebEngineUrlSchemeHandler that has a ritual and
  that Python can call so far, 3 names in all: 'metaObject', 'tr',
  'requestStarted'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebEngineUrlSchemeHandler::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QWebEngineUrlSchemeHandler::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWebEngineUrlSchemeHandler::~QWebEngineUrlSchemeHandler()': the
    destructor: Python never removes a C++ QWebEngineUrlSchemeHandler.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QWebEngineUrlSchemeHandler is created at the first use, not by
    'QWebEngineUrlSchemeHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineUrlSchemeHandler.
  - Qt tells when it has removed the C++ QWebEngineUrlSchemeHandler. Every
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
    Calls Qt's 'QString QWebEngineUrlSchemeHandler::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineurlschemehandler.html#tr

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
    #  QString QWebEngineUrlSchemeHandler::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QWebEngineUrlSchemeHandler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineUrlSchemeHandler'

  #  A C++ QWebEngineUrlSchemeHandler Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebEngineUrlSchemeHandler'

  #  The functions Qt calls itself that QWebEngineUrlSchemeHandler is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'requestStarted': (
          ('_ZN26QWebEngineUrlSchemeHandler14requestStartedEP23QWebEngineUr'
           'lRequestJob',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtWebEngineCore:QWebEngineUrlRequestJob'),
           )),
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
    Calls Qt's 'const QMetaObject *QWebEngineUrlSchemeHandler::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlschemehandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebEngineUrlSchemeHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QWebEngineUrlSchemeHandler10metaObjectEv',
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineUrlSchemeHandler::QWebEngineUrlSchemeHandler(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlschemehandler.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWebEngineUrlSchemeHandler::QWebEngineUrlSchemeHandler(QObject
    #      *parent)
    self._noteCreation(QWebEngineUrlSchemeHandler, lambda: Rituals.call(
        'ritual_ZN26QWebEngineUrlSchemeHandlerC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QWebEngineUrlRequestJob)
  @overload(NoneType)
  def requestStarted(self, a0: Optional[QWebEngineUrlRequestJob]) -> None:
    """
    Calls Qt's 'void
    QWebEngineUrlSchemeHandler::requestStarted(QWebEngineUrlRequestJob *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlschemehandler.html#requestStarted

    Parameters
    ----------

    a0 : Optional[QWebEngineUrlRequestJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QWebEngineUrlSchemeHandler::requestStarted(QWebEngineUrlRequestJob
    #      *a0)
    self.uglySide.call(
        'ritual_ZN26QWebEngineUrlSchemeHandler14requestStartedEP23QWebEngin'
        'eUrlRequestJob',
        self._addressOf(a0),
    )
