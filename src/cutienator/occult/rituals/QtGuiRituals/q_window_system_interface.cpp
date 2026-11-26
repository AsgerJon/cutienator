//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: the ritual of the handleExtendedKeyEvent taking a
//  QInputDevice is taken out, as Qt's library does not offer it (undefined
//  reference). Kept as it is when the generator runs again. Also added by
//  hand on 2026-11-25, instances of templates of the class: 69.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformdrag.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qrect.h>
#include <QtCore/qurl.h>
#include <QtGui/qregion.h>

//  bool QWindowSystemInterface::handleShortcutEvent(QWindow *window, ulong
//      timestamp, int k, Qt::KeyboardModifiers mods, quint32 nativeScanCode,
//      quint32 nativeVirtualKey, quint32 nativeModifiers, const QString
//      &text, bool autorep, ushort count)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface19handleShortcutEventEP7QWindowmi6QFlagsIN2Qt16KeyboardModifierEEjjjRK7QStringbt(
    QWindow *window,
    ulong timestamp,
    int k,
    int mods,
    quint32 nativeScanCode,
    quint32 nativeVirtualKey,
    quint32 nativeModifiers,
    const QString *text,
    bool autorep,
    ushort count) {
  return QWindowSystemInterface::handleShortcutEvent(
      window,
      timestamp,
      k,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      nativeScanCode,
      nativeVirtualKey,
      nativeModifiers,
      *text,
      autorep,
      count);
}

//  bool QWindowSystemInterface::handleExtendedKeyEvent(QWindow *window,
//      QEvent::Type type, int key, Qt::KeyboardModifiers modifiers, quint32
//      nativeScanCode, quint32 nativeVirtualKey, quint32 nativeModifiers,
//      const QString &text, bool autorep, ushort count)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface22handleExtendedKeyEventEP7QWindowN6QEvent4TypeEi6QFlagsIN2Qt16KeyboardModifierEEjjjRK7QStringbt(
    QWindow *window,
    QEvent::Type type,
    int key,
    int modifiers,
    quint32 nativeScanCode,
    quint32 nativeVirtualKey,
    quint32 nativeModifiers,
    const QString *text,
    bool autorep,
    ushort count) {
  return QWindowSystemInterface::handleExtendedKeyEvent(
      window,
      type,
      key,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      nativeScanCode,
      nativeVirtualKey,
      nativeModifiers,
      *text,
      autorep,
      count);
}

//  bool QWindowSystemInterface::handleExtendedKeyEvent(QWindow *window,
//      ulong timestamp, QEvent::Type type, int key, Qt::KeyboardModifiers
//      modifiers, quint32 nativeScanCode, quint32 nativeVirtualKey, quint32
//      nativeModifiers, const QString &text, bool autorep, ushort count)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface22handleExtendedKeyEventEP7QWindowmN6QEvent4TypeEi6QFlagsIN2Qt16KeyboardModifierEEjjjRK7QStringbt(
    QWindow *window,
    ulong timestamp,
    QEvent::Type type,
    int key,
    int modifiers,
    quint32 nativeScanCode,
    quint32 nativeVirtualKey,
    quint32 nativeModifiers,
    const QString *text,
    bool autorep,
    ushort count) {
  return QWindowSystemInterface::handleExtendedKeyEvent(
      window,
      timestamp,
      type,
      key,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      nativeScanCode,
      nativeVirtualKey,
      nativeModifiers,
      *text,
      autorep,
      count);
}

//  bool QWindowSystemInterface::handleWheelEvent(QWindow *window, const
//      QPointF &local, const QPointF &global, QPoint pixelDelta, QPoint
//      angleDelta, Qt::KeyboardModifiers mods, Qt::ScrollPhase phase,
//      Qt::MouseEventSource source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface16handleWheelEventEP7QWindowRK7QPointFS4_6QPointS5_6QFlagsIN2Qt16KeyboardModifierEENS7_11ScrollPhaseENS7_16MouseEventSourceE(
    QWindow *window,
    const QPointF *local,
    const QPointF *global,
    const QPoint *pixelDelta,
    const QPoint *angleDelta,
    int mods,
    Qt::ScrollPhase phase,
    Qt::MouseEventSource source) {
  return QWindowSystemInterface::handleWheelEvent(
      window,
      *local,
      *global,
      *pixelDelta,
      *angleDelta,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      phase,
      source);
}

//  bool QWindowSystemInterface::handleWheelEvent(QWindow *window, ulong
//      timestamp, const QPointF &local, const QPointF &global, QPoint
//      pixelDelta, QPoint angleDelta, Qt::KeyboardModifiers mods,
//      Qt::ScrollPhase phase, Qt::MouseEventSource source, bool inverted)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface16handleWheelEventEP7QWindowmRK7QPointFS4_6QPointS5_6QFlagsIN2Qt16KeyboardModifierEENS7_11ScrollPhaseENS7_16MouseEventSourceEb(
    QWindow *window,
    ulong timestamp,
    const QPointF *local,
    const QPointF *global,
    const QPoint *pixelDelta,
    const QPoint *angleDelta,
    int mods,
    Qt::ScrollPhase phase,
    Qt::MouseEventSource source,
    bool inverted) {
  return QWindowSystemInterface::handleWheelEvent(
      window,
      timestamp,
      *local,
      *global,
      *pixelDelta,
      *angleDelta,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      phase,
      source,
      inverted);
}

//  bool QWindowSystemInterface::handleWheelEvent(QWindow *window, ulong
//      timestamp, const QPointingDevice *device, const QPointF &local, const
//      QPointF &global, QPoint pixelDelta, QPoint angleDelta,
//      Qt::KeyboardModifiers mods, Qt::ScrollPhase phase,
//      Qt::MouseEventSource source, bool inverted)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface16handleWheelEventEP7QWindowmPK15QPointingDeviceRK7QPointFS7_6QPointS8_6QFlagsIN2Qt16KeyboardModifierEENSA_11ScrollPhaseENSA_16MouseEventSourceEb(
    QWindow *window,
    ulong timestamp,
    const QPointingDevice *device,
    const QPointF *local,
    const QPointF *global,
    const QPoint *pixelDelta,
    const QPoint *angleDelta,
    int mods,
    Qt::ScrollPhase phase,
    Qt::MouseEventSource source,
    bool inverted) {
  return QWindowSystemInterface::handleWheelEvent(
      window,
      timestamp,
      device,
      *local,
      *global,
      *pixelDelta,
      *angleDelta,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      phase,
      source,
      inverted);
}

//  void QWindowSystemInterface::registerInputDevice(const QInputDevice
//      *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface19registerInputDeviceEPK12QInputDevice(
    const QInputDevice *device) {
  QWindowSystemInterface::registerInputDevice(device);
}

//  void QWindowSystemInterface::handleEnterLeaveEvent(QWindow *enter,
//      QWindow *leave, const QPointF &local, const QPointF &global)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface21handleEnterLeaveEventEP7QWindowS1_RK7QPointFS4_(
    QWindow *enter,
    QWindow *leave,
    const QPointF *local,
    const QPointF *global) {
  QWindowSystemInterface::handleEnterLeaveEvent(
      enter,
      leave,
      *local,
      *global);
}

#if QT_CONFIG(draganddrop)
//  QPlatformDragQtResponse QWindowSystemInterface::handleDrag(QWindow
//      *window, const QMimeData *dropData, const QPoint &p, Qt::DropActions
//      supportedActions, Qt::MouseButtons buttons, Qt::KeyboardModifiers
//      modifiers)
extern "C" Q_DECL_EXPORT
QPlatformDragQtResponse *ritual_ZN22QWindowSystemInterface10handleDragEP7QWindowPK9QMimeDataRK6QPoint6QFlagsIN2Qt10DropActionEES8_INS9_11MouseButtonEES8_INS9_16KeyboardModifierEE(
    QWindow *window,
    const QMimeData *dropData,
    const QPoint *p,
    int supportedActions,
    int buttons,
    int modifiers) {
  return new QPlatformDragQtResponse(
      QWindowSystemInterface::handleDrag(
          window,
          dropData,
          *p,
          QFlags<Qt::DropAction>::fromInt(supportedActions),
          QFlags<Qt::MouseButton>::fromInt(buttons),
          QFlags<Qt::KeyboardModifier>::fromInt(modifiers)));
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  QPlatformDropQtResponse QWindowSystemInterface::handleDrop(QWindow
//      *window, const QMimeData *dropData, const QPoint &p, Qt::DropActions
//      supportedActions, Qt::MouseButtons buttons, Qt::KeyboardModifiers
//      modifiers)
extern "C" Q_DECL_EXPORT
QPlatformDropQtResponse *ritual_ZN22QWindowSystemInterface10handleDropEP7QWindowPK9QMimeDataRK6QPoint6QFlagsIN2Qt10DropActionEES8_INS9_11MouseButtonEES8_INS9_16KeyboardModifierEE(
    QWindow *window,
    const QMimeData *dropData,
    const QPoint *p,
    int supportedActions,
    int buttons,
    int modifiers) {
  return new QPlatformDropQtResponse(
      QWindowSystemInterface::handleDrop(
          window,
          dropData,
          *p,
          QFlags<Qt::DropAction>::fromInt(supportedActions),
          QFlags<Qt::MouseButton>::fromInt(buttons),
          QFlags<Qt::KeyboardModifier>::fromInt(modifiers)));
}
#endif  // QT_CONFIG(draganddrop)

//  bool QWindowSystemInterface::handleNativeEvent(QWindow *window, const
//      QByteArray &eventType, void *message, qintptr *result)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface17handleNativeEventEP7QWindowRK10QByteArrayPvPx(
    QWindow *window,
    const QByteArray *eventType,
    void *message,
    qintptr *result) {
  return QWindowSystemInterface::handleNativeEvent(
      window,
      *eventType,
      message,
      result);
}

//  void QWindowSystemInterface::handleScreenAdded(QPlatformScreen *screen,
//      bool isPrimary)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface17handleScreenAddedEP15QPlatformScreenb(
    QPlatformScreen *screen,
    bool isPrimary) {
  QWindowSystemInterface::handleScreenAdded(screen, isPrimary);
}

