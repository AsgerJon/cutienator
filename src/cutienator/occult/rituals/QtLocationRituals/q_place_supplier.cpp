//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplacesupplier.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qplacesupplier.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtLocation/qplaceicon.h>

//  QPlaceSupplier::QPlaceSupplier()
extern "C" Q_DECL_EXPORT
QPlaceSupplier *ritual_ZN14QPlaceSupplierC1Ev() {
  return new QPlaceSupplier();
}

//  QPlaceSupplier::QPlaceSupplier(const QPlaceSupplier &other)
extern "C" Q_DECL_EXPORT
QPlaceSupplier *ritual_ZN14QPlaceSupplierC1ERKS_(
    const QPlaceSupplier *other) {
  return new QPlaceSupplier(*other);
}

//  QPlaceSupplier::~QPlaceSupplier()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlaceSupplierD1Ev(QPlaceSupplier *self) {
  delete self;
}

//  bool operator==(const QPlaceSupplier &lhs, const QPlaceSupplier &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QPlaceSupplierS1_(
    const QPlaceSupplier *lhs,
    const QPlaceSupplier *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QPlaceSupplier &lhs, const QPlaceSupplier &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QPlaceSupplierS1_(
    const QPlaceSupplier *lhs,
    const QPlaceSupplier *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QString QPlaceSupplier::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QPlaceSupplier4nameEv(const QPlaceSupplier *self) {
  return new QString(self->name());
}

//  void QPlaceSupplier::setName(const QString &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlaceSupplier7setNameERK7QString(
    QPlaceSupplier *self,
    const QString *data) {
  self->setName(*data);
}

//  QString QPlaceSupplier::supplierId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QPlaceSupplier10supplierIdEv(
    const QPlaceSupplier *self) {
  return new QString(self->supplierId());
}

//  void QPlaceSupplier::setSupplierId(const QString &identifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlaceSupplier13setSupplierIdERK7QString(
    QPlaceSupplier *self,
    const QString *identifier) {
  self->setSupplierId(*identifier);
}

//  QUrl QPlaceSupplier::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK14QPlaceSupplier3urlEv(const QPlaceSupplier *self) {
  return new QUrl(self->url());
}

//  void QPlaceSupplier::setUrl(const QUrl &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlaceSupplier6setUrlERK4QUrl(
    QPlaceSupplier *self,
    const QUrl *data) {
  self->setUrl(*data);
}

//  QPlaceIcon QPlaceSupplier::icon() const
extern "C" Q_DECL_EXPORT
QPlaceIcon *ritual_ZNK14QPlaceSupplier4iconEv(const QPlaceSupplier *self) {
  return new QPlaceIcon(self->icon());
}

//  void QPlaceSupplier::setIcon(const QPlaceIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlaceSupplier7setIconERK10QPlaceIcon(
    QPlaceSupplier *self,
    const QPlaceIcon *icon) {
  self->setIcon(*icon);
}

//  bool QPlaceSupplier::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QPlaceSupplier7isEmptyEv(const QPlaceSupplier *self) {
  return self->isEmpty();
}

//  bool QPlaceSupplier::isEqual(const QPlaceSupplier &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QPlaceSupplier7isEqualERKS_(
    const QPlaceSupplier *self,
    const QPlaceSupplier *other) {
  return self->isEqual(*other);
}
