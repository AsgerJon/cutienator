//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qsysteminformationservice_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qsysteminformationservice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A Qt3DCore::QSystemInformationService that Python can take functions over in. Every Qt3DCore::QSystemInformationService
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QSystemInformationServiceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QSystemInformationServiceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QSystemInformationServiceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QSystemInformationServiceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QSystemInformationServiceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QSystemInformationServiceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QSystemInformationServiceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_QSystemInformationService : public Qt3DCore::QSystemInformationService {
public:
  using Qt3DCore::QSystemInformationService::QSystemInformationService;
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
      CuteQt3DCore_QSystemInformationServiceCall0 call = reinterpret_cast<CuteQt3DCore_QSystemInformationServiceCall0>(taken[0]);
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
      CuteQt3DCore_QSystemInformationServiceCall1 call = reinterpret_cast<CuteQt3DCore_QSystemInformationServiceCall1>(taken[1]);
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
      CuteQt3DCore_QSystemInformationServiceCall2 call = reinterpret_cast<CuteQt3DCore_QSystemInformationServiceCall2>(taken[2]);
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
      CuteQt3DCore_QSystemInformationServiceCall3 call = reinterpret_cast<CuteQt3DCore_QSystemInformationServiceCall3>(taken[3]);
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
      CuteQt3DCore_QSystemInformationServiceCall4 call = reinterpret_cast<CuteQt3DCore_QSystemInformationServiceCall4>(taken[4]);
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
      CuteQt3DCore_QSystemInformationServiceCall5 call = reinterpret_cast<CuteQt3DCore_QSystemInformationServiceCall5>(taken[5]);
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
      CuteQt3DCore_QSystemInformationServiceCall6 call = reinterpret_cast<CuteQt3DCore_QSystemInformationServiceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::QSystemInformationService::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore25QSystemInformationService10metaObjectEv(
    const Qt3DCore::QSystemInformationService *self) {
  return self->metaObject();
}

//  void *Qt3DCore::QSystemInformationService::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore25QSystemInformationService11qt_metacastEPKc(
    Qt3DCore::QSystemInformationService *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::QSystemInformationService::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore25QSystemInformationService11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::QSystemInformationService *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::QSystemInformationService::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore25QSystemInformationService2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::QSystemInformationService::tr(s, c, n));
}

//  Qt3DCore::QSystemInformationService::QSystemInformationService(QAspectEng
//      ine *aspectEngine)
extern "C" Q_DECL_EXPORT
Qt3DCore::QSystemInformationService *ritual_ZN8Qt3DCore25QSystemInformationServiceC1EPNS_13QAspectEngineE(
    Qt3DCore::QAspectEngine *aspectEngine) {
  return new CuteQt3DCore_QSystemInformationService(aspectEngine);
}

//  bool Qt3DCore::QSystemInformationService::isTraceEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore25QSystemInformationService14isTraceEnabledEv(
    const Qt3DCore::QSystemInformationService *self) {
  return self->isTraceEnabled();
}

//  bool Qt3DCore::QSystemInformationService::isGraphicsTraceEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore25QSystemInformationService22isGraphicsTraceEnabledEv(
    const Qt3DCore::QSystemInformationService *self) {
  return self->isGraphicsTraceEnabled();
}

//  bool Qt3DCore::QSystemInformationService::isCommandServerEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore25QSystemInformationService22isCommandServerEnabledEv(
    const Qt3DCore::QSystemInformationService *self) {
  return self->isCommandServerEnabled();
}

//  QStringList Qt3DCore::QSystemInformationService::aspectNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK8Qt3DCore25QSystemInformationService11aspectNamesEv(
    const Qt3DCore::QSystemInformationService *self) {
  return new QList<QString>(self->aspectNames());
}

//  int Qt3DCore::QSystemInformationService::threadPoolThreadCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8Qt3DCore25QSystemInformationService21threadPoolThreadCountEv(
    const Qt3DCore::QSystemInformationService *self) {
  return self->threadPoolThreadCount();
}

