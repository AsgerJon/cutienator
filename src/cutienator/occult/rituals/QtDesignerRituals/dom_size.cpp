//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  DomSize::DomSize()
extern "C" Q_DECL_EXPORT
DomSize *ritual_ZN7DomSizeC1Ev() {
  return new DomSize();
}

//  DomSize::~DomSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomSizeD1Ev(DomSize *self) {
  delete self;
}

//  void DomSize::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomSize4readER16QXmlStreamReader(
    DomSize *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomSize::write(QXmlStreamWriter &writer, const QString &tagName)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK7DomSize5writeER16QXmlStreamWriterRK7QString(
    const DomSize *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  int DomSize::elementWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7DomSize12elementWidthEv(const DomSize *self) {
  return self->elementWidth();
}

//  void DomSize::setElementWidth(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomSize15setElementWidthEi(DomSize *self, int a) {
  self->setElementWidth(a);
}

//  bool DomSize::hasElementWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomSize15hasElementWidthEv(const DomSize *self) {
  return self->hasElementWidth();
}

//  void DomSize::clearElementWidth()
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomSize17clearElementWidthEv(DomSize *self) {
  self->clearElementWidth();
}

//  int DomSize::elementHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7DomSize13elementHeightEv(const DomSize *self) {
  return self->elementHeight();
}

//  void DomSize::setElementHeight(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomSize16setElementHeightEi(DomSize *self, int a) {
  self->setElementHeight(a);
}

//  bool DomSize::hasElementHeight() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomSize16hasElementHeightEv(const DomSize *self) {
  return self->hasElementHeight();
}

//  void DomSize::clearElementHeight()
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomSize18clearElementHeightEv(DomSize *self) {
  self->clearElementHeight();
}
