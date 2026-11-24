//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qguiapplication_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qguiapplication_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformdrag.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpixmap.h>
#include <QtGui/qpalette.h>
#include <cstring>

//  Only a class built on QGuiApplicationPrivate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGuiApplicationPrivate : QGuiApplicationPrivate {
  using QGuiApplicationPrivate::handleThemeChanged;
  using QGuiApplicationPrivate::basePalette;
  using QGuiApplicationPrivate::notifyDragStarted;
};

//  A QGuiApplicationPrivate that Python can take functions over in. Every QGuiApplicationPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGuiApplicationPrivateCall0)(const void *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGuiApplicationPrivateCall1)(const void *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQGuiApplicationPrivateCall2)(const void *, int *);
typedef void (*CuteQGuiApplicationPrivateCall3)(const void *, QWindow *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGuiApplicationPrivateCall4)(const void *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGuiApplicationPrivateCall5)(const void *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQGuiApplicationPrivateCall6)(const void *, int *);
typedef bool (*CuteQGuiApplicationPrivateCall7)(const void *, QWindow *, int *);
typedef const QPixmap * (*CuteQGuiApplicationPrivateCall8)(const void *, int, const QPixmap *, int *);
typedef void (*CuteQGuiApplicationPrivateCall9)(const void *, int *);
#if !defined(QT_NO_ACTION)
typedef void * (*CuteQGuiApplicationPrivateCall10)(const void *, int *);
#endif  // !defined(QT_NO_ACTION)
#if !defined(QT_NO_SHORTCUT)
typedef void * (*CuteQGuiApplicationPrivateCall11)(const void *, int *);
#endif  // !defined(QT_NO_SHORTCUT)
typedef void (*CuteQGuiApplicationPrivateCall12)(const void *, int *);
typedef const QPalette * (*CuteQGuiApplicationPrivateCall13)(const void *, int *);
#if QT_CONFIG(draganddrop)
typedef void (*CuteQGuiApplicationPrivateCall14)(const void *, const QDrag *, int *);
#endif  // QT_CONFIG(draganddrop)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGuiApplicationPrivateCall15)(const void *, QEvent *, QObject *, QPostEventList *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGuiApplicationPrivate : public QGuiApplicationPrivate {
public:
  using QGuiApplicationPrivate::QGuiApplicationPrivate;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN23QCoreApplicationPrivate21createEventDispatcherEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN23QCoreApplicationPrivate20eventDispatcherReadyEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN22QGuiApplicationPrivate27notifyLayoutDirectionChangeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QGuiApplicationPrivate24notifyActiveWindowChangeEP7QWindow")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN23QCoreApplicationPrivate20canQuitAutomaticallyEv")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN23QCoreApplicationPrivate4quitEv")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK22QGuiApplicationPrivate15defaultModalityEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QGuiApplicationPrivate18windowNeverBlockedEP7QWindow")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QGuiApplicationPrivate21applyQIconStyleHelperEN5QIcon4ModeERK7QPixmap")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QGuiApplicationPrivate23notifyWindowIconChangedEv")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZNK22QGuiApplicationPrivate19createActionPrivateEv")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if !defined(QT_NO_SHORTCUT)
    if (!std::strcmp(key, "_ZNK22QGuiApplicationPrivate21createShortcutPrivateEv")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_SHORTCUT)
    if (!std::strcmp(key, "_ZN22QGuiApplicationPrivate18handleThemeChangedEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QGuiApplicationPrivate11basePaletteEv")) {
      taken[13] = call;
      return true;
    }
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN22QGuiApplicationPrivate17notifyDragStartedEPK5QDrag")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN23QCoreApplicationPrivate13compressEventEP6QEventP7QObjectP14QPostEventList")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  void QGuiApplicationPrivate::createEventDispatcher()
  void createEventDispatcher() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGuiApplicationPrivateCall0 call = reinterpret_cast<CuteQGuiApplicationPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGuiApplicationPrivate::createEventDispatcher();
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QGuiApplicationPrivate::eventDispatcherReady()
  void eventDispatcherReady() override {
    if (taken[1]) {
      int handled = 0;
      CuteQGuiApplicationPrivateCall1 call = reinterpret_cast<CuteQGuiApplicationPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QGuiApplicationPrivate::eventDispatcherReady();
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QGuiApplicationPrivate::notifyLayoutDirectionChange()
  void notifyLayoutDirectionChange() override {
    if (taken[2]) {
      int handled = 0;
      CuteQGuiApplicationPrivateCall2 call = reinterpret_cast<CuteQGuiApplicationPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QGuiApplicationPrivate::notifyLayoutDirectionChange();
  }

  //  void QGuiApplicationPrivate::notifyActiveWindowChange(QWindow
  //      *previous)
  void notifyActiveWindowChange(QWindow *previous) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGuiApplicationPrivateCall3 call = reinterpret_cast<CuteQGuiApplicationPrivateCall3>(taken[3]);
      call(this, previous, &handled);
      if (handled) return;
    }
    QGuiApplicationPrivate::notifyActiveWindowChange(previous);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QGuiApplicationPrivate::canQuitAutomatically()
  bool canQuitAutomatically() override {
    if (taken[4]) {
      int handled = 0;
      CuteQGuiApplicationPrivateCall4 call = reinterpret_cast<CuteQGuiApplicationPrivateCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGuiApplicationPrivate::canQuitAutomatically();
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QGuiApplicationPrivate::quit()
  void quit() override {
    if (taken[5]) {
      int handled = 0;
      CuteQGuiApplicationPrivateCall5 call = reinterpret_cast<CuteQGuiApplicationPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QGuiApplicationPrivate::quit();
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  Qt::WindowModality QGuiApplicationPrivate::defaultModality() const
  Qt::WindowModality defaultModality() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGuiApplicationPrivateCall6 call = reinterpret_cast<CuteQGuiApplicationPrivateCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::WindowModality>(given);
    }
    return QGuiApplicationPrivate::defaultModality();
  }

  //  bool QGuiApplicationPrivate::windowNeverBlocked(QWindow *window)
  //      const
  bool windowNeverBlocked(QWindow *window) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQGuiApplicationPrivateCall7 call = reinterpret_cast<CuteQGuiApplicationPrivateCall7>(taken[7]);
      bool given = call(this, window, &handled);
      if (handled) return given;
    }
    return QGuiApplicationPrivate::windowNeverBlocked(window);
  }

  //  QPixmap QGuiApplicationPrivate::applyQIconStyleHelper(QIcon::Mode a0,
  //      const QPixmap &basePixmap) const
  QPixmap applyQIconStyleHelper(
      QIcon::Mode a0,
      const QPixmap &basePixmap) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQGuiApplicationPrivateCall8 call = reinterpret_cast<CuteQGuiApplicationPrivateCall8>(taken[8]);
      const QPixmap * given = call(this, static_cast<int>(a0), &basePixmap, &handled);
      if (handled && given) return *given;
    }
    return QGuiApplicationPrivate::applyQIconStyleHelper(a0, basePixmap);
  }

  //  void QGuiApplicationPrivate::notifyWindowIconChanged()
  void notifyWindowIconChanged() override {
    if (taken[9]) {
      int handled = 0;
      CuteQGuiApplicationPrivateCall9 call = reinterpret_cast<CuteQGuiApplicationPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QGuiApplicationPrivate::notifyWindowIconChanged();
  }

#if !defined(QT_NO_ACTION)
  //  QActionPrivate *QGuiApplicationPrivate::createActionPrivate() const
  QActionPrivate *createActionPrivate() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQGuiApplicationPrivateCall10 call = reinterpret_cast<CuteQGuiApplicationPrivateCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QActionPrivate *>(given);
    }
    return QGuiApplicationPrivate::createActionPrivate();
  }
