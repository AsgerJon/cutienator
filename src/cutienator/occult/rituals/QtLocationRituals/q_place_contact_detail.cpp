//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplacecontactdetail.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qplacecontactdetail.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QPlaceContactDetail::QPlaceContactDetail()
extern "C" Q_DECL_EXPORT
QPlaceContactDetail *ritual_ZN19QPlaceContactDetailC1Ev() {
  return new QPlaceContactDetail();
}

//  QPlaceContactDetail::QPlaceContactDetail(const QPlaceContactDetail
//      &other)
extern "C" Q_DECL_EXPORT
QPlaceContactDetail *ritual_ZN19QPlaceContactDetailC1ERKS_(
    const QPlaceContactDetail *other) {
  return new QPlaceContactDetail(*other);
}

//  QPlaceContactDetail::QPlaceContactDetail(QPlaceContactDetail &&other)
extern "C" Q_DECL_EXPORT
QPlaceContactDetail *ritual_ZN19QPlaceContactDetailC1EOS_(
    QPlaceContactDetail *other) {
  return new QPlaceContactDetail(std::move(*other));
}

//  QPlaceContactDetail::~QPlaceContactDetail()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlaceContactDetailD1Ev(QPlaceContactDetail *self) {
  delete self;
}

//  QPlaceContactDetail &QPlaceContactDetail::operator=(const
//      QPlaceContactDetail &other)
extern "C" Q_DECL_EXPORT
QPlaceContactDetail *ritual_ZN19QPlaceContactDetailaSERKS_(
    QPlaceContactDetail *self,
    const QPlaceContactDetail *other) {
  return &(self->operator=(*other));
}

//  QPlaceContactDetail &QPlaceContactDetail::operator=(QPlaceContactDetail
//      &&other)
extern "C" Q_DECL_EXPORT
QPlaceContactDetail *ritual_ZN19QPlaceContactDetailaSEOS_(
    QPlaceContactDetail *self,
    QPlaceContactDetail *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QPlaceContactDetail::swap(QPlaceContactDetail &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlaceContactDetail4swapERS_(
    QPlaceContactDetail *self,
    QPlaceContactDetail *other) {
  self->swap(*other);
}

//  bool operator==(const QPlaceContactDetail &lhs, const QPlaceContactDetail
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK19QPlaceContactDetailS1_(
    const QPlaceContactDetail *lhs,
    const QPlaceContactDetail *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QPlaceContactDetail &lhs, const QPlaceContactDetail
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK19QPlaceContactDetailS1_(
    const QPlaceContactDetail *lhs,
    const QPlaceContactDetail *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QString QPlaceContactDetail::label() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QPlaceContactDetail5labelEv(
    const QPlaceContactDetail *self) {
  return new QString(self->label());
}

//  void QPlaceContactDetail::setLabel(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlaceContactDetail8setLabelERK7QString(
    QPlaceContactDetail *self,
    const QString *label) {
  self->setLabel(*label);
}

//  QString QPlaceContactDetail::value() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QPlaceContactDetail5valueEv(
    const QPlaceContactDetail *self) {
  return new QString(self->value());
}

//  void QPlaceContactDetail::setValue(const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlaceContactDetail8setValueERK7QString(
    QPlaceContactDetail *self,
    const QString *value) {
  self->setValue(*value);
}

//  void QPlaceContactDetail::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlaceContactDetail5clearEv(QPlaceContactDetail *self) {
  self->clear();
}

//  bool QPlaceContactDetail::isEqual(const QPlaceContactDetail &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QPlaceContactDetail7isEqualERKS_(
    const QPlaceContactDetail *self,
    const QPlaceContactDetail *other) {
  return self->isEqual(*other);
}

//  QList<QPlaceContactDetail>::QList()
extern "C" Q_DECL_EXPORT
QList<QPlaceContactDetail> *ritual_list_make_QPlaceContactDetail() {
  return new QList<QPlaceContactDetail>();
}

//  void QList<QPlaceContactDetail>::append(const QPlaceContactDetail &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QPlaceContactDetail(
    QList<QPlaceContactDetail> *self,
    const QPlaceContactDetail *element) {
  self->append(*element);
}

//  qsizetype QList<QPlaceContactDetail>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QPlaceContactDetail(
    const QList<QPlaceContactDetail> *self) {
  return self->size();
}

//  const QPlaceContactDetail &QList<QPlaceContactDetail>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QPlaceContactDetail *ritual_list_at_QPlaceContactDetail(
    const QList<QPlaceContactDetail> *self,
    long long index) {
  return new QPlaceContactDetail(self->at(index));
}

//  QList<QPlaceContactDetail>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QPlaceContactDetail(QList<QPlaceContactDetail> *self) {
  delete self;
}