//  void Qt3DCore::QSystemInformationService::writePreviousFrameTraces()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore25QSystemInformationService24writePreviousFrameTracesEv(
    Qt3DCore::QSystemInformationService *self) {
  self->writePreviousFrameTraces();
}

//  void Qt3DCore::QSystemInformationService::revealLogFolder()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore25QSystemInformationService15revealLogFolderEv(
    Qt3DCore::QSystemInformationService *self) {
  self->revealLogFolder();
}

//  void Qt3DCore::QSystemInformationService::setTraceEnabled(bool
//      traceEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore25QSystemInformationService15setTraceEnabledEb(
    Qt3DCore::QSystemInformationService *self,
    bool traceEnabled) {
  self->setTraceEnabled(traceEnabled);
}

//  void Qt3DCore::QSystemInformationService::setGraphicsTraceEnabled(bool
//      graphicsTraceEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore25QSystemInformationService23setGraphicsTraceEnabledEb(
    Qt3DCore::QSystemInformationService *self,
    bool graphicsTraceEnabled) {
  self->setGraphicsTraceEnabled(graphicsTraceEnabled);
}

//  QVariant Qt3DCore::QSystemInformationService::executeCommand(const
//      QString &command)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8Qt3DCore25QSystemInformationService14executeCommandERK7QString(
    Qt3DCore::QSystemInformationService *self,
    const QString *command) {
  return new QVariant(self->executeCommand(*command));
}

//  void Qt3DCore::QSystemInformationService::dumpCommand(const QString
//      &command)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore25QSystemInformationService11dumpCommandERK7QString(
    Qt3DCore::QSystemInformationService *self,
    const QString *command) {
  self->dumpCommand(*command);
}

//  void Qt3DCore::QSystemInformationService::traceEnabledChanged(bool
//      traceEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore25QSystemInformationService19traceEnabledChangedEb(
    Qt3DCore::QSystemInformationService *self,
    bool traceEnabled) {
  self->traceEnabledChanged(traceEnabled);
}

//  void
//      Qt3DCore::QSystemInformationService::graphicsTraceEnabledChanged(bool
//      graphicsTraceEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore25QSystemInformationService27graphicsTraceEnabledChangedEb(
    Qt3DCore::QSystemInformationService *self,
    bool graphicsTraceEnabled) {
  self->graphicsTraceEnabledChanged(graphicsTraceEnabled);
}

//  QSystemInformationServicePrivate
//      *Qt3DCore::QSystemInformationService::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QSystemInformationServicePrivate *ritual_ZN8Qt3DCore25QSystemInformationService6d_funcEv(
    Qt3DCore::QSystemInformationService *self) {
  return self->d_func();
}

//  const QSystemInformationServicePrivate
//      *Qt3DCore::QSystemInformationService::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QSystemInformationServicePrivate *ritual_ZNK8Qt3DCore25QSystemInformationService6d_funcEv(
    const Qt3DCore::QSystemInformationService *self) {
  return self->d_func();
}

//  Qt3DCore::QSystemInformationService::QSystemInformationService(QAspectEng
//      ine *aspectEngine, const QString &description)
extern "C" Q_DECL_EXPORT
Qt3DCore::QSystemInformationService *ritual_ZN8Qt3DCore25QSystemInformationServiceC1EPNS_13QAspectEngineERK7QString(
    Qt3DCore::QAspectEngine *aspectEngine,
    const QString *description) {
  return new CuteQt3DCore_QSystemInformationService(
      aspectEngine,
      *description);
}

//  Qt3DCore::QSystemInformationService::QSystemInformationService(QSystemInf
//      ormationServicePrivate &dd)
extern "C" Q_DECL_EXPORT
Qt3DCore::QSystemInformationService *ritual_ZN8Qt3DCore25QSystemInformationServiceC1ERNS_32QSystemInformationServicePrivateE(
    Qt3DCore::QSystemInformationServicePrivate *dd) {
  return new CuteQt3DCore_QSystemInformationService(*dd);
}

//  a Python function taken by a CuteQt3DCore_QSystemInformationService, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QSystemInformationService(
    Qt3DCore::QSystemInformationService *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QSystemInformationService *>(self)->take(key, call);
}