//  void QWindowSystemInterface::handleScreenRemoved(QPlatformScreen *screen)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface19handleScreenRemovedEP15QPlatformScreen(
    QPlatformScreen *screen) {
  QWindowSystemInterface::handleScreenRemoved(screen);
}

//  void QWindowSystemInterface::handlePrimaryScreenChanged(QPlatformScreen
//      *newPrimary)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface26handlePrimaryScreenChangedEP15QPlatformScreen(
    QPlatformScreen *newPrimary) {
  QWindowSystemInterface::handlePrimaryScreenChanged(newPrimary);
}

//  void QWindowSystemInterface::handleScreenOrientationChange(QScreen
//      *screen, Qt::ScreenOrientation newOrientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface29handleScreenOrientationChangeEP7QScreenN2Qt17ScreenOrientationE(
    QScreen *screen,
    Qt::ScreenOrientation newOrientation) {
  QWindowSystemInterface::handleScreenOrientationChange(
      screen,
      newOrientation);
}

//  void QWindowSystemInterface::handleScreenGeometryChange(QScreen *screen,
//      const QRect &newGeometry, const QRect &newAvailableGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface26handleScreenGeometryChangeEP7QScreenRK5QRectS4_(
    QScreen *screen,
    const QRect *newGeometry,
    const QRect *newAvailableGeometry) {
  QWindowSystemInterface::handleScreenGeometryChange(
      screen,
      *newGeometry,
      *newAvailableGeometry);
}

//  void QWindowSystemInterface::handleScreenLogicalDotsPerInchChange(QScreen
//      *screen, qreal newDpiX, qreal newDpiY)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface36handleScreenLogicalDotsPerInchChangeEP7QScreendd(
    QScreen *screen,
    qreal newDpiX,
    qreal newDpiY) {
  QWindowSystemInterface::handleScreenLogicalDotsPerInchChange(
      screen,
      newDpiX,
      newDpiY);
}

//  void QWindowSystemInterface::handleScreenRefreshRateChange(QScreen
//      *screen, qreal newRefreshRate)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface29handleScreenRefreshRateChangeEP7QScreend(
    QScreen *screen,
    qreal newRefreshRate) {
  QWindowSystemInterface::handleScreenRefreshRateChange(
      screen,
      newRefreshRate);
}

//  void QWindowSystemInterface::handleFileOpenEvent(const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface19handleFileOpenEventERK7QString(
    const QString *fileName) {
  QWindowSystemInterface::handleFileOpenEvent(*fileName);
}

//  void QWindowSystemInterface::handleFileOpenEvent(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface19handleFileOpenEventERK4QUrl(
    const QUrl *url) {
  QWindowSystemInterface::handleFileOpenEvent(*url);
}

