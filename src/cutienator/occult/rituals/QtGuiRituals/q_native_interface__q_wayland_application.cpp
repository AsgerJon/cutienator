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
typedef void * (*CuteQNativeInterface_QWaylandApplicationCall0)(const void *, int *);
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
#if QT_CONFIG(wayland) || defined(Q_QDOC)
typedef void * (*CuteQNativeInterface_QWaylandApplicationCall1)(const void *, int *);
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
#if QT_CONFIG(wayland) || defined(Q_QDOC)
typedef void * (*CuteQNativeInterface_QWaylandApplicationCall2)(const void *, int *);
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
#if QT_CONFIG(wayland) || defined(Q_QDOC)
typedef void * (*CuteQNativeInterface_QWaylandApplicationCall3)(const void *, int *);
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
#if QT_CONFIG(wayland) || defined(Q_QDOC)
typedef void * (*CuteQNativeInterface_QWaylandApplicationCall4)(const void *, int *);
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
#if QT_CONFIG(wayland) || defined(Q_QDOC)
typedef void * (*CuteQNativeInterface_QWaylandApplicationCall5)(const void *, int *);
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
#if QT_CONFIG(wayland) || defined(Q_QDOC)
typedef uint (*CuteQNativeInterface_QWaylandApplicationCall6)(const void *, int *);
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
#if QT_CONFIG(wayland) || defined(Q_QDOC)
typedef void * (*CuteQNativeInterface_QWaylandApplicationCall7)(const void *, int *);
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
#if QT_CONFIG(wayland) || defined(Q_QDOC)
#if QT_CONFIG(xkbcommon)
typedef void * (*CuteQNativeInterface_QWaylandApplicationCall8)(const void *, int *);
#endif  // QT_CONFIG(xkbcommon)
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
class CuteQNativeInterface_QWaylandApplication : public QNativeInterface::QWaylandApplication {
public:
  using QNativeInterface::QWaylandApplication::QWaylandApplication;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(wayland) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK16QNativeInterface19QWaylandApplication7displayEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
#if QT_CONFIG(wayland) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK16QNativeInterface19QWaylandApplication10compositorEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
#if QT_CONFIG(wayland) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK16QNativeInterface19QWaylandApplication4seatEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
#if QT_CONFIG(wayland) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK16QNativeInterface19QWaylandApplication8keyboardEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
#if QT_CONFIG(wayland) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK16QNativeInterface19QWaylandApplication7pointerEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
#if QT_CONFIG(wayland) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK16QNativeInterface19QWaylandApplication5touchEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
#if QT_CONFIG(wayland) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK16QNativeInterface19QWaylandApplication15lastInputSerialEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
#if QT_CONFIG(wayland) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK16QNativeInterface19QWaylandApplication13lastInputSeatEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
#if QT_CONFIG(wayland) || defined(Q_QDOC)
#if QT_CONFIG(xkbcommon)
    if (!std::strcmp(key, "_ZNK16QNativeInterface19QWaylandApplication10xkbContextEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(xkbcommon)
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
    return false;
  }

#if QT_CONFIG(wayland) || defined(Q_QDOC)
  //  wl_display *QNativeInterface::QWaylandApplication::display() const
  wl_display *display() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQNativeInterface_QWaylandApplicationCall0 call = reinterpret_cast<CuteQNativeInterface_QWaylandApplicationCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<wl_display *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)

#if QT_CONFIG(wayland) || defined(Q_QDOC)
  //  wl_compositor *QNativeInterface::QWaylandApplication::compositor()
  //      const
  wl_compositor *compositor() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQNativeInterface_QWaylandApplicationCall1 call = reinterpret_cast<CuteQNativeInterface_QWaylandApplicationCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<wl_compositor *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)

#if QT_CONFIG(wayland) || defined(Q_QDOC)
  //  wl_seat *QNativeInterface::QWaylandApplication::seat() const
  wl_seat *seat() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNativeInterface_QWaylandApplicationCall2 call = reinterpret_cast<CuteQNativeInterface_QWaylandApplicationCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<wl_seat *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)

#if QT_CONFIG(wayland) || defined(Q_QDOC)
  //  wl_keyboard *QNativeInterface::QWaylandApplication::keyboard() const
  wl_keyboard *keyboard() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQNativeInterface_QWaylandApplicationCall3 call = reinterpret_cast<CuteQNativeInterface_QWaylandApplicationCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<wl_keyboard *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)

#if QT_CONFIG(wayland) || defined(Q_QDOC)
  //  wl_pointer *QNativeInterface::QWaylandApplication::pointer() const
  wl_pointer *pointer() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQNativeInterface_QWaylandApplicationCall4 call = reinterpret_cast<CuteQNativeInterface_QWaylandApplicationCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<wl_pointer *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)

