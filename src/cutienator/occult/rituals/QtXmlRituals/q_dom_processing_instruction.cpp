//  Written by dev_tooling.RitualGenerator from the records of QtXml/qdom.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtXml/qtxmlglobal.h>
#if QT_CONFIG(dom)
#if QT_CONFIG(dom)
#include <QtXml/qdom.h>
#include <QtCore/qstring.h>

//  QDomProcessingInstruction::QDomProcessingInstruction()
extern "C" Q_DECL_EXPORT
QDomProcessingInstruction *ritual_ZN25QDomProcessingInstructionC1Ev() {
  return new QDomProcessingInstruction();
}

//  QDomProcessingInstruction::QDomProcessingInstruction(const
//      QDomProcessingInstruction &processingInstruction)
extern "C" Q_DECL_EXPORT
QDomProcessingInstruction *ritual_ZN25QDomProcessingInstructionC1ERKS_(
    const QDomProcessingInstruction *processingInstruction) {
  return new QDomProcessingInstruction(*processingInstruction);
}

//  QString QDomProcessingInstruction::target() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QDomProcessingInstruction6targetEv(
    const QDomProcessingInstruction *self) {
  return new QString(self->target());
}

//  QString QDomProcessingInstruction::data() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QDomProcessingInstruction4dataEv(
    const QDomProcessingInstruction *self) {
  return new QString(self->data());
}

//  void QDomProcessingInstruction::setData(const QString &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDomProcessingInstruction7setDataERK7QString(
    QDomProcessingInstruction *self,
    const QString *data) {
  self->setData(*data);
}

//  QDomNode::NodeType QDomProcessingInstruction::nodeType() const
extern "C" Q_DECL_EXPORT
QDomNode::NodeType ritual_ZNK25QDomProcessingInstruction8nodeTypeEv(
    const QDomProcessingInstruction *self) {
  return self->nodeType();
}

//  QDomProcessingInstruction::QDomProcessingInstruction(QDomProcessingInstru
//      ctionPrivate *a0)
extern "C" Q_DECL_EXPORT
QDomProcessingInstruction *ritual_ZN25QDomProcessingInstructionC1EP32QDomProcessingInstructionPrivate(
    QDomProcessingInstructionPrivate *a0) {
  return new QDomProcessingInstruction(a0);
}

//  QDomProcessingInstruction::~QDomProcessingInstruction()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDomProcessingInstructionD1Ev(
    QDomProcessingInstruction *self) {
  delete self;
}

#endif  // QT_CONFIG(dom)
#endif  // QT_CONFIG(dom)
