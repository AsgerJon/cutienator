//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/logxlogydomain_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/logxlogydomain_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A LogXLogYDomain that Python can take functions over in. Every LogXLogYDomain
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteLogXLogYDomainCall0)(const void *, int *);
typedef void (*CuteLogXLogYDomainCall1)(const void *, qreal, qreal, qreal, qreal, int *);
typedef void (*CuteLogXLogYDomainCall2)(const void *, const QRectF *, int *);
typedef void (*CuteLogXLogYDomainCall3)(const void *, const QRectF *, int *);
typedef void (*CuteLogXLogYDomainCall4)(const void *, qreal, qreal, int *);
typedef const QPointF * (*CuteLogXLogYDomainCall5)(const void *, const QPointF *, int *);
typedef bool (*CuteLogXLogYDomainCall6)(const void *, QAbstractAxis *, int *);
typedef bool (*CuteLogXLogYDomainCall7)(const void *, QAbstractAxis *, int *);
typedef void (*CuteLogXLogYDomainCall8)(const void *, const QSizeF *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteLogXLogYDomainCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteLogXLogYDomainCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLogXLogYDomainCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLogXLogYDomainCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLogXLogYDomainCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLogXLogYDomainCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLogXLogYDomainCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteLogXLogYDomain : public LogXLogYDomain {
public:
  using LogXLogYDomain::LogXLogYDomain;
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

  //  DomainType LogXLogYDomain::type()
  AbstractDomain::DomainType type() override {
    if (taken[0]) {
      int handled = 0;
      CuteLogXLogYDomainCall0 call = reinterpret_cast<CuteLogXLogYDomainCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<AbstractDomain::DomainType>(given);
    }
    return LogXLogYDomain::type();
  }

  //  void LogXLogYDomain::setRange(qreal minX, qreal maxX, qreal minY,
  //      qreal maxY)
  void setRange(qreal minX, qreal maxX, qreal minY, qreal maxY) override {
    if (taken[1]) {
      int handled = 0;
      CuteLogXLogYDomainCall1 call = reinterpret_cast<CuteLogXLogYDomainCall1>(taken[1]);
      call(this, minX, maxX, minY, maxY, &handled);
      if (handled) return;
    }
    LogXLogYDomain::setRange(minX, maxX, minY, maxY);
  }

  //  void LogXLogYDomain::zoomIn(const QRectF &rect)
  void zoomIn(const QRectF &rect) override {
    if (taken[2]) {
      int handled = 0;
      CuteLogXLogYDomainCall2 call = reinterpret_cast<CuteLogXLogYDomainCall2>(taken[2]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    LogXLogYDomain::zoomIn(rect);
  }

  //  void LogXLogYDomain::zoomOut(const QRectF &rect)
  void zoomOut(const QRectF &rect) override {
    if (taken[3]) {
      int handled = 0;
      CuteLogXLogYDomainCall3 call = reinterpret_cast<CuteLogXLogYDomainCall3>(taken[3]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    LogXLogYDomain::zoomOut(rect);
  }

  //  void LogXLogYDomain::move(qreal dx, qreal dy)
  void move(qreal dx, qreal dy) override {
    if (taken[4]) {
      int handled = 0;
      CuteLogXLogYDomainCall4 call = reinterpret_cast<CuteLogXLogYDomainCall4>(taken[4]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    LogXLogYDomain::move(dx, dy);
  }

  //  QPointF LogXLogYDomain::calculateDomainPoint(const QPointF &point)
  //      const
  QPointF calculateDomainPoint(const QPointF &point) const override {
    if (taken[5]) {
      int handled = 0;
      CuteLogXLogYDomainCall5 call = reinterpret_cast<CuteLogXLogYDomainCall5>(taken[5]);
      const QPointF * given = call(this, &point, &handled);
      if (handled && given) return *given;
    }
    return LogXLogYDomain::calculateDomainPoint(point);
  }

  //  bool LogXLogYDomain::attachAxis(QAbstractAxis *axis)
  bool attachAxis(QAbstractAxis *axis) override {
    if (taken[6]) {
      int handled = 0;
      CuteLogXLogYDomainCall6 call = reinterpret_cast<CuteLogXLogYDomainCall6>(taken[6]);
      bool given = call(this, axis, &handled);
      if (handled) return given;
    }
    return LogXLogYDomain::attachAxis(axis);
  }

  //  bool LogXLogYDomain::detachAxis(QAbstractAxis *axis)
  bool detachAxis(QAbstractAxis *axis) override {
    if (taken[7]) {
      int handled = 0;
      CuteLogXLogYDomainCall7 call = reinterpret_cast<CuteLogXLogYDomainCall7>(taken[7]);
      bool given = call(this, axis, &handled);
      if (handled) return given;
    }
    return LogXLogYDomain::detachAxis(axis);
  }

  //  void AbstractDomain::setSize(const QSizeF &size)
  void setSize(const QSizeF &size) override {
    if (taken[8]) {
      int handled = 0;
      CuteLogXLogYDomainCall8 call = reinterpret_cast<CuteLogXLogYDomainCall8>(taken[8]);
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
      CuteLogXLogYDomainCall9 call = reinterpret_cast<CuteLogXLogYDomainCall9>(taken[9]);
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
      CuteLogXLogYDomainCall10 call = reinterpret_cast<CuteLogXLogYDomainCall10>(taken[10]);
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
      CuteLogXLogYDomainCall11 call = reinterpret_cast<CuteLogXLogYDomainCall11>(taken[11]);
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
      CuteLogXLogYDomainCall12 call = reinterpret_cast<CuteLogXLogYDomainCall12>(taken[12]);
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
      CuteLogXLogYDomainCall13 call = reinterpret_cast<CuteLogXLogYDomainCall13>(taken[13]);
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
      CuteLogXLogYDomainCall14 call = reinterpret_cast<CuteLogXLogYDomainCall14>(taken[14]);
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
      CuteLogXLogYDomainCall15 call = reinterpret_cast<CuteLogXLogYDomainCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *LogXLogYDomain::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14LogXLogYDomain10metaObjectEv(
    const LogXLogYDomain *self) {
  return self->metaObject();
}

//  QString LogXLogYDomain::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14LogXLogYDomain2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(LogXLogYDomain::tr(s, c, n));
}

//  LogXLogYDomain::LogXLogYDomain(QObject *object)
extern "C" Q_DECL_EXPORT
LogXLogYDomain *ritual_ZN14LogXLogYDomainC1EP7QObject(QObject *object) {
  return new CuteLogXLogYDomain(object);
}

//  LogXLogYDomain::~LogXLogYDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN14LogXLogYDomainD1Ev(LogXLogYDomain *self) {
  delete self;
}

//  DomainType LogXLogYDomain::type()
extern "C" Q_DECL_EXPORT
AbstractDomain::DomainType ritual_ZN14LogXLogYDomain4typeEv(
    LogXLogYDomain *self) {
  return self->type();
}

//  void LogXLogYDomain::setRange(qreal minX, qreal maxX, qreal minY, qreal
//      maxY)
extern "C" Q_DECL_EXPORT
void ritual_ZN14LogXLogYDomain8setRangeEdddd(
    LogXLogYDomain *self,
    qreal minX,
    qreal maxX,
    qreal minY,
    qreal maxY) {
  self->setRange(minX, maxX, minY, maxY);
}

//  void LogXLogYDomain::zoomIn(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14LogXLogYDomain6zoomInERK6QRectF(
    LogXLogYDomain *self,
    const QRectF *rect) {
  self->zoomIn(*rect);
}

//  void LogXLogYDomain::zoomOut(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14LogXLogYDomain7zoomOutERK6QRectF(
    LogXLogYDomain *self,
    const QRectF *rect) {
  self->zoomOut(*rect);
}

//  void LogXLogYDomain::move(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN14LogXLogYDomain4moveEdd(
    LogXLogYDomain *self,
    qreal dx,
    qreal dy) {
  self->move(dx, dy);
}

//  QPointF LogXLogYDomain::calculateGeometryPoint(const QPointF &point, bool
//      &ok) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK14LogXLogYDomain22calculateGeometryPointERK7QPointFRb(
    const LogXLogYDomain *self,
    const QPointF *point,
    bool *ok) {
  return new QPointF(self->calculateGeometryPoint(*point, *ok));
}

//  QPointF LogXLogYDomain::calculateDomainPoint(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK14LogXLogYDomain20calculateDomainPointERK7QPointF(
    const LogXLogYDomain *self,
    const QPointF *point) {
  return new QPointF(self->calculateDomainPoint(*point));
}

//  QList<QPointF> LogXLogYDomain::calculateGeometryPoints(const
//      QList<QPointF> &list) const
extern "C" Q_DECL_EXPORT
QList<QPointF> *ritual_ZNK14LogXLogYDomain23calculateGeometryPointsERK5QListI7QPointFE(
    const LogXLogYDomain *self,
    const QList<QPointF> *list) {
  return new QList<QPointF>(self->calculateGeometryPoints(*list));
}

//  bool LogXLogYDomain::attachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14LogXLogYDomain10attachAxisEP13QAbstractAxis(
    LogXLogYDomain *self,
    QAbstractAxis *axis) {
  return self->attachAxis(axis);
}

//  bool LogXLogYDomain::detachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14LogXLogYDomain10detachAxisEP13QAbstractAxis(
    LogXLogYDomain *self,
    QAbstractAxis *axis) {
  return self->detachAxis(axis);
}

//  void LogXLogYDomain::handleVerticalAxisBaseChanged(qreal baseY)
extern "C" Q_DECL_EXPORT
void ritual_ZN14LogXLogYDomain29handleVerticalAxisBaseChangedEd(
    LogXLogYDomain *self,
    qreal baseY) {
  self->handleVerticalAxisBaseChanged(baseY);
}

//  void LogXLogYDomain::handleHorizontalAxisBaseChanged(qreal baseX)
extern "C" Q_DECL_EXPORT
void ritual_ZN14LogXLogYDomain31handleHorizontalAxisBaseChangedEd(
    LogXLogYDomain *self,
    qreal baseX) {
  self->handleHorizontalAxisBaseChanged(baseX);
}

//  a Python function taken by a CuteLogXLogYDomain, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_LogXLogYDomain(
    LogXLogYDomain *self,
    const char *key,
    void *call) {
  return static_cast<CuteLogXLogYDomain *>(self)->take(key, call);
}

