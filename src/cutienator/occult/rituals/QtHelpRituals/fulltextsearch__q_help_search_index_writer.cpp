//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/6.12.0/QtHelp/private/qhelpsearchindexwriter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtHelp/QtHelp>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHelp/6.12.0/QtHelp/private/qhelpsearchindexwriter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A fulltextsearch::QHelpSearchIndexWriter that Python can take functions over in. Every fulltextsearch::QHelpSearchIndexWriter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*Cutefulltextsearch_QHelpSearchIndexWriterCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cutefulltextsearch_QHelpSearchIndexWriterCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cutefulltextsearch_QHelpSearchIndexWriterCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cutefulltextsearch_QHelpSearchIndexWriterCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cutefulltextsearch_QHelpSearchIndexWriterCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cutefulltextsearch_QHelpSearchIndexWriterCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cutefulltextsearch_QHelpSearchIndexWriterCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cutefulltextsearch_QHelpSearchIndexWriterCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class Cutefulltextsearch_QHelpSearchIndexWriter : public fulltextsearch::QHelpSearchIndexWriter {
public:
  using fulltextsearch::QHelpSearchIndexWriter::QHelpSearchIndexWriter;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QThread3runEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void fulltextsearch::QHelpSearchIndexWriter::run()
  void run() override {
    if (taken[0]) {
      int handled = 0;
      Cutefulltextsearch_QHelpSearchIndexWriterCall0 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexWriterCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    fulltextsearch::QHelpSearchIndexWriter::run();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QThread::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      Cutefulltextsearch_QHelpSearchIndexWriterCall1 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexWriterCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QThread::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      Cutefulltextsearch_QHelpSearchIndexWriterCall2 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexWriterCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      Cutefulltextsearch_QHelpSearchIndexWriterCall3 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexWriterCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      Cutefulltextsearch_QHelpSearchIndexWriterCall4 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexWriterCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      Cutefulltextsearch_QHelpSearchIndexWriterCall5 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexWriterCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      Cutefulltextsearch_QHelpSearchIndexWriterCall6 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexWriterCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      Cutefulltextsearch_QHelpSearchIndexWriterCall7 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexWriterCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *fulltextsearch::QHelpSearchIndexWriter::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14fulltextsearch22QHelpSearchIndexWriter10metaObjectEv(
    const fulltextsearch::QHelpSearchIndexWriter *self) {
  return self->metaObject();
}

//  void *fulltextsearch::QHelpSearchIndexWriter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14fulltextsearch22QHelpSearchIndexWriter11qt_metacastEPKc(
    fulltextsearch::QHelpSearchIndexWriter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  a Python function taken by a Cutefulltextsearch_QHelpSearchIndexWriter,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_fulltextsearch_QHelpSearchIndexWriter(
    fulltextsearch::QHelpSearchIndexWriter *self,
    const char *key,
    void *call) {
  return static_cast<Cutefulltextsearch_QHelpSearchIndexWriter *>(self)->take(key, call);
}
