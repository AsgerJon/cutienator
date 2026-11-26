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

//  DomWidget::DomWidget()
extern "C" Q_DECL_EXPORT
DomWidget *ritual_ZN9DomWidgetC1Ev() {
  return new DomWidget();
}

//  DomWidget::~DomWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomWidgetD1Ev(DomWidget *self) {
  delete self;
}

//  void DomWidget::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomWidget4readER16QXmlStreamReader(
    DomWidget *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomWidget::write(QXmlStreamWriter &writer, const QString &tagName)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9DomWidget5writeER16QXmlStreamWriterRK7QString(
    const DomWidget *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  bool DomWidget::hasAttributeClass() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9DomWidget17hasAttributeClassEv(const DomWidget *self) {
  return self->hasAttributeClass();
}

//  QString DomWidget::attributeClass() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9DomWidget14attributeClassEv(const DomWidget *self) {
  return new QString(self->attributeClass());
}

//  void DomWidget::setAttributeClass(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomWidget17setAttributeClassERK7QString(
    DomWidget *self,
    const QString *a) {
  self->setAttributeClass(*a);
}

//  void DomWidget::clearAttributeClass()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomWidget19clearAttributeClassEv(DomWidget *self) {
  self->clearAttributeClass();
}

//  bool DomWidget::hasAttributeName() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9DomWidget16hasAttributeNameEv(const DomWidget *self) {
  return self->hasAttributeName();
}

//  QString DomWidget::attributeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9DomWidget13attributeNameEv(const DomWidget *self) {
  return new QString(self->attributeName());
}

//  void DomWidget::setAttributeName(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomWidget16setAttributeNameERK7QString(
    DomWidget *self,
    const QString *a) {
  self->setAttributeName(*a);
}

//  void DomWidget::clearAttributeName()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomWidget18clearAttributeNameEv(DomWidget *self) {
  self->clearAttributeName();
}

//  bool DomWidget::hasAttributeNative() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9DomWidget18hasAttributeNativeEv(const DomWidget *self) {
  return self->hasAttributeNative();
}

//  bool DomWidget::attributeNative() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9DomWidget15attributeNativeEv(const DomWidget *self) {
  return self->attributeNative();
}

//  void DomWidget::setAttributeNative(bool a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomWidget18setAttributeNativeEb(DomWidget *self, bool a) {
  self->setAttributeNative(a);
}

//  void DomWidget::clearAttributeNative()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomWidget20clearAttributeNativeEv(DomWidget *self) {
  self->clearAttributeNative();
}

//  QStringList DomWidget::elementClass() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9DomWidget12elementClassEv(const DomWidget *self) {
  return new QList<QString>(self->elementClass());
}

//  void DomWidget::setElementClass(const QStringList &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomWidget15setElementClassERK5QListI7QStringE(
    DomWidget *self,
    const QList<QString> *a) {
  self->setElementClass(*a);
}

//  QList<DomProperty *> DomWidget::elementProperty() const
extern "C" Q_DECL_EXPORT
QList<DomProperty *> *ritual_ZNK9DomWidget15elementPropertyEv(
    const DomWidget *self) {
  return new QList<DomProperty *>(self->elementProperty());
}

//  void DomWidget::setElementProperty(const QList<DomProperty *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomWidget18setElementPropertyERK5QListIP11DomPropertyE(
    DomWidget *self,
    const QList<DomProperty *> *a) {
  self->setElementProperty(*a);
}

//  QList<DomProperty *> DomWidget::elementAttribute() const
extern "C" Q_DECL_EXPORT
QList<DomProperty *> *ritual_ZNK9DomWidget16elementAttributeEv(
    const DomWidget *self) {
  return new QList<DomProperty *>(self->elementAttribute());
}

//  void DomWidget::setElementAttribute(const QList<DomProperty *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomWidget19setElementAttributeERK5QListIP11DomPropertyE(
    DomWidget *self,
    const QList<DomProperty *> *a) {
  self->setElementAttribute(*a);
}

//  QList<DomRow *> DomWidget::elementRow() const
extern "C" Q_DECL_EXPORT
QList<DomRow *> *ritual_ZNK9DomWidget10elementRowEv(const DomWidget *self) {
  return new QList<DomRow *>(self->elementRow());
}

//  void DomWidget::setElementRow(const QList<DomRow *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomWidget13setElementRowERK5QListIP6DomRowE(
    DomWidget *self,
    const QList<DomRow *> *a) {
  self->setElementRow(*a);
}

//  QList<DomColumn *> DomWidget::elementColumn() const
extern "C" Q_DECL_EXPORT
QList<DomColumn *> *ritual_ZNK9DomWidget13elementColumnEv(
    const DomWidget *self) {
  return new QList<DomColumn *>(self->elementColumn());
}

