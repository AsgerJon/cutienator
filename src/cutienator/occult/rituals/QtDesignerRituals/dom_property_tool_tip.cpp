//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  DomPropertyToolTip::DomPropertyToolTip()
extern "C" Q_DECL_EXPORT
DomPropertyToolTip *ritual_ZN18DomPropertyToolTipC1Ev() {
  return new DomPropertyToolTip();
}

//  DomPropertyToolTip::~DomPropertyToolTip()
extern "C" Q_DECL_EXPORT
void ritual_ZN18DomPropertyToolTipD1Ev(DomPropertyToolTip *self) {
  delete self;
}

//  bool DomPropertyToolTip::hasAttributeName() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18DomPropertyToolTip16hasAttributeNameEv(
    const DomPropertyToolTip *self) {
  return self->hasAttributeName();
}

//  QString DomPropertyToolTip::attributeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18DomPropertyToolTip13attributeNameEv(
    const DomPropertyToolTip *self) {
  return new QString(self->attributeName());
}

//  void DomPropertyToolTip::setAttributeName(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN18DomPropertyToolTip16setAttributeNameERK7QString(
    DomPropertyToolTip *self,
    const QString *a) {
  self->setAttributeName(*a);
}

//  void DomPropertyToolTip::clearAttributeName()
extern "C" Q_DECL_EXPORT
void ritual_ZN18DomPropertyToolTip18clearAttributeNameEv(
    DomPropertyToolTip *self) {
  self->clearAttributeName();
}

//  QList<DomPropertyToolTip *>::QList()
extern "C" Q_DECL_EXPORT
QList<DomPropertyToolTip *> *ritual_list_make_DomPropertyToolTip_ptr() {
  return new QList<DomPropertyToolTip *>();
}

//  void QList<DomPropertyToolTip *>::append(const DomPropertyToolTip *
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_DomPropertyToolTip_ptr(
    QList<DomPropertyToolTip *> *self,
    DomPropertyToolTip *element) {
  self->append(element);
}

//  qsizetype QList<DomPropertyToolTip *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_DomPropertyToolTip_ptr(
    const QList<DomPropertyToolTip *> *self) {
  return self->size();
}

//  const DomPropertyToolTip * &QList<DomPropertyToolTip *>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
DomPropertyToolTip *ritual_list_at_DomPropertyToolTip_ptr(
    const QList<DomPropertyToolTip *> *self,
    long long index) {
  return self->at(index);
}

//  QList<DomPropertyToolTip *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_DomPropertyToolTip_ptr(
    QList<DomPropertyToolTip *> *self) {
  delete self;
}