//  bool QWindowSystemInterface::handleTabletEvent(QWindow *window, ulong
//      timestamp, const QPointingDevice *device, const QPointF &local, const
//      QPointF &global, Qt::MouseButtons buttons, qreal pressure, qreal
//      xTilt, qreal yTilt, qreal tangentialPressure, qreal rotation, qreal
//      z, Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface17handleTabletEventEP7QWindowmPK15QPointingDeviceRK7QPointFS7_6QFlagsIN2Qt11MouseButtonEEddddddS8_INS9_16KeyboardModifierEE(
    QWindow *window,
    ulong timestamp,
    const QPointingDevice *device,
    const QPointF *local,
    const QPointF *global,
    int buttons,
    qreal pressure,
    qreal xTilt,
    qreal yTilt,
    qreal tangentialPressure,
    qreal rotation,
    qreal z,
    int modifiers) {
  return QWindowSystemInterface::handleTabletEvent(
      window,
      timestamp,
      device,
      *local,
      *global,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      pressure,
      xTilt,
      yTilt,
      tangentialPressure,
      rotation,
      z,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  bool QWindowSystemInterface::handleTabletEvent(QWindow *window, const
//      QPointingDevice *device, const QPointF &local, const QPointF &global,
//      Qt::MouseButtons buttons, qreal pressure, qreal xTilt, qreal yTilt,
//      qreal tangentialPressure, qreal rotation, qreal z,
//      Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface17handleTabletEventEP7QWindowPK15QPointingDeviceRK7QPointFS7_6QFlagsIN2Qt11MouseButtonEEddddddS8_INS9_16KeyboardModifierEE(
    QWindow *window,
    const QPointingDevice *device,
    const QPointF *local,
    const QPointF *global,
    int buttons,
    qreal pressure,
    qreal xTilt,
    qreal yTilt,
    qreal tangentialPressure,
    qreal rotation,
    qreal z,
    int modifiers) {
  return QWindowSystemInterface::handleTabletEvent(
      window,
      device,
      *local,
      *global,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      pressure,
      xTilt,
      yTilt,
      tangentialPressure,
      rotation,
      z,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  bool QWindowSystemInterface::handleTabletEvent(QWindow *window, ulong
//      timestamp, const QPointF &local, const QPointF &global, int device,
//      int pointerType, Qt::MouseButtons buttons, qreal pressure, qreal
//      xTilt, qreal yTilt, qreal tangentialPressure, qreal rotation, qreal
//      z, qint64 uid, Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface17handleTabletEventEP7QWindowmRK7QPointFS4_ii6QFlagsIN2Qt11MouseButtonEEddddddxS5_INS6_16KeyboardModifierEE(
    QWindow *window,
    ulong timestamp,
    const QPointF *local,
    const QPointF *global,
    int device,
    int pointerType,
    int buttons,
    qreal pressure,
    qreal xTilt,
    qreal yTilt,
    qreal tangentialPressure,
    qreal rotation,
    qreal z,
    qint64 uid,
    int modifiers) {
  return QWindowSystemInterface::handleTabletEvent(
      window,
      timestamp,
      *local,
      *global,
      device,
      pointerType,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      pressure,
      xTilt,
      yTilt,
      tangentialPressure,
      rotation,
      z,
      uid,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  bool QWindowSystemInterface::handleTabletEvent(QWindow *window, const
//      QPointF &local, const QPointF &global, int device, int pointerType,
//      Qt::MouseButtons buttons, qreal pressure, qreal xTilt, qreal yTilt,
//      qreal tangentialPressure, qreal rotation, qreal z, qint64 uid,
//      Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface17handleTabletEventEP7QWindowRK7QPointFS4_ii6QFlagsIN2Qt11MouseButtonEEddddddxS5_INS6_16KeyboardModifierEE(
    QWindow *window,
    const QPointF *local,
    const QPointF *global,
    int device,
    int pointerType,
    int buttons,
    qreal pressure,
    qreal xTilt,
    qreal yTilt,
    qreal tangentialPressure,
    qreal rotation,
    qreal z,
    qint64 uid,
    int modifiers) {
  return QWindowSystemInterface::handleTabletEvent(
      window,
      *local,
      *global,
      device,
      pointerType,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      pressure,
      xTilt,
      yTilt,
      tangentialPressure,
      rotation,
      z,
      uid,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  bool QWindowSystemInterface::handleTabletEnterLeaveProximityEvent(QWindow
//      *window, ulong timestamp, const QPointingDevice *device, bool
//      inProximity, const QPointF &local, const QPointF &global,
//      Qt::MouseButtons buttons, qreal xTilt, qreal yTilt, qreal
//      tangentialPressure, qreal rotation, qreal z, Qt::KeyboardModifiers
//      modifiers)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface36handleTabletEnterLeaveProximityEventEP7QWindowmPK15QPointingDevicebRK7QPointFS7_6QFlagsIN2Qt11MouseButtonEEdddddS8_INS9_16KeyboardModifierEE(
    QWindow *window,
    ulong timestamp,
    const QPointingDevice *device,
    bool inProximity,
    const QPointF *local,
    const QPointF *global,
    int buttons,
    qreal xTilt,
    qreal yTilt,
    qreal tangentialPressure,
    qreal rotation,
    qreal z,
    int modifiers) {
  return QWindowSystemInterface::handleTabletEnterLeaveProximityEvent(
      window,
      timestamp,
      device,
      inProximity,
      *local,
      *global,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      xTilt,
      yTilt,
      tangentialPressure,
      rotation,
      z,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  bool QWindowSystemInterface::handleTabletEnterLeaveProximityEvent(QWindow
//      *window, const QPointingDevice *device, bool inProximity, const
//      QPointF &local, const QPointF &global, Qt::MouseButtons buttons,
//      qreal xTilt, qreal yTilt, qreal tangentialPressure, qreal rotation,
//      qreal z, Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface36handleTabletEnterLeaveProximityEventEP7QWindowPK15QPointingDevicebRK7QPointFS7_6QFlagsIN2Qt11MouseButtonEEdddddS8_INS9_16KeyboardModifierEE(
    QWindow *window,
    const QPointingDevice *device,
    bool inProximity,
    const QPointF *local,
    const QPointF *global,
    int buttons,
    qreal xTilt,
    qreal yTilt,
    qreal tangentialPressure,
    qreal rotation,
    qreal z,
    int modifiers) {
  return QWindowSystemInterface::handleTabletEnterLeaveProximityEvent(
      window,
      device,
      inProximity,
      *local,
      *global,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      xTilt,
      yTilt,
      tangentialPressure,
      rotation,
      z,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  bool QWindowSystemInterface::handleTabletEnterProximityEvent(ulong
//      timestamp, int deviceType, int pointerType, qint64 uid)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface31handleTabletEnterProximityEventEmiix(
    ulong timestamp,
    int deviceType,
    int pointerType,
    qint64 uid) {
  return QWindowSystemInterface::handleTabletEnterProximityEvent(
      timestamp,
      deviceType,
      pointerType,
      uid);
}

//  void QWindowSystemInterface::handleTabletEnterProximityEvent(int
//      deviceType, int pointerType, qint64 uid)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface31handleTabletEnterProximityEventEiix(
    int deviceType,
    int pointerType,
    qint64 uid) {
  QWindowSystemInterface::handleTabletEnterProximityEvent(
      deviceType,
      pointerType,
      uid);
}

//  bool QWindowSystemInterface::handleTabletLeaveProximityEvent(ulong
//      timestamp, int deviceType, int pointerType, qint64 uid)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface31handleTabletLeaveProximityEventEmiix(
    ulong timestamp,
    int deviceType,
    int pointerType,
    qint64 uid) {
  return QWindowSystemInterface::handleTabletLeaveProximityEvent(
      timestamp,
      deviceType,
      pointerType,
      uid);
}

//  void QWindowSystemInterface::handleTabletLeaveProximityEvent(int
//      deviceType, int pointerType, qint64 uid)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface31handleTabletLeaveProximityEventEiix(
    int deviceType,
    int pointerType,
    qint64 uid) {
  QWindowSystemInterface::handleTabletLeaveProximityEvent(
      deviceType,
      pointerType,
      uid);
}

#if !defined(QT_NO_GESTURES)
//  bool QWindowSystemInterface::handleGestureEvent(QWindow *window, ulong
//      timestamp, const QPointingDevice *device, Qt::NativeGestureType type,
//      const QPointF &local, const QPointF &global, int fingerCount)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface18handleGestureEventEP7QWindowmPK15QPointingDeviceN2Qt17NativeGestureTypeERK7QPointFS9_i(
    QWindow *window,
    ulong timestamp,
    const QPointingDevice *device,
    Qt::NativeGestureType type,
    const QPointF *local,
    const QPointF *global,
    int fingerCount) {
  return QWindowSystemInterface::handleGestureEvent(
      window,
      timestamp,
      device,
      type,
      *local,
      *global,
      fingerCount);
}
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
//  bool QWindowSystemInterface::handleGestureEventWithRealValue(QWindow
//      *window, ulong timestamp, const QPointingDevice *device,
//      Qt::NativeGestureType type, qreal value, const QPointF &local, const
//      QPointF &global, int fingerCount)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface31handleGestureEventWithRealValueEP7QWindowmPK15QPointingDeviceN2Qt17NativeGestureTypeEdRK7QPointFS9_i(
    QWindow *window,
    ulong timestamp,
    const QPointingDevice *device,
    Qt::NativeGestureType type,
    qreal value,
    const QPointF *local,
    const QPointF *global,
    int fingerCount) {
  return QWindowSystemInterface::handleGestureEventWithRealValue(
      window,
      timestamp,
      device,
      type,
      value,
      *local,
      *global,
      fingerCount);
}
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
//  bool QWindowSystemInterface::handleGestureEventWithValueAndDelta(QWindow
//      *window, ulong timestamp, const QPointingDevice *device,
//      Qt::NativeGestureType type, qreal value, const QPointF &delta, const
//      QPointF &local, const QPointF &global, int fingerCount)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface35handleGestureEventWithValueAndDeltaEP7QWindowmPK15QPointingDeviceN2Qt17NativeGestureTypeEdRK7QPointFS9_S9_i(
    QWindow *window,
    ulong timestamp,
    const QPointingDevice *device,
    Qt::NativeGestureType type,
    qreal value,
    const QPointF *delta,
    const QPointF *local,
    const QPointF *global,
    int fingerCount) {
  return QWindowSystemInterface::handleGestureEventWithValueAndDelta(
      window,
      timestamp,
      device,
      type,
      value,
      *delta,
      *local,
      *global,
      fingerCount);
}
#endif  // !defined(QT_NO_GESTURES)

//  void QWindowSystemInterface::handlePlatformPanelEvent(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface24handlePlatformPanelEventEP7QWindow(
    QWindow *window) {
  QWindowSystemInterface::handlePlatformPanelEvent(window);
}

#if QT_CONFIG(whatsthis)
//  void QWindowSystemInterface::handleEnterWhatsThisEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface25handleEnterWhatsThisEventEv() {
  QWindowSystemInterface::handleEnterWhatsThisEvent();
}
#endif  // QT_CONFIG(whatsthis)

//  bool QWindowSystemInterface::sendWindowSystemEvents(QEventLoop::ProcessEv
//      entsFlags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface22sendWindowSystemEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    int flags) {
  return QWindowSystemInterface::sendWindowSystemEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

//  void QWindowSystemInterface::setSynchronousWindowSystemEvents(bool
//      enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface32setSynchronousWindowSystemEventsEb(
    bool enable) {
  QWindowSystemInterface::setSynchronousWindowSystemEvents(enable);
}

//  bool QWindowSystemInterface::flushWindowSystemEvents(QEventLoop::ProcessE
//      ventsFlags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface23flushWindowSystemEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    int flags) {
  return QWindowSystemInterface::flushWindowSystemEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

//  void QWindowSystemInterface::deferredFlushWindowSystemEvents(QEventLoop::
//      ProcessEventsFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface31deferredFlushWindowSystemEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    int flags) {
  QWindowSystemInterface::deferredFlushWindowSystemEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

//  int QWindowSystemInterface::windowSystemEventsQueued()
extern "C" Q_DECL_EXPORT
int ritual_ZN22QWindowSystemInterface24windowSystemEventsQueuedEv() {
  return QWindowSystemInterface::windowSystemEventsQueued();
}

//  bool QWindowSystemInterface::nonUserInputEventsQueued()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface24nonUserInputEventsQueuedEv() {
  return QWindowSystemInterface::nonUserInputEventsQueued();
}

//  QWindowSystemInterface::~QWindowSystemInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterfaceD1Ev(QWindowSystemInterface *self) {
  delete self;
}

//  static void QWindowSystemInterface::handleApplicationStateChanged<
//      QWindowSystemInterface::DefaultDelivery>(Qt::ApplicationState
//      newState, bool forcePropagate)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface29handleApplicationStateChangedINS_15DefaultDeliveryEEEvN2Qt16ApplicationStateEb(
    Qt::ApplicationState newState,
    bool forcePropagate) {
  QWindowSystemInterface::handleApplicationStateChanged<
      QWindowSystemInterface::DefaultDelivery>(
      newState,
      forcePropagate);
}

//  static void QWindowSystemInterface::handleApplicationStateChanged<
//      QWindowSystemInterface::SynchronousDelivery>(Qt::ApplicationState
//      newState, bool forcePropagate)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface29handleApplicationStateChangedINS_19SynchronousDeliveryEEEvN2Qt16ApplicationStateEb(
    Qt::ApplicationState newState,
    bool forcePropagate) {
  QWindowSystemInterface::handleApplicationStateChanged<
      QWindowSystemInterface::SynchronousDelivery>(
      newState,
      forcePropagate);
}

