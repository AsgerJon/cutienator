//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformsessionmanager.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_SESSIONMANAGER)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformsessionmanager.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QPlatformSessionManager that Python can take functions over in. Every QPlatformSessionManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_SESSIONMANAGER)
typedef QString * (*CuteQPlatformSessionManagerCall0)(const void *, int *);
#endif  // !defined(QT_NO_SESSIONMANAGER)
#if !defined(QT_NO_SESSIONMANAGER)
typedef QString * (*CuteQPlatformSessionManagerCall1)(const void *, int *);
#endif  // !defined(QT_NO_SESSIONMANAGER)
#if !defined(QT_NO_SESSIONMANAGER)
typedef bool (*CuteQPlatformSessionManagerCall2)(const void *, int *);
#endif  // !defined(QT_NO_SESSIONMANAGER)
#if !defined(QT_NO_SESSIONMANAGER)
typedef bool (*CuteQPlatformSessionManagerCall3)(const void *, int *);
#endif  // !defined(QT_NO_SESSIONMANAGER)
#if !defined(QT_NO_SESSIONMANAGER)
typedef void (*CuteQPlatformSessionManagerCall4)(const void *, int *);
#endif  // !defined(QT_NO_SESSIONMANAGER)
#if !defined(QT_NO_SESSIONMANAGER)
typedef void (*CuteQPlatformSessionManagerCall5)(const void *, int *);
#endif  // !defined(QT_NO_SESSIONMANAGER)
#if !defined(QT_NO_SESSIONMANAGER)
typedef void (*CuteQPlatformSessionManagerCall6)(const void *, int, int *);
#endif  // !defined(QT_NO_SESSIONMANAGER)
#if !defined(QT_NO_SESSIONMANAGER)
typedef int (*CuteQPlatformSessionManagerCall7)(const void *, int *);
#endif  // !defined(QT_NO_SESSIONMANAGER)
#if !defined(QT_NO_SESSIONMANAGER)
typedef void (*CuteQPlatformSessionManagerCall8)(const void *, const QString *, const QString *, int *);
#endif  // !defined(QT_NO_SESSIONMANAGER)
#if !defined(QT_NO_SESSIONMANAGER)
typedef bool (*CuteQPlatformSessionManagerCall9)(const void *, int *);
#endif  // !defined(QT_NO_SESSIONMANAGER)
#if !defined(QT_NO_SESSIONMANAGER)
typedef void (*CuteQPlatformSessionManagerCall10)(const void *, int *);
#endif  // !defined(QT_NO_SESSIONMANAGER)
class CuteQPlatformSessionManager : public QPlatformSessionManager {
public:
  using QPlatformSessionManager::QPlatformSessionManager;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_SESSIONMANAGER)
    if (!std::strcmp(key, "_ZNK23QPlatformSessionManager9sessionIdEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_SESSIONMANAGER)
#if !defined(QT_NO_SESSIONMANAGER)
    if (!std::strcmp(key, "_ZNK23QPlatformSessionManager10sessionKeyEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_SESSIONMANAGER)
#if !defined(QT_NO_SESSIONMANAGER)
    if (!std::strcmp(key, "_ZN23QPlatformSessionManager17allowsInteractionEv")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_SESSIONMANAGER)
#if !defined(QT_NO_SESSIONMANAGER)
    if (!std::strcmp(key, "_ZN23QPlatformSessionManager22allowsErrorInteractionEv")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_SESSIONMANAGER)
#if !defined(QT_NO_SESSIONMANAGER)
    if (!std::strcmp(key, "_ZN23QPlatformSessionManager7releaseEv")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_SESSIONMANAGER)
#if !defined(QT_NO_SESSIONMANAGER)
    if (!std::strcmp(key, "_ZN23QPlatformSessionManager6cancelEv")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_SESSIONMANAGER)
#if !defined(QT_NO_SESSIONMANAGER)
    if (!std::strcmp(key, "_ZN23QPlatformSessionManager14setRestartHintEN15QSessionManager11RestartHintE")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_SESSIONMANAGER)
#if !defined(QT_NO_SESSIONMANAGER)
    if (!std::strcmp(key, "_ZNK23QPlatformSessionManager11restartHintEv")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_SESSIONMANAGER)
#if !defined(QT_NO_SESSIONMANAGER)
    if (!std::strcmp(key, "_ZN23QPlatformSessionManager18setManagerPropertyERK7QStringS2_")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_SESSIONMANAGER)
#if !defined(QT_NO_SESSIONMANAGER)
    if (!std::strcmp(key, "_ZNK23QPlatformSessionManager8isPhase2Ev")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_SESSIONMANAGER)
#if !defined(QT_NO_SESSIONMANAGER)
    if (!std::strcmp(key, "_ZN23QPlatformSessionManager13requestPhase2Ev")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_SESSIONMANAGER)
    return false;
  }

#if !defined(QT_NO_SESSIONMANAGER)
  //  QString QPlatformSessionManager::sessionId() const
  QString sessionId() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformSessionManagerCall0 call = reinterpret_cast<CuteQPlatformSessionManagerCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlatformSessionManager::sessionId();
  }
#endif  // !defined(QT_NO_SESSIONMANAGER)

#if !defined(QT_NO_SESSIONMANAGER)
  //  QString QPlatformSessionManager::sessionKey() const
  QString sessionKey() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformSessionManagerCall1 call = reinterpret_cast<CuteQPlatformSessionManagerCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlatformSessionManager::sessionKey();
  }
#endif  // !defined(QT_NO_SESSIONMANAGER)

#if !defined(QT_NO_SESSIONMANAGER)
  //  bool QPlatformSessionManager::allowsInteraction()
  bool allowsInteraction() override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformSessionManagerCall2 call = reinterpret_cast<CuteQPlatformSessionManagerCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformSessionManager::allowsInteraction();
  }
