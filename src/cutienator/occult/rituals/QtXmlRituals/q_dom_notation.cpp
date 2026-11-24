//  Written by dev_tooling.RitualGenerator from the records of QtXml/qdom.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtXml/qtxmlglobal.h>
#if QT_CONFIG(dom)
#if QT_CONFIG(dom)
#include <QtXml/qdom.h>
#include <QtCore/qstring.h>

//  QDomNotation::QDomNotation()
extern "C" Q_DECL_EXPORT
QDomNotation *ritual_ZN12QDomNotationC1Ev() {
  return new QDomNotation();
}

//  QDomNotation::QDomNotation(const QDomNotation &notation)
extern "C" Q_DECL_EXPORT
QDomNotation *ritual_ZN12QDomNotationC1ERKS_(const QDomNotation *notation) {
  return new QDomNotation(*notation);
}

//  QString QDomNotation::publicId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QDomNotation8publicIdEv(const QDomNotation *self) {
  return new QString(self->publicId());
}

//  QString QDomNotation::systemId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QDomNotation8systemIdEv(const QDomNotation *self) {
  return new QString(self->systemId());
}

//  QDomNode::NodeType QDomNotation::nodeType() const
extern "C" Q_DECL_EXPORT
QDomNode::NodeType ritual_ZNK12QDomNotation8nodeTypeEv(
    const QDomNotation *self) {
  return self->nodeType();
}

//  QDomNotation::QDomNotation(QDomNotationPrivate *a0)
extern "C" Q_DECL_EXPORT
QDomNotation *ritual_ZN12QDomNotationC1EP19QDomNotationPrivate(
    QDomNotationPrivate *a0) {
  return new QDomNotation(a0);
}

//  QDomNotation::~QDomNotation()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDomNotationD1Ev(QDomNotation *self) {
  delete self;
}

#endif  // QT_CONFIG(dom)
#endif  // QT_CONFIG(dom)
