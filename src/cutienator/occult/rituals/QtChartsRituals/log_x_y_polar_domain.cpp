//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/logxypolardomain_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/logxypolardomain_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A LogXYPolarDomain that Python can take functions over in. Every LogXYPolarDomain
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteLogXYPolarDomainCall0)(const void *, int *);
typedef void (*CuteLogXYPolarDomainCall1)(const void *, qreal, qreal, qreal, qreal, int *);
typedef void (*CuteLogXYPolarDomainCall2)(const void *, const QRectF *, int *);
typedef void (*CuteLogXYPolarDomainCall3)(const void *, const QRectF *, int *);
typedef void (*CuteLogXYPolarDomainCall4)(const void *, qreal, qreal, int *);
typedef const QPointF * (*CuteLogXYPolarDomainCall5)(const void *, const QPointF *, int *);
typedef bool (*CuteLogXYPolarDomainCall6)(const void *, QAbstractAxis *, int *);
typedef bool (*CuteLogXYPolarDomainCall7)(const void *, QAbstractAxis *, int *);
typedef void (*CuteLogXYPolarDomainCall8)(const void *, const QSizeF *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteLogXYPolarDomainCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteLogXYPolarDomainCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLogXYPolarDomainCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLogXYPolarDomainCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLogXYPolarDomainCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLogXYPolarDomainCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLogXYPolarDomainCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteLogXYPolarDomain : public LogXYPolarDomain {
public:
  using LogXYPolarDomain::LogXYPolarDomain;
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

  //  DomainType LogXYPolarDomain::type()
  AbstractDomain::DomainType type() override {
    if (taken[0]) {
      int handled = 0;
      CuteLogXYPolarDomainCall0 call = reinterpret_cast<CuteLogXYPolarDomainCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<AbstractDomain::DomainType>(given);
    }
    return LogXYPolarDomain::type();
  }

  //  void LogXYPolarDomain::setRange(qreal minX, qreal maxX, qreal minY,
  //      qreal maxY)
  void setRange(qreal minX, qreal maxX, qreal minY, qreal maxY) override {
    if (taken[1]) {
      int handled = 0;
      CuteLogXYPolarDomainCall1 call = reinterpret_cast<CuteLogXYPolarDomainCall1>(taken[1]);
      call(this, minX, maxX, minY, maxY, &handled);
      if (handled) return;
    }
    LogXYPolarDomain::setRange(minX, maxX, minY, maxY);
  }

  //  void LogXYPolarDomain::zoomIn(const QRectF &rect)
  void zoomIn(const QRectF &rect) override {
    if (taken[2]) {
      int handled = 0;
      CuteLogXYPolarDomainCall2 call = reinterpret_cast<CuteLogXYPolarDomainCall2>(taken[2]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    LogXYPolarDomain::zoomIn(rect);
  }

  //  void LogXYPolarDomain::zoomOut(const QRectF &rect)
  void zoomOut(const QRectF &rect) override {
    if (taken[3]) {
      int handled = 0;
      CuteLogXYPolarDomainCall3 call = reinterpret_cast<CuteLogXYPolarDomainCall3>(taken[3]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    LogXYPolarDomain::zoomOut(rect);
  }

  //  void LogXYPolarDomain::move(qreal dx, qreal dy)
  void move(qreal dx, qreal dy) override {
    if (taken[4]) {
      int handled = 0;
      CuteLogXYPolarDomainCall4 call = reinterpret_cast<CuteLogXYPolarDomainCall4>(taken[4]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    LogXYPolarDomain::move(dx, dy);
  }

  //  QPointF LogXYPolarDomain::calculateDomainPoint(const QPointF &point)
  //      const
  QPointF calculateDomainPoint(const QPointF &point) const override {
    if (taken[5]) {
      int handled = 0;
      CuteLogXYPolarDomainCall5 call = reinterpret_cast<CuteLogXYPolarDomainCall5>(taken[5]);
      const QPointF * given = call(this, &point, &handled);
      if (handled && given) return *given;
    }
    return LogXYPolarDomain::calculateDomainPoint(point);
  }

  //  bool LogXYPolarDomain::attachAxis(QAbstractAxis *axis)
  bool attachAxis(QAbstractAxis *axis) override {
    if (taken[6]) {
      int handled = 0;
      CuteLogXYPolarDomainCall6 call = reinterpret_cast<CuteLogXYPolarDomainCall6>(taken[6]);
      bool given = call(this, axis, &handled);
      if (handled) return given;
    }
    return LogXYPolarDomain::attachAxis(axis);
  }

  //  bool LogXYPolarDomain::detachAxis(QAbstractAxis *axis)
  bool detachAxis(QAbstractAxis *axis) override {
    if (taken[7]) {
      int handled = 0;
      CuteLogXYPolarDomainCall7 call = reinterpret_cast<CuteLogXYPolarDomainCall7>(taken[7]);
      bool given = call(this, axis, &handled);
      if (handled) return given;
    }
    return LogXYPolarDomain::detachAxis(axis);
  }

  //  void PolarDomain::setSize(const QSizeF &size)
  void setSize(const QSizeF &size) override {
    if (taken[8]) {
      int handled = 0;
      CuteLogXYPolarDomainCall8 call = reinterpret_cast<CuteLogXYPolarDomainCall8>(taken[8]);
      call(this, &size, &handled);
      if (handled) return;
    }
    PolarDomain::setSize(size);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteLogXYPolarDomainCall9 call = reinterpret_cast<CuteLogXYPolarDomainCall9>(taken[9]);
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
      CuteLogXYPolarDomainCall10 call = reinterpret_cast<CuteLogXYPolarDomainCall10>(taken[10]);
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
      CuteLogXYPolarDomainCall11 call = reinterpret_cast<CuteLogXYPolarDomainCall11>(taken[11]);
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
      CuteLogXYPolarDomainCall12 call = reinterpret_cast<CuteLogXYPolarDomainCall12>(taken[12]);
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
      CuteLogXYPolarDomainCall13 call = reinterpret_cast<CuteLogXYPolarDomainCall13>(taken[13]);
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
      CuteLogXYPolarDomainCall14 call = reinterpret_cast<CuteLogXYPolarDomainCall14>(taken[14]);
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
      CuteLogXYPolarDomainCall15 call = reinterpret_cast<CuteLogXYPolarDomainCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *LogXYPolarDomain::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16LogXYPolarDomain10metaObjectEv(
    const LogXYPolarDomain *self) {
  return self->metaObject();
}

//  void *LogXYPolarDomain::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16LogXYPolarDomain11qt_metacastEPKc(
    LogXYPolarDomain *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int LogXYPolarDomain::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16LogXYPolarDomain11qt_metacallEN11QMetaObject4CallEiPPv(
    LogXYPolarDomain *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString LogXYPolarDomain::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16LogXYPolarDomain2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(LogXYPolarDomain::tr(s, c, n));
}

//  LogXYPolarDomain::LogXYPolarDomain(QObject *object)
extern "C" Q_DECL_EXPORT
LogXYPolarDomain *ritual_ZN16LogXYPolarDomainC1EP7QObject(QObject *object) {
  return new CuteLogXYPolarDomain(object);
}

//  LogXYPolarDomain::~LogXYPolarDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN16LogXYPolarDomainD1Ev(LogXYPolarDomain *self) {
  delete self;
}

//  DomainType LogXYPolarDomain::type()
extern "C" Q_DECL_EXPORT
AbstractDomain::DomainType ritual_ZN16LogXYPolarDomain4typeEv(
    LogXYPolarDomain *self) {
  return self->type();
}

//  void LogXYPolarDomain::setRange(qreal minX, qreal maxX, qreal minY, qreal
//      maxY)
extern "C" Q_DECL_EXPORT
void ritual_ZN16LogXYPolarDomain8setRangeEdddd(
    LogXYPolarDomain *self,
    qreal minX,
    qreal maxX,
    qreal minY,
    qreal maxY) {
  self->setRange(minX, maxX, minY, maxY);
}

//  void LogXYPolarDomain::zoomIn(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN16LogXYPolarDomain6zoomInERK6QRectF(
    LogXYPolarDomain *self,
    const QRectF *rect) {
  self->zoomIn(*rect);
}

//  void LogXYPolarDomain::zoomOut(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN16LogXYPolarDomain7zoomOutERK6QRectF(
    LogXYPolarDomain *self,
    const QRectF *rect) {
  self->zoomOut(*rect);
}

//  void LogXYPolarDomain::move(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN16LogXYPolarDomain4moveEdd(
    LogXYPolarDomain *self,
    qreal dx,
    qreal dy) {
  self->move(dx, dy);
}

//  QPointF LogXYPolarDomain::calculateDomainPoint(const QPointF &point)
//      const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK16LogXYPolarDomain20calculateDomainPointERK7QPointF(
    const LogXYPolarDomain *self,
    const QPointF *point) {
  return new QPointF(self->calculateDomainPoint(*point));
}

//  bool LogXYPolarDomain::attachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16LogXYPolarDomain10attachAxisEP13QAbstractAxis(
    LogXYPolarDomain *self,
    QAbstractAxis *axis) {
  return self->attachAxis(axis);
}

//  bool LogXYPolarDomain::detachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16LogXYPolarDomain10detachAxisEP13QAbstractAxis(
    LogXYPolarDomain *self,
    QAbstractAxis *axis) {
  return self->detachAxis(axis);
}

//  void LogXYPolarDomain::handleHorizontalAxisBaseChanged(qreal baseX)
extern "C" Q_DECL_EXPORT
void ritual_ZN16LogXYPolarDomain31handleHorizontalAxisBaseChangedEd(
    LogXYPolarDomain *self,
    qreal baseX) {
  self->handleHorizontalAxisBaseChanged(baseX);
}

//  qreal LogXYPolarDomain::toAngularCoordinate(qreal value, bool &ok) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16LogXYPolarDomain19toAngularCoordinateEdRb(
    const LogXYPolarDomain *self,
    qreal value,
    bool *ok) {
  return self->toAngularCoordinate(value, *ok);
}

//  qreal LogXYPolarDomain::toRadialCoordinate(qreal value, bool &ok) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16LogXYPolarDomain18toRadialCoordinateEdRb(
    const LogXYPolarDomain *self,
    qreal value,
    bool *ok) {
  return self->toRadialCoordinate(value, *ok);
}

