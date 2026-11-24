//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qdownloadhelperservice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qdownloadhelperservice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <cstring>

//  A Qt3DCore::QDownloadRequest that Python can take functions over in. Every Qt3DCore::QDownloadRequest
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_QDownloadRequestCall0)(const void *, int *);
typedef void (*CuteQt3DCore_QDownloadRequestCall1)(const void *, int *);
class CuteQt3DCore_QDownloadRequest : public Qt3DCore::QDownloadRequest {
public:
  using Qt3DCore::QDownloadRequest::QDownloadRequest;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore16QDownloadRequest12onDownloadedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore16QDownloadRequest11onCompletedEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QDownloadRequest::onDownloaded()
  void onDownloaded() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QDownloadRequestCall0 call = reinterpret_cast<CuteQt3DCore_QDownloadRequestCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QDownloadRequest::onDownloaded();
  }

  //  void Qt3DCore::QDownloadRequest::onCompleted()
  void onCompleted() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QDownloadRequestCall1 call = reinterpret_cast<CuteQt3DCore_QDownloadRequestCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  Qt3DCore::QDownloadRequest::~QDownloadRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore16QDownloadRequestD1Ev(
    Qt3DCore::QDownloadRequest *self) {
  delete self;
}

//  QUrl Qt3DCore::QDownloadRequest::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK8Qt3DCore16QDownloadRequest3urlEv(
    const Qt3DCore::QDownloadRequest *self) {
  return new QUrl(self->url());
}

//  bool Qt3DCore::QDownloadRequest::succeeded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore16QDownloadRequest9succeededEv(
    const Qt3DCore::QDownloadRequest *self) {
  return self->succeeded();
}

//  bool Qt3DCore::QDownloadRequest::cancelled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore16QDownloadRequest9cancelledEv(
    const Qt3DCore::QDownloadRequest *self) {
  return self->cancelled();
}

//  void Qt3DCore::QDownloadRequest::onDownloaded()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore16QDownloadRequest12onDownloadedEv(
    Qt3DCore::QDownloadRequest *self) {
  self->onDownloaded();
}

//  void Qt3DCore::QDownloadRequest::onCompleted()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore16QDownloadRequest11onCompletedEv(
    Qt3DCore::QDownloadRequest *self) {
  self->onCompleted();
}

//  a Python function taken by a CuteQt3DCore_QDownloadRequest, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QDownloadRequest(
    Qt3DCore::QDownloadRequest *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QDownloadRequest *>(self)->take(key, call);
}

//  void Qt3DCore::QDownloadRequest::onDownloaded()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore16QDownloadRequest12onDownloadedEv(
    Qt3DCore::QDownloadRequest *self) {
  self->Qt3DCore::QDownloadRequest::onDownloaded();
}
