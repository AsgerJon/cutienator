//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qdatetimeaxis_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_datetime_axis)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qdatetimeaxis.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qdatetimeaxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDateTimeAxisPrivate that Python can take functions over in. Every QDateTimeAxisPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDateTimeAxisPrivateCall0)(const void *, QGraphicsItem *, int *);
typedef void (*CuteQDateTimeAxisPrivateCall1)(const void *, AbstractDomain *, int *);
typedef void (*CuteQDateTimeAxisPrivateCall2)(const void *, const QVariant *, int *);
typedef void (*CuteQDateTimeAxisPrivateCall3)(const void *, const QVariant *, int *);
typedef void (*CuteQDateTimeAxisPrivateCall4)(const void *, const QVariant *, const QVariant *, int *);
typedef qreal (*CuteQDateTimeAxisPrivateCall5)(const void *, int *);
typedef qreal (*CuteQDateTimeAxisPrivateCall6)(const void *, int *);
typedef void (*CuteQDateTimeAxisPrivateCall7)(const void *, qreal, qreal, int *);
typedef void (*CuteQDateTimeAxisPrivateCall8)(const void *, ChartTheme *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDateTimeAxisPrivateCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDateTimeAxisPrivateCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDateTimeAxisPrivateCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDateTimeAxisPrivateCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDateTimeAxisPrivateCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDateTimeAxisPrivateCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDateTimeAxisPrivateCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDateTimeAxisPrivate : public QDateTimeAxisPrivate {
public:
  using QDateTimeAxisPrivate::QDateTimeAxisPrivate;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate18initializeGraphicsEP13QGraphicsItem")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate16initializeDomainEP14AbstractDomain")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate6setMinERK8QVariant")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate6setMaxERK8QVariant")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate8setRangeERK8QVariantS2_")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate3minEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate3maxEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate8setRangeEdd")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate15initializeThemeEP10ChartThemeb")) {
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

  //  void QDateTimeAxisPrivate::initializeGraphics(QGraphicsItem *parent)
  void initializeGraphics(QGraphicsItem *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDateTimeAxisPrivateCall0 call = reinterpret_cast<CuteQDateTimeAxisPrivateCall0>(taken[0]);
      call(this, parent, &handled);
      if (handled) return;
    }
    QDateTimeAxisPrivate::initializeGraphics(parent);
  }

  //  void QDateTimeAxisPrivate::initializeDomain(AbstractDomain *domain)
  void initializeDomain(AbstractDomain *domain) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDateTimeAxisPrivateCall1 call = reinterpret_cast<CuteQDateTimeAxisPrivateCall1>(taken[1]);
      call(this, domain, &handled);
      if (handled) return;
    }
    QDateTimeAxisPrivate::initializeDomain(domain);
  }

  //  void QDateTimeAxisPrivate::setMin(const QVariant &min)
  void setMin(const QVariant &min) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDateTimeAxisPrivateCall2 call = reinterpret_cast<CuteQDateTimeAxisPrivateCall2>(taken[2]);
      call(this, &min, &handled);
      if (handled) return;
    }
    QDateTimeAxisPrivate::setMin(min);
  }

  //  void QDateTimeAxisPrivate::setMax(const QVariant &max)
  void setMax(const QVariant &max) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDateTimeAxisPrivateCall3 call = reinterpret_cast<CuteQDateTimeAxisPrivateCall3>(taken[3]);
      call(this, &max, &handled);
      if (handled) return;
    }
    QDateTimeAxisPrivate::setMax(max);
  }

  //  void QDateTimeAxisPrivate::setRange(const QVariant &min, const
  //      QVariant &max)
  void setRange(const QVariant &min, const QVariant &max) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDateTimeAxisPrivateCall4 call = reinterpret_cast<CuteQDateTimeAxisPrivateCall4>(taken[4]);
      call(this, &min, &max, &handled);
      if (handled) return;
    }
    QDateTimeAxisPrivate::setRange(min, max);
  }

  //  qreal QDateTimeAxisPrivate::min()
  qreal min() override {
    if (taken[5]) {
      int handled = 0;
      CuteQDateTimeAxisPrivateCall5 call = reinterpret_cast<CuteQDateTimeAxisPrivateCall5>(taken[5]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QDateTimeAxisPrivate::min();
  }

  //  qreal QDateTimeAxisPrivate::max()
  qreal max() override {
    if (taken[6]) {
      int handled = 0;
      CuteQDateTimeAxisPrivateCall6 call = reinterpret_cast<CuteQDateTimeAxisPrivateCall6>(taken[6]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QDateTimeAxisPrivate::max();
  }

  //  void QDateTimeAxisPrivate::setRange(qreal min, qreal max)
  void setRange(qreal min, qreal max) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDateTimeAxisPrivateCall7 call = reinterpret_cast<CuteQDateTimeAxisPrivateCall7>(taken[7]);
      call(this, min, max, &handled);
      if (handled) return;
    }
    QDateTimeAxisPrivate::setRange(min, max);
  }

  //  void QAbstractAxisPrivate::initializeTheme(ChartTheme *theme, bool
  //      forced)
  void initializeTheme(ChartTheme *theme, bool forced) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDateTimeAxisPrivateCall8 call = reinterpret_cast<CuteQDateTimeAxisPrivateCall8>(taken[8]);
      call(this, theme, forced, &handled);
      if (handled) return;
    }
    QAbstractAxisPrivate::initializeTheme(theme, forced);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDateTimeAxisPrivateCall9 call = reinterpret_cast<CuteQDateTimeAxisPrivateCall9>(taken[9]);
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
      CuteQDateTimeAxisPrivateCall10 call = reinterpret_cast<CuteQDateTimeAxisPrivateCall10>(taken[10]);
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
      CuteQDateTimeAxisPrivateCall11 call = reinterpret_cast<CuteQDateTimeAxisPrivateCall11>(taken[11]);
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
      CuteQDateTimeAxisPrivateCall12 call = reinterpret_cast<CuteQDateTimeAxisPrivateCall12>(taken[12]);
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
      CuteQDateTimeAxisPrivateCall13 call = reinterpret_cast<CuteQDateTimeAxisPrivateCall13>(taken[13]);
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
      CuteQDateTimeAxisPrivateCall14 call = reinterpret_cast<CuteQDateTimeAxisPrivateCall14>(taken[14]);
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
      CuteQDateTimeAxisPrivateCall15 call = reinterpret_cast<CuteQDateTimeAxisPrivateCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDateTimeAxisPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QDateTimeAxisPrivate10metaObjectEv(
    const QDateTimeAxisPrivate *self) {
  return self->metaObject();
}

//  QString QDateTimeAxisPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QDateTimeAxisPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDateTimeAxisPrivate::tr(s, c, n));
}

