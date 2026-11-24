//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>

//  QRhiVertexInputLayout::QRhiVertexInputLayout()
extern "C" Q_DECL_EXPORT
QRhiVertexInputLayout *ritual_ZN21QRhiVertexInputLayoutC1Ev() {
  return new QRhiVertexInputLayout();
}

//  const QRhiVertexInputBinding *QRhiVertexInputLayout::cbeginBindings()
//      const
extern "C" Q_DECL_EXPORT
const QRhiVertexInputBinding *ritual_ZNK21QRhiVertexInputLayout14cbeginBindingsEv(
    const QRhiVertexInputLayout *self) {
  return self->cbeginBindings();
}

//  const QRhiVertexInputBinding *QRhiVertexInputLayout::cendBindings() const
extern "C" Q_DECL_EXPORT
const QRhiVertexInputBinding *ritual_ZNK21QRhiVertexInputLayout12cendBindingsEv(
    const QRhiVertexInputLayout *self) {
  return self->cendBindings();
}

//  const QRhiVertexInputBinding *QRhiVertexInputLayout::bindingAt(qsizetype
//      index) const
extern "C" Q_DECL_EXPORT
const QRhiVertexInputBinding *ritual_ZNK21QRhiVertexInputLayout9bindingAtEx(
    const QRhiVertexInputLayout *self,
    qsizetype index) {
  return self->bindingAt(index);
}

//  qsizetype QRhiVertexInputLayout::bindingCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK21QRhiVertexInputLayout12bindingCountEv(
    const QRhiVertexInputLayout *self) {
  return self->bindingCount();
}

//  const QRhiVertexInputAttribute *QRhiVertexInputLayout::cbeginAttributes()
//      const
extern "C" Q_DECL_EXPORT
const QRhiVertexInputAttribute *ritual_ZNK21QRhiVertexInputLayout16cbeginAttributesEv(
    const QRhiVertexInputLayout *self) {
  return self->cbeginAttributes();
}

//  const QRhiVertexInputAttribute *QRhiVertexInputLayout::cendAttributes()
//      const
extern "C" Q_DECL_EXPORT
const QRhiVertexInputAttribute *ritual_ZNK21QRhiVertexInputLayout14cendAttributesEv(
    const QRhiVertexInputLayout *self) {
  return self->cendAttributes();
}

//  const QRhiVertexInputAttribute
//      *QRhiVertexInputLayout::attributeAt(qsizetype index) const
extern "C" Q_DECL_EXPORT
const QRhiVertexInputAttribute *ritual_ZNK21QRhiVertexInputLayout11attributeAtEx(
    const QRhiVertexInputLayout *self,
    qsizetype index) {
  return self->attributeAt(index);
}

//  qsizetype QRhiVertexInputLayout::attributeCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK21QRhiVertexInputLayout14attributeCountEv(
    const QRhiVertexInputLayout *self) {
  return self->attributeCount();
}

//  bool operator==(const QRhiVertexInputLayout &a, const
//      QRhiVertexInputLayout &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK21QRhiVertexInputLayoutS1_(
    const QRhiVertexInputLayout *a,
    const QRhiVertexInputLayout *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QRhiVertexInputLayout &a, const
//      QRhiVertexInputLayout &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK21QRhiVertexInputLayoutS1_(
    const QRhiVertexInputLayout *a,
    const QRhiVertexInputLayout *b) {
  return operator!=(*a, *b);
}

//  QDebug operator<<(QDebug a0, const QRhiVertexInputLayout &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK21QRhiVertexInputLayout(
    const QDebug *a0,
    const QRhiVertexInputLayout *a1) {
  return new QDebug(operator<<(*a0, *a1));
}

//  QRhiVertexInputLayout::~QRhiVertexInputLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRhiVertexInputLayoutD1Ev(QRhiVertexInputLayout *self) {
  delete self;
}