//  static void QWindowSystemInterface::handleApplicationStateChanged<
//      QWindowSystemInterface::AsynchronousDelivery>(Qt::ApplicationState
//      newState, bool forcePropagate)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface29handleApplicationStateChangedINS_20AsynchronousDeliveryEEEvN2Qt16ApplicationStateEb(
    Qt::ApplicationState newState,
    bool forcePropagate) {
  QWindowSystemInterface::handleApplicationStateChanged<
      QWindowSystemInterface::AsynchronousDelivery>(
      newState,
      forcePropagate);
}

//  static bool QWindowSystemInterface::handleApplicationTermination<
//      QWindowSystemInterface::DefaultDelivery>()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface28handleApplicationTerminationINS_15DefaultDeliveryEEEbv() {
  return QWindowSystemInterface::handleApplicationTermination<
      QWindowSystemInterface::DefaultDelivery>();
}

//  static bool QWindowSystemInterface::handleApplicationTermination<
//      QWindowSystemInterface::SynchronousDelivery>()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface28handleApplicationTerminationINS_19SynchronousDeliveryEEEbv() {
  return QWindowSystemInterface::handleApplicationTermination<
      QWindowSystemInterface::SynchronousDelivery>();
}

//  static bool QWindowSystemInterface::handleApplicationTermination<
//      QWindowSystemInterface::AsynchronousDelivery>()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface28handleApplicationTerminationINS_20AsynchronousDeliveryEEEbv() {
  return QWindowSystemInterface::handleApplicationTermination<
      QWindowSystemInterface::AsynchronousDelivery>();
}

//  static bool QWindowSystemInterface::handleCloseEvent<
//      QWindowSystemInterface::DefaultDelivery>(QWindow *window)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface16handleCloseEventINS_15DefaultDeliveryEEEbP7QWindow(
    QWindow *window) {
  return QWindowSystemInterface::handleCloseEvent<
      QWindowSystemInterface::DefaultDelivery>(
      window);
}

//  static bool QWindowSystemInterface::handleCloseEvent<
//      QWindowSystemInterface::SynchronousDelivery>(QWindow *window)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface16handleCloseEventINS_19SynchronousDeliveryEEEbP7QWindow(
    QWindow *window) {
  return QWindowSystemInterface::handleCloseEvent<
      QWindowSystemInterface::SynchronousDelivery>(
      window);
}

//  static bool QWindowSystemInterface::handleCloseEvent<
//      QWindowSystemInterface::AsynchronousDelivery>(QWindow *window)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface16handleCloseEventINS_20AsynchronousDeliveryEEEbP7QWindow(
    QWindow *window) {
  return QWindowSystemInterface::handleCloseEvent<
      QWindowSystemInterface::AsynchronousDelivery>(
      window);
}

#ifndef QT_NO_CONTEXTMENU
//  static bool QWindowSystemInterface::handleContextMenuEvent<
//      QWindowSystemInterface::DefaultDelivery>(QWindow *window, bool
//      mouseTriggered, const QPoint &pos, const QPoint &globalPos,
//      Qt::KeyboardModifiers mods)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface22handleContextMenuEventINS_15DefaultDeliveryEEEbP7QWindowbRK6QPointS6_6QFlagsIN2Qt16KeyboardModifierEE(
    QWindow *window,
    bool mouseTriggered,
    const QPoint *pos,
    const QPoint *globalPos,
    int mods) {
  return QWindowSystemInterface::handleContextMenuEvent<
      QWindowSystemInterface::DefaultDelivery>(
      window,
      mouseTriggered,
      *pos,
      *globalPos,
      QFlags<Qt::KeyboardModifier>::fromInt(mods));
}
#endif  // QT_NO_CONTEXTMENU

#ifndef QT_NO_CONTEXTMENU
//  static bool QWindowSystemInterface::handleContextMenuEvent<
//      QWindowSystemInterface::SynchronousDelivery>(QWindow *window, bool
//      mouseTriggered, const QPoint &pos, const QPoint &globalPos,
//      Qt::KeyboardModifiers mods)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface22handleContextMenuEventINS_19SynchronousDeliveryEEEbP7QWindowbRK6QPointS6_6QFlagsIN2Qt16KeyboardModifierEE(
    QWindow *window,
    bool mouseTriggered,
    const QPoint *pos,
    const QPoint *globalPos,
    int mods) {
  return QWindowSystemInterface::handleContextMenuEvent<
      QWindowSystemInterface::SynchronousDelivery>(
      window,
      mouseTriggered,
      *pos,
      *globalPos,
      QFlags<Qt::KeyboardModifier>::fromInt(mods));
}
#endif  // QT_NO_CONTEXTMENU

#ifndef QT_NO_CONTEXTMENU
//  static bool QWindowSystemInterface::handleContextMenuEvent<
//      QWindowSystemInterface::AsynchronousDelivery>(QWindow *window, bool
//      mouseTriggered, const QPoint &pos, const QPoint &globalPos,
//      Qt::KeyboardModifiers mods)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface22handleContextMenuEventINS_20AsynchronousDeliveryEEEbP7QWindowbRK6QPointS6_6QFlagsIN2Qt16KeyboardModifierEE(
    QWindow *window,
    bool mouseTriggered,
    const QPoint *pos,
    const QPoint *globalPos,
    int mods) {
  return QWindowSystemInterface::handleContextMenuEvent<
      QWindowSystemInterface::AsynchronousDelivery>(
      window,
      mouseTriggered,
      *pos,
      *globalPos,
      QFlags<Qt::KeyboardModifier>::fromInt(mods));
}
#endif  // QT_NO_CONTEXTMENU

//  static void QWindowSystemInterface::handleEnterEvent<
//      QWindowSystemInterface::DefaultDelivery>(QWindow *window, const
//      QPointF &local, const QPointF &global)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface16handleEnterEventINS_15DefaultDeliveryEEEvP7QWindowRK7QPointFS6_(
    QWindow *window,
    const QPointF *local,
    const QPointF *global) {
  QWindowSystemInterface::handleEnterEvent<
      QWindowSystemInterface::DefaultDelivery>(
      window,
      *local,
      *global);
}

//  static void QWindowSystemInterface::handleEnterEvent<
//      QWindowSystemInterface::SynchronousDelivery>(QWindow *window, const
//      QPointF &local, const QPointF &global)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface16handleEnterEventINS_19SynchronousDeliveryEEEvP7QWindowRK7QPointFS6_(
    QWindow *window,
    const QPointF *local,
    const QPointF *global) {
  QWindowSystemInterface::handleEnterEvent<
      QWindowSystemInterface::SynchronousDelivery>(
      window,
      *local,
      *global);
}

//  static void QWindowSystemInterface::handleEnterEvent<
//      QWindowSystemInterface::AsynchronousDelivery>(QWindow *window, const
//      QPointF &local, const QPointF &global)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface16handleEnterEventINS_20AsynchronousDeliveryEEEvP7QWindowRK7QPointFS6_(
    QWindow *window,
    const QPointF *local,
    const QPointF *global) {
  QWindowSystemInterface::handleEnterEvent<
      QWindowSystemInterface::AsynchronousDelivery>(
      window,
      *local,
      *global);
}

//  static bool QWindowSystemInterface::handleExposeEvent<
//      QWindowSystemInterface::DefaultDelivery>(QWindow *window, const
//      QRegion &region)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface17handleExposeEventINS_15DefaultDeliveryEEEbP7QWindowRK7QRegion(
    QWindow *window,
    const QRegion *region) {
  return QWindowSystemInterface::handleExposeEvent<
      QWindowSystemInterface::DefaultDelivery>(
      window,
      *region);
}

//  static bool QWindowSystemInterface::handleExposeEvent<
//      QWindowSystemInterface::SynchronousDelivery>(QWindow *window, const
//      QRegion &region)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface17handleExposeEventINS_19SynchronousDeliveryEEEbP7QWindowRK7QRegion(
    QWindow *window,
    const QRegion *region) {
  return QWindowSystemInterface::handleExposeEvent<
      QWindowSystemInterface::SynchronousDelivery>(
      window,
      *region);
}

//  static bool QWindowSystemInterface::handleExposeEvent<
//      QWindowSystemInterface::AsynchronousDelivery>(QWindow *window, const
//      QRegion &region)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface17handleExposeEventINS_20AsynchronousDeliveryEEEbP7QWindowRK7QRegion(
    QWindow *window,
    const QRegion *region) {
  return QWindowSystemInterface::handleExposeEvent<
      QWindowSystemInterface::AsynchronousDelivery>(
      window,
      *region);
}