//  QDateTimeAxisPrivate::QDateTimeAxisPrivate(QDateTimeAxis *q)
extern "C" Q_DECL_EXPORT
QDateTimeAxisPrivate *ritual_ZN20QDateTimeAxisPrivateC1EP13QDateTimeAxis(
    QDateTimeAxis *q) {
  return new CuteQDateTimeAxisPrivate(q);
}

//  QDateTimeAxisPrivate::~QDateTimeAxisPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeAxisPrivateD1Ev(QDateTimeAxisPrivate *self) {
  delete self;
}

//  void QDateTimeAxisPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeAxisPrivate18initializeGraphicsEP13QGraphicsItem(
    QDateTimeAxisPrivate *self,
    QGraphicsItem *parent) {
  self->initializeGraphics(parent);
}

//  void QDateTimeAxisPrivate::initializeDomain(AbstractDomain *domain)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeAxisPrivate16initializeDomainEP14AbstractDomain(
    QDateTimeAxisPrivate *self,
    AbstractDomain *domain) {
  self->initializeDomain(domain);
}

//  void QDateTimeAxisPrivate::setMin(const QVariant &min)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeAxisPrivate6setMinERK8QVariant(
    QDateTimeAxisPrivate *self,
    const QVariant *min) {
  self->setMin(*min);
}