#endif  // !defined(QT_NO_ACTION)

#if !defined(QT_NO_SHORTCUT)
  //  QShortcutPrivate *QGuiApplicationPrivate::createShortcutPrivate()
  //      const
  QShortcutPrivate *createShortcutPrivate() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQGuiApplicationPrivateCall11 call = reinterpret_cast<CuteQGuiApplicationPrivateCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QShortcutPrivate *>(given);
    }
    return QGuiApplicationPrivate::createShortcutPrivate();
  }
#endif  // !defined(QT_NO_SHORTCUT)

  //  void QGuiApplicationPrivate::handleThemeChanged()
  void handleThemeChanged() override {
    if (taken[12]) {
      int handled = 0;
      CuteQGuiApplicationPrivateCall12 call = reinterpret_cast<CuteQGuiApplicationPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QGuiApplicationPrivate::handleThemeChanged();
  }

  //  QPalette QGuiApplicationPrivate::basePalette() const
  QPalette basePalette() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQGuiApplicationPrivateCall13 call = reinterpret_cast<CuteQGuiApplicationPrivateCall13>(taken[13]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGuiApplicationPrivate::basePalette();
  }

#if QT_CONFIG(draganddrop)
  //  void QGuiApplicationPrivate::notifyDragStarted(const QDrag *a0)
  void notifyDragStarted(const QDrag *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQGuiApplicationPrivateCall14 call = reinterpret_cast<CuteQGuiApplicationPrivateCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QGuiApplicationPrivate::notifyDragStarted(a0);
  }
#endif  // QT_CONFIG(draganddrop)

#if !defined(QT_NO_QOBJECT)
  //  bool QCoreApplicationPrivate::compressEvent(QEvent *event, QObject
  //      *receiver, QPostEventList *postedEvents)
  bool compressEvent(
      QEvent *event,
      QObject *receiver,
      QPostEventList *postedEvents) override {
    if (taken[15]) {
      int handled = 0;
      CuteQGuiApplicationPrivateCall15 call = reinterpret_cast<CuteQGuiApplicationPrivateCall15>(taken[15]);
      bool given = call(this, event, receiver, postedEvents, &handled);
      if (handled) return given;
    }
    return QCoreApplicationPrivate::compressEvent(event, receiver, postedEvents);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QGuiApplication *QGuiApplicationPrivate::q_func()
extern "C" Q_DECL_EXPORT
QGuiApplication *ritual_ZN22QGuiApplicationPrivate6q_funcEv(
    QGuiApplicationPrivate *self) {
  return self->q_func();
}

//  const QGuiApplication *QGuiApplicationPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGuiApplication *ritual_ZNK22QGuiApplicationPrivate6q_funcEv(
    const QGuiApplicationPrivate *self) {
  return self->q_func();
}

//  QGuiApplicationPrivate::QGuiApplicationPrivate(int &argc, char **argv)
extern "C" Q_DECL_EXPORT
QGuiApplicationPrivate *ritual_ZN22QGuiApplicationPrivateC1ERiPPc(
    int *argc,
    char **argv) {
  return new CuteQGuiApplicationPrivate(*argc, argv);
}

//  QGuiApplicationPrivate::~QGuiApplicationPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivateD1Ev(QGuiApplicationPrivate *self) {
  delete self;
}

