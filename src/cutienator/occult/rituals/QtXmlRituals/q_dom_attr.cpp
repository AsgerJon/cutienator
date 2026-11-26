//  Written by dev_tooling.RitualGenerator from the records of QtXml/qdom.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtXml/qtxmlglobal.h>
#if QT_CONFIG(dom)
#if QT_CONFIG(dom)
#include <QtXml/qdom.h>
#include <QtCore/qstring.h>

//  QDomAttr::QDomAttr()
extern "C" Q_DECL_EXPORT
QDomAttr *ritual_ZN8QDomAttrC1Ev() {
  return new QDomAttr();
}

//  QDomAttr::QDomAttr(const QDomAttr &attr)
extern "C" Q_DECL_EXPORT
QDomAttr *ritual_ZN8QDomAttrC1ERKS_(const QDomAttr *attr) {
  return new QDomAttr(*attr);
}

//  QDomAttr &QDomAttr::operator=(const QDomAttr &other)
extern "C" Q_DECL_EXPORT
QDomAttr *ritual_ZN8QDomAttraSERKS_(QDomAttr *self, const QDomAttr *other) {
  return &(self->operator=(*other));
}

//  QString QDomAttr::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QDomAttr4nameEv(const QDomAttr *self) {
  return new QString(self->name());
}

//  bool QDomAttr::specified() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QDomAttr9specifiedEv(const QDomAttr *self) {
  return self->specified();
}

//  QDomElement QDomAttr::ownerElement() const
extern "C" Q_DECL_EXPORT
QDomElement *ritual_ZNK8QDomAttr12ownerElementEv(const QDomAttr *self) {
  return new QDomElement(self->ownerElement());
}

//  QString QDomAttr::value() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QDomAttr5valueEv(const QDomAttr *self) {
  return new QString(self->value());
}

//  void QDomAttr::setValue(const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QDomAttr8setValueERK7QString(
    QDomAttr *self,
    const QString *value) {
  self->setValue(*value);
}

//  QDomNode::NodeType QDomAttr::nodeType() const
extern "C" Q_DECL_EXPORT
QDomNode::NodeType ritual_ZNK8QDomAttr8nodeTypeEv(const QDomAttr *self) {
  return self->nodeType();
}

//  QDomAttr::QDomAttr(QDomAttrPrivate *a0)
extern "C" Q_DECL_EXPORT
QDomAttr *ritual_ZN8QDomAttrC1EP15QDomAttrPrivate(QDomAttrPrivate *a0) {
  return new QDomAttr(a0);
}

//  QDomAttr::~QDomAttr()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QDomAttrD1Ev(QDomAttr *self) {
  delete self;
}

#endif  // QT_CONFIG(dom)
#endif  // QT_CONFIG(dom)
