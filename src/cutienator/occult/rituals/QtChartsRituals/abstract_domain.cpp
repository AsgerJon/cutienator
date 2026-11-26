//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/abstractdomain_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/abstractdomain_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A AbstractDomain that Python can take functions over in. Every AbstractDomain
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteAbstractDomainCall0)(const void *, const QSizeF *, int *);
typedef int (*CuteAbstractDomainCall1)(const void *, int *);
typedef void (*CuteAbstractDomainCall2)(const void *, qreal, qreal, qreal, qreal, int *);
typedef void (*CuteAbstractDomainCall3)(const void *, const QRectF *, int *);
typedef void (*CuteAbstractDomainCall4)(const void *, const QRectF *, int *);
typedef void (*CuteAbstractDomainCall5)(const void *, qreal, qreal, int *);
typedef const QPointF * (*CuteAbstractDomainCall6)(const void *, const QPointF *, int *);
typedef bool (*CuteAbstractDomainCall7)(const void *, QAbstractAxis *, int *);
typedef bool (*CuteAbstractDomainCall8)(const void *, QAbstractAxis *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAbstractDomainCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAbstractDomainCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAbstractDomainCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAbstractDomainCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAbstractDomainCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAbstractDomainCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAbstractDomainCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteAbstractDomain : public AbstractDomain {
public:
  using AbstractDomain::AbstractDomain;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14AbstractDomain7setSizeERK6QSizeF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain4typeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain8setRangeEdddd")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain6zoomInERK6QRectF")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain7zoomOutERK6QRectF")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain4moveEdd")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14AbstractDomain20calculateDomainPointERK7QPointF")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain10attachAxisEP13QAbstractAxis")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14AbstractDomain10detachAxisEP13QAbstractAxis")) {
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

  //  void AbstractDomain::setSize(const QSizeF &size)
  void setSize(const QSizeF &size) override {
    if (taken[0]) {
      int handled = 0;
      CuteAbstractDomainCall0 call = reinterpret_cast<CuteAbstractDomainCall0>(taken[0]);
      call(this, &size, &handled);
      if (handled) return;
    }
    AbstractDomain::setSize(size);
  }

  //  DomainType AbstractDomain::type()
  AbstractDomain::DomainType type() override {
    if (taken[1]) {
      int handled = 0;
      CuteAbstractDomainCall1 call = reinterpret_cast<CuteAbstractDomainCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<AbstractDomain::DomainType>(given);
    }
    return {};
  }

  //  void AbstractDomain::setRange(qreal minX, qreal maxX, qreal minY,
  //      qreal maxY)
  void setRange(qreal minX, qreal maxX, qreal minY, qreal maxY) override {
    if (taken[2]) {
      int handled = 0;
      CuteAbstractDomainCall2 call = reinterpret_cast<CuteAbstractDomainCall2>(taken[2]);
      call(this, minX, maxX, minY, maxY, &handled);
      if (handled) return;
    }
  }

  //  void AbstractDomain::zoomIn(const QRectF &rect)
  void zoomIn(const QRectF &rect) override {
    if (taken[3]) {
      int handled = 0;
      CuteAbstractDomainCall3 call = reinterpret_cast<CuteAbstractDomainCall3>(taken[3]);
      call(this, &rect, &handled);
      if (handled) return;
    }
  }

  //  void AbstractDomain::zoomOut(const QRectF &rect)
  void zoomOut(const QRectF &rect) override {
    if (taken[4]) {
      int handled = 0;
      CuteAbstractDomainCall4 call = reinterpret_cast<CuteAbstractDomainCall4>(taken[4]);
      call(this, &rect, &handled);
      if (handled) return;
    }
  }

  //  void AbstractDomain::move(qreal dx, qreal dy)
  void move(qreal dx, qreal dy) override {
    if (taken[5]) {
      int handled = 0;
      CuteAbstractDomainCall5 call = reinterpret_cast<CuteAbstractDomainCall5>(taken[5]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
  }

  //  QPointF AbstractDomain::calculateDomainPoint(const QPointF &point)
  //      const
  QPointF calculateDomainPoint(const QPointF &point) const override {
    if (taken[6]) {
      int handled = 0;
      CuteAbstractDomainCall6 call = reinterpret_cast<CuteAbstractDomainCall6>(taken[6]);
      const QPointF * given = call(this, &point, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool AbstractDomain::attachAxis(QAbstractAxis *axis)
  bool attachAxis(QAbstractAxis *axis) override {
    if (taken[7]) {
      int handled = 0;
      CuteAbstractDomainCall7 call = reinterpret_cast<CuteAbstractDomainCall7>(taken[7]);
      bool given = call(this, axis, &handled);
      if (handled) return given;
    }
    return AbstractDomain::attachAxis(axis);
  }

  //  bool AbstractDomain::detachAxis(QAbstractAxis *axis)
  bool detachAxis(QAbstractAxis *axis) override {
    if (taken[8]) {
      int handled = 0;
      CuteAbstractDomainCall8 call = reinterpret_cast<CuteAbstractDomainCall8>(taken[8]);
      bool given = call(this, axis, &handled);
      if (handled) return given;
    }
    return AbstractDomain::detachAxis(axis);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteAbstractDomainCall9 call = reinterpret_cast<CuteAbstractDomainCall9>(taken[9]);
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
      CuteAbstractDomainCall10 call = reinterpret_cast<CuteAbstractDomainCall10>(taken[10]);
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
      CuteAbstractDomainCall11 call = reinterpret_cast<CuteAbstractDomainCall11>(taken[11]);
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
      CuteAbstractDomainCall12 call = reinterpret_cast<CuteAbstractDomainCall12>(taken[12]);
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
      CuteAbstractDomainCall13 call = reinterpret_cast<CuteAbstractDomainCall13>(taken[13]);
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
      CuteAbstractDomainCall14 call = reinterpret_cast<CuteAbstractDomainCall14>(taken[14]);
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
      CuteAbstractDomainCall15 call = reinterpret_cast<CuteAbstractDomainCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *AbstractDomain::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14AbstractDomain10metaObjectEv(
    const AbstractDomain *self) {
  return self->metaObject();
}

//  void *AbstractDomain::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14AbstractDomain11qt_metacastEPKc(
    AbstractDomain *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int AbstractDomain::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14AbstractDomain11qt_metacallEN11QMetaObject4CallEiPPv(
    AbstractDomain *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString AbstractDomain::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14AbstractDomain2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(AbstractDomain::tr(s, c, n));
}

//  AbstractDomain::~AbstractDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomainD1Ev(AbstractDomain *self) {
  delete self;
}

//  void AbstractDomain::setSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain7setSizeERK6QSizeF(
    AbstractDomain *self,
    const QSizeF *size) {
  self->setSize(*size);
}

//  QSizeF AbstractDomain::size() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK14AbstractDomain4sizeEv(const AbstractDomain *self) {
  return new QSizeF(self->size());
}

//  DomainType AbstractDomain::type()
extern "C" Q_DECL_EXPORT
AbstractDomain::DomainType ritual_ZN14AbstractDomain4typeEv(
    AbstractDomain *self) {
  return self->type();
}

//  void AbstractDomain::setRange(qreal minX, qreal maxX, qreal minY, qreal
//      maxY)
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain8setRangeEdddd(
    AbstractDomain *self,
    qreal minX,
    qreal maxX,
    qreal minY,
    qreal maxY) {
  self->setRange(minX, maxX, minY, maxY);
}

//  void AbstractDomain::setRangeX(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain9setRangeXEdd(
    AbstractDomain *self,
    qreal min,
    qreal max) {
  self->setRangeX(min, max);
}

//  void AbstractDomain::setRangeY(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain9setRangeYEdd(
    AbstractDomain *self,
    qreal min,
    qreal max) {
  self->setRangeY(min, max);
}

//  void AbstractDomain::setMinX(qreal min)
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain7setMinXEd(AbstractDomain *self, qreal min) {
  self->setMinX(min);
}

//  void AbstractDomain::setMaxX(qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain7setMaxXEd(AbstractDomain *self, qreal max) {
  self->setMaxX(max);
}