//  void QGuiApplicationPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate4initEv(QGuiApplicationPrivate *self) {
  self->init();
}

//  void QGuiApplicationPrivate::createPlatformIntegration()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate25createPlatformIntegrationEv(
    QGuiApplicationPrivate *self) {
  self->createPlatformIntegration();
}

//  void QGuiApplicationPrivate::createEventDispatcher()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate21createEventDispatcherEv(
    QGuiApplicationPrivate *self) {
  self->createEventDispatcher();
}

//  void QGuiApplicationPrivate::eventDispatcherReady()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate20eventDispatcherReadyEv(
    QGuiApplicationPrivate *self) {
  self->eventDispatcherReady();
}

//  void QGuiApplicationPrivate::notifyLayoutDirectionChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate27notifyLayoutDirectionChangeEv(
    QGuiApplicationPrivate *self) {
  self->notifyLayoutDirectionChange();
}

//  void QGuiApplicationPrivate::notifyActiveWindowChange(QWindow *previous)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate24notifyActiveWindowChangeEP7QWindow(
    QGuiApplicationPrivate *self,
    QWindow *previous) {
  self->notifyActiveWindowChange(previous);
}

//  bool QGuiApplicationPrivate::canQuitAutomatically()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QGuiApplicationPrivate20canQuitAutomaticallyEv(
    QGuiApplicationPrivate *self) {
  return self->canQuitAutomatically();
}

//  void QGuiApplicationPrivate::quit()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate4quitEv(QGuiApplicationPrivate *self) {
  self->quit();
}

//  void QGuiApplicationPrivate::maybeLastWindowClosed()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate21maybeLastWindowClosedEv(
    QGuiApplicationPrivate *self) {
  self->maybeLastWindowClosed();
}

//  bool QGuiApplicationPrivate::lastWindowClosed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QGuiApplicationPrivate16lastWindowClosedEv(
    const QGuiApplicationPrivate *self) {
  return self->lastWindowClosed();
}

//  void QGuiApplicationPrivate::captureGlobalModifierState(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate26captureGlobalModifierStateEP6QEvent(
    QEvent *e) {
  QGuiApplicationPrivate::captureGlobalModifierState(e);
}

//  QPlatformIntegration *QGuiApplicationPrivate::platformIntegration()
extern "C" Q_DECL_EXPORT
QPlatformIntegration *ritual_ZN22QGuiApplicationPrivate19platformIntegrationEv() {
  return QGuiApplicationPrivate::platformIntegration();
}

//  QPlatformTheme *QGuiApplicationPrivate::platformTheme()
extern "C" Q_DECL_EXPORT
QPlatformTheme *ritual_ZN22QGuiApplicationPrivate13platformThemeEv() {
  return QGuiApplicationPrivate::platformTheme();
}

//  QAbstractEventDispatcher
//      *QGuiApplicationPrivate::qt_qpa_core_dispatcher()
extern "C" Q_DECL_EXPORT
QAbstractEventDispatcher *ritual_ZN22QGuiApplicationPrivate22qt_qpa_core_dispatcherEv() {
  return QGuiApplicationPrivate::qt_qpa_core_dispatcher();
}

//  void QGuiApplicationPrivate::processMouseEvent(QWindowSystemInterfacePriv
//      ate::MouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate17processMouseEventEPN29QWindowSystemInterfacePrivate10MouseEventE(
    QWindowSystemInterfacePrivate::MouseEvent *e) {
  QGuiApplicationPrivate::processMouseEvent(e);
}

//  void QGuiApplicationPrivate::processKeyEvent(QWindowSystemInterfacePrivat
//      e::KeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate15processKeyEventEPN29QWindowSystemInterfacePrivate8KeyEventE(
    QWindowSystemInterfacePrivate::KeyEvent *e) {
  QGuiApplicationPrivate::processKeyEvent(e);
}

//  void QGuiApplicationPrivate::processWheelEvent(QWindowSystemInterfacePriv
//      ate::WheelEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate17processWheelEventEPN29QWindowSystemInterfacePrivate10WheelEventE(
    QWindowSystemInterfacePrivate::WheelEvent *e) {
  QGuiApplicationPrivate::processWheelEvent(e);
}

//  void QGuiApplicationPrivate::processTouchEvent(QWindowSystemInterfacePriv
//      ate::TouchEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate17processTouchEventEPN29QWindowSystemInterfacePrivate10TouchEventE(
    QWindowSystemInterfacePrivate::TouchEvent *e) {
  QGuiApplicationPrivate::processTouchEvent(e);
}

//  void QGuiApplicationPrivate::processCloseEvent(QWindowSystemInterfacePriv
//      ate::CloseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate17processCloseEventEPN29QWindowSystemInterfacePrivate10CloseEventE(
    QWindowSystemInterfacePrivate::CloseEvent *e) {
  QGuiApplicationPrivate::processCloseEvent(e);
}

//  void QGuiApplicationPrivate::processGeometryChangeEvent(QWindowSystemInte
//      rfacePrivate::GeometryChangeEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate26processGeometryChangeEventEPN29QWindowSystemInterfacePrivate19GeometryChangeEventE(
    QWindowSystemInterfacePrivate::GeometryChangeEvent *e) {
  QGuiApplicationPrivate::processGeometryChangeEvent(e);
}

