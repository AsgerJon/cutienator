//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebenginepermission.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWebEngineCore/qwebenginepermission.h>
#include <QtCore/qurl.h>
#include <QtCore/qlist.h>

//  QWebEnginePermission::QWebEnginePermission()
extern "C" Q_DECL_EXPORT
QWebEnginePermission *ritual_ZN20QWebEnginePermissionC1Ev() {
  return new QWebEnginePermission();
}

//  QWebEnginePermission::QWebEnginePermission(const QWebEnginePermission
//      &other)
extern "C" Q_DECL_EXPORT
QWebEnginePermission *ritual_ZN20QWebEnginePermissionC1ERKS_(
    const QWebEnginePermission *other) {
  return new QWebEnginePermission(*other);
}

//  QWebEnginePermission::QWebEnginePermission(QWebEnginePermission &&other)
extern "C" Q_DECL_EXPORT
QWebEnginePermission *ritual_ZN20QWebEnginePermissionC1EOS_(
    QWebEnginePermission *other) {
  return new QWebEnginePermission(std::move(*other));
}

//  QWebEnginePermission::~QWebEnginePermission()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWebEnginePermissionD1Ev(QWebEnginePermission *self) {
  delete self;
}

//  QWebEnginePermission &QWebEnginePermission::operator=(const
//      QWebEnginePermission &other)
extern "C" Q_DECL_EXPORT
QWebEnginePermission *ritual_ZN20QWebEnginePermissionaSERKS_(
    QWebEnginePermission *self,
    const QWebEnginePermission *other) {
  return &(self->operator=(*other));
}

//  QWebEnginePermission
//      &QWebEnginePermission::operator=(QWebEnginePermission &&other)
extern "C" Q_DECL_EXPORT
QWebEnginePermission *ritual_ZN20QWebEnginePermissionaSEOS_(
    QWebEnginePermission *self,
    QWebEnginePermission *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QWebEnginePermission::swap(QWebEnginePermission &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWebEnginePermission4swapERS_(
    QWebEnginePermission *self,
    QWebEnginePermission *other) {
  self->swap(*other);
}

//  QUrl QWebEnginePermission::origin() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK20QWebEnginePermission6originEv(
    const QWebEnginePermission *self) {
  return new QUrl(self->origin());
}

//  PermissionType QWebEnginePermission::permissionType() const
extern "C" Q_DECL_EXPORT
QWebEnginePermission::PermissionType ritual_ZNK20QWebEnginePermission14permissionTypeEv(
    const QWebEnginePermission *self) {
  return self->permissionType();
}

//  State QWebEnginePermission::state() const
extern "C" Q_DECL_EXPORT
QWebEnginePermission::State ritual_ZNK20QWebEnginePermission5stateEv(
    const QWebEnginePermission *self) {
  return self->state();
}

//  bool QWebEnginePermission::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QWebEnginePermission7isValidEv(
    const QWebEnginePermission *self) {
  return self->isValid();
}

//  void QWebEnginePermission::grant() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QWebEnginePermission5grantEv(
    const QWebEnginePermission *self) {
  self->grant();
}

//  void QWebEnginePermission::deny() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QWebEnginePermission4denyEv(
    const QWebEnginePermission *self) {
  self->deny();
}

//  void QWebEnginePermission::reset() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QWebEnginePermission5resetEv(
    const QWebEnginePermission *self) {
  self->reset();
}

//  bool
//      QWebEnginePermission::isPersistent(QWebEnginePermission::PermissionTy
//      pe permissionType)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QWebEnginePermission12isPersistentENS_14PermissionTypeE(
    QWebEnginePermission::PermissionType permissionType) {
  return QWebEnginePermission::isPersistent(permissionType);
}

//  bool operator==(const QWebEnginePermission &lhs, const
//      QWebEnginePermission &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK20QWebEnginePermissionS1_(
    const QWebEnginePermission *lhs,
    const QWebEnginePermission *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QWebEnginePermission &lhs, const
//      QWebEnginePermission &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK20QWebEnginePermissionS1_(
    const QWebEnginePermission *lhs,
    const QWebEnginePermission *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool QWebEnginePermission::equals(const QWebEnginePermission &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QWebEnginePermission6equalsERKS_(
    const QWebEnginePermission *self,
    const QWebEnginePermission *other) {
  return self->equals(*other);
}

//  QWebEnginePermission::QWebEnginePermission(QWebEnginePermissionPrivate
//      *pvt)
extern "C" Q_DECL_EXPORT
QWebEnginePermission *ritual_ZN20QWebEnginePermissionC1EP27QWebEnginePermissionPrivate(
    QWebEnginePermissionPrivate *pvt) {
  return new QWebEnginePermission(pvt);
}

//  QList<QWebEnginePermission>::QList()
extern "C" Q_DECL_EXPORT
QList<QWebEnginePermission> *ritual_list_make_QWebEnginePermission() {
  return new QList<QWebEnginePermission>();
}

//  void QList<QWebEnginePermission>::append(const QWebEnginePermission
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QWebEnginePermission(
    QList<QWebEnginePermission> *self,
    const QWebEnginePermission *element) {
  self->append(*element);
}

//  qsizetype QList<QWebEnginePermission>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QWebEnginePermission(
    const QList<QWebEnginePermission> *self) {
  return self->size();
}

//  const QWebEnginePermission &QList<QWebEnginePermission>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QWebEnginePermission *ritual_list_at_QWebEnginePermission(
    const QList<QWebEnginePermission> *self,
    long long index) {
  return new QWebEnginePermission(self->at(index));
}

//  QList<QWebEnginePermission>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QWebEnginePermission(
    QList<QWebEnginePermission> *self) {
  delete self;
}
