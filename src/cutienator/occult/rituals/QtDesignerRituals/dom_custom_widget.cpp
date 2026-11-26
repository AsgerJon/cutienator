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

//  DomCustomWidget::DomCustomWidget()
extern "C" Q_DECL_EXPORT
DomCustomWidget *ritual_ZN15DomCustomWidgetC1Ev() {
  return new DomCustomWidget();
}

//  DomCustomWidget::~DomCustomWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomCustomWidgetD1Ev(DomCustomWidget *self) {
  delete self;
}

//  void DomCustomWidget::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomCustomWidget4readER16QXmlStreamReader(
    DomCustomWidget *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomCustomWidget::write(QXmlStreamWriter &writer, const QString
//      &tagName) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15DomCustomWidget5writeER16QXmlStreamWriterRK7QString(
    const DomCustomWidget *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  QString DomCustomWidget::elementClass() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15DomCustomWidget12elementClassEv(
    const DomCustomWidget *self) {
  return new QString(self->elementClass());
}

//  void DomCustomWidget::setElementClass(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomCustomWidget15setElementClassERK7QString(
    DomCustomWidget *self,
    const QString *a) {
  self->setElementClass(*a);
}

//  bool DomCustomWidget::hasElementClass() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15DomCustomWidget15hasElementClassEv(
    const DomCustomWidget *self) {
  return self->hasElementClass();
}

//  void DomCustomWidget::clearElementClass()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomCustomWidget17clearElementClassEv(DomCustomWidget *self) {
  self->clearElementClass();
}

//  QString DomCustomWidget::elementExtends() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15DomCustomWidget14elementExtendsEv(
    const DomCustomWidget *self) {
  return new QString(self->elementExtends());
}

//  void DomCustomWidget::setElementExtends(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomCustomWidget17setElementExtendsERK7QString(
    DomCustomWidget *self,
    const QString *a) {
  self->setElementExtends(*a);
}

//  bool DomCustomWidget::hasElementExtends() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15DomCustomWidget17hasElementExtendsEv(
    const DomCustomWidget *self) {
  return self->hasElementExtends();
}

//  void DomCustomWidget::clearElementExtends()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomCustomWidget19clearElementExtendsEv(
    DomCustomWidget *self) {
  self->clearElementExtends();
}

//  DomHeader *DomCustomWidget::elementHeader() const
extern "C" Q_DECL_EXPORT
DomHeader *ritual_ZNK15DomCustomWidget13elementHeaderEv(
    const DomCustomWidget *self) {
  return self->elementHeader();
}

//  DomHeader *DomCustomWidget::takeElementHeader()
extern "C" Q_DECL_EXPORT
DomHeader *ritual_ZN15DomCustomWidget17takeElementHeaderEv(
    DomCustomWidget *self) {
  return self->takeElementHeader();
}

//  void DomCustomWidget::setElementHeader(DomHeader *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomCustomWidget16setElementHeaderEP9DomHeader(
    DomCustomWidget *self,
    DomHeader *a) {
  self->setElementHeader(a);
}

//  bool DomCustomWidget::hasElementHeader() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15DomCustomWidget16hasElementHeaderEv(
    const DomCustomWidget *self) {
  return self->hasElementHeader();
}

//  void DomCustomWidget::clearElementHeader()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomCustomWidget18clearElementHeaderEv(
    DomCustomWidget *self) {
  self->clearElementHeader();
}

//  DomSize *DomCustomWidget::elementSizeHint() const
extern "C" Q_DECL_EXPORT
DomSize *ritual_ZNK15DomCustomWidget15elementSizeHintEv(
    const DomCustomWidget *self) {
  return self->elementSizeHint();
}

//  DomSize *DomCustomWidget::takeElementSizeHint()
extern "C" Q_DECL_EXPORT
DomSize *ritual_ZN15DomCustomWidget19takeElementSizeHintEv(
    DomCustomWidget *self) {
  return self->takeElementSizeHint();
}

//  void DomCustomWidget::setElementSizeHint(DomSize *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomCustomWidget18setElementSizeHintEP7DomSize(
    DomCustomWidget *self,
    DomSize *a) {
  self->setElementSizeHint(a);
}

//  bool DomCustomWidget::hasElementSizeHint() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15DomCustomWidget18hasElementSizeHintEv(
    const DomCustomWidget *self) {
  return self->hasElementSizeHint();
}

//  void DomCustomWidget::clearElementSizeHint()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomCustomWidget20clearElementSizeHintEv(
    DomCustomWidget *self) {
  self->clearElementSizeHint();
}

//  QString DomCustomWidget::elementAddPageMethod() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15DomCustomWidget20elementAddPageMethodEv(
    const DomCustomWidget *self) {
  return new QString(self->elementAddPageMethod());
}

//  void DomCustomWidget::setElementAddPageMethod(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomCustomWidget23setElementAddPageMethodERK7QString(
    DomCustomWidget *self,
    const QString *a) {
  self->setElementAddPageMethod(*a);
}

//  bool DomCustomWidget::hasElementAddPageMethod() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15DomCustomWidget23hasElementAddPageMethodEv(
    const DomCustomWidget *self) {
  return self->hasElementAddPageMethod();
}