#endif  // !defined(QT_NO_SESSIONMANAGER)

#if !defined(QT_NO_SESSIONMANAGER)
  //  bool QPlatformSessionManager::allowsErrorInteraction()
  bool allowsErrorInteraction() override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformSessionManagerCall3 call = reinterpret_cast<CuteQPlatformSessionManagerCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformSessionManager::allowsErrorInteraction();
  }
#endif  // !defined(QT_NO_SESSIONMANAGER)

#if !defined(QT_NO_SESSIONMANAGER)
  //  void QPlatformSessionManager::release()
  void release() override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformSessionManagerCall4 call = reinterpret_cast<CuteQPlatformSessionManagerCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformSessionManager::release();
  }
#endif  // !defined(QT_NO_SESSIONMANAGER)

#if !defined(QT_NO_SESSIONMANAGER)
  //  void QPlatformSessionManager::cancel()
  void cancel() override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformSessionManagerCall5 call = reinterpret_cast<CuteQPlatformSessionManagerCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformSessionManager::cancel();
  }
#endif  // !defined(QT_NO_SESSIONMANAGER)

#if !defined(QT_NO_SESSIONMANAGER)
  //  void
  //      QPlatformSessionManager::setRestartHint(QSessionManager::RestartH
  //      int restartHint)
  void setRestartHint(QSessionManager::RestartHint restartHint) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformSessionManagerCall6 call = reinterpret_cast<CuteQPlatformSessionManagerCall6>(taken[6]);
      call(this, static_cast<int>(restartHint), &handled);
      if (handled) return;
    }
    QPlatformSessionManager::setRestartHint(restartHint);
  }
#endif  // !defined(QT_NO_SESSIONMANAGER)

#if !defined(QT_NO_SESSIONMANAGER)
  //  QSessionManager::RestartHint QPlatformSessionManager::restartHint()
  //      const
  QSessionManager::RestartHint restartHint() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformSessionManagerCall7 call = reinterpret_cast<CuteQPlatformSessionManagerCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSessionManager::RestartHint>(given);
    }
    return QPlatformSessionManager::restartHint();
  }
#endif  // !defined(QT_NO_SESSIONMANAGER)

#if !defined(QT_NO_SESSIONMANAGER)
  //  void QPlatformSessionManager::setManagerProperty(const QString &name,
  //      const QString &value)
  void setManagerProperty(
      const QString &name,
      const QString &value) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformSessionManagerCall8 call = reinterpret_cast<CuteQPlatformSessionManagerCall8>(taken[8]);
      call(this, &name, &value, &handled);
      if (handled) return;
    }
    QPlatformSessionManager::setManagerProperty(name, value);
  }
