//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/6.12.0/QtHelp/private/qhelpsearchindexreader_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtHelp/QtHelp>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHelp/6.12.0/QtHelp/private/qhelpsearchindexreader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A fulltextsearch::QHelpSearchIndexReader that Python can take functions over in. Every fulltextsearch::QHelpSearchIndexReader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*Cutefulltextsearch_QHelpSearchIndexReaderCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cutefulltextsearch_QHelpSearchIndexReaderCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cutefulltextsearch_QHelpSearchIndexReaderCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cutefulltextsearch_QHelpSearchIndexReaderCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cutefulltextsearch_QHelpSearchIndexReaderCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cutefulltextsearch_QHelpSearchIndexReaderCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cutefulltextsearch_QHelpSearchIndexReaderCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cutefulltextsearch_QHelpSearchIndexReaderCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class Cutefulltextsearch_QHelpSearchIndexReader : public fulltextsearch::QHelpSearchIndexReader {
public:
  using fulltextsearch::QHelpSearchIndexReader::QHelpSearchIndexReader;
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

  //  void fulltextsearch::QHelpSearchIndexReader::run()
  void run() override {
    if (taken[0]) {
      int handled = 0;
      Cutefulltextsearch_QHelpSearchIndexReaderCall0 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexReaderCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    fulltextsearch::QHelpSearchIndexReader::run();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QThread::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      Cutefulltextsearch_QHelpSearchIndexReaderCall1 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexReaderCall1>(taken[1]);
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
      Cutefulltextsearch_QHelpSearchIndexReaderCall2 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexReaderCall2>(taken[2]);
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
      Cutefulltextsearch_QHelpSearchIndexReaderCall3 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexReaderCall3>(taken[3]);
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
      Cutefulltextsearch_QHelpSearchIndexReaderCall4 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexReaderCall4>(taken[4]);
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
      Cutefulltextsearch_QHelpSearchIndexReaderCall5 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexReaderCall5>(taken[5]);
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
      Cutefulltextsearch_QHelpSearchIndexReaderCall6 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexReaderCall6>(taken[6]);
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
      Cutefulltextsearch_QHelpSearchIndexReaderCall7 call = reinterpret_cast<Cutefulltextsearch_QHelpSearchIndexReaderCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *fulltextsearch::QHelpSearchIndexReader::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14fulltextsearch22QHelpSearchIndexReader10metaObjectEv(
    const fulltextsearch::QHelpSearchIndexReader *self) {
  return self->metaObject();
}

//  a Python function taken by a Cutefulltextsearch_QHelpSearchIndexReader,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_fulltextsearch_QHelpSearchIndexReader(
    fulltextsearch::QHelpSearchIndexReader *self,
    const char *key,
    void *call) {
  return static_cast<Cutefulltextsearch_QHelpSearchIndexReader *>(self)->take(key, call);
}