//  void QGuiApplicationPrivate::processEnterEvent(QWindowSystemInterfacePriv
//      ate::EnterEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate17processEnterEventEPN29QWindowSystemInterfacePrivate10EnterEventE(
    QWindowSystemInterfacePrivate::EnterEvent *e) {
  QGuiApplicationPrivate::processEnterEvent(e);
}

//  void QGuiApplicationPrivate::processLeaveEvent(QWindowSystemInterfacePriv
//      ate::LeaveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate17processLeaveEventEPN29QWindowSystemInterfacePrivate10LeaveEventE(
    QWindowSystemInterfacePrivate::LeaveEvent *e) {
  QGuiApplicationPrivate::processLeaveEvent(e);
}

//  void QGuiApplicationPrivate::processFocusWindowEvent(QWindowSystemInterfa
//      cePrivate::FocusWindowEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate23processFocusWindowEventEPN29QWindowSystemInterfacePrivate16FocusWindowEventE(
    QWindowSystemInterfacePrivate::FocusWindowEvent *e) {
  QGuiApplicationPrivate::processFocusWindowEvent(e);
}

//  void QGuiApplicationPrivate::processWindowStateChangedEvent(QWindowSystem
//      InterfacePrivate::WindowStateChangedEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate30processWindowStateChangedEventEPN29QWindowSystemInterfacePrivate23WindowStateChangedEventE(
    QWindowSystemInterfacePrivate::WindowStateChangedEvent *e) {
  QGuiApplicationPrivate::processWindowStateChangedEvent(e);
}

//  void QGuiApplicationPrivate::processWindowScreenChangedEvent(QWindowSyste
//      mInterfacePrivate::WindowScreenChangedEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate31processWindowScreenChangedEventEPN29QWindowSystemInterfacePrivate24WindowScreenChangedEventE(
    QWindowSystemInterfacePrivate::WindowScreenChangedEvent *e) {
  QGuiApplicationPrivate::processWindowScreenChangedEvent(e);
}

//  void QGuiApplicationPrivate::processWindowDevicePixelRatioChangedEvent(QW
//      indowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate41processWindowDevicePixelRatioChangedEventEPN29QWindowSystemInterfacePrivate34WindowDevicePixelRatioChangedEventE(
    QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent *e) {
  QGuiApplicationPrivate::processWindowDevicePixelRatioChangedEvent(e);
}

//  void QGuiApplicationPrivate::processSafeAreaMarginsChangedEvent(QWindowSy
//      stemInterfacePrivate::SafeAreaMarginsChangedEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate34processSafeAreaMarginsChangedEventEPN29QWindowSystemInterfacePrivate27SafeAreaMarginsChangedEventE(
    QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent *e) {
  QGuiApplicationPrivate::processSafeAreaMarginsChangedEvent(e);
}

//  void QGuiApplicationPrivate::processWindowSystemEvent(QWindowSystemInterf
//      acePrivate::WindowSystemEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate24processWindowSystemEventEPN29QWindowSystemInterfacePrivate17WindowSystemEventE(
    QWindowSystemInterfacePrivate::WindowSystemEvent *e) {
  QGuiApplicationPrivate::processWindowSystemEvent(e);
}

//  void QGuiApplicationPrivate::processApplicationTermination(QWindowSystemI
//      nterfacePrivate::WindowSystemEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate29processApplicationTerminationEPN29QWindowSystemInterfacePrivate17WindowSystemEventE(
    QWindowSystemInterfacePrivate::WindowSystemEvent *e) {
  QGuiApplicationPrivate::processApplicationTermination(e);
}

//  void QGuiApplicationPrivate::processScreenOrientationChange(QWindowSystem
//      InterfacePrivate::ScreenOrientationEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate30processScreenOrientationChangeEPN29QWindowSystemInterfacePrivate22ScreenOrientationEventE(
    QWindowSystemInterfacePrivate::ScreenOrientationEvent *e) {
  QGuiApplicationPrivate::processScreenOrientationChange(e);
}

//  void QGuiApplicationPrivate::processScreenGeometryChange(QWindowSystemInt
//      erfacePrivate::ScreenGeometryEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate27processScreenGeometryChangeEPN29QWindowSystemInterfacePrivate19ScreenGeometryEventE(
    QWindowSystemInterfacePrivate::ScreenGeometryEvent *e) {
  QGuiApplicationPrivate::processScreenGeometryChange(e);
}

//  void QGuiApplicationPrivate::processScreenLogicalDotsPerInchChange(QWindo
//      wSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate37processScreenLogicalDotsPerInchChangeEPN29QWindowSystemInterfacePrivate29ScreenLogicalDotsPerInchEventE(
    QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent *e) {
  QGuiApplicationPrivate::processScreenLogicalDotsPerInchChange(e);
}

//  void QGuiApplicationPrivate::processScreenRefreshRateChange(QWindowSystem
//      InterfacePrivate::ScreenRefreshRateEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate30processScreenRefreshRateChangeEPN29QWindowSystemInterfacePrivate22ScreenRefreshRateEventE(
    QWindowSystemInterfacePrivate::ScreenRefreshRateEvent *e) {
  QGuiApplicationPrivate::processScreenRefreshRateChange(e);
}

//  void QGuiApplicationPrivate::processThemeChanged(QWindowSystemInterfacePr
//      ivate::ThemeChangeEvent *tce)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate19processThemeChangedEPN29QWindowSystemInterfacePrivate16ThemeChangeEventE(
    QWindowSystemInterfacePrivate::ThemeChangeEvent *tce) {
  QGuiApplicationPrivate::processThemeChanged(tce);
}

