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

//  DomLayoutItem::DomLayoutItem()
extern "C" Q_DECL_EXPORT
DomLayoutItem *ritual_ZN13DomLayoutItemC1Ev() {
  return new DomLayoutItem();
}

//  DomLayoutItem::~DomLayoutItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomLayoutItemD1Ev(DomLayoutItem *self) {
  delete self;
}

//  void DomLayoutItem::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomLayoutItem4readER16QXmlStreamReader(
    DomLayoutItem *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomLayoutItem::write(QXmlStreamWriter &writer, const QString
//      &tagName) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13DomLayoutItem5writeER16QXmlStreamWriterRK7QString(
    const DomLayoutItem *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  bool DomLayoutItem::hasAttributeRow() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13DomLayoutItem15hasAttributeRowEv(
    const DomLayoutItem *self) {
  return self->hasAttributeRow();
}

//  int DomLayoutItem::attributeRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13DomLayoutItem12attributeRowEv(const DomLayoutItem *self) {
  return self->attributeRow();
}

//  void DomLayoutItem::setAttributeRow(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomLayoutItem15setAttributeRowEi(
    DomLayoutItem *self,
    int a) {
  self->setAttributeRow(a);
}

//  void DomLayoutItem::clearAttributeRow()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomLayoutItem17clearAttributeRowEv(DomLayoutItem *self) {
  self->clearAttributeRow();
}

//  bool DomLayoutItem::hasAttributeColumn() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13DomLayoutItem18hasAttributeColumnEv(
    const DomLayoutItem *self) {
  return self->hasAttributeColumn();
}

//  int DomLayoutItem::attributeColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13DomLayoutItem15attributeColumnEv(const DomLayoutItem *self) {
  return self->attributeColumn();
}

//  void DomLayoutItem::setAttributeColumn(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomLayoutItem18setAttributeColumnEi(
    DomLayoutItem *self,
    int a) {
  self->setAttributeColumn(a);
}

//  void DomLayoutItem::clearAttributeColumn()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomLayoutItem20clearAttributeColumnEv(DomLayoutItem *self) {
  self->clearAttributeColumn();
}

//  bool DomLayoutItem::hasAttributeRowSpan() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13DomLayoutItem19hasAttributeRowSpanEv(
    const DomLayoutItem *self) {
  return self->hasAttributeRowSpan();
}

//  int DomLayoutItem::attributeRowSpan() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13DomLayoutItem16attributeRowSpanEv(
    const DomLayoutItem *self) {
  return self->attributeRowSpan();
}

//  void DomLayoutItem::setAttributeRowSpan(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomLayoutItem19setAttributeRowSpanEi(
    DomLayoutItem *self,
    int a) {
  self->setAttributeRowSpan(a);
}

//  void DomLayoutItem::clearAttributeRowSpan()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomLayoutItem21clearAttributeRowSpanEv(DomLayoutItem *self) {
  self->clearAttributeRowSpan();
}

//  bool DomLayoutItem::hasAttributeColSpan() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13DomLayoutItem19hasAttributeColSpanEv(
    const DomLayoutItem *self) {
  return self->hasAttributeColSpan();
}

//  int DomLayoutItem::attributeColSpan() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13DomLayoutItem16attributeColSpanEv(
    const DomLayoutItem *self) {
  return self->attributeColSpan();
}

//  void DomLayoutItem::setAttributeColSpan(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomLayoutItem19setAttributeColSpanEi(
    DomLayoutItem *self,
    int a) {
  self->setAttributeColSpan(a);
}

//  void DomLayoutItem::clearAttributeColSpan()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomLayoutItem21clearAttributeColSpanEv(DomLayoutItem *self) {
  self->clearAttributeColSpan();
}

//  bool DomLayoutItem::hasAttributeAlignment() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13DomLayoutItem21hasAttributeAlignmentEv(
    const DomLayoutItem *self) {
  return self->hasAttributeAlignment();
}

//  QString DomLayoutItem::attributeAlignment() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13DomLayoutItem18attributeAlignmentEv(
    const DomLayoutItem *self) {
  return new QString(self->attributeAlignment());
}

