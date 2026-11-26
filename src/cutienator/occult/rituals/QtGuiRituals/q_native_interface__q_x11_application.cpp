//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qguiapplication_platform.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(xcb) || defined(Q_QDOC)
#include <QtGui/qguiapplication.h>
#include <cstring>

//  A QNativeInterface::QX11Application that Python can take functions over in. Every QNativeInterface::QX11Application
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(xcb) || defined(Q_QDOC)
typedef void * (*CuteQNativeInterface_QX11ApplicationCall0)(const void *, int *);
#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)
#if QT_CONFIG(xcb) || defined(Q_QDOC)
typedef void * (*CuteQNativeInterface_QX11ApplicationCall1)(const void *, int *);
#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)
class CuteQNativeInterface_QX11Application : public QNativeInterface::QX11Application {
public:
  using QNativeInterface::QX11Application::QX11Application;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(xcb) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK16QNativeInterface15QX11Application7displayEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)
#if QT_CONFIG(xcb) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK16QNativeInterface15QX11Application10connectionEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)
    return false;
  }

#if QT_CONFIG(xcb) || defined(Q_QDOC)
  //  Display *QNativeInterface::QX11Application::display() const
  Display *display() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQNativeInterface_QX11ApplicationCall0 call = reinterpret_cast<CuteQNativeInterface_QX11ApplicationCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<Display *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)

#if QT_CONFIG(xcb) || defined(Q_QDOC)
  //  xcb_connection_t *QNativeInterface::QX11Application::connection()
  //      const
  xcb_connection_t *connection() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQNativeInterface_QX11ApplicationCall1 call = reinterpret_cast<CuteQNativeInterface_QX11ApplicationCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<xcb_connection_t *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)
};

//  QNativeInterface::QX11Application::~QX11Application()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface15QX11ApplicationD1Ev(
    QNativeInterface::QX11Application *self) {
  delete self;
}

//  QNativeInterface::QX11Application::QX11Application()
extern "C" Q_DECL_EXPORT
QNativeInterface::QX11Application *ritual_ZN16QNativeInterface15QX11ApplicationC1Ev() {
  return new CuteQNativeInterface_QX11Application();
}

//  Display *QNativeInterface::QX11Application::display() const
extern "C" Q_DECL_EXPORT
Display *ritual_ZNK16QNativeInterface15QX11Application7displayEv(
    const QNativeInterface::QX11Application *self) {
  return self->display();
}

//  xcb_connection_t *QNativeInterface::QX11Application::connection() const
extern "C" Q_DECL_EXPORT
xcb_connection_t *ritual_ZNK16QNativeInterface15QX11Application10connectionEv(
    const QNativeInterface::QX11Application *self) {
  return self->connection();
}

//  a Python function taken by a CuteQNativeInterface_QX11Application, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNativeInterface_QX11Application(
    QNativeInterface::QX11Application *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNativeInterface_QX11Application *>(self)->take(key, call);
}

#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)
