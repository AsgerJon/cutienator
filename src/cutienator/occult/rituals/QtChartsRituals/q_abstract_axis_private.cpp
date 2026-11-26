//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qabstractaxis_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qabstractaxis.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qabstractaxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAbstractAxisPrivate that Python can take functions over in. Every QAbstractAxisPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstractAxisPrivateCall0)(const void *, AbstractDomain *, int *);
typedef void (*CuteQAbstractAxisPrivateCall1)(const void *, QGraphicsItem *, int *);
typedef void (*CuteQAbstractAxisPrivateCall2)(const void *, ChartTheme *, bool, int *);
typedef void (*CuteQAbstractAxisPrivateCall3)(const void *, const QVariant *, int *);
typedef void (*CuteQAbstractAxisPrivateCall4)(const void *, const QVariant *, int *);
typedef void (*CuteQAbstractAxisPrivateCall5)(const void *, const QVariant *, const QVariant *, int *);
typedef void (*CuteQAbstractAxisPrivateCall6)(const void *, qreal, qreal, int *);
typedef qreal (*CuteQAbstractAxisPrivateCall7)(const void *, int *);
typedef qreal (*CuteQAbstractAxisPrivateCall8)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractAxisPrivateCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractAxisPrivateCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractAxisPrivateCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractAxisPrivateCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractAxisPrivateCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractAxisPrivateCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractAxisPrivateCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractAxisPrivate : public QAbstractAxisPrivate {
public:
  using QAbstractAxisPrivate::QAbstractAxisPrivate;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate16initializeDomainEP14AbstractDomain")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate18initializeGraphicsEP13QGraphicsItem")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate15initializeThemeEP10ChartThemeb")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate6setMinERK8QVariant")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate6setMaxERK8QVariant")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate8setRangeERK8QVariantS2_")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate8setRangeEdd")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate3minEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QAbstractAxisPrivate3maxEv")) {
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

  //  void QAbstractAxisPrivate::initializeDomain(AbstractDomain *domain)
  void initializeDomain(AbstractDomain *domain) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractAxisPrivateCall0 call = reinterpret_cast<CuteQAbstractAxisPrivateCall0>(taken[0]);
      call(this, domain, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractAxisPrivate::initializeGraphics(QGraphicsItem *parent)
  void initializeGraphics(QGraphicsItem *parent) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractAxisPrivateCall1 call = reinterpret_cast<CuteQAbstractAxisPrivateCall1>(taken[1]);
      call(this, parent, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractAxisPrivate::initializeTheme(ChartTheme *theme, bool
  //      forced)
  void initializeTheme(ChartTheme *theme, bool forced) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractAxisPrivateCall2 call = reinterpret_cast<CuteQAbstractAxisPrivateCall2>(taken[2]);
      call(this, theme, forced, &handled);
      if (handled) return;
    }
    QAbstractAxisPrivate::initializeTheme(theme, forced);
  }

  //  void QAbstractAxisPrivate::setMin(const QVariant &min)
  void setMin(const QVariant &min) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractAxisPrivateCall3 call = reinterpret_cast<CuteQAbstractAxisPrivateCall3>(taken[3]);
      call(this, &min, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractAxisPrivate::setMax(const QVariant &max)
  void setMax(const QVariant &max) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractAxisPrivateCall4 call = reinterpret_cast<CuteQAbstractAxisPrivateCall4>(taken[4]);
      call(this, &max, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractAxisPrivate::setRange(const QVariant &min, const
  //      QVariant &max)
  void setRange(const QVariant &min, const QVariant &max) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractAxisPrivateCall5 call = reinterpret_cast<CuteQAbstractAxisPrivateCall5>(taken[5]);
      call(this, &min, &max, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractAxisPrivate::setRange(qreal min, qreal max)
  void setRange(qreal min, qreal max) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractAxisPrivateCall6 call = reinterpret_cast<CuteQAbstractAxisPrivateCall6>(taken[6]);
      call(this, min, max, &handled);
      if (handled) return;
    }
  }

  //  qreal QAbstractAxisPrivate::min()
  qreal min() override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractAxisPrivateCall7 call = reinterpret_cast<CuteQAbstractAxisPrivateCall7>(taken[7]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  qreal QAbstractAxisPrivate::max()
  qreal max() override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractAxisPrivateCall8 call = reinterpret_cast<CuteQAbstractAxisPrivateCall8>(taken[8]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractAxisPrivateCall9 call = reinterpret_cast<CuteQAbstractAxisPrivateCall9>(taken[9]);
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
      CuteQAbstractAxisPrivateCall10 call = reinterpret_cast<CuteQAbstractAxisPrivateCall10>(taken[10]);
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
      CuteQAbstractAxisPrivateCall11 call = reinterpret_cast<CuteQAbstractAxisPrivateCall11>(taken[11]);
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
      CuteQAbstractAxisPrivateCall12 call = reinterpret_cast<CuteQAbstractAxisPrivateCall12>(taken[12]);
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
      CuteQAbstractAxisPrivateCall13 call = reinterpret_cast<CuteQAbstractAxisPrivateCall13>(taken[13]);
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
      CuteQAbstractAxisPrivateCall14 call = reinterpret_cast<CuteQAbstractAxisPrivateCall14>(taken[14]);
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
      CuteQAbstractAxisPrivateCall15 call = reinterpret_cast<CuteQAbstractAxisPrivateCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractAxisPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QAbstractAxisPrivate10metaObjectEv(
    const QAbstractAxisPrivate *self) {
  return self->metaObject();
}

//  void *QAbstractAxisPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QAbstractAxisPrivate11qt_metacastEPKc(
    QAbstractAxisPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractAxisPrivate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QAbstractAxisPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractAxisPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAbstractAxisPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QAbstractAxisPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractAxisPrivate::tr(s, c, n));
}

//  QAbstractAxisPrivate::QAbstractAxisPrivate(QAbstractAxis *q)
extern "C" Q_DECL_EXPORT
QAbstractAxisPrivate *ritual_ZN20QAbstractAxisPrivateC1EP13QAbstractAxis(
    QAbstractAxis *q) {
  return new CuteQAbstractAxisPrivate(q);
}

//  QAbstractAxisPrivate::~QAbstractAxisPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractAxisPrivateD1Ev(QAbstractAxisPrivate *self) {
  delete self;
}

//  Qt::Alignment QAbstractAxisPrivate::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QAbstractAxisPrivate9alignmentEv(
    const QAbstractAxisPrivate *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  Qt::Orientation QAbstractAxisPrivate::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK20QAbstractAxisPrivate11orientationEv(
    const QAbstractAxisPrivate *self) {
  return self->orientation();
}

//  void QAbstractAxisPrivate::setAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractAxisPrivate12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QAbstractAxisPrivate *self,
    int alignment) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  void QAbstractAxisPrivate::setLabelsTruncated(bool labelsTruncated)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractAxisPrivate18setLabelsTruncatedEb(
    QAbstractAxisPrivate *self,
    bool labelsTruncated) {
  self->setLabelsTruncated(labelsTruncated);
}

//  void QAbstractAxisPrivate::initializeDomain(AbstractDomain *domain)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractAxisPrivate16initializeDomainEP14AbstractDomain(
    QAbstractAxisPrivate *self,
    AbstractDomain *domain) {
  self->initializeDomain(domain);
}

//  void QAbstractAxisPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractAxisPrivate18initializeGraphicsEP13QGraphicsItem(
    QAbstractAxisPrivate *self,
    QGraphicsItem *parent) {
  self->initializeGraphics(parent);
}