//  DomainType LogXLogYDomain::type()
extern "C" Q_DECL_EXPORT
AbstractDomain::DomainType ritual_own_ZN14LogXLogYDomain4typeEv(
    LogXLogYDomain *self) {
  return self->LogXLogYDomain::type();
}

//  void LogXLogYDomain::setRange(qreal minX, qreal maxX, qreal minY, qreal
//      maxY)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14LogXLogYDomain8setRangeEdddd(
    LogXLogYDomain *self,
    qreal minX,
    qreal maxX,
    qreal minY,
    qreal maxY) {
  self->LogXLogYDomain::setRange(minX, maxX, minY, maxY);
}

//  void LogXLogYDomain::zoomIn(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14LogXLogYDomain6zoomInERK6QRectF(
    LogXLogYDomain *self,
    const QRectF *rect) {
  self->LogXLogYDomain::zoomIn(*rect);
}

//  void LogXLogYDomain::zoomOut(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14LogXLogYDomain7zoomOutERK6QRectF(
    LogXLogYDomain *self,
    const QRectF *rect) {
  self->LogXLogYDomain::zoomOut(*rect);
}

//  void LogXLogYDomain::move(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14LogXLogYDomain4moveEdd(
    LogXLogYDomain *self,
    qreal dx,
    qreal dy) {
  self->LogXLogYDomain::move(dx, dy);
}

//  QPointF LogXLogYDomain::calculateDomainPoint(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZNK14LogXLogYDomain20calculateDomainPointERK7QPointF(
    const LogXLogYDomain *self,
    const QPointF *point) {
  return new QPointF(self->LogXLogYDomain::calculateDomainPoint(*point));
}

//  bool LogXLogYDomain::attachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14LogXLogYDomain10attachAxisEP13QAbstractAxis(
    LogXLogYDomain *self,
    QAbstractAxis *axis) {
  return self->LogXLogYDomain::attachAxis(axis);
}

//  bool LogXLogYDomain::detachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14LogXLogYDomain10detachAxisEP13QAbstractAxis(
    LogXLogYDomain *self,
    QAbstractAxis *axis) {
  return self->LogXLogYDomain::detachAxis(axis);
}