#endif  // !defined(QT_NO_SESSIONMANAGER)

#if !defined(QT_NO_SESSIONMANAGER)
  //  bool QPlatformSessionManager::isPhase2() const
  bool isPhase2() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformSessionManagerCall9 call = reinterpret_cast<CuteQPlatformSessionManagerCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformSessionManager::isPhase2();
  }
#endif  // !defined(QT_NO_SESSIONMANAGER)

#if !defined(QT_NO_SESSIONMANAGER)
  //  void QPlatformSessionManager::requestPhase2()
  void requestPhase2() override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformSessionManagerCall10 call = reinterpret_cast<CuteQPlatformSessionManagerCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformSessionManager::requestPhase2();
  }
#endif  // !defined(QT_NO_SESSIONMANAGER)
};

//  QPlatformSessionManager::QPlatformSessionManager(const QString &id, const
//      QString &key)
extern "C" Q_DECL_EXPORT
QPlatformSessionManager *ritual_ZN23QPlatformSessionManagerC1ERK7QStringS2_(
    const QString *id,
    const QString *key) {
  return new CuteQPlatformSessionManager(*id, *key);
}

//  QPlatformSessionManager::~QPlatformSessionManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSessionManagerD1Ev(QPlatformSessionManager *self) {
  delete self;
}

//  QString QPlatformSessionManager::sessionId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QPlatformSessionManager9sessionIdEv(
    const QPlatformSessionManager *self) {
  return new QString(self->sessionId());
}

//  QString QPlatformSessionManager::sessionKey() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QPlatformSessionManager10sessionKeyEv(
    const QPlatformSessionManager *self) {
  return new QString(self->sessionKey());
}

//  bool QPlatformSessionManager::allowsInteraction()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QPlatformSessionManager17allowsInteractionEv(
    QPlatformSessionManager *self) {
  return self->allowsInteraction();
}

//  bool QPlatformSessionManager::allowsErrorInteraction()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QPlatformSessionManager22allowsErrorInteractionEv(
    QPlatformSessionManager *self) {
  return self->allowsErrorInteraction();
}

//  void QPlatformSessionManager::release()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSessionManager7releaseEv(
    QPlatformSessionManager *self) {
  self->release();
}

//  void QPlatformSessionManager::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSessionManager6cancelEv(
    QPlatformSessionManager *self) {
  self->cancel();
}

//  void QPlatformSessionManager::setRestartHint(QSessionManager::RestartHint
//      restartHint)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSessionManager14setRestartHintEN15QSessionManager11RestartHintE(
    QPlatformSessionManager *self,
    QSessionManager::RestartHint restartHint) {
  self->setRestartHint(restartHint);
}

//  QSessionManager::RestartHint QPlatformSessionManager::restartHint() const
extern "C" Q_DECL_EXPORT
QSessionManager::RestartHint ritual_ZNK23QPlatformSessionManager11restartHintEv(
    const QPlatformSessionManager *self) {
  return self->restartHint();
}

//  void QPlatformSessionManager::setRestartCommand(const QStringList
//      &command)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSessionManager17setRestartCommandERK5QListI7QStringE(
    QPlatformSessionManager *self,
    const QList<QString> *command) {
  self->setRestartCommand(*command);
}

//  QStringList QPlatformSessionManager::restartCommand() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK23QPlatformSessionManager14restartCommandEv(
    const QPlatformSessionManager *self) {
  return new QList<QString>(self->restartCommand());
}

//  void QPlatformSessionManager::setDiscardCommand(const QStringList
//      &command)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSessionManager17setDiscardCommandERK5QListI7QStringE(
    QPlatformSessionManager *self,
    const QList<QString> *command) {
  self->setDiscardCommand(*command);
}

//  QStringList QPlatformSessionManager::discardCommand() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK23QPlatformSessionManager14discardCommandEv(
    const QPlatformSessionManager *self) {
  return new QList<QString>(self->discardCommand());
}

