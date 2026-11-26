//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplaceuser.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qplaceuser.h>
#include <QtCore/qstring.h>

//  QPlaceUser::QPlaceUser()
extern "C" Q_DECL_EXPORT
QPlaceUser *ritual_ZN10QPlaceUserC1Ev() {
  return new QPlaceUser();
}

//  QPlaceUser::QPlaceUser(const QPlaceUser &other)
extern "C" Q_DECL_EXPORT
QPlaceUser *ritual_ZN10QPlaceUserC1ERKS_(const QPlaceUser *other) {
  return new QPlaceUser(*other);
}

//  QPlaceUser::QPlaceUser(QPlaceUser &&other)
extern "C" Q_DECL_EXPORT
QPlaceUser *ritual_ZN10QPlaceUserC1EOS_(QPlaceUser *other) {
  return new QPlaceUser(std::move(*other));
}

//  QPlaceUser::~QPlaceUser()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPlaceUserD1Ev(QPlaceUser *self) {
  delete self;
}

//  QPlaceUser &QPlaceUser::operator=(const QPlaceUser &other)
extern "C" Q_DECL_EXPORT
QPlaceUser *ritual_ZN10QPlaceUseraSERKS_(
    QPlaceUser *self,
    const QPlaceUser *other) {
  return &(self->operator=(*other));
}

//  QPlaceUser &QPlaceUser::operator=(QPlaceUser &&other)
extern "C" Q_DECL_EXPORT
QPlaceUser *ritual_ZN10QPlaceUseraSEOS_(
    QPlaceUser *self,
    QPlaceUser *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QPlaceUser::swap(QPlaceUser &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPlaceUser4swapERS_(QPlaceUser *self, QPlaceUser *other) {
  self->swap(*other);
}

//  bool operator==(const QPlaceUser &lhs, const QPlaceUser &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK10QPlaceUserS1_(
    const QPlaceUser *lhs,
    const QPlaceUser *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QPlaceUser &lhs, const QPlaceUser &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK10QPlaceUserS1_(
    const QPlaceUser *lhs,
    const QPlaceUser *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QString QPlaceUser::userId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QPlaceUser6userIdEv(const QPlaceUser *self) {
  return new QString(self->userId());
}

//  void QPlaceUser::setUserId(const QString &identifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPlaceUser9setUserIdERK7QString(
    QPlaceUser *self,
    const QString *identifier) {
  self->setUserId(*identifier);
}

//  QString QPlaceUser::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QPlaceUser4nameEv(const QPlaceUser *self) {
  return new QString(self->name());
}

//  void QPlaceUser::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QPlaceUser7setNameERK7QString(
    QPlaceUser *self,
    const QString *name) {
  self->setName(*name);
}

//  bool QPlaceUser::isEqual(const QPlaceUser &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QPlaceUser7isEqualERKS_(
    const QPlaceUser *self,
    const QPlaceUser *other) {
  return self->isEqual(*other);
}
