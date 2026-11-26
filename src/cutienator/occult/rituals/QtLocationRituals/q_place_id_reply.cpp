//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplaceidreply.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qplaceidreply.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPlaceIdReply that Python can take functions over in. Every QPlaceIdReply
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQPlaceIdReplyCall0)(const void *, int *);
typedef void (*CuteQPlaceIdReplyCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaceIdReplyCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaceIdReplyCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceIdReplyCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceIdReplyCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceIdReplyCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceIdReplyCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceIdReplyCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlaceIdReply : public QPlaceIdReply {
public:
  using QPlaceIdReply::QPlaceIdReply;
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

  //  QPlaceReply::Type QPlaceIdReply::type() const
  QPlaceReply::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlaceIdReplyCall0 call = reinterpret_cast<CuteQPlaceIdReplyCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPlaceReply::Type>(given);
    }
    return QPlaceIdReply::type();
  }

  //  void QPlaceReply::abort()
  void abort() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlaceIdReplyCall1 call = reinterpret_cast<CuteQPlaceIdReplyCall1>(taken[1]);
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
      CuteQPlaceIdReplyCall2 call = reinterpret_cast<CuteQPlaceIdReplyCall2>(taken[2]);
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
      CuteQPlaceIdReplyCall3 call = reinterpret_cast<CuteQPlaceIdReplyCall3>(taken[3]);
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
      CuteQPlaceIdReplyCall4 call = reinterpret_cast<CuteQPlaceIdReplyCall4>(taken[4]);
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
      CuteQPlaceIdReplyCall5 call = reinterpret_cast<CuteQPlaceIdReplyCall5>(taken[5]);
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
      CuteQPlaceIdReplyCall6 call = reinterpret_cast<CuteQPlaceIdReplyCall6>(taken[6]);
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
      CuteQPlaceIdReplyCall7 call = reinterpret_cast<CuteQPlaceIdReplyCall7>(taken[7]);
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
      CuteQPlaceIdReplyCall8 call = reinterpret_cast<CuteQPlaceIdReplyCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlaceIdReply::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QPlaceIdReply10metaObjectEv(
    const QPlaceIdReply *self) {
  return self->metaObject();
}

//  void *QPlaceIdReply::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QPlaceIdReply11qt_metacastEPKc(
    QPlaceIdReply *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlaceIdReply::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QPlaceIdReply11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlaceIdReply *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlaceIdReply::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QPlaceIdReply2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlaceIdReply::tr(s, c, n));
}

//  QPlaceIdReply::QPlaceIdReply(OperationType operationType, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QPlaceIdReply *ritual_ZN13QPlaceIdReplyC1ENS_13OperationTypeEP7QObject(
    QPlaceIdReply::OperationType operationType,
    QObject *parent) {
  return new CuteQPlaceIdReply(operationType, parent);
}

//  QPlaceIdReply::~QPlaceIdReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlaceIdReplyD1Ev(QPlaceIdReply *self) {
  delete self;
}

//  QPlaceReply::Type QPlaceIdReply::type() const
extern "C" Q_DECL_EXPORT
QPlaceReply::Type ritual_ZNK13QPlaceIdReply4typeEv(
    const QPlaceIdReply *self) {
  return self->type();
}

//  OperationType QPlaceIdReply::operationType() const
extern "C" Q_DECL_EXPORT
QPlaceIdReply::OperationType ritual_ZNK13QPlaceIdReply13operationTypeEv(
    const QPlaceIdReply *self) {
  return self->operationType();
}

//  QString QPlaceIdReply::id() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QPlaceIdReply2idEv(const QPlaceIdReply *self) {
  return new QString(self->id());
}

//  void QPlaceIdReply::setId(const QString &identifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlaceIdReply5setIdERK7QString(
    QPlaceIdReply *self,
    const QString *identifier) {
  self->setId(*identifier);
}

//  QPlaceIdReplyPrivate *QPlaceIdReply::d_func()
extern "C" Q_DECL_EXPORT
QPlaceIdReplyPrivate *ritual_ZN13QPlaceIdReply6d_funcEv(
    QPlaceIdReply *self) {
  return self->d_func();
}

//  const QPlaceIdReplyPrivate *QPlaceIdReply::d_func() const
extern "C" Q_DECL_EXPORT
const QPlaceIdReplyPrivate *ritual_ZNK13QPlaceIdReply6d_funcEv(
    const QPlaceIdReply *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQPlaceIdReply, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlaceIdReply(
    QPlaceIdReply *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlaceIdReply *>(self)->take(key, call);
}

//  QPlaceReply::Type QPlaceIdReply::type() const
extern "C" Q_DECL_EXPORT
QPlaceReply::Type ritual_own_ZNK13QPlaceIdReply4typeEv(
    const QPlaceIdReply *self) {
  return self->QPlaceIdReply::type();
}
