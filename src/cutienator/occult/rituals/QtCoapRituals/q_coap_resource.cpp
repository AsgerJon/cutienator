//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/qcoapresource.h, Qt 6.12.0. Changes made here are lost.
#include <QtCoap/qcoapresource.h>
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QCoapResource::QCoapResource()
extern "C" Q_DECL_EXPORT
QCoapResource *ritual_ZN13QCoapResourceC1Ev() {
  return new QCoapResource();
}

//  QCoapResource::QCoapResource(const QCoapResource &other)
extern "C" Q_DECL_EXPORT
QCoapResource *ritual_ZN13QCoapResourceC1ERKS_(const QCoapResource *other) {
  return new QCoapResource(*other);
}

//  QCoapResource::~QCoapResource()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCoapResourceD1Ev(QCoapResource *self) {
  delete self;
}

//  QCoapResource &QCoapResource::operator=(const QCoapResource &other)
extern "C" Q_DECL_EXPORT
QCoapResource *ritual_ZN13QCoapResourceaSERKS_(
    QCoapResource *self,
    const QCoapResource *other) {
  return &(self->operator=(*other));
}

//  void QCoapResource::swap(QCoapResource &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCoapResource4swapERS_(
    QCoapResource *self,
    QCoapResource *other) {
  self->swap(*other);
}

//  QHostAddress QCoapResource::host() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK13QCoapResource4hostEv(const QCoapResource *self) {
  return new QHostAddress(self->host());
}

//  QString QCoapResource::path() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QCoapResource4pathEv(const QCoapResource *self) {
  return new QString(self->path());
}

//  QString QCoapResource::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QCoapResource5titleEv(const QCoapResource *self) {
  return new QString(self->title());
}

//  bool QCoapResource::observable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCoapResource10observableEv(const QCoapResource *self) {
  return self->observable();
}

//  QString QCoapResource::resourceType() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QCoapResource12resourceTypeEv(
    const QCoapResource *self) {
  return new QString(self->resourceType());
}

//  QString QCoapResource::interface() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QCoapResource9interfaceEv(const QCoapResource *self) {
  return new QString(self->interface());
}

//  int QCoapResource::maximumSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QCoapResource11maximumSizeEv(const QCoapResource *self) {
  return self->maximumSize();
}

//  uint QCoapResource::contentFormat() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK13QCoapResource13contentFormatEv(const QCoapResource *self) {
  return self->contentFormat();
}

//  void QCoapResource::setHost(const QHostAddress &host)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCoapResource7setHostERK12QHostAddress(
    QCoapResource *self,
    const QHostAddress *host) {
  self->setHost(*host);
}

//  void QCoapResource::setPath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCoapResource7setPathERK7QString(
    QCoapResource *self,
    const QString *path) {
  self->setPath(*path);
}

//  void QCoapResource::setTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCoapResource8setTitleERK7QString(
    QCoapResource *self,
    const QString *title) {
  self->setTitle(*title);
}

//  void QCoapResource::setObservable(bool observable)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCoapResource13setObservableEb(
    QCoapResource *self,
    bool observable) {
  self->setObservable(observable);
}

//  void QCoapResource::setResourceType(const QString &resourceType)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCoapResource15setResourceTypeERK7QString(
    QCoapResource *self,
    const QString *resourceType) {
  self->setResourceType(*resourceType);
}

//  void QCoapResource::setInterface(const QString &interface)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCoapResource12setInterfaceERK7QString(
    QCoapResource *self,
    const QString *interface) {
  self->setInterface(*interface);
}

//  void QCoapResource::setMaximumSize(int maximumSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCoapResource14setMaximumSizeEi(
    QCoapResource *self,
    int maximumSize) {
  self->setMaximumSize(maximumSize);
}

//  void QCoapResource::setContentFormat(uint contentFormat)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCoapResource16setContentFormatEj(
    QCoapResource *self,
    uint contentFormat) {
  self->setContentFormat(contentFormat);
}

//  QList<QCoapResource>::QList()
extern "C" Q_DECL_EXPORT
QList<QCoapResource> *ritual_list_make_QCoapResource() {
  return new QList<QCoapResource>();
}

//  void QList<QCoapResource>::append(const QCoapResource &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QCoapResource(
    QList<QCoapResource> *self,
    const QCoapResource *element) {
  self->append(*element);
}

//  qsizetype QList<QCoapResource>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QCoapResource(const QList<QCoapResource> *self) {
  return self->size();
}

//  const QCoapResource &QList<QCoapResource>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QCoapResource *ritual_list_at_QCoapResource(
    const QList<QCoapResource> *self,
    long long index) {
  return new QCoapResource(self->at(index));
}

//  QList<QCoapResource>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QCoapResource(QList<QCoapResource> *self) {
  delete self;
}
