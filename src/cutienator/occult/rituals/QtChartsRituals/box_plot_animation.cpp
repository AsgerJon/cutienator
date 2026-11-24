//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/boxplotanimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_boxplot_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/boxplotanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A BoxPlotAnimation that Python can take functions over in. Every BoxPlotAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteBoxPlotAnimationCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteBoxPlotAnimationCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBoxPlotAnimationCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBoxPlotAnimationCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBoxPlotAnimationCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBoxPlotAnimationCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBoxPlotAnimationCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteBoxPlotAnimation : public BoxPlotAnimation {
public:
  using BoxPlotAnimation::BoxPlotAnimation;
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
      CuteBoxPlotAnimationCall0 call = reinterpret_cast<CuteBoxPlotAnimationCall0>(taken[0]);
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
      CuteBoxPlotAnimationCall1 call = reinterpret_cast<CuteBoxPlotAnimationCall1>(taken[1]);
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
      CuteBoxPlotAnimationCall2 call = reinterpret_cast<CuteBoxPlotAnimationCall2>(taken[2]);
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
      CuteBoxPlotAnimationCall3 call = reinterpret_cast<CuteBoxPlotAnimationCall3>(taken[3]);
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
      CuteBoxPlotAnimationCall4 call = reinterpret_cast<CuteBoxPlotAnimationCall4>(taken[4]);
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
      CuteBoxPlotAnimationCall5 call = reinterpret_cast<CuteBoxPlotAnimationCall5>(taken[5]);
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
      CuteBoxPlotAnimationCall6 call = reinterpret_cast<CuteBoxPlotAnimationCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *BoxPlotAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16BoxPlotAnimation10metaObjectEv(
    const BoxPlotAnimation *self) {
  return self->metaObject();
}

//  QString BoxPlotAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16BoxPlotAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(BoxPlotAnimation::tr(s, c, n));
}

//  BoxPlotAnimation::~BoxPlotAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN16BoxPlotAnimationD1Ev(BoxPlotAnimation *self) {
  delete self;
}

//  void BoxPlotAnimation::addBox(BoxWhiskers *box)
extern "C" Q_DECL_EXPORT
void ritual_ZN16BoxPlotAnimation6addBoxEP11BoxWhiskers(
    BoxPlotAnimation *self,
    BoxWhiskers *box) {
  self->addBox(box);
}

//  ChartAnimation *BoxPlotAnimation::boxAnimation(BoxWhiskers *box)
extern "C" Q_DECL_EXPORT
ChartAnimation *ritual_ZN16BoxPlotAnimation12boxAnimationEP11BoxWhiskers(
    BoxPlotAnimation *self,
    BoxWhiskers *box) {
  return self->boxAnimation(box);
}

//  ChartAnimation *BoxPlotAnimation::boxChangeAnimation(BoxWhiskers *box)
extern "C" Q_DECL_EXPORT
ChartAnimation *ritual_ZN16BoxPlotAnimation18boxChangeAnimationEP11BoxWhiskers(
    BoxPlotAnimation *self,
    BoxWhiskers *box) {
  return self->boxChangeAnimation(box);
}

//  void BoxPlotAnimation::setAnimationStart(BoxWhiskers *box)
extern "C" Q_DECL_EXPORT
void ritual_ZN16BoxPlotAnimation17setAnimationStartEP11BoxWhiskers(
    BoxPlotAnimation *self,
    BoxWhiskers *box) {
  self->setAnimationStart(box);
}

//  void BoxPlotAnimation::stopAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN16BoxPlotAnimation7stopAllEv(BoxPlotAnimation *self) {
  self->stopAll();
}

//  void BoxPlotAnimation::removeBoxAnimation(BoxWhiskers *box)
extern "C" Q_DECL_EXPORT
void ritual_ZN16BoxPlotAnimation18removeBoxAnimationEP11BoxWhiskers(
    BoxPlotAnimation *self,
    BoxWhiskers *box) {
  self->removeBoxAnimation(box);
}

//  a Python function taken by a CuteBoxPlotAnimation, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_BoxPlotAnimation(
    BoxPlotAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteBoxPlotAnimation *>(self)->take(key, call);
}

#endif  // QT_CONFIG(charts_boxplot_chart)
