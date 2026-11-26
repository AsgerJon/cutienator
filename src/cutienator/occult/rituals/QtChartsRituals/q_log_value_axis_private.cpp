//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qlogvalueaxis_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qlogvalueaxis.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qlogvalueaxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QLogValueAxisPrivate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQLogValueAxisPrivate : QLogValueAxisPrivate {
  using QLogValueAxisPrivate::setMin;
  using QLogValueAxisPrivate::setMax;
  using QLogValueAxisPrivate::setRange;
};

//  A QLogValueAxisPrivate that Python can take functions over in. Every QLogValueAxisPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQLogValueAxisPrivateCall0)(const void *, QGraphicsItem *, int *);
typedef void (*CuteQLogValueAxisPrivateCall1)(const void *, AbstractDomain *, int *);
typedef qreal (*CuteQLogValueAxisPrivateCall2)(const void *, int *);
typedef qreal (*CuteQLogValueAxisPrivateCall3)(const void *, int *);
typedef void (*CuteQLogValueAxisPrivateCall4)(const void *, qreal, qreal, int *);
typedef void (*CuteQLogValueAxisPrivateCall5)(const void *, const QVariant *, int *);
typedef void (*CuteQLogValueAxisPrivateCall6)(const void *, const QVariant *, int *);
typedef void (*CuteQLogValueAxisPrivateCall7)(const void *, const QVariant *, const QVariant *, int *);
typedef void (*CuteQLogValueAxisPrivateCall8)(const void *, ChartTheme *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLogValueAxisPrivateCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLogValueAxisPrivateCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLogValueAxisPrivateCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLogValueAxisPrivateCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLogValueAxisPrivateCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLogValueAxisPrivateCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLogValueAxisPrivateCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLogValueAxisPrivate : public QLogValueAxisPrivate {
public:
  using QLogValueAxisPrivate::QLogValueAxisPrivate;
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

  //  void QLogValueAxisPrivate::initializeGraphics(QGraphicsItem *parent)
  void initializeGraphics(QGraphicsItem *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQLogValueAxisPrivateCall0 call = reinterpret_cast<CuteQLogValueAxisPrivateCall0>(taken[0]);
      call(this, parent, &handled);
      if (handled) return;
    }
    QLogValueAxisPrivate::initializeGraphics(parent);
  }

  //  void QLogValueAxisPrivate::initializeDomain(AbstractDomain *domain)
  void initializeDomain(AbstractDomain *domain) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLogValueAxisPrivateCall1 call = reinterpret_cast<CuteQLogValueAxisPrivateCall1>(taken[1]);
      call(this, domain, &handled);
      if (handled) return;
    }
    QLogValueAxisPrivate::initializeDomain(domain);
  }

  //  qreal QLogValueAxisPrivate::min()
  qreal min() override {
    if (taken[2]) {
      int handled = 0;
      CuteQLogValueAxisPrivateCall2 call = reinterpret_cast<CuteQLogValueAxisPrivateCall2>(taken[2]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QLogValueAxisPrivate::min();
  }

  //  qreal QLogValueAxisPrivate::max()
  qreal max() override {
    if (taken[3]) {
      int handled = 0;
      CuteQLogValueAxisPrivateCall3 call = reinterpret_cast<CuteQLogValueAxisPrivateCall3>(taken[3]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QLogValueAxisPrivate::max();
  }

  //  void QLogValueAxisPrivate::setRange(qreal min, qreal max)
  void setRange(qreal min, qreal max) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLogValueAxisPrivateCall4 call = reinterpret_cast<CuteQLogValueAxisPrivateCall4>(taken[4]);
      call(this, min, max, &handled);
      if (handled) return;
    }
    QLogValueAxisPrivate::setRange(min, max);
  }

  //  void QLogValueAxisPrivate::setMin(const QVariant &min)
  void setMin(const QVariant &min) override {
    if (taken[5]) {
      int handled = 0;
      CuteQLogValueAxisPrivateCall5 call = reinterpret_cast<CuteQLogValueAxisPrivateCall5>(taken[5]);
      call(this, &min, &handled);
      if (handled) return;
    }
    QLogValueAxisPrivate::setMin(min);
  }

  //  void QLogValueAxisPrivate::setMax(const QVariant &max)
  void setMax(const QVariant &max) override {
    if (taken[6]) {
      int handled = 0;
      CuteQLogValueAxisPrivateCall6 call = reinterpret_cast<CuteQLogValueAxisPrivateCall6>(taken[6]);
      call(this, &max, &handled);
      if (handled) return;
    }
    QLogValueAxisPrivate::setMax(max);
  }

  //  void QLogValueAxisPrivate::setRange(const QVariant &min, const
  //      QVariant &max)
  void setRange(const QVariant &min, const QVariant &max) override {
    if (taken[7]) {
      int handled = 0;
      CuteQLogValueAxisPrivateCall7 call = reinterpret_cast<CuteQLogValueAxisPrivateCall7>(taken[7]);
      call(this, &min, &max, &handled);
      if (handled) return;
    }
    QLogValueAxisPrivate::setRange(min, max);
  }

  //  void QAbstractAxisPrivate::initializeTheme(ChartTheme *theme, bool
  //      forced)
  void initializeTheme(ChartTheme *theme, bool forced) override {
    if (taken[8]) {
      int handled = 0;
      CuteQLogValueAxisPrivateCall8 call = reinterpret_cast<CuteQLogValueAxisPrivateCall8>(taken[8]);
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
      CuteQLogValueAxisPrivateCall9 call = reinterpret_cast<CuteQLogValueAxisPrivateCall9>(taken[9]);
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
      CuteQLogValueAxisPrivateCall10 call = reinterpret_cast<CuteQLogValueAxisPrivateCall10>(taken[10]);
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
      CuteQLogValueAxisPrivateCall11 call = reinterpret_cast<CuteQLogValueAxisPrivateCall11>(taken[11]);
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
      CuteQLogValueAxisPrivateCall12 call = reinterpret_cast<CuteQLogValueAxisPrivateCall12>(taken[12]);
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
      CuteQLogValueAxisPrivateCall13 call = reinterpret_cast<CuteQLogValueAxisPrivateCall13>(taken[13]);
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
      CuteQLogValueAxisPrivateCall14 call = reinterpret_cast<CuteQLogValueAxisPrivateCall14>(taken[14]);
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
      CuteQLogValueAxisPrivateCall15 call = reinterpret_cast<CuteQLogValueAxisPrivateCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLogValueAxisPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QLogValueAxisPrivate10metaObjectEv(
    const QLogValueAxisPrivate *self) {
  return self->metaObject();
}

//  void *QLogValueAxisPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QLogValueAxisPrivate11qt_metacastEPKc(
    QLogValueAxisPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QLogValueAxisPrivate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QLogValueAxisPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QLogValueAxisPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QLogValueAxisPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QLogValueAxisPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QLogValueAxisPrivate::tr(s, c, n));
}

//  QLogValueAxisPrivate::QLogValueAxisPrivate(QLogValueAxis *q)
extern "C" Q_DECL_EXPORT
QLogValueAxisPrivate *ritual_ZN20QLogValueAxisPrivateC1EP13QLogValueAxis(
    QLogValueAxis *q) {
  return new CuteQLogValueAxisPrivate(q);
}

//  QLogValueAxisPrivate::~QLogValueAxisPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLogValueAxisPrivateD1Ev(QLogValueAxisPrivate *self) {
  delete self;
}

//  void QLogValueAxisPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLogValueAxisPrivate18initializeGraphicsEP13QGraphicsItem(
    QLogValueAxisPrivate *self,
    QGraphicsItem *parent) {
  self->initializeGraphics(parent);
}

