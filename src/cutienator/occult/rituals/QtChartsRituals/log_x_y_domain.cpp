//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/logxydomain_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/logxydomain_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A LogXYDomain that Python can take functions over in. Every LogXYDomain
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteLogXYDomainCall0)(const void *, int *);
typedef void (*CuteLogXYDomainCall1)(const void *, qreal, qreal, qreal, qreal, int *);
typedef void (*CuteLogXYDomainCall2)(const void *, const QRectF *, int *);
typedef void (*CuteLogXYDomainCall3)(const void *, const QRectF *, int *);
typedef void (*CuteLogXYDomainCall4)(const void *, qreal, qreal, int *);
typedef const QPointF * (*CuteLogXYDomainCall5)(const void *, const QPointF *, int *);
typedef bool (*CuteLogXYDomainCall6)(const void *, QAbstractAxis *, int *);
typedef bool (*CuteLogXYDomainCall7)(const void *, QAbstractAxis *, int *);
typedef void (*CuteLogXYDomainCall8)(const void *, const QSizeF *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteLogXYDomainCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteLogXYDomainCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLogXYDomainCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLogXYDomainCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLogXYDomainCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLogXYDomainCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLogXYDomainCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteLogXYDomain : public LogXYDomain {
public:
  using LogXYDomain::LogXYDomain;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14AbstractDomain4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain8setRangeEdddd")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain6zoomInERK6QRectF")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain7zoomOutERK6QRectF")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain4moveEdd")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14AbstractDomain20calculateDomainPointERK7QPointF")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain10attachAxisEP13QAbstractAxis")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain10detachAxisEP13QAbstractAxis")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain7setSizeERK6QSizeF")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  DomainType LogXYDomain::type()
  AbstractDomain::DomainType type() override {
    if (taken[0]) {
      int handled = 0;
      CuteLogXYDomainCall0 call = reinterpret_cast<CuteLogXYDomainCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<AbstractDomain::DomainType>(given);
    }
    return LogXYDomain::type();
  }

  //  void LogXYDomain::setRange(qreal minX, qreal maxX, qreal minY, qreal
  //      maxY)
  void setRange(qreal minX, qreal maxX, qreal minY, qreal maxY) override {
    if (taken[1]) {
      int handled = 0;
      CuteLogXYDomainCall1 call = reinterpret_cast<CuteLogXYDomainCall1>(taken[1]);
      call(this, minX, maxX, minY, maxY, &handled);
      if (handled) return;
    }
    LogXYDomain::setRange(minX, maxX, minY, maxY);
  }

  //  void LogXYDomain::zoomIn(const QRectF &rect)
  void zoomIn(const QRectF &rect) override {
    if (taken[2]) {
      int handled = 0;
      CuteLogXYDomainCall2 call = reinterpret_cast<CuteLogXYDomainCall2>(taken[2]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    LogXYDomain::zoomIn(rect);
  }

  //  void LogXYDomain::zoomOut(const QRectF &rect)
  void zoomOut(const QRectF &rect) override {
    if (taken[3]) {
      int handled = 0;
      CuteLogXYDomainCall3 call = reinterpret_cast<CuteLogXYDomainCall3>(taken[3]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    LogXYDomain::zoomOut(rect);
  }

  //  void LogXYDomain::move(qreal dx, qreal dy)
  void move(qreal dx, qreal dy) override {
    if (taken[4]) {
      int handled = 0;
      CuteLogXYDomainCall4 call = reinterpret_cast<CuteLogXYDomainCall4>(taken[4]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    LogXYDomain::move(dx, dy);
  }

  //  QPointF LogXYDomain::calculateDomainPoint(const QPointF &point) const
  QPointF calculateDomainPoint(const QPointF &point) const override {
    if (taken[5]) {
      int handled = 0;
      CuteLogXYDomainCall5 call = reinterpret_cast<CuteLogXYDomainCall5>(taken[5]);
      const QPointF * given = call(this, &point, &handled);
      if (handled && given) return *given;
    }
    return LogXYDomain::calculateDomainPoint(point);
  }

  //  bool LogXYDomain::attachAxis(QAbstractAxis *axis)
  bool attachAxis(QAbstractAxis *axis) override {
    if (taken[6]) {
      int handled = 0;
      CuteLogXYDomainCall6 call = reinterpret_cast<CuteLogXYDomainCall6>(taken[6]);
      bool given = call(this, axis, &handled);
      if (handled) return given;
    }
    return LogXYDomain::attachAxis(axis);
  }

  //  bool LogXYDomain::detachAxis(QAbstractAxis *axis)
  bool detachAxis(QAbstractAxis *axis) override {
    if (taken[7]) {
      int handled = 0;
      CuteLogXYDomainCall7 call = reinterpret_cast<CuteLogXYDomainCall7>(taken[7]);
      bool given = call(this, axis, &handled);
      if (handled) return given;
    }
    return LogXYDomain::detachAxis(axis);
  }

  //  void AbstractDomain::setSize(const QSizeF &size)
  void setSize(const QSizeF &size) override {
    if (taken[8]) {
      int handled = 0;
      CuteLogXYDomainCall8 call = reinterpret_cast<CuteLogXYDomainCall8>(taken[8]);
      call(this, &size, &handled);
      if (handled) return;
    }
    AbstractDomain::setSize(size);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteLogXYDomainCall9 call = reinterpret_cast<CuteLogXYDomainCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteLogXYDomainCall10 call = reinterpret_cast<CuteLogXYDomainCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteLogXYDomainCall11 call = reinterpret_cast<CuteLogXYDomainCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteLogXYDomainCall12 call = reinterpret_cast<CuteLogXYDomainCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteLogXYDomainCall13 call = reinterpret_cast<CuteLogXYDomainCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteLogXYDomainCall14 call = reinterpret_cast<CuteLogXYDomainCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteLogXYDomainCall15 call = reinterpret_cast<CuteLogXYDomainCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *LogXYDomain::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11LogXYDomain10metaObjectEv(
    const LogXYDomain *self) {
  return self->metaObject();
}

//  void *LogXYDomain::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11LogXYDomain11qt_metacastEPKc(
    LogXYDomain *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int LogXYDomain::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11LogXYDomain11qt_metacallEN11QMetaObject4CallEiPPv(
    LogXYDomain *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString LogXYDomain::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11LogXYDomain2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(LogXYDomain::tr(s, c, n));
}

//  LogXYDomain::LogXYDomain(QObject *object)
extern "C" Q_DECL_EXPORT
LogXYDomain *ritual_ZN11LogXYDomainC1EP7QObject(QObject *object) {
  return new CuteLogXYDomain(object);
}

//  LogXYDomain::~LogXYDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN11LogXYDomainD1Ev(LogXYDomain *self) {
  delete self;
}

//  DomainType LogXYDomain::type()
extern "C" Q_DECL_EXPORT
AbstractDomain::DomainType ritual_ZN11LogXYDomain4typeEv(LogXYDomain *self) {
  return self->type();
}

//  void LogXYDomain::setRange(qreal minX, qreal maxX, qreal minY, qreal
//      maxY)
extern "C" Q_DECL_EXPORT
void ritual_ZN11LogXYDomain8setRangeEdddd(
    LogXYDomain *self,
    qreal minX,
    qreal maxX,
    qreal minY,
    qreal maxY) {
  self->setRange(minX, maxX, minY, maxY);
}

//  void LogXYDomain::zoomIn(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN11LogXYDomain6zoomInERK6QRectF(
    LogXYDomain *self,
    const QRectF *rect) {
  self->zoomIn(*rect);
}

//  void LogXYDomain::zoomOut(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN11LogXYDomain7zoomOutERK6QRectF(
    LogXYDomain *self,
    const QRectF *rect) {
  self->zoomOut(*rect);
}

//  void LogXYDomain::move(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN11LogXYDomain4moveEdd(LogXYDomain *self, qreal dx, qreal dy) {
  self->move(dx, dy);
}

//  QPointF LogXYDomain::calculateGeometryPoint(const QPointF &point, bool
//      &ok) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11LogXYDomain22calculateGeometryPointERK7QPointFRb(
    const LogXYDomain *self,
    const QPointF *point,
    bool *ok) {
  return new QPointF(self->calculateGeometryPoint(*point, *ok));
}

//  QPointF LogXYDomain::calculateDomainPoint(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11LogXYDomain20calculateDomainPointERK7QPointF(
    const LogXYDomain *self,
    const QPointF *point) {
  return new QPointF(self->calculateDomainPoint(*point));
}

//  QList<QPointF> LogXYDomain::calculateGeometryPoints(const QList<QPointF>
//      &list) const
extern "C" Q_DECL_EXPORT
QList<QPointF> *ritual_ZNK11LogXYDomain23calculateGeometryPointsERK5QListI7QPointFE(
    const LogXYDomain *self,
    const QList<QPointF> *list) {
  return new QList<QPointF>(self->calculateGeometryPoints(*list));
}

//  bool LogXYDomain::attachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11LogXYDomain10attachAxisEP13QAbstractAxis(
    LogXYDomain *self,
    QAbstractAxis *axis) {
  return self->attachAxis(axis);
}

