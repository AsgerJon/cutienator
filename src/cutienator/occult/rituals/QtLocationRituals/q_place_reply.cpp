//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplacereply.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qplacereply.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPlaceReply that Python can take functions over in. Every QPlaceReply
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQPlaceReplyCall0)(const void *, int *);
typedef void (*CuteQPlaceReplyCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaceReplyCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaceReplyCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceReplyCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceReplyCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceReplyCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceReplyCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceReplyCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlaceReply : public QPlaceReply {
public:
  using QPlaceReply::QPlaceReply;
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
      CuteQPlaceReplyCall0 call = reinterpret_cast<CuteQPlaceReplyCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPlaceReply::Type>(given);
    }
    return QPlaceReply::type();
  }

  //  void QPlaceReply::abort()
  void abort() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlaceReplyCall1 call = reinterpret_cast<CuteQPlaceReplyCall1>(taken[1]);
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
      CuteQPlaceReplyCall2 call = reinterpret_cast<CuteQPlaceReplyCall2>(taken[2]);
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
      CuteQPlaceReplyCall3 call = reinterpret_cast<CuteQPlaceReplyCall3>(taken[3]);
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
      CuteQPlaceReplyCall4 call = reinterpret_cast<CuteQPlaceReplyCall4>(taken[4]);
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
      CuteQPlaceReplyCall5 call = reinterpret_cast<CuteQPlaceReplyCall5>(taken[5]);
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
      CuteQPlaceReplyCall6 call = reinterpret_cast<CuteQPlaceReplyCall6>(taken[6]);
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
      CuteQPlaceReplyCall7 call = reinterpret_cast<CuteQPlaceReplyCall7>(taken[7]);
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
      CuteQPlaceReplyCall8 call = reinterpret_cast<CuteQPlaceReplyCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlaceReply::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QPlaceReply10metaObjectEv(
    const QPlaceReply *self) {
  return self->metaObject();
}

//  QString QPlaceReply::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QPlaceReply2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlaceReply::tr(s, c, n));
}

//  QPlaceReply::QPlaceReply(QObject *parent)
extern "C" Q_DECL_EXPORT
QPlaceReply *ritual_ZN11QPlaceReplyC1EP7QObject(QObject *parent) {
  return new CuteQPlaceReply(parent);
}

//  QPlaceReply::~QPlaceReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPlaceReplyD1Ev(QPlaceReply *self) {
  delete self;
}

//  bool QPlaceReply::isFinished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QPlaceReply10isFinishedEv(const QPlaceReply *self) {
  return self->isFinished();
}

//  Type QPlaceReply::type() const
extern "C" Q_DECL_EXPORT
QPlaceReply::Type ritual_ZNK11QPlaceReply4typeEv(const QPlaceReply *self) {
  return self->type();
}

//  QString QPlaceReply::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QPlaceReply11errorStringEv(const QPlaceReply *self) {
  return new QString(self->errorString());
}

//  QPlaceReply::Error QPlaceReply::error() const
extern "C" Q_DECL_EXPORT
QPlaceReply::Error ritual_ZNK11QPlaceReply5errorEv(const QPlaceReply *self) {
  return self->error();
}

//  void QPlaceReply::abort()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPlaceReply5abortEv(QPlaceReply *self) {
  self->abort();
}

//  QPlaceReply::QPlaceReply(QPlaceReplyPrivate *a0, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlaceReply *ritual_ZN11QPlaceReplyC1EP18QPlaceReplyPrivateP7QObject(
    QPlaceReplyPrivate *a0,
    QObject *parent) {
  return new CuteQPlaceReply(a0, parent);
}

//  void QPlaceReply::setFinished(bool finished)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPlaceReply11setFinishedEb(
    QPlaceReply *self,
    bool finished) {
  self->setFinished(finished);
}

//  void QPlaceReply::setError(QPlaceReply::Error error, const QString
//      &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPlaceReply8setErrorENS_5ErrorERK7QString(
    QPlaceReply *self,
    QPlaceReply::Error error,
    const QString *errorString) {
  self->setError(error, *errorString);
}

//  a Python function taken by a CuteQPlaceReply, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlaceReply(
    QPlaceReply *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlaceReply *>(self)->take(key, call);
}

//  Type QPlaceReply::type() const
extern "C" Q_DECL_EXPORT
QPlaceReply::Type ritual_own_ZNK11QPlaceReply4typeEv(
    const QPlaceReply *self) {
  return self->QPlaceReply::type();
}

//  void QPlaceReply::abort()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QPlaceReply5abortEv(QPlaceReply *self) {
  self->QPlaceReply::abort();
}
