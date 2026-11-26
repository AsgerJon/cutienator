//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplacesearchreply.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qplacesearchreply.h>
#include <QtCore/qstring.h>
#include <QtLocation/qplacesearchresult.h>
#include <QtLocation/qplacesearchrequest.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QPlaceSearchReply that Python can take functions over in. Every QPlaceSearchReply
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQPlaceSearchReplyCall0)(const void *, int *);
typedef void (*CuteQPlaceSearchReplyCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaceSearchReplyCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaceSearchReplyCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceSearchReplyCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceSearchReplyCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceSearchReplyCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceSearchReplyCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceSearchReplyCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlaceSearchReply : public QPlaceSearchReply {
public:
  using QPlaceSearchReply::QPlaceSearchReply;
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
      CuteQPlaceSearchReplyCall0 call = reinterpret_cast<CuteQPlaceSearchReplyCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPlaceReply::Type>(given);
    }
    return QPlaceSearchReply::type();
  }

  //  void QPlaceReply::abort()
  void abort() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlaceSearchReplyCall1 call = reinterpret_cast<CuteQPlaceSearchReplyCall1>(taken[1]);
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
      CuteQPlaceSearchReplyCall2 call = reinterpret_cast<CuteQPlaceSearchReplyCall2>(taken[2]);
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
      CuteQPlaceSearchReplyCall3 call = reinterpret_cast<CuteQPlaceSearchReplyCall3>(taken[3]);
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
      CuteQPlaceSearchReplyCall4 call = reinterpret_cast<CuteQPlaceSearchReplyCall4>(taken[4]);
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
      CuteQPlaceSearchReplyCall5 call = reinterpret_cast<CuteQPlaceSearchReplyCall5>(taken[5]);
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
      CuteQPlaceSearchReplyCall6 call = reinterpret_cast<CuteQPlaceSearchReplyCall6>(taken[6]);
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
      CuteQPlaceSearchReplyCall7 call = reinterpret_cast<CuteQPlaceSearchReplyCall7>(taken[7]);
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
      CuteQPlaceSearchReplyCall8 call = reinterpret_cast<CuteQPlaceSearchReplyCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlaceSearchReply::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QPlaceSearchReply10metaObjectEv(
    const QPlaceSearchReply *self) {
  return self->metaObject();
}

//  void *QPlaceSearchReply::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QPlaceSearchReply11qt_metacastEPKc(
    QPlaceSearchReply *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlaceSearchReply::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QPlaceSearchReply11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlaceSearchReply *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlaceSearchReply::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QPlaceSearchReply2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlaceSearchReply::tr(s, c, n));
}

//  QPlaceSearchReply::QPlaceSearchReply(QObject *parent)
extern "C" Q_DECL_EXPORT
QPlaceSearchReply *ritual_ZN17QPlaceSearchReplyC1EP7QObject(
    QObject *parent) {
  return new CuteQPlaceSearchReply(parent);
}

//  QPlaceSearchReply::~QPlaceSearchReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlaceSearchReplyD1Ev(QPlaceSearchReply *self) {
  delete self;
}

//  QPlaceReply::Type QPlaceSearchReply::type() const
extern "C" Q_DECL_EXPORT
QPlaceReply::Type ritual_ZNK17QPlaceSearchReply4typeEv(
    const QPlaceSearchReply *self) {
  return self->type();
}

//  QList<QPlaceSearchResult> QPlaceSearchReply::results() const
extern "C" Q_DECL_EXPORT
QList<QPlaceSearchResult> *ritual_ZNK17QPlaceSearchReply7resultsEv(
    const QPlaceSearchReply *self) {
  return new QList<QPlaceSearchResult>(self->results());
}

//  QPlaceSearchRequest QPlaceSearchReply::request() const
extern "C" Q_DECL_EXPORT
QPlaceSearchRequest *ritual_ZNK17QPlaceSearchReply7requestEv(
    const QPlaceSearchReply *self) {
  return new QPlaceSearchRequest(self->request());
}

//  QPlaceSearchRequest QPlaceSearchReply::previousPageRequest() const
extern "C" Q_DECL_EXPORT
QPlaceSearchRequest *ritual_ZNK17QPlaceSearchReply19previousPageRequestEv(
    const QPlaceSearchReply *self) {
  return new QPlaceSearchRequest(self->previousPageRequest());
}

//  QPlaceSearchRequest QPlaceSearchReply::nextPageRequest() const
extern "C" Q_DECL_EXPORT
QPlaceSearchRequest *ritual_ZNK17QPlaceSearchReply15nextPageRequestEv(
    const QPlaceSearchReply *self) {
  return new QPlaceSearchRequest(self->nextPageRequest());
}

//  void QPlaceSearchReply::setResults(const QList<QPlaceSearchResult>
//      &results)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlaceSearchReply10setResultsERK5QListI18QPlaceSearchResultE(
    QPlaceSearchReply *self,
    const QList<QPlaceSearchResult> *results) {
  self->setResults(*results);
}

//  void QPlaceSearchReply::setRequest(const QPlaceSearchRequest &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlaceSearchReply10setRequestERK19QPlaceSearchRequest(
    QPlaceSearchReply *self,
    const QPlaceSearchRequest *request) {
  self->setRequest(*request);
}

//  void QPlaceSearchReply::setPreviousPageRequest(const QPlaceSearchRequest
//      &previous)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlaceSearchReply22setPreviousPageRequestERK19QPlaceSearchRequest(
    QPlaceSearchReply *self,
    const QPlaceSearchRequest *previous) {
  self->setPreviousPageRequest(*previous);
}

//  void QPlaceSearchReply::setNextPageRequest(const QPlaceSearchRequest
//      &next)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlaceSearchReply18setNextPageRequestERK19QPlaceSearchRequest(
    QPlaceSearchReply *self,
    const QPlaceSearchRequest *next) {
  self->setNextPageRequest(*next);
}

//  QPlaceSearchReplyPrivate *QPlaceSearchReply::d_func()
extern "C" Q_DECL_EXPORT
QPlaceSearchReplyPrivate *ritual_ZN17QPlaceSearchReply6d_funcEv(
    QPlaceSearchReply *self) {
  return self->d_func();
}

//  const QPlaceSearchReplyPrivate *QPlaceSearchReply::d_func() const
extern "C" Q_DECL_EXPORT
const QPlaceSearchReplyPrivate *ritual_ZNK17QPlaceSearchReply6d_funcEv(
    const QPlaceSearchReply *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQPlaceSearchReply, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlaceSearchReply(
    QPlaceSearchReply *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlaceSearchReply *>(self)->take(key, call);
}

//  QPlaceReply::Type QPlaceSearchReply::type() const
extern "C" Q_DECL_EXPORT
QPlaceReply::Type ritual_own_ZNK17QPlaceSearchReply4typeEv(
    const QPlaceSearchReply *self) {
  return self->QPlaceSearchReply::type();
}
