//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qvalueaxis_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qvalueaxis.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qvalueaxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QValueAxisPrivate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQValueAxisPrivate : QValueAxisPrivate {
  using QValueAxisPrivate::setMin;
  using QValueAxisPrivate::setMax;
  using QValueAxisPrivate::setRange;
};

//  A QValueAxisPrivate that Python can take functions over in. Every QValueAxisPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQValueAxisPrivateCall0)(const void *, QGraphicsItem *, int *);
typedef void (*CuteQValueAxisPrivateCall1)(const void *, AbstractDomain *, int *);
typedef qreal (*CuteQValueAxisPrivateCall2)(const void *, int *);
typedef qreal (*CuteQValueAxisPrivateCall3)(const void *, int *);
typedef void (*CuteQValueAxisPrivateCall4)(const void *, qreal, qreal, int *);
typedef void (*CuteQValueAxisPrivateCall5)(const void *, const QVariant *, int *);
typedef void (*CuteQValueAxisPrivateCall6)(const void *, const QVariant *, int *);
typedef void (*CuteQValueAxisPrivateCall7)(const void *, const QVariant *, const QVariant *, int *);
typedef void (*CuteQValueAxisPrivateCall8)(const void *, ChartTheme *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQValueAxisPrivateCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQValueAxisPrivateCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValueAxisPrivateCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValueAxisPrivateCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValueAxisPrivateCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValueAxisPrivateCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValueAxisPrivateCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQValueAxisPrivate : public QValueAxisPrivate {
public:
  using QValueAxisPrivate::QValueAxisPrivate;
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

  //  void QValueAxisPrivate::initializeGraphics(QGraphicsItem *parent)
  void initializeGraphics(QGraphicsItem *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQValueAxisPrivateCall0 call = reinterpret_cast<CuteQValueAxisPrivateCall0>(taken[0]);
      call(this, parent, &handled);
      if (handled) return;
    }
    QValueAxisPrivate::initializeGraphics(parent);
  }

  //  void QValueAxisPrivate::initializeDomain(AbstractDomain *domain)
  void initializeDomain(AbstractDomain *domain) override {
    if (taken[1]) {
      int handled = 0;
      CuteQValueAxisPrivateCall1 call = reinterpret_cast<CuteQValueAxisPrivateCall1>(taken[1]);
      call(this, domain, &handled);
      if (handled) return;
    }
    QValueAxisPrivate::initializeDomain(domain);
  }

  //  qreal QValueAxisPrivate::min()
  qreal min() override {
    if (taken[2]) {
      int handled = 0;
      CuteQValueAxisPrivateCall2 call = reinterpret_cast<CuteQValueAxisPrivateCall2>(taken[2]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QValueAxisPrivate::min();
  }

  //  qreal QValueAxisPrivate::max()
  qreal max() override {
    if (taken[3]) {
      int handled = 0;
      CuteQValueAxisPrivateCall3 call = reinterpret_cast<CuteQValueAxisPrivateCall3>(taken[3]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QValueAxisPrivate::max();
  }

  //  void QValueAxisPrivate::setRange(qreal min, qreal max)
  void setRange(qreal min, qreal max) override {
    if (taken[4]) {
      int handled = 0;
      CuteQValueAxisPrivateCall4 call = reinterpret_cast<CuteQValueAxisPrivateCall4>(taken[4]);
      call(this, min, max, &handled);
      if (handled) return;
    }
    QValueAxisPrivate::setRange(min, max);
  }

  //  void QValueAxisPrivate::setMin(const QVariant &min)
  void setMin(const QVariant &min) override {
    if (taken[5]) {
      int handled = 0;
      CuteQValueAxisPrivateCall5 call = reinterpret_cast<CuteQValueAxisPrivateCall5>(taken[5]);
      call(this, &min, &handled);
      if (handled) return;
    }
    QValueAxisPrivate::setMin(min);
  }

  //  void QValueAxisPrivate::setMax(const QVariant &max)
  void setMax(const QVariant &max) override {
    if (taken[6]) {
      int handled = 0;
      CuteQValueAxisPrivateCall6 call = reinterpret_cast<CuteQValueAxisPrivateCall6>(taken[6]);
      call(this, &max, &handled);
      if (handled) return;
    }
    QValueAxisPrivate::setMax(max);
  }

  //  void QValueAxisPrivate::setRange(const QVariant &min, const QVariant
  //      &max)
  void setRange(const QVariant &min, const QVariant &max) override {
    if (taken[7]) {
      int handled = 0;
      CuteQValueAxisPrivateCall7 call = reinterpret_cast<CuteQValueAxisPrivateCall7>(taken[7]);
      call(this, &min, &max, &handled);
      if (handled) return;
    }
    QValueAxisPrivate::setRange(min, max);
  }

  //  void QAbstractAxisPrivate::initializeTheme(ChartTheme *theme, bool
  //      forced)
  void initializeTheme(ChartTheme *theme, bool forced) override {
    if (taken[8]) {
      int handled = 0;
      CuteQValueAxisPrivateCall8 call = reinterpret_cast<CuteQValueAxisPrivateCall8>(taken[8]);
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
      CuteQValueAxisPrivateCall9 call = reinterpret_cast<CuteQValueAxisPrivateCall9>(taken[9]);
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
      CuteQValueAxisPrivateCall10 call = reinterpret_cast<CuteQValueAxisPrivateCall10>(taken[10]);
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
      CuteQValueAxisPrivateCall11 call = reinterpret_cast<CuteQValueAxisPrivateCall11>(taken[11]);
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
      CuteQValueAxisPrivateCall12 call = reinterpret_cast<CuteQValueAxisPrivateCall12>(taken[12]);
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
      CuteQValueAxisPrivateCall13 call = reinterpret_cast<CuteQValueAxisPrivateCall13>(taken[13]);
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
      CuteQValueAxisPrivateCall14 call = reinterpret_cast<CuteQValueAxisPrivateCall14>(taken[14]);
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
      CuteQValueAxisPrivateCall15 call = reinterpret_cast<CuteQValueAxisPrivateCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QValueAxisPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QValueAxisPrivate10metaObjectEv(
    const QValueAxisPrivate *self) {
  return self->metaObject();
}

//  void *QValueAxisPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QValueAxisPrivate11qt_metacastEPKc(
    QValueAxisPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QValueAxisPrivate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QValueAxisPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QValueAxisPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QValueAxisPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QValueAxisPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QValueAxisPrivate::tr(s, c, n));
}

//  QValueAxisPrivate::QValueAxisPrivate(QValueAxis *q)
extern "C" Q_DECL_EXPORT
QValueAxisPrivate *ritual_ZN17QValueAxisPrivateC1EP10QValueAxis(
    QValueAxis *q) {
  return new CuteQValueAxisPrivate(q);
}

//  QValueAxisPrivate::~QValueAxisPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QValueAxisPrivateD1Ev(QValueAxisPrivate *self) {
  delete self;
}

//  void QValueAxisPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QValueAxisPrivate18initializeGraphicsEP13QGraphicsItem(
    QValueAxisPrivate *self,
    QGraphicsItem *parent) {
  self->initializeGraphics(parent);
}

//  void QValueAxisPrivate::initializeDomain(AbstractDomain *domain)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QValueAxisPrivate16initializeDomainEP14AbstractDomain(
    QValueAxisPrivate *self,
    AbstractDomain *domain) {
  self->initializeDomain(domain);
}

//  qreal QValueAxisPrivate::min()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN17QValueAxisPrivate3minEv(QValueAxisPrivate *self) {
  return self->min();
}

//  qreal QValueAxisPrivate::max()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN17QValueAxisPrivate3maxEv(QValueAxisPrivate *self) {
  return self->max();
}

