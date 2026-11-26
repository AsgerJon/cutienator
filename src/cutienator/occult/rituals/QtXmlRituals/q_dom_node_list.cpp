//  Written by dev_tooling.RitualGenerator from the records of QtXml/qdom.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtXml/qtxmlglobal.h>
#if QT_CONFIG(dom)
#if QT_CONFIG(dom)
#include <QtXml/qdom.h>
#include <QtXml/QDomNodeList>

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

//  QDomNodeList &QDomNodeList::operator=(const QDomNodeList &other)
extern "C" Q_DECL_EXPORT
QDomNodeList *ritual_ZN12QDomNodeListaSERKS_(
    QDomNodeList *self,
    const QDomNodeList *other) {
  return &(self->operator=(*other));
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

//  const_iterator QDomNodeList::begin() const
extern "C" Q_DECL_EXPORT
QDomNodeList::const_iterator *ritual_ZNK12QDomNodeList5beginEv(
    const QDomNodeList *self) {
  return new QDomNodeList::const_iterator(self->begin());
}

//  const_iterator QDomNodeList::end() const
extern "C" Q_DECL_EXPORT
QDomNodeList::const_iterator *ritual_ZNK12QDomNodeList3endEv(
    const QDomNodeList *self) {
  return new QDomNodeList::const_iterator(self->end());
}

//  const_iterator QDomNodeList::cbegin() const
extern "C" Q_DECL_EXPORT
QDomNodeList::const_iterator *ritual_ZNK12QDomNodeList6cbeginEv(
    const QDomNodeList *self) {
  return new QDomNodeList::const_iterator(self->cbegin());
}

//  const_iterator QDomNodeList::cend() const
extern "C" Q_DECL_EXPORT
QDomNodeList::const_iterator *ritual_ZNK12QDomNodeList4cendEv(
    const QDomNodeList *self) {
  return new QDomNodeList::const_iterator(self->cend());
}

//  const_reverse_iterator QDomNodeList::rbegin() const
extern "C" Q_DECL_EXPORT
QDomNodeList::const_reverse_iterator *ritual_ZNK12QDomNodeList6rbeginEv(
    const QDomNodeList *self) {
  return new QDomNodeList::const_reverse_iterator(self->rbegin());
}

//  const_reverse_iterator QDomNodeList::rend() const
extern "C" Q_DECL_EXPORT
QDomNodeList::const_reverse_iterator *ritual_ZNK12QDomNodeList4rendEv(
    const QDomNodeList *self) {
  return new QDomNodeList::const_reverse_iterator(self->rend());
}

//  const_reverse_iterator QDomNodeList::crbegin() const
extern "C" Q_DECL_EXPORT
QDomNodeList::const_reverse_iterator *ritual_ZNK12QDomNodeList7crbeginEv(
    const QDomNodeList *self) {
  return new QDomNodeList::const_reverse_iterator(self->crbegin());
}

//  const_reverse_iterator QDomNodeList::crend() const
extern "C" Q_DECL_EXPORT
QDomNodeList::const_reverse_iterator *ritual_ZNK12QDomNodeList5crendEv(
    const QDomNodeList *self) {
  return new QDomNodeList::const_reverse_iterator(self->crend());
}

//  const_iterator QDomNodeList::constBegin() const
extern "C" Q_DECL_EXPORT
QDomNodeList::const_iterator *ritual_ZNK12QDomNodeList10constBeginEv(
    const QDomNodeList *self) {
  return new QDomNodeList::const_iterator(self->constBegin());
}

//  const_iterator QDomNodeList::constEnd() const
extern "C" Q_DECL_EXPORT
QDomNodeList::const_iterator *ritual_ZNK12QDomNodeList8constEndEv(
    const QDomNodeList *self) {
  return new QDomNodeList::const_iterator(self->constEnd());
}

//  QDomNodeList::QDomNodeList(QDomNodeListPrivate *a0)
extern "C" Q_DECL_EXPORT
QDomNodeList *ritual_ZN12QDomNodeListC1EP19QDomNodeListPrivate(
    QDomNodeListPrivate *a0) {
  return new QDomNodeList(a0);
}

//  a QDomNodeList::const_iterator a ritual of QDomNodeList gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDomNodeList__QDomNodeList_const_iterator(
    QDomNodeList::const_iterator *self) {
  delete self;
}

//  a QDomNodeList::const_reverse_iterator a ritual of QDomNodeList gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDomNodeList__QDomNodeList_const_reverse_iterator(
    QDomNodeList::const_reverse_iterator *self) {
  delete self;
}

#endif  // QT_CONFIG(dom)
#endif  // QT_CONFIG(dom)