//  void AbstractDomain::setMinY(qreal min)
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain7setMinYEd(AbstractDomain *self, qreal min) {
  self->setMinY(min);
}

//  void AbstractDomain::setMaxY(qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain7setMaxYEd(AbstractDomain *self, qreal max) {
  self->setMaxY(max);
}

//  qreal AbstractDomain::minX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14AbstractDomain4minXEv(const AbstractDomain *self) {
  return self->minX();
}

//  qreal AbstractDomain::maxX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14AbstractDomain4maxXEv(const AbstractDomain *self) {
  return self->maxX();
}

//  qreal AbstractDomain::minY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14AbstractDomain4minYEv(const AbstractDomain *self) {
  return self->minY();
}

//  qreal AbstractDomain::maxY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14AbstractDomain4maxYEv(const AbstractDomain *self) {
  return self->maxY();
}

//  qreal AbstractDomain::spanX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14AbstractDomain5spanXEv(const AbstractDomain *self) {
  return self->spanX();
}

//  qreal AbstractDomain::spanY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14AbstractDomain5spanYEv(const AbstractDomain *self) {
  return self->spanY();
}

//  bool AbstractDomain::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14AbstractDomain7isEmptyEv(const AbstractDomain *self) {
  return self->isEmpty();
}

//  void AbstractDomain::blockRangeSignals(bool block)
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain17blockRangeSignalsEb(
    AbstractDomain *self,
    bool block) {
  self->blockRangeSignals(block);
}

