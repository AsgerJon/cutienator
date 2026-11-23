"""
TestEventConstructors tests the events of Qt that take a device which
Qt fills in itself when it is left out: Qt then calls
'QPointingDevice::primaryPointingDevice()' or
'QInputDevice::primaryKeyboard()', and so does cutienator.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import subprocess
import sys

from worktoy.work_test import BaseTest

import cutienator
from cutienator.occult import Rituals

#  The devices exist once there is an application, so this runs in a
#  Python of its own. Each line it prints is a name, a colon and what
#  was found.
MADE_SHORT = """
from worktoy.waitaminute.dispatch import DispatchException

from cutienator.QtCore import QEvent, QPoint, QPointF, Qt
from cutienator.QtGui import QEnterEvent, QGuiApplication, QHoverEvent
from cutienator.QtGui import QInputDevice, QKeyEvent, QMouseEvent
from cutienator.QtGui import QPointingDevice, QWheelEvent

app = QGuiApplication([])
press, left = QEvent.Type.MouseButtonPress, Qt.MouseButton.LeftButton
none = Qt.KeyboardModifier.NoModifier
primary = QPointingDevice.primaryPointingDevice()
short = QMouseEvent(press, QPointF(3, 4), left, left, none)
print('mouse, device left out:',
      short.pointingDevice().name() == primary.name())
given = QMouseEvent(press, QPointF(3, 4), left, left, none, primary)
print('mouse, device given:',
      given.pointingDevice().name() == primary.name())
key = QKeyEvent(QEvent.Type.KeyPress, 65, none, 0, 0, 0)
keyboard = QInputDevice.primaryKeyboard()
print('key, device left out:', key.device().name() == keyboard.name())
wheel = QWheelEvent(
    QPointF(1, 1), QPointF(1, 1), QPoint(0, 0), QPoint(0, 120),
    Qt.MouseButton.NoButton, none, Qt.ScrollPhase.NoScrollPhase, False)
print('wheel:', wheel.angleDelta().y())
hover = QHoverEvent(
    QEvent.Type.HoverMove, QPointF(1, 1), QPointF(2, 2), QPointF(0, 0))
print('hover:', hover.type().name)
enter = QEnterEvent(QPointF(1, 1), QPointF(1, 1), QPointF(1, 1))
print('enter:', enter.type().name)
try:
  QMouseEvent(press, QPointF(3, 4), left, left, none, ...)
  print('three dots handed over: taken')
except DispatchException:
  print('three dots handed over: refused')
"""


class TestEventConstructors(BaseTest):
  """Runs one program in a Python of its own."""

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  HELPERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def setUpClass(cls) -> None:
    """Builds the shared object of rituals when a ritual file is newer."""
    super().setUpClass()
    if Rituals.isStale():
      Rituals.build()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TESTS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_the_device_qt_fills_in(self) -> None:
    """An event made without its device carries the one Qt names as
    the primary one, an event made with a device carries that one, and
    the three dots that stand for 'left out' are no value to hand
    over."""
    packageFolder = os.path.dirname(os.path.abspath(cutienator.__file__))
    environment = dict(os.environ)
    known = environment.get('PYTHONPATH', '')
    folders = [os.path.dirname(packageFolder), *known.split(os.pathsep)]
    environment['PYTHONPATH'] = os.pathsep.join(f for f in folders if f)
    environment.setdefault('QT_QPA_PLATFORM', 'offscreen')
    done = subprocess.run(
        (sys.executable, '-B', '-c', MADE_SHORT),
        capture_output=True, text=True, env=environment, timeout=120,
    )
    self.assertEqual(done.returncode, 0, done.stderr)
    expected = [
        'mouse, device left out: True',
        'mouse, device given: True',
        'key, device left out: True',
        'wheel: 120',
        'hover: HoverMove',
        'enter: Enter',
        'three dots handed over: refused',
    ]
    self.assertEqual(done.stdout.strip().split('\n'), expected)
