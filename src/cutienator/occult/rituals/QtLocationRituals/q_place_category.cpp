//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplacecategory.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qplacecategory.h>
#include <QtCore/qstring.h>
#include <QtLocation/qplaceicon.h>
#include <QtCore/qlist.h>

//  QPlaceCategory::QPlaceCategory()
extern "C" Q_DECL_EXPORT
QPlaceCategory *ritual_ZN14QPlaceCategoryC1Ev() {
  return new QPlaceCategory();
}

//  QPlaceCategory::QPlaceCategory(const QPlaceCategory &other)
extern "C" Q_DECL_EXPORT
QPlaceCategory *ritual_ZN14QPlaceCategoryC1ERKS_(
    const QPlaceCategory *other) {
  return new QPlaceCategory(*other);
}

//  QPlaceCategory::QPlaceCategory(QPlaceCategory &&other)
extern "C" Q_DECL_EXPORT
QPlaceCategory *ritual_ZN14QPlaceCategoryC1EOS_(QPlaceCategory *other) {
  return new QPlaceCategory(std::move(*other));
}

//  QPlaceCategory::~QPlaceCategory()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlaceCategoryD1Ev(QPlaceCategory *self) {
  delete self;
}

//  QPlaceCategory &QPlaceCategory::operator=(const QPlaceCategory &other)
extern "C" Q_DECL_EXPORT
QPlaceCategory *ritual_ZN14QPlaceCategoryaSERKS_(
    QPlaceCategory *self,
    const QPlaceCategory *other) {
  return &(self->operator=(*other));
}

//  QPlaceCategory &QPlaceCategory::operator=(QPlaceCategory &&other)
extern "C" Q_DECL_EXPORT
QPlaceCategory *ritual_ZN14QPlaceCategoryaSEOS_(
    QPlaceCategory *self,
    QPlaceCategory *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QPlaceCategory::swap(QPlaceCategory &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlaceCategory4swapERS_(
    QPlaceCategory *self,
    QPlaceCategory *other) {
  self->swap(*other);
}

//  bool operator==(const QPlaceCategory &lhs, const QPlaceCategory &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QPlaceCategoryS1_(
    const QPlaceCategory *lhs,
    const QPlaceCategory *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QPlaceCategory &lhs, const QPlaceCategory &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QPlaceCategoryS1_(
    const QPlaceCategory *lhs,
    const QPlaceCategory *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QString QPlaceCategory::categoryId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QPlaceCategory10categoryIdEv(
    const QPlaceCategory *self) {
  return new QString(self->categoryId());
}

//  void QPlaceCategory::setCategoryId(const QString &identifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlaceCategory13setCategoryIdERK7QString(
    QPlaceCategory *self,
    const QString *identifier) {
  self->setCategoryId(*identifier);
}

//  QString QPlaceCategory::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QPlaceCategory4nameEv(const QPlaceCategory *self) {
  return new QString(self->name());
}

//  void QPlaceCategory::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlaceCategory7setNameERK7QString(
    QPlaceCategory *self,
    const QString *name) {
  self->setName(*name);
}

//  QLocation::Visibility QPlaceCategory::visibility() const
extern "C" Q_DECL_EXPORT
QLocation::Visibility ritual_ZNK14QPlaceCategory10visibilityEv(
    const QPlaceCategory *self) {
  return self->visibility();
}

//  void QPlaceCategory::setVisibility(QLocation::Visibility visibility)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlaceCategory13setVisibilityEN9QLocation10VisibilityE(
    QPlaceCategory *self,
    QLocation::Visibility visibility) {
  self->setVisibility(visibility);
}

//  QPlaceIcon QPlaceCategory::icon() const
extern "C" Q_DECL_EXPORT
QPlaceIcon *ritual_ZNK14QPlaceCategory4iconEv(const QPlaceCategory *self) {
  return new QPlaceIcon(self->icon());
}

//  void QPlaceCategory::setIcon(const QPlaceIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlaceCategory7setIconERK10QPlaceIcon(
    QPlaceCategory *self,
    const QPlaceIcon *icon) {
  self->setIcon(*icon);
}

//  bool QPlaceCategory::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QPlaceCategory7isEmptyEv(const QPlaceCategory *self) {
  return self->isEmpty();
}

//  bool QPlaceCategory::isEqual(const QPlaceCategory &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QPlaceCategory7isEqualERKS_(
    const QPlaceCategory *self,
    const QPlaceCategory *other) {
  return self->isEqual(*other);
}

//  QList<QPlaceCategory>::QList()
extern "C" Q_DECL_EXPORT
QList<QPlaceCategory> *ritual_list_make_QPlaceCategory() {
  return new QList<QPlaceCategory>();
}

//  void QList<QPlaceCategory>::append(const QPlaceCategory &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QPlaceCategory(
    QList<QPlaceCategory> *self,
    const QPlaceCategory *element) {
  self->append(*element);
}

//  qsizetype QList<QPlaceCategory>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QPlaceCategory(
    const QList<QPlaceCategory> *self) {
  return self->size();
}

//  const QPlaceCategory &QList<QPlaceCategory>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QPlaceCategory *ritual_list_at_QPlaceCategory(
    const QList<QPlaceCategory> *self,
    long long index) {
  return new QPlaceCategory(self->at(index));
}

//  QList<QPlaceCategory>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QPlaceCategory(QList<QPlaceCategory> *self) {
  delete self;
}
