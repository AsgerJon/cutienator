//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebSockets/qmaskgenerator.h, Qt 6.12.0. Changes made here are lost.
#include <QtWebSockets/qmaskgenerator.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QMaskGenerator that Python can take functions over in. Every QMaskGenerator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQMaskGeneratorCall0)(const void *, int *);
typedef quint32 (*CuteQMaskGeneratorCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMaskGeneratorCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMaskGeneratorCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMaskGeneratorCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMaskGeneratorCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMaskGeneratorCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMaskGeneratorCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMaskGeneratorCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQMaskGenerator : public QMaskGenerator {
public:
  using QMaskGenerator::QMaskGenerator;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QMaskGenerator4seedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QMaskGenerator8nextMaskEv")) {
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

  //  bool QMaskGenerator::seed()
  bool seed() override {
    if (taken[0]) {
      int handled = 0;
      CuteQMaskGeneratorCall0 call = reinterpret_cast<CuteQMaskGeneratorCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  quint32 QMaskGenerator::nextMask()
  quint32 nextMask() override {
    if (taken[1]) {
      int handled = 0;
      CuteQMaskGeneratorCall1 call = reinterpret_cast<CuteQMaskGeneratorCall1>(taken[1]);
      quint32 given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQMaskGeneratorCall2 call = reinterpret_cast<CuteQMaskGeneratorCall2>(taken[2]);
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
      CuteQMaskGeneratorCall3 call = reinterpret_cast<CuteQMaskGeneratorCall3>(taken[3]);
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
      CuteQMaskGeneratorCall4 call = reinterpret_cast<CuteQMaskGeneratorCall4>(taken[4]);
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
      CuteQMaskGeneratorCall5 call = reinterpret_cast<CuteQMaskGeneratorCall5>(taken[5]);
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
      CuteQMaskGeneratorCall6 call = reinterpret_cast<CuteQMaskGeneratorCall6>(taken[6]);
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
      CuteQMaskGeneratorCall7 call = reinterpret_cast<CuteQMaskGeneratorCall7>(taken[7]);
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
      CuteQMaskGeneratorCall8 call = reinterpret_cast<CuteQMaskGeneratorCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QMaskGenerator::~QMaskGenerator()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMaskGeneratorD1Ev(QMaskGenerator *self) {
  delete self;
}

//  bool QMaskGenerator::seed()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QMaskGenerator4seedEv(QMaskGenerator *self) {
  return self->seed();
}

//  quint32 QMaskGenerator::nextMask()
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN14QMaskGenerator8nextMaskEv(QMaskGenerator *self) {
  return self->nextMask();
}

//  a Python function taken by a CuteQMaskGenerator, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMaskGenerator(
    QMaskGenerator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMaskGenerator *>(self)->take(key, call);
}