//  void QPlatformSessionManager::setManagerProperty(const QString &name,
//      const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSessionManager18setManagerPropertyERK7QStringS2_(
    QPlatformSessionManager *self,
    const QString *name,
    const QString *value) {
  self->setManagerProperty(*name, *value);
}

//  void QPlatformSessionManager::setManagerProperty(const QString &name,
//      const QStringList &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSessionManager18setManagerPropertyERK7QStringRK5QListIS0_E(
    QPlatformSessionManager *self,
    const QString *name,
    const QList<QString> *value) {
  self->setManagerProperty(*name, *value);
}

//  bool QPlatformSessionManager::isPhase2() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QPlatformSessionManager8isPhase2Ev(
    const QPlatformSessionManager *self) {
  return self->isPhase2();
}

//  void QPlatformSessionManager::requestPhase2()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSessionManager13requestPhase2Ev(
    QPlatformSessionManager *self) {
  self->requestPhase2();
}

//  void QPlatformSessionManager::appCommitData()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSessionManager13appCommitDataEv(
    QPlatformSessionManager *self) {
  self->appCommitData();
}

//  void QPlatformSessionManager::appSaveState()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformSessionManager12appSaveStateEv(
    QPlatformSessionManager *self) {
  self->appSaveState();
}

//  a Python function taken by a CuteQPlatformSessionManager, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformSessionManager(
    QPlatformSessionManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformSessionManager *>(self)->take(key, call);
}

//  QString QPlatformSessionManager::sessionId() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK23QPlatformSessionManager9sessionIdEv(
    const QPlatformSessionManager *self) {
  return new QString(self->QPlatformSessionManager::sessionId());
}

//  QString QPlatformSessionManager::sessionKey() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK23QPlatformSessionManager10sessionKeyEv(
    const QPlatformSessionManager *self) {
  return new QString(self->QPlatformSessionManager::sessionKey());
}

//  bool QPlatformSessionManager::allowsInteraction()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN23QPlatformSessionManager17allowsInteractionEv(
    QPlatformSessionManager *self) {
  return self->QPlatformSessionManager::allowsInteraction();
}

//  bool QPlatformSessionManager::allowsErrorInteraction()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN23QPlatformSessionManager22allowsErrorInteractionEv(
    QPlatformSessionManager *self) {
  return self->QPlatformSessionManager::allowsErrorInteraction();
}

//  void QPlatformSessionManager::release()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QPlatformSessionManager7releaseEv(
    QPlatformSessionManager *self) {
  self->QPlatformSessionManager::release();
}

//  void QPlatformSessionManager::cancel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QPlatformSessionManager6cancelEv(
    QPlatformSessionManager *self) {
  self->QPlatformSessionManager::cancel();
}

//  void QPlatformSessionManager::setRestartHint(QSessionManager::RestartHint
//      restartHint)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QPlatformSessionManager14setRestartHintEN15QSessionManager11RestartHintE(
    QPlatformSessionManager *self,
    QSessionManager::RestartHint restartHint) {
  self->QPlatformSessionManager::setRestartHint(restartHint);
}

//  QSessionManager::RestartHint QPlatformSessionManager::restartHint() const
extern "C" Q_DECL_EXPORT
QSessionManager::RestartHint ritual_own_ZNK23QPlatformSessionManager11restartHintEv(
    const QPlatformSessionManager *self) {
  return self->QPlatformSessionManager::restartHint();
}

//  void QPlatformSessionManager::setManagerProperty(const QString &name,
//      const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QPlatformSessionManager18setManagerPropertyERK7QStringS2_(
    QPlatformSessionManager *self,
    const QString *name,
    const QString *value) {
  self->QPlatformSessionManager::setManagerProperty(*name, *value);
}

//  bool QPlatformSessionManager::isPhase2() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK23QPlatformSessionManager8isPhase2Ev(
    const QPlatformSessionManager *self) {
  return self->QPlatformSessionManager::isPhase2();
}

//  void QPlatformSessionManager::requestPhase2()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QPlatformSessionManager13requestPhase2Ev(
    QPlatformSessionManager *self) {
  self->QPlatformSessionManager::requestPhase2();
}

#endif  // !defined(QT_NO_SESSIONMANAGER)
