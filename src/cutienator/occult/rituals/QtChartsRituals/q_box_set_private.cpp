//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qboxset_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qboxset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QBoxSetPrivate that Python can take functions over in. Every QBoxSetPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBoxSetPrivateCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBoxSetPrivateCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxSetPrivateCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxSetPrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxSetPrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxSetPrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxSetPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBoxSetPrivate : public QBoxSetPrivate {
public:
  using QBoxSetPrivate::QBoxSetPrivate;
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
      CuteQBoxSetPrivateCall0 call = reinterpret_cast<CuteQBoxSetPrivateCall0>(taken[0]);
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
      CuteQBoxSetPrivateCall1 call = reinterpret_cast<CuteQBoxSetPrivateCall1>(taken[1]);
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
      CuteQBoxSetPrivateCall2 call = reinterpret_cast<CuteQBoxSetPrivateCall2>(taken[2]);
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
      CuteQBoxSetPrivateCall3 call = reinterpret_cast<CuteQBoxSetPrivateCall3>(taken[3]);
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
      CuteQBoxSetPrivateCall4 call = reinterpret_cast<CuteQBoxSetPrivateCall4>(taken[4]);
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
      CuteQBoxSetPrivateCall5 call = reinterpret_cast<CuteQBoxSetPrivateCall5>(taken[5]);
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
      CuteQBoxSetPrivateCall6 call = reinterpret_cast<CuteQBoxSetPrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBoxSetPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QBoxSetPrivate10metaObjectEv(
    const QBoxSetPrivate *self) {
  return self->metaObject();
}

//  QString QBoxSetPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QBoxSetPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBoxSetPrivate::tr(s, c, n));
}

//  QBoxSetPrivate::QBoxSetPrivate(const QString label, QBoxSet *parent)
extern "C" Q_DECL_EXPORT
QBoxSetPrivate *ritual_ZN14QBoxSetPrivateC1E7QStringP7QBoxSet(
    const QString *label,
    QBoxSet *parent) {
  return new CuteQBoxSetPrivate(*label, parent);
}

//  QBoxSetPrivate::~QBoxSetPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBoxSetPrivateD1Ev(QBoxSetPrivate *self) {
  delete self;
}

//  bool QBoxSetPrivate::append(qreal value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QBoxSetPrivate6appendEd(QBoxSetPrivate *self, qreal value) {
  return self->append(value);
}

//  void QBoxSetPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBoxSetPrivate5clearEv(QBoxSetPrivate *self) {
  self->clear();
}

//  void QBoxSetPrivate::setValue(const int index, const qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBoxSetPrivate8setValueEid(
    QBoxSetPrivate *self,
    int index,
    qreal value) {
  self->setValue(index, value);
}

//  qreal QBoxSetPrivate::value(const int index)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN14QBoxSetPrivate5valueEi(QBoxSetPrivate *self, int index) {
  return self->value(index);
}

//  a Python function taken by a CuteQBoxSetPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBoxSetPrivate(
    QBoxSetPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBoxSetPrivate *>(self)->take(key, call);
}
