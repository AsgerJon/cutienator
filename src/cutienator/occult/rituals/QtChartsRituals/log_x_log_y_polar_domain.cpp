//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/logxlogypolardomain_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/logxlogypolardomain_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A LogXLogYPolarDomain that Python can take functions over in. Every LogXLogYPolarDomain
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteLogXLogYPolarDomainCall0)(const void *, int *);
typedef void (*CuteLogXLogYPolarDomainCall1)(const void *, qreal, qreal, qreal, qreal, int *);
typedef void (*CuteLogXLogYPolarDomainCall2)(const void *, const QRectF *, int *);
typedef void (*CuteLogXLogYPolarDomainCall3)(const void *, const QRectF *, int *);
typedef void (*CuteLogXLogYPolarDomainCall4)(const void *, qreal, qreal, int *);
typedef const QPointF * (*CuteLogXLogYPolarDomainCall5)(const void *, const QPointF *, int *);
typedef bool (*CuteLogXLogYPolarDomainCall6)(const void *, QAbstractAxis *, int *);
typedef bool (*CuteLogXLogYPolarDomainCall7)(const void *, QAbstractAxis *, int *);
typedef void (*CuteLogXLogYPolarDomainCall8)(const void *, const QSizeF *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteLogXLogYPolarDomainCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteLogXLogYPolarDomainCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLogXLogYPolarDomainCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLogXLogYPolarDomainCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLogXLogYPolarDomainCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLogXLogYPolarDomainCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLogXLogYPolarDomainCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteLogXLogYPolarDomain : public LogXLogYPolarDomain {
public:
  using LogXLogYPolarDomain::LogXLogYPolarDomain;
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

  //  DomainType LogXLogYPolarDomain::type()
  AbstractDomain::DomainType type() override {
    if (taken[0]) {
      int handled = 0;
      CuteLogXLogYPolarDomainCall0 call = reinterpret_cast<CuteLogXLogYPolarDomainCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<AbstractDomain::DomainType>(given);
    }
    return LogXLogYPolarDomain::type();
  }

  //  void LogXLogYPolarDomain::setRange(qreal minX, qreal maxX, qreal
  //      minY, qreal maxY)
  void setRange(qreal minX, qreal maxX, qreal minY, qreal maxY) override {
    if (taken[1]) {
      int handled = 0;
      CuteLogXLogYPolarDomainCall1 call = reinterpret_cast<CuteLogXLogYPolarDomainCall1>(taken[1]);
      call(this, minX, maxX, minY, maxY, &handled);
      if (handled) return;
    }
    LogXLogYPolarDomain::setRange(minX, maxX, minY, maxY);
  }

  //  void LogXLogYPolarDomain::zoomIn(const QRectF &rect)
  void zoomIn(const QRectF &rect) override {
    if (taken[2]) {
      int handled = 0;
      CuteLogXLogYPolarDomainCall2 call = reinterpret_cast<CuteLogXLogYPolarDomainCall2>(taken[2]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    LogXLogYPolarDomain::zoomIn(rect);
  }

  //  void LogXLogYPolarDomain::zoomOut(const QRectF &rect)
  void zoomOut(const QRectF &rect) override {
    if (taken[3]) {
      int handled = 0;
      CuteLogXLogYPolarDomainCall3 call = reinterpret_cast<CuteLogXLogYPolarDomainCall3>(taken[3]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    LogXLogYPolarDomain::zoomOut(rect);
  }

  //  void LogXLogYPolarDomain::move(qreal dx, qreal dy)
  void move(qreal dx, qreal dy) override {
    if (taken[4]) {
      int handled = 0;
      CuteLogXLogYPolarDomainCall4 call = reinterpret_cast<CuteLogXLogYPolarDomainCall4>(taken[4]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    LogXLogYPolarDomain::move(dx, dy);
  }

  //  QPointF LogXLogYPolarDomain::calculateDomainPoint(const QPointF
  //      &point) const
  QPointF calculateDomainPoint(const QPointF &point) const override {
    if (taken[5]) {
      int handled = 0;
      CuteLogXLogYPolarDomainCall5 call = reinterpret_cast<CuteLogXLogYPolarDomainCall5>(taken[5]);
      const QPointF * given = call(this, &point, &handled);
      if (handled && given) return *given;
    }
    return LogXLogYPolarDomain::calculateDomainPoint(point);
  }

  //  bool LogXLogYPolarDomain::attachAxis(QAbstractAxis *axis)
  bool attachAxis(QAbstractAxis *axis) override {
    if (taken[6]) {
      int handled = 0;
      CuteLogXLogYPolarDomainCall6 call = reinterpret_cast<CuteLogXLogYPolarDomainCall6>(taken[6]);
      bool given = call(this, axis, &handled);
      if (handled) return given;
    }
    return LogXLogYPolarDomain::attachAxis(axis);
  }

  //  bool LogXLogYPolarDomain::detachAxis(QAbstractAxis *axis)
  bool detachAxis(QAbstractAxis *axis) override {
    if (taken[7]) {
      int handled = 0;
      CuteLogXLogYPolarDomainCall7 call = reinterpret_cast<CuteLogXLogYPolarDomainCall7>(taken[7]);
      bool given = call(this, axis, &handled);
      if (handled) return given;
    }
    return LogXLogYPolarDomain::detachAxis(axis);
  }

  //  void PolarDomain::setSize(const QSizeF &size)
  void setSize(const QSizeF &size) override {
    if (taken[8]) {
      int handled = 0;
      CuteLogXLogYPolarDomainCall8 call = reinterpret_cast<CuteLogXLogYPolarDomainCall8>(taken[8]);
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
      CuteLogXLogYPolarDomainCall9 call = reinterpret_cast<CuteLogXLogYPolarDomainCall9>(taken[9]);
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
      CuteLogXLogYPolarDomainCall10 call = reinterpret_cast<CuteLogXLogYPolarDomainCall10>(taken[10]);
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
      CuteLogXLogYPolarDomainCall11 call = reinterpret_cast<CuteLogXLogYPolarDomainCall11>(taken[11]);
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
      CuteLogXLogYPolarDomainCall12 call = reinterpret_cast<CuteLogXLogYPolarDomainCall12>(taken[12]);
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
      CuteLogXLogYPolarDomainCall13 call = reinterpret_cast<CuteLogXLogYPolarDomainCall13>(taken[13]);
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
      CuteLogXLogYPolarDomainCall14 call = reinterpret_cast<CuteLogXLogYPolarDomainCall14>(taken[14]);
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
      CuteLogXLogYPolarDomainCall15 call = reinterpret_cast<CuteLogXLogYPolarDomainCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *LogXLogYPolarDomain::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19LogXLogYPolarDomain10metaObjectEv(
    const LogXLogYPolarDomain *self) {
  return self->metaObject();
}

//  QString LogXLogYPolarDomain::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19LogXLogYPolarDomain2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(LogXLogYPolarDomain::tr(s, c, n));
}

//  LogXLogYPolarDomain::LogXLogYPolarDomain(QObject *object)
extern "C" Q_DECL_EXPORT
LogXLogYPolarDomain *ritual_ZN19LogXLogYPolarDomainC1EP7QObject(
    QObject *object) {
  return new CuteLogXLogYPolarDomain(object);
}

//  LogXLogYPolarDomain::~LogXLogYPolarDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN19LogXLogYPolarDomainD1Ev(LogXLogYPolarDomain *self) {
  delete self;
}

//  DomainType LogXLogYPolarDomain::type()
extern "C" Q_DECL_EXPORT
AbstractDomain::DomainType ritual_ZN19LogXLogYPolarDomain4typeEv(
    LogXLogYPolarDomain *self) {
  return self->type();
}

//  void LogXLogYPolarDomain::setRange(qreal minX, qreal maxX, qreal minY,
//      qreal maxY)
extern "C" Q_DECL_EXPORT
void ritual_ZN19LogXLogYPolarDomain8setRangeEdddd(
    LogXLogYPolarDomain *self,
    qreal minX,
    qreal maxX,
    qreal minY,
    qreal maxY) {
  self->setRange(minX, maxX, minY, maxY);
}

//  void LogXLogYPolarDomain::zoomIn(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN19LogXLogYPolarDomain6zoomInERK6QRectF(
    LogXLogYPolarDomain *self,
    const QRectF *rect) {
  self->zoomIn(*rect);
}

//  void LogXLogYPolarDomain::zoomOut(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN19LogXLogYPolarDomain7zoomOutERK6QRectF(
    LogXLogYPolarDomain *self,
    const QRectF *rect) {
  self->zoomOut(*rect);
}

//  void LogXLogYPolarDomain::move(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN19LogXLogYPolarDomain4moveEdd(
    LogXLogYPolarDomain *self,
    qreal dx,
    qreal dy) {
  self->move(dx, dy);
}

//  QPointF LogXLogYPolarDomain::calculateDomainPoint(const QPointF &point)
//      const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK19LogXLogYPolarDomain20calculateDomainPointERK7QPointF(
    const LogXLogYPolarDomain *self,
    const QPointF *point) {
  return new QPointF(self->calculateDomainPoint(*point));
}

//  bool LogXLogYPolarDomain::attachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19LogXLogYPolarDomain10attachAxisEP13QAbstractAxis(
    LogXLogYPolarDomain *self,
    QAbstractAxis *axis) {
  return self->attachAxis(axis);
}

//  bool LogXLogYPolarDomain::detachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19LogXLogYPolarDomain10detachAxisEP13QAbstractAxis(
    LogXLogYPolarDomain *self,
    QAbstractAxis *axis) {
  return self->detachAxis(axis);
}

//  void LogXLogYPolarDomain::handleVerticalAxisBaseChanged(qreal baseY)
extern "C" Q_DECL_EXPORT
void ritual_ZN19LogXLogYPolarDomain29handleVerticalAxisBaseChangedEd(
    LogXLogYPolarDomain *self,
    qreal baseY) {
  self->handleVerticalAxisBaseChanged(baseY);
}

//  void LogXLogYPolarDomain::handleHorizontalAxisBaseChanged(qreal baseX)
extern "C" Q_DECL_EXPORT
void ritual_ZN19LogXLogYPolarDomain31handleHorizontalAxisBaseChangedEd(
    LogXLogYPolarDomain *self,
    qreal baseX) {
  self->handleHorizontalAxisBaseChanged(baseX);
}

//  qreal LogXLogYPolarDomain::toAngularCoordinate(qreal value, bool &ok)
//      const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19LogXLogYPolarDomain19toAngularCoordinateEdRb(
    const LogXLogYPolarDomain *self,
    qreal value,
    bool *ok) {
  return self->toAngularCoordinate(value, *ok);
}

//  qreal LogXLogYPolarDomain::toRadialCoordinate(qreal value, bool &ok)
//      const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19LogXLogYPolarDomain18toRadialCoordinateEdRb(
    const LogXLogYPolarDomain *self,
    qreal value,
    bool *ok) {
  return self->toRadialCoordinate(value, *ok);
}

