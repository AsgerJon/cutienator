//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativecontactdetails_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativecontactdetails_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDeclarativeContactDetails that Python can take functions over in. Every QDeclarativeContactDetails
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQDeclarativeContactDetailsCall0)(const void *, const QString *, const QVariant *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeContactDetailsCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeContactDetailsCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeContactDetailsCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeContactDetailsCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeContactDetailsCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeContactDetailsCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeContactDetailsCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativeContactDetails : public QDeclarativeContactDetails {
public:
  using QDeclarativeContactDetails::QDeclarativeContactDetails;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QQmlPropertyMap11updateValueERK7QStringRK8QVariant")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QVariant QDeclarativeContactDetails::updateValue(const QString &key,
  //      const QVariant &input)
  QVariant updateValue(const QString &key, const QVariant &input) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativeContactDetailsCall0 call = reinterpret_cast<CuteQDeclarativeContactDetailsCall0>(taken[0]);
      const QVariant * given = call(this, &key, &input, &handled);
      if (handled && given) return *given;
    }
    return QDeclarativeContactDetails::updateValue(key, input);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativeContactDetailsCall1 call = reinterpret_cast<CuteQDeclarativeContactDetailsCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativeContactDetailsCall2 call = reinterpret_cast<CuteQDeclarativeContactDetailsCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativeContactDetailsCall3 call = reinterpret_cast<CuteQDeclarativeContactDetailsCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativeContactDetailsCall4 call = reinterpret_cast<CuteQDeclarativeContactDetailsCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativeContactDetailsCall5 call = reinterpret_cast<CuteQDeclarativeContactDetailsCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativeContactDetailsCall6 call = reinterpret_cast<CuteQDeclarativeContactDetailsCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativeContactDetailsCall7 call = reinterpret_cast<CuteQDeclarativeContactDetailsCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativeContactDetails::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QDeclarativeContactDetails10metaObjectEv(
    const QDeclarativeContactDetails *self) {
  return self->metaObject();
}

//  QString QDeclarativeContactDetails::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QDeclarativeContactDetails2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeContactDetails::tr(s, c, n));
}

//  void QDeclarativeContactDetails::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativeContactDetails24qt_qmlMarker_uncreatableEv(
    QDeclarativeContactDetails *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QDeclarativeContactDetails::QDeclarativeContactDetails(QObject *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeContactDetails *ritual_ZN26QDeclarativeContactDetailsC1EP7QObject(
    QObject *parent) {
  return new CuteQDeclarativeContactDetails(parent);
}

//  QVariant QDeclarativeContactDetails::updateValue(const QString &key,
//      const QVariant &input)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN26QDeclarativeContactDetails11updateValueERK7QStringRK8QVariant(
    QDeclarativeContactDetails *self,
    const QString *key,
    const QVariant *input) {
  return new QVariant(self->updateValue(*key, *input));
}

//  a Python function taken by a CuteQDeclarativeContactDetails, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeContactDetails(
    QDeclarativeContactDetails *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeContactDetails *>(self)->take(key, call);
}

//  QVariant QDeclarativeContactDetails::updateValue(const QString &key,
//      const QVariant &input)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN26QDeclarativeContactDetails11updateValueERK7QStringRK8QVariant(
    QDeclarativeContactDetails *self,
    const QString *key,
    const QVariant *input) {
  return new QVariant(
      self->QDeclarativeContactDetails::updateValue(
          *key,
          *input));
}