//  void QGuiApplicationPrivate::processExposeEvent(QWindowSystemInterfacePri
//      vate::ExposeEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate18processExposeEventEPN29QWindowSystemInterfacePrivate11ExposeEventE(
    QWindowSystemInterfacePrivate::ExposeEvent *e) {
  QGuiApplicationPrivate::processExposeEvent(e);
}

//  void QGuiApplicationPrivate::processPaintEvent(QWindowSystemInterfacePriv
//      ate::PaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate17processPaintEventEPN29QWindowSystemInterfacePrivate10PaintEventE(
    QWindowSystemInterfacePrivate::PaintEvent *e) {
  QGuiApplicationPrivate::processPaintEvent(e);
}

//  void QGuiApplicationPrivate::processFileOpenEvent(QWindowSystemInterfaceP
//      rivate::FileOpenEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate20processFileOpenEventEPN29QWindowSystemInterfacePrivate13FileOpenEventE(
    QWindowSystemInterfacePrivate::FileOpenEvent *e) {
  QGuiApplicationPrivate::processFileOpenEvent(e);
}

//  void QGuiApplicationPrivate::processTabletEvent(QWindowSystemInterfacePri
//      vate::TabletEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate18processTabletEventEPN29QWindowSystemInterfacePrivate11TabletEventE(
    QWindowSystemInterfacePrivate::TabletEvent *e) {
  QGuiApplicationPrivate::processTabletEvent(e);
}

//  void QGuiApplicationPrivate::processTabletEnterProximityEvent(QWindowSyst
//      emInterfacePrivate::TabletEnterProximityEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate32processTabletEnterProximityEventEPN29QWindowSystemInterfacePrivate25TabletEnterProximityEventE(
    QWindowSystemInterfacePrivate::TabletEnterProximityEvent *e) {
  QGuiApplicationPrivate::processTabletEnterProximityEvent(e);
}

//  void QGuiApplicationPrivate::processTabletLeaveProximityEvent(QWindowSyst
//      emInterfacePrivate::TabletLeaveProximityEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate32processTabletLeaveProximityEventEPN29QWindowSystemInterfacePrivate25TabletLeaveProximityEventE(
    QWindowSystemInterfacePrivate::TabletLeaveProximityEvent *e) {
  QGuiApplicationPrivate::processTabletLeaveProximityEvent(e);
}

#if !defined(QT_NO_GESTURES)
//  void QGuiApplicationPrivate::processGestureEvent(QWindowSystemInterfacePr
//      ivate::GestureEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate19processGestureEventEPN29QWindowSystemInterfacePrivate12GestureEventE(
    QWindowSystemInterfacePrivate::GestureEvent *e) {
  QGuiApplicationPrivate::processGestureEvent(e);
}
#endif  // !defined(QT_NO_GESTURES)

//  void QGuiApplicationPrivate::processPlatformPanelEvent(QWindowSystemInter
//      facePrivate::PlatformPanelEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate25processPlatformPanelEventEPN29QWindowSystemInterfacePrivate18PlatformPanelEventE(
    QWindowSystemInterfacePrivate::PlatformPanelEvent *e) {
  QGuiApplicationPrivate::processPlatformPanelEvent(e);
}

#if !defined(QT_NO_CONTEXTMENU)
//  void QGuiApplicationPrivate::processContextMenuEvent(QWindowSystemInterfa
//      cePrivate::ContextMenuEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate23processContextMenuEventEPN29QWindowSystemInterfacePrivate16ContextMenuEventE(
    QWindowSystemInterfacePrivate::ContextMenuEvent *e) {
  QGuiApplicationPrivate::processContextMenuEvent(e);
}
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(draganddrop)
//  QPlatformDragQtResponse QGuiApplicationPrivate::processDrag(QWindow *w,
//      const QMimeData *dropData, const QPoint &p, Qt::DropActions
//      supportedActions, Qt::MouseButtons buttons, Qt::KeyboardModifiers
//      modifiers)
extern "C" Q_DECL_EXPORT
QPlatformDragQtResponse *ritual_ZN22QGuiApplicationPrivate11processDragEP7QWindowPK9QMimeDataRK6QPoint6QFlagsIN2Qt10DropActionEES8_INS9_11MouseButtonEES8_INS9_16KeyboardModifierEE(
    QWindow *w,
    const QMimeData *dropData,
    const QPoint *p,
    int supportedActions,
    int buttons,
    int modifiers) {
  return new QPlatformDragQtResponse(
      QGuiApplicationPrivate::processDrag(
          w,
          dropData,
          *p,
          QFlags<Qt::DropAction>::fromInt(supportedActions),
          QFlags<Qt::MouseButton>::fromInt(buttons),
          QFlags<Qt::KeyboardModifier>::fromInt(modifiers)));
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  QPlatformDropQtResponse QGuiApplicationPrivate::processDrop(QWindow *w,
//      const QMimeData *dropData, const QPoint &p, Qt::DropActions
//      supportedActions, Qt::MouseButtons buttons, Qt::KeyboardModifiers
//      modifiers)
extern "C" Q_DECL_EXPORT
QPlatformDropQtResponse *ritual_ZN22QGuiApplicationPrivate11processDropEP7QWindowPK9QMimeDataRK6QPoint6QFlagsIN2Qt10DropActionEES8_INS9_11MouseButtonEES8_INS9_16KeyboardModifierEE(
    QWindow *w,
    const QMimeData *dropData,
    const QPoint *p,
    int supportedActions,
    int buttons,
    int modifiers) {
  return new QPlatformDropQtResponse(
      QGuiApplicationPrivate::processDrop(
          w,
          dropData,
          *p,
          QFlags<Qt::DropAction>::fromInt(supportedActions),
          QFlags<Qt::MouseButton>::fromInt(buttons),
          QFlags<Qt::KeyboardModifier>::fromInt(modifiers)));
}
#endif  // QT_CONFIG(draganddrop)

//  bool QGuiApplicationPrivate::sendQWindowEventToQPlatformWindow(QWindow
//      *window, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QGuiApplicationPrivate33sendQWindowEventToQPlatformWindowEP7QWindowP6QEvent(
    QWindow *window,
    QEvent *event) {
  return QGuiApplicationPrivate::sendQWindowEventToQPlatformWindow(
      window,
      event);
}

//  bool QGuiApplicationPrivate::maybeForwardEventToVirtualKeyboard(QEvent
//      *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QGuiApplicationPrivate34maybeForwardEventToVirtualKeyboardEP6QEvent(
    QEvent *e) {
  return QGuiApplicationPrivate::maybeForwardEventToVirtualKeyboard(e);
}