#if QT_CONFIG(wayland) || defined(Q_QDOC)
  //  wl_touch *QNativeInterface::QWaylandApplication::touch() const
  wl_touch *touch() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQNativeInterface_QWaylandApplicationCall5 call = reinterpret_cast<CuteQNativeInterface_QWaylandApplicationCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<wl_touch *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)

#if QT_CONFIG(wayland) || defined(Q_QDOC)
  //  uint QNativeInterface::QWaylandApplication::lastInputSerial() const
  uint lastInputSerial() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQNativeInterface_QWaylandApplicationCall6 call = reinterpret_cast<CuteQNativeInterface_QWaylandApplicationCall6>(taken[6]);
      uint given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)

#if QT_CONFIG(wayland) || defined(Q_QDOC)
  //  wl_seat *QNativeInterface::QWaylandApplication::lastInputSeat() const
  wl_seat *lastInputSeat() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQNativeInterface_QWaylandApplicationCall7 call = reinterpret_cast<CuteQNativeInterface_QWaylandApplicationCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<wl_seat *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)

#if QT_CONFIG(wayland) || defined(Q_QDOC)
#if QT_CONFIG(xkbcommon)
  //  xkb_context *QNativeInterface::QWaylandApplication::xkbContext()
  //      const
  xkb_context *xkbContext() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQNativeInterface_QWaylandApplicationCall8 call = reinterpret_cast<CuteQNativeInterface_QWaylandApplicationCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<xkb_context *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(xkbcommon)
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
};

//  QNativeInterface::QWaylandApplication::~QWaylandApplication()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface19QWaylandApplicationD1Ev(
    QNativeInterface::QWaylandApplication *self) {
  delete self;
}

//  QNativeInterface::QWaylandApplication::QWaylandApplication()
extern "C" Q_DECL_EXPORT
QNativeInterface::QWaylandApplication *ritual_ZN16QNativeInterface19QWaylandApplicationC1Ev() {
  return new CuteQNativeInterface_QWaylandApplication();
}

//  wl_display *QNativeInterface::QWaylandApplication::display() const
extern "C" Q_DECL_EXPORT
wl_display *ritual_ZNK16QNativeInterface19QWaylandApplication7displayEv(
    const QNativeInterface::QWaylandApplication *self) {
  return self->display();
}

//  wl_compositor *QNativeInterface::QWaylandApplication::compositor() const
extern "C" Q_DECL_EXPORT
wl_compositor *ritual_ZNK16QNativeInterface19QWaylandApplication10compositorEv(
    const QNativeInterface::QWaylandApplication *self) {
  return self->compositor();
}

//  wl_seat *QNativeInterface::QWaylandApplication::seat() const
extern "C" Q_DECL_EXPORT
wl_seat *ritual_ZNK16QNativeInterface19QWaylandApplication4seatEv(
    const QNativeInterface::QWaylandApplication *self) {
  return self->seat();
}

//  wl_keyboard *QNativeInterface::QWaylandApplication::keyboard() const
extern "C" Q_DECL_EXPORT
wl_keyboard *ritual_ZNK16QNativeInterface19QWaylandApplication8keyboardEv(
    const QNativeInterface::QWaylandApplication *self) {
  return self->keyboard();
}

//  wl_pointer *QNativeInterface::QWaylandApplication::pointer() const
extern "C" Q_DECL_EXPORT
wl_pointer *ritual_ZNK16QNativeInterface19QWaylandApplication7pointerEv(
    const QNativeInterface::QWaylandApplication *self) {
  return self->pointer();
}

//  wl_touch *QNativeInterface::QWaylandApplication::touch() const
extern "C" Q_DECL_EXPORT
wl_touch *ritual_ZNK16QNativeInterface19QWaylandApplication5touchEv(
    const QNativeInterface::QWaylandApplication *self) {
  return self->touch();
}

//  uint QNativeInterface::QWaylandApplication::lastInputSerial() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK16QNativeInterface19QWaylandApplication15lastInputSerialEv(
    const QNativeInterface::QWaylandApplication *self) {
  return self->lastInputSerial();
}

//  wl_seat *QNativeInterface::QWaylandApplication::lastInputSeat() const
extern "C" Q_DECL_EXPORT
wl_seat *ritual_ZNK16QNativeInterface19QWaylandApplication13lastInputSeatEv(
    const QNativeInterface::QWaylandApplication *self) {
  return self->lastInputSeat();
}

#if QT_CONFIG(xkbcommon)
//  xkb_context *QNativeInterface::QWaylandApplication::xkbContext() const
extern "C" Q_DECL_EXPORT
xkb_context *ritual_ZNK16QNativeInterface19QWaylandApplication10xkbContextEv(
    const QNativeInterface::QWaylandApplication *self) {
  return self->xkbContext();
}
#endif  // QT_CONFIG(xkbcommon)

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