//  void QValueAxisPrivate::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QValueAxisPrivate8setRangeEdd(
    QValueAxisPrivate *self,
    qreal min,
    qreal max) {
  self->setRange(min, max);
}

//  qreal QValueAxisPrivate::tickInterval()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN17QValueAxisPrivate12tickIntervalEv(QValueAxisPrivate *self) {
  return self->tickInterval();
}

//  qreal QValueAxisPrivate::tickAnchor()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN17QValueAxisPrivate10tickAnchorEv(QValueAxisPrivate *self) {
  return self->tickAnchor();
}

//  void QValueAxisPrivate::setMin(const QVariant &min)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QValueAxisPrivate6setMinERK8QVariant(
    QValueAxisPrivate *self,
    const QVariant *min) {
  self->setMin(*min);
}

//  void QValueAxisPrivate::setMax(const QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QValueAxisPrivate6setMaxERK8QVariant(
    QValueAxisPrivate *self,
    const QVariant *max) {
  self->setMax(*max);
}

//  void QValueAxisPrivate::setRange(const QVariant &min, const QVariant
//      &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QValueAxisPrivate8setRangeERK8QVariantS2_(
    QValueAxisPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  self->setRange(*min, *max);
}

//  QValueAxis *QValueAxisPrivate::q_func()
extern "C" Q_DECL_EXPORT
QValueAxis *ritual_ZN17QValueAxisPrivate6q_funcEv(QValueAxisPrivate *self) {
  return self->q_func();
}

