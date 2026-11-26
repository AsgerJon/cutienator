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

//  A QPlaceSearchReplyUnsupported that Python can take functions over in. Every QPlaceSearchReplyUnsupported
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQPlaceSearchReplyUnsupportedCall0)(const void *, int *);
typedef void (*CuteQPlaceSearchReplyUnsupportedCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaceSearchReplyUnsupportedCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaceSearchReplyUnsupportedCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceSearchReplyUnsupportedCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceSearchReplyUnsupportedCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceSearchReplyUnsupportedCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceSearchReplyUnsupportedCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceSearchReplyUnsupportedCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlaceSearchReplyUnsupported : public QPlaceSearchReplyUnsupported {
public:
  using QPlaceSearchReplyUnsupported::QPlaceSearchReplyUnsupported;
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

  //  QPlaceReply::Type QPlaceSearchReply::type() const
  QPlaceReply::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlaceSearchReplyUnsupportedCall0 call = reinterpret_cast<CuteQPlaceSearchReplyUnsupportedCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPlaceReply::Type>(given);
    }
    return QPlaceSearchReply::type();
  }

  //  void QPlaceReply::abort()
  void abort() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlaceSearchReplyUnsupportedCall1 call = reinterpret_cast<CuteQPlaceSearchReplyUnsupportedCall1>(taken[1]);
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
      CuteQPlaceSearchReplyUnsupportedCall2 call = reinterpret_cast<CuteQPlaceSearchReplyUnsupportedCall2>(taken[2]);
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
      CuteQPlaceSearchReplyUnsupportedCall3 call = reinterpret_cast<CuteQPlaceSearchReplyUnsupportedCall3>(taken[3]);
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
      CuteQPlaceSearchReplyUnsupportedCall4 call = reinterpret_cast<CuteQPlaceSearchReplyUnsupportedCall4>(taken[4]);
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
      CuteQPlaceSearchReplyUnsupportedCall5 call = reinterpret_cast<CuteQPlaceSearchReplyUnsupportedCall5>(taken[5]);
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
      CuteQPlaceSearchReplyUnsupportedCall6 call = reinterpret_cast<CuteQPlaceSearchReplyUnsupportedCall6>(taken[6]);
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
      CuteQPlaceSearchReplyUnsupportedCall7 call = reinterpret_cast<CuteQPlaceSearchReplyUnsupportedCall7>(taken[7]);
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
      CuteQPlaceSearchReplyUnsupportedCall8 call = reinterpret_cast<CuteQPlaceSearchReplyUnsupportedCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlaceSearchReplyUnsupported::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QPlaceSearchReplyUnsupported10metaObjectEv(
    const QPlaceSearchReplyUnsupported *self) {
  return self->metaObject();
}

//  void *QPlaceSearchReplyUnsupported::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QPlaceSearchReplyUnsupported11qt_metacastEPKc(
    QPlaceSearchReplyUnsupported *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlaceSearchReplyUnsupported::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QPlaceSearchReplyUnsupported11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlaceSearchReplyUnsupported *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlaceSearchReplyUnsupported::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QPlaceSearchReplyUnsupported2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlaceSearchReplyUnsupported::tr(s, c, n));
}

//  QPlaceSearchReplyUnsupported::QPlaceSearchReplyUnsupported(QPlaceReply::E
//      rror errorCode, const QString &message, QPlaceManagerEngine *parent)
extern "C" Q_DECL_EXPORT
QPlaceSearchReplyUnsupported *ritual_ZN28QPlaceSearchReplyUnsupportedC1EN11QPlaceReply5ErrorERK7QStringP19QPlaceManagerEngine(
    QPlaceReply::Error errorCode,
    const QString *message,
    QPlaceManagerEngine *parent) {
  return new CuteQPlaceSearchReplyUnsupported(errorCode, *message, parent);
}

//  a Python function taken by a CuteQPlaceSearchReplyUnsupported, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlaceSearchReplyUnsupported(
    QPlaceSearchReplyUnsupported *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlaceSearchReplyUnsupported *>(self)->take(key, call);
}
