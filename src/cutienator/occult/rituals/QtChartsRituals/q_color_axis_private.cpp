//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qcoloraxis_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qcoloraxis.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qcoloraxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QColorAxisPrivate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQColorAxisPrivate : QColorAxisPrivate {
  using QColorAxisPrivate::setMin;
  using QColorAxisPrivate::setMax;
  using QColorAxisPrivate::setRange;
};

//  A QColorAxisPrivate that Python can take functions over in. Every QColorAxisPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQColorAxisPrivateCall0)(const void *, QGraphicsItem *, int *);
typedef void (*CuteQColorAxisPrivateCall1)(const void *, AbstractDomain *, int *);
typedef qreal (*CuteQColorAxisPrivateCall2)(const void *, int *);
typedef qreal (*CuteQColorAxisPrivateCall3)(const void *, int *);
typedef void (*CuteQColorAxisPrivateCall4)(const void *, qreal, qreal, int *);
typedef void (*CuteQColorAxisPrivateCall5)(const void *, const QVariant *, int *);
typedef void (*CuteQColorAxisPrivateCall6)(const void *, const QVariant *, int *);
typedef void (*CuteQColorAxisPrivateCall7)(const void *, const QVariant *, const QVariant *, int *);
typedef void (*CuteQColorAxisPrivateCall8)(const void *, ChartTheme *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQColorAxisPrivateCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQColorAxisPrivateCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQColorAxisPrivateCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQColorAxisPrivateCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQColorAxisPrivateCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQColorAxisPrivateCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQColorAxisPrivateCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQColorAxisPrivate : public QColorAxisPrivate {
public:
  using QColorAxisPrivate::QColorAxisPrivate;
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
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate3minEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate3maxEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate8setRangeEdd")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate6setMinERK8QVariant")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate6setMaxERK8QVariant")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate8setRangeERK8QVariantS2_")) {
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

  //  void QColorAxisPrivate::initializeGraphics(QGraphicsItem *parent)
  void initializeGraphics(QGraphicsItem *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQColorAxisPrivateCall0 call = reinterpret_cast<CuteQColorAxisPrivateCall0>(taken[0]);
      call(this, parent, &handled);
      if (handled) return;
    }
    QColorAxisPrivate::initializeGraphics(parent);
  }

  //  void QColorAxisPrivate::initializeDomain(AbstractDomain *domain)
  void initializeDomain(AbstractDomain *domain) override {
    if (taken[1]) {
      int handled = 0;
      CuteQColorAxisPrivateCall1 call = reinterpret_cast<CuteQColorAxisPrivateCall1>(taken[1]);
      call(this, domain, &handled);
      if (handled) return;
    }
    QColorAxisPrivate::initializeDomain(domain);
  }

  //  qreal QColorAxisPrivate::min()
  qreal min() override {
    if (taken[2]) {
      int handled = 0;
      CuteQColorAxisPrivateCall2 call = reinterpret_cast<CuteQColorAxisPrivateCall2>(taken[2]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QColorAxisPrivate::min();
  }

  //  qreal QColorAxisPrivate::max()
  qreal max() override {
    if (taken[3]) {
      int handled = 0;
      CuteQColorAxisPrivateCall3 call = reinterpret_cast<CuteQColorAxisPrivateCall3>(taken[3]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QColorAxisPrivate::max();
  }

  //  void QColorAxisPrivate::setRange(qreal min, qreal max)
  void setRange(qreal min, qreal max) override {
    if (taken[4]) {
      int handled = 0;
      CuteQColorAxisPrivateCall4 call = reinterpret_cast<CuteQColorAxisPrivateCall4>(taken[4]);
      call(this, min, max, &handled);
      if (handled) return;
    }
    QColorAxisPrivate::setRange(min, max);
  }

  //  void QColorAxisPrivate::setMin(const QVariant &min)
  void setMin(const QVariant &min) override {
    if (taken[5]) {
      int handled = 0;
      CuteQColorAxisPrivateCall5 call = reinterpret_cast<CuteQColorAxisPrivateCall5>(taken[5]);
      call(this, &min, &handled);
      if (handled) return;
    }
    QColorAxisPrivate::setMin(min);
  }

  //  void QColorAxisPrivate::setMax(const QVariant &max)
  void setMax(const QVariant &max) override {
    if (taken[6]) {
      int handled = 0;
      CuteQColorAxisPrivateCall6 call = reinterpret_cast<CuteQColorAxisPrivateCall6>(taken[6]);
      call(this, &max, &handled);
      if (handled) return;
    }
    QColorAxisPrivate::setMax(max);
  }

  //  void QColorAxisPrivate::setRange(const QVariant &min, const QVariant
  //      &max)
  void setRange(const QVariant &min, const QVariant &max) override {
    if (taken[7]) {
      int handled = 0;
      CuteQColorAxisPrivateCall7 call = reinterpret_cast<CuteQColorAxisPrivateCall7>(taken[7]);
      call(this, &min, &max, &handled);
      if (handled) return;
    }
    QColorAxisPrivate::setRange(min, max);
  }

  //  void QAbstractAxisPrivate::initializeTheme(ChartTheme *theme, bool
  //      forced)
  void initializeTheme(ChartTheme *theme, bool forced) override {
    if (taken[8]) {
      int handled = 0;
      CuteQColorAxisPrivateCall8 call = reinterpret_cast<CuteQColorAxisPrivateCall8>(taken[8]);
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
      CuteQColorAxisPrivateCall9 call = reinterpret_cast<CuteQColorAxisPrivateCall9>(taken[9]);
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
      CuteQColorAxisPrivateCall10 call = reinterpret_cast<CuteQColorAxisPrivateCall10>(taken[10]);
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
      CuteQColorAxisPrivateCall11 call = reinterpret_cast<CuteQColorAxisPrivateCall11>(taken[11]);
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
      CuteQColorAxisPrivateCall12 call = reinterpret_cast<CuteQColorAxisPrivateCall12>(taken[12]);
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
      CuteQColorAxisPrivateCall13 call = reinterpret_cast<CuteQColorAxisPrivateCall13>(taken[13]);
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
      CuteQColorAxisPrivateCall14 call = reinterpret_cast<CuteQColorAxisPrivateCall14>(taken[14]);
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
      CuteQColorAxisPrivateCall15 call = reinterpret_cast<CuteQColorAxisPrivateCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QColorAxisPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QColorAxisPrivate10metaObjectEv(
    const QColorAxisPrivate *self) {
  return self->metaObject();
}

//  QString QColorAxisPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QColorAxisPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QColorAxisPrivate::tr(s, c, n));
}

//  QColorAxisPrivate::QColorAxisPrivate(QColorAxis *q)
extern "C" Q_DECL_EXPORT
QColorAxisPrivate *ritual_ZN17QColorAxisPrivateC1EP10QColorAxis(
    QColorAxis *q) {
  return new CuteQColorAxisPrivate(q);
}

//  QColorAxisPrivate::~QColorAxisPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QColorAxisPrivateD1Ev(QColorAxisPrivate *self) {
  delete self;
}

//  void QColorAxisPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QColorAxisPrivate18initializeGraphicsEP13QGraphicsItem(
    QColorAxisPrivate *self,
    QGraphicsItem *parent) {
  self->initializeGraphics(parent);
}

//  void QColorAxisPrivate::initializeDomain(AbstractDomain *domain)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QColorAxisPrivate16initializeDomainEP14AbstractDomain(
    QColorAxisPrivate *self,
    AbstractDomain *domain) {
  self->initializeDomain(domain);
}

//  qreal QColorAxisPrivate::min()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN17QColorAxisPrivate3minEv(QColorAxisPrivate *self) {
  return self->min();
}

//  qreal QColorAxisPrivate::max()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN17QColorAxisPrivate3maxEv(QColorAxisPrivate *self) {
  return self->max();
}