//  bool LogXYDomain::detachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11LogXYDomain10detachAxisEP13QAbstractAxis(
    LogXYDomain *self,
    QAbstractAxis *axis) {
  return self->detachAxis(axis);
}

//  void LogXYDomain::handleHorizontalAxisBaseChanged(qreal baseX)
extern "C" Q_DECL_EXPORT
void ritual_ZN11LogXYDomain31handleHorizontalAxisBaseChangedEd(
    LogXYDomain *self,
    qreal baseX) {
  self->handleHorizontalAxisBaseChanged(baseX);
}

//  a Python function taken by a CuteLogXYDomain, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_LogXYDomain(
    LogXYDomain *self,
    const char *key,
    void *call) {
  return static_cast<CuteLogXYDomain *>(self)->take(key, call);
}

//  DomainType LogXYDomain::type()
extern "C" Q_DECL_EXPORT
AbstractDomain::DomainType ritual_own_ZN11LogXYDomain4typeEv(
    LogXYDomain *self) {
  return self->LogXYDomain::type();
}

//  void LogXYDomain::setRange(qreal minX, qreal maxX, qreal minY, qreal
//      maxY)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11LogXYDomain8setRangeEdddd(
    LogXYDomain *self,
    qreal minX,
    qreal maxX,
    qreal minY,
    qreal maxY) {
  self->LogXYDomain::setRange(minX, maxX, minY, maxY);
}