//  a Python function taken by a CuteLogXLogYPolarDomain, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_LogXLogYPolarDomain(
    LogXLogYPolarDomain *self,
    const char *key,
    void *call) {
  return static_cast<CuteLogXLogYPolarDomain *>(self)->take(key, call);
}

//  DomainType LogXLogYPolarDomain::type()
extern "C" Q_DECL_EXPORT
AbstractDomain::DomainType ritual_own_ZN19LogXLogYPolarDomain4typeEv(
    LogXLogYPolarDomain *self) {
  return self->LogXLogYPolarDomain::type();
}

//  void LogXLogYPolarDomain::setRange(qreal minX, qreal maxX, qreal minY,
//      qreal maxY)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19LogXLogYPolarDomain8setRangeEdddd(
    LogXLogYPolarDomain *self,
    qreal minX,
    qreal maxX,
    qreal minY,
    qreal maxY) {
  self->LogXLogYPolarDomain::setRange(minX, maxX, minY, maxY);
}

//  void LogXLogYPolarDomain::zoomIn(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19LogXLogYPolarDomain6zoomInERK6QRectF(
    LogXLogYPolarDomain *self,
    const QRectF *rect) {
  self->LogXLogYPolarDomain::zoomIn(*rect);
}

//  void LogXLogYPolarDomain::zoomOut(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19LogXLogYPolarDomain7zoomOutERK6QRectF(
    LogXLogYPolarDomain *self,
    const QRectF *rect) {
  self->LogXLogYPolarDomain::zoomOut(*rect);
}

//  void LogXLogYPolarDomain::move(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19LogXLogYPolarDomain4moveEdd(
    LogXLogYPolarDomain *self,
    qreal dx,
    qreal dy) {
  self->LogXLogYPolarDomain::move(dx, dy);
}

//  QPointF LogXLogYPolarDomain::calculateDomainPoint(const QPointF &point)
//      const
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZNK19LogXLogYPolarDomain20calculateDomainPointERK7QPointF(
    const LogXLogYPolarDomain *self,
    const QPointF *point) {
  return new QPointF(
      self->LogXLogYPolarDomain::calculateDomainPoint(
          *point));
}

//  bool LogXLogYPolarDomain::attachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19LogXLogYPolarDomain10attachAxisEP13QAbstractAxis(
    LogXLogYPolarDomain *self,
    QAbstractAxis *axis) {
  return self->LogXLogYPolarDomain::attachAxis(axis);
}

//  bool LogXLogYPolarDomain::detachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19LogXLogYPolarDomain10detachAxisEP13QAbstractAxis(
    LogXLogYPolarDomain *self,
    QAbstractAxis *axis) {
  return self->LogXLogYPolarDomain::detachAxis(axis);
}