//  void QColorAxisPrivate::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QColorAxisPrivate8setRangeEdd(
    QColorAxisPrivate *self,
    qreal min,
    qreal max) {
  self->setRange(min, max);
}

//  void QColorAxisPrivate::updateSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QColorAxisPrivate12updateSeriesEv(QColorAxisPrivate *self) {
  self->updateSeries();
}

//  void QColorAxisPrivate::setMin(const QVariant &min)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QColorAxisPrivate6setMinERK8QVariant(
    QColorAxisPrivate *self,
    const QVariant *min) {
  self->setMin(*min);
}

//  void QColorAxisPrivate::setMax(const QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QColorAxisPrivate6setMaxERK8QVariant(
    QColorAxisPrivate *self,
    const QVariant *max) {
  self->setMax(*max);
}

//  void QColorAxisPrivate::setRange(const QVariant &min, const QVariant
//      &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QColorAxisPrivate8setRangeERK8QVariantS2_(
    QColorAxisPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  self->setRange(*min, *max);
}

//  QColorAxis *QColorAxisPrivate::q_func()
extern "C" Q_DECL_EXPORT
QColorAxis *ritual_ZN17QColorAxisPrivate6q_funcEv(QColorAxisPrivate *self) {
  return self->q_func();
}

//  const QColorAxis *QColorAxisPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QColorAxis *ritual_ZNK17QColorAxisPrivate6q_funcEv(
    const QColorAxisPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQColorAxisPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QColorAxisPrivate(
    QColorAxisPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQColorAxisPrivate *>(self)->take(key, call);
}