//  void QDateTimeAxisPrivate::setMax(const QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeAxisPrivate6setMaxERK8QVariant(
    QDateTimeAxisPrivate *self,
    const QVariant *max) {
  self->setMax(*max);
}

//  void QDateTimeAxisPrivate::setRange(const QVariant &min, const QVariant
//      &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeAxisPrivate8setRangeERK8QVariantS2_(
    QDateTimeAxisPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  self->setRange(*min, *max);
}

//  qreal QDateTimeAxisPrivate::min()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN20QDateTimeAxisPrivate3minEv(QDateTimeAxisPrivate *self) {
  return self->min();
}

//  qreal QDateTimeAxisPrivate::max()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN20QDateTimeAxisPrivate3maxEv(QDateTimeAxisPrivate *self) {
  return self->max();
}

//  void QDateTimeAxisPrivate::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeAxisPrivate8setRangeEdd(
    QDateTimeAxisPrivate *self,
    qreal min,
    qreal max) {
  self->setRange(min, max);
}

//  QDateTimeAxis *QDateTimeAxisPrivate::q_func()
extern "C" Q_DECL_EXPORT
QDateTimeAxis *ritual_ZN20QDateTimeAxisPrivate6q_funcEv(
    QDateTimeAxisPrivate *self) {
  return self->q_func();
}

//  const QDateTimeAxis *QDateTimeAxisPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QDateTimeAxis *ritual_ZNK20QDateTimeAxisPrivate6q_funcEv(
    const QDateTimeAxisPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQDateTimeAxisPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDateTimeAxisPrivate(
    QDateTimeAxisPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDateTimeAxisPrivate *>(self)->take(key, call);
}

//  void QDateTimeAxisPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDateTimeAxisPrivate18initializeGraphicsEP13QGraphicsItem(
    QDateTimeAxisPrivate *self,
    QGraphicsItem *parent) {
  self->QDateTimeAxisPrivate::initializeGraphics(parent);
}

//  void QDateTimeAxisPrivate::initializeDomain(AbstractDomain *domain)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDateTimeAxisPrivate16initializeDomainEP14AbstractDomain(
    QDateTimeAxisPrivate *self,
    AbstractDomain *domain) {
  self->QDateTimeAxisPrivate::initializeDomain(domain);
}

//  void QDateTimeAxisPrivate::setMin(const QVariant &min)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDateTimeAxisPrivate6setMinERK8QVariant(
    QDateTimeAxisPrivate *self,
    const QVariant *min) {
  self->QDateTimeAxisPrivate::setMin(*min);
}

//  void QDateTimeAxisPrivate::setMax(const QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDateTimeAxisPrivate6setMaxERK8QVariant(
    QDateTimeAxisPrivate *self,
    const QVariant *max) {
  self->QDateTimeAxisPrivate::setMax(*max);
}

//  void QDateTimeAxisPrivate::setRange(const QVariant &min, const QVariant
//      &max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDateTimeAxisPrivate8setRangeERK8QVariantS2_(
    QDateTimeAxisPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  self->QDateTimeAxisPrivate::setRange(*min, *max);
}

//  qreal QDateTimeAxisPrivate::min()
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZN20QDateTimeAxisPrivate3minEv(QDateTimeAxisPrivate *self) {
  return self->QDateTimeAxisPrivate::min();
}

//  qreal QDateTimeAxisPrivate::max()
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZN20QDateTimeAxisPrivate3maxEv(QDateTimeAxisPrivate *self) {
  return self->QDateTimeAxisPrivate::max();
}

//  void QDateTimeAxisPrivate::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDateTimeAxisPrivate8setRangeEdd(
    QDateTimeAxisPrivate *self,
    qreal min,
    qreal max) {
  self->QDateTimeAxisPrivate::setRange(min, max);
}

#endif  // QT_CONFIG(charts_datetime_axis)