//  static void QWindowSystemInterface::handleFocusWindowChanged<
//      QWindowSystemInterface::DefaultDelivery>(QWindow *window,
//      Qt::FocusReason r)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface24handleFocusWindowChangedINS_15DefaultDeliveryEEEvP7QWindowN2Qt11FocusReasonE(
    QWindow *window,
    Qt::FocusReason r) {
  QWindowSystemInterface::handleFocusWindowChanged<
      QWindowSystemInterface::DefaultDelivery>(
      window,
      r);
}

//  static void QWindowSystemInterface::handleFocusWindowChanged<
//      QWindowSystemInterface::SynchronousDelivery>(QWindow *window,
//      Qt::FocusReason r)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface24handleFocusWindowChangedINS_19SynchronousDeliveryEEEvP7QWindowN2Qt11FocusReasonE(
    QWindow *window,
    Qt::FocusReason r) {
  QWindowSystemInterface::handleFocusWindowChanged<
      QWindowSystemInterface::SynchronousDelivery>(
      window,
      r);
}

//  static void QWindowSystemInterface::handleFocusWindowChanged<
//      QWindowSystemInterface::AsynchronousDelivery>(QWindow *window,
//      Qt::FocusReason r)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface24handleFocusWindowChangedINS_20AsynchronousDeliveryEEEvP7QWindowN2Qt11FocusReasonE(
    QWindow *window,
    Qt::FocusReason r) {
  QWindowSystemInterface::handleFocusWindowChanged<
      QWindowSystemInterface::AsynchronousDelivery>(
      window,
      r);
}

//  static void QWindowSystemInterface::handleGeometryChange<
//      QWindowSystemInterface::DefaultDelivery>(QWindow *window, const QRect
//      &newRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface20handleGeometryChangeINS_15DefaultDeliveryEEEvP7QWindowRK5QRect(
    QWindow *window,
    const QRect *newRect) {
  QWindowSystemInterface::handleGeometryChange<
      QWindowSystemInterface::DefaultDelivery>(
      window,
      *newRect);
}

//  static void QWindowSystemInterface::handleGeometryChange<
//      QWindowSystemInterface::SynchronousDelivery>(QWindow *window, const
//      QRect &newRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface20handleGeometryChangeINS_19SynchronousDeliveryEEEvP7QWindowRK5QRect(
    QWindow *window,
    const QRect *newRect) {
  QWindowSystemInterface::handleGeometryChange<
      QWindowSystemInterface::SynchronousDelivery>(
      window,
      *newRect);
}

//  static void QWindowSystemInterface::handleGeometryChange<
//      QWindowSystemInterface::AsynchronousDelivery>(QWindow *window, const
//      QRect &newRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface20handleGeometryChangeINS_20AsynchronousDeliveryEEEvP7QWindowRK5QRect(
    QWindow *window,
    const QRect *newRect) {
  QWindowSystemInterface::handleGeometryChange<
      QWindowSystemInterface::AsynchronousDelivery>(
      window,
      *newRect);
}

//  static bool QWindowSystemInterface::handleKeyEvent<
//      QWindowSystemInterface::DefaultDelivery>(QWindow *window, ulong
//      timestamp, QEvent::Type t, int k, Qt::KeyboardModifiers mods, const
//      QString &text, bool autorep, ushort count)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface14handleKeyEventINS_15DefaultDeliveryEEEbP7QWindowmN6QEvent4TypeEi6QFlagsIN2Qt16KeyboardModifierEERK7QStringbt(
    QWindow *window,
    ulong timestamp,
    QEvent::Type t,
    int k,
    int mods,
    const QString *text,
    bool autorep,
    ushort count) {
  return QWindowSystemInterface::handleKeyEvent<
      QWindowSystemInterface::DefaultDelivery>(
      window,
      timestamp,
      t,
      k,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      *text,
      autorep,
      count);
}

//  static bool QWindowSystemInterface::handleKeyEvent<
//      QWindowSystemInterface::DefaultDelivery>(QWindow *window,
//      QEvent::Type t, int k, Qt::KeyboardModifiers mods, const QString
//      &text, bool autorep, ushort count)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface14handleKeyEventINS_15DefaultDeliveryEEEbP7QWindowN6QEvent4TypeEi6QFlagsIN2Qt16KeyboardModifierEERK7QStringbt(
    QWindow *window,
    QEvent::Type t,
    int k,
    int mods,
    const QString *text,
    bool autorep,
    ushort count) {
  return QWindowSystemInterface::handleKeyEvent<
      QWindowSystemInterface::DefaultDelivery>(
      window,
      t,
      k,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      *text,
      autorep,
      count);
}

//  static bool QWindowSystemInterface::handleKeyEvent<
//      QWindowSystemInterface::SynchronousDelivery>(QWindow *window, ulong
//      timestamp, QEvent::Type t, int k, Qt::KeyboardModifiers mods, const
//      QString &text, bool autorep, ushort count)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface14handleKeyEventINS_19SynchronousDeliveryEEEbP7QWindowmN6QEvent4TypeEi6QFlagsIN2Qt16KeyboardModifierEERK7QStringbt(
    QWindow *window,
    ulong timestamp,
    QEvent::Type t,
    int k,
    int mods,
    const QString *text,
    bool autorep,
    ushort count) {
  return QWindowSystemInterface::handleKeyEvent<
      QWindowSystemInterface::SynchronousDelivery>(
      window,
      timestamp,
      t,
      k,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      *text,
      autorep,
      count);
}

//  static bool QWindowSystemInterface::handleKeyEvent<
//      QWindowSystemInterface::SynchronousDelivery>(QWindow *window,
//      QEvent::Type t, int k, Qt::KeyboardModifiers mods, const QString
//      &text, bool autorep, ushort count)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface14handleKeyEventINS_19SynchronousDeliveryEEEbP7QWindowN6QEvent4TypeEi6QFlagsIN2Qt16KeyboardModifierEERK7QStringbt(
    QWindow *window,
    QEvent::Type t,
    int k,
    int mods,
    const QString *text,
    bool autorep,
    ushort count) {
  return QWindowSystemInterface::handleKeyEvent<
      QWindowSystemInterface::SynchronousDelivery>(
      window,
      t,
      k,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      *text,
      autorep,
      count);
}

//  static bool QWindowSystemInterface::handleKeyEvent<
//      QWindowSystemInterface::AsynchronousDelivery>(QWindow *window, ulong
//      timestamp, QEvent::Type t, int k, Qt::KeyboardModifiers mods, const
//      QString &text, bool autorep, ushort count)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface14handleKeyEventINS_20AsynchronousDeliveryEEEbP7QWindowmN6QEvent4TypeEi6QFlagsIN2Qt16KeyboardModifierEERK7QStringbt(
    QWindow *window,
    ulong timestamp,
    QEvent::Type t,
    int k,
    int mods,
    const QString *text,
    bool autorep,
    ushort count) {
  return QWindowSystemInterface::handleKeyEvent<
      QWindowSystemInterface::AsynchronousDelivery>(
      window,
      timestamp,
      t,
      k,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      *text,
      autorep,
      count);
}

//  static bool QWindowSystemInterface::handleKeyEvent<
//      QWindowSystemInterface::AsynchronousDelivery>(QWindow *window,
//      QEvent::Type t, int k, Qt::KeyboardModifiers mods, const QString
//      &text, bool autorep, ushort count)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface14handleKeyEventINS_20AsynchronousDeliveryEEEbP7QWindowN6QEvent4TypeEi6QFlagsIN2Qt16KeyboardModifierEERK7QStringbt(
    QWindow *window,
    QEvent::Type t,
    int k,
    int mods,
    const QString *text,
    bool autorep,
    ushort count) {
  return QWindowSystemInterface::handleKeyEvent<
      QWindowSystemInterface::AsynchronousDelivery>(
      window,
      t,
      k,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      *text,
      autorep,
      count);
}

//  static void QWindowSystemInterface::handleLeaveEvent<
//      QWindowSystemInterface::DefaultDelivery>(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface16handleLeaveEventINS_15DefaultDeliveryEEEvP7QWindow(
    QWindow *window) {
  QWindowSystemInterface::handleLeaveEvent<
      QWindowSystemInterface::DefaultDelivery>(
      window);
}

//  static void QWindowSystemInterface::handleLeaveEvent<
//      QWindowSystemInterface::SynchronousDelivery>(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface16handleLeaveEventINS_19SynchronousDeliveryEEEvP7QWindow(
    QWindow *window) {
  QWindowSystemInterface::handleLeaveEvent<
      QWindowSystemInterface::SynchronousDelivery>(
      window);
}

//  static void QWindowSystemInterface::handleLeaveEvent<
//      QWindowSystemInterface::AsynchronousDelivery>(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface16handleLeaveEventINS_20AsynchronousDeliveryEEEvP7QWindow(
    QWindow *window) {
  QWindowSystemInterface::handleLeaveEvent<
      QWindowSystemInterface::AsynchronousDelivery>(
      window);
}

