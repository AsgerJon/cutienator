//  Written by dev_tooling.RitualGenerator from the records of QtXml/qdom.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtXml/qtxmlglobal.h>
#if QT_CONFIG(dom)
#if QT_CONFIG(dom)
#include <QtXml/qdom.h>

//  QDomCDATASection::QDomCDATASection()
extern "C" Q_DECL_EXPORT
QDomCDATASection *ritual_ZN16QDomCDATASectionC1Ev() {
  return new QDomCDATASection();
}

//  QDomCDATASection::QDomCDATASection(const QDomCDATASection &cdataSection)
extern "C" Q_DECL_EXPORT
QDomCDATASection *ritual_ZN16QDomCDATASectionC1ERKS_(
    const QDomCDATASection *cdataSection) {
  return new QDomCDATASection(*cdataSection);
}

//  QDomNode::NodeType QDomCDATASection::nodeType() const
extern "C" Q_DECL_EXPORT
QDomNode::NodeType ritual_ZNK16QDomCDATASection8nodeTypeEv(
    const QDomCDATASection *self) {
  return self->nodeType();
}

//  QDomCDATASection::QDomCDATASection(QDomCDATASectionPrivate *a0)
extern "C" Q_DECL_EXPORT
QDomCDATASection *ritual_ZN16QDomCDATASectionC1EP23QDomCDATASectionPrivate(
    QDomCDATASectionPrivate *a0) {
  return new QDomCDATASection(a0);
}

//  QDomCDATASection::~QDomCDATASection()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDomCDATASectionD1Ev(QDomCDATASection *self) {
  delete self;
}

#endif  // QT_CONFIG(dom)
#endif  // QT_CONFIG(dom)
