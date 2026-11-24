//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qpieslice_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_pie_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qpieslice.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qpieslice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qpen.h>
#include <QtGui/qbrush.h>
#include <QtGui/qfont.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPieSlicePrivate that Python can take functions over in. Every QPieSlicePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPieSlicePrivateCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPieSlicePrivateCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieSlicePrivateCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieSlicePrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieSlicePrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieSlicePrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieSlicePrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPieSlicePrivate : public QPieSlicePrivate {
public:
  using QPieSlicePrivate::QPieSlicePrivate;
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
      CuteQPieSlicePrivateCall0 call = reinterpret_cast<CuteQPieSlicePrivateCall0>(taken[0]);
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
      CuteQPieSlicePrivateCall1 call = reinterpret_cast<CuteQPieSlicePrivateCall1>(taken[1]);
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
      CuteQPieSlicePrivateCall2 call = reinterpret_cast<CuteQPieSlicePrivateCall2>(taken[2]);
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
      CuteQPieSlicePrivateCall3 call = reinterpret_cast<CuteQPieSlicePrivateCall3>(taken[3]);
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
      CuteQPieSlicePrivateCall4 call = reinterpret_cast<CuteQPieSlicePrivateCall4>(taken[4]);
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
      CuteQPieSlicePrivateCall5 call = reinterpret_cast<CuteQPieSlicePrivateCall5>(taken[5]);
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
      CuteQPieSlicePrivateCall6 call = reinterpret_cast<CuteQPieSlicePrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPieSlicePrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QPieSlicePrivate10metaObjectEv(
    const QPieSlicePrivate *self) {
  return self->metaObject();
}

//  QString QPieSlicePrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QPieSlicePrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPieSlicePrivate::tr(s, c, n));
}

//  QPieSlicePrivate::QPieSlicePrivate(QPieSlice *parent)
extern "C" Q_DECL_EXPORT
QPieSlicePrivate *ritual_ZN16QPieSlicePrivateC1EP9QPieSlice(
    QPieSlice *parent) {
  return new CuteQPieSlicePrivate(parent);
}

//  QPieSlicePrivate::~QPieSlicePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPieSlicePrivateD1Ev(QPieSlicePrivate *self) {
  delete self;
}

//  QPieSlicePrivate *QPieSlicePrivate::fromSlice(QPieSlice *slice)
extern "C" Q_DECL_EXPORT
QPieSlicePrivate *ritual_ZN16QPieSlicePrivate9fromSliceEP9QPieSlice(
    QPieSlice *slice) {
  return QPieSlicePrivate::fromSlice(slice);
}

//  void QPieSlicePrivate::setPen(const QPen &pen, bool themed)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPieSlicePrivate6setPenERK4QPenb(
    QPieSlicePrivate *self,
    const QPen *pen,
    bool themed) {
  self->setPen(*pen, themed);
}

//  void QPieSlicePrivate::setBrush(const QBrush &brush, bool themed)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPieSlicePrivate8setBrushERK6QBrushb(
    QPieSlicePrivate *self,
    const QBrush *brush,
    bool themed) {
  self->setBrush(*brush, themed);
}

//  void QPieSlicePrivate::setLabelBrush(const QBrush &brush, bool themed)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPieSlicePrivate13setLabelBrushERK6QBrushb(
    QPieSlicePrivate *self,
    const QBrush *brush,
    bool themed) {
  self->setLabelBrush(*brush, themed);
}

//  void QPieSlicePrivate::setLabelFont(const QFont &font, bool themed)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPieSlicePrivate12setLabelFontERK5QFontb(
    QPieSlicePrivate *self,
    const QFont *font,
    bool themed) {
  self->setLabelFont(*font, themed);
}

//  void QPieSlicePrivate::setPercentage(qreal percentage)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPieSlicePrivate13setPercentageEd(
    QPieSlicePrivate *self,
    qreal percentage) {
  self->setPercentage(percentage);
}

//  void QPieSlicePrivate::setStartAngle(qreal angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPieSlicePrivate13setStartAngleEd(
    QPieSlicePrivate *self,
    qreal angle) {
  self->setStartAngle(angle);
}

//  void QPieSlicePrivate::setAngleSpan(qreal span)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPieSlicePrivate12setAngleSpanEd(
    QPieSlicePrivate *self,
    qreal span) {
  self->setAngleSpan(span);
}

//  QPieSlice *QPieSlicePrivate::q_func()
extern "C" Q_DECL_EXPORT
QPieSlice *ritual_ZN16QPieSlicePrivate6q_funcEv(QPieSlicePrivate *self) {
  return self->q_func();
}

//  const QPieSlice *QPieSlicePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPieSlice *ritual_ZNK16QPieSlicePrivate6q_funcEv(
    const QPieSlicePrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQPieSlicePrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPieSlicePrivate(
    QPieSlicePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPieSlicePrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(charts_pie_chart)
