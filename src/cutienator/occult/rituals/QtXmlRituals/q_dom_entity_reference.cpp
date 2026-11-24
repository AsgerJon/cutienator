//  Written by dev_tooling.RitualGenerator from the records of QtXml/qdom.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtXml/qtxmlglobal.h>
#if QT_CONFIG(dom)
#if QT_CONFIG(dom)
#include <QtXml/qdom.h>

//  QDomEntityReference::QDomEntityReference()
extern "C" Q_DECL_EXPORT
QDomEntityReference *ritual_ZN19QDomEntityReferenceC1Ev() {
  return new QDomEntityReference();
}

//  QDomEntityReference::QDomEntityReference(const QDomEntityReference
//      &entityReference)
extern "C" Q_DECL_EXPORT
QDomEntityReference *ritual_ZN19QDomEntityReferenceC1ERKS_(
    const QDomEntityReference *entityReference) {
  return new QDomEntityReference(*entityReference);
}

//  QDomNode::NodeType QDomEntityReference::nodeType() const
extern "C" Q_DECL_EXPORT
QDomNode::NodeType ritual_ZNK19QDomEntityReference8nodeTypeEv(
    const QDomEntityReference *self) {
  return self->nodeType();
}

//  QDomEntityReference::QDomEntityReference(QDomEntityReferencePrivate *a0)
extern "C" Q_DECL_EXPORT
QDomEntityReference *ritual_ZN19QDomEntityReferenceC1EP26QDomEntityReferencePrivate(
    QDomEntityReferencePrivate *a0) {
  return new QDomEntityReference(a0);
}

//  QDomEntityReference::~QDomEntityReference()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDomEntityReferenceD1Ev(QDomEntityReference *self) {
  delete self;
}

#endif  // QT_CONFIG(dom)
#endif  // QT_CONFIG(dom)
