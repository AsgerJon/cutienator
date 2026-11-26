//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformaccessibility.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(accessibility)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformaccessibility.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QPlatformAccessibility that Python can take functions over in. Every QPlatformAccessibility
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef void (*CuteQPlatformAccessibilityCall0)(const void *, QAccessibleEvent *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQPlatformAccessibilityCall1)(const void *, QObject *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQPlatformAccessibilityCall2)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQPlatformAccessibilityCall3)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQPlatformAccessibility : public QPlatformAccessibility {
public:
  using QPlatformAccessibility::QPlatformAccessibility;
  CuteQPlatformAccessibility(const QPlatformAccessibility & other) : QPlatformAccessibility(other) {}
  void *taken[4] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN22QPlatformAccessibility25notifyAccessibilityUpdateEP16QAccessibleEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN22QPlatformAccessibility13setRootObjectEP7QObject")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN22QPlatformAccessibility10initializeEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN22QPlatformAccessibility7cleanupEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
  //  void
  //      QPlatformAccessibility::notifyAccessibilityUpdate(QAccessibleEven
  //      t *event)
  void notifyAccessibilityUpdate(QAccessibleEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformAccessibilityCall0 call = reinterpret_cast<CuteQPlatformAccessibilityCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QPlatformAccessibility::notifyAccessibilityUpdate(event);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QPlatformAccessibility::setRootObject(QObject *o)
  void setRootObject(QObject *o) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformAccessibilityCall1 call = reinterpret_cast<CuteQPlatformAccessibilityCall1>(taken[1]);
      call(this, o, &handled);
      if (handled) return;
    }
    QPlatformAccessibility::setRootObject(o);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QPlatformAccessibility::initialize()
  void initialize() override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformAccessibilityCall2 call = reinterpret_cast<CuteQPlatformAccessibilityCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformAccessibility::initialize();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QPlatformAccessibility::cleanup()
  void cleanup() override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformAccessibilityCall3 call = reinterpret_cast<CuteQPlatformAccessibilityCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformAccessibility::cleanup();
  }
#endif  // QT_CONFIG(accessibility)
};

//  QPlatformAccessibility::QPlatformAccessibility()
extern "C" Q_DECL_EXPORT
QPlatformAccessibility *ritual_ZN22QPlatformAccessibilityC1Ev() {
  return new CuteQPlatformAccessibility();
}

//  QPlatformAccessibility::~QPlatformAccessibility()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformAccessibilityD1Ev(QPlatformAccessibility *self) {
  delete self;
}

//  void QPlatformAccessibility::notifyAccessibilityUpdate(QAccessibleEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformAccessibility25notifyAccessibilityUpdateEP16QAccessibleEvent(
    QPlatformAccessibility *self,
    QAccessibleEvent *event) {
  self->notifyAccessibilityUpdate(event);
}

//  void QPlatformAccessibility::setRootObject(QObject *o)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformAccessibility13setRootObjectEP7QObject(
    QPlatformAccessibility *self,
    QObject *o) {
  self->setRootObject(o);
}

//  void QPlatformAccessibility::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformAccessibility10initializeEv(
    QPlatformAccessibility *self) {
  self->initialize();
}

//  void QPlatformAccessibility::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformAccessibility7cleanupEv(
    QPlatformAccessibility *self) {
  self->cleanup();
}

//  bool QPlatformAccessibility::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QPlatformAccessibility8isActiveEv(
    const QPlatformAccessibility *self) {
  return self->isActive();
}

//  void QPlatformAccessibility::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformAccessibility9setActiveEb(
    QPlatformAccessibility *self,
    bool active) {
  self->setActive(active);
}

//  void QPlatformAccessibility::clearActiveNotificationState()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformAccessibility28clearActiveNotificationStateEv(
    QPlatformAccessibility *self) {
  self->clearActiveNotificationState();
}

//  a Python function taken by a CuteQPlatformAccessibility, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformAccessibility(
    QPlatformAccessibility *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformAccessibility *>(self)->take(key, call);
}

//  void QPlatformAccessibility::notifyAccessibilityUpdate(QAccessibleEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QPlatformAccessibility25notifyAccessibilityUpdateEP16QAccessibleEvent(
    QPlatformAccessibility *self,
    QAccessibleEvent *event) {
  self->QPlatformAccessibility::notifyAccessibilityUpdate(event);
}

//  void QPlatformAccessibility::setRootObject(QObject *o)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QPlatformAccessibility13setRootObjectEP7QObject(
    QPlatformAccessibility *self,
    QObject *o) {
  self->QPlatformAccessibility::setRootObject(o);
}

//  void QPlatformAccessibility::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QPlatformAccessibility10initializeEv(
    QPlatformAccessibility *self) {
  self->QPlatformAccessibility::initialize();
}

//  void QPlatformAccessibility::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QPlatformAccessibility7cleanupEv(
    QPlatformAccessibility *self) {
  self->QPlatformAccessibility::cleanup();
}

#endif  // QT_CONFIG(accessibility)