//  void DomCustomWidget::clearElementAddPageMethod()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomCustomWidget25clearElementAddPageMethodEv(
    DomCustomWidget *self) {
  self->clearElementAddPageMethod();
}

//  int DomCustomWidget::elementContainer() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15DomCustomWidget16elementContainerEv(
    const DomCustomWidget *self) {
  return self->elementContainer();
}

//  void DomCustomWidget::setElementContainer(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomCustomWidget19setElementContainerEi(
    DomCustomWidget *self,
    int a) {
  self->setElementContainer(a);
}

//  bool DomCustomWidget::hasElementContainer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15DomCustomWidget19hasElementContainerEv(
    const DomCustomWidget *self) {
  return self->hasElementContainer();
}

//  void DomCustomWidget::clearElementContainer()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomCustomWidget21clearElementContainerEv(
    DomCustomWidget *self) {
  self->clearElementContainer();
}

//  QString DomCustomWidget::elementPixmap() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15DomCustomWidget13elementPixmapEv(
    const DomCustomWidget *self) {
  return new QString(self->elementPixmap());
}

//  void DomCustomWidget::setElementPixmap(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomCustomWidget16setElementPixmapERK7QString(
    DomCustomWidget *self,
    const QString *a) {
  self->setElementPixmap(*a);
}

//  bool DomCustomWidget::hasElementPixmap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15DomCustomWidget16hasElementPixmapEv(
    const DomCustomWidget *self) {
  return self->hasElementPixmap();
}

//  void DomCustomWidget::clearElementPixmap()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomCustomWidget18clearElementPixmapEv(
    DomCustomWidget *self) {
  self->clearElementPixmap();
}

//  DomSlots *DomCustomWidget::elementSlots() const
extern "C" Q_DECL_EXPORT
DomSlots *ritual_ZNK15DomCustomWidget12elementSlotsEv(
    const DomCustomWidget *self) {
  return self->elementSlots();
}

//  DomSlots *DomCustomWidget::takeElementSlots()
extern "C" Q_DECL_EXPORT
DomSlots *ritual_ZN15DomCustomWidget16takeElementSlotsEv(
    DomCustomWidget *self) {
  return self->takeElementSlots();
}

//  void DomCustomWidget::setElementSlots(DomSlots *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomCustomWidget15setElementSlotsEP8DomSlots(
    DomCustomWidget *self,
    DomSlots *a) {
  self->setElementSlots(a);
}

//  bool DomCustomWidget::hasElementSlots() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15DomCustomWidget15hasElementSlotsEv(
    const DomCustomWidget *self) {
  return self->hasElementSlots();
}

//  void DomCustomWidget::clearElementSlots()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomCustomWidget17clearElementSlotsEv(DomCustomWidget *self) {
  self->clearElementSlots();
}

//  DomPropertySpecifications
//      *DomCustomWidget::elementPropertyspecifications() const
extern "C" Q_DECL_EXPORT
DomPropertySpecifications *ritual_ZNK15DomCustomWidget29elementPropertyspecificationsEv(
    const DomCustomWidget *self) {
  return self->elementPropertyspecifications();
}

//  DomPropertySpecifications
//      *DomCustomWidget::takeElementPropertyspecifications()
extern "C" Q_DECL_EXPORT
DomPropertySpecifications *ritual_ZN15DomCustomWidget33takeElementPropertyspecificationsEv(
    DomCustomWidget *self) {
  return self->takeElementPropertyspecifications();
}

//  void DomCustomWidget::setElementPropertyspecifications(DomPropertySpecifi
//      cations *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomCustomWidget32setElementPropertyspecificationsEP25DomPropertySpecifications(
    DomCustomWidget *self,
    DomPropertySpecifications *a) {
  self->setElementPropertyspecifications(a);
}

//  bool DomCustomWidget::hasElementPropertyspecifications() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15DomCustomWidget32hasElementPropertyspecificationsEv(
    const DomCustomWidget *self) {
  return self->hasElementPropertyspecifications();
}

//  void DomCustomWidget::clearElementPropertyspecifications()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomCustomWidget34clearElementPropertyspecificationsEv(
    DomCustomWidget *self) {
  self->clearElementPropertyspecifications();
}

//  QList<DomCustomWidget *>::QList()
extern "C" Q_DECL_EXPORT
QList<DomCustomWidget *> *ritual_list_make_DomCustomWidget_ptr() {
  return new QList<DomCustomWidget *>();
}

//  void QList<DomCustomWidget *>::append(const DomCustomWidget * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_DomCustomWidget_ptr(
    QList<DomCustomWidget *> *self,
    DomCustomWidget *element) {
  self->append(element);
}

//  qsizetype QList<DomCustomWidget *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_DomCustomWidget_ptr(
    const QList<DomCustomWidget *> *self) {
  return self->size();
}

//  const DomCustomWidget * &QList<DomCustomWidget *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
DomCustomWidget *ritual_list_at_DomCustomWidget_ptr(
    const QList<DomCustomWidget *> *self,
    long long index) {
  return self->at(index);
}

//  QList<DomCustomWidget *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_DomCustomWidget_ptr(QList<DomCustomWidget *> *self) {
  delete self;
}