//  void QColorAxisPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QColorAxisPrivate18initializeGraphicsEP13QGraphicsItem(
    QColorAxisPrivate *self,
    QGraphicsItem *parent) {
  self->QColorAxisPrivate::initializeGraphics(parent);
}

//  void QColorAxisPrivate::initializeDomain(AbstractDomain *domain)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QColorAxisPrivate16initializeDomainEP14AbstractDomain(
    QColorAxisPrivate *self,
    AbstractDomain *domain) {
  self->QColorAxisPrivate::initializeDomain(domain);
}

//  qreal QColorAxisPrivate::min()
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZN17QColorAxisPrivate3minEv(QColorAxisPrivate *self) {
  return self->QColorAxisPrivate::min();
}

//  qreal QColorAxisPrivate::max()
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZN17QColorAxisPrivate3maxEv(QColorAxisPrivate *self) {
  return self->QColorAxisPrivate::max();
}

//  void QColorAxisPrivate::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QColorAxisPrivate8setRangeEdd(
    QColorAxisPrivate *self,
    qreal min,
    qreal max) {
  self->QColorAxisPrivate::setRange(min, max);
}

//  void QColorAxisPrivate::setMin(const QVariant &min)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QColorAxisPrivate6setMinERK8QVariant(
    QColorAxisPrivate *self,
    const QVariant *min) {
  static_cast<OwnQColorAxisPrivate *>(self)->OwnQColorAxisPrivate::setMin(
      *min);
}

//  void QColorAxisPrivate::setMax(const QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QColorAxisPrivate6setMaxERK8QVariant(
    QColorAxisPrivate *self,
    const QVariant *max) {
  static_cast<OwnQColorAxisPrivate *>(self)->OwnQColorAxisPrivate::setMax(
      *max);
}

//  void QColorAxisPrivate::setRange(const QVariant &min, const QVariant
//      &max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QColorAxisPrivate8setRangeERK8QVariantS2_(
    QColorAxisPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  static_cast<OwnQColorAxisPrivate *>(self)->OwnQColorAxisPrivate::setRange(
      *min,
      *max);
}