//  bool AbstractDomain::rangeSignalsBlocked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14AbstractDomain19rangeSignalsBlockedEv(
    const AbstractDomain *self) {
  return self->rangeSignalsBlocked();
}

//  void AbstractDomain::zoomReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain9zoomResetEv(AbstractDomain *self) {
  self->zoomReset();
}

//  void AbstractDomain::storeZoomReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain14storeZoomResetEv(AbstractDomain *self) {
  self->storeZoomReset();
}

//  bool AbstractDomain::isZoomed()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14AbstractDomain8isZoomedEv(AbstractDomain *self) {
  return self->isZoomed();
}

//  void AbstractDomain::zoomIn(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain6zoomInERK6QRectF(
    AbstractDomain *self,
    const QRectF *rect) {
  self->zoomIn(*rect);
}

//  void AbstractDomain::zoomOut(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain7zoomOutERK6QRectF(
    AbstractDomain *self,
    const QRectF *rect) {
  self->zoomOut(*rect);
}

//  void AbstractDomain::move(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain4moveEdd(
    AbstractDomain *self,
    qreal dx,
    qreal dy) {
  self->move(dx, dy);
}

//  QPointF AbstractDomain::calculateGeometryPoint(const QPointF &point, bool
//      &ok) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK14AbstractDomain22calculateGeometryPointERK7QPointFRb(
    const AbstractDomain *self,
    const QPointF *point,
    bool *ok) {
  return new QPointF(self->calculateGeometryPoint(*point, *ok));
}

//  QPointF AbstractDomain::calculateDomainPoint(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK14AbstractDomain20calculateDomainPointERK7QPointF(
    const AbstractDomain *self,
    const QPointF *point) {
  return new QPointF(self->calculateDomainPoint(*point));
}

//  QList<QPointF> AbstractDomain::calculateGeometryPoints(const
//      QList<QPointF> &list) const
extern "C" Q_DECL_EXPORT
QList<QPointF> *ritual_ZNK14AbstractDomain23calculateGeometryPointsERK5QListI7QPointFE(
    const AbstractDomain *self,
    const QList<QPointF> *list) {
  return new QList<QPointF>(self->calculateGeometryPoints(*list));
}

//  bool AbstractDomain::attachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14AbstractDomain10attachAxisEP13QAbstractAxis(
    AbstractDomain *self,
    QAbstractAxis *axis) {
  return self->attachAxis(axis);
}

//  bool AbstractDomain::detachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14AbstractDomain10detachAxisEP13QAbstractAxis(
    AbstractDomain *self,
    QAbstractAxis *axis) {
  return self->detachAxis(axis);
}

