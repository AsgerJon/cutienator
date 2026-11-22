//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextobject.h>
#include <QtCore/qstring.h>
#include <QtGui/qtextformat.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QTextObject that Python can take functions over in. Every QTextObject
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQTextObjectCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQTextObjectCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQTextObjectCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQTextObjectCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQTextObjectCall4)(const void *, QEvent *, int *);
typedef void (*CuteQTextObjectCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQTextObjectCall6)(const void *, const QMetaMethod *, int *);
class CuteQTextObject : public QTextObject {
public:
  using QTextObject::QTextObject;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTextObjectCall0 call = reinterpret_cast<CuteQTextObjectCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTextObjectCall1 call = reinterpret_cast<CuteQTextObjectCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTextObjectCall2 call = reinterpret_cast<CuteQTextObjectCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTextObjectCall3 call = reinterpret_cast<CuteQTextObjectCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTextObjectCall4 call = reinterpret_cast<CuteQTextObjectCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTextObjectCall5 call = reinterpret_cast<CuteQTextObjectCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTextObjectCall6 call = reinterpret_cast<CuteQTextObjectCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QTextObject::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QTextObject10metaObjectEv(
    const QTextObject *self) {
  return self->metaObject();
}

//  QString QTextObject::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QTextObject2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTextObject::tr(s, c, n));
}

//  QTextFormat QTextObject::format() const
extern "C" Q_DECL_EXPORT
QTextFormat *ritual_ZNK11QTextObject6formatEv(const QTextObject *self) {
  return new QTextFormat(self->format());
}

//  int QTextObject::formatIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextObject11formatIndexEv(const QTextObject *self) {
  return self->formatIndex();
}

//  QTextDocument *QTextObject::document() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK11QTextObject8documentEv(const QTextObject *self) {
  return self->document();
}

//  int QTextObject::objectIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextObject11objectIndexEv(const QTextObject *self) {
  return self->objectIndex();
}

//  a Python function taken by a CuteQTextObject, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTextObject(
    QTextObject *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTextObject *>(self)->take(key, call);
}