//  const QValueAxis *QValueAxisPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QValueAxis *ritual_ZNK17QValueAxisPrivate6q_funcEv(
    const QValueAxisPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQValueAxisPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QValueAxisPrivate(
    QValueAxisPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQValueAxisPrivate *>(self)->take(key, call);
}

//  void QValueAxisPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QValueAxisPrivate18initializeGraphicsEP13QGraphicsItem(
    QValueAxisPrivate *self,
    QGraphicsItem *parent) {
  self->QValueAxisPrivate::initializeGraphics(parent);
}

//  void QValueAxisPrivate::initializeDomain(AbstractDomain *domain)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QValueAxisPrivate16initializeDomainEP14AbstractDomain(
    QValueAxisPrivate *self,
    AbstractDomain *domain) {
  self->QValueAxisPrivate::initializeDomain(domain);
}

//  qreal QValueAxisPrivate::min()
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZN17QValueAxisPrivate3minEv(QValueAxisPrivate *self) {
  return self->QValueAxisPrivate::min();
}

//  qreal QValueAxisPrivate::max()
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZN17QValueAxisPrivate3maxEv(QValueAxisPrivate *self) {
  return self->QValueAxisPrivate::max();
}

//  void QValueAxisPrivate::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QValueAxisPrivate8setRangeEdd(
    QValueAxisPrivate *self,
    qreal min,
    qreal max) {
  self->QValueAxisPrivate::setRange(min, max);
}

//  void QValueAxisPrivate::setMin(const QVariant &min)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QValueAxisPrivate6setMinERK8QVariant(
    QValueAxisPrivate *self,
    const QVariant *min) {
  static_cast<OwnQValueAxisPrivate *>(self)->OwnQValueAxisPrivate::setMin(
      *min);
}

//  void QValueAxisPrivate::setMax(const QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QValueAxisPrivate6setMaxERK8QVariant(
    QValueAxisPrivate *self,
    const QVariant *max) {
  static_cast<OwnQValueAxisPrivate *>(self)->OwnQValueAxisPrivate::setMax(
      *max);
}

//  void QValueAxisPrivate::setRange(const QVariant &min, const QVariant
//      &max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QValueAxisPrivate8setRangeERK8QVariantS2_(
    QValueAxisPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  static_cast<OwnQValueAxisPrivate *>(self)->OwnQValueAxisPrivate::setRange(
      *min,
      *max);
}
