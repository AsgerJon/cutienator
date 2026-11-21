"""
WAIT stands in a class body for a class that is made later.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core import Object
from worktoy.waitaminute import MissingVariable, TypeException

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Never, Optional


class WAIT(Object):
  """
  Stands in a class body for a class that is made later, so that the
  body can name that class in '@overload' all the same.

    class QObject(CuteMixin, metaclass=MetaCute):

      QThread = WAIT['QThread']        # at the top of the class body

      @overload(QThread)
      def moveToThread(self, thread: QThread) -> bool:
        ...

    class QThread(QObject):            # later, in a file of its own
      ...

    QObject().moveToThread(QThread())  # works from here on

  Why it exists
  -------------

  Qt has classes that name each other. 'QObject::moveToThread' takes a
  'QThread', and 'QThread' is built on 'QObject'. In C++ that costs
  nothing: the one line 'class QThread;' says that a class of that name
  is coming. In Python '@overload(QThread)' needs the class itself, and
  'QThread' cannot be made before 'QObject', which it is built on. One
  of the two is always made too soon. A 'WAIT' is our 'class QThread;'.

  worktoy has 'THIS' for a class naming itself in its own body. 'WAIT'
  is for a class naming another class that does not exist yet.

  Terms
  -----

  - The late class is the class a 'WAIT' stands for: 'QThread' above.
  - The waiting class is the class whose body holds the 'WAIT':
    'QObject' above. It is made too soon to name the late class.
  - A waiting signature is a signature of '@overload' with a 'WAIT' in
    it: '(QThread,)' above.

  You provide
  -----------

  - One line per late class, at the top of the body of the waiting
    class, with the name of the late class on both sides:
    'QThread = WAIT['QThread']'. Or no line in the body at all: write
    the 'WAIT' right into the signature, as
    '@overload(WAIT['QThread'])', or bind it at the top of the file
    and name that, and the body gets the line for you. The class files
    the dev tooling writes bind theirs at the top of the file, beside
    the import a type checker reads:

      if TYPE_CHECKING:
        from . import QThread
      else:
        QThread = WAIT['QThread']
  - The late class itself, written as any cute class, under that name.
    Nothing has to be called once it is made.

  What happens, step by step
  --------------------------

  1. The body of 'QObject' runs in a 'CuteSpace', the namespace
     'MetaCute' prepares for every cute class. The line
     'QThread = WAIT['QThread']' puts a 'WAIT' at the name 'QThread',
     as any attribute of the class.
  2. The body reads the name 'overload'. 'CuteSpace' answers that read
     itself, with 'CuteOverload', whatever the file imported under the
     name.
  3. 'CuteOverload' finds the 'WAIT' in the signature. It does not call
     worktoy's 'overload', which refuses anything but a class. It
     leaves a 'WaitingOverload' at the name 'moveToThread', holding the
     function and every signature its stack of decorators gives it.
  4. 'CuteSpace' takes the 'WaitingOverload' out of the body. It puts
     each signature of it that names no late class on record at once,
     and keeps each of the others as a 'WaitingSignature', with its
     place among the other signatures of that name. worktoy screens
     the name, as for any overload.
  5. 'QObject' is made. Its 'moveToThread' has every signature but the
     waiting one. The 'WAIT' at 'QObject.QThread' tells 'MetaCute' that
     'QObject' waits for a class named 'QThread': see 'hookSetName'.
  6. 'QThread' is made. 'MetaCute' notices the name. It puts the class
     at 'QObject.QThread', has the 'CuteSpace' of 'QObject' put the
     signature back in its place with the class in it, and builds
     'moveToThread' again for 'QObject' and for every class built on it
     so far.

  Why no call is lost by waiting
  ------------------------------

  A waiting signature only matters to a call that hands over an object
  of the late class, and nothing can be an object of a class that is
  not made. Step 6 is the last part of making the late class: it runs
  as the class statement of the late class ends, before the class can
  have a single object. So the first object of the late class there
  ever is already finds every signature that waited for it in place.

  That holds however the object comes to be. A program that makes one
  has brought in the late class to do so. A cute function that gives
  an object of a class its file did not bring in brings in the file of
  that class itself, before it makes the object; the dev tooling
  writes every such function that way.

  What to expect
  --------------

  - Before the late class is made, the waiting signature is not there:
    nothing can be an object of a class that does not exist. The other
    signatures of the name work. A name whose every signature waits is
    not on the class at all until then.
  - After, the waiting class, the classes built on it before and after,
    and the late class itself all take the late class, at the place the
    signature was written in. A wrong argument is refused with
    'DispatchException', as for any signature.
  - Read through the waiting class, the name gives this 'WAIT' until
    the late class is made, and the class from then on. Read through an
    object it raises 'MissingVariable' until then.
  - A late class is recognised by its name alone, as its '__name__'.
  - A 'WAIT' for a class that is made already is settled as the waiting
    class is made.
  - 'MetaCute.getStillWaiting()' names the classes that are waited for
    and not made.
  - A waiting signature may share its function with other
    '@overload(...)' signatures, waiting or not, in one stack of
    decorators. It shares it with nothing else: 'overload.fallback',
    'overload.finalize', 'overload.flex' and a signature ending in
    'ARGS' are refused in a stack that waits, on that line, and so is
    'overload.flex' with a 'WAIT'.
  - A late class is known by its name, so a class made by 'MetaCute'
    under the name of a late class is taken for it. A class of a
    program that is built on a cute class must not have the name of a
    class of Qt.
  - A 'WAIT' is settled for the class whose body binds it, and for no
    other. A class built on 'QObject' that names 'QThread' in a
    signature of its own names a 'WAIT' of its own, by that line or
    right in the signature. A signature naming 'QObject.QThread' is
    refused with 'TypeError' on that line, and the message gives the
    line to write.
  - worktoy is used as it is. Nothing of this changes it.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables

  #  Fallback Variables

  #  Private Variables
  __waiting_name__: Optional[str] = None

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getWaitingName(self) -> str:
    """
    Gives the name of the late class, as 'QThread'.

    Provided by you, between the brackets of 'WAIT['QThread']'. There
    is no setter: a 'WAIT' waits for one class for as long as it exists.

    Raises
    ------

    MissingVariable
      This 'WAIT' was made without the brackets, which only code going
      around 'WAIT[...]' can do.
    """
    if self.__waiting_name__ is None:
      raise MissingVariable(self, '__waiting_name__', str)
    return self.__waiting_name__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def __class_getitem__(cls, lateClassName: str) -> WAIT:
    """
    Makes a 'WAIT' for one late class: 'WAIT['QThread']'.

    This is the only way to make one. Calling 'WAIT(...)' is not it.

    Parameters
    ----------

    lateClassName : str
      The name of the late class, exactly as its class statement will
      have it: 'QThread' for 'class QThread(QObject)'.

    Returns
    -------

    WAIT
      A new 'WAIT', to be bound in a class body to that same name.

    Raises
    ------

    TypeException
      'lateClassName' is not text.

    ValueError
      'lateClassName' is no name a class could have, as '' or '2x'.
    """
    if not isinstance(lateClassName, str):
      raise TypeException('lateClassName', lateClassName, str)
    if not lateClassName.isidentifier():
      infoSpec = """'WAIT' takes the name of a class between its
      brackets, as WAIT['QThread'], but received '%s'."""
      raise ValueError(' '.join((infoSpec % lateClassName).split()))
    self = object.__new__(cls)
    object.__setattr__(self, '__waiting_name__', lateClassName)
    return self

  def __str__(self) -> str:
    """Shows the 'WAIT' as it is written: WAIT['QThread']."""
    return """WAIT['%s']""" % self.getWaitingName()

  __repr__ = __str__

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

  def __instance_get__(self, instance: Any, owner: type, **kwargs) -> Never:
    """
    Refuses a read through an object, as 'QObject().QThread', for as
    long as the late class is not made: there is no class to give yet.

    'Object.__get__' calls this for every such read, after its hook
    'hookPreGet', which is why the refusal sits here and not in
    '__get__'. Once the late class is made, the class itself is at the
    name, and this method is never reached again for it.

    Raises
    ------

    MissingVariable
      Always. It is an 'AttributeError', so 'hasattr' answers False.
    """
    raise MissingVariable(instance, self.getFieldName(), type)

  def hookSetName(self, owner: type, name: str, **kwargs) -> None:
    """
    Tells the metaclass of the waiting class that this class waits.

    'Object.__set_name__' calls this as the waiting class is made, with
    the waiting class and the name this 'WAIT' is bound to. You never
    call it. From here on 'MetaCute' knows that 'owner' waits at 'name'
    for a class called as 'getWaitingName' says, and settles it when
    that class is made.

    Parameters
    ----------

    owner : type
      The waiting class, being made right now.

    name : str
      The name this 'WAIT' is bound to in the body of 'owner'.

    Raises
    ------

    TypeError
      'owner' is not made by 'MetaCute', so nothing would ever notice
      the late class. A 'WAIT' belongs in the body of a cute class.
    """
    try:
      addWaiting = type.__getattribute__(type(owner), 'addWaiting')
    except AttributeError as attributeError:
      infoSpec = """%s is bound at '%s.%s', and the class '%s' is made by
      '%s', which notices no late class. A 'WAIT' belongs in the body of
      a class made by 'MetaCute'."""
      info = infoSpec % (
          self, owner.__name__, name, owner.__name__,
          type(owner).__name__,
      )
      raise TypeError(' '.join(info.split())) from attributeError
    addWaiting(owner, name, self)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
