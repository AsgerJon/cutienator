//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebenginedesktopmediarequest.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWebEngineCore/qwebenginedesktopmediarequest.h>
#include <QtCore/qabstractitemmodel.h>

//  QWebEngineDesktopMediaRequest::QWebEngineDesktopMediaRequest()
extern "C" Q_DECL_EXPORT
QWebEngineDesktopMediaRequest *ritual_ZN29QWebEngineDesktopMediaRequestC1Ev() {
  return new QWebEngineDesktopMediaRequest();
}

//  QWebEngineDesktopMediaRequest::~QWebEngineDesktopMediaRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWebEngineDesktopMediaRequestD1Ev(
    QWebEngineDesktopMediaRequest *self) {
  delete self;
}

//  QWebEngineDesktopMediaRequest::QWebEngineDesktopMediaRequest(const
//      QWebEngineDesktopMediaRequest &other)
extern "C" Q_DECL_EXPORT
QWebEngineDesktopMediaRequest *ritual_ZN29QWebEngineDesktopMediaRequestC1ERKS_(
    const QWebEngineDesktopMediaRequest *other) {
  return new QWebEngineDesktopMediaRequest(*other);
}

//  QWebEngineDesktopMediaRequest::QWebEngineDesktopMediaRequest(QWebEngineDe
//      sktopMediaRequest &&other)
extern "C" Q_DECL_EXPORT
QWebEngineDesktopMediaRequest *ritual_ZN29QWebEngineDesktopMediaRequestC1EOS_(
    QWebEngineDesktopMediaRequest *other) {
  return new QWebEngineDesktopMediaRequest(std::move(*other));
}

//  QWebEngineDesktopMediaRequest
//      &QWebEngineDesktopMediaRequest::operator=(const
//      QWebEngineDesktopMediaRequest &other)
extern "C" Q_DECL_EXPORT
QWebEngineDesktopMediaRequest *ritual_ZN29QWebEngineDesktopMediaRequestaSERKS_(
    QWebEngineDesktopMediaRequest *self,
    const QWebEngineDesktopMediaRequest *other) {
  return &(self->operator=(*other));
}

//  QWebEngineDesktopMediaRequest
//      &QWebEngineDesktopMediaRequest::operator=(QWebEngineDesktopMediaReque
//      st &&other)
extern "C" Q_DECL_EXPORT
QWebEngineDesktopMediaRequest *ritual_ZN29QWebEngineDesktopMediaRequestaSEOS_(
    QWebEngineDesktopMediaRequest *self,
    QWebEngineDesktopMediaRequest *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QWebEngineDesktopMediaRequest::swap(QWebEngineDesktopMediaRequest
//      &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWebEngineDesktopMediaRequest4swapERS_(
    QWebEngineDesktopMediaRequest *self,
    QWebEngineDesktopMediaRequest *other) {
  self->swap(*other);
}

//  QAbstractListModel *QWebEngineDesktopMediaRequest::screensModel() const
extern "C" Q_DECL_EXPORT
QAbstractListModel *ritual_ZNK29QWebEngineDesktopMediaRequest12screensModelEv(
    const QWebEngineDesktopMediaRequest *self) {
  return self->screensModel();
}

//  QAbstractListModel *QWebEngineDesktopMediaRequest::windowsModel() const
extern "C" Q_DECL_EXPORT
QAbstractListModel *ritual_ZNK29QWebEngineDesktopMediaRequest12windowsModelEv(
    const QWebEngineDesktopMediaRequest *self) {
  return self->windowsModel();
}

//  void QWebEngineDesktopMediaRequest::selectScreen(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK29QWebEngineDesktopMediaRequest12selectScreenERK11QModelIndex(
    const QWebEngineDesktopMediaRequest *self,
    const QModelIndex *index) {
  self->selectScreen(*index);
}

//  void QWebEngineDesktopMediaRequest::selectWindow(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK29QWebEngineDesktopMediaRequest12selectWindowERK11QModelIndex(
    const QWebEngineDesktopMediaRequest *self,
    const QModelIndex *index) {
  self->selectWindow(*index);
}

//  void QWebEngineDesktopMediaRequest::cancel() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK29QWebEngineDesktopMediaRequest6cancelEv(
    const QWebEngineDesktopMediaRequest *self) {
  self->cancel();
}

//  QWebEngineDesktopMediaRequest::QWebEngineDesktopMediaRequest(QtWebEngineC
//      ore::DesktopMediaController *controller)
extern "C" Q_DECL_EXPORT
QWebEngineDesktopMediaRequest *ritual_ZN29QWebEngineDesktopMediaRequestC1EPN15QtWebEngineCore22DesktopMediaControllerE(
    QtWebEngineCore::DesktopMediaController *controller) {
  return new QWebEngineDesktopMediaRequest(controller);
}
