//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/candlestickanimation_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_candlestick_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/candlestickanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A CandlestickAnimation that Python can take functions over in. Every CandlestickAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteCandlestickAnimationCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteCandlestickAnimationCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCandlestickAnimationCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCandlestickAnimationCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCandlestickAnimationCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCandlestickAnimationCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCandlestickAnimationCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteCandlestickAnimation : public CandlestickAnimation {
public:
  using CandlestickAnimation::CandlestickAnimation;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteCandlestickAnimationCall0 call = reinterpret_cast<CuteCandlestickAnimationCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteCandlestickAnimationCall1 call = reinterpret_cast<CuteCandlestickAnimationCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteCandlestickAnimationCall2 call = reinterpret_cast<CuteCandlestickAnimationCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteCandlestickAnimationCall3 call = reinterpret_cast<CuteCandlestickAnimationCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteCandlestickAnimationCall4 call = reinterpret_cast<CuteCandlestickAnimationCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteCandlestickAnimationCall5 call = reinterpret_cast<CuteCandlestickAnimationCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteCandlestickAnimationCall6 call = reinterpret_cast<CuteCandlestickAnimationCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *CandlestickAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20CandlestickAnimation10metaObjectEv(
    const CandlestickAnimation *self) {
  return self->metaObject();
}

//  QString CandlestickAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20CandlestickAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(CandlestickAnimation::tr(s, c, n));
}

//  CandlestickAnimation::~CandlestickAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN20CandlestickAnimationD1Ev(CandlestickAnimation *self) {
  delete self;
}

//  void CandlestickAnimation::addCandlestick(Candlestick *candlestick)
extern "C" Q_DECL_EXPORT
void ritual_ZN20CandlestickAnimation14addCandlestickEP11Candlestick(
    CandlestickAnimation *self,
    Candlestick *candlestick) {
  self->addCandlestick(candlestick);
}

//  ChartAnimation *CandlestickAnimation::candlestickAnimation(Candlestick
//      *candlestick)
extern "C" Q_DECL_EXPORT
ChartAnimation *ritual_ZN20CandlestickAnimation20candlestickAnimationEP11Candlestick(
    CandlestickAnimation *self,
    Candlestick *candlestick) {
  return self->candlestickAnimation(candlestick);
}

//  ChartAnimation
//      *CandlestickAnimation::candlestickChangeAnimation(Candlestick
//      *candlestick)
extern "C" Q_DECL_EXPORT
ChartAnimation *ritual_ZN20CandlestickAnimation26candlestickChangeAnimationEP11Candlestick(
    CandlestickAnimation *self,
    Candlestick *candlestick) {
  return self->candlestickChangeAnimation(candlestick);
}

//  void CandlestickAnimation::setAnimationStart(Candlestick *candlestick)
extern "C" Q_DECL_EXPORT
void ritual_ZN20CandlestickAnimation17setAnimationStartEP11Candlestick(
    CandlestickAnimation *self,
    Candlestick *candlestick) {
  self->setAnimationStart(candlestick);
}

//  void CandlestickAnimation::stopAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN20CandlestickAnimation7stopAllEv(CandlestickAnimation *self) {
  self->stopAll();
}

//  void CandlestickAnimation::removeCandlestickAnimation(Candlestick
//      *candlestick)
extern "C" Q_DECL_EXPORT
void ritual_ZN20CandlestickAnimation26removeCandlestickAnimationEP11Candlestick(
    CandlestickAnimation *self,
    Candlestick *candlestick) {
  self->removeCandlestickAnimation(candlestick);
}

//  a Python function taken by a CuteCandlestickAnimation, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_CandlestickAnimation(
    CandlestickAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteCandlestickAnimation *>(self)->take(key, call);
}

#endif  // QT_CONFIG(charts_candlestick_chart)
