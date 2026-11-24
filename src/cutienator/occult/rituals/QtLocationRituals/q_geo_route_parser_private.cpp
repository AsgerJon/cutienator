//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeorouteparser_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeorouteparser_p.h>
#include <QtLocation/6.12.0/QtLocation/private/qgeorouteparser_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/qgeorouterequest.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <cstring>

//  A QGeoRouteParserPrivate that Python can take functions over in. Every QGeoRouteParserPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QUrl * (*CuteQGeoRouteParserPrivateCall0)(const void *, const QGeoRouteRequest *, const QString *, int *);
class CuteQGeoRouteParserPrivate : public QGeoRouteParserPrivate {
public:
  using QGeoRouteParserPrivate::QGeoRouteParserPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK22QGeoRouteParserPrivate10requestUrlERK16QGeoRouteRequestRK7QString")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QUrl QGeoRouteParserPrivate::requestUrl(const QGeoRouteRequest
  //      &request, const QString &prefix) const
  QUrl requestUrl(
      const QGeoRouteRequest &request,
      const QString &prefix) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoRouteParserPrivateCall0 call = reinterpret_cast<CuteQGeoRouteParserPrivateCall0>(taken[0]);
      const QUrl * given = call(this, &request, &prefix, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  QGeoRouteParser *QGeoRouteParserPrivate::q_func()
extern "C" Q_DECL_EXPORT
QGeoRouteParser *ritual_ZN22QGeoRouteParserPrivate6q_funcEv(
    QGeoRouteParserPrivate *self) {
  return self->q_func();
}

//  const QGeoRouteParser *QGeoRouteParserPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGeoRouteParser *ritual_ZNK22QGeoRouteParserPrivate6q_funcEv(
    const QGeoRouteParserPrivate *self) {
  return self->q_func();
}

//  QGeoRouteParserPrivate::~QGeoRouteParserPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoRouteParserPrivateD1Ev(QGeoRouteParserPrivate *self) {
  delete self;
}

//  QUrl QGeoRouteParserPrivate::requestUrl(const QGeoRouteRequest &request,
//      const QString &prefix) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK22QGeoRouteParserPrivate10requestUrlERK16QGeoRouteRequestRK7QString(
    const QGeoRouteParserPrivate *self,
    const QGeoRouteRequest *request,
    const QString *prefix) {
  return new QUrl(self->requestUrl(*request, *prefix));
}

//  a Python function taken by a CuteQGeoRouteParserPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoRouteParserPrivate(
    QGeoRouteParserPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoRouteParserPrivate *>(self)->take(key, call);
}