//  void DomLayoutItem::setAttributeAlignment(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomLayoutItem21setAttributeAlignmentERK7QString(
    DomLayoutItem *self,
    const QString *a) {
  self->setAttributeAlignment(*a);
}

//  void DomLayoutItem::clearAttributeAlignment()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomLayoutItem23clearAttributeAlignmentEv(
    DomLayoutItem *self) {
  self->clearAttributeAlignment();
}

//  Kind DomLayoutItem::kind() const
extern "C" Q_DECL_EXPORT
DomLayoutItem::Kind ritual_ZNK13DomLayoutItem4kindEv(
    const DomLayoutItem *self) {
  return self->kind();
}

//  DomWidget *DomLayoutItem::elementWidget() const
extern "C" Q_DECL_EXPORT
DomWidget *ritual_ZNK13DomLayoutItem13elementWidgetEv(
    const DomLayoutItem *self) {
  return self->elementWidget();
}

//  DomWidget *DomLayoutItem::takeElementWidget()
extern "C" Q_DECL_EXPORT
DomWidget *ritual_ZN13DomLayoutItem17takeElementWidgetEv(
    DomLayoutItem *self) {
  return self->takeElementWidget();
}

//  void DomLayoutItem::setElementWidget(DomWidget *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomLayoutItem16setElementWidgetEP9DomWidget(
    DomLayoutItem *self,
    DomWidget *a) {
  self->setElementWidget(a);
}

//  DomLayout *DomLayoutItem::elementLayout() const
extern "C" Q_DECL_EXPORT
DomLayout *ritual_ZNK13DomLayoutItem13elementLayoutEv(
    const DomLayoutItem *self) {
  return self->elementLayout();
}

//  DomLayout *DomLayoutItem::takeElementLayout()
extern "C" Q_DECL_EXPORT
DomLayout *ritual_ZN13DomLayoutItem17takeElementLayoutEv(
    DomLayoutItem *self) {
  return self->takeElementLayout();
}

//  void DomLayoutItem::setElementLayout(DomLayout *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomLayoutItem16setElementLayoutEP9DomLayout(
    DomLayoutItem *self,
    DomLayout *a) {
  self->setElementLayout(a);
}

//  DomSpacer *DomLayoutItem::elementSpacer() const
extern "C" Q_DECL_EXPORT
DomSpacer *ritual_ZNK13DomLayoutItem13elementSpacerEv(
    const DomLayoutItem *self) {
  return self->elementSpacer();
}

//  DomSpacer *DomLayoutItem::takeElementSpacer()
extern "C" Q_DECL_EXPORT
DomSpacer *ritual_ZN13DomLayoutItem17takeElementSpacerEv(
    DomLayoutItem *self) {
  return self->takeElementSpacer();
}

//  void DomLayoutItem::setElementSpacer(DomSpacer *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomLayoutItem16setElementSpacerEP9DomSpacer(
    DomLayoutItem *self,
    DomSpacer *a) {
  self->setElementSpacer(a);
}

//  void DomLayoutItem::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomLayoutItem5clearEv(DomLayoutItem *self) {
  self->clear();
}

//  QList<DomLayoutItem *>::QList()
extern "C" Q_DECL_EXPORT
QList<DomLayoutItem *> *ritual_list_make_DomLayoutItem_ptr() {
  return new QList<DomLayoutItem *>();
}

//  void QList<DomLayoutItem *>::append(const DomLayoutItem * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_DomLayoutItem_ptr(
    QList<DomLayoutItem *> *self,
    DomLayoutItem *element) {
  self->append(element);
}

//  qsizetype QList<DomLayoutItem *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_DomLayoutItem_ptr(
    const QList<DomLayoutItem *> *self) {
  return self->size();
}

//  const DomLayoutItem * &QList<DomLayoutItem *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
DomLayoutItem *ritual_list_at_DomLayoutItem_ptr(
    const QList<DomLayoutItem *> *self,
    long long index) {
  return self->at(index);
}

//  QList<DomLayoutItem *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_DomLayoutItem_ptr(QList<DomLayoutItem *> *self) {
  delete self;
}
