//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  DomGradientStop::DomGradientStop()
extern "C" Q_DECL_EXPORT
DomGradientStop *ritual_ZN15DomGradientStopC1Ev() {
  return new DomGradientStop();
}

//  DomGradientStop::~DomGradientStop()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomGradientStopD1Ev(DomGradientStop *self) {
  delete self;
}

//  bool DomGradientStop::hasAttributePosition() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15DomGradientStop20hasAttributePositionEv(
    const DomGradientStop *self) {
  return self->hasAttributePosition();
}

//  double DomGradientStop::attributePosition() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK15DomGradientStop17attributePositionEv(
    const DomGradientStop *self) {
  return self->attributePosition();
}

//  void DomGradientStop::setAttributePosition(double a)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomGradientStop20setAttributePositionEd(
    DomGradientStop *self,
    double a) {
  self->setAttributePosition(a);
}

//  void DomGradientStop::clearAttributePosition()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomGradientStop22clearAttributePositionEv(
    DomGradientStop *self) {
  self->clearAttributePosition();
}

//  DomColor *DomGradientStop::elementColor() const
extern "C" Q_DECL_EXPORT
DomColor *ritual_ZNK15DomGradientStop12elementColorEv(
    const DomGradientStop *self) {
  return self->elementColor();
}

//  DomColor *DomGradientStop::takeElementColor()
extern "C" Q_DECL_EXPORT
DomColor *ritual_ZN15DomGradientStop16takeElementColorEv(
    DomGradientStop *self) {
  return self->takeElementColor();
}

//  void DomGradientStop::setElementColor(DomColor *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomGradientStop15setElementColorEP8DomColor(
    DomGradientStop *self,
    DomColor *a) {
  self->setElementColor(a);
}

//  bool DomGradientStop::hasElementColor() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15DomGradientStop15hasElementColorEv(
    const DomGradientStop *self) {
  return self->hasElementColor();
}

//  void DomGradientStop::clearElementColor()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomGradientStop17clearElementColorEv(DomGradientStop *self) {
  self->clearElementColor();
}

//  QList<DomGradientStop *>::QList()
extern "C" Q_DECL_EXPORT
QList<DomGradientStop *> *ritual_list_make_DomGradientStop_ptr() {
  return new QList<DomGradientStop *>();
}

//  void QList<DomGradientStop *>::append(const DomGradientStop * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_DomGradientStop_ptr(
    QList<DomGradientStop *> *self,
    DomGradientStop *element) {
  self->append(element);
}

//  qsizetype QList<DomGradientStop *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_DomGradientStop_ptr(
    const QList<DomGradientStop *> *self) {
  return self->size();
}

//  const DomGradientStop * &QList<DomGradientStop *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
DomGradientStop *ritual_list_at_DomGradientStop_ptr(
    const QList<DomGradientStop *> *self,
    long long index) {
  return self->at(index);
}

//  QList<DomGradientStop *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_DomGradientStop_ptr(QList<DomGradientStop *> *self) {
  delete self;
}