//  void QLogValueAxisPrivate::initializeDomain(AbstractDomain *domain)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLogValueAxisPrivate16initializeDomainEP14AbstractDomain(
    QLogValueAxisPrivate *self,
    AbstractDomain *domain) {
  self->initializeDomain(domain);
}

//  qreal QLogValueAxisPrivate::min()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN20QLogValueAxisPrivate3minEv(QLogValueAxisPrivate *self) {
  return self->min();
}

//  qreal QLogValueAxisPrivate::max()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN20QLogValueAxisPrivate3maxEv(QLogValueAxisPrivate *self) {
  return self->max();
}

//  void QLogValueAxisPrivate::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLogValueAxisPrivate8setRangeEdd(
    QLogValueAxisPrivate *self,
    qreal min,
    qreal max) {
  self->setRange(min, max);
}

//  void QLogValueAxisPrivate::updateTickCount()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLogValueAxisPrivate15updateTickCountEv(
    QLogValueAxisPrivate *self) {
  self->updateTickCount();
}

//  void QLogValueAxisPrivate::setMin(const QVariant &min)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLogValueAxisPrivate6setMinERK8QVariant(
    QLogValueAxisPrivate *self,
    const QVariant *min) {
  self->setMin(*min);
}

//  void QLogValueAxisPrivate::setMax(const QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLogValueAxisPrivate6setMaxERK8QVariant(
    QLogValueAxisPrivate *self,
    const QVariant *max) {
  self->setMax(*max);
}