//  void LogXYDomain::zoomIn(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11LogXYDomain6zoomInERK6QRectF(
    LogXYDomain *self,
    const QRectF *rect) {
  self->LogXYDomain::zoomIn(*rect);
}

//  void LogXYDomain::zoomOut(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11LogXYDomain7zoomOutERK6QRectF(
    LogXYDomain *self,
    const QRectF *rect) {
  self->LogXYDomain::zoomOut(*rect);
}

//  void LogXYDomain::move(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11LogXYDomain4moveEdd(
    LogXYDomain *self,
    qreal dx,
    qreal dy) {
  self->LogXYDomain::move(dx, dy);
}

//  QPointF LogXYDomain::calculateDomainPoint(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZNK11LogXYDomain20calculateDomainPointERK7QPointF(
    const LogXYDomain *self,
    const QPointF *point) {
  return new QPointF(self->LogXYDomain::calculateDomainPoint(*point));
}

//  bool LogXYDomain::attachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11LogXYDomain10attachAxisEP13QAbstractAxis(
    LogXYDomain *self,
    QAbstractAxis *axis) {
  return self->LogXYDomain::attachAxis(axis);
}

//  bool LogXYDomain::detachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11LogXYDomain10detachAxisEP13QAbstractAxis(
    LogXYDomain *self,
    QAbstractAxis *axis) {
  return self->LogXYDomain::detachAxis(axis);
}
