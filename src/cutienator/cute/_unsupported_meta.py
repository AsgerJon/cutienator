"""
UnsupportedMeta makes the classes that stand in a cute class at the
names of functions of Qt that have no cute function yet.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class UnsupportedMeta(type):
  """
  The metaclass of a class that stands in a cute class at the name of a
  function of Qt that has no cute function yet, as 'nativeEvent' in the
  body of 'QWidget'. Its docstring names each function of Qt at that
  name, as Qt declares it, and says why it has none:

    class nativeEvent(metaclass=UnsupportedMeta):
      \"\"\"
      Qt's 'bool QWidget::nativeEvent(const QByteArray &eventType, void
      *message, qintptr *result)': names 'void', which has no cute
      class yet.
      \"\"\"

    QWidget.nativeEvent(...)   # NotImplementedError
    widget.nativeEvent(...)    # NotImplementedError
    QWidget.nativeEvent.oops   # NotImplementedError

  You never use it by name: the dev tooling writes such classes into
  the files of the cute classes. A function of Qt that gets its ritual
  later gets its cute function when its cute class is generated anew.

  What to expect
  --------------

  - Calling the class raises 'NotImplementedError', through the cute
    class and through an object of it alike: a class is no descriptor,
    so an object hands it on as it is.
  - Reading an attribute the class does not have raises
    'NotImplementedError' as well, saying what the class stands for.
  - A name with two underscores before and after it, as '__wrapped__',
    is refused with 'AttributeError', as any class refuses a name it
    lacks. Python and its tools ask for such names with 'hasattr',
    which lets only that error pass.
  - The message is the docstring. Under 'python -OO', which drops
    docstrings, it names the class alone.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getInfo(cls) -> str:
    """Gives the docstring of the class on one line: each function of Qt
    the class stands for, and why it has no cute function."""
    return ' '.join((cls.__doc__ or '').split())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __call__(cls, *__, **_) -> Never:
    """
    Refuses the call.

    Raises
    ------

    NotImplementedError
      Always, naming the function of Qt and why it has no cute
      function.
    """
    infoSpec = """'%s' cannot be called: it stands for a function of Qt
    that has no cute function yet. %s"""
    info = infoSpec % (cls.__qualname__, cls.getInfo())
    raise NotImplementedError(' '.join(info.split()))

  def __getattr__(cls, key: str) -> Never:
    """
    Refuses an attribute the class does not have. Python asks this only
    after the class and its metaclass have nothing at the name.

    Raises
    ------

    AttributeError
      The name has two underscores before and after it.

    NotImplementedError
      Any other name, naming the function of Qt and why it has no cute
      function.
    """
    if key.startswith('__') and key.endswith('__'):
      infoSpec = """type object '%s' has no attribute '%s'"""
      raise AttributeError(infoSpec % (cls.__qualname__, key))
    infoSpec = """'%s' has no attribute '%s': it stands for a function of
    Qt that has no cute function yet. %s"""
    info = infoSpec % (cls.__qualname__, key, cls.getInfo())
    raise NotImplementedError(' '.join(info.split()))