//  void AbstractDomain::looseNiceNumbers(qreal &min, qreal &max, int
//      &ticksCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain16looseNiceNumbersERdS0_Ri(
    qreal *min,
    qreal *max,
    int *ticksCount) {
  AbstractDomain::looseNiceNumbers(*min, *max, *ticksCount);
}

//  qreal AbstractDomain::niceNumber(qreal x, bool ceiling)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN14AbstractDomain10niceNumberEdb(qreal x, bool ceiling) {
  return AbstractDomain::niceNumber(x, ceiling);
}

//  void AbstractDomain::setReverseX(bool reverse)
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain11setReverseXEb(
    AbstractDomain *self,
    bool reverse) {
  self->setReverseX(reverse);
}

//  void AbstractDomain::setReverseY(bool reverse)
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain11setReverseYEb(
    AbstractDomain *self,
    bool reverse) {
  self->setReverseY(reverse);
}

//  bool AbstractDomain::isReverseX() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14AbstractDomain10isReverseXEv(const AbstractDomain *self) {
  return self->isReverseX();
}

//  bool AbstractDomain::isReverseY() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14AbstractDomain10isReverseYEv(const AbstractDomain *self) {
  return self->isReverseY();
}

//  void AbstractDomain::updated()
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain7updatedEv(AbstractDomain *self) {
  self->updated();
}

//  void AbstractDomain::rangeHorizontalChanged(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain22rangeHorizontalChangedEdd(
    AbstractDomain *self,
    qreal min,
    qreal max) {
  self->rangeHorizontalChanged(min, max);
}

//  void AbstractDomain::rangeVerticalChanged(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain20rangeVerticalChangedEdd(
    AbstractDomain *self,
    qreal min,
    qreal max) {
  self->rangeVerticalChanged(min, max);
}

//  void AbstractDomain::handleVerticalAxisRangeChanged(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain30handleVerticalAxisRangeChangedEdd(
    AbstractDomain *self,
    qreal min,
    qreal max) {
  self->handleVerticalAxisRangeChanged(min, max);
}

//  void AbstractDomain::handleHorizontalAxisRangeChanged(qreal min, qreal
//      max)
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain32handleHorizontalAxisRangeChangedEdd(
    AbstractDomain *self,
    qreal min,
    qreal max) {
  self->handleHorizontalAxisRangeChanged(min, max);
}

//  void AbstractDomain::handleReverseXChanged(bool reverse)
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain21handleReverseXChangedEb(
    AbstractDomain *self,
    bool reverse) {
  self->handleReverseXChanged(reverse);
}

//  void AbstractDomain::handleReverseYChanged(bool reverse)
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain21handleReverseYChangedEb(
    AbstractDomain *self,
    bool reverse) {
  self->handleReverseYChanged(reverse);
}

//  void AbstractDomain::adjustLogDomainRanges(qreal &min, qreal &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN14AbstractDomain21adjustLogDomainRangesERdS0_(
    AbstractDomain *self,
    qreal *min,
    qreal *max) {
  self->adjustLogDomainRanges(*min, *max);
}

//  QRectF AbstractDomain::fixZoomRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN14AbstractDomain11fixZoomRectERK6QRectF(
    AbstractDomain *self,
    const QRectF *rect) {
  return new QRectF(self->fixZoomRect(*rect));
}

//  a Python function taken by a CuteAbstractDomain, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_AbstractDomain(
    AbstractDomain *self,
    const char *key,
    void *call) {
  return static_cast<CuteAbstractDomain *>(self)->take(key, call);
}

//  void AbstractDomain::setSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14AbstractDomain7setSizeERK6QSizeF(
    AbstractDomain *self,
    const QSizeF *size) {
  self->AbstractDomain::setSize(*size);
}

//  bool AbstractDomain::attachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14AbstractDomain10attachAxisEP13QAbstractAxis(
    AbstractDomain *self,
    QAbstractAxis *axis) {
  return self->AbstractDomain::attachAxis(axis);
}

//  bool AbstractDomain::detachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14AbstractDomain10detachAxisEP13QAbstractAxis(
    AbstractDomain *self,
    QAbstractAxis *axis) {
  return self->AbstractDomain::detachAxis(axis);
}
