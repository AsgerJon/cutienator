"""
QQmlPropertyCapture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljavascriptexpression_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlPropertyCapture to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlJavaScriptExpression

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QObject
  from . import QQmlEngine, QQmlNotifier, QQmlPropertyCache, QQmlPropertyData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']
  QObject = WAIT['QObject']
  QQmlEngine = WAIT['QQmlEngine']
  QQmlNotifier = WAIT['QQmlNotifier']
  QQmlPropertyCache = WAIT['QQmlPropertyCache']
  QQmlPropertyData = WAIT['QQmlPropertyData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlPropertyCapture(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlPropertyCapture: a plain Python object standing
  in front of one C++ QQmlPropertyCapture.

  C++ hands a QQmlPropertyCapture around as a copy, so every C++
  QQmlPropertyCapture behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlPropertyCapture that has a ritual and that
  Python can call so far, 4 names in all: 'captureProperty',
  'captureTranslation', 'captureBindableProperty',
  'captureNonBindableProperty'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlPropertyCapture::~QQmlPropertyCapture()': the destructor:
    Python removes its C++ QQmlPropertyCapture by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQmlPropertyCapture is created at the first use, not by
    'QQmlPropertyCapture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlPropertyCapture back gives a copy the ritual made
    for Python, in a new cute QQmlPropertyCapture.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlPropertyCapture'

  #  Qt's '~QQmlPropertyCapture()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlPropertyCapture behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QQmlPropertyCaptureD1Ev'

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

  @overload(
      QQmlEngine, QQmlJavaScriptExpression,
      QQmlJavaScriptExpression.DeleteWatcher,
  )
  @overload(QQmlEngine, QQmlJavaScriptExpression, NoneType)
  @overload(QQmlEngine, NoneType, QQmlJavaScriptExpression.DeleteWatcher)
  @overload(QQmlEngine, NoneType, NoneType)
  @overload(
      NoneType, QQmlJavaScriptExpression,
      QQmlJavaScriptExpression.DeleteWatcher,
  )
  @overload(NoneType, QQmlJavaScriptExpression, NoneType)
  @overload(NoneType, NoneType, QQmlJavaScriptExpression.DeleteWatcher)
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      engine: Optional[QQmlEngine],
      e: Optional[QQmlJavaScriptExpression],
      w: Optional[QQmlJavaScriptExpression.DeleteWatcher],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlPropertyCapture::QQmlPropertyCapture(QQmlEngine *engine,
    QQmlJavaScriptExpression *e, QQmlJavaScriptExpression::DeleteWatcher
    *w)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycapture.html#QQmlPropertyCapture

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    e : Optional[QQmlJavaScriptExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    w : Optional[QQmlJavaScriptExpression.DeleteWatcher]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlPropertyCapture::QQmlPropertyCapture(QQmlEngine *engine,
    #      QQmlJavaScriptExpression *e,
    #      QQmlJavaScriptExpression::DeleteWatcher *w)
    self._noteCreation(QQmlPropertyCapture, lambda: Rituals.call(
        'ritual_ZN19QQmlPropertyCaptureC1EP10QQmlEngineP24QQmlJavaScriptExp'
        'ressionPNS2_13DeleteWatcherE',
        self._addressOf(engine), self._addressOf(e,
        'QQmlJavaScriptExpression'), self._addressOf(w),
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

  @overload(QQmlNotifier)
  @overload(NoneType)
  def captureProperty(self, a0: Optional[QQmlNotifier]) -> None:
    """
    Calls Qt's 'void QQmlPropertyCapture::captureProperty(QQmlNotifier *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycapture.html#captureProperty

    Parameters
    ----------

    a0 : Optional[QQmlNotifier]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPropertyCapture::captureProperty(QQmlNotifier *a0)
    self.uglySide.call(
        'ritual_ZN19QQmlPropertyCapture15capturePropertyEP12QQmlNotifier',
        self._addressOf(a0),
    )

  @overload(QObject, int, int)
  @overload(NoneType, int, int)
  @overload(QObject, int, int, bool)
  @overload(NoneType, int, int, bool)
  def captureProperty(
      self,
      a0: Optional[QObject],
      a1: int,
      a2: int,
      doNotify: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QQmlPropertyCapture::captureProperty(QObject *a0, int
    a1, int a2, bool doNotify)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycapture.html#captureProperty

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : int
      Passed on as it is.

    a2 : int
      Passed on as it is.

    doNotify : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQmlPropertyCapture::captureProperty(QObject *a0, int a1, int a2,
    #      bool doNotify)
    self.uglySide.call(
        'ritual_ZN19QQmlPropertyCapture15capturePropertyEP7QObjectiib',
        self._addressOf(a0, 'QObject'), a1, a2, doNotify,
    )

  @overload(QObject, QQmlPropertyCache, QQmlPropertyData)
  @overload(QObject, QQmlPropertyCache, NoneType)
  @overload(QObject, NoneType, QQmlPropertyData)
  @overload(QObject, NoneType, NoneType)
  @overload(NoneType, QQmlPropertyCache, QQmlPropertyData)
  @overload(NoneType, QQmlPropertyCache, NoneType)
  @overload(NoneType, NoneType, QQmlPropertyData)
  @overload(NoneType, NoneType, NoneType)
  @overload(QObject, QQmlPropertyCache, QQmlPropertyData, bool)
  @overload(QObject, QQmlPropertyCache, NoneType, bool)
  @overload(QObject, NoneType, QQmlPropertyData, bool)
  @overload(QObject, NoneType, NoneType, bool)
  @overload(NoneType, QQmlPropertyCache, QQmlPropertyData, bool)
  @overload(NoneType, QQmlPropertyCache, NoneType, bool)
  @overload(NoneType, NoneType, QQmlPropertyData, bool)
  @overload(NoneType, NoneType, NoneType, bool)
  def captureProperty(
      self,
      a0: Optional[QObject],
      a1: Optional[QQmlPropertyCache],
      a2: Optional[QQmlPropertyData],
      doNotify: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QQmlPropertyCapture::captureProperty(QObject *a0, const
    QQmlPropertyCache *a1, const QQmlPropertyData *a2, bool doNotify)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycapture.html#captureProperty

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQmlPropertyCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a2 : Optional[QQmlPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    doNotify : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQmlPropertyCapture::captureProperty(QObject *a0, const
    #      QQmlPropertyCache *a1, const QQmlPropertyData *a2, bool doNotify)
    self.uglySide.call(
        'ritual_ZN19QQmlPropertyCapture15capturePropertyEP7QObjectPK17QQmlP'
        'ropertyCachePK16QQmlPropertyDatab',
        self._addressOf(a0, 'QObject'), self._addressOf(a1),
        self._addressOf(a2), doNotify,
    )

  def captureTranslation(self) -> None:
    """
    Calls Qt's 'void QQmlPropertyCapture::captureTranslation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycapture.html#captureTranslation
    """
    #  void QQmlPropertyCapture::captureTranslation()
    self.uglySide.call(
        'ritual_ZN19QQmlPropertyCapture18captureTranslationEv',
    )

  @overload(QObject, QMetaObject, int)
  @overload(QObject, NoneType, int)
  @overload(NoneType, QMetaObject, int)
  @overload(NoneType, NoneType, int)
  def captureBindableProperty(
      self,
      o: Optional[QObject],
      metaObjectForBindable: Optional[QMetaObject],
      c: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlPropertyCapture::captureBindableProperty(QObject *o,
    const QMetaObject *metaObjectForBindable, int c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycapture.html#captureBindableProperty

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    metaObjectForBindable : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    c : int
      Passed on as it is.
    """
    #  void QQmlPropertyCapture::captureBindableProperty(QObject *o, const
    #      QMetaObject *metaObjectForBindable, int c)
    self.uglySide.call(
        'ritual_ZN19QQmlPropertyCapture23captureBindablePropertyEP7QObjectP'
        'K11QMetaObjecti',
        self._addressOf(o, 'QObject'), self._addressOf(metaObjectForBindable,
        'QMetaObject'), c,
    )

  @overload(QObject, int, int, bool)
  @overload(NoneType, int, int, bool)
  def captureNonBindableProperty(
      self,
      o: Optional[QObject],
      n: int,
      c: int,
      doNotify: bool,
  ) -> None:
    """
    Calls Qt's 'void QQmlPropertyCapture::captureNonBindableProperty(QObject
    *o, int n, int c, bool doNotify)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycapture.html

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    n : int
      Passed on as it is.

    c : int
      Passed on as it is.

    doNotify : bool
      Passed on as it is.
    """
    #  void QQmlPropertyCapture::captureNonBindableProperty(QObject *o, int
    #      n, int c, bool doNotify)
    self.uglySide.call(
        'ritual_ZN19QQmlPropertyCapture26captureNonBindablePropertyEP7QObje'
        'ctiib',
        self._addressOf(o, 'QObject'), n, c, doNotify,
    )
