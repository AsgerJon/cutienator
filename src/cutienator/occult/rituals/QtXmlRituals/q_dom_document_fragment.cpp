//  Written by dev_tooling.RitualGenerator from the records of QtXml/qdom.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtXml/qtxmlglobal.h>
#if QT_CONFIG(dom)
#include <QtXml/qdom.h>

//  QDomDocumentFragment::QDomDocumentFragment()
extern "C" Q_DECL_EXPORT
QDomDocumentFragment *ritual_ZN20QDomDocumentFragmentC1Ev() {
  return new QDomDocumentFragment();
}

//  QDomDocumentFragment::QDomDocumentFragment(const QDomDocumentFragment
//      &documentFragment)
extern "C" Q_DECL_EXPORT
QDomDocumentFragment *ritual_ZN20QDomDocumentFragmentC1ERKS_(
    const QDomDocumentFragment *documentFragment) {
  return new QDomDocumentFragment(*documentFragment);
}

//  QDomNode::NodeType QDomDocumentFragment::nodeType() const
extern "C" Q_DECL_EXPORT
QDomNode::NodeType ritual_ZNK20QDomDocumentFragment8nodeTypeEv(
    const QDomDocumentFragment *self) {
  return self->nodeType();
}

//  QDomDocumentFragment::QDomDocumentFragment(QDomDocumentFragmentPrivate
//      *a0)
extern "C" Q_DECL_EXPORT
QDomDocumentFragment *ritual_ZN20QDomDocumentFragmentC1EP27QDomDocumentFragmentPrivate(
    QDomDocumentFragmentPrivate *a0) {
  return new QDomDocumentFragment(a0);
}

//  QDomDocumentFragment::~QDomDocumentFragment()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDomDocumentFragmentD1Ev(QDomDocumentFragment *self) {
  delete self;
}

#endif  // QT_CONFIG(dom)
