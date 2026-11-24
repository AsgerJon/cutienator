//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qctf_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(ctf)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qctf_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QCtfLib that Python can take functions over in. Every QCtfLib
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQCtfLibCall0)(const void *, const QCtfTracePointEvent *, int *);
typedef void (*CuteQCtfLibCall1)(const void *, const QCtfTracePointEvent *, const QByteArray *, int *);
typedef bool (*CuteQCtfLibCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCtfLibCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCtfLibCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCtfLibCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCtfLibCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCtfLibCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCtfLibCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCtfLibCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCtfLib : public QCtfLib {
public:
  using QCtfLib::QCtfLib;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QCtfLib17tracepointEnabledERK19QCtfTracePointEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QCtfLib12doTracepointERK19QCtfTracePointEventRK10QByteArray")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QCtfLib14sessionEnabledEv")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QCtfLib::tracepointEnabled(const QCtfTracePointEvent &point)
  bool tracepointEnabled(const QCtfTracePointEvent &point) override {
    if (taken[0]) {
      int handled = 0;
      CuteQCtfLibCall0 call = reinterpret_cast<CuteQCtfLibCall0>(taken[0]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QCtfLib::doTracepoint(const QCtfTracePointEvent &point, const
  //      QByteArray &arr)
  void doTracepoint(
      const QCtfTracePointEvent &point,
      const QByteArray &arr) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCtfLibCall1 call = reinterpret_cast<CuteQCtfLibCall1>(taken[1]);
      call(this, &point, &arr, &handled);
      if (handled) return;
    }
  }

  //  bool QCtfLib::sessionEnabled()
  bool sessionEnabled() override {
    if (taken[2]) {
      int handled = 0;
      CuteQCtfLibCall2 call = reinterpret_cast<CuteQCtfLibCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQCtfLibCall3 call = reinterpret_cast<CuteQCtfLibCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQCtfLibCall4 call = reinterpret_cast<CuteQCtfLibCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQCtfLibCall5 call = reinterpret_cast<CuteQCtfLibCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQCtfLibCall6 call = reinterpret_cast<CuteQCtfLibCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQCtfLibCall7 call = reinterpret_cast<CuteQCtfLibCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQCtfLibCall8 call = reinterpret_cast<CuteQCtfLibCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQCtfLibCall9 call = reinterpret_cast<CuteQCtfLibCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCtfLib::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QCtfLib10metaObjectEv(const QCtfLib *self) {
  return self->metaObject();
}

//  QString QCtfLib::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QCtfLib2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QCtfLib::tr(s, c, n));
}

//  QCtfLib::~QCtfLib()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCtfLibD1Ev(QCtfLib *self) {
  delete self;
}

//  bool QCtfLib::tracepointEnabled(const QCtfTracePointEvent &point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QCtfLib17tracepointEnabledERK19QCtfTracePointEvent(
    QCtfLib *self,
    const QCtfTracePointEvent *point) {
  return self->tracepointEnabled(*point);
}

//  void QCtfLib::doTracepoint(const QCtfTracePointEvent &point, const
//      QByteArray &arr)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCtfLib12doTracepointERK19QCtfTracePointEventRK10QByteArray(
    QCtfLib *self,
    const QCtfTracePointEvent *point,
    const QByteArray *arr) {
  self->doTracepoint(*point, *arr);
}

//  bool QCtfLib::sessionEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QCtfLib14sessionEnabledEv(QCtfLib *self) {
  return self->sessionEnabled();
}

//  void QCtfLib::shutdown(bool *shutdown)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QCtfLib8shutdownEPb(QCtfLib *self, bool *shutdown) {
  self->shutdown(shutdown);
}

//  a Python function taken by a CuteQCtfLib, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCtfLib(QCtfLib *self, const char *key, void *call) {
  return static_cast<CuteQCtfLib *>(self)->take(key, call);
}

#endif  // QT_CONFIG(ctf)
