//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplacematchreply.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qplacematchreply.h>
#include <QtCore/qstring.h>
#include <QtLocation/qplace.h>
#include <QtLocation/qplacematchrequest.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QPlaceMatchReply that Python can take functions over in. Every QPlaceMatchReply
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQPlaceMatchReplyCall0)(const void *, int *);
typedef void (*CuteQPlaceMatchReplyCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaceMatchReplyCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaceMatchReplyCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceMatchReplyCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceMatchReplyCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceMatchReplyCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceMatchReplyCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceMatchReplyCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlaceMatchReply : public QPlaceMatchReply {
public:
  using QPlaceMatchReply::QPlaceMatchReply;
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

  //  QPlaceReply::Type QPlaceMatchReply::type() const
  QPlaceReply::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlaceMatchReplyCall0 call = reinterpret_cast<CuteQPlaceMatchReplyCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPlaceReply::Type>(given);
    }
    return QPlaceMatchReply::type();
  }

  //  void QPlaceReply::abort()
  void abort() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlaceMatchReplyCall1 call = reinterpret_cast<CuteQPlaceMatchReplyCall1>(taken[1]);
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
      CuteQPlaceMatchReplyCall2 call = reinterpret_cast<CuteQPlaceMatchReplyCall2>(taken[2]);
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
      CuteQPlaceMatchReplyCall3 call = reinterpret_cast<CuteQPlaceMatchReplyCall3>(taken[3]);
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
      CuteQPlaceMatchReplyCall4 call = reinterpret_cast<CuteQPlaceMatchReplyCall4>(taken[4]);
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
      CuteQPlaceMatchReplyCall5 call = reinterpret_cast<CuteQPlaceMatchReplyCall5>(taken[5]);
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
      CuteQPlaceMatchReplyCall6 call = reinterpret_cast<CuteQPlaceMatchReplyCall6>(taken[6]);
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
      CuteQPlaceMatchReplyCall7 call = reinterpret_cast<CuteQPlaceMatchReplyCall7>(taken[7]);
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
      CuteQPlaceMatchReplyCall8 call = reinterpret_cast<CuteQPlaceMatchReplyCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlaceMatchReply::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QPlaceMatchReply10metaObjectEv(
    const QPlaceMatchReply *self) {
  return self->metaObject();
}

//  void *QPlaceMatchReply::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QPlaceMatchReply11qt_metacastEPKc(
    QPlaceMatchReply *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlaceMatchReply::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QPlaceMatchReply11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlaceMatchReply *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlaceMatchReply::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QPlaceMatchReply2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlaceMatchReply::tr(s, c, n));
}

//  QPlaceMatchReply::QPlaceMatchReply(QObject *parent)
extern "C" Q_DECL_EXPORT
QPlaceMatchReply *ritual_ZN16QPlaceMatchReplyC1EP7QObject(QObject *parent) {
  return new CuteQPlaceMatchReply(parent);
}

//  QPlaceMatchReply::~QPlaceMatchReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPlaceMatchReplyD1Ev(QPlaceMatchReply *self) {
  delete self;
}

//  QPlaceReply::Type QPlaceMatchReply::type() const
extern "C" Q_DECL_EXPORT
QPlaceReply::Type ritual_ZNK16QPlaceMatchReply4typeEv(
    const QPlaceMatchReply *self) {
  return self->type();
}

//  QList<QPlace> QPlaceMatchReply::places() const
extern "C" Q_DECL_EXPORT
QList<QPlace> *ritual_ZNK16QPlaceMatchReply6placesEv(
    const QPlaceMatchReply *self) {
  return new QList<QPlace>(self->places());
}

//  QPlaceMatchRequest QPlaceMatchReply::request() const
extern "C" Q_DECL_EXPORT
QPlaceMatchRequest *ritual_ZNK16QPlaceMatchReply7requestEv(
    const QPlaceMatchReply *self) {
  return new QPlaceMatchRequest(self->request());
}

//  void QPlaceMatchReply::setPlaces(const QList<QPlace> &results)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPlaceMatchReply9setPlacesERK5QListI6QPlaceE(
    QPlaceMatchReply *self,
    const QList<QPlace> *results) {
  self->setPlaces(*results);
}

//  void QPlaceMatchReply::setRequest(const QPlaceMatchRequest &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPlaceMatchReply10setRequestERK18QPlaceMatchRequest(
    QPlaceMatchReply *self,
    const QPlaceMatchRequest *request) {
  self->setRequest(*request);
}

//  QPlaceMatchReplyPrivate *QPlaceMatchReply::d_func()
extern "C" Q_DECL_EXPORT
QPlaceMatchReplyPrivate *ritual_ZN16QPlaceMatchReply6d_funcEv(
    QPlaceMatchReply *self) {
  return self->d_func();
}

//  const QPlaceMatchReplyPrivate *QPlaceMatchReply::d_func() const
extern "C" Q_DECL_EXPORT
const QPlaceMatchReplyPrivate *ritual_ZNK16QPlaceMatchReply6d_funcEv(
    const QPlaceMatchReply *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQPlaceMatchReply, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlaceMatchReply(
    QPlaceMatchReply *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlaceMatchReply *>(self)->take(key, call);
}

//  QPlaceReply::Type QPlaceMatchReply::type() const
extern "C" Q_DECL_EXPORT
QPlaceReply::Type ritual_own_ZNK16QPlaceMatchReply4typeEv(
    const QPlaceMatchReply *self) {
  return self->QPlaceMatchReply::type();
}
