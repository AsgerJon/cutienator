//  Written by dev_tooling.RitualGenerator from the records of QtXml/qdom.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtXml/qtxmlglobal.h>
#if QT_CONFIG(dom)
#if QT_CONFIG(dom)
#include <QtXml/qdom.h>

//  QDomText::QDomText()
extern "C" Q_DECL_EXPORT
QDomText *ritual_ZN8QDomTextC1Ev() {
  return new QDomText();
}

//  QDomText::QDomText(const QDomText &text)
extern "C" Q_DECL_EXPORT
QDomText *ritual_ZN8QDomTextC1ERKS_(const QDomText *text) {
  return new QDomText(*text);
}

//  QDomText &QDomText::operator=(const QDomText &other)
extern "C" Q_DECL_EXPORT
QDomText *ritual_ZN8QDomTextaSERKS_(QDomText *self, const QDomText *other) {
  return &(self->operator=(*other));
}

//  QDomText QDomText::splitText(int offset)
extern "C" Q_DECL_EXPORT
QDomText *ritual_ZN8QDomText9splitTextEi(QDomText *self, int offset) {
  return new QDomText(self->splitText(offset));
}

//  QDomNode::NodeType QDomText::nodeType() const
extern "C" Q_DECL_EXPORT
QDomNode::NodeType ritual_ZNK8QDomText8nodeTypeEv(const QDomText *self) {
  return self->nodeType();
}

//  QDomText::QDomText(QDomTextPrivate *a0)
extern "C" Q_DECL_EXPORT
QDomText *ritual_ZN8QDomTextC1EP15QDomTextPrivate(QDomTextPrivate *a0) {
  return new QDomText(a0);
}

//  QDomText::~QDomText()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QDomTextD1Ev(QDomText *self) {
  delete self;
}

#endif  // QT_CONFIG(dom)
#endif  // QT_CONFIG(dom)
