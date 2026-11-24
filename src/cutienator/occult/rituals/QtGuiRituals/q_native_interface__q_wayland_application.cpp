//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qguiapplication_platform.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(wayland) || defined(Q_QDOC)
#include <QtGui/qguiapplication.h>
#include <cstring>

//  A QNativeInterface::QWaylandApplication that Python can take functions over in. Every QNativeInterface::QWaylandApplication
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(wayland) || defined(Q_QDOC)
typedef uint (*CuteQNativeInterface_QWaylandApplicationCall0)(const void *, int *);
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
class CuteQNativeInterface_QWaylandApplication : public QNativeInterface::QWaylandApplication {
public:
  using QNativeInterface::QWaylandApplication::QWaylandApplication;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(wayland) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK16QNativeInterface19QWaylandApplication15lastInputSerialEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
    return false;
  }

#if QT_CONFIG(wayland) || defined(Q_QDOC)
  //  uint QNativeInterface::QWaylandApplication::lastInputSerial() const
  uint lastInputSerial() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQNativeInterface_QWaylandApplicationCall0 call = reinterpret_cast<CuteQNativeInterface_QWaylandApplicationCall0>(taken[0]);
      uint given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
};

//  QNativeInterface::QWaylandApplication::~QWaylandApplication()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface19QWaylandApplicationD1Ev(
    QNativeInterface::QWaylandApplication *self) {
  delete self;
}

//  uint QNativeInterface::QWaylandApplication::lastInputSerial() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK16QNativeInterface19QWaylandApplication15lastInputSerialEv(
    const QNativeInterface::QWaylandApplication *self) {
  return self->lastInputSerial();
}

//  a Python function taken by a CuteQNativeInterface_QWaylandApplication,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNativeInterface_QWaylandApplication(
    QNativeInterface::QWaylandApplication *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNativeInterface_QWaylandApplication *>(self)->take(key, call);
}

#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
