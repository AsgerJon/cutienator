//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebenginefilesystemaccessrequest.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWebEngineCore/qwebenginefilesystemaccessrequest.h>
#include <QtCore/qurl.h>
#include <memory>
#include <QtWebEngineCore/QtWebEngineCore>

//  QWebEngineFileSystemAccessRequest::QWebEngineFileSystemAccessRequest()
extern "C" Q_DECL_EXPORT
QWebEngineFileSystemAccessRequest *ritual_ZN33QWebEngineFileSystemAccessRequestC1Ev() {
  return new QWebEngineFileSystemAccessRequest();
}

//  QWebEngineFileSystemAccessRequest::QWebEngineFileSystemAccessRequest(cons
//      t QWebEngineFileSystemAccessRequest &other)
extern "C" Q_DECL_EXPORT
QWebEngineFileSystemAccessRequest *ritual_ZN33QWebEngineFileSystemAccessRequestC1ERKS_(
    const QWebEngineFileSystemAccessRequest *other) {
  return new QWebEngineFileSystemAccessRequest(*other);
}

//  QWebEngineFileSystemAccessRequest
//      &QWebEngineFileSystemAccessRequest::operator=(const
//      QWebEngineFileSystemAccessRequest &other)
extern "C" Q_DECL_EXPORT
QWebEngineFileSystemAccessRequest *ritual_ZN33QWebEngineFileSystemAccessRequestaSERKS_(
    QWebEngineFileSystemAccessRequest *self,
    const QWebEngineFileSystemAccessRequest *other) {
  return &(self->operator=(*other));
}

//  QWebEngineFileSystemAccessRequest::QWebEngineFileSystemAccessRequest(QWeb
//      EngineFileSystemAccessRequest &&other)
extern "C" Q_DECL_EXPORT
QWebEngineFileSystemAccessRequest *ritual_ZN33QWebEngineFileSystemAccessRequestC1EOS_(
    QWebEngineFileSystemAccessRequest *other) {
  return new QWebEngineFileSystemAccessRequest(std::move(*other));
}

//  QWebEngineFileSystemAccessRequest &QWebEngineFileSystemAccessRequest::ope
//      rator=(QWebEngineFileSystemAccessRequest &&other)
extern "C" Q_DECL_EXPORT
QWebEngineFileSystemAccessRequest *ritual_ZN33QWebEngineFileSystemAccessRequestaSEOS_(
    QWebEngineFileSystemAccessRequest *self,
    QWebEngineFileSystemAccessRequest *other) {
  return &(self->operator=(std::move(*other)));
}

//  QWebEngineFileSystemAccessRequest::~QWebEngineFileSystemAccessRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QWebEngineFileSystemAccessRequestD1Ev(
    QWebEngineFileSystemAccessRequest *self) {
  delete self;
}

//  void
//      QWebEngineFileSystemAccessRequest::swap(QWebEngineFileSystemAccessReq
//      uest &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QWebEngineFileSystemAccessRequest4swapERS_(
    QWebEngineFileSystemAccessRequest *self,
    QWebEngineFileSystemAccessRequest *other) {
  self->swap(*other);
}

//  void QWebEngineFileSystemAccessRequest::accept()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QWebEngineFileSystemAccessRequest6acceptEv(
    QWebEngineFileSystemAccessRequest *self) {
  self->accept();
}

//  void QWebEngineFileSystemAccessRequest::reject()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QWebEngineFileSystemAccessRequest6rejectEv(
    QWebEngineFileSystemAccessRequest *self) {
  self->reject();
}

//  QUrl QWebEngineFileSystemAccessRequest::origin() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK33QWebEngineFileSystemAccessRequest6originEv(
    const QWebEngineFileSystemAccessRequest *self) {
  return new QUrl(self->origin());
}

//  QUrl QWebEngineFileSystemAccessRequest::filePath() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK33QWebEngineFileSystemAccessRequest8filePathEv(
    const QWebEngineFileSystemAccessRequest *self) {
  return new QUrl(self->filePath());
}

//  HandleType QWebEngineFileSystemAccessRequest::handleType() const
extern "C" Q_DECL_EXPORT
QWebEngineFileSystemAccessRequest::HandleType ritual_ZNK33QWebEngineFileSystemAccessRequest10handleTypeEv(
    const QWebEngineFileSystemAccessRequest *self) {
  return self->handleType();
}

//  AccessFlags QWebEngineFileSystemAccessRequest::accessFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK33QWebEngineFileSystemAccessRequest11accessFlagsEv(
    const QWebEngineFileSystemAccessRequest *self) {
  return static_cast<int>(self->accessFlags().toInt());
}

//  bool operator==(const QWebEngineFileSystemAccessRequest &lhs, const
//      QWebEngineFileSystemAccessRequest &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK33QWebEngineFileSystemAccessRequestS1_(
    const QWebEngineFileSystemAccessRequest *lhs,
    const QWebEngineFileSystemAccessRequest *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QWebEngineFileSystemAccessRequest &lhs, const
//      QWebEngineFileSystemAccessRequest &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK33QWebEngineFileSystemAccessRequestS1_(
    const QWebEngineFileSystemAccessRequest *lhs,
    const QWebEngineFileSystemAccessRequest *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QWebEngineFileSystemAccessRequest::QWebEngineFileSystemAccessRequest(std:
//      :shared_ptr<QtWebEngineCore::FileSystemAccessPermissionRequestControl
//      ler> a0)
extern "C" Q_DECL_EXPORT
QWebEngineFileSystemAccessRequest *ritual_ZN33QWebEngineFileSystemAccessRequestC1ESt10shared_ptrIN15QtWebEngineCore43FileSystemAccessPermissionRequestControllerEE(
    const std::shared_ptr<QtWebEngineCore::FileSystemAccessPermissionRequestController> *a0) {
  return new QWebEngineFileSystemAccessRequest(*a0);
}