//  bool QGuiApplicationPrivate::isUsingVirtualKeyboard()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QGuiApplicationPrivate22isUsingVirtualKeyboardEv() {
  return QGuiApplicationPrivate::isUsingVirtualKeyboard();
}

//  Qt::Alignment QGuiApplicationPrivate::visualAlignment(Qt::LayoutDirection
//      direction, Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QGuiApplicationPrivate15visualAlignmentEN2Qt15LayoutDirectionE6QFlagsINS0_13AlignmentFlagEE(
    Qt::LayoutDirection direction,
    int alignment) {
  return static_cast<int>(
      QGuiApplicationPrivate::visualAlignment(
          direction,
          QFlags<Qt::AlignmentFlag>::fromInt(alignment)).toInt());
}

//  QPixmap QGuiApplicationPrivate::getPixmapCursor(Qt::CursorShape cshape)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN22QGuiApplicationPrivate15getPixmapCursorEN2Qt11CursorShapeE(
    QGuiApplicationPrivate *self,
    Qt::CursorShape cshape) {
  return new QPixmap(self->getPixmapCursor(cshape));
}

//  void QGuiApplicationPrivate::_q_updateFocusObject(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate20_q_updateFocusObjectEP7QObject(
    QGuiApplicationPrivate *self,
    QObject *object) {
  self->_q_updateFocusObject(object);
}

//  QGuiApplicationPrivate *QGuiApplicationPrivate::instance()
extern "C" Q_DECL_EXPORT
QGuiApplicationPrivate *ritual_ZN22QGuiApplicationPrivate8instanceEv() {
  return QGuiApplicationPrivate::instance();
}

//  void QGuiApplicationPrivate::showModalWindow(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate15showModalWindowEP7QWindow(
    QWindow *window) {
  QGuiApplicationPrivate::showModalWindow(window);
}

//  void QGuiApplicationPrivate::hideModalWindow(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate15hideModalWindowEP7QWindow(
    QWindow *window) {
  QGuiApplicationPrivate::hideModalWindow(window);
}

//  void QGuiApplicationPrivate::updateBlockedStatus(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate19updateBlockedStatusEP7QWindow(
    QWindow *window) {
  QGuiApplicationPrivate::updateBlockedStatus(window);
}

//  Qt::WindowModality QGuiApplicationPrivate::defaultModality() const
extern "C" Q_DECL_EXPORT
Qt::WindowModality ritual_ZNK22QGuiApplicationPrivate15defaultModalityEv(
    const QGuiApplicationPrivate *self) {
  return self->defaultModality();
}

//  bool QGuiApplicationPrivate::windowNeverBlocked(QWindow *window) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QGuiApplicationPrivate18windowNeverBlockedEP7QWindow(
    const QGuiApplicationPrivate *self,
    QWindow *window) {
  return self->windowNeverBlocked(window);
}

//  qsizetype QGuiApplicationPrivate::popupCount()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN22QGuiApplicationPrivate10popupCountEv() {
  return QGuiApplicationPrivate::popupCount();
}

//  QWindow *QGuiApplicationPrivate::activePopupWindow()
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZN22QGuiApplicationPrivate17activePopupWindowEv() {
  return QGuiApplicationPrivate::activePopupWindow();
}

//  void QGuiApplicationPrivate::activatePopup(QWindow *popup)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate13activatePopupEP7QWindow(
    QWindow *popup) {
  QGuiApplicationPrivate::activatePopup(popup);
}

//  bool QGuiApplicationPrivate::closePopup(QWindow *popup)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QGuiApplicationPrivate10closePopupEP7QWindow(
    QWindow *popup) {
  return QGuiApplicationPrivate::closePopup(popup);
}

//  bool QGuiApplicationPrivate::closeAllPopups()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QGuiApplicationPrivate14closeAllPopupsEv() {
  return QGuiApplicationPrivate::closeAllPopups();
}

#if !defined(QT_NO_SESSIONMANAGER)
//  void QGuiApplicationPrivate::commitData()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate10commitDataEv(
    QGuiApplicationPrivate *self) {
  self->commitData();
}
#endif  // !defined(QT_NO_SESSIONMANAGER)

#if !defined(QT_NO_SESSIONMANAGER)
//  void QGuiApplicationPrivate::saveState()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate9saveStateEv(
    QGuiApplicationPrivate *self) {
  self->saveState();
}
#endif  // !defined(QT_NO_SESSIONMANAGER)

