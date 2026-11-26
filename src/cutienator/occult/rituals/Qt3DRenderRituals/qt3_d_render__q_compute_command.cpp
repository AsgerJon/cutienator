//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qcomputecommand.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qcomputecommand.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QComputeCommand that Python can take functions over in. Every Qt3DRender::QComputeCommand
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QComputeCommandCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QComputeCommandCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QComputeCommandCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QComputeCommandCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QComputeCommandCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QComputeCommandCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QComputeCommandCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QComputeCommand : public Qt3DRender::QComputeCommand {
public:
  using Qt3DRender::QComputeCommand::QComputeCommand;
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
      CuteQt3DRender_QComputeCommandCall0 call = reinterpret_cast<CuteQt3DRender_QComputeCommandCall0>(taken[0]);
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
      CuteQt3DRender_QComputeCommandCall1 call = reinterpret_cast<CuteQt3DRender_QComputeCommandCall1>(taken[1]);
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
      CuteQt3DRender_QComputeCommandCall2 call = reinterpret_cast<CuteQt3DRender_QComputeCommandCall2>(taken[2]);
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
      CuteQt3DRender_QComputeCommandCall3 call = reinterpret_cast<CuteQt3DRender_QComputeCommandCall3>(taken[3]);
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
      CuteQt3DRender_QComputeCommandCall4 call = reinterpret_cast<CuteQt3DRender_QComputeCommandCall4>(taken[4]);
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
      CuteQt3DRender_QComputeCommandCall5 call = reinterpret_cast<CuteQt3DRender_QComputeCommandCall5>(taken[5]);
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
      CuteQt3DRender_QComputeCommandCall6 call = reinterpret_cast<CuteQt3DRender_QComputeCommandCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QComputeCommand::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender15QComputeCommand10metaObjectEv(
    const Qt3DRender::QComputeCommand *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QComputeCommand::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender15QComputeCommand11qt_metacastEPKc(
    Qt3DRender::QComputeCommand *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QComputeCommand::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender15QComputeCommand11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QComputeCommand *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QComputeCommand::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender15QComputeCommand2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QComputeCommand::tr(s, c, n));
}

//  Qt3DRender::QComputeCommand::QComputeCommand(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QComputeCommand *ritual_ZN10Qt3DRender15QComputeCommandC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QComputeCommand(parent);
}

//  Qt3DRender::QComputeCommand::~QComputeCommand()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15QComputeCommandD1Ev(
    Qt3DRender::QComputeCommand *self) {
  delete self;
}

//  int Qt3DRender::QComputeCommand::workGroupX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender15QComputeCommand10workGroupXEv(
    const Qt3DRender::QComputeCommand *self) {
  return self->workGroupX();
}

//  int Qt3DRender::QComputeCommand::workGroupY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender15QComputeCommand10workGroupYEv(
    const Qt3DRender::QComputeCommand *self) {
  return self->workGroupY();
}

//  int Qt3DRender::QComputeCommand::workGroupZ() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender15QComputeCommand10workGroupZEv(
    const Qt3DRender::QComputeCommand *self) {
  return self->workGroupZ();
}

//  RunType Qt3DRender::QComputeCommand::runType() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QComputeCommand::RunType ritual_ZNK10Qt3DRender15QComputeCommand7runTypeEv(
    const Qt3DRender::QComputeCommand *self) {
  return self->runType();
}

//  void Qt3DRender::QComputeCommand::setWorkGroupX(int workGroupX)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15QComputeCommand13setWorkGroupXEi(
    Qt3DRender::QComputeCommand *self,
    int workGroupX) {
  self->setWorkGroupX(workGroupX);
}

//  void Qt3DRender::QComputeCommand::setWorkGroupY(int workGroupY)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15QComputeCommand13setWorkGroupYEi(
    Qt3DRender::QComputeCommand *self,
    int workGroupY) {
  self->setWorkGroupY(workGroupY);
}

//  void Qt3DRender::QComputeCommand::setWorkGroupZ(int workGroupZ)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15QComputeCommand13setWorkGroupZEi(
    Qt3DRender::QComputeCommand *self,
    int workGroupZ) {
  self->setWorkGroupZ(workGroupZ);
}

//  void Qt3DRender::QComputeCommand::setRunType(RunType runType)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15QComputeCommand10setRunTypeENS0_7RunTypeE(
    Qt3DRender::QComputeCommand *self,
    Qt3DRender::QComputeCommand::RunType runType) {
  self->setRunType(runType);
}

//  void Qt3DRender::QComputeCommand::trigger(int frameCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15QComputeCommand7triggerEi(
    Qt3DRender::QComputeCommand *self,
    int frameCount) {
  self->trigger(frameCount);
}

//  void Qt3DRender::QComputeCommand::trigger(int workGroupX, int workGroupY,
//      int workGroupZ, int frameCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15QComputeCommand7triggerEiiii(
    Qt3DRender::QComputeCommand *self,
    int workGroupX,
    int workGroupY,
    int workGroupZ,
    int frameCount) {
  self->trigger(workGroupX, workGroupY, workGroupZ, frameCount);
}

//  void Qt3DRender::QComputeCommand::workGroupXChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15QComputeCommand17workGroupXChangedEv(
    Qt3DRender::QComputeCommand *self) {
  self->workGroupXChanged();
}

//  void Qt3DRender::QComputeCommand::workGroupYChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15QComputeCommand17workGroupYChangedEv(
    Qt3DRender::QComputeCommand *self) {
  self->workGroupYChanged();
}

//  void Qt3DRender::QComputeCommand::workGroupZChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15QComputeCommand17workGroupZChangedEv(
    Qt3DRender::QComputeCommand *self) {
  self->workGroupZChanged();
}

//  void Qt3DRender::QComputeCommand::runTypeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15QComputeCommand14runTypeChangedEv(
    Qt3DRender::QComputeCommand *self) {
  self->runTypeChanged();
}

//  QComputeCommandPrivate *Qt3DRender::QComputeCommand::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QComputeCommandPrivate *ritual_ZN10Qt3DRender15QComputeCommand6d_funcEv(
    Qt3DRender::QComputeCommand *self) {
  return self->d_func();
}

//  const QComputeCommandPrivate *Qt3DRender::QComputeCommand::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QComputeCommandPrivate *ritual_ZNK10Qt3DRender15QComputeCommand6d_funcEv(
    const Qt3DRender::QComputeCommand *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QComputeCommand, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QComputeCommand(
    Qt3DRender::QComputeCommand *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QComputeCommand *>(self)->take(key, call);
}
