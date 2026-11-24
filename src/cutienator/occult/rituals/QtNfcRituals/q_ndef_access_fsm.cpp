//  Written by dev_tooling.RitualGenerator from the records of
//  QtNfc/6.12.0/QtNfc/private/qndefaccessfsm_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNfc/6.12.0/QtNfc/private/qtnfcglobal_p.h>
#include <QtNfc/QtNfc>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNfc/6.12.0/QtNfc/private/qndefaccessfsm_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtNfc/qndefmessage.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QNdefAccessFsm that Python can take functions over in. Every QNdefAccessFsm
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQNdefAccessFsmCall0)(const void *, const QByteArray *, int *);
typedef int (*CuteQNdefAccessFsmCall1)(const void *, int *);
typedef int (*CuteQNdefAccessFsmCall2)(const void *, int *);
class CuteQNdefAccessFsm : public QNdefAccessFsm {
public:
  using QNdefAccessFsm::QNdefAccessFsm;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QNdefAccessFsm15provideResponseERK10QByteArray")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QNdefAccessFsm17detectNdefSupportEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QNdefAccessFsm12readMessagesEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  Action QNdefAccessFsm::provideResponse(const QByteArray &response)
  QNdefAccessFsm::Action provideResponse(
      const QByteArray &response) override {
    if (taken[0]) {
      int handled = 0;
      CuteQNdefAccessFsmCall0 call = reinterpret_cast<CuteQNdefAccessFsmCall0>(taken[0]);
      int given = call(this, &response, &handled);
      if (handled) return static_cast<QNdefAccessFsm::Action>(given);
    }
    return {};
  }

  //  Action QNdefAccessFsm::detectNdefSupport()
  QNdefAccessFsm::Action detectNdefSupport() override {
    if (taken[1]) {
      int handled = 0;
      CuteQNdefAccessFsmCall1 call = reinterpret_cast<CuteQNdefAccessFsmCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QNdefAccessFsm::Action>(given);
    }
    return {};
  }

  //  Action QNdefAccessFsm::readMessages()
  QNdefAccessFsm::Action readMessages() override {
    if (taken[2]) {
      int handled = 0;
      CuteQNdefAccessFsmCall2 call = reinterpret_cast<CuteQNdefAccessFsmCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QNdefAccessFsm::Action>(given);
    }
    return {};
  }
};

//  QNdefAccessFsm::~QNdefAccessFsm()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QNdefAccessFsmD1Ev(QNdefAccessFsm *self) {
  delete self;
}

//  Action QNdefAccessFsm::provideResponse(const QByteArray &response)
extern "C" Q_DECL_EXPORT
QNdefAccessFsm::Action ritual_ZN14QNdefAccessFsm15provideResponseERK10QByteArray(
    QNdefAccessFsm *self,
    const QByteArray *response) {
  return self->provideResponse(*response);
}

//  Action QNdefAccessFsm::detectNdefSupport()
extern "C" Q_DECL_EXPORT
QNdefAccessFsm::Action ritual_ZN14QNdefAccessFsm17detectNdefSupportEv(
    QNdefAccessFsm *self) {
  return self->detectNdefSupport();
}

//  Action QNdefAccessFsm::readMessages()
extern "C" Q_DECL_EXPORT
QNdefAccessFsm::Action ritual_ZN14QNdefAccessFsm12readMessagesEv(
    QNdefAccessFsm *self) {
  return self->readMessages();
}

//  Action QNdefAccessFsm::writeMessages(const QList<QNdefMessage> &messages)
extern "C" Q_DECL_EXPORT
QNdefAccessFsm::Action ritual_ZN14QNdefAccessFsm13writeMessagesERK5QListI12QNdefMessageE(
    QNdefAccessFsm *self,
    const QList<QNdefMessage> *messages) {
  return self->writeMessages(*messages);
}

//  a Python function taken by a CuteQNdefAccessFsm, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNdefAccessFsm(
    QNdefAccessFsm *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNdefAccessFsm *>(self)->take(key, call);
}