//  QInputDeviceManager *QGuiApplicationPrivate::inputDeviceManager()
extern "C" Q_DECL_EXPORT
QInputDeviceManager *ritual_ZN22QGuiApplicationPrivate18inputDeviceManagerEv() {
  return QGuiApplicationPrivate::inputDeviceManager();
}

//  const QColorTrcLut *QGuiApplicationPrivate::colorProfileForA8Text()
extern "C" Q_DECL_EXPORT
const QColorTrcLut *ritual_ZN22QGuiApplicationPrivate21colorProfileForA8TextEv(
    QGuiApplicationPrivate *self) {
  return self->colorProfileForA8Text();
}

//  const QColorTrcLut *QGuiApplicationPrivate::colorProfileForA32Text()
extern "C" Q_DECL_EXPORT
const QColorTrcLut *ritual_ZN22QGuiApplicationPrivate22colorProfileForA32TextEv(
    QGuiApplicationPrivate *self) {
  return self->colorProfileForA32Text();
}

//  QPixmap QGuiApplicationPrivate::applyQIconStyleHelper(QIcon::Mode a0,
//      const QPixmap &basePixmap) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK22QGuiApplicationPrivate21applyQIconStyleHelperEN5QIcon4ModeERK7QPixmap(
    const QGuiApplicationPrivate *self,
    QIcon::Mode a0,
    const QPixmap *basePixmap) {
  return new QPixmap(self->applyQIconStyleHelper(a0, *basePixmap));
}

//  void QGuiApplicationPrivate::notifyWindowIconChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate23notifyWindowIconChangedEv(
    QGuiApplicationPrivate *self) {
  self->notifyWindowIconChanged();
}

//  void QGuiApplicationPrivate::applyWindowGeometrySpecificationTo(QWindow
//      *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate34applyWindowGeometrySpecificationToEP7QWindow(
    QWindow *window) {
  QGuiApplicationPrivate::applyWindowGeometrySpecificationTo(window);
}

//  void QGuiApplicationPrivate::setApplicationState(Qt::ApplicationState
//      state, bool forcePropagate)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate19setApplicationStateEN2Qt16ApplicationStateEb(
    Qt::ApplicationState state,
    bool forcePropagate) {
  QGuiApplicationPrivate::setApplicationState(state, forcePropagate);
}

//  void QGuiApplicationPrivate::resetCachedDevicePixelRatio()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate27resetCachedDevicePixelRatioEv() {
  QGuiApplicationPrivate::resetCachedDevicePixelRatio();
}

#if !defined(QT_NO_ACTION)
//  QActionPrivate *QGuiApplicationPrivate::createActionPrivate() const
extern "C" Q_DECL_EXPORT
QActionPrivate *ritual_ZNK22QGuiApplicationPrivate19createActionPrivateEv(
    const QGuiApplicationPrivate *self) {
  return self->createActionPrivate();
}
#endif  // !defined(QT_NO_ACTION)

#if !defined(QT_NO_SHORTCUT)
//  QShortcutPrivate *QGuiApplicationPrivate::createShortcutPrivate() const
extern "C" Q_DECL_EXPORT
QShortcutPrivate *ritual_ZNK22QGuiApplicationPrivate21createShortcutPrivateEv(
    const QGuiApplicationPrivate *self) {
  return self->createShortcutPrivate();
}
#endif  // !defined(QT_NO_SHORTCUT)

//  void QGuiApplicationPrivate::updatePalette()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate13updatePaletteEv() {
  QGuiApplicationPrivate::updatePalette();
}

//  QEvent::Type QGuiApplicationPrivate::contextMenuEventType()
extern "C" Q_DECL_EXPORT
QEvent::Type ritual_ZN22QGuiApplicationPrivate20contextMenuEventTypeEv() {
  return QGuiApplicationPrivate::contextMenuEventType();
}

//  QThreadPool *QGuiApplicationPrivate::qtGuiThreadPool()
extern "C" Q_DECL_EXPORT
QThreadPool *ritual_ZN22QGuiApplicationPrivate15qtGuiThreadPoolEv() {
  return QGuiApplicationPrivate::qtGuiThreadPool();
}

//  void QGuiApplicationPrivate::_q_updatePrimaryScreenDpis()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate26_q_updatePrimaryScreenDpisEv(
    QGuiApplicationPrivate *self) {
  self->_q_updatePrimaryScreenDpis();
}

//  void QGuiApplicationPrivate::handleThemeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate18handleThemeChangedEv(
    QGuiApplicationPrivate *self) {
  self->handleThemeChanged();
}

//  bool QGuiApplicationPrivate::setPalette(const QPalette &palette)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QGuiApplicationPrivate10setPaletteERK8QPalette(
    const QPalette *palette) {
  return QGuiApplicationPrivate::setPalette(*palette);
}

//  QPalette QGuiApplicationPrivate::basePalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK22QGuiApplicationPrivate11basePaletteEv(
    const QGuiApplicationPrivate *self) {
  return new QPalette(self->basePalette());
}

//  void QGuiApplicationPrivate::handlePaletteChanged(const char *className)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate20handlePaletteChangedEPKc(
    QGuiApplicationPrivate *self,
    const char *className) {
  self->handlePaletteChanged(className);
}

#if QT_CONFIG(draganddrop)
//  void QGuiApplicationPrivate::notifyDragStarted(const QDrag *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate17notifyDragStartedEPK5QDrag(
    QGuiApplicationPrivate *self,
    const QDrag *a0) {
  self->notifyDragStarted(a0);
}
#endif  // QT_CONFIG(draganddrop)