//  void QLogValueAxisPrivate::setRange(const QVariant &min, const QVariant
//      &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLogValueAxisPrivate8setRangeERK8QVariantS2_(
    QLogValueAxisPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  self->setRange(*min, *max);
}

//  QLogValueAxis *QLogValueAxisPrivate::q_func()
extern "C" Q_DECL_EXPORT
QLogValueAxis *ritual_ZN20QLogValueAxisPrivate6q_funcEv(
    QLogValueAxisPrivate *self) {
  return self->q_func();
}

//  const QLogValueAxis *QLogValueAxisPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QLogValueAxis *ritual_ZNK20QLogValueAxisPrivate6q_funcEv(
    const QLogValueAxisPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQLogValueAxisPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLogValueAxisPrivate(
    QLogValueAxisPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLogValueAxisPrivate *>(self)->take(key, call);
}

//  void QLogValueAxisPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QLogValueAxisPrivate18initializeGraphicsEP13QGraphicsItem(
    QLogValueAxisPrivate *self,
    QGraphicsItem *parent) {
  self->QLogValueAxisPrivate::initializeGraphics(parent);
}

//  void QLogValueAxisPrivate::initializeDomain(AbstractDomain *domain)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QLogValueAxisPrivate16initializeDomainEP14AbstractDomain(
    QLogValueAxisPrivate *self,
    AbstractDomain *domain) {
  self->QLogValueAxisPrivate::initializeDomain(domain);
}

//  qreal QLogValueAxisPrivate::min()
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZN20QLogValueAxisPrivate3minEv(QLogValueAxisPrivate *self) {
  return self->QLogValueAxisPrivate::min();
}

//  qreal QLogValueAxisPrivate::max()
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZN20QLogValueAxisPrivate3maxEv(QLogValueAxisPrivate *self) {
  return self->QLogValueAxisPrivate::max();
}

//  void QLogValueAxisPrivate::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QLogValueAxisPrivate8setRangeEdd(
    QLogValueAxisPrivate *self,
    qreal min,
    qreal max) {
  self->QLogValueAxisPrivate::setRange(min, max);
}

//  void QLogValueAxisPrivate::setMin(const QVariant &min)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QLogValueAxisPrivate6setMinERK8QVariant(
    QLogValueAxisPrivate *self,
    const QVariant *min) {
  static_cast<OwnQLogValueAxisPrivate *>(self)->OwnQLogValueAxisPrivate::setMin(
      *min);
}

//  void QLogValueAxisPrivate::setMax(const QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QLogValueAxisPrivate6setMaxERK8QVariant(
    QLogValueAxisPrivate *self,
    const QVariant *max) {
  static_cast<OwnQLogValueAxisPrivate *>(self)->OwnQLogValueAxisPrivate::setMax(
      *max);
}

//  void QLogValueAxisPrivate::setRange(const QVariant &min, const QVariant
//      &max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QLogValueAxisPrivate8setRangeERK8QVariantS2_(
    QLogValueAxisPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  static_cast<OwnQLogValueAxisPrivate *>(self)->OwnQLogValueAxisPrivate::setRange(
      *min,
      *max);
}
