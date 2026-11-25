//  Written by hand on 2026-11-25 from
//  QtQuickControls2IOSStyleImpl/6.12.0/QtQuickControls2IOSStyleImpl/private/
//  qquickioscursorflashtimer_p.h, Qt 6.12.0, from Qt's source. Kept
//  as it is when the generator runs again.
//  Qt builds this part only with its feature 'quickcontrols2-ios',
//  for macOS and iOS. Qt's library offers nothing of this class by
//  name: only its virtual functions are called, through the object,
//  and the destructor C++ writes for it, virtual through QObject,
//  through 'delete'.
//  Not written: the constructor, 'tr' and the other functions, which
//  are defined outside the header; the signals.
#include <QtCore/qglobal.h>
#include <QtQuickControls2/6.12.0/QtQuickControls2/private/qtquickcontrols2-config_p.h>
#if QT_CONFIG(quickcontrols2_ios)
#include <QtQuickControls2IOSStyleImpl/qtquickcontrols2iosstyleimplexports.h>
#include <QtQuickControls2IOSStyleImpl/6.12.0/QtQuickControls2IOSStyleImpl/private/qquickioscursorflashtimer_p.h>

//  const QMetaObject *QQuickIOSCursorFlashTimer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuickIOSCursorFlashTimer10metaObjectEv(
    const QQuickIOSCursorFlashTimer *self) {
  return self->metaObject();
}

//  QQuickIOSCursorFlashTimer::~QQuickIOSCursorFlashTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickIOSCursorFlashTimerD1Ev(
    QQuickIOSCursorFlashTimer *self) {
  delete self;
}

//  void QQuickIOSCursorFlashTimer::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickIOSCursorFlashTimer10timerEventEP11QTimerEvent(
    QQuickIOSCursorFlashTimer *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

#endif  // QT_CONFIG(quickcontrols2_ios)
