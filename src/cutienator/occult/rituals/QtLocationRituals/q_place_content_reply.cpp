//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplacecontentreply.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qplacecontentreply.h>
#include <QtCore/qstring.h>
#include <QtLocation/qplacecontent.h>
#include <QtLocation/qplacecontentrequest.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QPlaceContentReply that Python can take functions over in. Every QPlaceContentReply
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQPlaceContentReplyCall0)(const void *, int *);
typedef void (*CuteQPlaceContentReplyCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaceContentReplyCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaceContentReplyCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceContentReplyCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceContentReplyCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceContentReplyCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceContentReplyCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceContentReplyCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlaceContentReply : public QPlaceContentReply {
public:
  using QPlaceContentReply::QPlaceContentReply;
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

  //  QPlaceReply::Type QPlaceContentReply::type() const
  QPlaceReply::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlaceContentReplyCall0 call = reinterpret_cast<CuteQPlaceContentReplyCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPlaceReply::Type>(given);
    }
    return QPlaceContentReply::type();
  }

  //  void QPlaceReply::abort()
  void abort() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlaceContentReplyCall1 call = reinterpret_cast<CuteQPlaceContentReplyCall1>(taken[1]);
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
      CuteQPlaceContentReplyCall2 call = reinterpret_cast<CuteQPlaceContentReplyCall2>(taken[2]);
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
      CuteQPlaceContentReplyCall3 call = reinterpret_cast<CuteQPlaceContentReplyCall3>(taken[3]);
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
      CuteQPlaceContentReplyCall4 call = reinterpret_cast<CuteQPlaceContentReplyCall4>(taken[4]);
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
      CuteQPlaceContentReplyCall5 call = reinterpret_cast<CuteQPlaceContentReplyCall5>(taken[5]);
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
      CuteQPlaceContentReplyCall6 call = reinterpret_cast<CuteQPlaceContentReplyCall6>(taken[6]);
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
      CuteQPlaceContentReplyCall7 call = reinterpret_cast<CuteQPlaceContentReplyCall7>(taken[7]);
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
      CuteQPlaceContentReplyCall8 call = reinterpret_cast<CuteQPlaceContentReplyCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlaceContentReply::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QPlaceContentReply10metaObjectEv(
    const QPlaceContentReply *self) {
  return self->metaObject();
}

//  void *QPlaceContentReply::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QPlaceContentReply11qt_metacastEPKc(
    QPlaceContentReply *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlaceContentReply::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QPlaceContentReply11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlaceContentReply *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlaceContentReply::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QPlaceContentReply2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlaceContentReply::tr(s, c, n));
}

//  QPlaceContentReply::QPlaceContentReply(QObject *parent)
extern "C" Q_DECL_EXPORT
QPlaceContentReply *ritual_ZN18QPlaceContentReplyC1EP7QObject(
    QObject *parent) {
  return new CuteQPlaceContentReply(parent);
}

//  QPlaceContentReply::~QPlaceContentReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlaceContentReplyD1Ev(QPlaceContentReply *self) {
  delete self;
}

//  QPlaceReply::Type QPlaceContentReply::type() const
extern "C" Q_DECL_EXPORT
QPlaceReply::Type ritual_ZNK18QPlaceContentReply4typeEv(
    const QPlaceContentReply *self) {
  return self->type();
}

//  QPlaceContent::Collection QPlaceContentReply::content() const
extern "C" Q_DECL_EXPORT
QMap<int, QPlaceContent> *ritual_ZNK18QPlaceContentReply7contentEv(
    const QPlaceContentReply *self) {
  return new QMap<int, QPlaceContent>(self->content());
}

//  int QPlaceContentReply::totalCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QPlaceContentReply10totalCountEv(
    const QPlaceContentReply *self) {
  return self->totalCount();
}

//  QPlaceContentRequest QPlaceContentReply::request() const
extern "C" Q_DECL_EXPORT
QPlaceContentRequest *ritual_ZNK18QPlaceContentReply7requestEv(
    const QPlaceContentReply *self) {
  return new QPlaceContentRequest(self->request());
}

//  QPlaceContentRequest QPlaceContentReply::previousPageRequest() const
extern "C" Q_DECL_EXPORT
QPlaceContentRequest *ritual_ZNK18QPlaceContentReply19previousPageRequestEv(
    const QPlaceContentReply *self) {
  return new QPlaceContentRequest(self->previousPageRequest());
}

//  QPlaceContentRequest QPlaceContentReply::nextPageRequest() const
extern "C" Q_DECL_EXPORT
QPlaceContentRequest *ritual_ZNK18QPlaceContentReply15nextPageRequestEv(
    const QPlaceContentReply *self) {
  return new QPlaceContentRequest(self->nextPageRequest());
}

//  void QPlaceContentReply::setContent(const QPlaceContent::Collection
//      &content)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlaceContentReply10setContentERK4QMapIi13QPlaceContentE(
    QPlaceContentReply *self,
    const QMap<int, QPlaceContent> *content) {
  self->setContent(*content);
}

//  void QPlaceContentReply::setTotalCount(int total)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlaceContentReply13setTotalCountEi(
    QPlaceContentReply *self,
    int total) {
  self->setTotalCount(total);
}

//  void QPlaceContentReply::setRequest(const QPlaceContentRequest &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlaceContentReply10setRequestERK20QPlaceContentRequest(
    QPlaceContentReply *self,
    const QPlaceContentRequest *request) {
  self->setRequest(*request);
}

//  void QPlaceContentReply::setPreviousPageRequest(const
//      QPlaceContentRequest &previous)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlaceContentReply22setPreviousPageRequestERK20QPlaceContentRequest(
    QPlaceContentReply *self,
    const QPlaceContentRequest *previous) {
  self->setPreviousPageRequest(*previous);
}

//  void QPlaceContentReply::setNextPageRequest(const QPlaceContentRequest
//      &next)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlaceContentReply18setNextPageRequestERK20QPlaceContentRequest(
    QPlaceContentReply *self,
    const QPlaceContentRequest *next) {
  self->setNextPageRequest(*next);
}

//  QPlaceContentReplyPrivate *QPlaceContentReply::d_func()
extern "C" Q_DECL_EXPORT
QPlaceContentReplyPrivate *ritual_ZN18QPlaceContentReply6d_funcEv(
    QPlaceContentReply *self) {
  return self->d_func();
}

//  const QPlaceContentReplyPrivate *QPlaceContentReply::d_func() const
extern "C" Q_DECL_EXPORT
const QPlaceContentReplyPrivate *ritual_ZNK18QPlaceContentReply6d_funcEv(
    const QPlaceContentReply *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQPlaceContentReply, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlaceContentReply(
    QPlaceContentReply *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlaceContentReply *>(self)->take(key, call);
}

//  QPlaceReply::Type QPlaceContentReply::type() const
extern "C" Q_DECL_EXPORT
QPlaceReply::Type ritual_own_ZNK18QPlaceContentReply4typeEv(
    const QPlaceContentReply *self) {
  return self->QPlaceContentReply::type();
}
