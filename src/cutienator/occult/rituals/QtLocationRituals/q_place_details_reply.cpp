//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplacedetailsreply.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qplacedetailsreply.h>
#include <QtCore/qstring.h>
#include <QtLocation/qplace.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPlaceDetailsReply that Python can take functions over in. Every QPlaceDetailsReply
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQPlaceDetailsReplyCall0)(const void *, int *);
typedef void (*CuteQPlaceDetailsReplyCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaceDetailsReplyCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaceDetailsReplyCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceDetailsReplyCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceDetailsReplyCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceDetailsReplyCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceDetailsReplyCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceDetailsReplyCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlaceDetailsReply : public QPlaceDetailsReply {
public:
  using QPlaceDetailsReply::QPlaceDetailsReply;
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

  //  QPlaceReply::Type QPlaceDetailsReply::type() const
  QPlaceReply::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlaceDetailsReplyCall0 call = reinterpret_cast<CuteQPlaceDetailsReplyCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPlaceReply::Type>(given);
    }
    return QPlaceDetailsReply::type();
  }

  //  void QPlaceReply::abort()
  void abort() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlaceDetailsReplyCall1 call = reinterpret_cast<CuteQPlaceDetailsReplyCall1>(taken[1]);
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
      CuteQPlaceDetailsReplyCall2 call = reinterpret_cast<CuteQPlaceDetailsReplyCall2>(taken[2]);
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
      CuteQPlaceDetailsReplyCall3 call = reinterpret_cast<CuteQPlaceDetailsReplyCall3>(taken[3]);
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
      CuteQPlaceDetailsReplyCall4 call = reinterpret_cast<CuteQPlaceDetailsReplyCall4>(taken[4]);
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
      CuteQPlaceDetailsReplyCall5 call = reinterpret_cast<CuteQPlaceDetailsReplyCall5>(taken[5]);
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
      CuteQPlaceDetailsReplyCall6 call = reinterpret_cast<CuteQPlaceDetailsReplyCall6>(taken[6]);
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
      CuteQPlaceDetailsReplyCall7 call = reinterpret_cast<CuteQPlaceDetailsReplyCall7>(taken[7]);
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
      CuteQPlaceDetailsReplyCall8 call = reinterpret_cast<CuteQPlaceDetailsReplyCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlaceDetailsReply::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QPlaceDetailsReply10metaObjectEv(
    const QPlaceDetailsReply *self) {
  return self->metaObject();
}

//  void *QPlaceDetailsReply::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QPlaceDetailsReply11qt_metacastEPKc(
    QPlaceDetailsReply *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlaceDetailsReply::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QPlaceDetailsReply11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlaceDetailsReply *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlaceDetailsReply::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QPlaceDetailsReply2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlaceDetailsReply::tr(s, c, n));
}

//  QPlaceDetailsReply::QPlaceDetailsReply(QObject *parent)
extern "C" Q_DECL_EXPORT
QPlaceDetailsReply *ritual_ZN18QPlaceDetailsReplyC1EP7QObject(
    QObject *parent) {
  return new CuteQPlaceDetailsReply(parent);
}

//  QPlaceDetailsReply::~QPlaceDetailsReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlaceDetailsReplyD1Ev(QPlaceDetailsReply *self) {
  delete self;
}

//  QPlaceReply::Type QPlaceDetailsReply::type() const
extern "C" Q_DECL_EXPORT
QPlaceReply::Type ritual_ZNK18QPlaceDetailsReply4typeEv(
    const QPlaceDetailsReply *self) {
  return self->type();
}

//  QPlace QPlaceDetailsReply::place() const
extern "C" Q_DECL_EXPORT
QPlace *ritual_ZNK18QPlaceDetailsReply5placeEv(
    const QPlaceDetailsReply *self) {
  return new QPlace(self->place());
}

//  void QPlaceDetailsReply::setPlace(const QPlace &place)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlaceDetailsReply8setPlaceERK6QPlace(
    QPlaceDetailsReply *self,
    const QPlace *place) {
  self->setPlace(*place);
}

//  QPlaceDetailsReplyPrivate *QPlaceDetailsReply::d_func()
extern "C" Q_DECL_EXPORT
QPlaceDetailsReplyPrivate *ritual_ZN18QPlaceDetailsReply6d_funcEv(
    QPlaceDetailsReply *self) {
  return self->d_func();
}

//  const QPlaceDetailsReplyPrivate *QPlaceDetailsReply::d_func() const
extern "C" Q_DECL_EXPORT
const QPlaceDetailsReplyPrivate *ritual_ZNK18QPlaceDetailsReply6d_funcEv(
    const QPlaceDetailsReply *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQPlaceDetailsReply, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlaceDetailsReply(
    QPlaceDetailsReply *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlaceDetailsReply *>(self)->take(key, call);
}

//  QPlaceReply::Type QPlaceDetailsReply::type() const
extern "C" Q_DECL_EXPORT
QPlaceReply::Type ritual_own_ZNK18QPlaceDetailsReply4typeEv(
    const QPlaceDetailsReply *self) {
  return self->QPlaceDetailsReply::type();
}
