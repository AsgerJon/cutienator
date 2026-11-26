//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qscreen_platform.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(wayland) || defined(Q_QDOC)
#include <QtGui/qscreen.h>
#include <cstring>

//  A QNativeInterface::QWaylandScreen that Python can take functions over in. Every QNativeInterface::QWaylandScreen
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(wayland) || defined(Q_QDOC)
typedef void * (*CuteQNativeInterface_QWaylandScreenCall0)(const void *, int *);
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
class CuteQNativeInterface_QWaylandScreen : public QNativeInterface::QWaylandScreen {
public:
  using QNativeInterface::QWaylandScreen::QWaylandScreen;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(wayland) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK16QNativeInterface14QWaylandScreen6outputEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
    return false;
  }

#if QT_CONFIG(wayland) || defined(Q_QDOC)
  //  wl_output *QNativeInterface::QWaylandScreen::output() const
  wl_output *output() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQNativeInterface_QWaylandScreenCall0 call = reinterpret_cast<CuteQNativeInterface_QWaylandScreenCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<wl_output *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
};

//  QNativeInterface::QWaylandScreen::~QWaylandScreen()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface14QWaylandScreenD1Ev(
    QNativeInterface::QWaylandScreen *self) {
  delete self;
}

//  QNativeInterface::QWaylandScreen::QWaylandScreen()
extern "C" Q_DECL_EXPORT
QNativeInterface::QWaylandScreen *ritual_ZN16QNativeInterface14QWaylandScreenC1Ev() {
  return new CuteQNativeInterface_QWaylandScreen();
}

//  wl_output *QNativeInterface::QWaylandScreen::output() const
extern "C" Q_DECL_EXPORT
wl_output *ritual_ZNK16QNativeInterface14QWaylandScreen6outputEv(
    const QNativeInterface::QWaylandScreen *self) {
  return self->output();
}

//  a Python function taken by a CuteQNativeInterface_QWaylandScreen, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNativeInterface_QWaylandScreen(
    QNativeInterface::QWaylandScreen *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNativeInterface_QWaylandScreen *>(self)->take(key, call);
}

#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