//  static bool QWindowSystemInterface::handleMouseEvent<
//      QWindowSystemInterface::DefaultDelivery>(QWindow *window, ulong
//      timestamp, const QPointingDevice *device, const QPointF &local, const
//      QPointF &global, Qt::MouseButtons state, Qt::MouseButton button,
//      QEvent::Type type, Qt::KeyboardModifiers mods, Qt::MouseEventSource
//      source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface16handleMouseEventINS_15DefaultDeliveryEEEbP7QWindowmPK15QPointingDeviceRK7QPointFS9_6QFlagsIN2Qt11MouseButtonEESC_N6QEvent4TypeESA_INSB_16KeyboardModifierEENSB_16MouseEventSourceE(
    QWindow *window,
    ulong timestamp,
    const QPointingDevice *device,
    const QPointF *local,
    const QPointF *global,
    int state,
    Qt::MouseButton button,
    QEvent::Type type,
    int mods,
    Qt::MouseEventSource source) {
  return QWindowSystemInterface::handleMouseEvent<
      QWindowSystemInterface::DefaultDelivery>(
      window,
      timestamp,
      device,
      *local,
      *global,
      QFlags<Qt::MouseButton>::fromInt(state),
      button,
      type,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      source);
}

//  static bool QWindowSystemInterface::handleMouseEvent<
//      QWindowSystemInterface::DefaultDelivery>(QWindow *window, ulong
//      timestamp, const QPointF &local, const QPointF &global,
//      Qt::MouseButtons state, Qt::MouseButton button, QEvent::Type type,
//      Qt::KeyboardModifiers mods, Qt::MouseEventSource source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface16handleMouseEventINS_15DefaultDeliveryEEEbP7QWindowmRK7QPointFS6_6QFlagsIN2Qt11MouseButtonEES9_N6QEvent4TypeES7_INS8_16KeyboardModifierEENS8_16MouseEventSourceE(
    QWindow *window,
    ulong timestamp,
    const QPointF *local,
    const QPointF *global,
    int state,
    Qt::MouseButton button,
    QEvent::Type type,
    int mods,
    Qt::MouseEventSource source) {
  return QWindowSystemInterface::handleMouseEvent<
      QWindowSystemInterface::DefaultDelivery>(
      window,
      timestamp,
      *local,
      *global,
      QFlags<Qt::MouseButton>::fromInt(state),
      button,
      type,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      source);
}

//  static bool QWindowSystemInterface::handleMouseEvent<
//      QWindowSystemInterface::DefaultDelivery>(QWindow *window, const
//      QPointingDevice *device, const QPointF &local, const QPointF &global,
//      Qt::MouseButtons state, Qt::MouseButton button, QEvent::Type type,
//      Qt::KeyboardModifiers mods, Qt::MouseEventSource source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface16handleMouseEventINS_15DefaultDeliveryEEEbP7QWindowPK15QPointingDeviceRK7QPointFS9_6QFlagsIN2Qt11MouseButtonEESC_N6QEvent4TypeESA_INSB_16KeyboardModifierEENSB_16MouseEventSourceE(
    QWindow *window,
    const QPointingDevice *device,
    const QPointF *local,
    const QPointF *global,
    int state,
    Qt::MouseButton button,
    QEvent::Type type,
    int mods,
    Qt::MouseEventSource source) {
  return QWindowSystemInterface::handleMouseEvent<
      QWindowSystemInterface::DefaultDelivery>(
      window,
      device,
      *local,
      *global,
      QFlags<Qt::MouseButton>::fromInt(state),
      button,
      type,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      source);
}

//  static bool QWindowSystemInterface::handleMouseEvent<
//      QWindowSystemInterface::DefaultDelivery>(QWindow *window, const
//      QPointF &local, const QPointF &global, Qt::MouseButtons state,
//      Qt::MouseButton button, QEvent::Type type, Qt::KeyboardModifiers
//      mods, Qt::MouseEventSource source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface16handleMouseEventINS_15DefaultDeliveryEEEbP7QWindowRK7QPointFS6_6QFlagsIN2Qt11MouseButtonEES9_N6QEvent4TypeES7_INS8_16KeyboardModifierEENS8_16MouseEventSourceE(
    QWindow *window,
    const QPointF *local,
    const QPointF *global,
    int state,
    Qt::MouseButton button,
    QEvent::Type type,
    int mods,
    Qt::MouseEventSource source) {
  return QWindowSystemInterface::handleMouseEvent<
      QWindowSystemInterface::DefaultDelivery>(
      window,
      *local,
      *global,
      QFlags<Qt::MouseButton>::fromInt(state),
      button,
      type,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      source);
}

//  static bool QWindowSystemInterface::handleMouseEvent<
//      QWindowSystemInterface::SynchronousDelivery>(QWindow *window, ulong
//      timestamp, const QPointingDevice *device, const QPointF &local, const
//      QPointF &global, Qt::MouseButtons state, Qt::MouseButton button,
//      QEvent::Type type, Qt::KeyboardModifiers mods, Qt::MouseEventSource
//      source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface16handleMouseEventINS_19SynchronousDeliveryEEEbP7QWindowmPK15QPointingDeviceRK7QPointFS9_6QFlagsIN2Qt11MouseButtonEESC_N6QEvent4TypeESA_INSB_16KeyboardModifierEENSB_16MouseEventSourceE(
    QWindow *window,
    ulong timestamp,
    const QPointingDevice *device,
    const QPointF *local,
    const QPointF *global,
    int state,
    Qt::MouseButton button,
    QEvent::Type type,
    int mods,
    Qt::MouseEventSource source) {
  return QWindowSystemInterface::handleMouseEvent<
      QWindowSystemInterface::SynchronousDelivery>(
      window,
      timestamp,
      device,
      *local,
      *global,
      QFlags<Qt::MouseButton>::fromInt(state),
      button,
      type,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      source);
}

//  static bool QWindowSystemInterface::handleMouseEvent<
//      QWindowSystemInterface::SynchronousDelivery>(QWindow *window, ulong
//      timestamp, const QPointF &local, const QPointF &global,
//      Qt::MouseButtons state, Qt::MouseButton button, QEvent::Type type,
//      Qt::KeyboardModifiers mods, Qt::MouseEventSource source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface16handleMouseEventINS_19SynchronousDeliveryEEEbP7QWindowmRK7QPointFS6_6QFlagsIN2Qt11MouseButtonEES9_N6QEvent4TypeES7_INS8_16KeyboardModifierEENS8_16MouseEventSourceE(
    QWindow *window,
    ulong timestamp,
    const QPointF *local,
    const QPointF *global,
    int state,
    Qt::MouseButton button,
    QEvent::Type type,
    int mods,
    Qt::MouseEventSource source) {
  return QWindowSystemInterface::handleMouseEvent<
      QWindowSystemInterface::SynchronousDelivery>(
      window,
      timestamp,
      *local,
      *global,
      QFlags<Qt::MouseButton>::fromInt(state),
      button,
      type,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      source);
}

//  static bool QWindowSystemInterface::handleMouseEvent<
//      QWindowSystemInterface::SynchronousDelivery>(QWindow *window, const
//      QPointingDevice *device, const QPointF &local, const QPointF &global,
//      Qt::MouseButtons state, Qt::MouseButton button, QEvent::Type type,
//      Qt::KeyboardModifiers mods, Qt::MouseEventSource source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface16handleMouseEventINS_19SynchronousDeliveryEEEbP7QWindowPK15QPointingDeviceRK7QPointFS9_6QFlagsIN2Qt11MouseButtonEESC_N6QEvent4TypeESA_INSB_16KeyboardModifierEENSB_16MouseEventSourceE(
    QWindow *window,
    const QPointingDevice *device,
    const QPointF *local,
    const QPointF *global,
    int state,
    Qt::MouseButton button,
    QEvent::Type type,
    int mods,
    Qt::MouseEventSource source) {
  return QWindowSystemInterface::handleMouseEvent<
      QWindowSystemInterface::SynchronousDelivery>(
      window,
      device,
      *local,
      *global,
      QFlags<Qt::MouseButton>::fromInt(state),
      button,
      type,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      source);
}

//  static bool QWindowSystemInterface::handleMouseEvent<
//      QWindowSystemInterface::SynchronousDelivery>(QWindow *window, const
//      QPointF &local, const QPointF &global, Qt::MouseButtons state,
//      Qt::MouseButton button, QEvent::Type type, Qt::KeyboardModifiers
//      mods, Qt::MouseEventSource source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface16handleMouseEventINS_19SynchronousDeliveryEEEbP7QWindowRK7QPointFS6_6QFlagsIN2Qt11MouseButtonEES9_N6QEvent4TypeES7_INS8_16KeyboardModifierEENS8_16MouseEventSourceE(
    QWindow *window,
    const QPointF *local,
    const QPointF *global,
    int state,
    Qt::MouseButton button,
    QEvent::Type type,
    int mods,
    Qt::MouseEventSource source) {
  return QWindowSystemInterface::handleMouseEvent<
      QWindowSystemInterface::SynchronousDelivery>(
      window,
      *local,
      *global,
      QFlags<Qt::MouseButton>::fromInt(state),
      button,
      type,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      source);
}

