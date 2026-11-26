//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplacesearchsuggestionreply.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtLocation/qplacesearchsuggestionreply.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QPlaceSearchSuggestionReply that Python can take functions over in. Every QPlaceSearchSuggestionReply
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQPlaceSearchSuggestionReplyCall0)(const void *, int *);
typedef void (*CuteQPlaceSearchSuggestionReplyCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaceSearchSuggestionReplyCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaceSearchSuggestionReplyCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceSearchSuggestionReplyCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceSearchSuggestionReplyCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceSearchSuggestionReplyCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceSearchSuggestionReplyCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceSearchSuggestionReplyCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlaceSearchSuggestionReply : public QPlaceSearchSuggestionReply {
public:
  using QPlaceSearchSuggestionReply::QPlaceSearchSuggestionReply;
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

  //  Type QPlaceSearchSuggestionReply::type() const
  QPlaceReply::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlaceSearchSuggestionReplyCall0 call = reinterpret_cast<CuteQPlaceSearchSuggestionReplyCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPlaceReply::Type>(given);
    }
    return QPlaceSearchSuggestionReply::type();
  }

  //  void QPlaceReply::abort()
  void abort() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlaceSearchSuggestionReplyCall1 call = reinterpret_cast<CuteQPlaceSearchSuggestionReplyCall1>(taken[1]);
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
      CuteQPlaceSearchSuggestionReplyCall2 call = reinterpret_cast<CuteQPlaceSearchSuggestionReplyCall2>(taken[2]);
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
      CuteQPlaceSearchSuggestionReplyCall3 call = reinterpret_cast<CuteQPlaceSearchSuggestionReplyCall3>(taken[3]);
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
      CuteQPlaceSearchSuggestionReplyCall4 call = reinterpret_cast<CuteQPlaceSearchSuggestionReplyCall4>(taken[4]);
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
      CuteQPlaceSearchSuggestionReplyCall5 call = reinterpret_cast<CuteQPlaceSearchSuggestionReplyCall5>(taken[5]);
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
      CuteQPlaceSearchSuggestionReplyCall6 call = reinterpret_cast<CuteQPlaceSearchSuggestionReplyCall6>(taken[6]);
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
      CuteQPlaceSearchSuggestionReplyCall7 call = reinterpret_cast<CuteQPlaceSearchSuggestionReplyCall7>(taken[7]);
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
      CuteQPlaceSearchSuggestionReplyCall8 call = reinterpret_cast<CuteQPlaceSearchSuggestionReplyCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlaceSearchSuggestionReply::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QPlaceSearchSuggestionReply10metaObjectEv(
    const QPlaceSearchSuggestionReply *self) {
  return self->metaObject();
}

//  void *QPlaceSearchSuggestionReply::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QPlaceSearchSuggestionReply11qt_metacastEPKc(
    QPlaceSearchSuggestionReply *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlaceSearchSuggestionReply::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QPlaceSearchSuggestionReply11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlaceSearchSuggestionReply *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlaceSearchSuggestionReply::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QPlaceSearchSuggestionReply2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlaceSearchSuggestionReply::tr(s, c, n));
}

//  QPlaceSearchSuggestionReply::QPlaceSearchSuggestionReply(QObject *parent)
extern "C" Q_DECL_EXPORT
QPlaceSearchSuggestionReply *ritual_ZN27QPlaceSearchSuggestionReplyC1EP7QObject(
    QObject *parent) {
  return new CuteQPlaceSearchSuggestionReply(parent);
}

//  QPlaceSearchSuggestionReply::~QPlaceSearchSuggestionReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QPlaceSearchSuggestionReplyD1Ev(
    QPlaceSearchSuggestionReply *self) {
  delete self;
}

//  QStringList QPlaceSearchSuggestionReply::suggestions() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK27QPlaceSearchSuggestionReply11suggestionsEv(
    const QPlaceSearchSuggestionReply *self) {
  return new QList<QString>(self->suggestions());
}

//  Type QPlaceSearchSuggestionReply::type() const
extern "C" Q_DECL_EXPORT
QPlaceReply::Type ritual_ZNK27QPlaceSearchSuggestionReply4typeEv(
    const QPlaceSearchSuggestionReply *self) {
  return self->type();
}

//  void QPlaceSearchSuggestionReply::setSuggestions(const QStringList
//      &suggestions)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QPlaceSearchSuggestionReply14setSuggestionsERK5QListI7QStringE(
    QPlaceSearchSuggestionReply *self,
    const QList<QString> *suggestions) {
  self->setSuggestions(*suggestions);
}

//  QPlaceSearchSuggestionReplyPrivate *QPlaceSearchSuggestionReply::d_func()
extern "C" Q_DECL_EXPORT
QPlaceSearchSuggestionReplyPrivate *ritual_ZN27QPlaceSearchSuggestionReply6d_funcEv(
    QPlaceSearchSuggestionReply *self) {
  return self->d_func();
}

//  const QPlaceSearchSuggestionReplyPrivate
//      *QPlaceSearchSuggestionReply::d_func() const
extern "C" Q_DECL_EXPORT
const QPlaceSearchSuggestionReplyPrivate *ritual_ZNK27QPlaceSearchSuggestionReply6d_funcEv(
    const QPlaceSearchSuggestionReply *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQPlaceSearchSuggestionReply, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlaceSearchSuggestionReply(
    QPlaceSearchSuggestionReply *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlaceSearchSuggestionReply *>(self)->take(key, call);
}

//  Type QPlaceSearchSuggestionReply::type() const
extern "C" Q_DECL_EXPORT
QPlaceReply::Type ritual_own_ZNK27QPlaceSearchSuggestionReply4typeEv(
    const QPlaceSearchSuggestionReply *self) {
  return self->QPlaceSearchSuggestionReply::type();
}