//  void DomWidget::setElementColumn(const QList<DomColumn *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomWidget16setElementColumnERK5QListIP9DomColumnE(
    DomWidget *self,
    const QList<DomColumn *> *a) {
  self->setElementColumn(*a);
}

//  QList<DomItem *> DomWidget::elementItem() const
extern "C" Q_DECL_EXPORT
QList<DomItem *> *ritual_ZNK9DomWidget11elementItemEv(
    const DomWidget *self) {
  return new QList<DomItem *>(self->elementItem());
}

//  void DomWidget::setElementItem(const QList<DomItem *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomWidget14setElementItemERK5QListIP7DomItemE(
    DomWidget *self,
    const QList<DomItem *> *a) {
  self->setElementItem(*a);
}

//  QList<DomLayout *> DomWidget::elementLayout() const
extern "C" Q_DECL_EXPORT
QList<DomLayout *> *ritual_ZNK9DomWidget13elementLayoutEv(
    const DomWidget *self) {
  return new QList<DomLayout *>(self->elementLayout());
}

//  void DomWidget::setElementLayout(const QList<DomLayout *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomWidget16setElementLayoutERK5QListIP9DomLayoutE(
    DomWidget *self,
    const QList<DomLayout *> *a) {
  self->setElementLayout(*a);
}

//  QList<DomWidget *> DomWidget::elementWidget() const
extern "C" Q_DECL_EXPORT
QList<DomWidget *> *ritual_ZNK9DomWidget13elementWidgetEv(
    const DomWidget *self) {
  return new QList<DomWidget *>(self->elementWidget());
}

//  void DomWidget::setElementWidget(const QList<DomWidget *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomWidget16setElementWidgetERK5QListIPS_E(
    DomWidget *self,
    const QList<DomWidget *> *a) {
  self->setElementWidget(*a);
}

//  QList<DomAction *> DomWidget::elementAction() const
extern "C" Q_DECL_EXPORT
QList<DomAction *> *ritual_ZNK9DomWidget13elementActionEv(
    const DomWidget *self) {
  return new QList<DomAction *>(self->elementAction());
}

//  void DomWidget::setElementAction(const QList<DomAction *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomWidget16setElementActionERK5QListIP9DomActionE(
    DomWidget *self,
    const QList<DomAction *> *a) {
  self->setElementAction(*a);
}

//  QList<DomActionGroup *> DomWidget::elementActionGroup() const
extern "C" Q_DECL_EXPORT
QList<DomActionGroup *> *ritual_ZNK9DomWidget18elementActionGroupEv(
    const DomWidget *self) {
  return new QList<DomActionGroup *>(self->elementActionGroup());
}

//  void DomWidget::setElementActionGroup(const QList<DomActionGroup *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomWidget21setElementActionGroupERK5QListIP14DomActionGroupE(
    DomWidget *self,
    const QList<DomActionGroup *> *a) {
  self->setElementActionGroup(*a);
}

//  QList<DomActionRef *> DomWidget::elementAddAction() const
extern "C" Q_DECL_EXPORT
QList<DomActionRef *> *ritual_ZNK9DomWidget16elementAddActionEv(
    const DomWidget *self) {
  return new QList<DomActionRef *>(self->elementAddAction());
}

//  void DomWidget::setElementAddAction(const QList<DomActionRef *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomWidget19setElementAddActionERK5QListIP12DomActionRefE(
    DomWidget *self,
    const QList<DomActionRef *> *a) {
  self->setElementAddAction(*a);
}

//  QStringList DomWidget::elementZOrder() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9DomWidget13elementZOrderEv(
    const DomWidget *self) {
  return new QList<QString>(self->elementZOrder());
}

//  void DomWidget::setElementZOrder(const QStringList &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomWidget16setElementZOrderERK5QListI7QStringE(
    DomWidget *self,
    const QList<QString> *a) {
  self->setElementZOrder(*a);
}

//  QList<DomWidget *>::QList()
extern "C" Q_DECL_EXPORT
QList<DomWidget *> *ritual_list_make_DomWidget_ptr() {
  return new QList<DomWidget *>();
}

//  void QList<DomWidget *>::append(const DomWidget * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_DomWidget_ptr(
    QList<DomWidget *> *self,
    DomWidget *element) {
  self->append(element);
}

//  qsizetype QList<DomWidget *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_DomWidget_ptr(const QList<DomWidget *> *self) {
  return self->size();
}

//  const DomWidget * &QList<DomWidget *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
DomWidget *ritual_list_at_DomWidget_ptr(
    const QList<DomWidget *> *self,
    long long index) {
  return self->at(index);
}

//  QList<DomWidget *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_DomWidget_ptr(QList<DomWidget *> *self) {
  delete self;
}
