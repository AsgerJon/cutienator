//  Written by dev_tooling.RitualGenerator from the records of QtXml/qdom.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtXml/qtxmlglobal.h>
#if QT_CONFIG(dom)
#if QT_CONFIG(dom)
#include <QtXml/qdom.h>

//  QDomComment::QDomComment()
extern "C" Q_DECL_EXPORT
QDomComment *ritual_ZN11QDomCommentC1Ev() {
  return new QDomComment();
}

//  QDomComment::QDomComment(const QDomComment &comment)
extern "C" Q_DECL_EXPORT
QDomComment *ritual_ZN11QDomCommentC1ERKS_(const QDomComment *comment) {
  return new QDomComment(*comment);
}

//  QDomComment &QDomComment::operator=(const QDomComment &other)
extern "C" Q_DECL_EXPORT
QDomComment *ritual_ZN11QDomCommentaSERKS_(
    QDomComment *self,
    const QDomComment *other) {
  return &(self->operator=(*other));
}

//  QDomNode::NodeType QDomComment::nodeType() const
extern "C" Q_DECL_EXPORT
QDomNode::NodeType ritual_ZNK11QDomComment8nodeTypeEv(
    const QDomComment *self) {
  return self->nodeType();
}

//  QDomComment::QDomComment(QDomCommentPrivate *a0)
extern "C" Q_DECL_EXPORT
QDomComment *ritual_ZN11QDomCommentC1EP18QDomCommentPrivate(
    QDomCommentPrivate *a0) {
  return new QDomComment(a0);
}

//  QDomComment::~QDomComment()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDomCommentD1Ev(QDomComment *self) {
  delete self;
}

#endif  // QT_CONFIG(dom)
#endif  // QT_CONFIG(dom)