//  void QGuiApplicationPrivate::clearPalette()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate12clearPaletteEv() {
  QGuiApplicationPrivate::clearPalette();
}

//  a Python function taken by a CuteQGuiApplicationPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGuiApplicationPrivate(
    QGuiApplicationPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGuiApplicationPrivate *>(self)->take(key, call);
}

//  void QGuiApplicationPrivate::createEventDispatcher()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QGuiApplicationPrivate21createEventDispatcherEv(
    QGuiApplicationPrivate *self) {
  self->QGuiApplicationPrivate::createEventDispatcher();
}

//  void QGuiApplicationPrivate::eventDispatcherReady()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QGuiApplicationPrivate20eventDispatcherReadyEv(
    QGuiApplicationPrivate *self) {
  self->QGuiApplicationPrivate::eventDispatcherReady();
}

//  void QGuiApplicationPrivate::notifyLayoutDirectionChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QGuiApplicationPrivate27notifyLayoutDirectionChangeEv(
    QGuiApplicationPrivate *self) {
  self->QGuiApplicationPrivate::notifyLayoutDirectionChange();
}

//  void QGuiApplicationPrivate::notifyActiveWindowChange(QWindow *previous)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QGuiApplicationPrivate24notifyActiveWindowChangeEP7QWindow(
    QGuiApplicationPrivate *self,
    QWindow *previous) {
  self->QGuiApplicationPrivate::notifyActiveWindowChange(previous);
}

//  bool QGuiApplicationPrivate::canQuitAutomatically()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QGuiApplicationPrivate20canQuitAutomaticallyEv(
    QGuiApplicationPrivate *self) {
  return self->QGuiApplicationPrivate::canQuitAutomatically();
}

//  void QGuiApplicationPrivate::quit()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QGuiApplicationPrivate4quitEv(
    QGuiApplicationPrivate *self) {
  self->QGuiApplicationPrivate::quit();
}

//  Qt::WindowModality QGuiApplicationPrivate::defaultModality() const
extern "C" Q_DECL_EXPORT
Qt::WindowModality ritual_own_ZNK22QGuiApplicationPrivate15defaultModalityEv(
    const QGuiApplicationPrivate *self) {
  return self->QGuiApplicationPrivate::defaultModality();
}

//  bool QGuiApplicationPrivate::windowNeverBlocked(QWindow *window) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK22QGuiApplicationPrivate18windowNeverBlockedEP7QWindow(
    const QGuiApplicationPrivate *self,
    QWindow *window) {
  return self->QGuiApplicationPrivate::windowNeverBlocked(window);
}

//  QPixmap QGuiApplicationPrivate::applyQIconStyleHelper(QIcon::Mode a0,
//      const QPixmap &basePixmap) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZNK22QGuiApplicationPrivate21applyQIconStyleHelperEN5QIcon4ModeERK7QPixmap(
    const QGuiApplicationPrivate *self,
    QIcon::Mode a0,
    const QPixmap *basePixmap) {
  return new QPixmap(
      self->QGuiApplicationPrivate::applyQIconStyleHelper(
          a0,
          *basePixmap));
}

//  void QGuiApplicationPrivate::notifyWindowIconChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QGuiApplicationPrivate23notifyWindowIconChangedEv(
    QGuiApplicationPrivate *self) {
  self->QGuiApplicationPrivate::notifyWindowIconChanged();
}

#if !defined(QT_NO_ACTION)
//  QActionPrivate *QGuiApplicationPrivate::createActionPrivate() const
extern "C" Q_DECL_EXPORT
QActionPrivate *ritual_own_ZNK22QGuiApplicationPrivate19createActionPrivateEv(
    const QGuiApplicationPrivate *self) {
  return self->QGuiApplicationPrivate::createActionPrivate();
}
#endif  // !defined(QT_NO_ACTION)

#if !defined(QT_NO_SHORTCUT)
//  QShortcutPrivate *QGuiApplicationPrivate::createShortcutPrivate() const
extern "C" Q_DECL_EXPORT
QShortcutPrivate *ritual_own_ZNK22QGuiApplicationPrivate21createShortcutPrivateEv(
    const QGuiApplicationPrivate *self) {
  return self->QGuiApplicationPrivate::createShortcutPrivate();
}
#endif  // !defined(QT_NO_SHORTCUT)

//  void QGuiApplicationPrivate::handleThemeChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QGuiApplicationPrivate18handleThemeChangedEv(
    QGuiApplicationPrivate *self) {
  static_cast<OwnQGuiApplicationPrivate *>(self)->OwnQGuiApplicationPrivate::handleThemeChanged();
}

//  QPalette QGuiApplicationPrivate::basePalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK22QGuiApplicationPrivate11basePaletteEv(
    const QGuiApplicationPrivate *self) {
  return new QPalette(
      static_cast<const OwnQGuiApplicationPrivate *>(self)->OwnQGuiApplicationPrivate::basePalette());
}

#if QT_CONFIG(draganddrop)
//  void QGuiApplicationPrivate::notifyDragStarted(const QDrag *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QGuiApplicationPrivate17notifyDragStartedEPK5QDrag(
    QGuiApplicationPrivate *self,
    const QDrag *a0) {
  static_cast<OwnQGuiApplicationPrivate *>(self)->OwnQGuiApplicationPrivate::notifyDragStarted(
      a0);
}
#endif  // QT_CONFIG(draganddrop)