//  void QAbstractAxisPrivate::initializeTheme(ChartTheme *theme, bool
//      forced)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractAxisPrivate15initializeThemeEP10ChartThemeb(
    QAbstractAxisPrivate *self,
    ChartTheme *theme,
    bool forced) {
  self->initializeTheme(theme, forced);
}

//  void QAbstractAxisPrivate::initializeAnimations(QChart::AnimationOptions
//      options, int duration, QEasingCurve &curve)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractAxisPrivate20initializeAnimationsE6QFlagsIN6QChart15AnimationOptionEEiR12QEasingCurve(
    QAbstractAxisPrivate *self,
    int options,
    int duration,
    QEasingCurve *curve) {
  self->initializeAnimations(
      QFlags<QChart::AnimationOption>::fromInt(options),
      duration,
      *curve);
}

//  void QAbstractAxisPrivate::setMin(const QVariant &min)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractAxisPrivate6setMinERK8QVariant(
    QAbstractAxisPrivate *self,
    const QVariant *min) {
  self->setMin(*min);
}

//  void QAbstractAxisPrivate::setMax(const QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractAxisPrivate6setMaxERK8QVariant(
    QAbstractAxisPrivate *self,
    const QVariant *max) {
  self->setMax(*max);
}

//  void QAbstractAxisPrivate::setRange(const QVariant &min, const QVariant
//      &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractAxisPrivate8setRangeERK8QVariantS2_(
    QAbstractAxisPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  self->setRange(*min, *max);
}

//  void QAbstractAxisPrivate::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractAxisPrivate8setRangeEdd(
    QAbstractAxisPrivate *self,
    qreal min,
    qreal max) {
  self->setRange(min, max);
}

//  qreal QAbstractAxisPrivate::min()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN20QAbstractAxisPrivate3minEv(QAbstractAxisPrivate *self) {
  return self->min();
}

//  qreal QAbstractAxisPrivate::max()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN20QAbstractAxisPrivate3maxEv(QAbstractAxisPrivate *self) {
  return self->max();
}

//  ChartAxisElement *QAbstractAxisPrivate::axisItem()
extern "C" Q_DECL_EXPORT
ChartAxisElement *ritual_ZN20QAbstractAxisPrivate8axisItemEv(
    QAbstractAxisPrivate *self) {
  return self->axisItem();
}

//  void QAbstractAxisPrivate::handleRangeChanged(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractAxisPrivate18handleRangeChangedEdd(
    QAbstractAxisPrivate *self,
    qreal min,
    qreal max) {
  self->handleRangeChanged(min, max);
}

//  void QAbstractAxisPrivate::rangeChanged(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractAxisPrivate12rangeChangedEdd(
    QAbstractAxisPrivate *self,
    qreal min,
    qreal max) {
  self->rangeChanged(min, max);
}

//  QAbstractAxis *QAbstractAxisPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN20QAbstractAxisPrivate6q_funcEv(
    QAbstractAxisPrivate *self) {
  return self->q_func();
}

//  const QAbstractAxis *QAbstractAxisPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractAxis *ritual_ZNK20QAbstractAxisPrivate6q_funcEv(
    const QAbstractAxisPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQAbstractAxisPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractAxisPrivate(
    QAbstractAxisPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractAxisPrivate *>(self)->take(key, call);
}

//  void QAbstractAxisPrivate::initializeTheme(ChartTheme *theme, bool
//      forced)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QAbstractAxisPrivate15initializeThemeEP10ChartThemeb(
    QAbstractAxisPrivate *self,
    ChartTheme *theme,
    bool forced) {
  self->QAbstractAxisPrivate::initializeTheme(theme, forced);
}
