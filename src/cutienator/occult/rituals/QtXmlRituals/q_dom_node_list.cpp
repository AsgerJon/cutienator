//  Written by dev_tooling.RitualGenerator from the records of QtXml/qdom.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtXml/qtxmlglobal.h>
#if QT_CONFIG(dom)
#if QT_CONFIG(dom)
#include <QtXml/qdom.h>

//  QDomNodeList::QDomNodeList()
extern "C" Q_DECL_EXPORT
QDomNodeList *ritual_ZN12QDomNodeListC1Ev() {
  return new QDomNodeList();
}

//  QDomNodeList::QDomNodeList(const QDomNodeList &nodeList)
extern "C" Q_DECL_EXPORT
QDomNodeList *ritual_ZN12QDomNodeListC1ERKS_(const QDomNodeList *nodeList) {
  return new QDomNodeList(*nodeList);
}

//  QDomNodeList::~QDomNodeList()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDomNodeListD1Ev(QDomNodeList *self) {
  delete self;
}

//  QDomNode QDomNodeList::item(int index) const
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZNK12QDomNodeList4itemEi(
    const QDomNodeList *self,
    int index) {
  return new QDomNode(self->item(index));
}

//  QDomNode QDomNodeList::at(int index) const
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZNK12QDomNodeList2atEi(
    const QDomNodeList *self,
    int index) {
  return new QDomNode(self->at(index));
}

//  int QDomNodeList::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QDomNodeList6lengthEv(const QDomNodeList *self) {
  return self->length();
}

//  int QDomNodeList::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QDomNodeList5countEv(const QDomNodeList *self) {
  return self->count();
}

//  int QDomNodeList::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QDomNodeList4sizeEv(const QDomNodeList *self) {
  return self->size();
}

//  bool QDomNodeList::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QDomNodeList7isEmptyEv(const QDomNodeList *self) {
  return self->isEmpty();
}

//  bool operator==(const QDomNodeList &lhs, const QDomNodeList &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK12QDomNodeListS1_(
    const QDomNodeList *lhs,
    const QDomNodeList *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QDomNodeList &lhs, const QDomNodeList &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK12QDomNodeListS1_(
    const QDomNodeList *lhs,
    const QDomNodeList *rhs) {
  return operator!=(*lhs, *rhs);
}

//  int QDomNodeList::noexceptLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QDomNodeList14noexceptLengthEv(const QDomNodeList *self) {
  return self->noexceptLength();
}

//  QDomNodeList::QDomNodeList(QDomNodeListPrivate *a0)
extern "C" Q_DECL_EXPORT
QDomNodeList *ritual_ZN12QDomNodeListC1EP19QDomNodeListPrivate(
    QDomNodeListPrivate *a0) {
  return new QDomNodeList(a0);
}

#endif  // QT_CONFIG(dom)
#endif  // QT_CONFIG(dom)
