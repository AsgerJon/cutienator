//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/unsupportedreplies_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/unsupportedreplies_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPlaceReplyUnsupported that Python can take functions over in. Every QPlaceReplyUnsupported
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQPlaceReplyUnsupportedCall0)(const void *, int *);
typedef void (*CuteQPlaceReplyUnsupportedCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaceReplyUnsupportedCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaceReplyUnsupportedCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceReplyUnsupportedCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceReplyUnsupportedCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceReplyUnsupportedCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceReplyUnsupportedCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceReplyUnsupportedCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlaceReplyUnsupported : public QPlaceReplyUnsupported {
public:
  using QPlaceReplyUnsupported::QPlaceReplyUnsupported;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QPlaceReply4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QPlaceReply5abortEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  Type QPlaceReply::type() const
  QPlaceReply::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlaceReplyUnsupportedCall0 call = reinterpret_cast<CuteQPlaceReplyUnsupportedCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPlaceReply::Type>(given);
    }
    return QPlaceReply::type();
  }

  //  void QPlaceReply::abort()
  void abort() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlaceReplyUnsupportedCall1 call = reinterpret_cast<CuteQPlaceReplyUnsupportedCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QPlaceReply::abort();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlaceReplyUnsupportedCall2 call = reinterpret_cast<CuteQPlaceReplyUnsupportedCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlaceReplyUnsupportedCall3 call = reinterpret_cast<CuteQPlaceReplyUnsupportedCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlaceReplyUnsupportedCall4 call = reinterpret_cast<CuteQPlaceReplyUnsupportedCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlaceReplyUnsupportedCall5 call = reinterpret_cast<CuteQPlaceReplyUnsupportedCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlaceReplyUnsupportedCall6 call = reinterpret_cast<CuteQPlaceReplyUnsupportedCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlaceReplyUnsupportedCall7 call = reinterpret_cast<CuteQPlaceReplyUnsupportedCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlaceReplyUnsupportedCall8 call = reinterpret_cast<CuteQPlaceReplyUnsupportedCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlaceReplyUnsupported::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QPlaceReplyUnsupported10metaObjectEv(
    const QPlaceReplyUnsupported *self) {
  return self->metaObject();
}

//  QString QPlaceReplyUnsupported::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QPlaceReplyUnsupported2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlaceReplyUnsupported::tr(s, c, n));
}

//  QPlaceReplyUnsupported::QPlaceReplyUnsupported(const QString &message,
//      QPlaceManagerEngine *parent)
extern "C" Q_DECL_EXPORT
QPlaceReplyUnsupported *ritual_ZN22QPlaceReplyUnsupportedC1ERK7QStringP19QPlaceManagerEngine(
    const QString *message,
    QPlaceManagerEngine *parent) {
  return new CuteQPlaceReplyUnsupported(*message, parent);
}

//  a Python function taken by a CuteQPlaceReplyUnsupported, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlaceReplyUnsupported(
    QPlaceReplyUnsupported *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlaceReplyUnsupported *>(self)->take(key, call);
}
