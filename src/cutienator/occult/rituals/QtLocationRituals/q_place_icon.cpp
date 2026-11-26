//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplaceicon.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qplaceicon.h>
#include <QtCore/qsize.h>
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QPlaceIcon::QPlaceIcon()
extern "C" Q_DECL_EXPORT
QPlaceIcon *ritual_ZN10QPlaceIconC1Ev() {
  return new QPlaceIcon();
}

//  QPlaceIcon::QPlaceIcon(const QPlaceIcon &other)
extern "C" Q_DECL_EXPORT
QPlaceIcon *ritual_ZN10QPlaceIconC1ERKS_(const QPlaceIcon *other) {
  return new QPlaceIcon(*other);
}

//  QPlaceIcon::QPlaceIcon(QPlaceIcon &&other)
extern "C" Q_DECL_EXPORT
QPlaceIcon *ritual_ZN10QPlaceIconC1EOS_(QPlaceIcon *other) {
  return new QPlaceIcon(std::move(*other));
}

//  QPlaceIcon::~QPlaceIcon()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPlaceIconD1Ev(QPlaceIcon *self) {
  delete self;
}

//  QPlaceIcon &QPlaceIcon::operator=(const QPlaceIcon &other)
extern "C" Q_DECL_EXPORT
QPlaceIcon *ritual_ZN10QPlaceIconaSERKS_(
    QPlaceIcon *self,
    const QPlaceIcon *other) {
  return &(self->operator=(*other));
}

//  QPlaceIcon &QPlaceIcon::operator=(QPlaceIcon &&other)
extern "C" Q_DECL_EXPORT
QPlaceIcon *ritual_ZN10QPlaceIconaSEOS_(
    QPlaceIcon *self,
    QPlaceIcon *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QPlaceIcon::swap(QPlaceIcon &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPlaceIcon4swapERS_(QPlaceIcon *self, QPlaceIcon *other) {
  self->swap(*other);
}

//  bool operator==(const QPlaceIcon &lhs, const QPlaceIcon &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK10QPlaceIconS1_(
    const QPlaceIcon *lhs,
    const QPlaceIcon *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QPlaceIcon &lhs, const QPlaceIcon &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK10QPlaceIconS1_(
    const QPlaceIcon *lhs,
    const QPlaceIcon *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QUrl QPlaceIcon::url(const QSize &size) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10QPlaceIcon3urlERK5QSize(
    const QPlaceIcon *self,
    const QSize *size) {
  return new QUrl(self->url(*size));
}

//  QPlaceManager *QPlaceIcon::manager() const
extern "C" Q_DECL_EXPORT
QPlaceManager *ritual_ZNK10QPlaceIcon7managerEv(const QPlaceIcon *self) {
  return self->manager();
}

//  void QPlaceIcon::setManager(QPlaceManager *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPlaceIcon10setManagerEP13QPlaceManager(
    QPlaceIcon *self,
    QPlaceManager *manager) {
  self->setManager(manager);
}

//  QVariantMap QPlaceIcon::parameters() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK10QPlaceIcon10parametersEv(
    const QPlaceIcon *self) {
  return new QMap<QString, QVariant>(self->parameters());
}

//  void QPlaceIcon::setParameters(const QVariantMap &parameters)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPlaceIcon13setParametersERK4QMapI7QString8QVariantE(
    QPlaceIcon *self,
    const QMap<QString, QVariant> *parameters) {
  self->setParameters(*parameters);
}

//  bool QPlaceIcon::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QPlaceIcon7isEmptyEv(const QPlaceIcon *self) {
  return self->isEmpty();
}

//  bool QPlaceIcon::isEqual(const QPlaceIcon &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QPlaceIcon7isEqualERKS_(
    const QPlaceIcon *self,
    const QPlaceIcon *other) {
  return self->isEqual(*other);
}
