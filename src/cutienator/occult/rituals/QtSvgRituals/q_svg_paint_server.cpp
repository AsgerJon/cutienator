//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgpaintserver_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgpaintserver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgPaintServer that Python can take functions over in. Every QSvgPaintServer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgPaintServerCall0)(const void *, int *);
class CuteQSvgPaintServer : public QSvgPaintServer {
public:
  using QSvgPaintServer::QSvgPaintServer;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QSvgPaintServer4typeEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  Type QSvgPaintServer::type() const
  QSvgPaintServer::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgPaintServerCall0 call = reinterpret_cast<CuteQSvgPaintServerCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgPaintServer::Type>(given);
    }
    return {};
  }
};

//  QSvgPaintServer::~QSvgPaintServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgPaintServerD1Ev(QSvgPaintServer *self) {
  delete self;
}

//  Type QSvgPaintServer::type() const
extern "C" Q_DECL_EXPORT
QSvgPaintServer::Type ritual_ZNK15QSvgPaintServer4typeEv(
    const QSvgPaintServer *self) {
  return self->type();
}

//  a Python function taken by a CuteQSvgPaintServer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgPaintServer(
    QSvgPaintServer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgPaintServer *>(self)->take(key, call);
}