//  static bool QWindowSystemInterface::handleMouseEvent<
//      QWindowSystemInterface::AsynchronousDelivery>(QWindow *window, ulong
//      timestamp, const QPointingDevice *device, const QPointF &local, const
//      QPointF &global, Qt::MouseButtons state, Qt::MouseButton button,
//      QEvent::Type type, Qt::KeyboardModifiers mods, Qt::MouseEventSource
//      source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface16handleMouseEventINS_20AsynchronousDeliveryEEEbP7QWindowmPK15QPointingDeviceRK7QPointFS9_6QFlagsIN2Qt11MouseButtonEESC_N6QEvent4TypeESA_INSB_16KeyboardModifierEENSB_16MouseEventSourceE(
    QWindow *window,
    ulong timestamp,
    const QPointingDevice *device,
    const QPointF *local,
    const QPointF *global,
    int state,
    Qt::MouseButton button,
    QEvent::Type type,
    int mods,
    Qt::MouseEventSource source) {
  return QWindowSystemInterface::handleMouseEvent<
      QWindowSystemInterface::AsynchronousDelivery>(
      window,
      timestamp,
      device,
      *local,
      *global,
      QFlags<Qt::MouseButton>::fromInt(state),
      button,
      type,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      source);
}

//  static bool QWindowSystemInterface::handleMouseEvent<
//      QWindowSystemInterface::AsynchronousDelivery>(QWindow *window, ulong
//      timestamp, const QPointF &local, const QPointF &global,
//      Qt::MouseButtons state, Qt::MouseButton button, QEvent::Type type,
//      Qt::KeyboardModifiers mods, Qt::MouseEventSource source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface16handleMouseEventINS_20AsynchronousDeliveryEEEbP7QWindowmRK7QPointFS6_6QFlagsIN2Qt11MouseButtonEES9_N6QEvent4TypeES7_INS8_16KeyboardModifierEENS8_16MouseEventSourceE(
    QWindow *window,
    ulong timestamp,
    const QPointF *local,
    const QPointF *global,
    int state,
    Qt::MouseButton button,
    QEvent::Type type,
    int mods,
    Qt::MouseEventSource source) {
  return QWindowSystemInterface::handleMouseEvent<
      QWindowSystemInterface::AsynchronousDelivery>(
      window,
      timestamp,
      *local,
      *global,
      QFlags<Qt::MouseButton>::fromInt(state),
      button,
      type,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      source);
}

//  static bool QWindowSystemInterface::handleMouseEvent<
//      QWindowSystemInterface::AsynchronousDelivery>(QWindow *window, const
//      QPointingDevice *device, const QPointF &local, const QPointF &global,
//      Qt::MouseButtons state, Qt::MouseButton button, QEvent::Type type,
//      Qt::KeyboardModifiers mods, Qt::MouseEventSource source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface16handleMouseEventINS_20AsynchronousDeliveryEEEbP7QWindowPK15QPointingDeviceRK7QPointFS9_6QFlagsIN2Qt11MouseButtonEESC_N6QEvent4TypeESA_INSB_16KeyboardModifierEENSB_16MouseEventSourceE(
    QWindow *window,
    const QPointingDevice *device,
    const QPointF *local,
    const QPointF *global,
    int state,
    Qt::MouseButton button,
    QEvent::Type type,
    int mods,
    Qt::MouseEventSource source) {
  return QWindowSystemInterface::handleMouseEvent<
      QWindowSystemInterface::AsynchronousDelivery>(
      window,
      device,
      *local,
      *global,
      QFlags<Qt::MouseButton>::fromInt(state),
      button,
      type,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      source);
}

//  static bool QWindowSystemInterface::handleMouseEvent<
//      QWindowSystemInterface::AsynchronousDelivery>(QWindow *window, const
//      QPointF &local, const QPointF &global, Qt::MouseButtons state,
//      Qt::MouseButton button, QEvent::Type type, Qt::KeyboardModifiers
//      mods, Qt::MouseEventSource source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface16handleMouseEventINS_20AsynchronousDeliveryEEEbP7QWindowRK7QPointFS6_6QFlagsIN2Qt11MouseButtonEES9_N6QEvent4TypeES7_INS8_16KeyboardModifierEENS8_16MouseEventSourceE(
    QWindow *window,
    const QPointF *local,
    const QPointF *global,
    int state,
    Qt::MouseButton button,
    QEvent::Type type,
    int mods,
    Qt::MouseEventSource source) {
  return QWindowSystemInterface::handleMouseEvent<
      QWindowSystemInterface::AsynchronousDelivery>(
      window,
      *local,
      *global,
      QFlags<Qt::MouseButton>::fromInt(state),
      button,
      type,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      source);
}

//  static bool QWindowSystemInterface::handlePaintEvent<
//      QWindowSystemInterface::DefaultDelivery>(QWindow *window, const
//      QRegion &region)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface16handlePaintEventINS_15DefaultDeliveryEEEbP7QWindowRK7QRegion(
    QWindow *window,
    const QRegion *region) {
  return QWindowSystemInterface::handlePaintEvent<
      QWindowSystemInterface::DefaultDelivery>(
      window,
      *region);
}

//  static bool QWindowSystemInterface::handlePaintEvent<
//      QWindowSystemInterface::SynchronousDelivery>(QWindow *window, const
//      QRegion &region)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface16handlePaintEventINS_19SynchronousDeliveryEEEbP7QWindowRK7QRegion(
    QWindow *window,
    const QRegion *region) {
  return QWindowSystemInterface::handlePaintEvent<
      QWindowSystemInterface::SynchronousDelivery>(
      window,
      *region);
}

//  static bool QWindowSystemInterface::handlePaintEvent<
//      QWindowSystemInterface::AsynchronousDelivery>(QWindow *window, const
//      QRegion &region)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface16handlePaintEventINS_20AsynchronousDeliveryEEEbP7QWindowRK7QRegion(
    QWindow *window,
    const QRegion *region) {
  return QWindowSystemInterface::handlePaintEvent<
      QWindowSystemInterface::AsynchronousDelivery>(
      window,
      *region);
}

//  static void QWindowSystemInterface::handleSafeAreaMarginsChanged<
//      QWindowSystemInterface::DefaultDelivery>(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface28handleSafeAreaMarginsChangedINS_15DefaultDeliveryEEEvP7QWindow(
    QWindow *window) {
  QWindowSystemInterface::handleSafeAreaMarginsChanged<
      QWindowSystemInterface::DefaultDelivery>(
      window);
}

//  static void QWindowSystemInterface::handleSafeAreaMarginsChanged<
//      QWindowSystemInterface::SynchronousDelivery>(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface28handleSafeAreaMarginsChangedINS_19SynchronousDeliveryEEEvP7QWindow(
    QWindow *window) {
  QWindowSystemInterface::handleSafeAreaMarginsChanged<
      QWindowSystemInterface::SynchronousDelivery>(
      window);
}

//  static void QWindowSystemInterface::handleSafeAreaMarginsChanged<
//      QWindowSystemInterface::AsynchronousDelivery>(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface28handleSafeAreaMarginsChangedINS_20AsynchronousDeliveryEEEvP7QWindow(
    QWindow *window) {
  QWindowSystemInterface::handleSafeAreaMarginsChanged<
      QWindowSystemInterface::AsynchronousDelivery>(
      window);
}

//  static void QWindowSystemInterface::handleThemeChange<
//      QWindowSystemInterface::DefaultDelivery>()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface17handleThemeChangeINS_15DefaultDeliveryEEEvv() {
  QWindowSystemInterface::handleThemeChange<
      QWindowSystemInterface::DefaultDelivery>();
}

//  static void QWindowSystemInterface::handleThemeChange<
//      QWindowSystemInterface::SynchronousDelivery>()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface17handleThemeChangeINS_19SynchronousDeliveryEEEvv() {
  QWindowSystemInterface::handleThemeChange<
      QWindowSystemInterface::SynchronousDelivery>();
}

//  static void QWindowSystemInterface::handleThemeChange<
//      QWindowSystemInterface::AsynchronousDelivery>()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface17handleThemeChangeINS_20AsynchronousDeliveryEEEvv() {
  QWindowSystemInterface::handleThemeChange<
      QWindowSystemInterface::AsynchronousDelivery>();
}

