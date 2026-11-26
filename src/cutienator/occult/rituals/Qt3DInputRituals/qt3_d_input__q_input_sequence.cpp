//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/qinputsequence.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DInput/qinputsequence.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DInput/Qt3DInput>

//  A Qt3DInput::QInputSequence that Python can take functions over in. Every Qt3DInput::QInputSequence
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QInputSequenceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QInputSequenceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QInputSequenceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QInputSequenceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QInputSequenceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QInputSequenceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QInputSequenceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DInput_QInputSequence : public Qt3DInput::QInputSequence {
public:
  using Qt3DInput::QInputSequence::QInputSequence;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DInput_QInputSequenceCall0 call = reinterpret_cast<CuteQt3DInput_QInputSequenceCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_QInputSequenceCall1 call = reinterpret_cast<CuteQt3DInput_QInputSequenceCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DInput_QInputSequenceCall2 call = reinterpret_cast<CuteQt3DInput_QInputSequenceCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DInput_QInputSequenceCall3 call = reinterpret_cast<CuteQt3DInput_QInputSequenceCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DInput_QInputSequenceCall4 call = reinterpret_cast<CuteQt3DInput_QInputSequenceCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DInput_QInputSequenceCall5 call = reinterpret_cast<CuteQt3DInput_QInputSequenceCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DInput_QInputSequenceCall6 call = reinterpret_cast<CuteQt3DInput_QInputSequenceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DInput::QInputSequence::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput14QInputSequence10metaObjectEv(
    const Qt3DInput::QInputSequence *self) {
  return self->metaObject();
}

//  void *Qt3DInput::QInputSequence::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput14QInputSequence11qt_metacastEPKc(
    Qt3DInput::QInputSequence *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DInput::QInputSequence::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput14QInputSequence11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::QInputSequence *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DInput::QInputSequence::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput14QInputSequence2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QInputSequence::tr(s, c, n));
}

//  Qt3DInput::QInputSequence::QInputSequence(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DInput::QInputSequence *ritual_ZN9Qt3DInput14QInputSequenceC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DInput_QInputSequence(parent);
}

//  Qt3DInput::QInputSequence::~QInputSequence()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput14QInputSequenceD1Ev(
    Qt3DInput::QInputSequence *self) {
  delete self;
}

//  int Qt3DInput::QInputSequence::timeout() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput14QInputSequence7timeoutEv(
    const Qt3DInput::QInputSequence *self) {
  return self->timeout();
}

//  int Qt3DInput::QInputSequence::buttonInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput14QInputSequence14buttonIntervalEv(
    const Qt3DInput::QInputSequence *self) {
  return self->buttonInterval();
}

//  void Qt3DInput::QInputSequence::addSequence(QAbstractActionInput *input)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput14QInputSequence11addSequenceEPNS_20QAbstractActionInputE(
    Qt3DInput::QInputSequence *self,
    Qt3DInput::QAbstractActionInput *input) {
  self->addSequence(input);
}

//  void Qt3DInput::QInputSequence::removeSequence(QAbstractActionInput
//      *input)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput14QInputSequence14removeSequenceEPNS_20QAbstractActionInputE(
    Qt3DInput::QInputSequence *self,
    Qt3DInput::QAbstractActionInput *input) {
  self->removeSequence(input);
}

//  QList<QAbstractActionInput *> Qt3DInput::QInputSequence::sequences()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DInput::QAbstractActionInput *> *ritual_ZNK9Qt3DInput14QInputSequence9sequencesEv(
    const Qt3DInput::QInputSequence *self) {
  return new QList<Qt3DInput::QAbstractActionInput *>(self->sequences());
}

//  void Qt3DInput::QInputSequence::setTimeout(int timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput14QInputSequence10setTimeoutEi(
    Qt3DInput::QInputSequence *self,
    int timeout) {
  self->setTimeout(timeout);
}

//  void Qt3DInput::QInputSequence::setButtonInterval(int buttonInterval)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput14QInputSequence17setButtonIntervalEi(
    Qt3DInput::QInputSequence *self,
    int buttonInterval) {
  self->setButtonInterval(buttonInterval);
}

//  void Qt3DInput::QInputSequence::timeoutChanged(int timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput14QInputSequence14timeoutChangedEi(
    Qt3DInput::QInputSequence *self,
    int timeout) {
  self->timeoutChanged(timeout);
}

//  void Qt3DInput::QInputSequence::buttonIntervalChanged(int buttonInterval)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput14QInputSequence21buttonIntervalChangedEi(
    Qt3DInput::QInputSequence *self,
    int buttonInterval) {
  self->buttonIntervalChanged(buttonInterval);
}

//  QInputSequencePrivate *Qt3DInput::QInputSequence::d_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QInputSequencePrivate *ritual_ZN9Qt3DInput14QInputSequence6d_funcEv(
    Qt3DInput::QInputSequence *self) {
  return self->d_func();
}

//  const QInputSequencePrivate *Qt3DInput::QInputSequence::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QInputSequencePrivate *ritual_ZNK9Qt3DInput14QInputSequence6d_funcEv(
    const Qt3DInput::QInputSequence *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DInput_QInputSequence, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QInputSequence(
    Qt3DInput::QInputSequence *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QInputSequence *>(self)->take(key, call);
}

//  a QList<Qt3DInput::QAbstractActionInput *> a ritual of
//      Qt3DInput::QInputSequence gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_QInputSequence__QList_Qt3DInput_QAbstractActionInput(
    QList<Qt3DInput::QAbstractActionInput *> *self) {
  delete self;
}
