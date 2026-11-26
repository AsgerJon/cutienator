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

//  DomColor::DomColor()
extern "C" Q_DECL_EXPORT
DomColor *ritual_ZN8DomColorC1Ev() {
  return new DomColor();
}

//  DomColor::~DomColor()
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomColorD1Ev(DomColor *self) {
  delete self;
}

//  void DomColor::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomColor4readER16QXmlStreamReader(
    DomColor *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomColor::write(QXmlStreamWriter &writer, const QString &tagName)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK8DomColor5writeER16QXmlStreamWriterRK7QString(
    const DomColor *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  bool DomColor::hasAttributeAlpha() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8DomColor17hasAttributeAlphaEv(const DomColor *self) {
  return self->hasAttributeAlpha();
}

//  int DomColor::attributeAlpha() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8DomColor14attributeAlphaEv(const DomColor *self) {
  return self->attributeAlpha();
}

//  void DomColor::setAttributeAlpha(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomColor17setAttributeAlphaEi(DomColor *self, int a) {
  self->setAttributeAlpha(a);
}

//  void DomColor::clearAttributeAlpha()
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomColor19clearAttributeAlphaEv(DomColor *self) {
  self->clearAttributeAlpha();
}

//  int DomColor::elementRed() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8DomColor10elementRedEv(const DomColor *self) {
  return self->elementRed();
}

//  void DomColor::setElementRed(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomColor13setElementRedEi(DomColor *self, int a) {
  self->setElementRed(a);
}

//  bool DomColor::hasElementRed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8DomColor13hasElementRedEv(const DomColor *self) {
  return self->hasElementRed();
}

//  void DomColor::clearElementRed()
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomColor15clearElementRedEv(DomColor *self) {
  self->clearElementRed();
}

//  int DomColor::elementGreen() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8DomColor12elementGreenEv(const DomColor *self) {
  return self->elementGreen();
}

//  void DomColor::setElementGreen(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomColor15setElementGreenEi(DomColor *self, int a) {
  self->setElementGreen(a);
}

//  bool DomColor::hasElementGreen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8DomColor15hasElementGreenEv(const DomColor *self) {
  return self->hasElementGreen();
}

//  void DomColor::clearElementGreen()
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomColor17clearElementGreenEv(DomColor *self) {
  self->clearElementGreen();
}

//  int DomColor::elementBlue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8DomColor11elementBlueEv(const DomColor *self) {
  return self->elementBlue();
}

//  void DomColor::setElementBlue(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomColor14setElementBlueEi(DomColor *self, int a) {
  self->setElementBlue(a);
}

//  bool DomColor::hasElementBlue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8DomColor14hasElementBlueEv(const DomColor *self) {
  return self->hasElementBlue();
}

//  void DomColor::clearElementBlue()
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomColor16clearElementBlueEv(DomColor *self) {
  self->clearElementBlue();
}

//  QList<DomColor *>::QList()
extern "C" Q_DECL_EXPORT
QList<DomColor *> *ritual_list_make_DomColor_ptr() {
  return new QList<DomColor *>();
}

//  void QList<DomColor *>::append(const DomColor * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_DomColor_ptr(
    QList<DomColor *> *self,
    DomColor *element) {
  self->append(element);
}

//  qsizetype QList<DomColor *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_DomColor_ptr(const QList<DomColor *> *self) {
  return self->size();
}

//  const DomColor * &QList<DomColor *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
DomColor *ritual_list_at_DomColor_ptr(
    const QList<DomColor *> *self,
    long long index) {
  return self->at(index);
}

//  QList<DomColor *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_DomColor_ptr(QList<DomColor *> *self) {
  delete self;
}