//  a Python function taken by a CuteLogXYPolarDomain, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_LogXYPolarDomain(
    LogXYPolarDomain *self,
    const char *key,
    void *call) {
  return static_cast<CuteLogXYPolarDomain *>(self)->take(key, call);
}

//  DomainType LogXYPolarDomain::type()
extern "C" Q_DECL_EXPORT
AbstractDomain::DomainType ritual_own_ZN16LogXYPolarDomain4typeEv(
    LogXYPolarDomain *self) {
  return self->LogXYPolarDomain::type();
}

//  void LogXYPolarDomain::setRange(qreal minX, qreal maxX, qreal minY, qreal
//      maxY)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16LogXYPolarDomain8setRangeEdddd(
    LogXYPolarDomain *self,
    qreal minX,
    qreal maxX,
    qreal minY,
    qreal maxY) {
  self->LogXYPolarDomain::setRange(minX, maxX, minY, maxY);
}

//  void LogXYPolarDomain::zoomIn(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16LogXYPolarDomain6zoomInERK6QRectF(
    LogXYPolarDomain *self,
    const QRectF *rect) {
  self->LogXYPolarDomain::zoomIn(*rect);
}

//  void LogXYPolarDomain::zoomOut(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16LogXYPolarDomain7zoomOutERK6QRectF(
    LogXYPolarDomain *self,
    const QRectF *rect) {
  self->LogXYPolarDomain::zoomOut(*rect);
}

//  void LogXYPolarDomain::move(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16LogXYPolarDomain4moveEdd(
    LogXYPolarDomain *self,
    qreal dx,
    qreal dy) {
  self->LogXYPolarDomain::move(dx, dy);
}

//  QPointF LogXYPolarDomain::calculateDomainPoint(const QPointF &point)
//      const
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZNK16LogXYPolarDomain20calculateDomainPointERK7QPointF(
    const LogXYPolarDomain *self,
    const QPointF *point) {
  return new QPointF(self->LogXYPolarDomain::calculateDomainPoint(*point));
}

//  bool LogXYPolarDomain::attachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16LogXYPolarDomain10attachAxisEP13QAbstractAxis(
    LogXYPolarDomain *self,
    QAbstractAxis *axis) {
  return self->LogXYPolarDomain::attachAxis(axis);
}

//  bool LogXYPolarDomain::detachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16LogXYPolarDomain10detachAxisEP13QAbstractAxis(
    LogXYPolarDomain *self,
    QAbstractAxis *axis) {
  return self->LogXYPolarDomain::detachAxis(axis);
}