//  static bool QWindowSystemInterface::handleTouchCancelEvent<
//      QWindowSystemInterface::DefaultDelivery>(QWindow *window, ulong
//      timestamp, const QPointingDevice *device, Qt::KeyboardModifiers mods)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface22handleTouchCancelEventINS_15DefaultDeliveryEEEbP7QWindowmPK15QPointingDevice6QFlagsIN2Qt16KeyboardModifierEE(
    QWindow *window,
    ulong timestamp,
    const QPointingDevice *device,
    int mods) {
  return QWindowSystemInterface::handleTouchCancelEvent<
      QWindowSystemInterface::DefaultDelivery>(
      window,
      timestamp,
      device,
      QFlags<Qt::KeyboardModifier>::fromInt(mods));
}

//  static bool QWindowSystemInterface::handleTouchCancelEvent<
//      QWindowSystemInterface::DefaultDelivery>(QWindow *window, const
//      QPointingDevice *device, Qt::KeyboardModifiers mods)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface22handleTouchCancelEventINS_15DefaultDeliveryEEEbP7QWindowPK15QPointingDevice6QFlagsIN2Qt16KeyboardModifierEE(
    QWindow *window,
    const QPointingDevice *device,
    int mods) {
  return QWindowSystemInterface::handleTouchCancelEvent<
      QWindowSystemInterface::DefaultDelivery>(
      window,
      device,
      QFlags<Qt::KeyboardModifier>::fromInt(mods));
}

//  static bool QWindowSystemInterface::handleTouchCancelEvent<
//      QWindowSystemInterface::SynchronousDelivery>(QWindow *window, ulong
//      timestamp, const QPointingDevice *device, Qt::KeyboardModifiers mods)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface22handleTouchCancelEventINS_19SynchronousDeliveryEEEbP7QWindowmPK15QPointingDevice6QFlagsIN2Qt16KeyboardModifierEE(
    QWindow *window,
    ulong timestamp,
    const QPointingDevice *device,
    int mods) {
  return QWindowSystemInterface::handleTouchCancelEvent<
      QWindowSystemInterface::SynchronousDelivery>(
      window,
      timestamp,
      device,
      QFlags<Qt::KeyboardModifier>::fromInt(mods));
}

//  static bool QWindowSystemInterface::handleTouchCancelEvent<
//      QWindowSystemInterface::SynchronousDelivery>(QWindow *window, const
//      QPointingDevice *device, Qt::KeyboardModifiers mods)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface22handleTouchCancelEventINS_19SynchronousDeliveryEEEbP7QWindowPK15QPointingDevice6QFlagsIN2Qt16KeyboardModifierEE(
    QWindow *window,
    const QPointingDevice *device,
    int mods) {
  return QWindowSystemInterface::handleTouchCancelEvent<
      QWindowSystemInterface::SynchronousDelivery>(
      window,
      device,
      QFlags<Qt::KeyboardModifier>::fromInt(mods));
}

//  static bool QWindowSystemInterface::handleTouchCancelEvent<
//      QWindowSystemInterface::AsynchronousDelivery>(QWindow *window, ulong
//      timestamp, const QPointingDevice *device, Qt::KeyboardModifiers mods)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface22handleTouchCancelEventINS_20AsynchronousDeliveryEEEbP7QWindowmPK15QPointingDevice6QFlagsIN2Qt16KeyboardModifierEE(
    QWindow *window,
    ulong timestamp,
    const QPointingDevice *device,
    int mods) {
  return QWindowSystemInterface::handleTouchCancelEvent<
      QWindowSystemInterface::AsynchronousDelivery>(
      window,
      timestamp,
      device,
      QFlags<Qt::KeyboardModifier>::fromInt(mods));
}

//  static bool QWindowSystemInterface::handleTouchCancelEvent<
//      QWindowSystemInterface::AsynchronousDelivery>(QWindow *window, const
//      QPointingDevice *device, Qt::KeyboardModifiers mods)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QWindowSystemInterface22handleTouchCancelEventINS_20AsynchronousDeliveryEEEbP7QWindowPK15QPointingDevice6QFlagsIN2Qt16KeyboardModifierEE(
    QWindow *window,
    const QPointingDevice *device,
    int mods) {
  return QWindowSystemInterface::handleTouchCancelEvent<
      QWindowSystemInterface::AsynchronousDelivery>(
      window,
      device,
      QFlags<Qt::KeyboardModifier>::fromInt(mods));
}

//  static void QWindowSystemInterface::handleWindowDevicePixelRatioChanged<
//      QWindowSystemInterface::DefaultDelivery>(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface35handleWindowDevicePixelRatioChangedINS_15DefaultDeliveryEEEvP7QWindow(
    QWindow *window) {
  QWindowSystemInterface::handleWindowDevicePixelRatioChanged<
      QWindowSystemInterface::DefaultDelivery>(
      window);
}

//  static void QWindowSystemInterface::handleWindowDevicePixelRatioChanged<
//      QWindowSystemInterface::SynchronousDelivery>(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface35handleWindowDevicePixelRatioChangedINS_19SynchronousDeliveryEEEvP7QWindow(
    QWindow *window) {
  QWindowSystemInterface::handleWindowDevicePixelRatioChanged<
      QWindowSystemInterface::SynchronousDelivery>(
      window);
}

//  static void QWindowSystemInterface::handleWindowDevicePixelRatioChanged<
//      QWindowSystemInterface::AsynchronousDelivery>(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface35handleWindowDevicePixelRatioChangedINS_20AsynchronousDeliveryEEEvP7QWindow(
    QWindow *window) {
  QWindowSystemInterface::handleWindowDevicePixelRatioChanged<
      QWindowSystemInterface::AsynchronousDelivery>(
      window);
}

//  static void QWindowSystemInterface::handleWindowScreenChanged<
//      QWindowSystemInterface::DefaultDelivery>(QWindow *window, QScreen
//      *newScreen)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface25handleWindowScreenChangedINS_15DefaultDeliveryEEEvP7QWindowP7QScreen(
    QWindow *window,
    QScreen *newScreen) {
  QWindowSystemInterface::handleWindowScreenChanged<
      QWindowSystemInterface::DefaultDelivery>(
      window,
      newScreen);
}

//  static void QWindowSystemInterface::handleWindowScreenChanged<
//      QWindowSystemInterface::SynchronousDelivery>(QWindow *window, QScreen
//      *newScreen)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface25handleWindowScreenChangedINS_19SynchronousDeliveryEEEvP7QWindowP7QScreen(
    QWindow *window,
    QScreen *newScreen) {
  QWindowSystemInterface::handleWindowScreenChanged<
      QWindowSystemInterface::SynchronousDelivery>(
      window,
      newScreen);
}

//  static void QWindowSystemInterface::handleWindowScreenChanged<
//      QWindowSystemInterface::AsynchronousDelivery>(QWindow *window,
//      QScreen *newScreen)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface25handleWindowScreenChangedINS_20AsynchronousDeliveryEEEvP7QWindowP7QScreen(
    QWindow *window,
    QScreen *newScreen) {
  QWindowSystemInterface::handleWindowScreenChanged<
      QWindowSystemInterface::AsynchronousDelivery>(
      window,
      newScreen);
}

//  static void QWindowSystemInterface::handleWindowStateChanged<
//      QWindowSystemInterface::DefaultDelivery>(QWindow *window,
//      Qt::WindowStates newState, int oldState)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface24handleWindowStateChangedINS_15DefaultDeliveryEEEvP7QWindow6QFlagsIN2Qt11WindowStateEEi(
    QWindow *window,
    int newState,
    int oldState) {
  QWindowSystemInterface::handleWindowStateChanged<
      QWindowSystemInterface::DefaultDelivery>(
      window,
      QFlags<Qt::WindowState>::fromInt(newState),
      oldState);
}

//  static void QWindowSystemInterface::handleWindowStateChanged<
//      QWindowSystemInterface::SynchronousDelivery>(QWindow *window,
//      Qt::WindowStates newState, int oldState)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface24handleWindowStateChangedINS_19SynchronousDeliveryEEEvP7QWindow6QFlagsIN2Qt11WindowStateEEi(
    QWindow *window,
    int newState,
    int oldState) {
  QWindowSystemInterface::handleWindowStateChanged<
      QWindowSystemInterface::SynchronousDelivery>(
      window,
      QFlags<Qt::WindowState>::fromInt(newState),
      oldState);
}

//  static void QWindowSystemInterface::handleWindowStateChanged<
//      QWindowSystemInterface::AsynchronousDelivery>(QWindow *window,
//      Qt::WindowStates newState, int oldState)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface24handleWindowStateChangedINS_20AsynchronousDeliveryEEEvP7QWindow6QFlagsIN2Qt11WindowStateEEi(
    QWindow *window,
    int newState,
    int oldState) {
  QWindowSystemInterface::handleWindowStateChanged<
      QWindowSystemInterface::AsynchronousDelivery>(
      window,
      QFlags<Qt::WindowState>::fromInt(newState),
      oldState);
}
